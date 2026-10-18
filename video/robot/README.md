# «Robot bilan bir piyola choy» (13-video)

- Ssenariy: `ideas/robot-choyxona.md`. Ovoz: `dialog.flac` (Manus, 157.5 s, Robot + Odam).
- Uslub: sinematik, tik 9:16. Namunalar: `img/ref_robot.jpg`, `img/ref_odam.jpg` (`REF.md`).
- Rasmlar: `img/01..22` (ChatGPT), rasm promptlari `PROMPTS.md` (`prompts.py`).
- Video promptlari: `VIDEO.md` va sahifa `sahnalar.html` (https://claude.ai/artifact/E1GagDTD86pU2HizkJT2MP), `video_prompts.py`.
- Kliplar: `clips/sNN.mp4` (Veo, 720×1280, 8 s). 4-sahna: Veo «mashhur shaxslar» deb rad etgan, egasi rasmni neon chiziqli chizma qilib o'zi yasagan.
- 14-sahna Vidu'da (540×958, 5 s, «Vidu AI» belgisi): `clips/s14_vidu_asl.mp4` asli, `clips/s14.mp4` belgisi kesib tashlangan (crop 496×882, 720×1280 ga kattalashtirilgan). Vidu 5 s bergani uchun 9 s dan uzun sahnalar (15, 16, 18) Veo'da (8 s) qilinadi.
- 15-sahna Dreamina'da (704×1248, 60 fps, 8 s, «Dreamina AI» va «AI» belgilari): `clips/s15_dreamina_asl.mp4` asli, `clips/s15.mp4` belgilar kesilgan (crop 644×1144+30+40, 24 fps, 720×1280).
- 16-sahna Hailuo'da (768×1344, 8 s, «MINIMAX | Hailuo AI» belgisi): `clips/s16_hailuo_asl.mp4` asli, `clips/s16.mp4` belgi kesilgan (crop 708×1260+30+0, 720×1280). Oxirida shartnomada ma'nosiz harflarga o'xshash chiziqlar bor (o'qib bo'lmaydi).
- 17-sahna: asosiy klip `clips/s17.mp4` (egasining 2-varianti, 480×864, 10 s, belgisiz; robot o'zgarmaydi). Zaxira: `s17_hailuo.mp4` (4 s dan keyin robot ko'zlari o'zgaradi).
- Vaqtlar: `timeline.py` — har bir ovoz qatori va sahna kesimi. Egasi 0:19, 0:56, 1:01 ni tasdiqlagan.
- Yig'ish: `python3 video/robot/preview.py <papka> [sahnalar soni]` — kliplar vaqtga moslanadi (ko'pi bilan ×1.48 minterpolate), cine + sfx, ovoz + musiqa (hozircha Dutar's Whisper 3:17 dan; egasi boshqasini beradi), uz subtitr, 9-sahnada qizil STOP.
- Musiqa (egasi, 2026-10-18): Curious Unease boshi yaxshi; Kafeda 1:10 dan mos kelmadi. Yakuniy musiqa hamma video tayyor bo'lib, matn o'zgargach tanlanadi.
- Hali qilinmagan: 14–22 kliplari, musiqa, avatar (3 s) + yakuniy karta, en/ru subtitr, post matnlari.
