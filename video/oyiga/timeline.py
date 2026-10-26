# «Oyiga atigi…» — dialog.wav (76.36 s, Manus, 24 kHz mono) dagi ovoz qatorlari.
# Vaqtlar silencedetect (-40 dB, 0.3 s) bo'yicha; 2, 9, 11-qator ichidagi bo'linish bo'g'in soniga qarab (pauza topilmadi).
LINES = [
    (1, "USTA", 0.0, 6.12), (2, "DIYOR", 7.70, 11.84), (3, "USTA", 13.41, 15.66), (4, "DIYOR", 17.23, 24.06),
    (5, "USTA", 25.53, 29.36), (6, "DIYOR", 30.98, 36.43), (7, "USTA", 38.19, 43.44), (8, "USTA", 45.26, 53.59),
    (9, "DIYOR", 54.86, 57.60), (10, "USTA", 59.12, 64.69), (11, "USTA", 66.04, 76.06),
]
VOICE_END = 76.36

# Kliplarning ishlatiladigan qismi (README.md jadvali): xato chiqqan joydan oldin kesiladi.
CLIP_USE = {
    1: (0.0, 3.8),   # v2: 3.5 s dan yaqin planda yuz o'zgara boshlaydi → ~1.66x
    2: (0.0, 5.6),   # 6 s dan telefonni qulog'iga tutadi
    3: (2.0, 6.4),
    4: (0.0, 6.6),   # 7 s dan yuz o'zgaradi → ~1.26x
    5: (0.8, 7.0),   # tanga ~3.4 s da tushadi, 3.6 s da uchqun, ikkinchi ustun
    6: (2.8, 8.0),   # 1.4–2.6 s da Diyor yashil rangga bo'yalgan → ~1.38x
    7: (0.0, 7.6),
    8: (0.0, 6.8),   # 7 s dan belgilar so'nadi → ~1.41x
    9: (0.0, 4.4),
    10: (0.5, 7.5),
    11: (0.0, 8.0),  # ~1.32x; tepadagi qora tasma gradient bilan yumshatiladi, ustida @sahiychishopbot
}
# Montajda qo'shiladigan kamera harakati (kamera/harakat.py): Veo kamerani deyarli qimirlatmagan kliplar.
MOVE = {7: ("pushin", 0.10), 8: ("pushin", 0.08), 9: ("panleft", 0.06)}

# --- /video-yig uchun ---
# Sahna kesimlari: har sahna o'z ovoz qatoridan ~0.25 s oldin; 2-sahna 1-qator tugashi bilan (1-klip qisqa).
CUT = [0, 6.3, 13.15, 17.0, 25.3, 30.75, 37.95, 45.0, 54.6, 58.9, 65.8, 76.36]
CLIP = [f"use/s{i:02}" for i in range(1, 12)]
U, O = "R", "O"   # R = Usta (sariq subtitr), O = Diyor (oq)
SUB = [
 (0.1, 1.95, U, "Oyiga atigi yuz ming."), (2.66, 6.12, U, "Lekin jami qanchaligini hech kim aytmadi."),
 (7.70, 10.3, O, "Usta, oyiga atigi yuz ming ekan!"), (10.3, 11.84, O, "Bemalol olaman."),
 (13.41, 14.21, U, "Necha oyga?"), (14.54, 15.66, U, "Jami qancha to'laysan?"),
 (17.23, 18.45, O, "Yuz ming..."), (19.23, 20.67, O, "o'n ikki oy..."), (21.67, 24.06, O, "bir million ikki yuz ming."),
 (25.53, 27.63, U, "Bunga boshlang'ich to'lov,"), (27.97, 29.36, U, "xizmat haqi qo'shilsa-chi?"),
 (30.98, 33.66, O, "Sotuvchi faqat oylik to'lovni aytdi."), (34.91, 36.43, O, "Naqd narxini so'ramabman."),
 (38.19, 41.03, U, "Kichik bo'lingan narx katta summani yashiradi."), (41.71, 43.44, U, "Ikkalasini yonma-yon qo'y."),
 (45.26, 46.31, U, "Uchta savol ber."), (47.15, 48.68, U, "Naqd narxi qancha?"), (49.65, 51.24, U, "Jami qancha to'layman?"),
 (52.11, 53.59, U, "Kechiksam nima bo'ladi?"),
 (54.86, 55.9, O, "Shoshilmayman."), (55.9, 57.60, O, "Avval hisoblab ko'raman."),
 (59.12, 62.22, U, "«Oyiga atigi» degandan keyin bitta savol qoladi:"), (62.84, 64.69, U, "oxirida jami qancha?"),
 (66.04, 69.8, U, "Narx yorlig'i yoki shartnoma suratini botimizga yuboring:"), (69.8, 70.8, U, "@sahiychishopbot"),
 (70.8, 73.0, U, "Jami qancha to'lashingizni hisoblab,"), (73.0, 76.06, U, "sotuvchiga qaysi savollarni berishni aytib beradi."),
]
# Ekrandagi katta yozuvlar: (boshi, oxiri, matn, o'lcham, rang, (x, y)). Raqamlar misol (ssenariy).
TEXT = [
 (0.1, 6.2, "OYIGA ATIGI 100 000", 84, "FFC23A", (540, 260)),
 (13.41, 16.9, "12 OY", 110, "FF4A3A", (540, 300)),
 (21.67, 24.9, "100 000 × 12 = 1 200 000", 66, "FFC23A", (540, 300)),
 (25.53, 30.6, "+ BOSHLANG'ICH TO'LOV", 64, "FF4A3A", (540, 260)),
 (27.97, 30.6, "+ XIZMAT HAQI", 64, "FF4A3A", (540, 350)),
 (47.15, 54.5, "1. NAQD NARXI?", 70, "FFC23A", (540, 980)),
 (49.65, 54.5, "2. JAMI QANCHA?", 70, "FFC23A", (540, 1080)),
 (52.11, 54.5, "3. KECHIKSA-CHI?", 70, "FF4A3A", (540, 1180)),
 (62.84, 65.7, "OXIRIDA JAMI QANCHA?", 74, "FFC23A", (540, 300)),
 (69.8, 76.3, "@sahiychishopbot", 96, "FFC23A", (540, 260)),
]
BOOM = [27.9]       # 5-sahna: ikkinchi ustun uchqun bilan o'sib chiqadi
COIN = [27.65]      # 5-sahna: qizil tanga ustunga tushgan payt (jiring) — prep_clips.py dialog_fx.wav ga qo'shadi
MUSIC_FADE = 5
