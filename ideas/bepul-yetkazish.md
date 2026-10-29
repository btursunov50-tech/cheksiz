# «Bepul yetkazish» — Baron formatida Diyor & Usta (2026-10-29)

Asos: `ideas/diyor-usta.md` 1-ssenariy (egasining PDF'i) + Baron formati (`ideas/IDEAS.md` 23-qator): sodda ishonch → «Jim, Diyor. Qara.» → tasdiqlangan tarixiy fakt → «kim foyda ko'radi?» → botga chaqiriq. Kompaniya va olim nomlari videoda aytilmaydi.

## Ssenariy (~75 s, 9:16)
| # | Kadr | Gap |
|---|---|---|
| 1 | Usta yaqin plan, kameraga; orqada Diyor telefonda xarid qilyapti | **Usta:** «Bepul yetkazish bepul emas. Uning pulini baribir to'laysan.» |
| 2 | Diyor telefon ekranidagi savatga qaraydi | **Diyor:** «Usta, shampun oldim, yetkazish yigirma ming ekan. Yana qirq minglik narsa qo'shsam, bepul bo'larkan!» |
| 3 | Usta qoshini ko'taradi | **Usta:** «Diyor, o'sha qirq minglik narsa senga kerakmi?» — **Diyor:** «Unchalik emas… lekin bepul-ku!» |
| 4 | Usta qo'lini ko'taradi, kadr eski rangga o'tadi | **Usta:** «Jim, Diyor. Qara. 2002-yil, Amerika.» |
| 5 | Eski ofis, ekranlarda buyurtmalar ko'payadi (yuzlar xira) | **Usta:** «Dunyodagi eng katta onlayn do'kon bepul yetkazishni 99 dollardan 49 dollarga, ikki oydan keyin 25 dollarga tushirdi.» |
| 6 | Savatlarga narsalar qo'shilib ketadi | **Usta:** «Odamlar chegaraga yetish uchun savatga yana narsa qo'shdi. Do'kon buni “ijobiy natija” deb e'lon qildi.» |
| 7 | Diyor ko'zi katta | **Diyor:** «Bizni sanashgan ekan-da?!» |
| 8 | Ekranda xarita: hamma mamlakatda yashil strelka yuqoriga, bitta mamlakatda — yo'q | **Usta:** «Faqat Fransiyada yetkazish uchun bir frank, ya'ni yigirma sent olishgan. U yerda sotuv deyarli o'smagan.» |
| 9 | O'sha mamlakatda «0» paydo bo'ladi, strelka yuqoriga | **Usta:** «Narxni nolga tushirishgan zahoti, u yerda ham sotuv o'sib ketdi.» |
| 10 | Stolda ikki shokolad: qimmat va arzon (yorliqsiz, brendsiz) | **Usta:** «Olimlar sinab ko'rgan: qimmat shokoladni ko'pchilik tanlagan. Arzonini “bepul” qilishgan zahoti — hamma bepuliga o'tgan.» |
| 11 | Diyor savatiga qaraydi | **Diyor:** «Demak, “bepul” so'zi miyani aldaydi?» — **Usta:** «Aldamaydi. Shoshiltiradi.» |
| 12 | Ekranda hisob: 20 000 tejadi → 40 000 sarfladi | **Usta:** «Hisobla: yigirma ming tejading, qirq ming sarflading.» |
| 13 | 3 belgi birma-bir: 🛒 · 📅 · ❓ | **Usta:** «Uchta qoida. Faqat kerakli narsani ol. Yaqinda baribir oladigan narsalarni bitta buyurtmaga yig'. Va so'ra: yetkazish pullik bo'lmaganida ham shuni olarmidim?» |
| 14 | Usta yaqin plan, kameraga | **Usta:** «Ular senga yetkazishni emas, “tekin” degan tuyg'uni sotadi. Har gal so'ra: bundan kim foyda ko'radi?» |
| 15 | Usta telefonda bot, katta **@sahiychishopbot** | **Usta:** «Savatingizdagi narsalarni va yetkazish shartini botimizga yozing: @sahiychishopbot. Bepul yetkazish uchun ortiqcha qancha to'layotganingizni hisoblab, nimani olib tashlash mumkinligini aytadi.» |
| — | Avatar + plashka | **Usta (ovoz):** «Siz-chi? Bepul yetkazish uchun keraksiz narsa olganmisiz? Izohga yozing!» |

Hook (1-qator) EN: «Free delivery is not free. You still pay for it.» — **87.0** (`hookscore.py`).

## Faktlar (tekshirildi, 2026-10-29)
- 2002-yil 18-iyun: onlayn do'kon bepul yetkazish chegarasini $99 → $49 ga tushirdi (sinov); 26-avgust: $49 sinovining ijobiy natijasini aytib, $25 ga tushirdi. Manba: do'konning o'z press-relizlari (press.aboutamazon.com, 2002-06 va 2002-08), ecommercetimes.com.
- Fransiya: boshqa mamlakatlarda bepul yetkazish bilan sotuv o'sgan, Fransiyada bir frank (~20 sent) olingan va o'smagan; bepul qilinganda o'sgan. Manba: Dan Ariely, «Predictably Irrational» (2008), 3-bob; cardinalpath.com, customerthink.com (kitobdan iqtibos). Aniq chegara summasi manbalarda farq qiladi ($30 / $31.90), shuning uchun videoda aytilmaydi.
- Shokolad tajribasi: qimmat trufel 15 sent vs arzon shokolad 1 sent → ko'pchilik trufelni tanlagan; ikkalasi 1 sentga arzonlashtirilganda (14 sent vs 0) ko'pchilik bepuliga o'tgan. Manba: Shampanier, Mazar, Ariely, «Zero as a Special Price», Marketing Science, 2007.
- Videoda raqamlar (20 000, 40 000 so'm) — misol.

## Botga chaqiriq
`bot/knowledge.js` ga mavzu qo'shiladi (videoni yig'ish PR'ida): savat + yetkazish sharti → ortiqcha xarajat hisobi, nimani olib tashlash mumkin.
