// Daily "Xayrli tong" post to the Telegram channel (Vercel Cron, see vercel.json).
//
// Cron: 00:00 UTC = 05:00 Tashkent. The bot must be an admin of the channel with
// "Post messages". Content (video, tips, wishes) comes from bot/tong.js.
//
// Manual use, with WEBHOOK_SECRET as key:
//   /api/tong?key=<WEBHOOK_SECRET>&show=1      shows today's post as JSON, sends nothing
//   /api/tong?key=<WEBHOOK_SECRET>&preview=1   sends today's post to the owner only
//   /api/tong?key=<WEBHOOK_SECRET>&post=1      posts to the channel now (once per day)

const { buildPost, CHANNEL } = require("../bot/tong");

const TOKEN = process.env.TELEGRAM_BOT_TOKEN;
const SECRET = process.env.WEBHOOK_SECRET || "";
const CRON_SECRET = process.env.CRON_SECRET || "";
const OWNER_CHAT_ID = process.env.OWNER_CHAT_ID ? String(process.env.OWNER_CHAT_ID) : "";
const CHAT = process.env.TONG_CHAT_ID || CHANNEL;

function envBySuffix(suffix) {
  const key = Object.keys(process.env).sort().find((k) => k.endsWith(suffix) && !k.includes("READ_ONLY"));
  return key ? process.env[key] : "";
}
const httpsOnly = (url) => (url && url.startsWith("https://") ? url : "");
const REDIS_URL =
  httpsOnly(process.env.KV_REST_API_URL) || httpsOnly(envBySuffix("_REST_API_URL")) || httpsOnly(process.env.UPSTASH_REDIS_REST_URL);
const REDIS_TOKEN =
  process.env.KV_REST_API_TOKEN || envBySuffix("_REST_API_TOKEN") || process.env.UPSTASH_REDIS_REST_TOKEN || "";

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

async function tg(method, payload) {
  const res = await fetch(`https://api.telegram.org/bot${TOKEN}/${method}`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(payload),
  });
  return res.json();
}

// Sends the video with its caption; if Telegram cannot fetch the video, the text still goes out.
async function send(chatId, post) {
  const r = await tg("sendAnimation", { chat_id: chatId, animation: post.video, caption: post.caption });
  if (r.ok) return r;
  const fallback = await tg("sendMessage", { chat_id: chatId, text: post.caption });
  return { ...fallback, videoError: r.description };
}

async function tellOwner(text) {
  if (OWNER_CHAT_ID) await tg("sendMessage", { chat_id: OWNER_CHAT_ID, text }).catch(() => {});
}

function fromCron(req) {
  const auth = req.headers.authorization || "";
  if (CRON_SECRET) return auth === `Bearer ${CRON_SECRET}`;
  return /vercel-cron/i.test(req.headers["user-agent"] || "");
}

module.exports = async function handler(req, res) {
  if (!TOKEN) return res.status(500).json({ error: "TELEGRAM_BOT_TOKEN is not set" });
  const q = req.query || {};
  const byOwner = SECRET && q.key === SECRET;
  const post = buildPost();

  if (byOwner && q.show) return res.status(200).json(post);
  if (byOwner && q.preview) {
    if (!OWNER_CHAT_ID) return res.status(400).json({ error: "OWNER_CHAT_ID is not set" });
    return res.status(200).json(await send(OWNER_CHAT_ID, post));
  }
  if (!(fromCron(req) || (byOwner && q.post))) return res.status(401).send("unauthorized");

  // Once per Tashkent day, even if the cron fires twice or the owner also posts by hand.
  const key = `iam:tong:${post.date}`;
  if (REDIS_URL && REDIS_TOKEN) {
    try {
      if ((await redis("SET", key, "1", "NX", "EX", 172800)) !== "OK") {
        return res.status(200).json({ skipped: "already posted today", date: post.date });
      }
    } catch (err) {
      console.error("tong dedupe failed:", err.message);
    }
  }

  const result = await send(CHAT, post);
  if (!result.ok) {
    if (REDIS_URL && REDIS_TOKEN) await redis("DEL", key).catch(() => {});
    await tellOwner(`⚠️ Ertalabki post kanalga chiqmadi (${post.date}): ${result.description || "noma'lum xato"}`);
  } else if (result.videoError) {
    await tellOwner(`⚠️ Ertalabki post faqat matn bilan chiqdi, video yuklanmadi: ${result.videoError}`);
  }
  res.status(result.ok ? 200 : 502).json(result);
};
