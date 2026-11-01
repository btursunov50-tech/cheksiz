# «Telefon jiringlaydi» — build_tl.py yasaydi.
CUT = [0.0, 6.92, 9.89, 15.4, 22.75, 29.4, 34.19, 37.36, 43.16, 51.64, 61.42, 64.29, 74.4, 83.46]
CLIP = ['use/s01', 'use/s02', 'use/s03', 'use/s04', 'use/s05', 'use/s06', 'use/s07', 'use/s08', 'use/s09', 'use/s10', 'use/s11', 'use/s12', 'use/s13']
SUB = [
 (0.15, 6.57, 'R', 'Telefoning jiringlaganda sen telefonni emas, telefon seni boshqaradi.'),
 (7.07, 9.54, 'O', 'Usta, bir daqiqa, xabar keldi!'),
 (10.04, 12.26, 'R', 'Diyor, eshit.'),
 (12.26, 15.05, 'R', '2006-yil, Amerika.'),
 (15.55, 19.09, 'R', "Bir muhandis cheksiz aylantirishni o'ylab topdi:"),
 (19.09, 22.4, 'R', 'sahifa tugamaydi, pastga tushaverasan.'),
 (22.9, 26.15, 'R', "Sahifa tugasa, to'xtaysan."),
 (26.15, 29.05, 'R', "Tugamasa, to'xtamaysan."),
 (29.55, 33.84, 'R', 'Keyinchalik u shu ixtirosidan afsuslanishini ochiq aytdi.'),
 (34.34, 37.01, 'O', 'Ilovalar bizni ataylab ushlab turadimi?!'),
 (37.51, 42.81, 'R', "Bir tadqiqotga ko'ra, o'rtacha foydalanuvchi kuniga qirq oltitaga yaqin bildirishnoma oladi."),
 (43.31, 47.06, 'R', "Ilovalar sening e'tiboring bilan pul topadi:"),
 (47.06, 51.29, 'R', "qancha uzoq qarasang, shuncha ko'p reklama ko'rsatiladi."),
 (51.79, 52.95, 'R', 'Uchta qoida.'),
 (52.95, 55.5, 'R', "Keraksiz bildirishnomani o'chir."),
 (55.5, 57.36, 'R', 'Kechasi tinch rejimni yoq.'),
 (57.36, 59.91, 'R', "Ilovani ochishdan oldin so'ra:"),
 (59.91, 61.07, 'R', 'nega ochyapman?'),
 (61.57, 63.94, 'O', 'Telefon jim, men tinch!'),
 (64.44, 70.93, 'R', "Ular senga ilovani emas, «o'tkazib yuboraman» degan qo'rquvni sotadi."),
 (70.93, 71.97, 'R', "Har gal so'ra:"),
 (71.97, 74.05, 'R', "bundan kim foyda ko'radi?"),
 (74.55, 80.25, 'R', "Qaysi bildirishnomani o'chirishni bilmasangiz, ilova nomini botimizga yozing:"),
 (80.25, 81.27, 'R', '@sahiychishopbot.'),
 (81.27, 83.11, 'R', "Bosqichma-bosqich o'rgatadi."),
]
TEXT = [
 (0.2, 3.2, 'TELEFON SENI BOSHQARADI', 66, 'FFC23A', (540, 250)),
 (12.89, 15.3, '2006 · AQSh', 96, 'FFC23A', (540, 250)),
 (16.4, 22.65, 'CHEKSIZ AYLANTIRISH', 64, 'FFC23A', (540, 250)),
 (38.86, 43.06, 'KUNIGA ~46 TA BILDIRISHNOMA', 54, 'FFC23A', (540, 250)),
 (45.16, 51.54, "E'TIBOR = PUL", 80, 'FF4A3A', (540, 250)),
 (53.04, 55.24, "1. KERAKSIZINI O'CHIR", 60, 'FFC23A', (540, 250)),
 (55.34, 57.54, '2. KECHASI TINCH REJIM', 60, '5FD3A6', (540, 250)),
 (57.64, 61.32, '3. NEGA OCHYAPMAN?', 60, 'FF4A3A', (540, 250)),
 (69.79, 74.3, "BUNDAN KIM FOYDA KO'RADI?", 60, 'FFC23A', (540, 250)),
 (77.9, 83.46, '@sahiychishopbot', 96, 'FFC23A', (540, 250)),
]
MUSIC_FADE = 5
AV_LINE = (83.96, 88.0)
