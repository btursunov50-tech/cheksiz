// Telegram webhook for the "Infinite AI & Me" bot (Vercel serverless function).
//
// Environment variables (set in Vercel -> Settings -> Environment Variables):
//   TELEGRAM_BOT_TOKEN   token from @BotFather
//   ANTHROPIC_API_KEY    key from console.anthropic.com
//   WEBHOOK_SECRET       any long random string you choose
//   OWNER_CHAT_ID        your numeric Telegram ID (send /myid to the bot to get it)
//   OWNER_USERNAME       optional, e.g. @your_username - shown to customers as the manager
//   ANTHROPIC_MODEL      optional, defaults to claude-opus-5-5
//   ANTHROPIC_EFFORT     optional, defaults to low
//   GROQ_API_KEY         optional, key from console.groq.com - turns on voice message
//                        understanding (speech-to-text with Whisper). Without it the bot
//                        asks customers to type instead.
//   STT_MODEL            optional, defaults to whisper-large-v3
//   PROSPECT_MODEL       optional, model for the /top lead-finding agents
//                        (defaults to ANTHROPIC_MODEL, then claude-opus-5-5)
//
// One-time setup after deploying: open
//   https://<your-domain>/api/infinite-bot?setup=<WEBHOOK_SECRET>
// in a browser. It registers this URL as the bot's webhook.
//
// Owner-only command /top: the owner sends a list of businesses (one per line)
// and three agents (bot/prospect.js) prepare a personal offer for each one. Each
// business runs in its own invocation of this function, which calls itself for
// the next one, so a long list never hits the function time limit.

const Anthropic = require("@anthropic-ai/sdk");
const { waitUntil } = require("@vercel/functions");
const { buildSystemPrompt, SITE_URL, VIDEO_URL } = require("../bot/knowledge");
const { prepareOffer, RefusedError } = require("../bot/prospect");

const TOKEN = process.env.TELEGRAM_BOT_TOKEN;
const SECRET = process.env.WEBHOOK_SECRET || "";
const OWNER_CHAT_ID = process.env.OWNER_CHAT_ID ? String(process.env.OWNER_CHAT_ID) : "";
const OWNER_USERNAME = process.env.OWNER_USERNAME || "";
const MODEL = process.env.ANTHROPIC_MODEL || "claude-opus-5-5";
const EFFORT = process.env.ANTHROPIC_EFFORT || "low";
const GROQ_API_KEY = process.env.GROQ_API_KEY || "";
const STT_MODEL = process.env.STT_MODEL || "whisper-large-v3";
// Longer recordings are refused so one message cannot eat the function's time limit.
const MAX_VOICE_SECONDS = 300;
const MAX_PROSPECTS = 15;

const SYSTEM_PROMPT = buildSystemPrompt({ ownerUsername: OWNER_USERNAME });

const LEAD_TOOL = {
  name: "submit_lead",
  description:
    "Send a new customer's request to the manager. Call it only after the customer has given at least their name, a contact (phone, WhatsApp or Telegram) and what they need, and you have repeated it back to them.",
  strict: true,
  input_schema: {
    type: "object",
    additionalProperties: false,
    properties: {
      name: { type: "string", description: "Customer name" },
      contact: { type: "string", description: "Phone, WhatsApp or Telegram contact" },
      business: { type: "string", description: "Business type in Uzbek (Latin), or empty string if unknown" },
      location: { type: "string", description: "City and country in Uzbek (Latin), or empty string if unknown" },
      needs: { type: "string", description: "Services the customer wants, written in Uzbek (Latin) for the manager" },
      language: { type: "string", description: "Language the customer writes in, named in Uzbek (e.g. dariy, pushtu, o'zbek)" },
    },
    required: ["name", "contact", "business", "location", "needs", "language"],
  },
};

