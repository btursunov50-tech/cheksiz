# «Bepul yetkazish»: kliplarni clips/use/ ga kesadi (Diyorli sahnalar neon bilan) va timeline.py yasaydi.
# voice/NN_*.wav (ajrat.py) bo'lsa — sahna uzunligi ovozdan, SUB va AV_LINE qo'shiladi; bo'lmasa — taxminiy uzunlik, ovozsiz.
# Ishlatish: python3 video/yetkazish/build_tl.py  →  yig.py --dir video/yetkazish --voice dialog.wav ...
import os, re, subprocess
D = os.path.dirname(os.path.abspath(__file__)); C = os.path.join(D, "clips"); U = os.path.join(C, "use"); os.makedirs(U, exist_ok=True)
# sahna: (manba klip, ishlatiladigan qism, gap)
S = [
 ("s01_n", 0, 6.0, "Bepul yetkazish bepul emas. Uning pulini baribir to'laysan."),
 ("s02_n", 0, 7.3, "Usta, shampun oldim, yetkazish yigirma ming ekan. Yana qirq minglik narsa qo'shsam, bepul bo'larkan!"),
 ("s03_n", 0, 6.0, "O'sha qirq minglik narsa senga kerakmi? Unchalik emas... lekin bepul-ku!"),
 ("s04", 0, 6.0, "Jim, Diyor. Qara. Ikki ming ikkinchi yil, Amerika."),
 ("s05", 0, 8.0, "Dunyodagi eng katta onlayn do'kon bepul yetkazishni to'qson to'qqiz dollardan qirq to'qqiz dollarga, ikki oydan keyin yigirma besh dollarga tushirdi."),
 ("s06", 0, 8.0, "Odamlar chegaraga yetish uchun savatga yana narsa qo'shdi. Do'kon buni ijobiy natija deb e'lon qildi."),
 ("s07_n", 0, 2.4, "Bizni sanashgan ekan-da?!"),
 ("s08", 0, 5.0, "Faqat Fransiyada yetkazish uchun bir frank, ya'ni yigirma sent olishgan. U yerda sotuv deyarli o'smagan."),
 ("s09", 0, 6.0, "Narxni nolga tushirishgan zahoti, u yerda ham sotuv o'sib ketdi."),
 ("s10_y", 0, 8.0, "Olimlar sinab ko'rgan: qimmat shokoladni ko'pchilik tanlagan. Arzonini bepul qilishgan zahoti, hamma bepuliga o'tgan."),
 ("s11_n", 0, 8.0, "Demak, bepul so'zi miyani aldaydi? Aldamaydi. Shoshiltiradi."),
 ("s12_n", 0, 7.0, "Hisobla: yigirma ming tejading, qirq ming sarflading."),
 ("s13", 0, 8.0, "Uchta qoida. Faqat kerakli narsani ol. Yaqinda baribir oladigan narsalarni bitta buyurtmaga yig'. Va so'ra: yetkazish pullik bo'lmaganida ham shuni olarmidim?"),
 ("s14", 0, 8.0, "Ular senga yetkazishni emas, tekin degan tuyg'uni sotadi. Har gal so'ra: bundan kim foyda ko'radi?"),
 ("s15_n", 0, 7.5, "Savatingizdagi narsalarni va yetkazish shartini botimizga yozing. Bepul yetkazish uchun ortiqcha qancha to'layotganingizni hisoblab, nimani olib tashlash mumkinligini aytadi."),
]
syl = lambda t: len(re.findall(r"o'|g'|[aeiouAEIOU]", t))
V = os.path.join(D, "voice")
VF = sorted(f for f in os.listdir(V) if f.endswith(".wav")) if os.path.isdir(V) else []
dur = lambda f: float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f], capture_output=True, text=True).stdout)
L = {int(f[:2]): dur(os.path.join(V, f)) for f in VF}
# ovoz tartibi (ajrat.py): sahna → qatorlar
LINES = {1: [1], 2: [2], 3: [3, 4], 4: [5], 5: [6], 6: [7], 7: [8], 8: [9], 9: [10], 10: [11], 11: [12, 13], 12: [14], 13: [15], 14: [16], 15: [17]}
TXT = {1: "Bepul yetkazish bepul emas. Uning pulini baribir to'laysan.", 2: "Usta, shampun oldim, yetkazish yigirma ming ekan. Yana qirq minglik narsa qo'shsam, bepul bo'larkan!",
 3: "O'sha qirq minglik narsa senga kerakmi?", 4: "Unchalik emas... lekin bepul-ku!", 5: "Jim, Diyor. Qara. 2002-yil, Amerika.",
 6: "Dunyodagi eng katta onlayn do'kon bepul yetkazishni 99 dollardan 49 dollarga, ikki oydan keyin 25 dollarga tushirdi.",
 7: "Odamlar chegaraga yetish uchun savatga yana narsa qo'shdi. Do'kon buni «ijobiy natija» deb e'lon qildi.", 8: "Bizni sanashgan ekan-da?!",
 9: "Faqat Fransiyada yetkazish uchun bir frank, ya'ni yigirma sent olishgan. U yerda sotuv deyarli o'smagan.",
 10: "Narxni nolga tushirishgan zahoti, u yerda ham sotuv o'sib ketdi.",
 11: "Olimlar sinab ko'rgan: qimmat shokoladni ko'pchilik tanlagan. Arzonini «bepul» qilishgan zahoti, hamma bepuliga o'tgan.",
 12: "Demak, «bepul» so'zi miyani aldaydi?", 13: "Aldamaydi. Shoshiltiradi.", 14: "Hisobla: yigirma ming tejading, qirq ming sarflading.",
 15: "Uchta qoida. Faqat kerakli narsani ol. Yaqinda baribir oladigan narsalarni bitta buyurtmaga yig'. Va so'ra: yetkazish pullik bo'lmaganida ham shuni olarmidim?",
 16: "Ular senga yetkazishni emas, «tekin» degan tuyg'uni sotadi. Har gal so'ra: bundan kim foyda ko'radi?",
 17: "Savatingizdagi narsalarni va yetkazish shartini botimizga yozing: @sahiychishopbot. Bepul yetkazish uchun ortiqcha qancha to'layotganingizni hisoblab, nimani olib tashlash mumkinligini aytadi."}
