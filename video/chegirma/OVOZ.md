# «70 foiz chegirma» — Manus ovoz bloki (2026-10-27, batafsil versiya)

Ssenariy: `ideas/chegirma.md`. Hook (1-qator) EN balli 100.0. Ovozlar «Sovg'a yutdingiz!» va «Oyiga atigi…» dagi bilan bir xil (seriya): Manus'ga namuna sifatida `video/oyiga/dialog.wav` biriktiriladi. 10–12-qatorlar — egasi qo'shgan hazil (o'tib ketayotgan qiz). 15-qator — avatar savoli Usta ovozida (`timeline.AV_LINE`).

```
VAZIFA
O'zbekcha qisqa video (mini-drama, 9:16, YouTube Shorts / Instagram Reels) uchun ikki kishilik ovoz yozuvini yasab ber. Qahramonlar: USTA va DIYOR. Bu seriyaning 3-qismi ("Sovg'a yutdingiz!" va "Oyiga atigi" dan keyin), qahramonlar o'sha-o'sha, ovozlari ham o'sha-o'sha bo'lishi shart.

NAMUNA OVOZ (juda muhim)
Biriktirilgan "dialog.wav" — oldingi qism ("Oyiga atigi"). Unda USTA (past, chuqur ovoz) va DIYOR (yosh, balandroq ovoz) gaplashadi. Ikkala ovozni AYNAN shu namunadagidek qil: o'sha tembr, o'sha yosh, o'sha gapirish tezligi. Tomoshabin "bular o'sha Usta va Diyor-ku" deb tanishi kerak. Yangi ovoz o'ylab topma.

NATIJA (ikkalasi ham kerak)
1. Bitta umumiy WAV fayl: 15 ta qator tartib bilan, har qatordan keyin aniq 1 soniya jimlik. Nomi: chegirma_dialog.wav
2. Har bir qator alohida WAV fayl: 01_usta.wav, 02_diyor.wav, 03_usta.wav, 04_diyor.wav, 05_usta.wav, 06_diyor.wav, 07_usta.wav, 08_usta.wav, 09_diyor.wav, 10_usta.wav, 11_diyor.wav, 12_usta.wav, 13_usta.wav, 14_usta.wav, 15_usta.wav
Format: WAV, 44.1 kHz yoki 48 kHz, mono. Musiqa yo'q, ovoz effekti yo'q, fon shovqini yo'q, aks-sado (reverb) yo'q — toza studiya ovozi. Har qator boshida va oxirida ortiqcha jimlik bo'lmasin (umumiy fayldagi 1 soniyadan tashqari).

TIL VA O'QISH QOIDALARI
- Til: o'zbek tili (lotin yozuvi), tabiiy toshkentcha talaffuz. Rus yoki turk talaffuzi emas.
- Qatorlarni AYNAN yozilganidek o'qi: so'z qo'shma, so'z tashlama, tarjima qilma, o'z so'zing bilan aytma.
- Kvadrat qavs ichidagi yozuvlar [...] faqat rejissyor ko'rsatmasi: ularni ovoz chiqarib o'qima.
- "..." (uch nuqta) — gap orasida qisqa to'xtash (0.3–0.5 soniya), ikkilanish.
- Tezlik: 1.0x (oddiy suhbat tezligi). Qavsdagi "~5 s" — shu qator taxminan qancha davom etishi kerak; juda tez yoki juda sekin bo'lmasin.
- Uslub: kino. Ikki tirik odam ko'chada va do'konda gaplashayotgandek, matn o'qib berayotgandek EMAS. Jilmayish, kulgi, hayajon ovozdan eshitilsin.
- O'zbek harflari: o' va g' aniq aytilsin (to'lash, yorlig'i, ko'zing, o'ttiz), "q" chuqur (qancha, qirq, qidiryapsan), "x" bo'g'iz tovushi (xarid, xotirjam).

QAHRAMON 1: USTA
- Kim: 30-35 yoshlardagi erkak, do'ppi va to'n kiygan, hayotni ko'rgan, aqlli ustoz. Diyorning yaqin akasidek.
- Ovozi: past (bas-bariton), chuqur, iliq, sokin, ishonchli. Namunadagi Usta ovozi.
- Gapirishi: shoshilmaydi, so'zlarini o'ylab aytadi, muhim so'zdan oldin qisqa to'xtaydi. Hech qachon baqirmaydi. Hazil qilganda ovozida kulgi bor, lekin masxara qilmaydi.
- Butun yozuv davomida ovozi bir xil qolsin (15-qatorgacha).

QAHRAMON 2: DIYOR
- Kim: 20-22 yoshlardagi sodda, quvnoq, yaxshi niyatli yigit. "Chegirma" so'zini eshitsa darhol ishonadi, lekin tez tushunadi.
- Ovozi: Ustanikidan aniq balandroq va yengilroq, yosh, tiniq. Namunadagi Diyor ovozi. Bola ovozi emas — yigit ovozi.
- Gapirishi: tezroq, hissiyoti ovozidan darhol bilinadi: hayajonlansa tezlashadi va ovozi ko'tariladi, uyalsa sekinlashadi va pasayadi.
- Butun yozuv davomida ovozi bir xil qolsin.

MUHIM: USTA va DIYOR ovozlari bir-biriga umuman o'xshamasin — eshitgan odam darhol farqlasin.

TALAFFUZ (aniq aytilsin)
- "@sahiychishopbot" = "sahiychi shop bot" — uchta so'z, har biri aniq, "sahiychi" so'zida urg'u oxirgi bo'g'inda: sa-hiy-CHI.
- Raqamlar so'z bilan: "yetmish", "uch yuz ming", "bir yuz yetmish ming", "bir yuz o'ttiz ming", "qirq uch".
- "foiz" — "fo-iz" (ikki bo'g'in).

QATORLAR (rejissyor ko'rsatmasi + matn)
1. USTA [sahna: do'kon oldida, tomoshabinga qarab. Sokin, sirli, bilimdon; birinchi gapdan keyin 0.5 s to'xtab, ikkinchi gapni maslahat ohangida; urg'u: "emas", "hisoblang"; ~5 s]: Bu yetmish foizlik chegirma yetmish foiz emas. To'lashdan oldin hisoblang.
2. DIYOR [sahna: chegirmani ko'rib yugurib keladi. Juda hayajonli, nafasi tiqilib, tez; "qarang!" baland; raqamlarni quvonch bilan; oxirgi gapda vahima: "yutqazaman!"; ~5.5 s]: Usta, qarang! Uch yuz ming edi, bir yuz yetmish ming bo'libdi! Hozir olmasam, yutqazaman!
3. USTA [sahna: do'kon ichi, qo'llari qovushtirilgan. Xotirjam, ozgina jilmayib, oddiy lekin o'tkir savol; urg'u: "oldin ham"; ~3.5 s]: Bu narsani chegirmani ko'rishdan oldin ham qidirayotgan edingmi?
4. DIYOR [sahna: qotib qoladi. Hayajoni so'nadi; "Yo'q..." dan keyin to'xtab, sekin, uyalib, ovozi pasayib; ~3 s]: Yo'q... Chegirmani ko'rib qoldim.
5. USTA [sahna: yorliqni ko'taradi, ostidan haqiqiy foiz chiqadi. "Hisoblaylik" — sekin, o'qituvchidek; raqamlarni birma-bir, har biridan keyin qisqa to'xtab; oxirgi gapda ozgina kinoya va jilmayish; urg'u: "yetmish emas", "qirq uch"; ~7 s]: Hisoblaylik. Uch yuz mingdan bir yuz o'ttiz ming tushgan. Bu yetmish emas, qirq uch foiz.
6. DIYOR [sahna: barmog'ida sanaydi. Hayron, biroz norozi, savol ohangida ovozi ko'tarilib; urg'u: "nega"; ~2.5 s]: Unda nega yetmish deb yozishgan?
7. USTA [sahna: kassadagi taymer yonida, kaftini ko'rsatib "shoshilma" deydi. Yumshoq, tushuntiruvchi, dono; birinchi gapda "ko'zni" va "qo'lni" ni ajratib; ikkinchi gap sekin va ishonchli; ~6 s]: Katta raqam ko'zni, taymer qo'lni shoshiltiradi. Kerakli narsa shoshilishni talab qilmaydi.
8. USTA [sahna: uchta barmog'ini ko'rsatadi. Aniq, ishonchli; "Uchta tekshiruv" dan keyin 0.5 s to'xtash; har savoldan keyin qisqa to'xtash; oxirgi savol — eng muhimi, sekinroq va mehr bilan; ~9 s]: Uchta tekshiruv. Boshqa do'kondagi narxi qancha? O'lchami, sifati, kafolati bir xilmi? Va shu mahsulot senga kecha ham kerakmidi?
9. DIYOR [sahna: do'kondan chiqib keladi, mamnun. Xotirjam, jilmayib, o'ziga ishongan holda; ~3 s]: Demak, avval hisoblayman, keyin olaman.
10. USTA [sahna: ko'chada chiroyli qiz o'tib ketadi, Diyor qarab qoladi; Usta yelkasiga uradi. Hazil, kulgi aralash, do'stona tanbeh; "Hoy-hoy" cho'zib, quvnoq; savol oxirida kulgi; ~4 s]: Hoy-hoy, Diyor! Sen do'konda chegirma qidiryapsanmi yoki ko'chada kelin?
11. DIYOR [sahna: cho'chib tushadi, yuzi qizaradi. Shoshib, uyalib, so'zlari chalkashib, har "..." da duduqlanib; oxirgi so'z tez va baland, o'zini oqlab; ~2.5 s]: Yo'q, usta... men... hisoblayapman!
12. USTA [sahna: kulib, chakkasiga barmog'ini tegizadi. Kulib, mehribon tanbeh; birinchi gap maslahat, ikkinchisi hazil bilan, ritmli: "Avval hisob, — keyin kelin!"; ~4 s]: Ko'zing narxda bo'lsin, ukam. Avval hisob, keyin kelin!
13. USTA [sahna: yaqin plan, kameraga qarab. Iliq, sokin, hikmat aytayotgandek; "foiz emas" va "ehtiyoj" ni ajratib; ~3.5 s]: Xaridni foiz emas, ehtiyoj hal qilsin.
14. USTA [sahna: telefonni tomoshabinga uzatadi. Do'stona, tomoshabinga to'g'ridan-to'g'ri murojaat, reklama ohangisiz, maslahat beruvchi; "sahiychi shop bot" ni sekin va aniq; ~9 s]: Chegirma yorlig'ini suratga olib botimizga yuboring: @sahiychishopbot. Haqiqiy foizni hisoblab, nimani tekshirishni aytib beradi.
15. USTA [sahna: oxirgi savol tomoshabinga. Iliq, qiziqib so'rayotgan ohangda; "Siz-chi?" dan keyin 0.5 s to'xtash; "Izohga yozing!" quvnoq; ~4 s]: Siz-chi? Eng katta chegirmangiz qancha edi? Izohga yozing!

OXIRIDA TEKSHIR
- 15 ta qator bor, hammasi aynan matndagidek, qavsdagi ko'rsatmalar o'qilmagan.
- Usta va Diyor ovozlari namunadagidek va bir-biridan aniq farq qiladi.
- Umumiy faylda har qatordan keyin 1 soniya jimlik, musiqa va shovqin yo'q.
```

