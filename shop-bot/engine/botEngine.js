const Anthropic = require("@anthropic-ai/sdk");
const { logOrder } = require("./sheetsLogger");

const anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });
const MODEL = process.env.ANTHROPIC_MODEL || "claude-haiku-4-5-20251001";

const SUBMIT_ORDER_TOOL = {
  name: "submit_order",
  description:
    "Mijoz buyurtmasini tasdiqlagandan keyin chaqiriladi. Faqat mijoz aniq 'ha, tasdiqlayman' yoki shunga o'xshash tasdiq bergandan keyingina chaqir.",
  input_schema: {
    type: "object",
    properties: {
      items: {
        type: "array",
        description: "Buyurtma qilingan mahsulotlar ro'yxati",
        items: {
          type: "object",
          properties: {
            product: { type: "string" },
            quantity: { type: "integer" },
            color: { type: "string" },
            size: { type: "string" },
          },
          required: ["product", "quantity"],
        },
      },
      deliveryOrPickup: {
        type: "string",
        description: "Yetkazib berish manzili yoki 'do'kondan olib ketish'",
      },
      customerPhone: { type: "string" },
      customerName: { type: "string" },
      estimatedTotal: { type: "string" },
    },
    required: ["items", "deliveryOrPickup", "customerPhone"],
  },
};

const SHOW_MEDIA_TOOL = {
  name: "show_product_media",
  description:
    "Mijoz mahsulotning haqiqiy rasmi yoki videosini ko'rishni so'raganda chaqiriladi (masalan: 'rasmini yuboring', 'video bormi', 'real o'zini ko'rsating', 'o'zini ko'rsam bo'ladimi'). productId sifatida MAHSULOTLAR ro'yxatidagi mos keluvchi 'id' maydonini ber.",
  input_schema: {
    type: "object",
    properties: {
      productId: { type: "string", description: "products ro'yxatidagi mos mahsulotning 'id' qiymati" },
    },
    required: ["productId"],
  },
};

const TOOLS = [SUBMIT_ORDER_TOOL, SHOW_MEDIA_TOOL];

function buildSystemPrompt(knowledgeBase) {
  return `Sen "${knowledgeBase.business.name}" do'koni uchun ishlaydigan AI sotuv yordamchisisan.
Vazifang: mijozlarning savollariga aniq va qisqa javob berish, mahsulot tanlashda yordam berish va buyurtma qabul qilish.

DO'KON MA'LUMOTLARI:
${JSON.stringify(knowledgeBase.business, null, 2)}

KO'P SO'RALADIGAN SAVOLLAR:
${knowledgeBase.faq.map((f) => `- ${f.question}\n  ${f.answer}`).join("\n")}

MAHSULOTLAR (har birining "media" maydonida haqiqiy rasm/video borligi ko'rsatilgan):
${JSON.stringify(knowledgeBase.products, null, 2)}

QOIDALAR:
1. Faqat yuqoridagi ma'lumotlarga asoslanib javob ber. Bilmagan narsangni to'qib chiqarma — "aniqlashtirib beraman" deb ayt.
2. Mijoz mahsulot tanlasa — rang, o'lcham, miqdorni so'ra.
3. Yetkazib berish yoki do'kondan olib ketishni so'ra, telefon raqamini so'ra.
4. Hammasi aniq bo'lgach, buyurtmani QISQA qilib qayta o'qib ber va "to'g'rimi?" deb tasdiqlat.
5. Mijoz "ha", "tasdiqlayman" kabi javob berganidan KEYINGINA submit_order tool'ni chaqir. Undan oldin chaqirma.
6. Mijoz mahsulotning haqiqiy rasmi/videosini so'rasa ("real ko'rsating", "rasmini yuboring", "video bormi" va h.k.) — show_product_media tool'ni chaqir. Agar o'sha mahsulotning media.photos va media.videos ikkalasi ham bo'sh bo'lsa, tool'ni chaqirmasdan, "hozircha rasm/video yuklanmagan, tez orada qo'shamiz" deb ayt.
7. Har doim o'zbek tilida, do'stona va qisqa yoz. Ortiqcha uzun javob yozma.`;
}

function buildUserContent({ userMessage, imageBase64, imageMediaType }) {
  if (!imageBase64) {
    return userMessage;
  }
  const content = [
    {
      type: "image",
      source: { type: "base64", media_type: imageMediaType || "image/jpeg", data: imageBase64 },
    },
  ];
  content.push({ type: "text", text: userMessage || "Mijoz rasm yubordi. Rasmni ko'rib, mos javob bering." });
  return content;
}

async function handleMessage({ knowledgeBase, history, userMessage, imageBase64, imageMediaType }) {
  const messages = [
    ...history,
    { role: "user", content: buildUserContent({ userMessage, imageBase64, imageMediaType }) },
  ];

  const response = await anthropic.messages.create({
    model: MODEL,
    max_tokens: 1024,
    system: buildSystemPrompt(knowledgeBase),
    tools: TOOLS,
    messages,
  });

  const toolUseBlocks = response.content.filter((b) => b.type === "tool_use");

  if (toolUseBlocks.length === 0) {
    const replyText = response.content
      .filter((b) => b.type === "text")
      .map((b) => b.text)
      .join("\n");
    messages.push({ role: "assistant", content: response.content });
    return { replyText, order: null, mediaToSend: [], updatedHistory: messages };
  }

  let order = null;
  const mediaToSend = [];
  const toolResults = [];

  for (const block of toolUseBlocks) {
    if (block.name === "submit_order") {
      order = {
        ...block.input,
        business: knowledgeBase.business.name,
        timestamp: new Date().toISOString(),
      };
      await logOrder(order);
      toolResults.push({
        type: "tool_result",
        tool_use_id: block.id,
        content: "Buyurtma muvaffaqiyatli qabul qilindi va yozib qo'yildi.",
      });
    } else if (block.name === "show_product_media") {
      const product = knowledgeBase.products.find((p) => p.id === block.input.productId);
      const media = product && product.media ? product.media : null;
      const hasMedia = media && ((media.photos && media.photos.length) || (media.videos && media.videos.length));

      if (hasMedia) {
        mediaToSend.push({
          productId: block.input.productId,
          productName: product.name,
          photos: media.photos || [],
          videos: media.videos || [],
        });
        toolResults.push({
          type: "tool_result",
          tool_use_id: block.id,
          content: "Rasm/video mijozga yuborildi.",
        });
      } else {
        toolResults.push({
          type: "tool_result",
          tool_use_id: block.id,
          content: "Bu mahsulot uchun hali rasm/video yuklanmagan.",
        });
      }
    }
  }

  const messagesWithToolResult = [
    ...messages,
    { role: "assistant", content: response.content },
    { role: "user", content: toolResults },
  ];

  const followUp = await anthropic.messages.create({
    model: MODEL,
    max_tokens: 512,
    system: buildSystemPrompt(knowledgeBase),
    tools: TOOLS,
    messages: messagesWithToolResult,
  });

  const replyText = followUp.content
    .filter((b) => b.type === "text")
    .map((b) => b.text)
    .join("\n");

  const updatedHistory = [...messagesWithToolResult, { role: "assistant", content: followUp.content }];

  return { replyText, order, mediaToSend, updatedHistory };
}

module.exports = { handleMessage };
