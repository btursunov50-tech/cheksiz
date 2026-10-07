# CLAUDE.md — Infinite AI & Me (cheksiz)

## Who you work with
- Owner: Boxo (Telegram @Boxo_xxxx), from Uzbekistan, turns 50 in December 2026 (not 18: an earlier note was wrong and it ended up in a public LinkedIn post). Never state the owner's age or personal details in public text without asking. Runs **Infinite AI & Me**, a small human + AI agency that sells QR catalog sites, AI Telegram bots, QR menus, AI video ads, logos, Google Maps listings and posts to small businesses in Uzbekistan (Tashkent first) and Afghanistan.
- Answer in **Uzbek (Latin)**, simply and clearly, without jargon. Use short sections and tables.
- Whenever you mention a website or settings page, **give the direct link** (Vercel, Anthropic Console, GitHub, the bot, the site).
- The owner has said: **do everything you can without asking**. That includes opening a PR and merging it yourself (squash) once checks pass. Still ask before spending the owner's money or changing anything outside this repo.
- Be honest about limits: say what you could not test or reach.

## What is in the repo
| Path | What |
|---|---|
| `infinite/index.html` | Agency site in 16 languages (keys `s1t`…`s10d` etc., English is the fallback). The video changes with the language (`videoFor` in the page). |
| `infinite/media/` | Ad videos: `infinite-ai-ad.mp4` (original, Dari voice), `-uz`, `-ru`, `-en` versions built from it. |
| `btrend/` | B-Trend.MCHJ product catalog (first client / demo). |
| `api/infinite-bot.js` | Telegram bot webhook (Vercel function, `maxDuration` 300). Chat with Claude, voice messages (Groq/ElevenLabs/OpenAI STT), images (Anthropic Files API), leads sent to the owner, owner-only `/top`. |
| `bot/knowledge.js` | Services, prices (UZS for Uzbekistan, USD elsewhere), languages, system prompt, `videoFor(lang)`. **Edit prices and services here.** |
| `bot/prospect.js` | `/top`: researcher (web search), writer, reviewer agents that draft personal offers for Tashkent businesses. Drafts go only to the owner, who sends them by hand. |
| `bot/README.md` | Setup steps in Uzbek (env vars, webhook, Groq, Upstash, `/top`, images). |
| `video/` | Shorts/Reels maker: `template.html` (scenes + subtitles), `render.js` (Playwright frames), `mark.png` (gold ∞), `README.md` (steps, ffmpeg mix). |
| `infinite/media/logo-mark.png`, `favicon-64.png`, `icon-192.png`, `apple-touch-icon.png` | Gold ∞ logo (header) and site icons, cut from `infinity.jpg`. |

## Live services
- Site: https://cheksiz-one.vercel.app/infinite/
- Bot: https://t.me/sahiychishopbot
- Vercel project: https://vercel.com/btursunov50-7332s-projects/cheksiz (env vars: `/settings/environment-variables`, logs: `/logs`)
- After a deploy that changes `allowed_updates`, the owner must open `https://cheksiz-one.vercel.app/api/infinite-bot?setup=<WEBHOOK_SECRET>` once.
- Anthropic: Opus model for both the bot and `/top` (the owner chose to keep Opus). Auto-reload is on (top up to $15 below $5). A `/top` run costs about $0.45 per business.

## Social channels
The owner posts AI-themed short videos (Uzbek voice) on YouTube Shorts, Instagram, Facebook and LinkedIn. First one: MrBeast in Tashkent, 2026-10-07 (https://youtube.com/shorts/pxNi5MwMMGs).

## Lessons learned
- `/top`: web search rejects `user_location` with country `UZ`, so leave it out. Offer bots to high-message businesses (cafes, salons, clinics, courses, chains). For low-volume, high-value shops (furniture) offer a catalog, Google Maps or photos. Never pitch a bot as a replacement for the manager. Drafts link the bot demo and the Infinite site, not B-Trend.
- Telegram bots cannot message anyone first. Outreach is sent by the owner from their own account, 2–3 a day, during business hours.
- Videos: original scenes cut at 6/14/22 s. In scene 3 the cartoon girl speaks twice (about 14.5–16.6 s brand name, then 18–21 s call to action). The old English subtitles are removed by inpainting only the letters (OpenCV), not with boxes or blurred strips. Music: Uzbek/Russian use "Dutar's Whisper" from 3:17, English uses "SMART wallpaper" from 0:07, ducked under the voice.
- This cloud environment cannot reach many hosts (the Vercel site, TTS services, Hugging Face). Ask the owner to check live pages, and use files they upload.
- Before starting work, fetch `origin/main`: the owner also works from other sessions.
- Short videos (see `video/README.md`): Claude cannot hear audio and this environment has no Uzbek TTS/STT. Give the owner the voice text, they make the voice elsewhere; ask for one file per sentence, or align scenes by pauses and syllable counts, then ask the owner to check sync. Every video ends with a red "OBUNA BO'LING" button and, under it in gold, the bot (@sahiychishopbot) and the site. Music sits under the voice (sidechain ducking), not too quiet. Blur names/IDs in screenshots. YouTube gets a clean video plus uz/ru/en `.srt`; Instagram/Facebook get Russian subtitles burned in; LinkedIn gets English burned in and a "how I made it with AI" post. Don't put real people's AI faces or voices in videos.
- Uzbek news sites (kun.uz, daryo.uz, spot.uz) are blocked here; search in Uzbek/Russian and cite the search results.
