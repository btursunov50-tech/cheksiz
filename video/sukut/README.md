# «G'azabda sukut»
Ssenariy: `ideas/g4-goyalar.md` (4-bo'lim). Rasm promptlari: `rasm_promptlar.py` → `sahnalar.html` (https://claude.ai/artifact/LkUnPRmoViLFuYxqhwAXNG).
Tasdiqlangan rasmlar (2026-11-08): ref_man (avtobusdagi odam), s01–s08 (zaxira s02_v2, s05_v1 — oyoq kiyim bilan so'rida, ishlatilmaydi).
Eslatmalar: 7-sahnada fondagi avtobus tablosi xira, o'qilmaydi; 5-sahnada Diyor qo'li allaqachon ko'ksida — Veo'da o'rnidan turib boshqa so'riga o'tadi; 8-sahnada telefon tokchada, keyin choy quyadi.

## Kliplar (Veo, 720×1280, 8 s, belgisiz) — 2026-11-08
| Sahna | Holat | Izoh |
|---|---|---|
| 1 | ✅ | Yuz o'zgarmaydi; jahl ikkilanishga o'tadi, barmoq tegmaydi |
| 2 | ✅ | Odam baqiradi (namunaga mos), Diyor xotirjam; ko'z yumishi sezilarli emas |
| 3 | ✅ | Hamkasbi kinoyadan ko'ra do'stona jilmayadi (kichik), Diyor jilmayib ishlaydi; push-in |
| 4 | ✅ | Telefonni skameykaga qo'yadi, daraxtlarga qaraydi |
| 5 | ✅ birlashtirildi | `clips/s05.mp4` (7.0 s) = `s05b` 0–3.0 s (bosh egadi, choy ichadi) + `s05a` 2.4 s dan (so'ridan tushadi, o'ngga ketadi); 5–6 s da sekin zoom — Diyor kadrdan chiqadi, oxiri bahslashayotgan ikki kishi. `s05a` oxirida Diyor so'ri ustida oyoq kiyimda yurardi — kesildi |
| 6 | ✅ | Rahbar qog'ozni stolga qo'yib baqiradi, Diyor xotirjam (yon tomondan) |
| 7 | ✅ | Odam namunaga mos; ikkilanib, keyin qo'l qisadi, Diyor jilmayadi |
| 8 | ✅ | Kiradi, onasini quchoqlab yuzidan o'padi, o'tirib to'la piyoladan ichadi; yuz yosh, namunaga mos. Zaxira s08_v2 (onasi ham choy ichadi) |
Hamma 8 sahna klipi tayyor (2026-11-08). Keyingi: hikoyachi ovozi.

Oyatlar (egasi 2026-11-08): ekranda sura nomi va oyat raqami YOZILMAYDI; faqat ma'nosi va ostida «Qur'oni Karimdan». Post matnlarida ham shunday.

## Ekrandagi oyat ma'nolari (raqamsiz, ostida «Qur'oni Karimdan») — egasi tekshiradi
| Sahna | Matn (manba faqat ichki eslatma) |
|---|---|
| 2 | «...g'azabini ichiga yutuvchi va odamlarni afv etuvchilar. Alloh yaxshilik qiluvchilarni sevadi.» (Oli Imron 134) |
| 3 | «Yomonlikni eng go'zal yo'l bilan qaytaring: shunda sen bilan adovatli kimsa go'yo qadrdon do'stdek bo'lib qoladi.» (Fussilat 34) |
| 4 | «Johillar ularga xitob qilsa, «Salom» deydilar.» (Furqon 63) |
| 5 | «Behuda so'zni eshitsalar, undan yuz o'giradilar.» (Qasas 55) |
| 6 | «Sabr va namoz bilan yordam so'rang. Albatta, Alloh sabr qiluvchilar bilandir.» (Baqara 153) |
| 7 | «Afv yo'lini tuting, yaxshilikka buyuring va johillardan yuz o'giring.» (A'rof 199) |
| 8 | «Afv etsinlar va kechirsinlar. Alloh sizni mag'firat qilishini istamaysizmi?» (Nur 22) |
Bot kartasidan oldin ovozsiz karta: «Bu so'zlar Qur'oni Karimdan olingan».

Egasi (2026-11-09): oyatlar sahnalar ostida emas (subtitr bilan ekranni yopib qo'ydi); hikoyadan keyin (~0:49) 7 ta oyat alohida-alohida kartada, sura nomi va oyat raqami bilan. «Qur'oni Karimdan olingan» kartasi olib tashlandi.

## Musiqa
«Kafeda inson va robot» (`video/robot/music/kafeda_inson_va_robot.mp3`, boshidan). Egasi 2026-11-09 da 3 ta namunadan B ni tanladi (Dutar's Whisper va The Silk Road yoqmadi).

## Tayyor (2026-11-09)
`python3 video/sukut/build.py <work> uz|ru|en` → uch til; ovoz o'zbekcha, yozuvlar (subtitr, oyat, bot kartasi, avatar savoli) tarjima. Fayllar `video/final/sukut/`, matnlar `POSTS.md`, joylash kuni 23-noyabr. Bot mavzusi «jahl chiqargan xabarga xotirjam javob» `bot/knowledge.js` ga qo'shildi.
