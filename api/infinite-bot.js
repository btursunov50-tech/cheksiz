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
//   KV_REST_API_URL / KV_REST_API_TOKEN   optional, Upstash Redis (Vercel Storage);
//                        keeps chat memory across restarts. Without it memory is in-process only.
//   GROQ_API_KEY or ELEVENLABS_API_KEY or OPENAI_API_KEY
//                        optional, speech-to-text for voice messages (first one set is used)
//   STT_MODEL            optional, overrides the speech-to-text model
//
// One-time setup after deploying: open
//   https://<your-domain>/api/infinite-bot?setup=<WEBHOOK_SECRET>
// in a browser. It registers this URL as the bot's webhook.

const Anthropic = require("@anthropic-ai/sdk");
const { buildSystemPrompt, SITE_URL, VIDEO_URL } = require("../bot/knowledge");

const TOKEN = process.env.TELEGRAM_BOT_TOKEN;
const SECRET = process.env.WEBHOOK_SECRET || "";
const OWNER_CHAT_ID = process.env.OWNER_CHAT_ID ? String(process.env.OWNER_CHAT_ID) : "";
const OWNER_USERNAME = process.env.OWNER_USERNAME || "";
const MODEL = process.env.ANTHROPIC_MODEL || "claude-opus-5-5";
const EFFORT = process.env.ANTHROPIC_EFFORT || "low";

const REDIS_URL = process.env.KV_REST_API_URL || process.env.UPSTASH_REDIS_REST_URL || "";
const REDIS_TOKEN = process.env.KV_REST_API_TOKEN || process.env.UPSTASH_REDIS_REST_TOKEN || "";
const HISTORY_TTL_SECONDS = 30 * 24 * 3600;
const MAX_VOICE_SECONDS = 300;

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

async function sendText(chatId, text, extra = {}) {
  const parts = [];
  for (let i = 0; i < text.length; i += 4000) parts.push(text.slice(i, i + 4000));
  for (const part of parts) {
    await tg("sendMessage", { chat_id: chatId, text: part, disable_web_page_preview: true, ...extra });
  }
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

function sttProvider() {
  if (process.env.GROQ_API_KEY) {
    return {
      url: "https://api.groq.com/openai/v1/audio/transcriptions",
      headers: { authorization: `Bearer ${process.env.GROQ_API_KEY}` },
      fields: { model: process.env.STT_MODEL || "whisper-large-v3" },
    };
  }
  if (process.env.ELEVENLABS_API_KEY) {
    return {
      url: "https://api.elevenlabs.io/v1/speech-to-text",
      headers: { "xi-api-key": process.env.ELEVENLABS_API_KEY },
      fields: { model_id: process.env.STT_MODEL || "scribe_v1" },
    };
  }
  if (process.env.OPENAI_API_KEY) {
    return {
      url: "https://api.openai.com/v1/audio/transcriptions",
      headers: { authorization: `Bearer ${process.env.OPENAI_API_KEY}` },
      fields: { model: process.env.STT_MODEL || "gpt-4o-transcribe" },
    };
  }
  return null;
}

// Downloads a Telegram voice/audio file and returns its transcript, or "" when
// speech-to-text is not configured or fails.
async function transcribe(media) {
  const provider = sttProvider();
  if (!provider || (media.duration || 0) > MAX_VOICE_SECONDS) return "";
  try {
    const file = await tg("getFile", { file_id: media.file_id });
    if (!file.ok) return "";
    const audio = await fetch(`https://api.telegram.org/file/bot${TOKEN}/${file.result.file_path}`);
    if (!audio.ok) throw new Error(`download ${audio.status}`);
    const form = new FormData();
    const name = file.result.file_path.split("/").pop() || "voice.ogg";
    form.append("file", new Blob([await audio.arrayBuffer()], { type: media.mime_type || "audio/ogg" }), name);
    for (const [k, v] of Object.entries(provider.fields)) form.append(k, v);
    const res = await fetch(provider.url, { method: "POST", headers: provider.headers, body: form });
    const data = await res.json().catch(() => ({}));
    if (!res.ok) throw new Error(`${res.status} ${JSON.stringify(data).slice(0, 200)}`);
    return (data.text || "").trim();
  } catch (err) {
    console.error("Transcription failed:", err.message);
    return "";
  }
}

function textOf(content) {
  return content.filter((b) => b.type === "text").map((b) => b.text).join("\n").trim();
}

async function askClaude(chatId, userText, from) {
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

  let userText;
  if (text.startsWith("/start")) {
    await clearHistory(chatId);
    userText = `The customer just opened the bot (/start).${langHint} Greet them in their language, say in 2-3 sentences what Infinite AI & Me does, and ask what business they have.`;
  } else if (text) {
    userText = text + langHint;
  } else if (msg.voice || msg.audio) {
    await tg("sendChatAction", { chat_id: chatId, action: "typing" });
    const heard = await transcribe(msg.voice || msg.audio);
    userText = heard
      ? `[Voice message, automatically transcribed - may contain recognition errors]: ${heard}${langHint}`
      : `[The customer sent a voice message that could not be transcribed.]${langHint}`;
  } else if (msg.video_note) {
    userText = `[The customer sent a round video message, which you cannot watch.]${langHint}`;
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
    await clearHistory(chatId); // a half-finished exchange would break the next request
    reply = "Sorry, something went wrong. Please try again in a minute.";
  }
  if (reply) await sendText(chatId, reply, text.startsWith("/start") ? linkButtons() : {});
}

async function setup(req, res) {
  const host = req.headers["x-forwarded-host"] || req.headers.host;
  const url = `https://${host}/api/infinite-bot`;
  const webhook = await tg("setWebhook", {
    url,
    secret_token: SECRET,
    allowed_updates: ["message"],
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

  if (req.method === "GET") {
    const q = req.query || {};
    if (SECRET && q.setup === SECRET) return setup(req, res);
    res.status(200).send("Infinite AI & Me bot is running.");
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
  } catch (err) {
    console.error("Update failed:", err);
  }
  // Always 200 so Telegram does not resend the same update.
  res.status(200).send("ok");
};
