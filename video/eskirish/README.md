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
- Fonuslar (egasi, 2026-10-28): ko'cha fonuslari kodda ko'k neonga bo'yalgan (`fonus.py`, `fonus_hammasi.sh`; asl rasmlar `img/asl/`). Veo va rasm promptlarida ham «street lamps glow cool neon blue».
