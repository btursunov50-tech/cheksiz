# Infinite AI & Me — Telegram bot (@sahiychishopbot)

Bot Vercel'da 24/7 ishlaydi (`api/infinite-bot.js`). Mijoz saytdagi 16 tilning
istalganida yozsa, shu tilda javob beradi, xizmat va narxlarni ("...dan") aytadi,
mijozning ismi, telefoni va ehtiyojini yig'ib, sizga Telegram'da yuboradi.

Narx va xizmatlarni o'zgartirish: `bot/knowledge.js` faylidagi `SERVICES` ro'yxati.

## Ishga tushirish (bir marta)

### 1. Telegram token
1. @BotFather → `/mybots` → **@sahiychishopbot** → **API Token** → **Revoke current token**.
   (Eski token kompyuterdagi eski kodda qolgan; yangisini olish xavfsizroq.)
2. Yangi tokenni nusxalab oling. **Chatga yozmang.**

### 2. Anthropic API kaliti
1. https://console.anthropic.com → **API Keys** → **Create Key** → nomi `infinite-ai-bot`.
2. **Settings → Limits** da oylik chegarani qo'ying (masalan $10).

### 3. Vercel sozlamalari
https://vercel.com → **cheksiz** loyihasi → **Settings → Environment Variables**.
Quyidagilarni qo'shing (Environment: **Production**):

| Name | Value |
|---|---|
| `TELEGRAM_BOT_TOKEN` | BotFather bergan token |
| `ANTHROPIC_API_KEY` | Anthropic kaliti |
| `WEBHOOK_SECRET` | o'zingiz o'ylab topgan uzun so'z, masalan `infinite2026_kabul_xyz` |
| `OWNER_USERNAME` | Telegram username'ingiz, masalan `@Boxo_xxxx` |

So'ng **Deployments** → oxirgi deploy → **⋯ → Redeploy**.

### 4. Webhook'ni yoqish
Brauzerda oching (o'z `WEBHOOK_SECRET` ingizni qo'ying):

```
https://cheksiz-one.vercel.app/api/infinite-bot?setup=WEBHOOK_SECRET
```

Javobda `"ok": true` chiqsa — bot ulandi.

### 5. Mijoz xabarlari sizga kelishi uchun
1. Telegram'da botga `/myid` yozing — u ID raqamingizni aytadi.
2. Vercel'da yana bitta o'zgaruvchi qo'shing: `OWNER_CHAT_ID` = shu raqam.
3. Yana **Redeploy** qiling.

### 6. Sinov
Botga `/start` yozing, keyin dariy, o'zbek, rus tillarida savol bering va
"menga sayt kerak" deb ism-telefon qoldiring — sizga "🔔 New customer" xabari kelishi kerak.

## Eslatmalar
- AI modeli: `claude-opus-5-5` (o'zgartirish: `ANTHROPIC_MODEL`). Javob chuqurligi: `ANTHROPIC_EFFORT` (`low` — tez va arzon).
- Suhbat xotirasi server "issiq" turganda saqlanadi; uzoq tanaffusdan keyin bot suhbatni yangidan boshlaydi.
- Ovozli xabarlarni tushunish keyingi bosqichda qo'shiladi; hozircha bot matn bilan yozishni so'raydi.
- Vercel bepul (Hobby) tarifi rasmiy jihatdan notijorat loyihalar uchun; mijozlar ko'paygach Pro tarifga o'ting.