## Video vaqtlari (taxminiy; ovoz kelgach aniqlanadi)

| Sahna | Klip (olinadigan qism) | Qator | Kadr |
|---|---|---|---|
| 1 | s01_y (0–8 s) | 1 Usta | Banner «-70%», «300 000», «170 000» |
| 2 | s02 (0–8 s) | 2 Diyor | Hayajonda, bannerga ko'rsatadi |
| 3 | s03 (0.3–5 s) | 3 Usta | Do'kon ichi, qo'llari qovushtirilgan |
| 4 | s04 (0–3.5 s) | 4 Diyor | O'ylanib qoladi |
| 5 | s05_y (0–8 s) | 5 Usta | «-70%» yorliq tushadi, ostidan «-43%» (sekinlashuv + zarba) |
| 6 | s06 (0–2.6 s) | 6 Diyor | Barmog'ida sanaydi |
| 7 | s07_y (0–8 s) | 7 Usta | Taymer «00:59:59» |
| 8 | s08 (0–8 s, ~1.15x) | 8 Usta | 3 barmoq, 3 belgi |
| 9 | s09 (0–2.7 s) | 9 Diyor | Do'kondan chiqadi |
| 10 | s10 (0–2.4 s) | — | Qiz o'tib ketadi, Diyor qarab qoladi |
| 10b | s10b (0–8 s) | 10 Usta + 11 Diyor | Usta yelkasiga uradi, Diyor uyaladi |
| 10c | s10c (2.3–5.5 s, ~1.25x) | 12 Usta | Usta chakkasiga barmoq tegizadi |
| 11 | s11 (0–8 s) | 13 Usta | Yaqin plan |
| 12 | s12 (0–7.6 s) | 14 Usta | Telefon, @sahiychishopbot |
| — | avatar | 15 Usta | Avatar + plashka (avatar shu qatorga cho'ziladi) |
| — | yakuniy karta | — | 4 s |
