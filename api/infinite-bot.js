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
//   <PREFIX>_REST_API_URL / <PREFIX>_REST_API_TOKEN   optional, Upstash Redis (Vercel Storage);
//                        keeps chat memory across restarts. Without it memory is in-process only.
//   GROQ_API_KEY or ELEVENLABS_API_KEY or OPENAI_API_KEY
//                        optional, speech-to-text for voice messages (first one set is used)
//   STT_MODEL            optional, overrides the speech-to-text model
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
const { toFile } = require("@anthropic-ai/sdk");
const { waitUntil } = require("@vercel/functions");
const { buildSystemPrompt, SITE_URL, videoFor } = require("../bot/knowledge");
const { prepareOffer, RefusedError } = require("../bot/prospect");
const { SUBS_KEY: TONG_SUBS } = require("../bot/tong");
const { DEMO_PROMPT, DEMO_INTRO, DEMO_KEYBOARD, DEMO_EXIT } = require("../bot/demo");

const TOKEN = process.env.TELEGRAM_BOT_TOKEN;
const SECRET = process.env.WEBHOOK_SECRET || "";
const OWNER_CHAT_ID = process.env.OWNER_CHAT_ID ? String(process.env.OWNER_CHAT_ID) : "";
const OWNER_USERNAME = process.env.OWNER_USERNAME || "";
const MODEL = process.env.ANTHROPIC_MODEL || "claude-opus-5-5";
const EFFORT = process.env.ANTHROPIC_EFFORT || "low";

// Vercel's Upstash integration names its variables <PREFIX>_REST_API_URL / _TOKEN,
// where the prefix is chosen when connecting (KV by default), so match on the suffix.
function envBySuffix(suffix) {
  const key = Object.keys(process.env).sort().find((k) => k.endsWith(suffix) && !k.includes("READ_ONLY"));
  return key ? process.env[key] : "";
}
const httpsOnly = (url) => (url && url.startsWith("https://") ? url : "");
const REDIS_URL =
  httpsOnly(process.env.KV_REST_API_URL) || httpsOnly(envBySuffix("_REST_API_URL")) || httpsOnly(process.env.UPSTASH_REDIS_REST_URL);
const REDIS_TOKEN =
  process.env.KV_REST_API_TOKEN || envBySuffix("_REST_API_TOKEN") || process.env.UPSTASH_REDIS_REST_TOKEN || "";
const HISTORY_TTL_SECONDS = 30 * 24 * 3600;
const MAX_VOICE_SECONDS = 300;
const MAX_PROSPECTS = 15;
// Claude accepts images up to 5 MB; Telegram photos are far smaller.
const MAX_IMAGE_BYTES = 5 * 1024 * 1024;
const IMAGE_TYPES = ["image/jpeg", "image/png", "image/gif", "image/webp"];

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

// Conversation memory is kept in Upstash Redis when configured, so a customer who
// comes back days later continues the same chat. The in-process map is a fallback.
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

async function redis(...command) {
  const res = await fetch(REDIS_URL, {
    method: "POST",
    headers: { authorization: `Bearer ${REDIS_TOKEN}`, "content-type": "application/json" },
    body: JSON.stringify(command),
  });
  const data = await res.json();
  if (data.error) throw new Error(`Redis ${command[0]}: ${data.error}`);
  return data.result;
}

const historyKey = (chatId) => `iam:chat:${chatId}`;

async function loadHistory(chatId) {
  if (REDIS_URL && REDIS_TOKEN) {
    try {
      const raw = await redis("GET", historyKey(chatId));
      return raw ? JSON.parse(raw) : [];
    } catch (err) {
      console.error("loadHistory failed:", err.message);
    }
  }
  return conversations.get(chatId) || [];
}

async function saveHistory(chatId, history) {
  conversations.set(chatId, history);
  if (!REDIS_URL || !REDIS_TOKEN) return;
  try {
    await redis("SET", historyKey(chatId), JSON.stringify(history), "EX", HISTORY_TTL_SECONDS);
  } catch (err) {
    console.error("saveHistory failed:", err.message);
  }
}

