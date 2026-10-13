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

## Allaqachon qurganimizdan chiqadigan yangi xizmatlar (narxini egasi belgilaydi)

| Xizmat | Bizda tayyor | Kimga |
|---|---|---|
| Telegram kanal uchun har kungi avto-post (ertalabki tabrik, kun maslahati, aksiya) | `api/tong.js` (har kuni 05:00, video + matn) | Do'kon, kafe, o'quv markaz kanallari |
| Kanal postlarini guruhlarga avtomatik tarqatish | `bot/groups.js` | Bir nechta guruhi bor bizneslar |
| Demo rejimli bot (sotuvdan oldin ko'rsatish) | `bot/demo.js` | Har bir mijozga taklif paytida |
| Trend video 24 soatda (fakt tekshiruvi, subtitr uz/ru/en) | `video/` quvuri | Brendlar, bloggerlar |
| Arabcha/inglizcha bot va reklama (Ko'rfazdagi diaspora bizneslari) | Bot 16 til biladi | Saudiya, BAA, Qatardagi kichik biznes |