// Conversation memory lives in the warm function instance. It is lost on a cold
// start, which is acceptable for short sales chats.
const conversations = new Map();
const seenUpdates = new Set();
// History is append-only: editing or trimming earlier turns would invalidate the
// model's thinking blocks, so a long chat starts fresh instead of being trimmed.
const MAX_HISTORY = 40;

let client;
function anthropic() {
  if (!client) client = new Anthropic();
  return client;
}

async function tg(method, payload) {
  const res = await fetch(`https://api.telegram.org/bot${TOKEN}/${method}`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(payload),
  });
  const data = await res.json().catch(() => ({}));
  if (!data.ok) console.error(`Telegram ${method} failed:`, JSON.stringify(data).slice(0, 300));
  return data;
}

async function sendText(chatId, text, extra = {}) {
  const parts = [];
  for (let i = 0; i < text.length; i += 4000) parts.push(text.slice(i, i + 4000));
  for (const part of parts) {
    await tg("sendMessage", { chat_id: chatId, text: part, disable_web_page_preview: true, ...extra });
  }
}

// Downloads a voice/audio/video-note file from Telegram and turns it into text.
// Returns the transcript, or "" when it could not be produced.
async function transcribe(media, kind) {
  if (!GROQ_API_KEY) return "";
  const info = await tg("getFile", { file_id: media.file_id });
  const filePath = info.ok && info.result && info.result.file_path;
  if (!filePath) return "";

  const fileRes = await fetch(`https://api.telegram.org/file/bot${TOKEN}/${filePath}`);
  if (!fileRes.ok) {
    console.error("Voice download failed:", fileRes.status);
    return "";
  }
  const bytes = await fileRes.arrayBuffer();

  // Telegram voice notes are Ogg/Opus with an .oga extension; Whisper wants a known one.
  const ext = (filePath.split(".").pop() || "").toLowerCase();
  const name = kind === "video_note" ? "note.mp4" : ext === "oga" || !ext ? "voice.ogg" : `audio.${ext}`;

  const form = new FormData();
  form.append("file", new Blob([bytes]), name);
  form.append("model", STT_MODEL);
  form.append("response_format", "json");
  form.append("temperature", "0");

  const sttRes = await fetch("https://api.groq.com/openai/v1/audio/transcriptions", {
    method: "POST",
    headers: { authorization: `Bearer ${GROQ_API_KEY}` },
    body: form,
  });
  const data = await sttRes.json().catch(() => ({}));
  if (!sttRes.ok) {
    console.error("Transcription failed:", sttRes.status, JSON.stringify(data).slice(0, 300));
    return "";
  }
  return String(data.text || "").trim();
}

function linkButtons() {
  return {
    reply_markup: {
      inline_keyboard: [[
        { text: "🌐 Website", url: SITE_URL },
        { text: "🎬 Video", url: VIDEO_URL },
      ]],
    },
  };
}

async function notifyOwner(lead, from) {
  if (!OWNER_CHAT_ID) {
    console.warn("OWNER_CHAT_ID is not set; lead not forwarded:", JSON.stringify(lead));
    return false;
  }
  const who = from.username ? `@${from.username}` : `${from.first_name || ""} ${from.last_name || ""}`.trim();
  const text = [
    "🔔 Yangi mijoz — Infinite AI & Me",
    `Ism: ${lead.name}`,
    `Aloqa: ${lead.contact}`,
    `Telegram: ${who} (id ${from.id})`,
    `Biznes: ${lead.business || "-"}`,
    `Joylashuv: ${lead.location || "-"}`,
    `Kerak: ${lead.needs}`,
    `Mijoz tili: ${lead.language}`,
  ].join("\n");
  const res = await tg("sendMessage", { chat_id: OWNER_CHAT_ID, text });
  return Boolean(res.ok);
}

function textOf(content) {
  return content.filter((b) => b.type === "text").map((b) => b.text).join("\n").trim();
}

