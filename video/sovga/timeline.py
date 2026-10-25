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
    5: (0.0, 3.6),   # 1.6 s da barmoq ekranga tegadi (kichik), ~4 s dan oltin chaqnash, chaqmoq, ekran qorayib qizil ko'zlar yo'qoladi → ~1.8x
    6: (0.0, 8.0),
    7: [(0.0, 2.6), (5.0, 8.0)],   # 2.8–4.8 s eshikdan olov chiqib Tulkini qoplaydi (olov xato) → 2 bo'lak, ~1.3x
    8: [(0.0, 2.7), (3.7, 8.0)],   # 2.8–3.6 s sovg'a qutisi qum soatga «erib» o'tadi (ikki narsa ustma-ust) → 2 bo'lak, ~1.7x
    12: (0.0, 8.0),  # sekin dolly out, tepada sarlavha uchun bo'sh joy; ekranga bot suhbati qo'yiladi → ~1.4x
}
