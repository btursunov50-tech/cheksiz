// Owner-only reminders from bot/reminders.js (Vercel Cron, see vercel.json).
// Cron: 04:00 UTC = 09:00 Tashkent. Sends that day's messages to OWNER_CHAT_ID only.
// Manual: /api/remind?key=<WEBHOOK_SECRET>&show=1 (shows today's list), &send=1 (sends now).

const REMINDERS = require("../bot/reminders");

const TOKEN = process.env.TELEGRAM_BOT_TOKEN;
const SECRET = process.env.WEBHOOK_SECRET || "";
const CRON_SECRET = process.env.CRON_SECRET || "";
const OWNER_CHAT_ID = process.env.OWNER_CHAT_ID ? String(process.env.OWNER_CHAT_ID) : "";

// Tashkent is UTC+5 all year.
const today = (now = new Date()) => new Date(now.getTime() + 5 * 3600 * 1000).toISOString().slice(0, 10);

function fromCron(req) {
  const auth = req.headers.authorization || "";
  if (CRON_SECRET) return auth === `Bearer ${CRON_SECRET}`;
  return /vercel-cron/i.test(req.headers["user-agent"] || "");
}

module.exports = async function handler(req, res) {
  const q = req.query || {};
  const byOwner = SECRET && q.key === SECRET;
  const date = today();
  const list = REMINDERS[date] || [];
  if (byOwner && q.show) return res.status(200).json({ date, list });
  if (!(fromCron(req) || (byOwner && q.send))) return res.status(401).send("unauthorized");
  if (!TOKEN || !OWNER_CHAT_ID) return res.status(500).json({ error: "TELEGRAM_BOT_TOKEN or OWNER_CHAT_ID is not set" });
  const results = [];
  for (const text of list) {
    const r = await fetch(`https://api.telegram.org/bot${TOKEN}/sendMessage`, {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ chat_id: OWNER_CHAT_ID, text }),
    }).then((x) => x.json());
    results.push(r.ok);
  }
  res.status(200).json({ date, sent: results.filter(Boolean).length, total: list.length });
};