async function askClaude(chatId, userText, from) {
  let history = conversations.get(chatId) || [];
  if (history.length > MAX_HISTORY) history = [];
  const startLen = history.length;
  history.push({ role: "user", content: userText });

  let reply = "";
  for (let round = 0; round < 3; round++) {
    const response = await anthropic().beta.messages.create({
      model: MODEL,
      max_tokens: 4096,
      betas: ["server-side-fallback-2026-07-01"],
      fallbacks: "default",
      output_config: { effort: EFFORT },
      system: [{ type: "text", text: SYSTEM_PROMPT, cache_control: { type: "ephemeral" } }],
      tools: [LEAD_TOOL],
      messages: history,
    });

    if (response.stop_reason === "refusal") {
      reply = "Sorry, I can't help with that. Please ask about our websites, bots or video ads.";
      history.length = startLen; // drop this whole exchange so it doesn't poison later requests
      break;
    }

    history.push({ role: "assistant", content: response.content });
    const toolUses = response.content.filter((b) => b.type === "tool_use");
    reply = textOf(response.content) || reply;

    if (response.stop_reason !== "tool_use" || toolUses.length === 0) break;

    const results = [];
    for (const tu of toolUses) {
      if (tu.name === "submit_lead") {
        const ok = await notifyOwner(tu.input, from);
        results.push({
          type: "tool_result",
          tool_use_id: tu.id,
          content: ok ? "Sent to the manager." : "Could not reach the manager right now; ask the customer to also write to the manager directly.",
          is_error: !ok,
        });
      } else {
        results.push({ type: "tool_result", tool_use_id: tu.id, content: "Unknown tool.", is_error: true });
      }
    }
    history.push({ role: "user", content: results });
  }

  conversations.set(chatId, history);
  return reply;
}

async function handleMessage(msg) {
  const chatId = msg.chat.id;
  const from = msg.from || {};
  const langHint = from.language_code ? ` [Telegram language hint: ${from.language_code}]` : "";

  if (msg.chat.type !== "private") return;

  const text = (msg.text || "").trim();

  if (text === "/myid") {
    await sendText(chatId, `Your Telegram ID: ${chatId}\nPut it in OWNER_CHAT_ID to receive customer requests.`);
    return;
  }

  if (/^\/top(@\w+)?(\s|$)/.test(text) && OWNER_CHAT_ID && String(chatId) === OWNER_CHAT_ID) {
    await startProspecting(chatId, text.replace(/^\/top(@\w+)?/, ""));
    return;
  }

  let userText;
  if (text.startsWith("/start")) {
    conversations.delete(chatId);
    userText = `The customer just opened the bot (/start).${langHint} Greet them in their language, say in 2-3 sentences what Infinite AI & Me does, and ask what business they have.`;
  } else if (text) {
    userText = text + langHint;
  } else if (msg.voice || msg.audio || msg.video_note) {
    const kind = msg.voice ? "voice" : msg.audio ? "audio" : "video_note";
    const media = msg[kind];
    let transcript = "";
    if (GROQ_API_KEY && (media.duration || 0) <= MAX_VOICE_SECONDS) {
      await tg("sendChatAction", { chat_id: chatId, action: "typing" });
      try {
        transcript = await transcribe(media, kind);
      } catch (err) {
        console.error("Transcription error:", err && err.message);
      }
    }
    if (transcript) {
      userText = `[Voice message, transcribed automatically - names, numbers and phone numbers may contain mistakes; confirm them with the customer before sending a lead.]\n${transcript}${msg.caption ? `\n[Caption: "${msg.caption}"]` : ""}${langHint}`;
    } else if (GROQ_API_KEY && (media.duration || 0) > MAX_VOICE_SECONDS) {
      userText = `[The customer sent a voice message longer than ${MAX_VOICE_SECONDS / 60} minutes, which is too long to listen to. Ask them to send a shorter one or write.]${langHint}`;
    } else {
      userText = `[The customer sent a voice message, which you could not listen to.]${langHint}`;
    }
  } else if (msg.photo || msg.document || msg.video || msg.sticker) {
    userText = `[The customer sent a ${msg.photo ? "photo" : msg.sticker ? "sticker" : "file"}${msg.caption ? ` with caption: "${msg.caption}"` : ""}.]${langHint}`;
  } else {
    return;
  }

  await tg("sendChatAction", { chat_id: chatId, action: "typing" });
  let reply;
  try {
    reply = await askClaude(chatId, userText, from);
  } catch (err) {
    console.error("Claude error:", err && err.status, err && err.message);
    conversations.delete(chatId); // a half-finished exchange would break the next request
    reply = "Sorry, something went wrong. Please try again in a minute.";
  }
  if (reply) await sendText(chatId, reply, text.startsWith("/start") ? linkButtons() : {});
}

