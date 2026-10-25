# «Robot bilan bir piyola choy» — yakuniy gap (2026-10-25)

**Qaror (egasi): yangi ovoz yozilmaydi.** «Izohga LAVASH AI deb yozing» kesib olindi (`dialog_v2.flac`, 155.3 s dan jim, 158.5 s gacha), botga chaqiriq ekranda yozuv bilan (`timeline.py` → `TEXT`). Pastdagi ovoz bloki zaxira.

Egasi: oxirgi «Izohga «LAVASH AI» deb yozing» o'rniga botga chaqiriq (CLAUDE.md, 2026-10-24 qoidasi).
`dialog.flac` dagi 153.85–155.1 s «Sizda ham do'kon bormi?» qoladi; 155.3–157.4 s «Izohga «LAVASH AI» deb yozing.» o'rniga yangi fayl qo'yiladi.
Robot ovozi qolgan qismdagi bilan bir xil bo'lishi kerak: namuna `voice/robot_namuna.mp3` (dialog.flac 0–8 s).
Bot bunga haqiqatan javob beradi: `bot/knowledge.js` dagi xizmatlar va «biznesga qanday yordam beradi» qoidasi.

```
OVOZ SOZLAMALARI
Ovoz: ROBOT — videoning qolgan qismidagi robot ovozi bilan aynan bir xil (o'sha vosita, o'sha ovoz; namuna fayl biriktirilgan). Sokin, mehribon, biroz kinoyali erkak ovozi.
Til: o'zbek tili (lotin yozuvi), tabiiy toshkentcha talaffuz.
Tezlik: 1.0x. Har qatordan keyin 1 soniya pauza.
Natija: bitta WAV fayl, musiqasiz, effektsiz.
Talaffuz: "AI" = "ey-ay"; "@sahiychishopbot" = "sahiychi shop bot".

1. ROBOT [do'stona, kameraga qarab; ~3.5 s]: Do'koningizga AI qanday yordam berishini botimizdan so'rang.
2. ROBOT [aniq, sekinroq; ~2 s]: @sahiychishopbot.
3. ROBOT [iliq, jilmayib; ~4 s]: Biznesingizni yozing, qaysi ishni AIga topshirsa bo'lishini tushuntiradi.
```

| Qator | Videoda | Kadr |
|---|---|---|
| (eski) «Sizda ham do'kon bormi?» | 153.85–155.1 s | 22-sahna, robot kameraga |
| 1–3 (yangi) | 155.3 s dan, ~11 s | 22-sahna davomi; ekranda katta **@sahiychishopbot** |
| — | +3 s | Avatar: «Siz-chi? AIga nimani ishonasiz? Izohga yozing!» |
| — | +4 s | Yakuniy karta |
