# «Telefoning eskirmagan»: voice/NN_*.wav (ajrat.py) → dialog.wav + timeline.py (CUT, CLIP, SUB, TEXT, BOOM, AV_LINE).
# Sahna uzunligi = shu sahnadagi gaplar + tanaffus; har qator sahna boshidan 0.15 s keyin. Subtitr bo'linishi — silencedetect pauzalari.
# Ishlatish: python3 video/eskirish/build_tl.py
import os, subprocess
D = os.path.dirname(os.path.abspath(__file__)); V = os.path.join(D, "voice")
dur = lambda f: float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f], capture_output=True, text=True).stdout)
F = {int(n[:2]): os.path.join(V, n) for n in os.listdir(V) if n.endswith(".wav")}
L0 = {n: dur(f) for n, f in F.items()}          # asl (Manus) uzunliklar — PARTS vaqtlari shularda
TEMPO = float(os.environ.get("TEMPO", "1"))     # ovoz tezligi: 0.9 = 10% sekinroq (atempo, ohang o'zgarmaydi)
TP = {n: TEMPO for n in F}                       # qator bo'yicha tezlik: TEMPO_N="20:0.7,21:0.7"
for kv in filter(None, os.environ.get("TEMPO_N", "").split(",")): k, v = kv.split(":"); TP[int(k)] = float(v)
if any(v != 1 for v in TP.values()):
    VT = os.path.join(D, "voice_t"); os.makedirs(VT, exist_ok=True)
    for n, f in F.items():
        o = os.path.join(VT, os.path.basename(f))
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f, "-af", f"atempo={TP[n]}", o], check=True); F[n] = o
L = {n: dur(f) for n, f in F.items()}
GAP = 0.3
def sc(clip, lines):          # bir sahnada bir yoki ikki qator ketma-ket
    t, at = 0.15, []
    for n in lines: at.append((n, t)); t += L[n] + GAP
    return (clip, t - GAP + 0.35, at)
SC = [sc("use/s01", [1]), sc("use/s02", [2]), sc("use/s03", [3, 4]), sc("use/s04", [5]), sc("use/s05", [6]), sc("use/s06", [7]),
      sc("use/s06b", [8]), sc("use/s07", [9, 10]), sc("use/s08", [11]), sc("use/s09", [12]), sc("use/s10", [13]), sc("use/s11", [14, 15]),
      sc("use/s12", [16, 17]), sc("use/s13", [18]), sc("use/s14", [19]), sc("use/s15", [20])]
CUT = [0.0]; AT = {}
for clip, d, lines in SC:
    for n, o in lines: AT[n] = round(CUT[-1] + o, 3)
    CUT.append(round(CUT[-1] + d, 3))
T = CUT[-1]; AT[21] = round(T + 0.5, 3)
ins, fc = [], ""
for i, n in enumerate(sorted(F)):
    ins += ["-i", F[n]]; fc += f"[{i}:a]aresample=48000,adelay={int(AT[n] * 1000)}:all=1[a{i}];"
fc += "".join(f"[a{i}]" for i in range(len(F))) + f"amix=inputs={len(F)}:normalize=0,apad=whole_dur={AT[21] + L[21] + 0.5}[o]"
subprocess.run(["ffmpeg", "-v", "error", "-y"] + ins + ["-filter_complex", fc, "-map", "[o]", "-ac", "1", os.path.join(D, "dialog.wav")], check=True)

