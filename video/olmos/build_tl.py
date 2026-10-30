# «Olmos uzuk»: voice/NN_*.wav (bip_ajrat.py) + clips → clips/use/ (kesilgan) + dialog.wav + timeline.py.
# Uzun gaplar ikki klipga bo'linadi: 2-gap (s02 → s02b, to'y orzusi), 7-gap (s06 → s06b). 13-klip (bot) kelgach S ga qo'shiladi.
# Ishlatish: python3 video/olmos/build_tl.py  → yig.py --dir video/olmos --voice dialog.wav ...
import os, re, subprocess
D = os.path.dirname(os.path.abspath(__file__)); C = os.path.join(D, "clips"); U = os.path.join(C, "use"); V = os.path.join(D, "voice")
os.makedirs(U, exist_ok=True)
dur = lambda f: float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f], capture_output=True, text=True).stdout)
VF = sorted(f for f in os.listdir(V) if f.endswith(".wav")); L = {int(f[:2]): dur(os.path.join(V, f)) for f in VF}
TXT = {1: "Olmos noyob emas. Senga shunday deb aytishgan.",
 2: "Usta, to'yga olmos uzuk olaman! Sevgilimga olmos uzukni berib, sevgim qanchalik kuchli ekanini isbotlayman! Lekin pulim yetmaydi, kredit olaman!",
 3: "Diyor, kim aytdi sevgi olmosda deb?", 4: "Hamma biladi-ku! Kinoda ham, reklamada ham.",
 5: "Diyor, eshit. 1938-yil, Amerika.",
 6: "Dunyodagi eng katta olmos kompaniyasi reklama agentligini yollaydi. Vazifa: odamlar olmosni sevgi belgisi deb o'ylasin.",
 7: "1947-yil. Bitta shior yoziladi: «Olmos — abadiy». Keyin bu asrning eng mashhur reklama shiori deb tan olindi.",
 8: "Yo'q, mumkin emas! Shiormi?!",
 9: "Televizorda, gazetada, kinoda — har joyda: uzuk olmosli bo'lsin, deyishdi. Keyinroq reklama aytdi: uzukka ikki oylik maoshingni sarfla.",
 10: "Sen sevgi sotib olmayapsan. Kredit sotib olyapsan.", 11: "Demak, sevgilim olmosni emas, meni xohlaydi?", 12: "Inshaalloh.",
 13: "Uchta savol. Bu uzukni kreditsiz ola olasanmi? To'ydan keyin necha oy to'laysan? Sevgiling bilan birga gaplashdingmi?",
 14: "Ular senga tosh emas, «sevgi shu narxda» degan tuyg'uni sotadi. Har gal so'ra: bundan kim foyda ko'radi?",
 15: "To'y xarajatlaringiz ro'yxatini botimizga yozing: @sahiychishopbot. Jamini va kreditning ortiqcha to'lovini hisoblab, qayerda tejash mumkinligini aytadi."}
DIYOR = {2, 4, 8, 11}
# sahna: (klip, kesish (boshi, oxiri) yoki None, qatorlar [(qator, ulush)]; ulush<1 — qatorning shu sahnaga tushadigan qismi)
S = [("s01", None, [(1, 1)]), ("s02", None, [(2, 0.42)]), ("s02b", None, [(2, 0.58)]), ("s03", None, [(3, 1), (4, 1)]),
     ("s04", (0, 6.5), [(5, 1)]), ("s05", None, [(6, 1)]), ("s06", None, [(7, 0.5)]), ("s06b", None, [(7, 0.5)]),
     ("s07", None, [(8, 1)]), ("s08", None, [(9, 1)]), ("s09", (0, 2.8), [(10, 1)]), ("s10", None, [(11, 1)]),
     ("s10b", None, [(12, 1)]), ("s11", (0, 7), [(13, 1)]), ("s12", None, [(14, 1)])]