async function clearHistory(chatId) {
  conversations.delete(chatId);
  if (!REDIS_URL || !REDIS_TOKEN) return;
  try {
    await redis("DEL", historyKey(chatId));
  } catch (err) {
    console.error("clearHistory failed:", err.message);
  }
}

// True the first time an update id is seen. Telegram retries on slow responses, and
// separate function instances do not share memory, so Redis is the source of truth.
async function firstDelivery(updateId) {
  if (seenUpdates.has(updateId)) return false;
  seenUpdates.add(updateId);
  if (seenUpdates.size > 500) seenUpdates.delete(seenUpdates.values().next().value);
  if (!REDIS_URL || !REDIS_TOKEN) return true;
  try {
    return (await redis("SET", `iam:update:${updateId}`, "1", "NX", "EX", 3600)) === "OK";
  } catch (err) {
    console.error("dedupe failed:", err.message);
    return true;
  }
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

// Morning post subscription (api/tong.js sends to everyone in the set). Returns true if it changed.
async function setTongSub(chatId, on) {
  if (!REDIS_URL || !REDIS_TOKEN) return false;
  try {
    return (await redis(on ? "SADD" : "SREM", TONG_SUBS, String(chatId))) === 1;
  } catch (err) {
    console.error("tong subscription failed:", err.message);
    return false;
  }
}

const tongButton = (on) => ({
  reply_markup: {
    inline_keyboard: [[on ? { text: "🔕 To'xtatish", callback_data: "tong:off" } : { text: "☀️ Qayta yoqish", callback_data: "tong:on" }]],
  },
});
const TONG_ON_TEXT = "☀️ Siz har kungi ertalabki tabrikka obuna bo'ldingiz. Har kuni ertalab gulli video va kun maslahati keladi.\nTo'xtatish: /tong_off";
const TONG_OFF_TEXT = "🔕 Ertalabki tabrik to'xtatildi. Qayta yoqish: /tong_on";

// Demo mode ("Demo Kafe", bot/demo.js): kept per chat for a week.
const demoChats = new Set();
async function isDemo(chatId) {
  if (REDIS_URL && REDIS_TOKEN) {
    try {
      return (await redis("GET", `iam:mode:${chatId}`)) === "demo";
    } catch (err) {
      console.error("isDemo failed:", err.message);
    }
  }
  return demoChats.has(chatId);
}
async function setDemo(chatId, on) {
  if (on) demoChats.add(chatId);
  else demoChats.delete(chatId);
  if (!REDIS_URL || !REDIS_TOKEN) return;
  try {
    if (on) await redis("SET", `iam:mode:${chatId}`, "demo", "EX", 7 * 24 * 3600);
    else await redis("DEL", `iam:mode:${chatId}`);
  } catch (err) {
    console.error("setDemo failed:", err.message);
  }
}
const DEMO_END_TEXT = "Demo tugadi. Endi yana Infinite AI & Me yordamchisiman: biznesingiz haqida yozing, sizga mos bot yoki sayt taklif qilaman.";

async function sendText(chatId, text, extra = {}) {
  const parts = [];
  for (let i = 0; i < text.length; i += 4000) parts.push(text.slice(i, i + 4000));
  for (const part of parts) {
    await tg("sendMessage", { chat_id: chatId, text: part, disable_web_page_preview: true, ...extra });
  }
}

function linkButtons(lang) {
  return {
    reply_markup: {
      inline_keyboard: [[
        { text: "🌐 Website", url: SITE_URL },
        { text: "🎬 Video", url: videoFor(lang) },
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

function sttProvider() {
  if (process.env.GROQ_API_KEY) {
    return {
      name: "groq",
      url: "https://api.groq.com/openai/v1/audio/transcriptions",
      headers: { authorization: `Bearer ${process.env.GROQ_API_KEY}` },
      fields: { model: process.env.STT_MODEL || "whisper-large-v3", response_format: "verbose_json" },
      languageField: "language",
    };
  }
  if (process.env.ELEVENLABS_API_KEY) {
    return {
      name: "elevenlabs",
      url: "https://api.elevenlabs.io/v1/speech-to-text",
      headers: { "xi-api-key": process.env.ELEVENLABS_API_KEY },
      fields: { model_id: process.env.STT_MODEL || "scribe_v1" },
      languageField: "language_code",
    };
  }
  if (process.env.OPENAI_API_KEY) {
    return {
      name: "openai",
      url: "https://api.openai.com/v1/audio/transcriptions",
      headers: { authorization: `Bearer ${process.env.OPENAI_API_KEY}` },
      fields: { model: process.env.STT_MODEL || "gpt-4o-transcribe" },
    };
  }
  return null;
}

// Whisper often mistakes Uzbek speech for a related Turkic language. Our customers are
// mostly Uzbek, so such results are re-run with Uzbek forced, unless the customer's
// Telegram is set to that Turkic language.
const TURKIC_MISHEARS = {
  turkish: "tr", kazakh: "kk", azerbaijani: "az", tatar: "tt", bashkir: "ba", turkmen: "tk",
  tr: "tr", kk: "kk", az: "az", tt: "tt", ba: "ba", tk: "tk",
};

async function sttRequest(provider, audio, name, mimeType, language) {
  const form = new FormData();
  form.append("file", new Blob([audio], { type: mimeType }), name);
  for (const [k, v] of Object.entries(provider.fields)) form.append(k, v);
  if (language) form.append(provider.name === "elevenlabs" ? "language_code" : "language", language);
  const res = await fetch(provider.url, { method: "POST", headers: provider.headers, body: form });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) throw new Error(`${res.status} ${JSON.stringify(data).slice(0, 200)}`);
  const detected = provider.languageField ? String(data[provider.languageField] || "").toLowerCase() : "";
  return { text: (data.text || "").trim(), language: language || detected };
}

// Downloads a Telegram voice/audio file and returns { text, language }; text is ""
// when speech-to-text is not configured or fails.
async function transcribe(media, telegramLang) {
  const provider = sttProvider();
  if (!provider) {
    console.error("Transcription skipped: no GROQ_API_KEY / ELEVENLABS_API_KEY / OPENAI_API_KEY set");
    return { text: "", language: "" };
  }
  if ((media.duration || 0) > MAX_VOICE_SECONDS) return { text: "", language: "" };
  try {
    const file = await tg("getFile", { file_id: media.file_id });
    if (!file.ok) return { text: "", language: "" };
    const dl = await fetch(`https://api.telegram.org/file/bot${TOKEN}/${file.result.file_path}`);
    if (!dl.ok) throw new Error(`download ${dl.status}`);
    const audio = await dl.arrayBuffer();
    // Telegram stores voice notes as .oga, which speech-to-text APIs reject by extension.
    const name = (file.result.file_path.split("/").pop() || "voice.ogg").replace(/\.oga$/i, ".ogg");
    const mimeType = media.mime_type || "audio/ogg";
    let result = await sttRequest(provider, audio, name, mimeType);
    const misheard = TURKIC_MISHEARS[result.language];
    if (misheard && misheard !== telegramLang) {
      result = await sttRequest(provider, audio, name, mimeType, provider.name === "elevenlabs" ? "uzb" : "uz");
    }
    console.log(`Voice (${provider.name}, ${result.language || "?"}): ${result.text.slice(0, 120)}`);
    return result;
  } catch (err) {
    console.error(`Transcription failed (${provider.name}):`, err.message);
    return { text: "", language: "" };
  }
}

// Uploads a customer's photo (or an image sent as a file) to the Anthropic Files API
// and returns its file id, or "" if it cannot be used. History keeps only the small
// file reference, so stored chats stay small and are never rewritten.
async function uploadImage(msg) {
  let fileId, mimeType, size;
  if (msg.photo && msg.photo.length) {
    const largest = msg.photo[msg.photo.length - 1];
    fileId = largest.file_id;
    mimeType = "image/jpeg";
    size = largest.file_size || 0;
  } else if (msg.document && IMAGE_TYPES.includes(msg.document.mime_type)) {
    fileId = msg.document.file_id;
    mimeType = msg.document.mime_type;
    size = msg.document.file_size || 0;
  } else {
    return "";
  }
  if (size > MAX_IMAGE_BYTES) return "";
  try {
    const file = await tg("getFile", { file_id: fileId });
    if (!file.ok) return "";
    const dl = await fetch(`https://api.telegram.org/file/bot${TOKEN}/${file.result.file_path}`);
    if (!dl.ok) throw new Error(`download ${dl.status}`);
    const bytes = Buffer.from(await dl.arrayBuffer());
    if (bytes.length > MAX_IMAGE_BYTES) return "";
    const name = file.result.file_path.split("/").pop() || "photo.jpg";
    const uploaded = await anthropic().files.upload({
      file: await toFile(bytes, name, { type: mimeType }),
      expires_in_seconds: 90 * 24 * 3600, // longest allowed; chats older than this start fresh on error
    });
    return uploaded.id;
  } catch (err) {
    console.error("Image upload failed:", err && err.status, err && err.message);
    return "";
  }
}

function textOf(content) {
  return content.filter((b) => b.type === "text").map((b) => b.text).join("\n").trim();
}

async function askClaude(chatId, userText, from, demo = false) {
  let history = await loadHistory(chatId);
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
      system: [{ type: "text", text: demo ? DEMO_PROMPT : SYSTEM_PROMPT, cache_control: { type: "ephemeral" } }],
      ...(demo ? {} : { tools: [LEAD_TOOL] }), // demo orders never reach the owner
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

  await saveHistory(chatId, history);
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

  if (/^\/?demo(@\w+)?$/i.test(text)) {
    await setDemo(chatId, true);
    await clearHistory(chatId);
    await sendText(chatId, DEMO_INTRO, DEMO_KEYBOARD);
    return;
  }
  if (text === DEMO_EXIT) {
    await setDemo(chatId, false);
    await clearHistory(chatId);
    await sendText(chatId, DEMO_END_TEXT, { reply_markup: { remove_keyboard: true } });
    return;
  }

  if (/^\/tong_(on|off)(@\w+)?$/.test(text)) {
    const on = text.startsWith("/tong_on");
    await setTongSub(chatId, on);
    await sendText(chatId, on ? TONG_ON_TEXT : TONG_OFF_TEXT, tongButton(on));
    return;
  }

  if (/^\/top(@\w+)?(\s|$)/.test(text) && OWNER_CHAT_ID && String(chatId) === OWNER_CHAT_ID) {
    await startProspecting(chatId, text.replace(/^\/top(@\w+)?/, ""));
    return;
  }

  let userText;
  if (text.startsWith("/start")) {
    await clearHistory(chatId);
    if (await isDemo(chatId)) {
      await setDemo(chatId, false);
      await sendText(chatId, "Demo tugadi.", { reply_markup: { remove_keyboard: true } });
    }
    userText = `The customer just opened the bot (/start).${langHint} Greet them in their language, say in one sentence what Infinite AI & Me does, list our main services as a short list (catalog website, AI Telegram bot, website + bot package, QR menu, AI video ad, logo, Google Maps) with a few words on how each helps, and ask what business they have.`;
  } else if (text) {
    userText = text + langHint;
  } else if (msg.voice || msg.audio) {
    await tg("sendChatAction", { chat_id: chatId, action: "typing" });
    const heard = await transcribe(msg.voice || msg.audio, from.language_code);
    const guess = heard.language ? `; speech recognition guessed the language as "${heard.language}", which may be wrong` : "";
    userText = heard.text
      ? `[Voice message, automatically transcribed - may contain recognition errors${guess}]: ${heard.text}${langHint}`
      : `[The customer sent a voice message that could not be transcribed.]${langHint}`;
  } else if (msg.video_note) {
    userText = `[The customer sent a round video message, which you cannot watch.]${langHint}`;
  } else if (msg.photo || (msg.document && IMAGE_TYPES.includes(msg.document.mime_type))) {
    await tg("sendChatAction", { chat_id: chatId, action: "typing" });
    const imageId = await uploadImage(msg);
    const caption = msg.caption ? ` with caption: "${msg.caption}"` : " without a caption";
    userText = imageId
      ? [
          { type: "image", source: { type: "file", file_id: imageId } },
          { type: "text", text: `[The customer sent this image${caption}.]${langHint}` },
        ]
      : `[The customer sent an image${caption}, but it could not be opened.]${langHint}`;
  } else if (msg.document || msg.video || msg.sticker) {
    userText = `[The customer sent a ${msg.sticker ? "sticker" : msg.video ? "video" : "file"}${msg.caption ? ` with caption: "${msg.caption}"` : ""}.]${langHint}`;
  } else {
    return;
  }

  await tg("sendChatAction", { chat_id: chatId, action: "typing" });
  let reply;
  try {
    reply = await askClaude(chatId, userText, from, !text.startsWith("/start") && (await isDemo(chatId)));
  } catch (err) {
    console.error("Claude error:", err && err.status, err && err.message);
    await clearHistory(chatId); // a half-finished exchange would break the next request
    reply = "Sorry, something went wrong. Please try again in a minute.";
  }
  if (reply) await sendText(chatId, reply, text.startsWith("/start") ? linkButtons(from.language_code) : {});
  // /start also subscribes to the morning post; tell them once, with a stop button.
  if (text.startsWith("/start") && (await setTongSub(chatId, true))) {
    await sendText(chatId, TONG_ON_TEXT, tongButton(true));
  }
}

// Read-only health check: which optional features are configured (no secrets shown).
async function status(res) {
  const provider = sttProvider();
  let memory = "not configured";
  if (REDIS_URL && REDIS_TOKEN) {
    try {
      memory = (await redis("PING")) === "PONG" ? "ok" : "unexpected reply";
    } catch (err) {
      memory = `error: ${err.message}`;
    }
  }
  let voice = "not configured";
  if (provider) {
    try {
      const r = await fetch(provider.name === "elevenlabs" ? "https://api.elevenlabs.io/v1/user" : provider.url.replace(/audio\/transcriptions$/, "models"), {
        headers: provider.headers,
      });
      voice = r.ok ? `${provider.name}: key ok` : `${provider.name}: key rejected (${r.status})`;
    } catch (err) {
      voice = `${provider.name}: error ${err.message}`;
    }
  }
  res.status(200).json({ memory, voice, owner_chat_id: Boolean(OWNER_CHAT_ID), model: MODEL });
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
    // Only the owner sees this, so show the real error to make problems fixable.
    const detail = String((err && err.message) || err).slice(0, 300);
    const why = err instanceof RefusedError ? "AI bu so'rovni rad etdi" : `texnik xato: ${detail}`;
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
  if (chatId && (cb.data === "tong:on" || cb.data === "tong:off")) {
    const on = cb.data === "tong:on";
    await setTongSub(chatId, on);
    await tg("answerCallbackQuery", { callback_query_id: cb.id, text: on ? "Yoqildi" : "To'xtatildi" });
    // The button may sit under a video post, so send a fresh note instead of editing it.
    await sendText(chatId, on ? TONG_ON_TEXT : TONG_OFF_TEXT, tongButton(on));
    return;
  }
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
    if (SECRET && q.status === SECRET) return status(res);
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
  if (update.update_id != null && !(await firstDelivery(update.update_id))) {
    return res.status(200).send("ok");
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
