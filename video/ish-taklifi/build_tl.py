# «Oyiga 490 million»: kliplarni clips/use/ ga kesadi, ovozdan sahna uzunligini hisoblaydi, dialog.wav va timeline.py yasaydi.
import os, re, subprocess
D = os.path.dirname(os.path.abspath(__file__)); C = os.path.join(D, "clips"); U = os.path.join(C, "use"); V = os.path.join(D, "voice"); os.makedirs(U, exist_ok=True)
dur = lambda f: float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f], capture_output=True, text=True).stdout)
VF = sorted(f for f in os.listdir(V) if f.endswith(".wav")); L = {int(f[:2]): dur(os.path.join(V, f)) for f in VF}
TXT = {1: "Oyiga to'rt yuz to'qson million so'm. Tajriba shart emas. Ariza topshirasizmi?",
 2: "Post shunday deydi: Claude odamlarni masofaviy ishga taklif qilmoqda, ariza 22-noyabrgacha, vazifa — sun'iy intellektni aylanib o'tish.",
 3: "Men, Claude, o'zim tekshirdim. Bunday vakansiya topilmadi.",
 4: "Lekin asosi haqiqiy: Anthropic'da xavfsizlik dasturi bor. Tadqiqotchilar Claude'ning himoyasidagi zaif joyni topib, kompaniyaga yashirin xabar beradi va mukofot oladi.",
 5: "Bu oylik maosh emas. Bu topilgan har bir zaiflik uchun mukofot, eng ko'pi taxminan o'ttiz besh ming dollar.",
 6: "Va «tajribasiz» ham emas: yangi zaiflikni topish uchun chuqur bilim kerak. Postning o'zi ham muhandislar va olimlarni afzal ko'radi.",
 7: "Qizil bayroqlar: manba yo'q, havola yo'q, «shoshiling» degan muddat, va «kimga yuborishni bilasiz» degan klik tuzog'i.",
 8: "Firibgarlar aynan shunday e'lon bilan pasport, karta va tasdiq kodini so'raydi, yoki oldindan pul oladi.",
 9: "Uchta qoida. Vakansiyani faqat kompaniyaning rasmiy saytidan tekshiring. Ish beruvchi oldindan pul, karta yoki kod so'ramaydi. Shoshiltirsa, to'xtang.",
 10: "Har gal so'rang: bundan kim foyda ko'radi?",
 11: "Shubhali post yoki vakansiya matnini botimizga yuboring: @sahiychishopbot. Qizil bayroqlarni topib, qanday tekshirishni bosqichma-bosqich o'rgatadi."}
# sahna: (klip, kesish (boshi, eng kech oxiri) yoki None, qator, ulush boshi, ulush oxiri)
S = [("s01", (0, 3.9), 1, 0, .5), ("s02", (2.6, 6.5), 1, .5, 1), ("s03", (0, 4.6), 2, 0, .5), ("s04", (0, 5.0), 2, .5, 1),
     ("s05", (0, 7.9), 3, 0, 1), ("s06", None, 4, 0, 1), ("s07", None, 5, 0, 1), ("s08", (0, 6.5), 6, 0, 1), ("s09", None, 7, 0, 1),
     ("s10", None, 8, 0, 1), ("s11", None, 9, 0, 1), ("s12", (0, 4.5), 10, 0, 1), ("s13", (0, 6.9), 11, 0, 1)]
CUT = [0.0]; CLIP = []; AT = {}
for clip, cut, q, s0, s1 in S:
    d = (0.15 if s0 == 0 else 0) + L[q] * (s1 - s0) + (0.35 if s1 == 1 else 0)
    if s0 == 0: AT[q] = round(CUT[-1] + 0.15, 3)
    src = os.path.join(C, clip + ".mp4"); full = dur(src); a, mx = cut if cut else (0, full)
    b = min(mx, a + d); out = os.path.join(U, clip + ".mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-vf", f"trim={a}:{b},setpts=PTS-STARTPTS,scale=720:1280,setsar=1,fps=24", "-an", "-c:v", "libx264", "-crf", "16", out], check=True)
    CUT.append(round(CUT[-1] + d, 2)); CLIP.append("use/" + clip)
