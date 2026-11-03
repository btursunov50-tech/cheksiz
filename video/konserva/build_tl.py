# «Konserva»: kliplarni clips/use/ ga kesadi, ovozdan sahna uzunligini hisoblaydi, dialog.wav va timeline.py yasaydi.
# Uzun gaplar ikki klipga bo'linadi: 4-gap (s04 + s04b), 9-gap (s08?? yo'q: s09 + s09b_use). Ishlatish: python3 video/konserva/build_tl.py
import os, re, subprocess
D = os.path.dirname(os.path.abspath(__file__)); C = os.path.join(D, "clips"); U = os.path.join(C, "use"); V = os.path.join(D, "voice"); os.makedirs(U, exist_ok=True)
dur = lambda f: float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f], capture_output=True, text=True).stdout)
VF = sorted(f for f in os.listdir(V) if f.endswith(".wav")); L = {int(f[:2]): dur(os.path.join(V, f)) for f in VF}
TXT = {1: "Bankadagi bir sana «xavfsiz» deydi, boshqasi «mazali». Ular bir xil emas.",
 2: "Tasavvur qiling: do'konga kirdingiz, bir banka konserva oldingiz. Sanani ko'rdingiz va xotirjam bo'ldingiz.",
 3: "Lekin bu sana aslida nimani bildiradi?",
 4: "Birinchidan, yozuvlarning farqini bilib oling. Tayyorlangan sana — mahsulot qachon ishlab chiqarilganini ko'rsatadi. Yaroqlilik muddati — shu sanagacha mahsulot xavfsiz. «Eng yaxshi sifatgacha» — bu sifat sanasi.",
 5: "Muddati o'tgan mahsulotni yemang.",
 6: "Ikkinchidan, quruq mahsulotga ham ishonavermang. Guruch, makaron va un to'g'ri saqlansa uzoq turadi, lekin namlik va hasharotlar ularni muddatidan oldin buzishi mumkin.",
 7: "Uchinchidan, bankaga qarang. Shishgan, oqayotgan, qattiq zanglagan yoki choklari shikastlangan bo'lsa, yemang.",
 8: "Eng xavflisi botulizm: og'ir zaharlanishga olib keladigan kasallik. Xavfli konserva ba'zan tashqaridan bilinmaydi. Shuning uchun shubhali konservani tatib ko'rib tekshirmang.",
 9: "To'rtinchidan, sut mahsulotlari. Hidi yoki ko'rinishi o'zgargan bo'lsa, ichmang. Hid normal bo'lsa ham, bu to'liq xavfsizlikni kafolatlamaydi.",
 10: "Do'konda esa uchta ish qiling. Sanani tekshiring. Qadoq butunligiga ishonch hosil qiling. Saqlash shartlariga amal qiling.",
 11: "Arzon ekan deb shubhali mahsulotni sotib olmang. Pulni tejash mumkin, lekin sog'liqni xavf ostiga qo'yishga arzimaydi.",
 12: "Mahsulot yorlig'ining suratini botimizga yuboring: @sahiychishopbot. Yozuvlar nimani bildirishini tushuntirib, tekshirishni bosqichma-bosqich o'rgatadi.",
 13: "Videoni yaqinlaringizga ham yuboring: balki kimnidir jiddiy xatodan asrab qolar."}
# sahna: (klip, kesish (boshi, eng kech oxiri) yoki None, qator, ulush boshi, ulush oxiri)
S = [("s01", None, 1, 0, 1), ("s02", None, 2, 0, 1), ("s03", (2.6, 4.7), 3, 0, 1), ("s04", None, 4, 0, .5), ("s04b", None, 4, .5, 1),
     ("s05", (1.2, 5.4), 5, 0, 1), ("s06", None, 6, 0, 1), ("s07", None, 7, 0, 1), ("s08", None, 8, 0, 1), ("s09", None, 9, 0, .55),
     ("s09b_use", None, 9, .55, 1), ("s10", None, 10, 0, 1), ("s11", None, 11, 0, 1), ("s12", (0.6, 7.9), 12, 0, 1), ("s13", (1.2, 7.7), 13, 0, 1)]
