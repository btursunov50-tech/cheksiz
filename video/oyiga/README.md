# «Oyiga atigi…» — ish holati

Ssenariy `ideas/oyiga-atigi.md`, ovoz `dialog.wav` (qatorlar vaqti `OVOZ.md`), rasmlar va Veo promptlari `rasm_promptlar.py` → `rasmlar.html` (https://claude.ai/artifact/ABGrkqpb7Uqj83UuSqdVsZ).

## Kliplar (Veo, 720×1280, 8 s, belgisiz)
| # | Fayl | Holat | Qaysi qism | Izoh |
|---|---|---|---|---|
| 1 | `clips/s01.mp4` (v2) | ✅ qisman | 0–3.4 s (~1.8x sekin, 1-qatorga ~6.1 s) | Yorliqlar oxirigacha bo'sh, Usta yorliqni olmaydi. Lekin 3.5 s dan keyin yaqin planda yuz o'zgaradi: ingichkalashadi, qoshlar keskin, tishlarini ko'rsatib kuladi, do'ppi naqshi boshqa — olinmaydi. Zaxira: `clips/s01_v1.mp4` (yorliqda soxta yozuv) |
| 2 | `clips/s02.mp4` | ✅ | 0–5.6 s | Sakraydi, quvonadi; 6 s dan keyin telefonni qulog'iga qo'yadi (qo'ng'iroqqa o'xshaydi) — olinmaydi |
| 3 | `clips/s03.mp4` | ✅ | ~2.0–6.4 s (sahna ~4.2 s) | Lupa yaqinlashadi, fokus yuzga ko'chadi, Usta ko'zini qisib qoshini ko'taradi; yorliq bo'sh, yozuv yo'q |
| 4 | `clips/s04.mp4` | ✅ | 0–6.6 s (~1.25x sekin) | Sanaydi, tangalar yonadi, hayratda og'zi ochiladi; 7 s dan keyin yuzi o'zgaradi — olinmaydi |
| 6 | `clips/s06.mp4` | ✅ (qisman) | 2.8–8.0 s (~1.35x sekin) | 1.4–2.6 s da Veo Diyorni butunlay yashil-ko'k rangga bo'yab qo'ydi (nur «xiralashsin» degani noto'g'ri tushunilgan) — olinmaydi. 3 s dan keyin: tabassum so'nadi, uyalib yerga qaraydi, yonog'i qizaradi — juda yaxshi; sotuvchi kadrdan chiqib boradi |
| 5 | `clips/s05.mp4` (v3) | ✅ | 0.8–7.0 s | Tanga tushadi, 3.6 s da katta uchqun, yonida ikkinchi ustun o'sib chiqadi (egasining g'oyasi). Yuz 6.5 s gacha namunadek. Kichik: uchqundan keyin tepadagi qizil tangalar ko'rinmaydi, stolga bir nechta tanga sochiladi, ikkinchi ustun o'ngda (quti oldida). Zaxira: `clips/s05_v1.mp4` (ustun yo'qoladi — ishlatilmaydi) |
| 7 | `clips/s07.mp4` | ✅ | 0–7.6 s | Usta taroziga ishora qiladi, keyin kaftini ko'rsatadi, barmog'ini ko'taradi — jonli; yuz namunadek, qo'llar 5 barmoqli. O'ng palla pastda turadi. Kamera deyarli qimirlamagan (harakat 4.7, «pastga burilish» bajarilmagan) — montajda `kamera/harakat.py --move pushin` bilan sekin yaqinlashish qo'shiladi |
| 8 | `clips/s08.mp4` | ✅ | 0–6.8 s (~1.4x sekin) | 3 barmoq oxirigacha turadi, belgilar birma-bir yonadi, yuz namunadek. Kichik: 4 s atrofida qum soat bir lahza qizilini yo'qotadi, tangada mayda belgi bor (o'qilmaydi). 7 s dan keyin belgilar so'nib, qo'l tushadi — olinmaydi. Kamera kam yuradi — montajda sekin yaqinlashish |
| 9 | `clips/s09.mp4` | ✅ | 0–4.4 s | Diyor telefonni javonga qo'yadi va qo'yib yuboradi, kameraga o'girilib ayyorona jilmayadi, daftarni ko'kragida ushlaydi. Yuz namunadek, telefonlarda belgi yo'q. Kamera kam yuradi (5.3) — montajda yon tomonga suzish/yaqinlashish |
| 10 | `clips/s10.mp4` | ✅ | 0.5–7.5 s | Yaqin plan: Usta jilmayadi, boshini qiyshaytiradi, ko'zlari kuladi, oxirida qoshini ko'tarib «savol» beradi. Yuz va do'ppi butun klip davomida namunadek. Kamera sekin yaqinlashadi (10.8) |
| 11 | `clips/s11.mp4` | ✅ | 0–8 s (~1.4x sekin, qator ~11 s) | Usta telefonni ko'rsatadi, 1–2.5 s da ekrandan bo'sh moviy xabar pufakchalari uchib chiqadi (yozuvsiz), Diyor bosh barmog'ini ko'taradi, Usta qo'li Diyor yelkasida. Ikkala yuz namunadek. Kamera uzoqlashib ko'tariladi: 3 s dan keyin kadr tepasida qora tasma o'sadi (7.8 s da ~410 px) — u yerga katta @sahiychishopbot yoziladi, tasma cheti montajda gradient bilan yumshatiladi |

## Yig'ish (2026-10-26)
- Musiqa: «Doira and the Robot» (`video/robot/music/doira_and_the_robot.mp3`, 41 s dan, egasi tanladi, ovozi 0.4 — egasi «ozgina pasaytir»), Suno → «Music: made with Suno», monetizatsiyasiz.
- Buyruq: `python3 video/oyiga/prep_clips.py` keyin `yig.py --dir video/oyiga --voice dialog_fx.wav --avq "Siz-chi?|Nasiyaga nima olgansiz?|Izohga yozing!" --music video/robot/music/doira_and_the_robot.mp3:41 --music-vol 0.4 --send`.
- Natija: `video/final/oyiga/1-telegram-oyiga-uz.mp4` (83.4 s; qotgan/qora kadr, ovozsiz joy yo'q).
- en/ru: `python3 video/oyiga/tarjima.py` (timeline_en/ru.py + 3 ta .srt), keyin `yig.py ... --reuse --tl en --lang en` (avatar: «And you?|What did you buy on installments?|Write in the comments!») va `--tl ru --lang ru` («А вы?|Что брали в рассрочку?|Пишите в комментариях!»). Post matnlari: `POSTS.md`.