U, O = "R", "O"
PARTS = {
    1: [(0, 2.0, "Telefoning eskirmagan."), (2.0, L0[1], "Balki faqat batareyasi charchagandir.")],
    2: [(0, 2.98, "Usta, telefonim qotyapti, quvvati kechgacha yetmaydi."), (3.19, 4.60, "Ikki yil bo'ldi, eskirdi."), (4.85, L0[2], "Nasiyaga yangisini olaman!")],
    3: [(0, L0[3], "Diyor, kim aytdi telefon eskirgani uchun qotayotganini?")],
    4: [(0, L0[4], "Hamma biladi-ku!")],
    5: [(0, 2.01, "Jim, Diyor. Qara."), (2.66, L0[5], "Jeneva, 1924-yil, dekabr.")],
    6: [(0, 3.07, "Dunyodagi eng katta lampochka zavodlari kelishib oldi:"), (3.60, L0[6], "oddiy lampochka ming soatdan ortiq yonmasin.")],
    7: [(0, 2.8, "Undan oldin 2500 soatgacha yonardi."), (2.8, L0[7], "Uzoqroq yonadiganini chiqargan zavod jarima to'lardi.")],
    8: [(0, L0[8], "Ataylab-a?!")],
    9: [(0, 2.08, "2017-yil."), (2.61, L0[9], "Eng mashhur telefon kompaniyalaridan biri bir sirni tan oldi.")],
    10: [(0, L0[10], "Qanaqa sir?")],
    11: [(0, 3.23, "Batareyasi eskirgan telefonlarni o'zi sekinlashtirib qo'ygan."), (3.77, 5.20, "To'satdan o'chib qolmasin deb."), (5.68, L0[11], "Lekin egasiga aytmagan.")],
    12: [(0, 3.04, "Odamlar «telefonim eskirdi» deb, yangisini sotib olgan."), (3.64, L0[12], "Ko'pincha esa faqat batareyani almashtirish yetardi.")],
    13: [(0, 4.20, "Bu ochilgach, kompaniya Amerikada odamlarga yarim milliard dollargacha to'lashga rozi bo'ldi."), (4.64, L0[13], "Fransiyada 25 million yevro jarima oldi.")],
    14: [(0, 2.06, "Demak, mening telefonim ham eskirmagan,"), (2.34, L0[14], "shunchaki batareyasi charchagan bo'lishi mumkin?")],
    15: [(0, L0[15], "Bo'lishi mumkin.")],
    16: [(0, L0[16], "Kechir, eski do'stim... sen aybsiz ekansan!")],
    17: [(0, L0[17], "Quchoqlama, batareyasini tekshir!")],
    18: [(0, 2.04, "Yangisini olishdan oldin uchta tekshiruv."), (2.53, 4.04, "Batareya holati necha foiz?"), (4.58, 5.79, "Xotira to'lib qolmaganmi?"), (6.37, L0[18], "Batareya almashtirish qancha turadi?")],
    19: [(0, 3.37, "Ular senga telefon emas, «eskirding» degan tuyg'uni sotadi."), (3.85, L0[19], "Har gal so'ra: bundan kim foyda ko'radi?")],
    20: [(0, 2.6, "Telefoningiz qotyaptimi? Botimizga modelini yozing:"), (2.6, 3.9, "@sahiychishopbot"), (3.9, 6.4, "Batareya holatini qayerdan ko'rishni"), (6.4, L0[20], "va yangisini olishdan oldin nimani tekshirishni o'rgatadi.")],
}
PARTS = {n: [(x / TP[n], y / TP[n], t) for x, y, t in v] for n, v in PARTS.items()}
WHO = {n: (O if n in (2, 4, 8, 10, 14, 16) else U) for n in PARTS}
SUB = [(round(AT[n] + a, 2), round(AT[n] + b, 2), WHO[n], t) for n in sorted(PARTS) for a, b, t in PARTS[n]]
c = lambda k: CUT[k - 1]      # k-sahna boshi (SC tartibida, 1 dan)
TEXT = [
    (AT[5] + 2.66 / TP[5], c(5) - 0.1, "JENEVA · 1924", 96, "F2B544", (540, 300)),
    (c(5) + 0.3, c(6) - 0.1, "LAMPOCHKA: 1000 SOATDAN KO'P EMAS", 52, "F2B544", (540, 300)),
    (c(6) + 0.2, AT[7] + 2.8 / TP[7], "AVVAL: 2500 SOAT", 70, "F2B544", (540, 300)),
    (AT[7] + 2.8 / TP[7], c(7) - 0.1, "UZOQ YONSA — JARIMA", 66, "FF4A3A", (540, 300)),
    (AT[9], AT[9] + 2.6 / TP[9], "2017", 120, "F2B544", (540, 300)),
    (c(9) + 0.2, c(10) - 0.1, "ESKI BATAREYA → SEKIN TELEFON", 54, "FF4A3A", (540, 300)),
    (c(10) + 0.2, AT[12] + 3.0 / TP[12], "«ESKIRDI!» → YANGI TELEFON", 56, "F2B544", (540, 300)),
    (AT[12] + 3.6 / TP[12], c(11) - 0.1, "KO'PINCHA BATAREYA YETARDI", 56, "5FD3A6", (540, 300)),
    (AT[13] + 0.5 / TP[13], c(12) - 0.1, "AQSh: $500 000 000 GACHA", 62, "F2B544", (540, 250)),
    (AT[13] + 4.64 / TP[13], c(12) - 0.1, "FRANSIYA: €25 000 000", 62, "FF4A3A", (540, 340)),
    (AT[18] + 2.53 / TP[18], c(15) - 0.05, "1. BATAREYA HOLATI?", 62, "F2B544", (540, 1050)),
    (AT[18] + 4.58 / TP[18], c(15) - 0.05, "2. XOTIRA TO'LMAGANMI?", 62, "5FD3A6", (540, 1150)),
    (AT[18] + 6.37 / TP[18], c(15) - 0.05, "3. ALMASHTIRISH NARXI?", 62, "F2B544", (540, 1250)),
    (AT[19] + 3.85 / TP[19], c(16) - 0.05, "BUNDAN KIM FOYDA KO'RADI?", 64, "F2B544", (540, 300)),
    (AT[20] + 2.6 / TP[20], T, "@sahiychishopbot", 96, "F2B544", (540, 250)),
    (AT[20] + 3.9 / TP[20], T, "BATAREYANI TEKSHIRISHNI O'RGATADI", 50, "FFFFFF", (540, 360)),
]
TEXT = [(round(a, 2), round(b, 2), x, s, col, p) for a, b, x, s, col, p in TEXT]
BOOM = [round(c(12) + 3.0 * (CUT[12] - CUT[11]) / 6.0, 2)]   # 10-sahna: bolg'a zarbasi (klip 3 s da, sekinlashuvga moslab)
with open(os.path.join(D, "timeline.py"), "w") as f:
    f.write("# «Telefoning eskirmagan» — build_tl.py yasaydi (qo'lda o'zgartirmang).\n")
    f.write(f"CUT = {CUT}\nCLIP = {[s[0] for s in SC]}\n")
    f.write("SUB = [\n" + "".join(f" {x!r},\n" for x in SUB) + "]\n")
    f.write("TEXT = [\n" + "".join(f" {x!r},\n" for x in TEXT) + "]\n")
    f.write(f"BOOM = {BOOM}\nAV_LINE = ({AT[21]}, {round(AT[21] + L[21], 3)})\nMUSIC_FADE = 5\n")
print("T =", T, "| CUT:", CUT)
