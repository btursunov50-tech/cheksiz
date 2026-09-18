const fs = require("fs");
const path = require("path");

const LOCAL_FALLBACK_PATH = path.join(__dirname, "..", "data", "orders.local.json");

function appendLocalOrder(order) {
  let existing = [];
  if (fs.existsSync(LOCAL_FALLBACK_PATH)) {
    try {
      existing = JSON.parse(fs.readFileSync(LOCAL_FALLBACK_PATH, "utf8"));
    } catch {
      existing = [];
    }
  }
  existing.push(order);
  fs.writeFileSync(LOCAL_FALLBACK_PATH, JSON.stringify(existing, null, 2));
}

async function logOrder(order) {
  const webhookUrl = process.env.SHEETS_WEBHOOK_URL;

  if (!webhookUrl) {
    appendLocalOrder(order);
    return { stored: "local", path: LOCAL_FALLBACK_PATH };
  }

  const response = await fetch(webhookUrl, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(order),
  });

  if (!response.ok) {
    appendLocalOrder(order);
    return { stored: "local_after_webhook_failure", status: response.status };
  }

  return { stored: "sheets" };
}

module.exports = { logOrder };