DIYOR = {2, 4, 8, 12}
GAP = 0.3
CUT = [0.0]; CLIP = []; AT = {}
for i, (src, a, b, line) in enumerate(S, 1):
    n = f"s{i:02}"; out = os.path.join(U, n + ".mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(C, src + ".mp4"), "-vf",
                    f"trim={a}:{b},setpts=PTS-STARTPTS,scale=720:1280,setsar=1,fps=24", "-an", "-c:v", "libx264", "-crf", "16", out], check=True)
    if L:
        t = 0.15
        for q in LINES[i]: AT[q] = round(CUT[-1] + t, 3); t += L[q] + GAP
        d = t - GAP + 0.35
    else:
        d = min(max(syl(line) / 4.6 * 1.1 + 0.4, 3.0), (b - a) * 1.75)
    CUT.append(round(CUT[-1] + d, 2)); CLIP.append("use/" + n)
T = CUT[-1]
c = lambda k: CUT[k - 1]
TEXT = [
    (c(2) + 1.0, c(3) - 0.1, "YETKAZISH: 20 000", 70, "FFC23A", (540, 260)),
    (c(2) + 3.2, c(3) - 0.1, "+40 000 → BEPUL?", 70, "FF4A3A", (540, 360)),
    (c(4) + 1.2, c(5) - 0.1, "2002 · AQSh", 96, "FFC23A", (540, 250)),
    (c(5) + 0.8, c(6) - 0.1, "$99 → $49 → $25", 84, "FFC23A", (540, 250)),
    (c(6) + 0.8, c(7) - 0.1, "SAVATGA YANA NARSA", 64, "FFC23A", (540, 250)),
    (c(8) + 0.8, c(9) - 0.1, "FRANSIYA: 1 FRANK", 72, "FFC23A", (540, 250)),
    (c(9) + 0.6, c(10) - 0.1, "0 → SOTUV O'SDI", 72, "5FD3A6", (540, 250)),
    (c(10) + 0.8, c(11) - 0.1, "«BEPUL» → HAMMA SHUNI OLDI", 54, "FFC23A", (540, 250)),
    (c(12) + 0.6, c(13) - 0.1, "TEJADI: 20 000", 70, "5FD3A6", (540, 250)),
    (c(12) + 2.0, c(13) - 0.1, "SARFLADI: 40 000", 70, "FF4A3A", (540, 350)),
    (c(13) + 1.2, c(14) - 0.1, "1. FAQAT KERAKLISI", 62, "FFC23A", (540, 1050)),
    (c(13) + 3.5, c(14) - 0.1, "2. BITTA BUYURTMAGA YIG'", 58, "5FD3A6", (540, 1150)),
    (c(13) + 6.5, c(14) - 0.1, "3. PULLIK BO'LSA HAM OLARMIDIM?", 50, "FF4A3A", (540, 1250)),
    (c(14) + 4.5, c(15) - 0.1, "BUNDAN KIM FOYDA KO'RADI?", 64, "FFC23A", (540, 250)),
    (c(15) + 2.0, T, "@sahiychishopbot", 96, "FFC23A", (540, 250)),
    (c(15) + 3.5, T, "ORTIQCHA XARAJATNI HISOBLAYDI", 50, "FFFFFF", (540, 360)),
]
TEXT = [(round(a, 2), round(b, 2), x, s, col, p) for a, b, x, s, col, p in TEXT]
SUB = []
if L:
    AT[18] = round(T + 0.5, 3)
    for q, txt in TXT.items():   # qator ichida gaplarga bo'linadi, vaqt bo'g'inga mutanosib
        parts = [p.strip() for p in re.split(r"(?<=[.!?:])\s+", txt) if p.strip()]
        tot = sum(max(syl(p), 1) for p in parts); t0 = AT[q]
        for p in parts:
            d = L[q] * max(syl(p), 1) / tot
            SUB.append((round(t0, 2), round(t0 + d, 2), "O" if q in DIYOR else "R", p)); t0 += d
    ins, fc = [], ""
    for k, f in enumerate(VF):
        q = int(f[:2]); ins += ["-i", os.path.join(V, f)]; fc += f"[{k}:a]aresample=48000,adelay={int(AT[q] * 1000)}:all=1[a{k}];"
    fc += "".join(f"[a{k}]" for k in range(len(VF))) + f"amix=inputs={len(VF)}:normalize=0,apad=whole_dur={AT[18] + L[18] + 0.5}[o]"
    subprocess.run(["ffmpeg", "-v", "error", "-y"] + ins + ["-filter_complex", fc, "-map", "[o]", "-ac", "1", os.path.join(D, "dialog.wav")], check=True)
else:
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=mono", "-t", str(T + 0.5), os.path.join(D, "dialog.wav")], check=True)
with open(os.path.join(D, "timeline.py"), "w") as f:
    f.write("# «Bepul yetkazish» — build_tl.py yasaydi (ovozsiz ko'rib chiqish versiyasi).\n")
    f.write(f"CUT = {CUT}\nCLIP = {CLIP}\n")
    f.write("SUB = [\n" + "".join(f" {x!r},\n" for x in SUB) + "]\n")
    f.write("TEXT = [\n" + "".join(f" {x!r},\n" for x in TEXT) + "]\nMUSIC_FADE = 5\n")
    if L: f.write(f"AV_LINE = ({AT[18]}, {round(AT[18] + L[18], 3)})\n")
print("T =", T, "| CUT:", CUT)
