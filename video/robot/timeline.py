# «Robot bilan bir piyola choy»: ovoz qatorlari (dialog.flac dagi vaqtlar, pauzalar bo'yicha topilgan,
# egasi 0:19, 0:56, 1:01 ni tasdiqlagan) va sahna kesimlari.
# (boshi, oxiri, kim R=robot / O=odam, matn) — uzun qatorlar gaplarga bo'lingan.
SUB = [
 (0.1, 4.5, "R", "Do'koningdan har kuni pul oqib ketyapti."), (5.0, 7.8, "R", "Sen esa buni ko'rmaysan."),
 (8.3, 12.8, "O", "Qanaqa pul? Men seni faqat rasm va video uchun ishlataman."),
 (13.5, 18.9, "R", "Rasm yaxshi. Lekin meni rasm uchun o'ylab topishmagan."),
 (19.8, 27.4, "R", "1956-yili olimlar so'rashdi: mashina odamning aqliy ishini qila oladimi?"),
 (28.1, 32.9, "R", "Sen kun bo'yi kassaga, telefonga, mijozga qaraysan."), (33.5, 36.5, "R", "Oshpaz stoliga esa hech kim qaramaydi."),
 (37.5, 39.9, "R", "Bitta lavash sousiz ketdi."), (40.5, 41.9, "R", "Mijoz indamadi."), (42.1, 44.2, "R", "Lekin qaytib kelmadi."),
 (44.8, 47.7, "O", "Nazoratchi yollaymanmi? Unga oylik kerak."),
 (48.4, 51.9, "R", "Bitta kichik kamera. U faqat stolni ko'radi."), (52.4, 55.7, "R", "Go'sht, sabzavot, sous."),
 (56.5, 57.5, "R", "To'xtang."), (57.6, 59.0, "R", "Sous hali qo'shilmadi."),
 (59.8, 61.2, "O", "Faqat lavash uchunmi?"), (61.4, 62.7, "R", "Yo'q."),
 (62.9, 67.5, "R", "Eng qimmat ish qo'l bilan emas, bosh bilan qilinadi."), (68.2, 71.0, "R", "Shifokor, yurist."),
 (71.55, 75.7, "R", "Bitta yaxshi shifokorni tayyorlash qancha turadi?"),
 (76.4, 77.9, "R", "Avval tug'ilishi kerak."), (78.35, 79.5, "R", "Keyin maktab."),
 (79.9, 81.2, "R", "Keyin institut."), (81.85, 85.7, "R", "Keyin yillar davomida amaliyot."),
 (87.05, 91.75, "R", "Sen esa uning oldiga yigirma daqiqaga kirasan."), (92.45, 96.55, "R", "Va o'sha yillarning hammasi uchun to'laysan."),
 (96.9, 99.0, "O", "AI-shifokor arzonroqmi?"),
 (99.25, 103.1, "R", "Men tahlilingni oddiy tilda tushuntiraman."), (103.9, 106.65, "R", "Shifokorga qanday savol berishni aytaman."),
 (107.3, 109.45, "R", "Kechasi soat uchda ham."),
 (109.65, 110.45, "O", "Yurist-chi?"),
 (110.55, 112.1, "R", "Shartnoma qoralamasi."), (112.7, 114.75, "R", "Qiyin so'zlarni tushuntirish."),
 (115.25, 118.3, "R", "Ijara shartnomasida yashirin jarimani topish."), (118.45, 120.05, "R", "Bir necha daqiqada."),
 (120.35, 122.25, "O", "Unda shifokor bilan yurist kerak emasmi?"),
 (122.45, 123.3, "R", "Kerak."), (123.6, 126.6, "R", "Mening javoblarimni kimdir tekshirishi kerak."),
 (127.35, 129.85, "R", "Ayniqsa ish murakkab bo'lsa."), (130.5, 133.6, "R", "Yoki xato juda qimmat bo'lsa."),
 (133.85, 136.9, "O", "Kamera, tahlillar, shartnomalar..."), (137.0, 140.35, "O", "Telefonimga, pullarimga kirib olmaysanmi?"),
 (141.1, 143.65, "R", "Men parol so'ramayman."), (144.3, 145.55, "R", "Parolingni so'ragan «AI»dan qoch."), (145.85, 146.55, "R", "U AI emas, firibgar."),
 (147.0, 148.55, "O", "Unda oshpazni bo'shatamanmi?"),
 (149.05, 149.8, "R", "Yo'q."), (150.05, 153.3, "R", "Men lavash o'ray olmayman. Oshpaz qo'l, men ko'z."),
 (153.85, 155.1, "R", "Sizda ham do'kon bormi?"),
]
# Sahna kesimlari (s): sahna i = CUT[i-1]..CUT[i]
CUT = [0, 8.0, 13.3, 19.5, 27.8, 37.3, 44.5, 48.1, 56.2, 59.5, 71.3,
       79.6, 86.6, 96.7, 99.1, 109.55, 120.2, 122.35, 133.7, 140.7, 146.8, 153.5, 158.5]
CLIP = [f"s{i:02}" for i in range(1, 23)]
START = {9: 1.4}   # klipning qayeridan boshlanadi (sahna raqami: soniya)
STOP = (56.45, 59.4)  # 9-sahnada qizil STOP
# Egasi (2026-10-25): «Izohga LAVASH AI deb yozing» olib tashlandi (dialog_v2.flac, 155.3 s dan jim);
# o'rniga ekranda botga chaqiriq (yangi ovoz yozilmaydi). --voice dialog_v2.flac
TEXT = [
 (154.0, 158.5, "Botdan so'rang:", 70, "FFFFFF", (540, 330)),
 (154.0, 158.5, "@sahiychishopbot", 96, "FFC23A", (540, 430)),
 (155.3, 158.5, "Do'koningizga AI qanday yordam beradi?", 54, "FFFFFF", (540, 1250)),
]
# Musiqa VAQTINCHA (egasi 2026-10-18: boshi — Curious Unease — yaxshi; 1:10 dan Kafeda o'xshamadi, aralash bo'lib ketdi.
# Yakuniy musiqa butun video tayyor bo'lib, matn o'zgarishlari tugagach tanlanadi.)
# (egasining Suno treklari, bepul tarif: tijoratsiz, «Music: made with Suno»).
# (fayl, trekdagi boshlanish s, videodagi boshlanish s, videodagi oxiri s) — qismlar orasida 2 s o'tish.
MUSIC = [  # eski preview.py uchun (yakuniy musiqa: MUSIC_FADE izohi)
 ("curious_unease.mp3", 0.0, 0.0, 72.3),            # sir, xavotir: pul oqib ketyapti, lavash xatosi
 ("kafeda_inson_va_robot.mp3", 8.0, 70.3, 147.8),   # tinch suhbat: shifokor, yurist, tekshiruv
 ("doira_and_the_robot.mp3", 41.0, 145.8, 175.0),   # quvnoq doira: kulgu, chaqiriq, avatar, yakuniy karta
]
MUSIC_FADE = 5  # egasi (2026-10-25): Dutar's Whisper 10 s dan, avatar + yakuniy karta ustida 5 s da so'nadi
