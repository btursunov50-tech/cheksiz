#!/usr/bin/env python3
"""«Bitta tugma» (Excel/Word) rolikni yig'adi: python3 video/tugma/build.py <work> [uz|ru|en] → <work>/<lang>/tugma_<lang>.mp4 (+ .srt)
Sahnalar: Veo kliplari (clips/*_toza.mp4, s02.mp4) + kodda chizilgan Excel/Word ekranlari (chiz/chiz.py). Ovoz o'zbekcha (voice/01–10), yozuvlar tilga qarab.
Musiqa: Doira and the Robot (Suno, egasi) 8 s dan; MUS / MUS_SS bilan almashtiriladi."""
import os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont
R = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
Q = f"{R}/video/tugma"; C = f"{Q}/clips"; V = f"{Q}/voice"
W0 = sys.argv[1]; LANG = sys.argv[2] if len(sys.argv) > 2 else "uz"
W = f"{W0}/{LANG}"; os.makedirs(W, exist_ok=True); CW = f"{W0}/seg"; os.makedirs(CW, exist_ok=True)
def run(c): subprocess.run(c, check=True)
dur = lambda f: float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f], capture_output=True, text=True).stdout)
B = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"; BL = "/usr/share/fonts/opentype/inter/Inter-Black.otf"
F = lambda s, f=B: ImageFont.truetype(f, s)
T_ALL = {"uz": dict(hook="BITTA TUGMA!", say=[
  "Kalkulyatorda sanashni to'xtating! Bitta tugma buni bir soniyada qiladi.",
  "Ko'pchilik shunday deydi: Excel faqat dasturchilar uchun. Yo'q, u siz uchun.",
  "Raqamlar ostidagi katakka turing va Alt bilan tenglik belgisini bosing: hammasi o'zi qo'shiladi.",
  "Ctrl bilan T harfini bosing: oddiy ro'yxat bir zumda chiroyli jadvalga aylanadi.",
  "Ism va familiyani ajratish kerakmi? Bittasini o'zingiz yozing, Ctrl bilan E harfini bosing: qolganini Excel o'zi to'ldiradi.",
  "Ishga kirish uchun qayerda ishlaganingiz va nima qila olishingiz haqida varaqa kerakmi? Word'da noldan yozmang: Fayl, Yaratish, tayyor namunani tanlang va o'z ma'lumotingizni yozing.",
  "Saqlayotganda PDF'ni tanlang: hujjat har qanday telefonda bir xil ochiladi.",
  "Ish ikki soat emas, ikki daqiqa bo'ldi.",
  "Excel yoki Word'da qayerda qotib qoldingiz? Ekran rasmini @sahiychishopbot'ga yuboring: qaysi tugmani bosishni qadamma-qadam ko'rsatadi.",
  "Siz-chi? Excel'da qaysi ish sizga eng qiyin? Izohga yozing!"],
  avq="Siz-chi?|Excel'da qaysi ish sizga eng qiyin?|Izohga yozing!")}
T = T_ALL[LANG]
VL = [dur(f"{V}/{i:02}_usta.wav") for i in range(1, 11)]
CH = f"{W0}/chiz"
if not all(os.path.exists(f"{CH}/{n}.mp4") for n in ("s03", "s04", "s05", "s06w", "s07", "s09")):
    run(["python3", f"{Q}/chiz/chiz.py", CH])
# (manba, boshi, davomiyligi, sekinlashtirish) — Veo 24 fps 720x1280, chizilgan 30 fps 1080x1920
P = 0.3
SEG = [("v", "s01_toza", 0, round(P + VL[0] + 0.4, 2)), ("v", "s02", 0, round(P + VL[1] + 0.4, 2)),
       ("c", "s03", 0, None), ("c", "s04", 0, None), ("v", "s_qoshimcha_toza", 0, 2.4), ("c", "s05", 0, None),
       ("v", "s06_toza", 0, 6.0), ("c", "s06w", 0, None), ("c", "s07", 0, None), ("v", "s08_toza", 0, 5.9), ("c", "s09", 0, None)]
