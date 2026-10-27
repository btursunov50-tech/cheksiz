# «70 foiz chegirma» — ish holati

Ssenariy `ideas/chegirma.md`, ovoz bloki `OVOZ.md` (15 qator), rasm va Veo promptlari `rasm_promptlar.py` → `rasmlar.html` (https://claude.ai/artifact/Ph5iXda1mbx5Ro4jTaWSYr). 12 ta rasm tasdiqlangan (`img/sNN.png`).

## Kliplar (Veo, 720×1280, 8 s)
| # | Fayl | Holat | Qaysi qism | Izoh |
|---|---|---|---|---|
| 1 | `clips/s01_v1.mp4` | ✅ (egasi: «qolsin, boshqa ovoz qo'yasan baribir») | 0–8 s | O'zbekcha gap promptda yo'q edi, lekin ovozni baribir o'zimiz qo'yamiz. Bannerga «-70%» va narxlar `yuza.py` bilan yoziladi |
| 2 | `clips/s02.mp4` | ✅ (egasi: «bu qolsin») | 0–8 s | O'zbekcha promptdan: Diyor hayajonda gapiradi, ishora qiladi, joyida sakraydi, yuz va moviy nur namunadek, yomg'ir, soyabonli odamlar yuradi. 7 s dan do'konga qarab burilib kiradi — 3-sahnaga (do'kon ichi) tabiiy o'tish |
| 3 | `clips/s03.mp4` | ✅ | ~0.3–5 s (ovoz ~3.5 s) | Usta gapiradi (lab qimirlaydi), qo'llari qovushtirilgan, boshini qiyshaytirib jilmayadi; yuz 4 kadrda namunadek. Diyor oldinda xira, jim. Eshikdan ko'chada odamlar yuradi. Kamera deyarli qotgan (8.2) — fokus ko'chishi bo'lmagan, lekin kadr yaxshi |
| 4 | `clips/s04.mp4` | ⚠️ qisman | 0–3.5 s (ovoz ~3 s) | Kamera Diyorga yaqinlashadi (push-in), Diyor gapiradi, ryukzak tasmasini ushlab o'ylanib yuqoriga qaraydi; Usta orqada jim, qo'llari qovushtirilgan; derazadan odamlar o'tadi; nur moviy. **Muammo (Veo):** ~3.5 s dan keyin Diyorning yuzi namunadan chiqadi — cho'ziqroq, kattaroq yoshli, realistik (multfilm yuzi yo'qoladi). Rasm to'g'ri edi. Telefon 0.3–1.3 s da cho'ntakka kirib ketadi |
| 5 | `clips/s05.mp4` → `s05_y.mp4` | ✅ | 0–8 s | Usta yorliqni ko'taradi, gapiradi; 5.4–6.5 s yorliq tushadi (sekinlashuv + yerga tushish ovozi shu yerda). Yuz namunadek. `yuza.py` bilan yozuvlar: yorliqda «-70%», kartada «~~300 000~~ 170 000», yorliq tushganda «-43%» |
| 6 | `clips/s06.mp4` | ⚠️ qisman | 0–2.6 s (ovoz ~2.5 s) | Diyor barmog'ida sanaydi, oyna binafsha. **Muammo (Veo):** ~2.8 s dan keyin yuzi realistik va kattaroq yoshli bo'lib qoladi, qoshi chimirilgan |
| 7 | `clips/s07.mp4` → `s07_y.mp4` | ✅ | 0–8 s | Usta kaftini ko'rsatadi, gapiradi, jilmayadi. Veo taymerga buzuq raqamlar chizgan — `yuza.py` bo'yab yopdi va «00:59:59» qo'ydi (soniyalar kamayadi) |
| 8 | `clips/s08.mp4` | ✅ | 0–8 s (ovoz ~10 s → ~1.25x sekinlashadi) | 3 barmoq (0–3 s), keyin musht; lupa, lenta, so'roq belgilari joyida; orqada odamlar yuradi. Yuz namunadek |
| 9 | `clips/s09.mp4` | ⚠️ qisman | 0–2.7 s (ovoz ~3 s → ~1.15x) | Diyor do'kondan chiqib kameraga yuradi, kalkulyator qo'lida. **Muammo (Veo):** 2.8 s dan vitrinada «Diyor» yozuvi chiqadi, 5 s dan kalkulyator oq telefonga aylanadi |
| 10 | `clips/s10.mp4` (2-variant) | ✅ faqat boshi | 0–2.4 s | Qiz o'ngga o'tib ketadi (1 s da kadrdan chiqadi) va **qaytmaydi**; Diyor qarab qoladi, Usta yelkasiga qo'l qo'yadi. Yuzlar 0–2.4 s da namunadek (Diyor sochi tekis, qora). 3 s dan keyin Usta qariroq ko'rinadi, Diyor yuzi o'zgaradi — shuning uchun faqat boshi olinadi, gaplar 10b/10c da |
| 10b | `clips/s10b.mp4` (2-variant, yangi rasmdan) | ✅ | 0–8 s (ovoz ~6.5 s) | Keng plan, kamera deyarli qotgan (promptdagi yaqinlashish chiqmagan). Usta 1.5–3 s da Diyorning yelkasiga uradi va gapiradi; Diyor ~5 s da cho'chib, yuzi qizarib, qo'llarini yoyib gapiradi. Diyor yuzi butun klipda namunadek (sochi tekis, qora). Usta 4 s dan yuzi sal ingichka va cho'ziqroq — keng planda kichik ko'rinadi. Qiz qaytmaydi |
| 10c | `clips/s10c.mp4` (2-variant, yangi rasmdan) | ⚠️ qisman | 2.3–5.5 s (ovoz ~4 s → ~1.25x sekinlashadi) | Kamera Ustaga yaqinlashadi; Usta kulib gapiradi va chakkasiga barmog'ini tegizadi, Diyor uyalib boshini egadi va qashiydi. **Muammo (Veo):** Diyor 1–3 s da yosh bolaga o'xshab qoladi (namunada ~20 yosh); 2.3 s dan boshi egik, yuzi kam ko'rinadi. Usta 6 s dan juda yaqin, kulgan yuzi qariroq. Sochlar to'g'ri (tekis, qora) |
| 11 | `clips/s11.mp4` | ✅ | 0–8 s | Usta yaqindan kameraga gapiradi, yuz butun klip davomida namunadek |
| 12 | `clips/s12.mp4` | ✅ | 0–7.6 s | Usta telefonni uzatadi, Diyor bosh barmog'ini ko'taradi. 7.7 s dan Veo kadrni almashtiradi (ikkalasi yo'qoladi), shuning uchun kesiladi. 1.3–3 s da telefon yonida «$» belgili oq pufakchalar uchadi (kichik) |

**Yuz tekshiruvi (2026-10-27, egasi so'radi):** 10, 10b, 10c kliplarida Diyor sochi jingalak va jigarrang (namunada tekis, qora, to'zg'in), yuzi ozg'in va realistik; Usta ozg'in, qariroq, soqoli siyrak. Xato 10-klipda Veo'dan boshlangan, 10b/10c shu klip kadridan boshlangani uchun xato ularga ham o'tdi (Claude tekshirmay olgan). Yangi 10b rasmi tasdiqlangan s10.png dan ChatGPT tahriri bilan olinadi, keyin 10, 10b, 10c qayta yasaladi. Promptlarga soch va yosh qulfi qo'shildi.
Yangi `img/s10b.png` (2026-10-27): s10.png dan qiz olib tashlangan; Usta va Diyor yuzlari s10.png va namunalar bilan solishtirildi — bir xil (Diyor sochi tekis, qora). 10b va 10c shu rasmdan qayta yasaladi.

## Yig'ish (2026-10-27)
- Ovoz: Manus, 15 ta alohida fayl (`voice/`). `build_tl.py` → `dialog.wav` + `timeline.py`, `prep_clips.py` → `clips/use/`.
- Musiqa: **Doira and the Robot** (egasi, Suno bepul tarif → «Music: made with Suno», monetizatsiya yo'q; 0:41 dan, vol 0.4) — egasi almashtirdi (2026-10-27, avval dutor_55 edi).
- Buyruq: `python3 video/chegirma/build_tl.py && python3 video/chegirma/prep_clips.py && python3 .claude/skills/video-yig/yig.py --dir video/chegirma --work <tmp> --voice dialog.wav --avq "Siz-chi?|Eng katta chegirmangiz qancha edi?|Izohga yozing!" --music video/robot/music/doira_and_the_robot.mp3:41 --music-vol 0.4 --send`
- Natija: `video/final/chegirma/1-telegram-chegirma-uz.mp4` (89.5 s, qora/qotgan kadr va ovozsiz joy yo'q). en/ru versiyalari egasi uz versiyani tasdiqlagach.

**10-sahna qayta (2026-10-27, egasi: «qiz ko'rinmay qolgan»):** qiz rasmi `img/ref_qiz.png` ✅ (yuzi Usta va Diyordan farq qiladi, atlas ko'ylak, oq sumka, qo'llar to'g'ri). Veo «Ingredients» klipi `clips/s10_ingr_xato.mp4` ❌: ko'ylak oddiy pushti, sumka yo'q, qiz kameraga qarab yuradi, Usta oq to'nda, vitrinada yozuv. Yangi yo'l: ChatGPT'da qizni `s10b.png` ga qo'shish → Veo «Frames to video» (birinchi kadr = shu rasm, oxirgi kadr = `s10b.png`).
