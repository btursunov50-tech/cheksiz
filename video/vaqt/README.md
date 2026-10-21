# «VAQT» (2026-10-20)
Ssenariy: `ideas/vaqt-savdogari.md` (90 s versiya + AI epilogi, xotiralar: qizi va nabirasi Aziz).
Ovoz: `voice/01..14_*.flac` (Manus, 4 ovoz). **`07_vaqt_ottiz.flac` = «O'ttiz yil» — ishlatiladi** (egasi, 2026-10-20); `07_vaqt.flac` = «Yetti yil» (zaxira, ishlatilmaydi).
Fayllar rejadan ~2 baravar uzun (0.9x tezlik + oxirida ~1 s jimlik); montajda pauzalar qisqartiriladi. 01, 04, 06, 12, 14 da cho'qqi 0 dB — xirillash bo'lsa egasi aytadi.

Rasmlar: `img/ref_hoji.jpg`, `img/ref_qizi.jpg`, `img/ref_aziz.jpg` (tasdiqlangan namunalar; Azizning ikkinchi varianti yuzi boshqa, olib tashlandi), `img/s02_boy_aziz.jpg` (2-sahna, namunalarga mos).
Sahnalar (2026-10-20): `s03_tanga.jpg` (asosiy; `_b` zaxira), `s04_sandiq.jpg`, `s05_qum.jpg`, `s07_tavba.jpg` — boyning yuzi namunaga mos.
`s08_uygonish`, `s09_hovli` (Azizning doppisi naqshi namunadan biroz boshqa), `s10_daftar`, `x1_qogirchoq`, `x2_toy` (2026-10-20).
`x5_rasm` ✅; `x3_chaqaloq_eski`, `x4_qadam_eski`: qizi o'smirdek yosh chiqqan, qayta qilinadi (yangi prompt X3/X4). Epilog bugungi kunda (13b).
`s13_bugun` (epilog, bugungi kun), `x3_chaqaloq`, `x4_qadam` (qizi hali ham yoshroq ko'rinadi, lekin oltin chiziqqa aylanganda yosh sezilmaydi). Barcha rasmlar tayyor.
Veo promptlari sahifasi: `sahnalar.py` → `sahnalar.html`, https://claude.ai/artifact/6KB4HumUpbVbKfmyke8SxJ (14 klip: 2–5, 5 xotira, 7–10, 13). Xotiralar ham Veo bilan, keyin `kod/xotira.py` uslubida oltin rang + qum.
VAQT yangi qiyofa (egasi, 2026-10-21: neon aralash odam): shisha teri, ostida ko'k neon tomirlar, ichida oltin qum oqadi, ko'zlari oltin, ko'kragida qum soati, neon tolali qalpoqli chopon, etagi qumga aylanadi. Veo'da 3, 4, 5, 7, 9-sahnalarda. Kodli `kod/vaqt.html` zaxira.

## Kliplar (2026-10-21, Veo, 720×1280, 8 s) — `clips/`
| Klip | Holat |
|---|---|
| s02 | ✅ Aziz kirib keladi, bobo qaramaydi, Aziz chiqib ketadi |
| s03 | ❌ VAQT boshqa: qalpoqsiz, yalang'och mushakli, sariq ko'zli (qo'rqinchli). Veo xatosi (VAQT rasmi yo'q edi). Tanga tushishi (0–1.8 s) yaxshi |
| s04 | ✅ VAQT to'g'ri (qalpoq, shisha teri, neon tomirlar). `img/ref_vaqt.jpg` shu klipning 6.2 s kadridan |
| s05 | ✅ shisha qo'l tegadi, tangalar qumga aylanadi |
| s07 | ❌ VAQT yuzi qo'rqinchli (sariq ko'zlar); qum soatining yuqorisi qorong'i emas. Boy to'g'ri |
| x1–x5 | ✅ xotiralar (qo'g'irchoq, to'y, chaqaloq, birinchi qadam, rasm sekin tushadi) |
Tuzatish: 3, 7 (va 9) uchun VAQT bilan yangi boshlang'ich rasm (`ref_vaqt` biriktiriladi), keyin Veo.