T = CUT[-1]; AT[12] = round(T + 0.5, 3)
sc = {n: i + 1 for i, (n, *_r) in enumerate(S)}; c = lambda n: CUT[sc[n] - 1]
TEXT = [
    (0.2, 3.4, "OYIGA 490 MILLION?", 70, "FFC23A", (540, 250)),
    (c("s05") + 0.5, c("s06") - 0.1, "VAKANSIYA TOPILMADI", 58, "FF4A3A", (540, 250)),
    (c("s06") + 1.0, c("s07") - 0.1, "BUG BOUNTY = ZAIFLIK UCHUN MUKOFOT", 44, "FFC23A", (540, 250)),
    (c("s07") + 3.0, c("s08") - 0.1, "OYLIK EMAS", 80, "FF4A3A", (540, 250)),
    (c("s08") + 0.5, c("s09") - 0.1, "TAJRIBASIZ EMAS", 62, "FFC23A", (540, 250)),
    (c("s09") + 0.8, c("s10") - 0.1, "QIZIL BAYROQLAR", 70, "FF4A3A", (540, 250)),
    (c("s11") + 2.6, c("s11") + 5.8, "1. RASMIY SAYT", 60, "FFC23A", (540, 250)),
    (c("s11") + 6.0, c("s11") + 9.4, "2. PUL, KARTA, KOD SO'RAMAYDI", 46, "5FD3A6", (540, 250)),
    (c("s11") + 9.6, c("s12") - 0.1, "3. SHOSHILTIRSA, TO'XTANG", 52, "FF4A3A", (540, 250)),
    (c("s12") + 0.3, c("s13") - 0.1, "BUNDAN KIM FOYDA KO'RADI?", 56, "FFC23A", (540, 250)),
    (c("s13") + 4.0, c("s13") + 7.5, "@sahiychishopbot", 96, "FFC23A", (540, 250)),
]
TEXT = [(round(a, 2), round(b, 2), x, s, col, p) for a, b, x, s, col, p in TEXT]
SUB = []
syl = lambda s: max(len(re.findall(r"o'|g'|[aeiouAEIOU]", s)), 1)
for q, txt in TXT.items():
    parts = [p.strip() for p in re.split(r"(?<=[.!?:])\s+", txt) if p.strip()]; tot = sum(syl(p) for p in parts); t0 = AT[q]
    for p in parts:
        d = L[q] * syl(p) / tot; SUB.append((round(t0, 2), round(t0 + d, 2), "R", p)); t0 += d
ins, fc = [], ""
for k, f in enumerate(VF):
    q = int(f[:2]); ins += ["-i", os.path.join(V, f)]; fc += f"[{k}:a]aresample=48000,adelay={int(AT[q] * 1000)}:all=1[a{k}];"
fc += "".join(f"[a{k}]" for k in range(len(VF))) + f"amix=inputs={len(VF)}:normalize=0,apad=whole_dur={AT[12] + L[12] + 0.5}[o]"
subprocess.run(["ffmpeg", "-v", "error", "-y"] + ins + ["-filter_complex", fc, "-map", "[o]", "-ac", "1", os.path.join(D, "dialog.wav")], check=True)
with open(os.path.join(D, "timeline.py"), "w") as f:
    f.write("# «Oyiga 490 million» — build_tl.py yasaydi.\n")
    f.write(f"CUT = {CUT}\nCLIP = {CLIP}\n")
    f.write("SUB = [\n" + "".join(f" {x!r},\n" for x in SUB) + "]\n")
    f.write("TEXT = [\n" + "".join(f" {x!r},\n" for x in TEXT) + "]\nMUSIC_FADE = 5\n")
    f.write(f"AV_LINE = ({AT[12]}, {round(AT[12] + L[12], 3)})\n")
print("T =", T, "| CUT:", CUT)
for i, s in enumerate(SUB): print(i, s[3][:60])