segs, lens = [], []
for k, (kind, name, ss, d) in enumerate(SEG):
    src = f"{C}/{name}.mp4" if kind == "v" else f"{CH}/{name}.mp4"; L = dur(src) - ss; d = d or L
    o = f"{CW}/{k:02}_{name}_{d}.mp4"
    if not os.path.exists(o):
        f = max(1.0, d / L)
        vf = (f"setpts={f:.4f}*(PTS-STARTPTS)," + ("minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:me_mode=bidir," if f > 1.02 else "fps=30,") +
              f"trim=0:{d},setpts=PTS-STARTPTS,scale=1080:1920:flags=lanczos,setsar=1,format=yuv420p")
        run(["ffmpeg", "-v", "error", "-y", "-ss", str(ss), "-i", src, "-vf", vf, "-an", "-r", "30", "-c:v", "libx264", "-crf", "18", "-preset", "fast", o])
    segs.append(o); lens.append(d)
starts, t = [], 0
for d in lens: starts.append(round(t, 2)); t += d
STORY = t
# ovoz qatorlari: (qator, boshlanishi)
VS = [(0, starts[0] + P), (1, starts[1] + P), (2, starts[2] + 0.5), (3, starts[3] + 0.3), (4, starts[4] + 0.3),
      (5, starts[6] + 0.3), (6, starts[8] + 0.3), (7, starts[9] + 0.6), (8, starts[10] + 0.3)]
open(f"{W}/seq.txt", "w").write("".join(f"file '{x}'\n" for x in segs))
run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{W}/seq.txt", "-c", "copy", f"{W}/story.mp4"])
cine = f"{W0}/cine_story.mp4"
if not os.path.exists(cine): run(["bash", f"{R}/video/cine.sh", f"{W}/story.mp4", cine, " ".join(str(c) for c in starts[1:])])
def wrap(d, text, font, maxw):
    ls, cur = [], ""
    for w_ in text.split():
        t_ = (cur + " " + w_).strip()
        if d.textlength(t_, font=font) <= maxw: cur = t_
        else: ls.append(cur); cur = w_
    return ls + [cur]
def txtpng(path, text, size, col, font=B, box=(0, 0, 0, 160)):
    im = Image.new("RGBA", (1080, 400), (0, 0, 0, 0)); d = ImageDraw.Draw(im); f = F(size, font); ls = wrap(d, text, f, 940)
    h = len(ls) * (size + 14) + 30
    if box[3]: d.rounded_rectangle([40, 0, 1040, h], radius=26, fill=box)
    y = 16
    for l in ls: d.text(((1080 - d.textlength(l, font=f)) / 2, y), l, font=f, fill=col, stroke_width=2, stroke_fill="black"); y += size + 14
    im.save(path)
def chunks(text, n=8):  # uzun gapni bo'laklarga (vaqt so'z soniga qarab)
    ws = text.split(); out = []
    while ws:
        k = min(len(ws), n)
        for j in range(k, max(3, k - 4), -1):
            if ws[j - 1][-1] in ".,:?!": k = j; break
        out.append(" ".join(ws[:k])); ws = ws[k:]
    return out
ov, srt = [], []
txtpng(f"{W}/hook.png", T["hook"], 104, (255, 60, 70), font=BL, box=(0, 0, 0, 0)); ov.append(("hook.png", 130, 0.2, 3.0))
n = 0
for k, a in VS:
    parts = chunks(T["say"][k]); tot = sum(len(p.split()) for p in parts); t0 = a
    for p in parts:
        d_ = VL[k] * len(p.split()) / tot; n += 1
        txtpng(f"{W}/sub{n}.png", p, 52, "white")
        if k != 8: ov.append((f"sub{n}.png", 1450, t0, t0 + d_ - 0.03))  # 9-qator: bot kartasida yozuv o'zi bor
        srt.append((t0, t0 + d_, p)); t0 += d_
args = ["ffmpeg", "-v", "error", "-y", "-i", cine]; fc = []; prev = "0:v"
for i, (png, y, a, b) in enumerate(ov, 1):
    args += ["-i", f"{W}/{png}"]; fc.append(f"[{prev}][{i}:v]overlay=0:{y}:enable='between(t,{a:.2f},{b:.2f})'[o{i}]"); prev = f"o{i}"