if os.path.exists(os.path.join(C, "s13.mp4")): S.append(("s13", None, [(15, 1)]))
GAP, MIN = 0.3, {"s10b": 3.0}
CUT = [0.0]; CLIP = []; AT = {}; started = {}
for clip, cut, lines in S:
    if cut:
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(C, clip + ".mp4"), "-vf", f"trim={cut[0]}:{cut[1]},setpts=PTS-STARTPTS",
                        "-an", "-c:v", "libx264", "-crf", "16", os.path.join(U, clip + ".mp4")], check=True)
        CLIP.append("use/" + clip)
    else: CLIP.append(clip)
    t = 0.0
    for q, share in lines:
        if q not in started:
            t += 0.15; AT[q] = round(CUT[-1] + t, 3); started[q] = 1
        t += L[q] * share
        if share == 1 or round(sum(sh for qq, sh in [x for c_, _, ls in S for x in ls] if qq == q), 2) <= 1 and AT[q] + L[q] <= CUT[-1] + t + 0.01: t += GAP
    d = max(t + (0.2 if lines[-1][1] == 1 else 0.0), MIN.get(clip, 0))
    CUT.append(round(CUT[-1] + d, 2))
T = CUT[-1]; AT[16] = round(T + 0.5, 3)
syl = lambda s: max(len(re.findall(r"o'|g'|[aeiouAEIOU]", s)), 1)
SUB = []
for q, txt in TXT.items():
    if q not in AT: continue
    parts = [p.strip() for p in re.split(r"(?<=[.!?:])\s+", txt) if p.strip()]; tot = sum(syl(p) for p in parts); t0 = AT[q]
    for p in parts:
        d = L[q] * syl(p) / tot; SUB.append((round(t0, 2), round(t0 + d, 2), "O" if q in DIYOR else "R", p)); t0 += d
ins, fc = [], ""
for k, f in enumerate(VF):
    q = int(f[:2])
    if q not in AT: continue
    ins += ["-i", os.path.join(V, f)]; fc += f"[{len(ins)//2-1}:a]aresample=48000,adelay={int(AT[q] * 1000)}:all=1[a{len(ins)//2-1}];"
n = len(ins) // 2
fc += "".join(f"[a{k}]" for k in range(n)) + f"amix=inputs={n}:normalize=0,apad=whole_dur={AT[16] + L[16] + 0.5}[o]"
subprocess.run(["ffmpeg", "-v", "error", "-y"] + ins + ["-filter_complex", fc, "-map", "[o]", "-ac", "1", os.path.join(D, "dialog.wav")], check=True)
c = lambda k: CUT[k]     # k-sahna boshi (0 dan, S tartibida)
TEXT = [
    (AT[5] + 1.2, c(5) - 0.1, "1938 · AQSh", 96, "F2B544", (540, 250)),
    (AT[7] + 0.2, c(8) - 0.1, "1947", 110, "F2B544", (540, 230)),
    (AT[7] + 2.5, c(8) - 0.1, "«OLMOS — ABADIY»", 74, "FFFFFF", (540, 360)),
    (AT[9] + 9.0, c(10) - 0.1, "UZUK = 2 OYLIK MAOSH?", 62, "FF4A3A", (540, 250)),
    (AT[13] + 1.0, c(14) - 0.05, "1. KREDITSIZ OLA OLASANMI?", 54, "F2B544", (540, 1050)),
    (AT[13] + 3.4, c(14) - 0.05, "2. NECHA OY TO'LAYSAN?", 58, "5FD3A6", (540, 1150)),
    (AT[13] + 5.6, c(14) - 0.05, "3. BIRGA GAPLASHDINGMI?", 58, "FF5EA8", (540, 1250)),
    (AT[14] + 6.5, c(15) - 0.05, "BUNDAN KIM FOYDA KO'RADI?", 64, "F2B544", (540, 250)),
]
if 15 in AT: TEXT += [(AT[15] + 2.5, T, "@sahiychishopbot", 96, "F2B544", (540, 250)), (AT[15] + 4.0, T, "TO'Y XARAJATINI HISOBLAYDI", 52, "FFFFFF", (540, 360))]
TEXT = [(round(a, 2), round(b, 2), x, s, col, p) for a, b, x, s, col, p in TEXT]
with open(os.path.join(D, "timeline.py"), "w") as f:
    f.write("# «Olmos uzuk» — build_tl.py yasaydi (qo'lda o'zgartirmang).\n")
    f.write(f"CUT = {CUT}\nCLIP = {CLIP}\n")
    f.write("SUB = [\n" + "".join(f" {x!r},\n" for x in SUB) + "]\n")
    f.write("TEXT = [\n" + "".join(f" {x!r},\n" for x in TEXT) + "]\n")
    f.write(f"AV_LINE = ({AT[16]}, {round(AT[16] + L[16], 3)})\nMUSIC_FADE = 5\n")
print("T =", T, "| CUT:", CUT)
