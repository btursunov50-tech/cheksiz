# «70 foiz chegirma»: voice/NN_*.wav (Manus, har qator alohida) → dialog.wav + timeline.py (CUT, SUB, TEXT, AV_LINE, BOOM).
# Sahna uzunligi = shu sahnadagi ovoz + kichik tanaffus; har qator sahna kesimidan 0.15 s keyin boshlanadi.
# Qator ichidagi subtitr bo'linishlari: silencedetect (-40 dB, 0.2 s) pauzalari; pauzasiz qatorlarda bo'g'in soniga qarab.
# Ishlatish: python3 video/chegirma/build_tl.py  →  keyin prep_clips.py, keyin /video-yig
import os, subprocess
D = os.path.dirname(os.path.abspath(__file__)); V = os.path.join(D, "voice")
dur = lambda f: float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f],
                                     capture_output=True, text=True).stdout)
F = {int(n[:2]): os.path.join(V, n) for n in os.listdir(V) if n.endswith(".wav")}
L = {n: dur(f) for n, f in F.items()}

# (klip, sahna uzunligi, [(qator, sahna ichidagi boshlanishi)])
SC = [
    ("use/s01", L[1] + 0.45, [(1, 0.15)]),
    ("use/s02", L[2] + 0.5, [(2, 0.15)]),
    ("use/s03", L[3] + 0.45, [(3, 0.15)]),
    ("use/s04", L[4] + 0.4, [(4, 0.15)]),
    ("use/s05", 9.6, [(5, 0.15)]),             # 5.3–6.6 s sekinlashuv (yorliq tushadi) → klip 9.3 s; tushish ~7.9 s da
    ("use/s06", L[6] + 0.45, [(6, 0.15)]),
    ("use/s07", L[7] + 0.45, [(7, 0.15)]),
    ("use/s08", L[8] + 0.45, [(8, 0.15)]),
    ("use/s09", L[9] + 0.4, [(9, 0.15)]),
    ("use/s10", 2.4, []),                      # qiz o'tib ketadi, gap yo'q
    ("use/s10b", 8.0, [(10, 0.15), (11, 5.25)]),  # Diyor ~5 s da cho'chiydi
    ("use/s10c", L[12] + 0.45, [(12, 0.15)]),
    ("use/s11", L[13] + 0.45, [(13, 0.15)]),
    ("use/s12", L[14] + 0.45, [(14, 0.15)]),
]
CUT = [0.0]; AT = {}
for clip, d, lines in SC:
    for n, o in lines: AT[n] = round(CUT[-1] + o, 3)
    CUT.append(round(CUT[-1] + d, 3))
T = CUT[-1]; AT[15] = round(T + 0.5, 3)

# dialog.wav: hamma qatorlar o'z joyida; 15-qator (avatar) T dan keyin — yig.py AV_LINE bilan avatar ustiga oladi
ins, fc = [], ""
for i, n in enumerate(sorted(F)):
    ins += ["-i", F[n]]; fc += f"[{i}:a]aresample=48000,adelay={int(AT[n] * 1000)}:all=1[a{i}];"
fc += "".join(f"[a{i}]" for i in range(len(F))) + f"amix=inputs={len(F)}:normalize=0,apad=whole_dur={AT[15] + L[15] + 0.5}[o]"
subprocess.run(["ffmpeg", "-v", "error", "-y"] + ins + ["-filter_complex", fc, "-map", "[o]", "-ac", "1", os.path.join(D, "dialog.wav")], check=True)

