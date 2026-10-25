# «Sovg'a yutdingiz!» — dialog.wav (95.68 s, 24 kHz mono) dagi ovoz qatorlari.
# Vaqtlar silencedetect (-35 dB, 0.45 s) bo'yicha; egasi tekshirishi kerak: 19.7 s, 77.3 s, 84.0 s.
LINES = [
    # (qator, kim, boshlanish, tugash)
    (1, "USTA", 1.11, 5.25),
    (2, "DIYOR", 6.82, 10.75),
    (3, "TELEFON", 12.21, 18.06),
    (4, "DIYOR", 19.73, 20.34),
    (5, "USTA", 22.00, 25.71),
    (6, "DIYOR", 27.19, 32.70),
    (7, "USTA", 34.36, 41.45),
    (8, "USTA", 43.06, 49.04),
    (9, "USTA", 50.73, 60.97),
    (10, "USTA", 62.60, 71.23),
    (11, "DIYOR", 72.85, 76.74),
    (12, "USTA", 77.35, 82.65),
    (13, "USTA", 84.04, 94.38),
]
VOICE_END = 95.68  # keyin avatar 3 s + yakuniy karta 4 s

# Kliplarning ishlatiladigan qismi (klip ichidagi soniyalar): xato chiqqan joydan oldin kesiladi.
CLIP_USE = {
    1: [(0.0, 1.2), (5.0, 8.0)],   # 1.2 s dan oq «komiks» chiziqlar, chiroqdan olov chiqadi (1.6–4.6 s) → ikki bo'lak: keng kadr + kalit va Tulki ko'zlari yaqin plani, ~1.3x
    2: (0.0, 3.0),
    3: (0.0, 8.0),   # v2: Tulki ko'zlari qizil va hiylakor oxirigacha; Diyor 4.8 s dan xavotirli → ~1.2x   # v2: 3 s dan keyin qum soatda qum tepaga to'planadi (teskari), sovg'a qimirlab ketadi → ~1.8x sekinlashadi
    4: (0.0, 6.0),   # Diyor 5 s dan keyin kadrdan chiqadi, oxiri Ustada
    5: (0.0, 4.0),   # 1.6 s da barmoq ekranga tegadi (kichik), ~4 s dan oltin chaqnash, chaqmoq, ekran qorayib qizil ko'zlar yo'qoladi → ~1.8x
    6: (0.0, 8.0),
    7: [(0.0, 2.6), (5.0, 8.0)],   # 2.8–4.8 s eshikdan olov chiqib Tulkini qoplaydi (olov xato) → 2 bo'lak, ~1.3x
    8: [(0.0, 2.7), (3.7, 8.0)],   # 2.8–3.6 s sovg'a qutisi qum soatga «erib» o'tadi (ikki narsa ustma-ust) → 2 bo'lak, ~1.7x
    9: (0.0, 5.8),   # 5.4 s dan Diyor hovliga «sakrab» kichrayib qoladi; 3 s dan stolda ikkinchi kalit (kichik) → ~1.85x
    10: (0.0, 4.6),  # v2: Diyor xotirjam jilmayadi; 4.7 s dan o'ng tepada ingichka chaqmoq → ~1.15x
    11: (0.0, 8.0),  # sekin yaqinlashish, Usta va chiroq o'zgarmaydi; sahna ~5.5 s, kerakli qismi olinadi
    12: (0.0, 8.0),  # sekin dolly out, tepada sarlavha uchun bo'sh joy; ekranga bot suhbati qo'yiladi → ~1.4x
}

# --- /video-yig uchun ---
# Sahna kesimlari: har sahna o'z ovoz qatoridan ~0.25 s oldin boshlanadi (12 sahna).
CUT = [0, 6.6, 12.0, 21.8, 27.0, 34.1, 42.8, 50.5, 62.3, 72.6, 77.1, 83.8, 95.68]
# CLIP_USE bo'laklari prep_clips.py bilan clips/use/sNN.mp4 ga yig'iladi.
CLIP = [f"use/s{i:02}" for i in range(1, 13)]
U, O = "R", "O"   # R = Usta (sariq subtitr), O = Diyor va Telefon (oq)
SUB = [
 (1.11, 2.0, U, "To'xta!"), (2.0, 5.25, U, "«Siz yutdingiz» degan notanishga SMS kodni hech qachon o'qib berma."),
 (6.82, 8.3, O, "Voy! iPhone yutibman!"), (8.95, 10.77, O, "Faqat besh daqiqa vaqt bor ekan."),
 (12.21, 14.6, O, "Assalomu alaykum, bankdan bezovta qilyapman."), (14.6, 15.8, O, "Sizga kod keldi."),
 (15.8, 18.06, O, "Shuni ayting, sovg'angizni rasmiylashtiramiz."), (19.73, 20.8, O, "Hozir, hozir..."),
 (22.0, 25.71, U, "Kodni aytishdan oldin, SMSni menga ovoz chiqarib o'qi."),
 (27.19, 28.9, O, "Telegram kodi..."), (30.59, 32.7, O, "«Bu kodni hech kimga bermang»..."),
 (34.36, 35.9, U, "Bu sovg'a kodi emas."), (35.9, 37.92, U, "Bu sening Telegramingning kaliti."),
 (38.54, 41.45, U, "Kalitni bersang, eshikni o'zing ochib berasan."),
 (43.06, 44.88, U, "Ular sovg'a bermaydi."), (45.35, 49.04, U, "Sening nomingdan yaqinlaringdan pul so'rashadi."),
 (50.73, 51.6, U, "Uchta belgi."), (52.47, 54.05, U, "Tanlovda qatnashmagansan."), (54.94, 56.0, U, "Shoshiltirishyapti."),
 (56.93, 57.87, U, "Kod so'rashyapti."), (58.87, 60.97, U, "Uchalasi bo'lsa, bu tuzoq."),
 (62.6, 63.4, U, "Go'shakni qo'y."), (63.82, 66.42, U, "Bankka o'zing rasmiy raqamdan qo'ng'iroq qil."),
 (66.8, 68.84, U, "Telegramda bulutli parolni yoq:"), (69.29, 71.23, U, "kodni bilib olishsa ham, kira olmaydi."),
 (72.85, 74.7, O, "Besh daqiqa tugadi."), (75.35, 76.74, O, "Men esa hech narsa yo'qotmadim."),
 (77.35, 82.65, U, "Haqiqiy sovg'a senga hech qachon kod so'ratmaydi."),
 (84.04, 85.16, U, "Shubhali xabar keldimi?"), (85.48, 88.73, U, "Skrinshotini botimizga yuboring: @sahiychishopbot"),
 (88.93, 91.6, U, "Firibgarlikmi yo'qmi, tushuntiradi,"), (91.6, 94.39, U, "bulutli parolni qanday yoqishni bosqichma-bosqich o'rgatadi."),
]
# Ekrandagi katta yozuvlar: (boshi, oxiri, matn, o'lcham, rang, (x, y))
TEXT = [
 (52.47, 62.0, "1. TANLOV YO'Q", 70, "FF4A3A", (540, 420)),
 (54.94, 62.0, "2. SHOSHILTIRISH", 70, "FF4A3A", (540, 520)),
 (56.93, 62.0, "3. KOD SO'RASH", 70, "FF4A3A", (540, 620)),
 (85.48, 95.6, "@sahiychishopbot", 96, "FFC23A", (540, 300)),
]
MUSIC_FADE = 5  # musiqa avatar va yakuniy karta ustida davom etib, 5 s da so'nadi
