require("dotenv").config();
const fs = require("fs");
const path = require("path");
const TelegramBot = require("node-telegram-bot-api");
const { handleMessage } = require("./engine/botEngine");

const TOKEN = process.env.TELEGRAM_BOT_TOKEN;
if (!TOKEN) {
  console.error("Xato: TELEGRAM_BOT_TOKEN .env faylida topilmadi. README.md ga qarang.");
  process.exit(1);
}
if (!process.env.ANTHROPIC_API_KEY) {
  console.error("Xato: ANTHROPIC_API_KEY .env faylida topilmadi. README.md ga qarang.");
  process.exit(1);
}

const OWNER_CHAT_ID = process.env.OWNER_CHAT_ID ? String(process.env.OWNER_CHAT_ID) : null;

const knowledgePath = process.env.KNOWLEDGE_FILE
  ? path.resolve(process.env.KNOWLEDGE_FILE)
  : path.join(__dirname, "data", "knowledge.json");
let knowledgeBase = JSON.parse(fs.readFileSync(knowledgePath, "utf8"));

function saveKnowledgeBase() {
  fs.writeFileSync(knowledgePath, JSON.stringify(knowledgeBase, null, 2));
}

function findProductByCaption(caption) {
  if (!caption) return null;
  const normalized = caption.trim().toLowerCase();
  return (
    knowledgeBase.products.find((p) => p.id.toLowerCase() === normalized) ||
    knowledgeBase.products.find((p) => p.name.toLowerCase() === normalized) ||
    knowledgeBase.products.find((p) => p.name.toLowerCase().includes(normalized)) ||
    null
  );
}

const bot = new TelegramBot(TOKEN, { polling: true });

// Har bir mijoz (chat) uchun suhbat tarixi xotirada saqlanadi.
// Eslatma: server qayta ishga tushsa tarix o'chadi. Katta miqyos uchun
// buni Redis/DB ga ko'chirish kerak bo'ladi — demo va kichik do'kon uchun yetarli.
const conversations = new Map();

console.log(`Bot ishga tushdi: ${knowledgeBase.business.name}`);
if (OWNER_CHAT_ID) {
  console.log(`Do'kon egasi rejimi yoqilgan (OWNER_CHAT_ID: ${OWNER_CHAT_ID}) - rasm/video biriktirish mumkin.`);
} else {
  console.log("Eslatma: OWNER_CHAT_ID sozlanmagan - mahsulotlarga rasm/video biriktirish o'chirilgan.");
}

async function downloadTelegramFileAsBase64(fileId) {
  const fileUrl = await bot.getFileLink(fileId);
  const response = await fetch(fileUrl);
  const arrayBuffer = await response.arrayBuffer();
  return Buffer.from(arrayBuffer).toString("base64");
}

async function sendProductMedia(chatId, mediaToSend) {
  for (const item of mediaToSend) {
    for (const photoFileId of item.photos) {
      await bot.sendPhoto(chatId, photoFileId, { caption: item.productName });
    }
    for (const videoFileId of item.videos) {
      await bot.sendVideo(chatId, videoFileId, { caption: item.productName });
    }
  }
}

bot.on("message", async (msg) => {
  const chatId = msg.chat.id;
  const isOwner = OWNER_CHAT_ID && String(chatId) === OWNER_CHAT_ID;

  // Do'kon egasi rasm/video yuborsa va caption'da mahsulot nomi/ID bo'lsa -
  // o'sha mediani mahsulotga biriktiramiz (mijozlarga ko'rsatish uchun).
  if (isOwner && (msg.photo || msg.video)) {
    const product = findProductByCaption(msg.caption);
    if (!product) {
      await bot.sendMessage(
        chatId,
        "Mahsulot topilmadi. Rasm/video yuborganda caption (izoh) sifatida mahsulot nomini yoki ID'sini yozing, masalan: \"Kuzgi Dvoyka\"."
      );
      return;
    }

    product.media = product.media || { photos: [], videos: [] };

    if (msg.photo) {
      const largest = msg.photo[msg.photo.length - 1];
      product.media.photos.push(largest.file_id);
    }
    if (msg.video) {
      product.media.videos.push(msg.video.file_id);
    }

    saveKnowledgeBase();
    await bot.sendMessage(chatId, `Saqlandi: "${product.name}" mahsulotiga rasm/video biriktirildi.`);
    return;
  }

  const text = msg.text;
  const hasCustomerPhoto = !isOwner && msg.photo && msg.photo.length > 0;

  if (!text && !hasCustomerPhoto) return;

  if (text === "/start") {
    conversations.delete(chatId);
    await bot.sendMessage(
      chatId,
      `Salom! Men ${knowledgeBase.business.name} yordamchisiman. Mahsulotlar, narxlar yoki yetkazib berish haqida savol bering, yoki to'g'ridan-to'g'ri buyurtma bering.`
    );
    return;
  }

  const history = conversations.get(chatId) || [];

  try {
    await bot.sendChatAction(chatId, "typing");

    let imageBase64 = null;
    if (hasCustomerPhoto) {
      const largest = msg.photo[msg.photo.length - 1];
      imageBase64 = await downloadTelegramFileAsBase64(largest.file_id);
    }

    const { replyText, order, mediaToSend, updatedHistory } = await handleMessage({
      knowledgeBase,
      history,
      userMessage: text || msg.caption || "",
      imageBase64,
      imageMediaType: "image/jpeg",
    });

    conversations.set(chatId, updatedHistory);

    if (replyText) {
      await bot.sendMessage(chatId, replyText);
    }

    if (mediaToSend && mediaToSend.length > 0) {
      await sendProductMedia(chatId, mediaToSend);
    }

    if (order) {
      console.log("Yangi buyurtma:", JSON.stringify(order, null, 2));
      const staffChatId = process.env.STAFF_NOTIFY_CHAT_ID;
      if (staffChatId) {
        await bot.sendMessage(
          staffChatId,
          `🆕 Yangi buyurtma!\n${JSON.stringify(order, null, 2)}`
        );
      }
    }
  } catch (err) {
    console.error("Xabarni qayta ishlashda xato:", err);
    await bot.sendMessage(
      chatId,
      "Kechirasiz, texnik nosozlik yuz berdi. Birozdan so'ng qayta urinib ko'ring."
    );
  }
});

bot.on("polling_error", (err) => console.error("Polling xatosi:", err.message));
