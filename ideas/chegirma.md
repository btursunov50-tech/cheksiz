# «70 foiz chegirma» — kuchaytirilgan ssenariy (2026-10-27)

Asos: `ideas/diyor-usta.md`, 2-ssenariy. Format: tik 9:16, ~70 s, mini-drama. Qahramonlar: **Diyor** va **Usta** (seriya, `video/sovga/img/ref_*`). Raqamlar misol; hech bir do'kon nomi yo'q.

O'zgarishlar (asl matnga nisbatan):
- Asl matndagi raqamlar o'zi tuzoq: 300 000 → 170 000 bu 70% emas, **43%**. Shu burilish videoning markazi bo'ldi: yorliqdagi foiz bilan haqiqiy hisob farq qiladi.
- Hook: «Bu 70 foizlik chegirma 70 foiz emas. To'lashdan oldin hisoblang.» (EN 100.0; asl birinchi qator kuchsiz).
- Ko'rinadigan burilish: Usta yorliqdagi «70%» ni ushlab, ostidan «43%» chiqadi.
- «Faqat bugun» taymeri: shoshiltirish — sabab emas.
- Oxirida 3 ta tekshiruv + botga chaqiriq (bot yorliq suratidan haqiqiy foizni hisoblaydi, `bot/knowledge.js` «Discounts»).

## Sahnalar

| # | Nima ko'rinadi | Gap |
|---|---|---|
| 1 | Do'kon oynasida katta qizil «-70%» yozuvi, ostida chizilgan «300 000», yonida katta «170 000». Usta yorliqqa barmog'ini qo'yadi | **Usta:** «Bu 70 foizlik chegirma 70 foiz emas. To'lashdan oldin hisoblang.» |
| 2 | Diyor ko'zlari yonib, sumkasini ochadi | **Diyor:** «Usta, qarang! Uch yuz ming edi, bir yuz yetmish ming bo'libdi! Hozir olmasam, yutqazaman!» |
| 3 | Usta xotirjam | **Usta:** «Bu narsani chegirmani ko'rishdan oldin ham qidirayotgan edingmi?» |
| 4 | Diyor qotib qoladi | **Diyor:** «Yo'q… Chegirmani ko'rib qoldim.» |
| 5 | Usta «-70%» yorliqni ko'taradi, ostidan «-43%» chiqadi (sekinlashuv) | **Usta:** «Hisoblaylik. Uch yuz mingdan bir yuz o'ttiz ming tushgan. Bu yetmish emas, qirq uch foiz.» |
| 6 | Diyor barmog'ida sanaydi, hayron | **Diyor:** «Unda nega yetmish deb yozishgan?» |
| 7 | Yorliq ustida qizil taymer «faqat bugun 00:59:59» yonadi | **Usta:** «Katta raqam ko'zni, taymer qo'lni shoshiltiradi. Kerakli narsa shoshilishni talab qilmaydi.» |
| 8 | Ekranda 3 ta tekshiruv birma-bir: 🔎 boshqa do'kon narxi · 📏 o'lcham, sifat, kafolat · ❓ kecha kerakmidi? | **Usta:** «Uchta tekshiruv: boshqa do'kondagi narxi qancha? O'lchami, sifati, kafolati bir xilmi? Va kecha ham kerakmidi?» |
| 9 | Diyor sumkasini yopib, jilmayadi | **Diyor:** «Demak, avval hisoblayman, keyin olaman.» |
| 10 | Usta kameraga | **Usta:** «Xaridni foiz emas, ehtiyoj hal qilsin.» |
| 11 | Usta telefonda: yorliq surati botga ketadi, bot «haqiqiy chegirma: 43%» deb javob beradi. Katta yozuv **@sahiychishopbot** | **Usta:** «Chegirma yorlig'ini suratga olib botimizga yuboring: @sahiychishopbot. Haqiqiy foizni hisoblab, nimani tekshirishni aytib beradi.» |
| — | Avatar: «Siz-chi? Eng katta chegirmangiz qancha edi? Izohga yozing!» | — |
| — | Yakuniy karta | — |

Sekinlashuv (1 marta): 5-sahnada «-70%» yorliq ko'tarilib, ostidan «-43%» chiqqanda; yorliq yerga tushsa — zarba ovozi.
Ranglar (egasi qoidasi): har kadrda 2–3 ta — qizil (chegirma), sariq (narx), ko'k (tun/Diyor nuri).

## Hook variantlari (EN, `hookscore.py`)
| Hook | Ball |
|---|---|
| «Bu 70 foizlik chegirma 70 foiz emas. To'lashdan oldin hisoblang.» (This 70% discount is not 70%. Do the math before you pay.) | **100.0** ✅ |
| «To'xta. 70 foizlik chegirmani olishdan oldin bitta savol ber.» | 100.0 |
| «Kecha kerak bo'lmagan narsani 70 foizga olishdan oldin bitta savol bering.» | 70.0 |

## Tekshirilgan hisob
(300 000 − 170 000) / 300 000 = 0.433 → **43%**. 70% chegirma bo'lsa, narx 90 000 bo'lardi.

Holat: 📝 ssenariy, egasi tasdig'ini kutmoqda.
