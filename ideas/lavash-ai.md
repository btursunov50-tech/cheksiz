# «Lavash AI»: kamera bilan retsept nazorati (2026-10-15, egasi Manus bilan maslahatlashgan)

## G'oya
Lavash tayyorlash stoli ustiga kamera qo'yiladi. AI har bir lavashda retseptdagi ingredientlar (non, go'sht, karam, pomidor, sous…) borligini tekshiradi va xato bo'lsa menejerga xabar beradi. Kunlik hisobot: qaysi ingredient ko'p unutilyapti, qaysi smenada xato ko'p.

## Manus ma'lumotlari tekshirildi
- WWT + Plainsight + Google Cloud + Intel: AQSh fast-food tarmog'ida ovqat miqdorini kamera bilan o'lchash sinovi, **95% boshlang'ich aniqlik** (sinov bosqichi, kompaniyalarning o'z ma'lumoti, mustaqil tekshiruv yo'q).
- Agot AI: buyurtma yig'ilishini kamera bilan tekshiradi, xatolarning 85% dan ko'pini aniqlaydi (CNBC, 2021; KFC, Pizza Hut, Taco Bell egalari bilan sinov).
- Intel'ning ochiq «Order Accuracy» namunaviy paketi bor: vision-language model kadrdagi narsalarni buyurtma bilan solishtiradi. Bepul asos sifatida ishlatsa bo'ladi.
- Xodimlarni kamera bilan kuzatish AQShda ham tanqid qilingan («deeply unsettling»): xizmatni xodimni jazolash emas, sifatga yordam deb sotish kerak, yuzlar kadrga tushmasin.

## Bizning baho
- G'oya to'g'ri: «AI sotmaymiz, bir xil sifat va kam isrofni sotamiz».
- Manus narxi (30–60 mln so'm o'rnatish) Toshkent lavashxonasi uchun juda baland. Birinchi mijozga arzon pilot, keyin oylik obuna.
- Qiyin joylari: oq sous oq nonda va ingredientlar ostida ko'rinmaydi; kamera bug', yorug'lik, qo'llar orasida xato qiladi. Real aniqlik 80–90% atrofida bo'ladi, shuning uchun «tekshirish kerak» signali, «xato» hukmi emas.
- Shaxsiy ma'lumotlar: kamera faqat stolni ko'rsin, yuzni emas; xodimlar roziligi yozma olinsin.

## Bosqichlar
0. Video sinov (pulsiz): egasi tanish lavashxonada stol ustidan 10–15 daqiqa telefon video yozadi; Claude prototipni shu videoda sinaydi.
1. Prototip (Claude yozadi): kadrdan ingredientlarni aniqlash, retsept chek-listi, natija ekrani, Telegram bot orqali menejerga xabar va kunlik hisobot.
2. Pilot (1 lavashxona, 2–4 hafta): arzon IP kamera + eski noutbuk/mini-kompyuter; natijalarni o'lchash.
3. Sotish: pilot raqamlari bilan («bir oyda N ta lavash tekshirildi, M ta xato topildi»).

## Kim nima qiladi
- Claude: dastur, model sozlash, bot/hisobot, sotuv taqdimoti, narx hisob-kitobi, video.
- Egasi: lavashxona topish, kelishuv, kamera o'rnatish (yoki usta), joyida sinov, pul sarflari haqida qaror.

Holat: 🟡 egasi qaror qiladi (pilot uchun lavashxona va sinov video kerak).

## Soddaroq variant (egasining fikri, 2026-10-15)
Egasi: 200–300 ming so'mlik Wi-Fi kamera yetmaydimi? Avval telefon video bilan sinab ko'rish.

Xulosa: **video emas, rasm**. Har bir lavash o'ralishidan oldingi bitta kadr yetadi. Rasm Claude'ga (bizning bot/Vercel) yuboriladi, u retsept bilan solishtiradi, natija menejerning Telegramiga.

Uch daraja (sodda → murakkab):
1. **Foto-bot (uskunasiz)**: oshpaz yoki kassir ochiq lavashni telefonda suratga olib botga yuboradi (bot rasmni allaqachon tushunadi). Hammasini emas, har 10 tadan birini yoki smena boshida. Narx: faqat API.
2. **Eski telefon = kamera**: eski Android telefon ushlagichda stol ustida, bizning kichik veb-sahifa har necha soniyada yoki harakat bo'lganda rasm oladi va yuboradi. Qo'shimcha kompyuter kerak emas.
3. **Arzon Wi-Fi kamera (200–300 ming)**: faqat **RTSP** qo'llasa ishlaydi (masalan, Tapo, Imou'ning ko'p modellari; Xiaomi'ning ko'pchiligi faqat o'z ilovasida ko'rsatadi). Kamerani o'qib, rasm yuboradigan qurilma (eski telefon yoki noutbuk) baribir kerak.

Telefon video sinovi: egasi stol ustidan 10–15 daqiqa video oladi → Claude kadrlarni o'zi ko'rib, ingredientlar ko'rinadimi tekshiradi → ishlasa 1-darajadan boshlaymiz.
- 2026-10-15: egasi 2026-10-16 da uyda kamerada lavash videosini va lavash menyusini beradi. Bot 2026-10-16 soat 20:00 da eslatadi.
