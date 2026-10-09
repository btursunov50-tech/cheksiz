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
"menga sayt kerak" deb ism-telefon qoldiring — sizga "🔔 Yangi mijoz" xabari kelishi kerak.

### 7. Suhbat xotirasi (bepul)
Vercel → **cheksiz** loyihasi → **Storage** → **Create Database** → **Upstash for Redis** →
Free tarif → **Connect**. Prefix: `KV` (yoki istalgan lotin harfli nom). Vercel o'zi kerakli o'zgaruvchilarni qo'shadi.
So'ng **Redeploy**. Endi bot mijozni 30 kungacha eslab qoladi.

### 8. Ovozli xabarlar
1. https://console.groq.com → ro'yxatdan o'ting → **API Keys** → **Create API Key**.
2. Vercel'ga qo'shing: `GROQ_API_KEY` = shu kalit (Production) → **Redeploy**.
3. Botga o'zbek, dariy va pushtu tillarida ovozli xabar yuborib sinang.
   Pushtu yomon tanilsa, Groq o'rniga ElevenLabs kalitini (`ELEVENLABS_API_KEY`) qo'ying.

### 9. Xarajat chegarasi
https://console.anthropic.com → **Settings → Limits** → oylik limit (masalan $10).
Limitga yetganda bot "Sorry, something went wrong" deb javob beradi — balansni to'ldiring.

## Eslatmalar
- AI modeli: `claude-opus-5-5` (o'zgartirish: `ANTHROPIC_MODEL`). Javob chuqurligi: `ANTHROPIC_EFFORT` (`low` — tez va arzon).
- Xotira (7-qadam) ulanmagan bo'lsa, suhbat faqat server "issiq" turganda saqlanadi.
- Ovozli xabar matnga aylantiriladi, bot matn bilan javob beradi. 5 daqiqadan uzun ovoz qabul qilinmaydi.
- Vercel bepul (Hobby) tarifi rasmiy jihatdan notijorat loyihalar uchun; mijozlar ko'paygach Pro tarifga o'ting.

### 10. Mijoz topish: /top (faqat siz uchun)
Uch agent har bir biznes uchun shaxsiy taklif xatini tayyorlaydi:
1. **Tadqiqotchi** internetdan biznesni o'rganadi: nima sotadi, sayti, katalogi, xaritada bormi.
2. **Yozuvchi** shu ma'lumot asosida qisqa, shaxsiy xat yozadi.
3. **Tekshiruvchi** xatni 10 ballik shkalada baholaydi. 8 dan past bo'lsa, xat qayta yoziladi (ko'pi bilan 2 marta).

Botga shunday yozing (har qatorda bitta biznes, bir martada 15 tagacha):
```
/top
Mebel Lux — instagram.com/mebellux
Comfort Home, Chilonzor
```
Har biri 1-3 daqiqada tayyor bo'ladi. Xatni **bot yubormaydi**: siz o'qib, nusxalab,
o'zingiz yuborasiz va "✅ Yubordim" ni bosasiz. Buyruq faqat `OWNER_CHAT_ID` dan ishlaydi.

- Yangi deploy'dan keyin **4-qadamdagi webhook havolasini yana bir marta oching** (tugmalar ishlashi uchun).
- Narxi: bitta biznes taxminan $0.20–0.50 (Anthropic hisobingizdan).
- Agentlar Toshkent uchun sozlangan (`PROSPECT_REGION` bilan o'zgartirish mumkin).
- Instagram/Telegram sahifalarini agent har doim ham ocha olmaydi — havola bersangiz natija yaxshiroq.

### 11. Rasmlarni tushunish
Mijoz rasm yuborsa (menyu, do'kon, mahsulot, logotip, Instagram sahifasi skrinshoti),
bot uni ko'rib tahlil qiladi va mos xizmatni taklif qiladi. Rasm ostidagi savolga ham javob beradi.
Qo'shimcha sozlash kerak emas: rasm Anthropic Files API'ga yuklanadi (90 kun saqlanadi).
5 MB dan katta rasmlar va video/PDF fayllar hozircha qabul qilinmaydi.


### 12. Har kuni ertalabki post (kanal)
Har kuni soat **05:00 da** (Toshkent) bot [kanalga](https://t.me/infinite_ai_and_me) "Xayrli tong"
postini o'zi joylaydi: qimirlaydigan gulli video + shior + kun maslahati + bot havolasi.
Pul sarflanmaydi (maslahatlar oldindan yozilgan, Claude ishlatilmaydi).

- Bot kanalda **admin** bo'lishi va "Публикация сообщений" huquqi yoqilgan bo'lishi kerak.
- Vaqt `vercel.json` dagi `crons` da (UTC 00:00 = Toshkent 05:00). Bepul Vercel tarifida
  post 05:00–05:59 oralig'ida chiqadi.
- Videolar: `infinite/media/tong/` (`dushanba.mp4` … `yakshanba.mp4`, maxsus kunlar `YYYY-MM-DD.mp4`).
- Maslahatlar, tilaklar va maxsus kunlar: `bot/tong.js`.
- Sinash (kanalga chiqmaydi, faqat sizga keladi):
  `https://cheksiz-one.vercel.app/api/tong?key=<WEBHOOK_SECRET>&preview=1`
- Cron o'tkazib yuborsa, qo'lda joylash: `...&post=1` (bir kunda faqat bir marta chiqadi).
- Xato bo'lsa, bot sizga (OWNER_CHAT_ID) xabar yuboradi.
