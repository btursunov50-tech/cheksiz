// "Mijoz topish" pipeline for the owner: three agents prepare a personal offer
// for one business. Nothing is sent to the business - the owner reads, edits
// and sends each message by hand.
//
//   1. Researcher  - searches the web for the business and what it is missing
//   2. Writer      - drafts a short personal offer from the research
//   3. Reviewer    - scores the draft; below PASS_SCORE it goes back to the writer

const Anthropic = require("@anthropic-ai/sdk");
const { SERVICES, SITE_URL } = require("./knowledge");

const MODEL = process.env.PROSPECT_MODEL || process.env.ANTHROPIC_MODEL || "claude-opus-5-5";
const REGION = process.env.PROSPECT_REGION || "Tashkent, Uzbekistan";
// Our own sales bot doubles as a live demo the business can try.
const BOT_DEMO_URL = process.env.PROSPECT_BOT_DEMO_URL || "https://t.me/sahiychishopbot";
const PASS_SCORE = 8;
const MAX_REWRITES = 2;

let client;
function anthropic() {
  if (!client) client = new Anthropic();
  return client;
}

const PRICE_LIST = SERVICES.map((s) => `- ${s.name} (${s.details}): ${s.uzs}`).join("\n");

const ABOUT_US = `"Infinite AI & Me" is a small human + AI team from Uzbekistan that builds QR catalog websites, AI Telegram bots, AI video ads and related services for small businesses.
Live demo of an AI Telegram bot (our own sales bot - anyone can open it and chat): ${BOT_DEMO_URL}
Our website (services, prices, video): ${SITE_URL}
Price list for Uzbekistan (starting prices, in UZS):
${PRICE_LIST}`;

const RESEARCHER_PROMPT = `You research small businesses in ${REGION} for "Infinite AI & Me", so the team can offer them a useful digital service.

${ABOUT_US}

The owner gives you one business: a name and sometimes a link, phone or district. Use web search and web fetch to find out, in at most a few searches:
- what the business is and sells, its district/address;
- where it is present online: website, Instagram, Telegram channel, Google Maps, Yandex Maps, 2GIS, OLX;
- what it is missing that we could fix: no website or catalog, prices only "in direct", no online ordering or bot, not on maps, few or poor photos, inactive pages;
- its public business contacts (business phone, Instagram, Telegram) - business contacts only, never private persons' personal data;
- the language and script it uses with customers (Uzbek Latin, Uzbek Cyrillic, Russian).

Instagram and Telegram pages often cannot be opened; then rely on search results, map listings and other sites, and say what you could not check. Never invent facts. If you cannot find a business with this name in ${REGION}, say so.

Answer in English, plain text, with exactly these sections:
FOUND: yes or no
BUSINESS: name, category, district
ONLINE PRESENCE: each channel with its link and what you saw
GAPS: what is missing, each with the evidence
CONTACT: best public channel to write to, with the handle/number
LANGUAGE: language and script it uses
BEST OFFER: one or two services from our price list that fit best, and why. Judge how many customer messages the business likely gets: a bot fits businesses with many repeated questions or orders (cafes, delivery, courses, clinics, beauty salons); for businesses with few, expensive orders where personal contact closes the sale (furniture, renovation, premium goods) prefer the catalog website, Google Maps listing or product photos over a bot
UNVERIFIED: anything you could not confirm`;

const WRITER_PROMPT = `You write the first message that "Infinite AI & Me" sends to a business in ${REGION}. The owner will read it, maybe edit it, and send it by hand on Instagram or Telegram.

${ABOUT_US}

Rules for the message:
- Write in the language and script the business uses (default: Uzbek Latin). Natural, polite, like a real person - not an advert.
- 50 to 90 words. Plain text, at most one emoji, no hashtags.
- Start with a short greeting, then one or two concrete things you noticed about THIS business (from the research only), then how one service would help their customers, then both of our links - the bot demo ${BOT_DEMO_URL} (invite them to write to it and see how it answers) and our website ${SITE_URL} - then one easy question (for example, whether they want to see how it would look for them).
- Never suggest replacing the owner's or manager's personal contact with customers. Present a bot as a helper that answers routine questions and collects requests at night and on days off, then hands the customer to the manager, who closes the sale personally.
- Offer one main service. A price is optional; if you give one, use the price list exactly and say "...dan" (starting from).
- Never invent facts, results, discounts, deadlines or guarantees. Do not mention anything the research marks as unverified.
- Mention gaps kindly as opportunities, never as criticism of the business. Leave out private-sounding details (staff names, days off, personal accounts).
- No pressure or spam phrases ("faqat bugun", "shoshiling", "100% kafolat").

If the research says the business was not found, or there is too little information for a personal message, set skip to true and explain why in skip_reason.
Fill why_fit in Uzbek Latin for the owner: one or two sentences on why this offer fits.`;

