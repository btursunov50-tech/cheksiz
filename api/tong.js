// Daily "Xayrli tong" post to the Telegram channel (Vercel Cron, see vercel.json).
//
// Cron: 00:00 UTC = 05:00 Tashkent. The bot must be an admin of the channel with
// "Post messages". Content (video, tips, wishes) comes from bot/tong.js.
// After the channel, the same post goes to every private chat in SUBS_KEY (people who
// pressed /start in the bot; /tong_off or the stop button removes them). Chats that
// blocked the bot are dropped from the list.
//
// Manual use, with WEBHOOK_SECRET as key:
//   /api/tong?key=<WEBHOOK_SECRET>&show=1      today's post and the subscriber count, sends nothing
//   /api/tong?key=<WEBHOOK_SECRET>&preview=1   sends today's post to the owner only
//   /api/tong?key=<WEBHOOK_SECRET>&post=1      posts now (channel + subscribers, once per day)
//   /api/tong?key=<WEBHOOK_SECRET>&import=1    adds everyone who chatted with the bot (last 30 days) to the list
//   /api/tong?key=<WEBHOOK_SECRET>&clip=1      sends CLIP from bot/tong.js to the channel + subscribers (once)

const { buildPost, CHANNEL, SUBS_KEY, CLIP } = require("../bot/tong");

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
const hasRedis = () => Boolean(REDIS_URL && REDIS_TOKEN);

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

const STOP_BUTTON = { inline_keyboard: [[{ text: "🔕 To'xtatish", callback_data: "tong:off" }]] };

// post = { kind: "animation" | "video", media, caption }. If Telegram cannot fetch the
// media, the text still goes out.
async function send(chatId, post, extra = {}) {
  const field = post.kind === "video" ? "video" : "animation";
  const method = post.kind === "video" ? "sendVideo" : "sendAnimation";
  const r = await tg(method, { chat_id: chatId, [field]: post.media, caption: post.caption, supports_streaming: true, ...extra });
  if (r.ok) return r;
  if (r.error_code === 403) return r; // blocked the bot: no point in a text fallback
  const fallback = await tg("sendMessage", { chat_id: chatId, text: post.caption, ...extra });
  return { ...fallback, videoError: r.description };
}

async function tellOwner(text) {
  if (OWNER_CHAT_ID) await tg("sendMessage", { chat_id: OWNER_CHAT_ID, text }).catch(() => {});
}

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

// Channel first; subscribers then reuse the file Telegram already has.
async function broadcast(post) {
  const channel = await send(CHAT, post);
  const msg = channel.ok && channel.result;
  const sent = msg && (post.kind === "video" ? msg.video : msg.animation || msg.document);
  const media = sent && sent.file_id;
  const subscribers = { sent: 0, failed: 0, removed: 0 };
  if (hasRedis()) {
    const ids = (await redis("SMEMBERS", SUBS_KEY).catch(() => [])) || [];
    for (const id of ids) {
      const r = await send(id, media ? { ...post, media } : post, { reply_markup: STOP_BUTTON });
      if (r.ok) subscribers.sent++;
      else if (r.error_code === 403 || /chat not found|user is deactivated/i.test(r.description || "")) {
        subscribers.removed++;
        await redis("SREM", SUBS_KEY, id).catch(() => {});
      } else subscribers.failed++;
      await sleep(50); // stay well under Telegram's ~30 messages per second
    }
  }
  return { channel, subscribers };
}

// Adds every private chat that still has bot memory (iam:chat:<id>, kept 30 days).
async function importChats() {
  let cursor = "0";
  let added = 0;
  do {
    const [next, keys] = await redis("SCAN", cursor, "MATCH", "iam:chat:*", "COUNT", 500);
    cursor = String(next);
    const ids = keys.map((k) => k.slice("iam:chat:".length)).filter((id) => /^\d+$/.test(id));
    if (ids.length) added += await redis("SADD", SUBS_KEY, ...ids);
  } while (cursor !== "0");
  return { added, total: await redis("SCARD", SUBS_KEY) };
}

// True the first time this key is claimed (always true without Redis).
async function once(key) {
  if (!hasRedis()) return true;
  try {
    return (await redis("SET", key, "1", "NX", "EX", 7 * 86400)) === "OK";
  } catch (err) {
    console.error("once failed:", err.message);
    return true;
  }
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
  const daily = buildPost();
  const post = { kind: "animation", media: daily.video, caption: daily.caption };

  if (byOwner && q.show) {
    const subscribers = hasRedis() ? await redis("SCARD", SUBS_KEY).catch(() => null) : null;
    return res.status(200).json({ ...daily, subscribers });
  }
  if (byOwner && q.preview) {
    if (!OWNER_CHAT_ID) return res.status(400).json({ error: "OWNER_CHAT_ID is not set" });
    return res.status(200).json(await send(OWNER_CHAT_ID, post));
  }
  if (byOwner && q.import) {
    if (!hasRedis()) return res.status(400).json({ error: "Redis (Upstash) is not set" });
    return res.status(200).json(await importChats());
  }
  if (byOwner && q.clip) {
    if (!(await once(`iam:clip:${CLIP.id}`))) return res.status(200).json({ skipped: "clip already sent" });
    const result = await broadcast({ kind: "video", media: CLIP.video, caption: CLIP.caption });
    if (!result.channel.ok) await tellOwner(`⚠️ Klip kanalga chiqmadi: ${result.channel.description || "noma'lum xato"}`);
    return res.status(200).json(result);
  }
  if (!(fromCron(req) || (byOwner && q.post))) return res.status(401).send("unauthorized");

  // Once per Tashkent day, even if the cron fires twice or the owner also posts by hand.
  if (!(await once(`iam:tong:${daily.date}`))) {
    return res.status(200).json({ skipped: "already posted today", date: daily.date });
  }

  const result = await broadcast(post);
  if (!result.channel.ok && !result.subscribers.sent && hasRedis()) await redis("DEL", `iam:tong:${daily.date}`).catch(() => {});
  if (!result.channel.ok) {
    await tellOwner(`⚠️ Ertalabki post kanalga chiqmadi (${daily.date}): ${result.channel.description || "noma'lum xato"}`);
  } else if (result.channel.videoError) {
    await tellOwner(`⚠️ Ertalabki post faqat matn bilan chiqdi, video yuklanmadi: ${result.channel.videoError}`);
  }
  res.status(result.channel.ok ? 200 : 502).json(result);
};
