// Owner-only reminders from bot/reminders.js (Vercel Cron, see vercel.json).
// Crons: 04:00, 15:00 and 16:00 UTC = 09:00, 20:00 and 21:00 Tashkent (Hobby crons fire within the hour).
// Each run sends to OWNER_CHAT_ID only today's messages for the current Tashkent hour
// (plain strings = 09:00, { at: 20, text } = 20:00).
// Manual: /api/remind?key=<WEBHOOK_SECRET>&show=1 (today's list), &send=1 (sends the 09:00 ones now, &at=20 for 20:00).

const REMINDERS = require("../bot/reminders");

const TOKEN = process.env.TELEGRAM_BOT_TOKEN;
const SECRET = process.env.WEBHOOK_SECRET || "";
const CRON_SECRET = process.env.CRON_SECRET || "";
const OWNER_CHAT_ID = process.env.OWNER_CHAT_ID ? String(process.env.OWNER_CHAT_ID) : "";

// Tashkent is UTC+5 all year.
const tashkent = (now = new Date()) => new Date(now.getTime() + 5 * 3600 * 1000);
const hourOf = (item) => (typeof item === "string" ? 9 : Number(item.at));
const textOf = (item) => (typeof item === "string" ? item : item.text);

function fromCron(req) {
  const auth = req.headers.authorization || "";
  if (CRON_SECRET) return auth === `Bearer ${CRON_SECRET}`;
  return /vercel-cron/i.test(req.headers["user-agent"] || "");
}

module.exports = async function handler(req, res) {
  const q = req.query || {};
  const byOwner = SECRET && q.key === SECRET;
  const t = tashkent();
  const date = t.toISOString().slice(0, 10);
  const all = REMINDERS[date] || [];
  if (byOwner && q.show) return res.status(200).json({ date, list: all });
  const cron = fromCron(req);
  if (!(cron || (byOwner && q.send))) return res.status(401).send("unauthorized");
  const hour = cron ? t.getUTCHours() : Number(q.at || 9);
  const list = all.filter((item) => hourOf(item) === hour).map(textOf);
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
  res.status(200).json({ date, hour, sent: results.filter(Boolean).length, total: list.length });
};
