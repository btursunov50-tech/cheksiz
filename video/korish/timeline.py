# «Ko'rish bor. Pul yo'q.» — yangi ovoz (2026-10-18), har qator alohida fayl: voice/NN_*.flac.
# VOICE: (fayl, oldidagi pauza s, kim, matn). Pauzalar montajda qo'yiladi (BOOM, ofitsiant qiz, yakun).
VOICE = [
 ("01_yigit1", 0.3, "Y1", "Yuz ming ko'rish, akajon!"),
 ("02_yigit2", 0.4, "Y2", "Yuz ming ko'rish. Nechta odam sotib oldi?"),
 ("03_yigit2", 1.5, "Y2", "Nol. Demak, bu savdo emas. Shovqin."),          # oldida BOOM + jimlik
 ("04_diktor", 0.6, "D", "Trend seni ko'rsatadi. Lekin sotmaydi. Odam yuz ming marta ko'rsa ham, nima sotayotganingni bilmasa, ketadi. Qaytmaydi."),
 ("05_yigit2", 3.0, "Y2", "Odamni yig'ish oson. Ushlab qolish qiyin. Ishingni ko'rsatmasang, u tomoshabin. Mijoz emas."),  # oldida ofitsiant qiz
 ("06_diktor", 0.6, "D", "Mahsulotni ko'rsat. Foydasini ayt. Boshqalardan farqini isbotla. Ko'rish ishonchga aylanadi. Ishonch buyurtmaga."),
 ("07_yigit2", 0.6, "Y2", "Operator shart emas. Katta kamera shart emas. Bitta surat. To'g'ri gap. Tamom."),
 ("08_yigit2", 1.2, "Y2", "Shovqin qilma. Ishingni ko'rsat."),            # musiqa to'xtaydi, keyin BOOM
]
# Qator uzunliklari (s): 2.04, 3.60, 7.20, 15.12, 12.14, 18.02, 9.02, 3.24 = 70.4. 01 yangi (adeclip + ohang 0.92: 211 -> 192 Hz, asli 01_yigit1_asl.flac); 07 yangi (chegaraga tegmaydi); pauzalar bilan ~78 s + avatar 3 + karta 4.

# --- Yig'ish (/video-yig, --voice ovoz.flac). ovoz.flac: python3 video/korish/ovoz.py; SUB vaqtlari pauzalar bo'yicha qo'lda tekshirilgan ---
# 2-ovoz (Manus, 2026-10-18): 01 «akajon» bilan qayta; 03 tezlashtirilgan («Nol» 1.5x, qolgani 1.2x, pauzalar 1 s gacha qisqartirilgan).
# SUB: (boshi, oxiri, "R" = diktor (ko'k) / "O" = yigitlar (oq), matn)
SUB = [
 (0.3, 3.43, "O", "Yuz ming ko'rish, akajon!"),
 (4.31, 5.68, "O", "Yuz ming ko'rish."), (6.31, 7.9, "O", "Nechta odam sotib oldi?"),
 (9.54, 10.47, "O", "Nol."), (11.17, 15.51, "O", "Demak, bu savdo emas."), (16.35, 17.38, "O", "Shovqin."),
 (18.09, 20.32, "R", "Trend seni ko'rsatadi."), (20.94, 22.37, "R", "Lekin sotmaydi."),
 (23.36, 26.1, "R", "Odam yuz ming marta ko'rsa ham,"), (26.23, 29.53, "R", "nima sotayotganingni bilmasa, ketadi."),
 (30.28, 31.2, "R", "Qaytmaydi."),
 (34.37, 36.83, "O", "Odamni yig'ish oson."), (37.5, 39.26, "O", "Ushlab qolish qiyin."),
 (40.21, 41.9, "O", "Ishingni ko'rsatmasang,"), (42.25, 43.96, "O", "u tomoshabin."), (44.72, 46.02, "O", "Mijoz emas."),
 (46.73, 48.9, "R", "Mahsulotni ko'rsat."), (49.52, 50.68, "R", "Foydasini ayt."),
 (51.2, 53.58, "R", "Boshqalardan farqini isbotla."), (54.4, 56.38, "R", "Ko'rish ishonchga aylanadi."),
 (56.69, 58.31, "R", "Ishonch buyurtmaga."),
 (59.48, 60.87, "O", "Operator shart emas."), (61.34, 62.97, "O", "Katta kamera shart emas."),
 (63.24, 64.22, "O", "Bitta surat."), (64.65, 65.44, "O", "To'g'ri gap."), (65.91, 66.57, "O", "Tamom."),
 (67.62, 68.98, "O", "Shovqin qilma."), (69.71, 70.87, "O", "Ishingni ko'rsat."),
]
# Sahnalar: s03 6.55 dan -> klipdagi keskin zoom (1.45 s) 8.0 ga, «Nechta odam sotib oldi?» dan keyingi jimlikka tushadi.
# 6-diktor qatori: non «Ko'rsat. Ayt», tikuvchi «isbotla», gulchi «ishonch -> buyurtma».
CUT = [0, 4.0, 6.55, 11.0, 17.6, 25.0, 31.4, 35.0, 40.0, 46.4, 51.0, 54.2, 58.9, 67.3, 71.6]
CLIP = ["s01", "s02", "s03", "s04", "s05a", "s05b", "s05w", "s06a", "s06b", "s07", "s08", "s09", "s10", "s11"]
START = {7: 1.5, 14: 1.4}
BOOM = [8.0]
MUSIC_END = 67.3   # musiqa oxirgi gapdan oldin to'xtaydi (shu kesimda zarba bor)
# Ekrandagi katta yozuvlar (ovozda yo'q): (boshi, oxiri, matn, o'lcham)
TEXT = [(0.4, 3.4, "100 000 KO'RISH", 120), (16.3, 17.6, "SHOVQIN", 170),
        (46.7, 49.4, "KO'RSAT", 170), (49.5, 51.0, "AYT", 190), (51.2, 54.1, "ISBOTLA", 170)]
