# Shop AI Bot

Universal Telegram AI-bot: savollarga javob beradi, buyurtma qabul qiladi va
buyurtmani Google Sheets'ga yozadi. Bitta bot — `data/knowledge.json`
faylini almashtirib, istalgan biznes turiga (kafe, bar, do'kon, fast-food
budka) moslashtiriladi.

## 1. Birinchi marta ishga tushirish

### 1.1. Telegram bot yaratish (5 daqiqa)

1. Telegram'da `@BotFather` ni toping va yozing.
2. `/newbot` buyrug'ini yuboring.
3. Botga nom bering (masalan "Abu Sahiy Shop Bot").
4. Username bering, `bot` bilan tugashi kerak (masalan `AbuSahiyShop_bot`).
5. BotFather sizga **token** beradi (masalan `123456:ABC-DEF...`) — buni saqlab qo'ying.

### 1.2. Anthropic API kalitini olish

1. https://console.anthropic.com ga kiring (ro'yxatdan o'ting agar hali yo'q bo'lsa).
2. API kalit yarating.
3. Hisobingizga biroz kredit qo'shing (bir necha dollar boshlash uchun yetarli — har bir
   suhbat juda arzon, Claude Haiku modeli ishlatiladi).

### 1.3. Loyihani sozlash

```bash
cd shop-bot
npm install
cp .env.example .env
```

`.env` faylini oching va to'ldiring:

```
TELEGRAM_BOT_TOKEN=BotFather bergan token
ANTHROPIC_API_KEY=Anthropic'dan olingan kalit
```

### 1.4. Ishga tushirish

```bash
npm start
```

Terminalda "Bot ishga tushdi: ..." degan xabar chiqsa — tayyor. Endi
Telegram'da o'sha botni toping va `/start` yozing.

## 2. Do'kon ma'lumotlarini to'ldirish

`data/knowledge.json` faylini oching. Ichida "TO'LDIRING" deb yozilgan
joylarni haqiqiy ma'lumot bilan almashtiring:

- `business.location` — aniq manzil (shahar, mall/bozor nomi, qavat)
- `business.workHours` — ish vaqti
- `business.phone` — aloqa telefoni
- `business.delivery.note` — yetkazib berish narxi va muddati
- `products` — har bir mahsulot uchun narx, o'lcham

Mahsulot qo'shish uchun `products` ro'yxatiga yangi obyekt qo'shing, xuddi
borlaridek formatda. Fayl saqlangach, bot avtomatik yangi ma'lumotdan
foydalanadi (botni qayta ishga tushirish kerak).

## 3. Google Sheets'ga buyurtmalarni ulash (ixtiyoriy, lekin tavsiya etiladi)

Buni sozlamasangiz ham bot ishlayveradi — buyurtmalar
`data/orders.local.json` fayliga yoziladi. Lekin do'kon egasi jadval
ko'rishni istasa:

1. Yangi Google Sheets jadval oching.
2. Extensions → Apps Script.
3. `google-apps-script.js` faylidagi kodni ko'chirib, Apps Script
   muharririga joylashtiring.
4. Deploy → New deployment → Web app.
   - Execute as: Me
   - Who has access: Anyone
5. Deploy tugmasini bosing, sizga bir **Web app URL** beriladi.
6. Shu URL'ni `.env` faylidagi `SHEETS_WEBHOOK_URL` ga qo'ying.
7. Botni qayta ishga tushiring.

## 4. Xodimga Telegram orqali bildirishnoma (ixtiyoriy)

Yangi buyurtma kelganda sotuvchiga avtomatik xabar yuborish uchun:

1. O'z Telegram chat ID'ingizni bilib oling (masalan `@userinfobot` ga yozib).
2. `.env` faylidagi `STAFF_NOTIFY_CHAT_ID` ga shu ID'ni qo'ying.

## 4.1. Mahsulotlarga haqiqiy rasm/video biriktirish

Mijozlar ko'pincha "haqiqiy rasmini ko'rsating" yoki "video bormi" deb
so'raydi. Bot bunga matn bilan emas, do'kon egasi yuborgan HAQIQIY rasm/video
bilan javob bera oladi.

**Sozlash:**

1. O'z Telegram chat ID'ingizni bilib oling (`@userinfobot` ga yozib).
2. `.env` faylidagi `OWNER_CHAT_ID` ga shu ID'ni qo'ying.
3. Botni qayta ishga tushiring (`npm start`).

**Foydalanish:**

1. O'zingiz (do'kon egasi sifatida) botga mahsulot rasmi yoki videosini
   yuboring.
2. Rasmga **caption (izoh)** sifatida mahsulot nomini yozing, masalan
   `Kuzgi Dvoyka` (aynan `data/knowledge.json` dagi `name` bilan mos yoki
   unga yaqin bo'lishi kerak).
3. Bot "Saqlandi: ..." deb tasdiqlaydi.
4. Shundan keyin mijoz o'sha mahsulot haqida "rasmini yuboring" yoki
   "video bormi" desa, bot avtomatik ravishda siz yuborgan haqiqiy
   rasm/videoni mijozga jo'natadi.

Bitta mahsulotga bir nechta rasm/video yuborsangiz, hammasi saqlanadi va
mijoz so'raganda hammasi yuboriladi.

## 4.2. Mijoz rasm yuborsa

Agar mijoz (do'kon egasi emas) botga rasm yuborsa — masalan "shunga o'xshash
narsa bormi?" deb rasm bilan savol bersa — bot AI orqali rasmni ko'rib,
mos javob berishga harakat qiladi.

## 5. Yangi mijozga (boshqa do'konga) sotish

Har bir yangi mijoz uchun butun loyihani qaytadan yozish SHART EMAS:

1. Loyihani nusxalang (yoki `KNOWLEDGE_FILE` orqali alohida knowledge
   fayl ko'rsating).
2. Yangi `knowledge-<mijoz-nomi>.json` fayl yarating, o'sha mijozning
   mahsulotlari/ma'lumotlari bilan to'ldiring.
3. Yangi `.env` faylida:
   - Yangi Telegram bot tokeni (har mijozga alohida bot)
   - `KNOWLEDGE_FILE=./data/knowledge-<mijoz-nomi>.json`
4. `npm start` — alohida server sifatida ishga tushiring (yoki bitta
   serverga bir nechta bot process'ini qo'shing).

Shu tartibda bitta kodni ko'p marta, ko'p mijozga sota olasiz.

## 6. Keyingi qadam: web sahifa + QR kod

Hozirgi versiya faqat Telegram orqali ishlaydi (eng tez ishga tushadigan
variant). Keyingi bosqichda shu bitta `botEngine.js` asosida QR-kod orqali
ochiladigan veb-chat sahifa ham qo'shish mumkin — mator (AI mantiq) bir xil
qoladi, faqat "old tomoni" (interfeys) qo'shiladi.