// ---- /top: lead finding for the owner ----

const TOP_HELP = [
  "🔍 Mijoz topish",
  "",
  "/top dan keyin har bir qatorga bitta biznes yozing: nomi, bo'lsa havola, telefon yoki tuman. Masalan:",
  "",
  "/top",
  "Mebel Lux — instagram.com/mebellux",
  "Comfort Home, Chilonzor",
  "Shirin Tort qandolatxonasi, Yunusobod",
  "",
  `Bir martada ${MAX_PROSPECTS} tagacha. Har biriga 1-3 daqiqa ketadi. Xatlarni bot yubormaydi — siz o'qib, o'zingiz yuborasiz.`,
].join("\n");

async function startProspecting(chatId, body) {
  const items = body
    .split("\n")
    .map((line) => line.trim())
    .filter(Boolean)
    .slice(0, MAX_PROSPECTS);
  if (items.length === 0) {
    await sendText(chatId, TOP_HELP);
    return;
  }
  if (!SECRET || !selfUrl) {
    await sendText(chatId, "WEBHOOK_SECRET sozlanmagan — /top ishlamaydi.");
    return;
  }
  await sendText(chatId, `🔍 ${items.length} ta biznes navbatga qo'yildi. Tadqiqot boshlandi — har biri tayyor bo'lishi bilan yuboraman.`);
  await queueNext({ chatId, items, index: 0, ready: 0 });
}

// The webhook's own URL, remembered from the first request so jobs can chain.
let selfUrl = "";

async function queueNext(job) {
  try {
    const res = await fetch(`${selfUrl}?job=1`, {
      method: "POST",
      headers: { "content-type": "application/json", "x-job-secret": SECRET },
      body: JSON.stringify(job),
    });
    if (!res.ok) throw new Error(`status ${res.status}`);
  } catch (err) {
    console.error("Could not queue prospect job:", err && err.message);
    await sendText(job.chatId, `⚠️ Navbatni davom ettirib bo'lmadi (${job.index + 1}/${job.items.length} dan). Qolganlarini /top bilan qayta yuboring.`);
  }
}

const leadButtons = {
  reply_markup: {
    inline_keyboard: [[
      { text: "✅ Yubordim", callback_data: "lead:sent" },
      { text: "⏭ O'tkazish", callback_data: "lead:skip" },
    ]],
  },
};

