# «VAQT» — kodda yasalgan qismlar (Veo'siz)
`hook.html` (canvas, `setT(t)`): ko'k neon chiziq tik-tik bilan qum soatini chizadi → oltin qum oqadi → soat qumga sochiladi → qum «VAQT» yozuviga yig'iladi. 10 s, 9:16.
Render: `node video/render.js video/vaqt/kod/hook.html <frames> 10 30`, ovoz ffmpeg `aevalsrc` bilan (tik, zarba, shitirlash). Natija: `hook.mp4`.
Rejada kodda: Vaqt gavdasi (neon tolalar), oltin chiziqli xotiralar, tangalar qumga aylanishi, final yozuv. Veo faqat jonli sahnalar uchun (boy, karvonsaroy, hovli).
`xotira.py RASM.jpg CHIQISH.mp4`: xotira animatsiyasi (oltin konturlar chiziladi → rasm oltin rangda ochiladi, sekin push-in → qumga aylanib to'kiladi), 6.2 s, 720x1280. Birinchi variant (faqat chiziqlar) tushunarsiz chiqdi, egasi rad etdi.
`vaqt.html` (canvas, shaffof fon): neon VAQT gavdasi — qalpoqli, chopondagi siymo, minglab ko'k tolalar, ko'kragida oltin qum soati, uchqunlar, etakdan uchadigan tolachalar. `#enter` — tepadan to'qilib paydo bo'ladi, `#warm` — oltinga o'tib so'nadi. Render: `node video/vaqt/kod/render_png.js "video/vaqt/kod/vaqt.html#enter" <papka> 5 30` (PNG, alfa kanal bilan).