U, O = "R", "O"   # R = Usta (sariq subtitr), O = Diyor (oq)
# qator → [(boshi, oxiri, matn)] qator ichidagi vaqtlar (s)
PARTS = {
    1: [(0.0, 2.53, "Bu yetmish foizlik chegirma"), (2.95, 4.49, "yetmish foiz emas."), (5.42, L[1], "To'lashdan oldin hisoblang.")],
    2: [(0.0, 1.3, "Usta, qarang! Uch yuz ming edi,"), (1.3, 2.45, "bir yuz yetmish ming bo'libdi!"), (2.45, L[2], "Hozir olmasam, yutqazaman!")],
    3: [(0.0, 2.3, "Bu narsani chegirmani ko'rishdan oldin"), (2.3, 3.73, "ham qidirayotgan edingmi?")],
    4: [(0.0, 0.9, "Yo'q..."), (0.96, L[4], "Chegirmani ko'rib qoldim.")],
    5: [(0.0, 0.73, "Hisoblaylik."), (1.24, 4.02, "Uch yuz mingdan bir yuz o'ttiz ming tushgan."), (4.69, 6.16, "Bu yetmish emas,"), (6.63, L[5], "qirq uch foiz.")],
    6: [(0.0, L[6], "Unda nega yetmish deb yozishgan?")],
    7: [(0.0, 1.61, "Katta raqam ko'zni,"), (2.31, 4.01, "taymer qo'lni shoshiltiradi."), (4.61, L[7], "Kerakli narsa shoshilishni talab qilmaydi.")],
    8: [(0.0, 0.75, "Uchta tekshiruv."), (1.44, 3.17, "Boshqa do'kondagi narxi qancha?"), (3.90, 6.20, "O'lchami, sifati, kafolati bir xilmi?"),
        (6.70, L[8], "Va shu mahsulot senga kecha ham kerakmidi?")],
    9: [(0.0, 1.88, "Demak, avval hisoblayman,"), (2.34, L[9], "keyin olaman.")],
    10: [(0.0, 0.86, "Hoy-hoy, Diyor!"), (0.86, 3.43, "Sen do'konda chegirma qidiryapsanmi"), (3.43, L[10], "yoki ko'chada kelin?")],
    11: [(0.0, L[11], "Yo'q, usta... men... hisoblayapman!")],
    12: [(0.0, 1.77, "Ko'zing narxda bo'lsin, ukam."), (2.33, L[12], "Avval hisob, keyin kelin!")],
    13: [(0.0, 1.91, "Xaridni foiz emas,"), (2.33, L[13], "ehtiyoj hal qilsin.")],
    14: [(0.0, 2.45, "Chegirma yorlig'ini suratga olib"), (2.71, 3.72, "botimizga yuboring:"), (3.72, 4.44, "@sahiychishopbot"),
         (4.44, 5.73, "Haqiqiy foizni hisoblab,"), (5.73, L[14], "nimani tekshirishni aytib beradi.")],
}
WHO = {n: (O if n in (2, 4, 6, 9, 11) else U) for n in PARTS}
SUB = [(round(AT[n] + a, 2), round(AT[n] + b, 2), WHO[n], t) for n in sorted(PARTS) for a, b, t in PARTS[n]]

c = lambda k: CUT[k - 1]   # k-sahna boshi (1 dan)
# ekrandagi katta yozuvlar (YOZUVLAR.md): (boshi, oxiri, matn, o'lcham, rang, (x, y))
TEXT = [
    (AT[2] + 0.4, c(3) - 0.1, "300 000 → 170 000", 84, "FFC23A", (540, 300)),
    (AT[5] + 1.24, AT[5] + 4.6, "300 000 − 170 000 = 130 000", 58, "FFC23A", (540, 170)),
    (AT[5] + 4.69, c(6) - 0.1, "130 000 ÷ 300 000 = 43%", 62, "FF4A3A", (540, 170)),
    (c(6) + 0.1, c(7) - 0.05, "70% BO'LSA: 90 000 BO'LARDI", 62, "FFC23A", (540, 300)),
    (c(7) + 0.2, c(8) - 0.1, "FAQAT BUGUN?", 90, "FF5EA8", (540, 300)),
    (AT[8] + 1.44, c(9) - 0.05, "1. BOSHQA DO'KON NARXI?", 60, "FFC23A", (540, 1180)),
    (AT[8] + 3.90, c(9) - 0.05, "2. O'LCHAM · SIFAT · KAFOLAT", 56, "FFC23A", (540, 1280)),
    (AT[8] + 6.70, c(9) - 0.05, "3. KECHA HAM KERAKMIDI?", 60, "FF4A3A", (540, 1380)),
    (AT[9] + 0.2, c(10) - 0.05, "AVVAL HISOB, KEYIN XARID", 70, "FFC23A", (540, 300)),
    (AT[12] + 2.33, c(13) - 0.05, "AVVAL HISOB, KEYIN KELIN!", 70, "FFC23A", (540, 300)),
    (AT[13] + 0.2, c(14) - 0.05, "FOIZ EMAS, EHTIYOJ", 80, "FFC23A", (540, 170)),
    (AT[14] + 2.71, T, "@sahiychishopbot", 96, "FFC23A", (540, 260)),
    (AT[14] + 4.44, T, "HAQIQIY FOIZNI HISOBLAYDI", 58, "FFFFFF", (540, 370)),
]
TEXT = [(round(a, 2), round(b, 2), x, s, col, p) for a, b, x, s, col, p in TEXT]
BOOM = [round(c(5) + 7.90, 2)]   # 5-sahna: pushti yorliq stolga tushadi (sekinlashuvdan keyin)

with open(os.path.join(D, "timeline.py"), "w") as f:
    f.write("# «70 foiz chegirma» — build_tl.py yasaydi (qo'lda o'zgartirmang, build_tl.py ni o'zgartiring).\n")
    f.write(f"CUT = {CUT}\nCLIP = {[s[0] for s in SC]}\n")
    f.write("SUB = [\n" + "".join(f" {x!r},\n" for x in SUB) + "]\n")
    f.write("TEXT = [\n" + "".join(f" {x!r},\n" for x in TEXT) + "]\n")
    f.write(f"BOOM = {BOOM}\nAV_LINE = ({AT[15]}, {round(AT[15] + L[15], 3)})\nMUSIC_FADE = 5\n")
print("T =", T, "| CUT:", CUT)