const REVIEWER_PROMPT = `You review a first sales message from "Infinite AI & Me" to a business in ${REGION}, before the owner sends it by hand. Be strict but fair.

${ABOUT_US}

Score it from 0 to 10. Check:
1. Personal: swap test - if you replace the business name with a competitor's, does the message still fit? Then it is generic (score 6 or lower).
2. Truth: every fact about the business comes from the research; nothing marked unverified is used.
3. Prices and services match the price list exactly; no invented discounts, deadlines or guarantees.
4. Language and script match what the business uses; grammar is natural.
5. Length 50-90 words, gaps framed kindly (not as criticism), polite, not pushy, no spam phrases, one clear easy question at the end, both the bot demo link and our website link included.

Set pass to true only when the score is ${PASS_SCORE} or higher and nothing in checks 2-3 is broken. Write problems and instructions in English for the writer; keep instructions short and concrete.`;

const DRAFT_SCHEMA = {
  type: "object",
  additionalProperties: false,
  properties: {
    skip: { type: "boolean" },
    skip_reason: { type: "string" },
    business_name: { type: "string" },
    contact: { type: "string", description: "Best public channel and handle/number to send the message to" },
    offer: { type: "string", description: "Offered service(s) in Uzbek Latin" },
    why_fit: { type: "string" },
    message: { type: "string" },
  },
  required: ["skip", "skip_reason", "business_name", "contact", "offer", "why_fit", "message"],
};

const REVIEW_SCHEMA = {
  type: "object",
  additionalProperties: false,
  properties: {
    score: { type: "integer" },
    pass: { type: "boolean" },
    problems: { type: "array", items: { type: "string" } },
    instructions: { type: "string" },
  },
  required: ["score", "pass", "problems", "instructions"],
};

class RefusedError extends Error {}

async function call(params) {
  const response = await anthropic().beta.messages.create({
    model: MODEL,
    max_tokens: 16000,
    betas: ["server-side-fallback-2026-07-01"],
    fallbacks: "default",
    ...params,
  });
  if (response.stop_reason === "refusal") throw new RefusedError("The model declined this request.");
  return response;
}

function textOf(content) {
  return content.filter((b) => b.type === "text").map((b) => b.text).join("").trim();
}

function parseJson(response, what) {
  if (response.stop_reason === "max_tokens") throw new Error(`${what}: answer was cut off`);
  return JSON.parse(textOf(response.content));
}

async function research(business) {
  const messages = [{ role: "user", content: `Business to research:\n${business}` }];
  let response;
  // Server-side web tools can pause a long turn; resend it unchanged to continue.
  for (let i = 0; i < 4; i++) {
    response = await call({
      system: RESEARCHER_PROMPT,
      output_config: { effort: process.env.PROSPECT_RESEARCH_EFFORT || "medium" },
      tools: [
        // No user_location: the API rejects country code UZ. The prompt keeps the search in Tashkent.
        { type: "web_search_20260209", name: "web_search", max_uses: 6 },
        { type: "web_fetch_20260209", name: "web_fetch", max_uses: 4 },
      ],
      messages,
    });
    if (response.stop_reason !== "pause_turn") break;
    messages.push({ role: "assistant", content: response.content });
  }
  const report = textOf(response.content);
  if (!report) throw new Error("Researcher returned no report");
  return report;
}

async function write(business, report, previous) {
  let content = `Business from the owner's list:\n${business}\n\nResearch:\n${report}`;
  if (previous) {
    content += `\n\nYour previous draft:\n${previous.draft.message}\n\nReviewer score ${previous.review.score}/10. Problems:\n- ${previous.review.problems.join("\n- ")}\nInstructions: ${previous.review.instructions}\n\nWrite an improved version.`;
  }
  const response = await call({
    system: WRITER_PROMPT,
    output_config: { effort: process.env.PROSPECT_WRITE_EFFORT || "medium", format: { type: "json_schema", schema: DRAFT_SCHEMA } },
    messages: [{ role: "user", content }],
  });
  return parseJson(response, "Writer");
}

async function review(report, draft) {
  const response = await call({
    system: REVIEWER_PROMPT,
    output_config: { effort: process.env.PROSPECT_REVIEW_EFFORT || "medium", format: { type: "json_schema", schema: REVIEW_SCHEMA } },
    messages: [{ role: "user", content: `Research:\n${report}\n\nOffered service: ${draft.offer}\n\nMessage to review:\n${draft.message}` }],
  });
  return parseJson(response, "Reviewer");
}

// Runs the three agents for one business. Resolves to
//   { skipped: true, name, reason }  or
//   { skipped: false, draft, review, rounds }
async function prepareOffer(business) {
  const report = await research(business);

  let draft = await write(business, report);
  if (draft.skip) return { skipped: true, name: draft.business_name || business, reason: draft.skip_reason };

  let verdict = await review(report, draft);
  let rounds = 1;
  let best = { draft, review: verdict };
  while (!verdict.pass && rounds <= MAX_REWRITES) {
    draft = await write(business, report, { draft, review: verdict });
    if (draft.skip) break;
    verdict = await review(report, draft);
    rounds++;
    if (verdict.score >= best.review.score) best = { draft, review: verdict };
  }
  return { skipped: false, draft: best.draft, review: best.review, rounds };
}

module.exports = { prepareOffer, RefusedError, PASS_SCORE };
