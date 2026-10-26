# «Oyiga atigi…» — kuchaytirilgan ssenariy (2026-10-26)

Asos: `ideas/diyor-usta.md`, 3-ssenariy. Format: tik 9:16, ~75 s, mini-drama. Qahramonlar: **Diyor** (sodda yigit) va **Usta** (~30 yosh, sokin), «Sovg'a yutdingiz!» dagi o'sha ikkovi (`video/sovga/img/ref_*`). Raqamlar misol, fakt emas; biror bank yoki do'kon nomi aytilmaydi.

O'zgarishlar (asl matnga nisbatan):
- Hook: «Oyiga atigi yuz ming. Lekin jami qanchaligini hech kim aytmadi.» (EN 100.0, `hookscore.py`; asl «Telefon yoqdi! Oyiga atigi…» kuchsiz).
- Ko'rinadigan burilish: vitrinada «100 000/oy» katta, jami summa mayda; Usta lupa bilan mayda yozuvni kattalashtiradi.
- Diyor hisoblaydi va qo'shimcha to'lovlar (boshlang'ich to'lov, xizmat haqi) birma-bir qo'shilib, son o'sib boradi.
- Oxirida aniq foyda: sotuvchiga beriladigan 3 savol.
- Botga chaqiriq mavzuga mos (`bot/knowledge.js`, «Installments»).

## Sahnalar

| # | Nima ko'rinadi | Gap |
|---|---|---|
| 1 | Telefon do'koni vitrinasi: «100 000 so'm/oy» katta, ostida mayda yozuv | **Usta:** «Oyiga atigi yuz ming. Lekin jami qanchaligini hech kim aytmadi.» |
| 2 | Diyor telefonni ushlab quvonadi | **Diyor:** «Usta, oyiga atigi yuz ming ekan! Bemalol olaman.» |
| 3 | Usta lupa bilan mayda yozuvni kattalashtiradi: «12 oy» | **Usta:** «Necha oyga? Jami qancha to'laysan?» |
| 4 | Diyor barmoqlarida sanaydi, havoda raqamlar chiqadi | **Diyor:** «Yuz ming… o'n ikki oy… bir million ikki yuz ming.» |
| 5 | Ekranda raqam o'sadi: + boshlang'ich to'lov, + xizmat haqi | **Usta:** «Bunga boshlang'ich to'lov, xizmat haqi qo'shilsa-chi?» |
| 6 | Diyor sotuvchiga qaraydi, sotuvchi faqat «100 000» ni ko'rsatadi | **Diyor:** «Sotuvchi faqat oylik to'lovni aytdi. Naqd narxini so'ramabman.» |
| 7 | Usta tarozi: bir pallada «naqd narx», bir pallada «jami to'lov» | **Usta:** «Kichik bo'lingan narx katta summani yashiradi. Ikkalasini yonma-yon qo'y.» |
| 8 | Ekranda 3 savol birma-bir chiqadi: 💵 naqd narx · 🧾 jami summa · ⚠️ kechiksam jarima | **Usta:** «Uchta savol ber: naqd narxi qancha? Jami qancha to'layman? Kechiksam nima bo'ladi?» |
| 9 | Diyor telefonni vitrinaga qaytarib qo'yadi, jilmayadi | **Diyor:** «Shoshilmayman. Avval hisoblab ko'raman.» |
| 10 | Usta kameraga qaraydi | **Usta:** «"Oyiga atigi" degandan keyin bitta savol qoladi: oxirida jami qancha?» |
| 11 | Usta telefonda: narx yorlig'i surati botga ketadi, bot jami summani yozadi. Katta yozuv **@sahiychishopbot** | **Usta:** «Narx yorlig'i yoki shartnoma suratini botimizga yuboring: @sahiychishopbot. Jami qancha to'lashingizni hisoblab, sotuvchiga qaysi savollarni berishni aytib beradi.» |
| — | Avatar, plashka: «Siz nasiyaga nima olgansiz? Izohga yozing!» | — |
| — | Yakuniy karta | — |

Sekinlashuv (1 marta): 5-sahnada raqam o'sib borganda, oxirgi raqam «tushganda» tanga ovozi.

## Hook variantlari (EN, `hookscore.py`)
| Hook | Ball |
|---|---|
| «Oyiga atigi yuz ming. Lekin jami qanchaligini hech kim aytmadi.» (One hundred thousand a month. But nobody told you the total.) | **100.0** ✅ |
| «To'xta. Nasiyaga olishdan oldin bitta savol ber: jami qancha?» | 84.2 |
| «Sotuvchi oylik narxni aytdi. Jamisini emas.» | 62.2 |

Holat: 📝 ssenariy, egasi tasdig'ini kutmoqda.