GAP = 0.3
CUT = [0.0]; CLIP = []; AT = {}
for clip, cut, q, s0, s1 in S:
    d = (0.15 if s0 == 0 else 0) + L[q] * (s1 - s0) + (0.35 if s1 == 1 else 0)
    if s0 == 0: AT[q] = round(CUT[-1] + 0.15, 3)
    src = os.path.join(C, clip + ".mp4"); full = dur(src); a, mx = cut if cut else (0, full)
    b = min(mx, a + d); out = os.path.join(U, clip + ".mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-vf", f"trim={a}:{b},setpts=PTS-STARTPTS,scale=720:1280,setsar=1,fps=24", "-an", "-c:v", "libx264", "-crf", "16", out], check=True)
    CUT.append(round(CUT[-1] + d, 2)); CLIP.append("use/" + clip)
T = CUT[-1]; c = lambda k: CUT[k - 1]   # k-sahna boshi (1 dan, S tartibida)
AT[14] = round(T + 0.5, 3)
sc = {n: i + 1 for i, (n, *_r) in enumerate(S)}
TEXT = [
    (0.2, 3.2, "IKKI SANA, IKKI MA'NO", 64, "FFC23A", (540, 250)),
    (c(sc["s04"]) + 1.0, c(sc["s04b"]) - 0.1, "ISHLAB CHIQARILGAN SANA", 56, "FFC23A", (540, 250)),
    (c(sc["s04b"]) + 0.3, c(sc["s04b"]) + 4.0, "YAROQLILIK MUDDATI = XAVFSIZ", 52, "5FD3A6", (540, 250)),
    (c(sc["s04b"]) + 4.1, c(sc["s05"]) - 0.1, "«ENG YAXSHI» = SIFAT", 58, "FFC23A", (540, 250)),
    (c(sc["s05"]) + 0.2, c(sc["s06"]) - 0.1, "MUDDATI O'TGANINI YEMANG", 56, "FF4A3A", (540, 250)),
    (c(sc["s07"]) + 1.0, c(sc["s08"]) - 0.1, "SHISHGAN · OQAYOTGAN · ZANGLAGAN", 46, "FF4A3A", (540, 250)),
    (c(sc["s08"]) + 0.6, c(sc["s09"]) - 0.1, "BOTULIZM: TATIB KO'RMANG", 56, "FF4A3A", (540, 250)),
    (c(sc["s10"]) + 1.0, c(sc["s10"]) + 3.2, "1. SANANI TEKSHIRING", 56, "FFC23A", (540, 250)),
    (c(sc["s10"]) + 3.3, c(sc["s10"]) + 5.6, "2. QADOQ BUTUNMI?", 56, "5FD3A6", (540, 250)),
    (c(sc["s10"]) + 5.7, c(sc["s11"]) - 0.1, "3. SAQLASH SHARTLARI", 56, "FFC23A", (540, 250)),
    (c(sc["s12"]) + 3.0, c(sc["s13"]) - 0.1, "@sahiychishopbot", 96, "FFC23A", (540, 250)),
    (c(sc["s12"]) + 4.5, c(sc["s13"]) - 0.1, "YORLIQ SURATINI YUBORING", 50, "FFFFFF", (540, 360)),
]
# s12 (bot) 12-gap sahnasi: c(sc["s12"]) — TEXT dagi indekslar nomi bo'yicha. s11 = 11-gap, s12 = 12-gap
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
fc += "".join(f"[a{k}]" for k in range(len(VF))) + f"amix=inputs={len(VF)}:normalize=0,apad=whole_dur={AT[14] + L[14] + 0.5}[o]"
subprocess.run(["ffmpeg", "-v", "error", "-y"] + ins + ["-filter_complex", fc, "-map", "[o]", "-ac", "1", os.path.join(D, "dialog.wav")], check=True)
with open(os.path.join(D, "timeline.py"), "w") as f:
    f.write("# «Konserva» — build_tl.py yasaydi.\n")
    f.write(f"CUT = {CUT}\nCLIP = {CLIP}\n")
    f.write("SUB = [\n" + "".join(f" {x!r},\n" for x in SUB) + "]\n")
    f.write("TEXT = [\n" + "".join(f" {x!r},\n" for x in TEXT) + "]\nMUSIC_FADE = 5\n")
    f.write(f"AV_LINE = ({AT[14]}, {round(AT[14] + L[14], 3)})\n")
print("T =", T, "| CUT:", CUT)
