# «Oyiga 490 million» — build_tl.py yasaydi.
CUT = [0.0, 3.46, 7.12, 11.91, 16.9, 21.23, 32.79, 43.4, 51.84, 62.01, 69.78, 83.8, 87.49, 98.44]
CLIP = ['use/s01', 'use/s02', 'use/s03', 'use/s04', 'use/s05', 'use/s06', 'use/s07', 'use/s08', 'use/s09', 'use/s10', 'use/s11', 'use/s12', 'use/s13']
SUB = [
 (0.15, 3.06, 'R', "Oyiga to'rt yuz to'qson million so'm."),
 (3.06, 4.65, 'R', 'Tajriba shart emas.'),
 (4.65, 6.76, 'R', 'Ariza topshirasizmi?'),
 (7.27, 8.33, 'R', 'Post shunday deydi:'),
 (8.33, 16.56, 'R', "Claude odamlarni masofaviy ishga taklif qilmoqda, ariza 22-noyabrgacha, vazifa — sun'iy intellektni aylanib o'tish."),
 (17.05, 18.86, 'R', "Men, Claude, o'zim tekshirdim."),
 (18.86, 20.88, 'R', 'Bunday vakansiya topilmadi.'),
 (21.38, 22.86, 'R', 'Lekin asosi haqiqiy:'),
 (22.86, 24.88, 'R', "Anthropic'da xavfsizlik dasturi bor."),
 (24.88, 32.44, 'R', "Tadqiqotchilar Claude'ning himoyasidagi zaif joyni topib, kompaniyaga yashirin xabar beradi va mukofot oladi."),
 (32.94, 35.08, 'R', 'Bu oylik maosh emas.'),
 (35.08, 43.05, 'R', "Bu topilgan har bir zaiflik uchun mukofot, eng ko'pi taxminan o'ttiz besh ming dollar."),
 (43.55, 45.03, 'R', 'Va «tajribasiz» ham emas:'),
 (45.03, 47.98, 'R', 'yangi zaiflikni topish uchun chuqur bilim kerak.'),
 (47.98, 51.49, 'R', "Postning o'zi ham muhandislar va olimlarni afzal ko'radi."),
 (51.99, 53.33, 'R', 'Qizil bayroqlar:'),
 (53.33, 61.66, 'R', "manba yo'q, havola yo'q, «shoshiling» degan muddat, va «kimga yuborishni bilasiz» degan klik tuzog'i."),
 (62.16, 69.43, 'R', "Firibgarlar aynan shunday e'lon bilan pasport, karta va tasdiq kodini so'raydi, yoki oldindan pul oladi."),
 (69.93, 71.34, 'R', 'Uchta qoida.'),
 (71.34, 76.97, 'R', 'Vakansiyani faqat kompaniyaning rasmiy saytidan tekshiring.'),
 (76.97, 81.76, 'R', "Ish beruvchi oldindan pul, karta yoki kod so'ramaydi."),
 (81.76, 83.45, 'R', "Shoshiltirsa, to'xtang."),
 (83.95, 85.01, 'R', "Har gal so'rang:"),
 (85.01, 87.14, 'R', "bundan kim foyda ko'radi?"),
 (87.64, 91.99, 'R', 'Shubhali post yoki vakansiya matnini botimizga yuboring:'),
 (91.99, 93.08, 'R', '@sahiychishopbot.'),
 (93.08, 98.09, 'R', "Qizil bayroqlarni topib, qanday tekshirishni bosqichma-bosqich o'rgatadi."),
]
TEXT = [
 (0.2, 3.4, 'OYIGA 490 MILLION?', 70, 'FFC23A', (540, 250)),
 (17.4, 21.13, 'VAKANSIYA TOPILMADI', 58, 'FF4A3A', (540, 250)),
 (22.23, 32.69, 'BUG BOUNTY = ZAIFLIK UCHUN MUKOFOT', 44, 'FFC23A', (540, 250)),
 (35.79, 43.3, 'OYLIK EMAS', 80, 'FF4A3A', (540, 250)),
 (43.9, 51.74, 'TAJRIBASIZ EMAS', 62, 'FFC23A', (540, 250)),
 (52.64, 61.91, 'QIZIL BAYROQLAR', 70, 'FF4A3A', (540, 250)),
 (72.38, 75.58, '1. RASMIY SAYT', 60, 'FFC23A', (540, 250)),
 (75.78, 79.18, "2. PUL, KARTA, KOD SO'RAMAYDI", 46, '5FD3A6', (540, 250)),
 (79.38, 83.7, "3. SHOSHILTIRSA, TO'XTANG", 52, 'FF4A3A', (540, 250)),
 (84.1, 87.39, "BUNDAN KIM FOYDA KO'RADI?", 56, 'FFC23A', (540, 250)),
 (91.49, 94.99, '@sahiychishopbot', 96, 'FFC23A', (540, 250)),
]
MUSIC_FADE = 5
AV_LINE = (98.94, 102.874)
