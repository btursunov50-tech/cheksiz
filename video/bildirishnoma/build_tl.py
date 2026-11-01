# «Telefon jiringlaydi»: kliplarni clips/use/ ga kesadi, ovozdan sahna uzunligini hisoblaydi, dialog.wav va timeline.py yasaydi.
# Ishlatish: python3 video/bildirishnoma/build_tl.py → yig.py --dir video/bildirishnoma --voice dialog.wav ...
import os, re, subprocess
D = os.path.dirname(os.path.abspath(__file__)); C = os.path.join(D, "clips"); U = os.path.join(C, "use"); os.makedirs(U, exist_ok=True)
V = os.path.join(D, "voice")
VF = sorted(f for f in os.listdir(V) if f.endswith(".wav"))
dur = lambda f: float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f], capture_output=True, text=True).stdout)
L = {int(f[:2]): dur(os.path.join(V, f)) for f in VF}
# sahna → (klip boshi, klip oxiri chegarasi); sahna i = ovoz qatori i
S = {1: (0, 7.9), 2: (0, 7.9), 3: (0, 7.9), 4: (0, 7.9), 5: (0, 7.9), 6: (0, 7.9), 7: (0, 7.9), 8: (0, 7.9), 9: (0, 7.9), 10: (0, 7.9), 11: (3.6, 7.6), 12: (0, 7.9), 13: (0, 6.5)}
TXT = {1: "Telefoning jiringlaganda sen telefonni emas, telefon seni boshqaradi.", 2: "Usta, bir daqiqa, xabar keldi!", 3: "Diyor, eshit. 2006-yil, Amerika.",
 4: "Bir muhandis cheksiz aylantirishni o'ylab topdi: sahifa tugamaydi, pastga tushaverasan.", 5: "Sahifa tugasa, to'xtaysan. Tugamasa, to'xtamaysan.",
 6: "Keyinchalik u shu ixtirosidan afsuslanishini ochiq aytdi.", 7: "Ilovalar bizni ataylab ushlab turadimi?!",
 8: "Bir tadqiqotga ko'ra, o'rtacha foydalanuvchi kuniga qirq oltitaga yaqin bildirishnoma oladi.",
 9: "Ilovalar sening e'tiboring bilan pul topadi: qancha uzoq qarasang, shuncha ko'p reklama ko'rsatiladi.",
 10: "Uchta qoida. Keraksiz bildirishnomani o'chir. Kechasi tinch rejimni yoq. Ilovani ochishdan oldin so'ra: nega ochyapman?",
 11: "Telefon jim, men tinch!", 12: "Ular senga ilovani emas, «o'tkazib yuboraman» degan qo'rquvni sotadi. Har gal so'ra: bundan kim foyda ko'radi?",
 13: "Qaysi bildirishnomani o'chirishni bilmasangiz, ilova nomini botimizga yozing: @sahiychishopbot. Bosqichma-bosqich o'rgatadi."}
DIYOR = {2, 7, 11}
syl = lambda t: len(re.findall(r"o'|g'|[aeiouAEIOU]", t))
CUT = [0.0]; CLIP = []; AT = {}
for i in range(1, 14):
    a, mx = S[i]; d = 0.15 + L[i] + 0.35; AT[i] = round(CUT[-1] + 0.15, 3)
    b = min(mx, a + d) if a + d < mx else mx
    n = f"s{i:02}"; out = os.path.join(U, n + ".mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(C, n + ".mp4"), "-vf",
                    f"trim={a}:{b},setpts=PTS-STARTPTS,scale=720:1280,setsar=1,fps=24", "-an", "-c:v", "libx264", "-crf", "16", out], check=True)
    CUT.append(round(CUT[-1] + d, 2)); CLIP.append("use/" + n)
T = CUT[-1]; c = lambda k: CUT[k - 1]
AT[14] = round(T + 0.5, 3)
TEXT = [
    (c(3) + 3.0, c(4) - 0.1, "2006 · AQSh", 96, "FFC23A", (540, 250)),
    (c(4) + 1.0, c(5) - 0.1, "CHEKSIZ AYLANTIRISH", 64, "FFC23A", (540, 250)),
    (c(8) + 1.5, c(9) - 0.1, "KUNIGA ~46 TA BILDIRISHNOMA", 54, "FFC23A", (540, 250)),
    (c(9) + 2.0, c(10) - 0.1, "E'TIBOR = PUL", 80, "FF4A3A", (540, 250)),
    (c(10) + 1.4, c(10) + 3.6, "1. KERAKSIZINI O'CHIR", 60, "FFC23A", (540, 250)),
    (c(10) + 3.7, c(10) + 5.9, "2. KECHASI TINCH REJIM", 60, "5FD3A6", (540, 250)),
    (c(10) + 6.0, c(11) - 0.1, "3. NEGA OCHYAPMAN?", 60, "FF4A3A", (540, 250)),
    (c(12) + 5.5, c(13) - 0.1, "BUNDAN KIM FOYDA KO'RADI?", 60, "FFC23A", (540, 250)),
    (c(13) + 3.5, T, "@sahiychishopbot", 96, "FFC23A", (540, 250)),
]
TEXT = [(round(a, 2), round(b, 2), x, s, col, p) for a, b, x, s, col, p in TEXT]
SUB = []
for q, txt in TXT.items():
    parts = [p.strip() for p in re.split(r"(?<=[.!?:])\s+", txt) if p.strip()]
    tot = sum(max(syl(p), 1) for p in parts); t0 = AT[q]
    for p in parts:
        d = L[q] * max(syl(p), 1) / tot
        SUB.append((round(t0, 2), round(t0 + d, 2), "O" if q in DIYOR else "R", p)); t0 += d
ins, fc = [], ""
for k, f in enumerate(VF):
    q = int(f[:2]); ins += ["-i", os.path.join(V, f)]; fc += f"[{k}:a]aresample=48000,adelay={int(AT[q] * 1000)}:all=1[a{k}];"
fc += "".join(f"[a{k}]" for k in range(len(VF))) + f"amix=inputs={len(VF)}:normalize=0,apad=whole_dur={AT[14] + L[14] + 0.5}[o]"
subprocess.run(["ffmpeg", "-v", "error", "-y"] + ins + ["-filter_complex", fc, "-map", "[o]", "-ac", "1", os.path.join(D, "dialog.wav")], check=True)
with open(os.path.join(D, "timeline.py"), "w") as f:
    f.write("# «Telefon jiringlaydi» — build_tl.py yasaydi.\n")
    f.write(f"CUT = {CUT}\nCLIP = {CLIP}\n")
    f.write("SUB = [\n" + "".join(f" {x!r},\n" for x in SUB) + "]\n")
    f.write("TEXT = [\n" + "".join(f" {x!r},\n" for x in TEXT) + "]\nMUSIC_FADE = 5\n")
    f.write(f"AV_LINE = ({AT[14]}, {round(AT[14] + L[14], 3)})\n")
print("T =", T, "| CUT:", CUT)
