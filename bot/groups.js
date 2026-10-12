// Channel posts → the owner's Telegram groups.
//
// The owner adds the bot to a group (as a member who may send messages, or admin).
// Only groups the OWNER added are kept (my_chat_member update in api/infinite-bot.js),
// so a stranger cannot make the bot post into a group. Every new channel post
// (channel_post update; the bot must be a channel admin) and the morning post from
// api/tong.js are forwarded there with "Forwarded from Infinite AI & Me".
// Removing the bot from a group removes the group from the list.

const GROUPS_KEY = "iam:groups";

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

// forwardMessage to every group, once per channel message (SET NX, kept 7 days).
// tg(method, payload) and redis(...command) are the caller's helpers.
async function forwardToGroups({ tg, redis, fromChatId, messageId }) {
  const result = { sent: 0, failed: 0, removed: 0 };
  const fresh = await redis("SET", `iam:fwd:${fromChatId}:${messageId}`, "1", "NX", "EX", 7 * 86400).catch(() => "OK");
  if (fresh !== "OK") return { ...result, skipped: "already forwarded" };
  const ids = (await redis("SMEMBERS", GROUPS_KEY).catch(() => [])) || [];
  for (const id of ids) {
    let r = await tg("forwardMessage", { chat_id: id, from_chat_id: fromChatId, message_id: messageId });
    const moved = r.parameters && r.parameters.migrate_to_chat_id;
    if (!r.ok && moved) {
      // The group became a supergroup and got a new id.
      await redis("SREM", GROUPS_KEY, id).catch(() => {});
      await redis("SADD", GROUPS_KEY, String(moved)).catch(() => {});
      r = await tg("forwardMessage", { chat_id: moved, from_chat_id: fromChatId, message_id: messageId });
    }
    if (r.ok) result.sent++;
    else if (r.error_code === 403 || /chat not found|group chat was deactivated/i.test(r.description || "")) {
      result.removed++;
      await redis("SREM", GROUPS_KEY, String(moved || id)).catch(() => {});
    } else result.failed++;
    await sleep(100);
  }
  return result;
}

module.exports = { GROUPS_KEY, forwardToGroups };