async function runProspectJob(job) {
  const { chatId, items, index } = job;
  const label = `${index + 1}/${items.length}`;
  let ready = job.ready || 0;
  try {
    const result = await prepareOffer(items[index]);
    if (result.skipped) {
      await sendText(chatId, `⏭ ${label} — ${result.name}\nXat yozilmadi: ${result.reason}`);
    } else {
      const { draft, review, rounds } = result;
      ready++;
      await sendText(chatId, [
        `✅ ${label} — ${draft.business_name}`,
        `Baho: ${review.score}/10${review.pass ? "" : " ⚠️ talabga yetmadi, diqqat bilan tekshiring"}${rounds > 1 ? ` (${rounds}-variant)` : ""}`,
        `Kimga: ${draft.contact}`,
        `Taklif: ${draft.offer}`,
        `Nega: ${draft.why_fit}`,
        "",
        "Xat pastda 👇 (bosib turib nusxalang)",
      ].join("\n"));
      await sendText(chatId, draft.message, leadButtons);
    }
  } catch (err) {
    console.error("Prospect failed:", err && err.status, err && err.message);
    const why = err instanceof RefusedError ? "AI bu so'rovni rad etdi" : "texnik xato";
    await sendText(chatId, `⚠️ ${label} — ${items[index]}\nTayyorlab bo'lmadi (${why}).`);
  }

  if (index + 1 < items.length) {
    await queueNext({ chatId, items, index: index + 1, ready });
  } else {
    await sendText(chatId, `🏁 Tayyor: ${items.length} ta biznesdan ${ready} ta xat. Yuborganingizdan keyin "✅ Yubordim" ni bosing.`);
  }
}

async function handleCallback(cb) {
  const chatId = cb.message && cb.message.chat && cb.message.chat.id;
  if (!OWNER_CHAT_ID || String(chatId) !== OWNER_CHAT_ID || !String(cb.data || "").startsWith("lead:")) {
    await tg("answerCallbackQuery", { callback_query_id: cb.id });
    return;
  }
  const sent = cb.data === "lead:sent";
  await tg("answerCallbackQuery", { callback_query_id: cb.id, text: sent ? "Belgilandi: yuborildi" : "O'tkazib yuborildi" });
  await tg("editMessageReplyMarkup", {
    chat_id: chatId,
    message_id: cb.message.message_id,
    reply_markup: { inline_keyboard: [[{ text: sent ? "✅ Yuborildi" : "⏭ O'tkazildi", callback_data: "lead:done" }]] },
  });
}

async function setup(req, res) {
  const host = req.headers["x-forwarded-host"] || req.headers.host;
  const url = `https://${host}/api/infinite-bot`;
  const webhook = await tg("setWebhook", {
    url,
    secret_token: SECRET,
    allowed_updates: ["message", "callback_query"],
    drop_pending_updates: true,
  });
  const commands = await tg("setMyCommands", {
    commands: [{ command: "start", description: "Start / Boshlash / شروع" }],
  });
  res.status(200).json({ webhook_url: url, setWebhook: webhook, setMyCommands: commands });
}

module.exports = async function handler(req, res) {
  if (!TOKEN) {
    res.status(500).json({ error: "TELEGRAM_BOT_TOKEN is not set" });
    return;
  }

  const host = req.headers["x-forwarded-host"] || req.headers.host;
  if (host && !selfUrl) selfUrl = `https://${host}/api/infinite-bot`;

  if (req.method === "GET") {
    const q = req.query || {};
    if (SECRET && q.setup === SECRET) return setup(req, res);
    res.status(200).send("Infinite AI & Me bot is running.");
    return;
  }

  if ((req.query || {}).job) {
    if (!SECRET || req.headers["x-job-secret"] !== SECRET) {
      res.status(401).send("unauthorized");
      return;
    }
    // Answer at once so the caller is free; the work continues in the background.
    waitUntil(runProspectJob(req.body).catch((err) => console.error("Prospect job crashed:", err)));
    res.status(202).send("queued");
    return;
  }

  if (SECRET && req.headers["x-telegram-bot-api-secret-token"] !== SECRET) {
    res.status(401).send("unauthorized");
    return;
  }

  const update = req.body || {};
  if (update.update_id != null) {
    if (seenUpdates.has(update.update_id)) return res.status(200).send("ok");
    seenUpdates.add(update.update_id);
    if (seenUpdates.size > 500) seenUpdates.delete(seenUpdates.values().next().value);
  }

  try {
    if (update.message) await handleMessage(update.message);
    else if (update.callback_query) await handleCallback(update.callback_query);
  } catch (err) {
    console.error("Update failed:", err);
  }
  // Always 200 so Telegram does not resend the same update.
  res.status(200).send("ok");
};
