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

function buildSystemPrompt(knowledgeBase) {
  return `Sen "${knowledgeBase.business.name}" do'koni uchun ishlaydigan AI sotuv yordamchisisan.
Vazifang: mijozlarning savollariga aniq va qisqa javob berish, mahsulot tanlashda yordam berish va buyurtma qabul qilish.

DO'KON MA'LUMOTLARI:
${JSON.stringify(knowledgeBase.business, null, 2)}

KO'P SO'RALADIGAN SAVOLLAR:
${knowledgeBase.faq.map((f) => `- ${f.question}\n  ${f.answer}`).join("\n")}

MAHSULOTLAR:
${JSON.stringify(knowledgeBase.products, null, 2)}

QOIDALAR:
1. Faqat yuqoridagi ma'lumotlarga asoslanib javob ber. Bilmagan narsangni to'qib chiqarma — "aniqlashtirib beraman" deb ayt.
2. Mijoz mahsulot tanlasa — rang, o'lcham, miqdorni so'ra.
3. Yetkazib berish yoki do'kondan olib ketishni so'ra, telefon raqamini so'ra.
4. Hammasi aniq bo'lgach, buyurtmani QISQA qilib qayta o'qib ber va "to'g'rimi?" deb tasdiqlat.
5. Mijoz "ha", "tasdiqlayman" kabi javob berganidan KEYINGINA submit_order tool'ni chaqir. Undan oldin chaqirma.
6. Har doim o'zbek tilida, do'stona va qisqa yoz. Ortiqcha uzun javob yozma.`;
}

async function handleMessage({ knowledgeBase, history, userMessage }) {
  const messages = [...history, { role: "user", content: userMessage }];

  const response = await anthropic.messages.create({
    model: MODEL,
    max_tokens: 1024,
    system: buildSystemPrompt(knowledgeBase),
    tools: [SUBMIT_ORDER_TOOL],
    messages,
  });

  let replyText = "";
  let orderResult = null;

  for (const block of response.content) {
    if (block.type === "text") {
      replyText += block.text;
    } else if (block.type === "tool_use" && block.name === "submit_order") {
      const order = {
        ...block.input,
        business: knowledgeBase.business.name,
        timestamp: new Date().toISOString(),
      };
      orderResult = await logOrder(order);

      const toolResultMessages = [
        ...messages,
        { role: "assistant", content: response.content },
        {
          role: "user",
          content: [
            {
              type: "tool_result",
              tool_use_id: block.id,
              content: "Buyurtma muvaffaqiyatli qabul qilindi va yozib qo'yildi.",
            },
          ],
        },
      ];

      const followUp = await anthropic.messages.create({
        model: MODEL,
        max_tokens: 512,
        system: buildSystemPrompt(knowledgeBase),
        tools: [SUBMIT_ORDER_TOOL],
        messages: toolResultMessages,
      });

      replyText = followUp.content
        .filter((b) => b.type === "text")
        .map((b) => b.text)
        .join("\n");

      messages.push({ role: "assistant", content: response.content });
      messages.push(toolResultMessages[toolResultMessages.length - 1]);
      messages.push({ role: "assistant", content: followUp.content });

      return { replyText, order, orderResult, updatedHistory: messages };
    }
  }

  messages.push({ role: "assistant", content: response.content });
  return { replyText, order: null, orderResult: null, updatedHistory: messages };
}

module.exports = { handleMessage };
