# «Telefoning eskirmagan» (Diyor & Usta, 4-qism, Baron formati)

- Ssenariy: `ideas/eskirish.md`. Ovoz bloki: `OVOZ.md` (bitta fayl, qatorlar orasida 1000 Hz BIP).
- Rasm promptlari: `rasm_promptlar.py` → `rasmlar.html`, Artifact: https://claude.ai/artifact/WY4CroEsDWcynVsh9pgSox (16 ta rasm, 9:16). Namunalar `img/ref_usta.png`, `img/ref_diyor.png` («70 foiz chegirma» dagi).
- Veo promptlari: `veo_promptlar.py` → `sahnalar.html`, o'sha Artifact: https://claude.ai/artifact/WY4CroEsDWcynVsh9pgSox (kamera gapi boshida va oxirida, «joyida qolsin» yo'q, o'zbekcha gaplar).
- Holat: ✅ 16 ta rasm tayyor (2026-10-28); Veo kliplari va ovoz (Manus) kutilmoqda.

## Rasmlar
| # | Fayl | Holat | Izoh |
|---|---|---|---|
| 1 | `img/s01.png` (tahrirdan keyin; eski `s01_a.png`) | ✅ | Usta yuzi silliqroq, soqoli qalinroq, ajinlar kamaydi: namunaga yaqinlashdi (yuzi hali biroz cho'ziqroq, Veo klipida kuzatiladi). Qolgani o'zgarmagan |
| 2 | `img/s02.png` | ✅ | Diyor telefonni silkitadi, jahli chiqqan; soch tekis, qora, ryukzak, ingichka moviy nur; qo'llar 5 barmoqli; yozuv yo'q |
| 3 | `img/s03.png` | ✅ | Usta yuzi namunaga yaqin (~30 yosh, qalin qisqa soqol, do'ppida oq naqsh), qo'llari qovushtirilgan, bir qoshi ko'tarilgan; Diyor orqadan xira (soch qora, ryukzak). Yozuv yo'q |
| 4 | `img/s04.png` | ✅ | Usta kaftini ko'rsatadi (5 barmoq), yuzi 3-rasmdagidek; o'ngda sepiya Jeneva (ko'l, tog', tramvay), odamlar orqadan |
| 5 | `img/s05.png` (asl: `s05_a.png`) | ✅ | 1924 zal, 7 ta erkak, yuzlar shlyapa soyasida; egasi so'rovi bilan stoldagi 7 ta lampochka kodda ko'k neonga bo'yaldi (qandil va devor chiroqlari sariq qoldi) |
| 6 | `img/s06.png` (asl: `s06_a.png`) | ✅ | Laboratoriya, qatorda lampochkalar, bittasi o'chgan (o'rtada); texnik orqasidan, yuzi yo'q; yozuv yo'q. Egasi so'rovi bilan kodda: soat raqamlari va strelkalari ko'k neon (siferblat qorong'ilatildi), shiftdagi lampalar ko'k neon |
| 6b | `img/s06b.png` | ✅ | Diyor yaqin planda hayratda (ko'zlar katta, og'iz ochiq, qo'l iyagida); yuz namunaga mos, soch tekis qora, ingichka moviy nur; telefon orqasida logotip yo'q (kamera bo'rtig'i bor); barmoqlar to'g'ri |
| 7 | `img/s07.png` | ✅ | Kanal bo'yi, orqada teleminora namunadek (3 qiya oyoq, 2 disk, shpil, oltin chiroqlar). Usta telefonni ushlab qaraydi, yuzi namunaga mos; Diyor engashib qiziqib qaraydi, soch tekis qora. Qo'llar to'g'ri, telefonda logotip yo'q, yozuv yo'q |
| 8 | `img/s08.png` | ✅ | Telefon ekranida qizil, deyarli bo'sh batareya va shilliqqurt; logotip/yozuv yo'q |
| 9 | `img/s09.png` | ✅ | Telefon do'koni: odamlar orqasidan (yuzsiz), oq qutilar, savatda eski telefonlar. Qutilarda o'qilmaydigan mayda kulrang belgilar bor, logotip emas; savatdagi ba'zi telefonlar kamerasi mashhur brendga o'xshaydi, lekin belgi yo'q |
| 10 | `img/s10.png` | ✅ | Sud bolg'asi, tarozi, dollarga o'xshash pul (yozuvi xira), yorilgan ekranda qizil batareya. O'qiladigan yozuv yo'q |
| 11 | `img/s11.png` | ✅ | Teleminora namunadek; Diyor telefoniga quvonib qaraydi (umidli emas, hayajonli — mos), soch qora tekis, moviy nur juda kuchsiz; Usta orqada jilmayadi, yuzi namunaga mos; qo'llar to'g'ri |
| 13 | `img/s13.png` | ✅ | Usta 3 barmoq (to'g'ri), tepada 3 neon belgi: batareya (sariq), chip (ko'k), kalit (yashil), yozuvsiz; yuz namunaga mos; teleminora namunadek |
| 15 | `img/s15.png` | ✅ | Usta telefonni ko'rsatadi: bo'sh chat pufakchalari + yashil batareya (tekshirilgandan keyin — mos); qo'li Diyor yelkasida; Diyor bosh barmog'ini ko'taradi, jilmayadi. Diyor sochi to'lqinliroq, moviy nuri yo'q (kichik farq). Yozuv yo'q. Tepada osmon — @sahiychishopbot shu yerga |
| 12 | `img/s12.png` | ✅ | Hazil: Diyor telefonni ko'kragiga bosib, ko'zlarini yumib jilmayadi; Usta kulib barmog'i bilan ko'rsatadi. Yuzlar namunaga mos, Diyor sochi qora, ingichka moviy nur bor; qo'llar to'g'ri; teleminora namunadek; yozuv yo'q |
| 14 | `img/s14.png` | ✅ | Usta yaqin plan, kameraga dono va iliq qaraydi; yuz 13-rasm va namunaga mos; orqada teleminora va kanal; yozuv yo'q |
- Fonuslar (egasi, 2026-10-28, 4-urinish): har fonus shishasi aniq o'lchangan (--glass), faqat shisha ichi ko'k neon; uzoqdagi zich qatorlarda navbatma-navbat, atrofga nur yoyilmaydi (`fonus.py`, `fonus_hammasi.sh`; asl rasmlar `img/asl/`). Veo va rasm promptlarida ham «street lamps glow cool neon blue».

## Kliplar
| # | Fayl | Holat | Olinadigan qism | Izoh |
|---|---|---|---|---|
| 1 | `clips/s01.mp4` | ✅ | 0–5.5 s (ovoz ~4 s) | Kamera sekin yaqinlashadi (harakat 19.8 — Veo kamerani qimirlatdi). Usta gapiradi, qo'lini telefonga uzatadi; Diyor telefonga jahl bilan qaraydi, sochi tekis qora, ingichka moviy nur. Ko'k fonus o'ngda ko'rinadi. Yuzlar namunaga mos. 6 s dan quyosh nuri kuchli, Usta ko'zini yumadi, kadr ikkalasining boshini kesadi — ishlatilmaydi |
| 5 | `clips/s05.mp4` | ✅ | 0–8 s | Kamera yuqoridan stolga tushadi, qo'l siqishadi, qog'oz uzatiladi; ko'k lampochkalar ko'k qoldi; yuzlar shlyapa soyasida (6–8 s da yarim ko'rinadi, umumiy, haqiqiy odam emas); sepiya saqlangan |
| 6 | `clips/s06.mp4` | ⚠️ qisman | 0–4.5 s (ovoz ~7 s → ~1.6x sekinlashadi) | Kamera lampochkalar bo'ylab suzadi, soat va shift lampalari ko'k qoldi, o'chgan lampochka bor. **Xato (Veo):** 4.6 s dan bitta lampochkadan olov chiqadi |
| 8 | `clips/s08.mp4` → `s08_y.mp4` | ✅ (tuzatildi) | 0–8 s | Shilliqqurt sekin o'rmalaydi, orqada ko'k tutun. **Xato (Veo):** batareya 1 s dan to'lib, 4 s da to'liq qizil bo'lib qoldi (ma'noga zid). `batareya.py` 0-kadrdagi deyarli bo'sh batareyani har kadrga telefon harakatiga moslab qayta yopishtirdi va 2 marta miltillatdi. Kamera kam harakat (4.3) |
| 1–4 (Dola) | `clips/dola_1_4.mp4` | ⚠️ sinov | — | Dola (Seedance) 30 s so'ralgan, **15.1 s** chiqdi: 4 kadr ~3–4 s dan (ovoz uchun qisqa, 1.5x sekinlashtirish kerak). Pastki o'ng burchakda «Dola AI» suv belgisi. Kamera harakati yaxshi (23.2). Ko'k fonuslar va Jeneva fonida qoldi. **Muammo:** 2-kadrda (4–8 s) fon boshqa ko'chaga almashgan (binolar, park emas) va Diyor yuzi realistik, kattaroq yoshli bo'lib qolgan; 3-kadrda Diyor kameraga burilgan |
| 1–4 (Seedance skill, 1-qism) | `clips/sd_qism1.mp4` | ✅ ko'p qismi | 0–13.5 s | Skill orqali Dola/Seedance: yana **15.1 s** (30 s emas). «Dola AI» suv belgisi pastki o'ngda. Oldingidan yaxshi: 1–3-kadr bir xil park ko'chasida, Diyor yuzi multfilmcha (jahlli ifoda yaxshi), Usta namunaga mos, kamera harakati kuchli (22.8). 3-kadrda Diyor orqasi bilan (8 s gacha). 4-kadrda Jeneva sepiya emas, tungi ko'k shahar (chiroyli). 13.9 s dan Usta burilib ketadi, 14.8 s da kaft yaqindan — kesiladi |
| 1–4 (Seedance bo'laklari) | `clips/s01_sd` (0–2.4), `s02_sd` (2.45–5.45), `s03_sd` (5.5–9.0), `s04_sd` (9.15–13.5) | ✅ 3, 4 olinadi | — | `sd_qism1.mp4` dan kesildi, «Dola AI» belgisi delogo bilan o'chirildi. 3-sahna (3.5 s, ovoz ~5 s → 1.4x) va 4-sahna (4.3 s, tungi Jeneva) ishlatiladi; 1-sahna Veo klipi yaxshiroq; 2-sahna atigi 3 s (ovoz ~6 s → 2x, juda ko'p) — Veo'da qayta |
| 2 | `clips/s02.mp4` (Hailuo) | ✅ | 0–8 s (ovoz ~6 s) | Hailuo 768×1344, «MINIMAX · Hailuo AI» belgisi avtomatik kesildi. Qo'lda chayqalib yaqinlashadi (19.9). Diyor jahl bilan gapiradi, yuzi multfilmcha va namunaga mos, sochi tekis qora; ko'k fonuslar qolgan. 4.5 s dan telefon kadrdan chiqadi (yaqin plan), moviy nur kuchsizlanadi |
| 6b | `clips/s06b.mp4` (Hailuo) | ✅ | 0–3 s (ovoz ~1.5 s) | Keskin yaqinlashish (16.9), Diyor hayratda, ko'zlar katta, og'iz ochiq; yuz namunaga mos. Belgi kesildi. 3 s dan juda yaqin (faqat yuz), 6 s dan yuzi realistikroq — ishlatilmaydi |
| 7 | `clips/s07.mp4` (Hailuo) | ✅ | 0–8 s (ovoz ~6 s) | Ikkalasi atrofida aylanib yaqinlashadi (19.4), teleminora va ko'k fonus ko'rinadi. Usta telefonga qarab gapiradi, Diyor engashib qiziqib qaraydi; yuzlar namunaga mos, telefonda logotip yo'q. Belgi kesildi. Oxirida kadr juda yaqin, Diyor boshi chetda — 6.5 s gacha olish yaxshiroq |
| 9 | `clips/s09.mp4` → `s09_y.mp4` (Hailuo) | ✅ qisman | 0–4.7 s (ovoz ~6 s → ~1.3x) | Do'kon peshtaxtasidan savatga egilib tushadi (29.0, tez). Odamlar orqasidan, yuzsiz, oq qutilar. **Xato (Hailuo):** savatdagi ko'k telefonda olma logotipi (1.5 s dan). `logo_ochir.py` 4.7 s gacha tozaladi; 5 s dan qora logotip ko'rinadi — ishlatilmaydi |
