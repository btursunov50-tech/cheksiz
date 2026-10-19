# Neon uslub: «Sabr qil — zafar yaqin» (2026-10-19)

Egasining eski `sahna5.html` grafikasi (yorug' osmon, rangli odamchalar, «SABR QIL — ZAFAR YAQIN», Zumar 39:53) asosida yangi neon uslub.
`sabr.html` — canvas animatsiya, `setT(t)`; uslub URL oxiridagi `#A`, `#B`, `#C` bilan tanlanadi.
- A «Neon tun»: to'q ko'k osmon, yulduzlar, hilol, neon odamchalar, perspektiv neon to'r.
- B «Neon tong»: yumshoq binafsha-shaftoli tong, quyosh, yashil maydon.
- C «Neon chiziq»: qora fon, odamchalar chiziq bo'lib chiziladi, hilol faqat kontur.
- D «Jigarrang tun» va E «Jigarrang chiziq» (egasi: «Kalamushqir»ga o'xshasin, rang kam, jigarrang ko'proq, ko'k neon va sariqlar, qizil kam): to'q jigarrang fon, qog'oz donadorligi, vinyetka, sariq-oltin odamchalar qo'lda chizilgandek ikki chiziqli, markazdagi qahramon ko'k neon; E da odamchalar chizilib paydo bo'ladi.
Ko'z charchamasligi uchun: miltillash yo'q, harakat sekin, glow o'rtacha, matn 2 qatorda katta.

Render: `node video/render.js "video/neon/sabr.html#A" <frames> 12 30` → ffmpeg. Namunalar: `sabr_A.mp4` … `sabr_E.mp4` (9:16, 12 s, ovozsiz).