run(args + ["-filter_complex", ";".join(fc) + f";[{prev}]format=yuv420p[v]", "-map", "[v]", "-c:v", "libx264", "-crf", "20", "-r", "30", f"{W}/main_v.mp4"])
sys.path.insert(0, f"{R}/.claude/skills/video-yig"); from yig import avq_plate
avq_plate(T["avq"], f"{W}/avq.png"); AV = round(0.3 + VL[9] + 0.8, 2)
run(["ffmpeg", "-v", "error", "-y", "-i", f"{R}/video/avatar.mp4", "-i", f"{W}/avq.png", "-filter_complex",
     f"[0:v]split[p][q];[q]reverse[r];[p][r]concat=n=2:v=1,trim=0:{AV},setpts=PTS-STARTPTS,scale=1080:1920:flags=lanczos,fps=30,setsar=1[a];[a][1:v]overlay=0:1200:enable='gte(t,0.3)',format=yuv420p[v]",
     "-map", "[v]", "-c:v", "libx264", "-crf", "20", "-r", "30", f"{W}/av.mp4"])
open(f"{W}/seq2.txt", "w").write("".join(f"file '{x}'\n" for x in [f"{W}/main_v.mp4", f"{W}/av.mp4", f"{R}/video/end/end_{LANG}.mp4"]))
run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{W}/seq2.txt", "-c", "copy", f"{W}/allv.mp4"])
END = 4.0; TOT = STORY + AV + END; VS.append((9, STORY + 0.3))
M = os.environ.get("MUS", f"{R}/video/robot/music/doira_and_the_robot.mp3")  # egasi tanladi (A), 2026-11-10
run(["ffmpeg", "-v", "error", "-y", "-ss", os.environ.get("MUS_SS", "8"), "-t", str(TOT + 1), "-i", M, "-filter_complex",
     f"[0:a]afade=t=in:d=1.5,afade=t=out:st={TOT - 3}:d=3,volume=0.7,aresample=48000,aformat=channel_layouts=stereo,atrim=0:{TOT}[a]", "-map", "[a]", "-ar", "48000", f"{W}/mus.wav"])
run(["bash", f"{R}/video/sfx.sh", f"{W}/mus.wav", f"{W}/mix0.wav", " ".join(str(c) for c in starts[1:])])
ins = ["-i", f"{W}/mix0.wav"]; fcs = ""; labs = ""
for j, (k, a) in enumerate(VS):
    ins += ["-i", f"{V}/{k + 1:02}_usta.wav"]; fcs += f"[{j + 1}:a]aresample=48000,aformat=channel_layouts=stereo,adelay={int(a * 1000)}|{int(a * 1000)}[v{j}];"; labs += f"[v{j}]"
fcs += f"{labs}amix=inputs={len(VS)}:normalize=0,volume=1.6,apad=whole_dur={TOT}[vo];[vo]asplit[vk][vm];[0:a][vk]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[md];[md][vm]amix=inputs=2:normalize=0,loudnorm=I=-15:TP=-1.5:LRA=11[o]"
run(["ffmpeg", "-v", "error", "-y"] + ins + ["-filter_complex", fcs, "-map", "[o]", "-ar", "48000", f"{W}/mix.wav"])
run(["ffmpeg", "-v", "error", "-y", "-i", f"{W}/allv.mp4", "-i", f"{W}/mix.wav", "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", f"{W}/tugma_{LANG}{os.environ.get('TAG', '')}.mp4"])
def ts(x): return f"{int(x//3600):02}:{int(x%3600//60):02}:{int(x%60):02},{int(round(x%1*1000)):03}"
srt.append((STORY + 0.3, STORY + 0.3 + VL[9], T["say"][9]))
open(f"{W}/tugma-{LANG}.srt", "w").write("".join(f"{i+1}\n{ts(a)} --> {ts(b)}\n{t_}\n\n" for i, (a, b, t_) in enumerate(srt)))
print("starts", starts, "story", round(STORY, 1), "total", round(TOT, 1))
for k, a in VS: print(k + 1, round(a, 2), "->", round(a + VL[k], 2))
