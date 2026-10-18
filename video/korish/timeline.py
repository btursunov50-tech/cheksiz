# «Ko'rish bor. Pul yo'q.» — yangi ovoz (2026-10-18), har qator alohida fayl: voice/NN_*.flac.
# VOICE: (fayl, oldidagi pauza s, kim, matn). Pauzalar montajda qo'yiladi (BOOM, ofitsiant qiz, yakun).
VOICE = [
 ("01_yigit1", 0.3, "Y1", "Yuz ming ko'rish, brat!"),
 ("02_yigit2", 0.4, "Y2", "Yuz ming ko'rish. Nechta odam sotib oldi?"),
 ("03_yigit2", 1.5, "Y2", "Nol. Demak, bu savdo emas. Shovqin."),          # oldida BOOM + jimlik
 ("04_diktor", 0.6, "D", "Trend seni ko'rsatadi. Lekin sotmaydi. Odam yuz ming marta ko'rsa ham, nima sotayotganingni bilmasa, ketadi. Qaytmaydi."),
 ("05_yigit2", 3.0, "Y2", "Odamni yig'ish oson. Ushlab qolish qiyin. Ishingni ko'rsatmasang, u tomoshabin. Mijoz emas."),  # oldida ofitsiant qiz
 ("06_diktor", 0.6, "D", "Mahsulotni ko'rsat. Foydasini ayt. Boshqalardan farqini isbotla. Ko'rish ishonchga aylanadi. Ishonch buyurtmaga."),
 ("07_yigit2", 0.6, "Y2", "Operator shart emas. Katta kamera shart emas. Bitta surat. To'g'ri gap. Tamom."),
 ("08_yigit2", 1.2, "Y2", "Shovqin qilma. Ishingni ko'rsat."),            # musiqa to'xtaydi, keyin BOOM
]
# Qator uzunliklari (s): 2.04, 3.60, 7.20, 15.12, 12.14, 18.02, 9.02, 3.24 = 70.4. 01 yangi (adeclip + ohang 0.92: 211 -> 192 Hz, asli 01_yigit1_asl.flac); 07 yangi (chegaraga tegmaydi); pauzalar bilan ~78 s + avatar 3 + karta 4.

# --- Yig'ish (/video-yig, --voice ovoz.flac). ovoz.flac va SUB vaqtlari: python3 video/korish/ovoz.py ---
# SUB: (boshi, oxiri, "R" = diktor (sariq) / "O" = yigitlar (oq), matn)
SUB = [
 (0.57, 2.12, "O", "Yuz ming ko'rish, brat!"),
 (2.74, 4.29, "O", "Yuz ming ko'rish."), (4.88, 6.17, "O", "Nechta odam sotib oldi?"),
 (8.11, 8.92, "O", "Nol."), (9.69, 12.36, "O", "Demak, bu savdo emas."), (13.52, 14.39, "O", "Shovqin."),
 (15.96, 18.51, "R", "Trend seni ko'rsatadi."), (19.05, 20.41, "R", "Lekin sotmaydi."),
 (21.31, 23.97, "R", "Odam yuz ming marta ko'rsa ham,"), (24.3, 27.88, "R", "nima sotayotganingni bilmasa, ketadi."),
 (28.36, 29.8, "R", "Qaytmaydi."),
 (33.76, 35.9, "O", "Odamni yig'ish oson."), (36.3, 38.27, "O", "Ushlab qolish qiyin."),
 (39.18, 42.23, "O", "Ishingni ko'rsatmasang, u tomoshabin."), (43.2, 45.06, "O", "Mijoz emas."),
 (46.5, 48.86, "R", "Mahsulotni ko'rsat."), (49.3, 51.15, "R", "Foydasini ayt."),
 (52.58, 55.61, "R", "Boshqalardan farqini isbotla."), (57.03, 59.79, "R", "Ko'rish ishonchga aylanadi."),
 (61.39, 63.86, "R", "Ishonch buyurtmaga."),
 (65.12, 67.1, "O", "Operator shart emas."), (67.49, 69.3, "O", "Katta kamera shart emas."),
 (69.71, 70.91, "O", "Bitta surat."), (71.67, 72.37, "O", "To'g'ri gap."), (72.83, 73.55, "O", "Tamom."),
 (75.69, 76.77, "O", "Shovqin qilma."), (77.43, 78.38, "O", "Ishingni ko'rsat."),
]
# Sahnalar: s03 4.9 dan boshlanadi -> klipdagi keskin zoom (1.45 s) 6.35 ga, ya'ni «Nechta odam sotib oldi?» tugagan joyga tushadi.
# 6-diktor qatori: non «Ko'rsat. Ayt», tikuvchi «isbotla», gulchi «ishonch -> buyurtma» (guldasta xaridorga o'tadi).
CUT = [0, 2.6, 4.9, 9.5, 15.4, 23.9, 30.8, 34.4, 39.0, 46.3, 51.9, 56.6, 64.8, 74.6, 79.2]
CLIP = ["s01", "s02", "s03", "s04", "s05a", "s05b", "s05w", "s06a", "s06b", "s07", "s08", "s09", "s10", "s11"]
START = {7: 1.5, 14: 1.4}
BOOM = [6.35]
# Ekrandagi katta yozuvlar (ovozda yo'q): (boshi, oxiri, matn, o'lcham)
TEXT = [(0.4, 2.5, "100 000 KO'RISH", 120), (13.4, 15.3, "SHOVQIN", 170),
        (46.5, 49.2, "KO'RSAT", 170), (49.3, 52.4, "AYT", 190), (52.6, 56.5, "ISBOTLA", 170)]
