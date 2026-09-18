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

const knowledgePath = process.env.KNOWLEDGE_FILE
  ? path.resolve(process.env.KNOWLEDGE_FILE)
  : path.join(__dirname, "data", "knowledge.json");
const knowledgeBase = JSON.parse(fs.readFileSync(knowledgePath, "utf8"));

const bot = new TelegramBot(TOKEN, { polling: true });

// Har bir mijoz (chat) uchun suhbat tarixi xotirada saqlanadi.
// Eslatma: server qayta ishga tushsa tarix o'chadi. Katta miqyos uchun
// buni Redis/DB ga ko'chirish kerak bo'ladi — demo va kichik do'kon uchun yetarli.
const conversations = new Map();

console.log(`Bot ishga tushdi: ${knowledgeBase.business.name}`);

bot.on("message", async (msg) => {
  const chatId = msg.chat.id;
  const text = msg.text;
  if (!text) return;

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
    const { replyText, order, updatedHistory } = await handleMessage({
      knowledgeBase,
      history,
      userMessage: text,
    });

    conversations.set(chatId, updatedHistory);

    if (replyText) {
      await bot.sendMessage(chatId, replyText);
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
