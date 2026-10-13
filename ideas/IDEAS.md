# G'oyalar banki

Egasi yuborgan videolar, postlar va savollardan olingan saboqlar. Har yozuvda: nima ekan, haqiqatmi, bizga nima foyda, keyingi qadam.
Holat: ✅ qilindi · 🟡 taklif (egasi qaror qiladi) · ❌ kerak emas.

## Saboqlar (2026-10-12)

| # | Manba | Nima | Haqiqat | Bizga foyda | Holat |
|---|---|---|---|---|---|
| 1 | Instagram skill videosi | Claude uchun 13 ta Instagram ko'nikmasi (MIT) | Ishlaydi | Hook ball (`hookscore.py`), caption, DM. Hooklarimiz 43–49 dan 78–86 ga chiqdi | ✅ `.claude/skills/ig-*` |
| 2 | FreeLLMAPI videosi («800 mln bepul token») | 34 ta bepul AI tarifini bitta joyga yig'adigan dastur | Qisman. Kuchli modellar yo'q, doim yoqilgan kompyuter kerak, bepul video amalda yo'q (Pollinations 2026-07-10 dan pullik) | Botga mos emas. Faqat egasining bepul qoralamalari uchun | ❌ |
| 3 | Shu video oxiri | «TOKEN deb yozing, havolani yuboraman» usuli | Izoh sonini oshiradi | Bizning postlarda: «BOT deb yozing, demo havolasini yuboraman» | 🟡 |
| 4 | Telegram post: «Reset for free» | Claude limitini bir marta bepul tiklash (22-oktabrgacha) | To'g'ri | Egasi ishlatdi | ✅ |
| 5 | «Arabistonda AI ish ko'p» | Ko'rfazda AI e'lonlari 3 baravar o'sgan | Asosan tajribali dasturchilar uchun | Ko'chish emas, u yerdagi mijozlarga masofadan xizmat. Bot va sayt arabchani allaqachon biladi. U yerda WhatsApp asosiy | 🟡 |
| 6 | MrBeast trendi | Kun mavzusidagi tezkor yangilik videosi | 1-videomiz 1 kunda ~1400 ko'rish oldi | Trend videolar ko'p ko'riladi. Fakt tekshirish va yuz xiralashtirish bilan | ✅ |
| 7 | Ruscha dars «Забудь монтаж» (32 daq., 2026-10-13) | Ingliz tilida uzun (20 daq.) yuzsiz YouTube kanali: NexLev konnektori Claude'ga raqobatchilar statistikasini beradi, Claude g'oya, sarlavha va ssenariy yozadi, Vidrush videoni yig'adi | Usul real (raqobatchilarning «autlayer» videolarini tahlil qilish). $130 000 daromadni tekshirib bo'lmaydi; muallif o'z nisha saytini va xizmatlarni reklama qiladi. Narx: NexLev €13–42/oy, Vidrush $99/oy (kutish ro'yxati). YouTube 2025-iyuldan «inauthentic content» qoidasi bo'yicha shablon bilan ommaviy yasalgan AI kanallarni monetizatsiyadan chiqaradi | Pul sarflamasdan olamiz: 4 bosqichli prompt tartibi (tahlil → formula → 10 g'oya → sarlavha → ssenariy). Egasi raqobatchilar skrinshotini yuboradi, tahlilni men qilaman | 🟡 |
| 8 | Ruscha video: telefon fermasi (2026-10-13) | Yuzlab soxta Instagram/TikTok akkauntlar: antidetekt brauzer, proksi, virtual raqamlar, sotib olingan akkauntlar ($40), bir videoni tezlik/kesish bilan «noyob» qilib ommaviy joylash | Platformalar qoidasini buzadi (soxta akkaunt, spam, cheklovni chetlab o'tish). Videoning o'zida ham akkaunt bloklangani ko'rsatiladi. Daromad grafiklari tekshirib bo'lmaydigan reklama | Ferma qilmaymiz. Halol qismini olamiz: bitta videodan har platforma uchun alohida versiya (allaqachon qilyapmiz) va bir mavzuga 2–3 xil hook bilan versiya qilib, qaysi biri yaxshi ishlashini sinash | ❌ (halol qismi 🟡) |
| 9 | Ruscha Reels: Bob Proctor «Kimsiz?» intervyusi (2026-10-13) | Eski TV intervyu (sepiya, VHS), o'rtada so'zma-so'z katta subtitr, bitta falsafiy savol | Format ishlaydi: savol-hook + obro'li ovoz + ritmik subtitr. Lekin kadrlar birovniki (Content ID), real odamning yuzi/ovozini AI bilan yasamaymiz | Formatni olamiz: «Siz kimsiz? Ismingiz emas. Kasbingiz ham emas.» (hook 81.4) → biznes egasi bir xil savolga javob beradigan «mashina» emas → AI bot. To'qima retro boshlovchi (Veo) + bot demo ekran yozuvi | 🟡 ssenariy berildi |
| 10 | YouTube Shorts (youtu.be/DhsydObgwG8) asosida yozilgan ssenariy «AI aytilmagan gaplarni tarjima qiladi» (2026-10-13) | Ota va o'g'il janjallashadi, AI har bir qo'pol gapning tagidagi haqiqiy hisni ekranga chiqaradi, oxiri yarashuv | Videoni ochib bo'lmadi (YouTube bu yerda yopiq), faqat ssenariy o'qildi. Bank ilovasini AI ochishi va «AI botimiz hislarni tushunadi» degan reklama gapi noto'g'ri va'da, qo'rquvni kuchaytiradi | «Nusxa»ning juftligi: u yerda AI xavf, bu yerda AI yaxshi tomondan. Bir xil chizma uslub va oila. Hook «“Ishlagan pulingni stolga qo'y!” Dadam buni nazarda tutmagan edi.» (EN 83.0) | 🟡 Saqlandi: `ideas/aytilmagan-gaplar.md`, bot 2026-10-17 da eslatadi |

## Allaqachon qurganimizdan chiqadigan yangi xizmatlar (narxini egasi belgilaydi)

| Xizmat | Bizda tayyor | Kimga |
|---|---|---|
| Telegram kanal uchun har kungi avto-post (ertalabki tabrik, kun maslahati, aksiya) | `api/tong.js` (har kuni 05:00, video + matn) | Do'kon, kafe, o'quv markaz kanallari |
| Kanal postlarini guruhlarga avtomatik tarqatish | `bot/groups.js` | Bir nechta guruhi bor bizneslar |
| Demo rejimli bot (sotuvdan oldin ko'rsatish) | `bot/demo.js` | Har bir mijozga taklif paytida |
| Trend video 24 soatda (fakt tekshiruvi, subtitr uz/ru/en) | `video/` quvuri | Brendlar, bloggerlar |
| Arabcha/inglizcha bot va reklama (Ko'rfazdagi diaspora bizneslari) | Bot 16 til biladi | Saudiya, BAA, Qatardagi kichik biznes |
