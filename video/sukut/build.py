#!/usr/bin/env python3
"""«G'azabda sukut» rolikni yig'adi. python3 video/sukut/build.py <work> [uz|ru|en] → <work>/<lang>/sukut_<lang>.mp4 (+ .srt)
Tepada hikoyachi gapi (katta), pastda oyat ma'nosi + «Qur'oni Karimdan» (raqamsiz, egasi 2026-11-08).
1-sahna: «To'xtang!» da kadr qotadi, kulrang (1.1 s). Hikoyadan keyin 7 ta oyat alohida kartalarda, sura nomi va raqami bilan (ovozsiz, musiqa ostida), keyin bot kartasi.
Musiqa: «Dutar's Whisper» (egasining treki) 3:17 dan, ovoz ostida (sidechain)."""
import os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont
R = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
Q = f"{R}/video/sukut"; C = f"{Q}/clips"; V = f"{Q}/voice"
W0 = sys.argv[1]; LANG = sys.argv[2] if len(sys.argv) > 2 else "uz"
W = f"{W0}/{LANG}"; os.makedirs(W, exist_ok=True); CW = f"{W0}/clips"; os.makedirs(CW, exist_ok=True)
def run(c): subprocess.run(c, check=True)
dur = lambda f: float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f], capture_output=True, text=True).stdout)
B = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"; BL = "/usr/share/fonts/opentype/inter/Inter-Black.otf"; IT = "/usr/share/fonts/opentype/inter/Inter-SemiBoldItalic.otf"
if not os.path.exists(IT): IT = B
F = lambda s, f=B: ImageFont.truetype(f, s)
T = {
 "uz": dict(say=["To'xtang! Shu izohga javob yozishdan oldin buni ko'ring.", "G'azab kelganda jim turish — kuchsizlik emas, kuch.", "Hasadga tabassum bilan javob bering.",
   "Qo'zg'atuvchiga javob bermaslik — aql.", "Befoyda bahsdan o'z vaqtida chiqing.", "Bosim ostida xotirjam bo'ling.", "Kechira olgan odam — g'olib.", "Bugun bitta odamni kechiring.",
   "Jahlingizni chiqargan xabarni @sahiychishopbot'ga yuboring: xotirjam va hurmatli javob yozishga yordam beradi.", "Siz-chi? Oxirgi marta qachon jim turib, yutdingiz? Izohga yozing!"],
  ayah=["«...g'azabini ichiga yutuvchi va odamlarni afv etuvchilar. Alloh yaxshilik qiluvchilarni sevadi.»",
   "«Yomonlikni eng go'zal yo'l bilan qaytaring: shunda sen bilan adovatli kimsa go'yo qadrdon do'stdek bo'lib qoladi.»",
   "«Johillar ularga xitob qilsa, \"Salom\" deydilar.»", "«Behuda so'zni eshitsalar, undan yuz o'giradilar.»",
   "«Sabr va namoz bilan yordam so'rang. Albatta, Alloh sabr qiluvchilar bilandir.»", "«Afv yo'lini tuting, yaxshilikka buyuring va johillardan yuz o'giring.»",
   "«Afv etsinlar va kechirsinlar. Alloh sizni mag'firat qilishini istamaysizmi?»"],
  src="Qur'oni Karimdan", hook="TO'XTANG!",
  refs=["Oli Imron surasi, 134-oyat", "Fussilat surasi, 34-oyat", "Furqon surasi, 63-oyat", "Qasas surasi, 55-oyat", "Baqara surasi, 153-oyat", "A'rof surasi, 199-oyat", "Nur surasi, 22-oyat"],
  b1=["Jahlingizni chiqargan", "xabar keldimi?"], b2=["Botga yuboring:", "xotirjam va hurmatli", "javob yozishga yordam beradi"],
  avq="Siz-chi?|Oxirgi marta qachon jim turib, yutdingiz?|Izohga yozing!"),
}[LANG]
# (klip, boshi, davomiyligi)
SC = [("s01", 0, 7.6), ("s02", 0, 5.5), ("s03", 0, 4.6), ("s04", 0, 5.0), ("s05", 0, 7.0), ("s06", 0, 5.0), ("s07", 0, 6.0), ("s08", 0, 7.9)]
AYD, BOT, END = 3.4, 7.0, 4.0  # egasi 2026-11-09: oyatlar sahnalarda emas, 0:49 dan alohida-alohida, sura va raqami bilan
QUR = AYD * 7
VL = [dur(f"{V}/{i:02}_usta.wav") for i in range(1, 11)]
AV = round(0.3 + VL[9] + 0.8, 2)
FREEZE = (1.9, 1.1)   # 1-sahna: klipning 1.9 s da kadr qotadi, 1.1 s
segs = []
for i, (c, s, d) in enumerate(SC):
    o = f"{CW}/c{i}.mp4"
    if os.path.exists(o): segs.append(o); continue
    if i == 0:
        f0, fd = FREEZE
        run(["ffmpeg", "-v", "error", "-y", "-i", f"{C}/{c}.mp4", "-filter_complex",
             f"[0:v]scale=1080:1920:flags=lanczos,fps=30,setsar=1,split=3[a][b][c];[a]trim=0:{f0},setpts=PTS-STARTPTS[p1];"
             f"[b]trim={f0}:{f0 + 0.04},setpts=PTS-STARTPTS,tpad=stop_mode=clone:stop_duration={fd},trim=0:{fd},hue=s=0.15,eq=brightness=-0.04[fr];"
             f"[c]trim={f0}:{d - fd},setpts=PTS-STARTPTS[p2];[p1][fr][p2]concat=n=3:v=1,format=yuv420p[v]",
             "-map", "[v]", "-an", "-c:v", "libx264", "-crf", "18", "-preset", "fast", o])
    else:
        run(["ffmpeg", "-v", "error", "-y", "-ss", str(s), "-t", str(d), "-i", f"{C}/{c}.mp4", "-vf",
             "scale=1080:1920:flags=lanczos,fps=30,setsar=1,format=yuv420p", "-an", "-c:v", "libx264", "-crf", "18", "-preset", "fast", o])
    segs.append(o)
def wrap(d, text, font, maxw):
    ls, cur = [], ""
    for w_ in text.split():
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=font) <= maxw: cur = t
        else: ls.append(cur); cur = w_
    return ls + [cur]
def card(path, lines_spec, bg=(10, 12, 20)):
    im = Image.new("RGB", (1080, 1920), bg); d = ImageDraw.Draw(im)
    tot = sum(sz + gap for _, sz, _, _, gap in lines_spec); y = 960 - tot // 2
    for txt, sz, font, col, gap in lines_spec:
        d.text(((1080 - d.textlength(txt, font=F(sz, font))) / 2, y), txt, font=F(sz, font), fill=col); y += sz + gap
    im.save(path)
dd0 = ImageDraw.Draw(Image.new("RGB", (1, 1)))
ay = []
for k in range(7):
    lines = [(l, 58, IT, (255, 240, 210), 18) for l in wrap(dd0, T["ayah"][k], F(58, IT), 920)]
    card(f"{W}/ayah_c{k}.png", lines + [("", 10, B, (0, 0, 0), 30), (T["refs"][k], 44, BL, (242, 200, 110), 10)], bg=(12, 10, 8))
    run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-t", str(AYD), "-i", f"{W}/ayah_c{k}.png", "-vf", f"fade=t=in:d=0.35,fade=t=out:st={AYD - 0.35}:d=0.35,format=yuv420p,fps=30", "-c:v", "libx264", "-crf", "18", f"{W}/ayah_c{k}.mp4"])
    ay.append(f"{W}/ayah_c{k}.mp4")
im = Image.new("RGB", (1080, 1920), (8, 12, 26)); d = ImageDraw.Draw(im); y = 520
for l in T["b1"]: d.text(((1080 - d.textlength(l, font=F(66))) / 2, y), l, font=F(66), fill="white"); y += 86
y += 50
for l in T["b2"]: d.text(((1080 - d.textlength(l, font=F(52))) / 2, y), l, font=F(52), fill=(170, 220, 255)); y += 70
h = "@sahiychishopbot"; fh = F(76, BL); tw = d.textlength(h, font=fh); y += 70
d.rounded_rectangle([(1080 - tw) / 2 - 40, y - 20, (1080 + tw) / 2 + 40, y + 130], radius=30, fill=(30, 160, 230)); d.text(((1080 - tw) / 2, y), h, font=fh, fill="white")
im.save(f"{W}/bot.png")
run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-t", str(BOT), "-i", f"{W}/bot.png", "-vf", "zoompan=z='1+0.0005*on':d=1:s=1080x1920:fps=30,fade=t=in:d=0.4,format=yuv420p", "-c:v", "libx264", "-crf", "18", f"{W}/bot.mp4"])
segs += ay + [f"{W}/bot.mp4"]
open(f"{W}/seq.txt", "w").write("".join(f"file '{x}'\n" for x in segs))
run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{W}/seq.txt", "-c", "copy", f"{W}/story.mp4"])
starts, t = [], 0
for _, _, d_ in SC: starts.append(round(t, 2)); t += d_
starts.append(round(t, 2))
for k in range(1, 7): starts.append(round(t + AYD * k, 2))
starts.append(round(t + QUR, 2)); STORY = t + QUR + BOT
cine = f"{W0}/cine_story.mp4"
if not os.path.exists(cine): run(["bash", f"{R}/video/cine.sh", f"{W}/story.mp4", cine, " ".join(str(c) for c in starts[1:])])
# yozuvlar
def txtpng(path, text, size, col, maxw=940, box=(0, 0, 0, 150), font=B, small=None):
    im = Image.new("RGBA", (1080, 520), (0, 0, 0, 0)); d = ImageDraw.Draw(im); f = F(size, font); ls = wrap(d, text, f, maxw)
    h = len(ls) * (size + 14) + (size // 2 + 20 if small else 0) + 30
    d.rounded_rectangle([40, 0, 1040, h], radius=26, fill=box); y = 18
    for l in ls: d.text(((1080 - d.textlength(l, font=f)) / 2, y), l, font=f, fill=col, stroke_width=2, stroke_fill="black"); y += size + 14
    if small: fs = F(size * 2 // 3); d.text(((1080 - d.textlength(small, font=fs)) / 2, y + 6), small, font=fs, fill=(242, 200, 110))
    im.save(path)
VS = []  # (ovoz qatori, boshlanish)
VS.append((0, 0.3)); fr0 = 0.3 + 0.92  # «To'xtang!» tugashi
for k in range(1, 8): VS.append((k, starts[k] + 0.4))
VS.append((8, STORY - BOT + 0.4)); a10 = STORY + 0.3; VS.append((9, a10))
ov, fl = [], []
txtpng(f"{W}/hook.png", T["hook"], 110, (255, 70, 70), font=BL, box=(0, 0, 0, 0)); ov.append(("hook.png", 120, 0.2, FREEZE[0] + FREEZE[1]))
for k in range(8):
    a = VS[k][1]; b = a + VL[k] + (0.4 if k else 0)
    txtpng(f"{W}/say{k}.png", T["say"][k] if k else T["say"][0].split("!", 1)[1].strip(), 54, "white")
    if k == 0: a = FREEZE[0] + FREEZE[1]
    ov.append((f"say{k}.png", 260, a, min(b, starts[k + 1] - 0.1)))
args = ["ffmpeg", "-v", "error", "-y", "-i", cine]; parts = []; prev = "0:v"
for n, (png, y, a, b) in enumerate(ov, 1):
    args += ["-i", f"{W}/{png}"]; parts.append(f"[{prev}][{n}:v]overlay=0:{y}:enable='between(t,{a:.2f},{b:.2f})'[o{n}]"); prev = f"o{n}"
fc = ";".join(parts) + f";[{prev}]format=yuv420p"
run(args + ["-filter_complex", fc + "[v]", "-map", "[v]", "-c:v", "libx264", "-crf", "20", "-preset", "medium", "-r", "30", f"{W}/main_v.mp4"])
sys.path.insert(0, f"{R}/.claude/skills/video-yig"); from yig import avq_plate
avq_plate(T["avq"], f"{W}/avq.png")
run(["ffmpeg", "-v", "error", "-y", "-i", f"{R}/video/avatar.mp4", "-i", f"{W}/avq.png", "-filter_complex",
     f"[0:v]split[p][q];[q]reverse[r];[p][r]concat=n=2:v=1,trim=0:{AV},setpts=PTS-STARTPTS,scale=1080:1920:flags=lanczos,fps=30,setsar=1[a];[a][1:v]overlay=0:1200:enable='gte(t,0.3)',format=yuv420p[v]",
     "-map", "[v]", "-c:v", "libx264", "-crf", "20", "-r", "30", f"{W}/av.mp4"])
open(f"{W}/seq2.txt", "w").write("".join(f"file '{x}'\n" for x in [f"{W}/main_v.mp4", f"{W}/av.mp4", f"{R}/video/end/end_{LANG}.mp4"]))
run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{W}/seq2.txt", "-c", "copy", f"{W}/allv.mp4"])
TOT = STORY + AV + END
# ovoz: musiqa + tiqillash (qotish payti) + sfx + hikoyachi (ducking)
M = f"{R}/video/robot/music/dutars_whisper.mp3"
run(["ffmpeg", "-v", "error", "-y", "-ss", "197", "-t", str(TOT + 1), "-i", M,
     "-f", "lavfi", "-t", str(FREEZE[1]), "-i", "aevalsrc='0.6*sin(2*PI*1800*t)*exp(-60*mod(t,0.5))':s=48000",
     "-filter_complex", f"[0:a]afade=t=in:d=1.5,afade=t=out:st={TOT - 3}:d=3,volume=0.7,aresample=48000,aformat=channel_layouts=stereo[m];"
     f"[1:a]adelay={int(FREEZE[0]*1000)}|{int(FREEZE[0]*1000)},aformat=channel_layouts=stereo[k];[m][k]amix=inputs=2:normalize=0,atrim=0:{TOT}[a]",
     "-map", "[a]", "-ar", "48000", "-ac", "2", f"{W}/mus.wav"])
run(["bash", f"{R}/video/sfx.sh", f"{W}/mus.wav", f"{W}/mix0.wav", " ".join(str(c) for c in starts[1:])])
ins = ["-i", f"{W}/mix0.wav"]; fc = ""; labs = ""
for j, (k, a) in enumerate(VS):
    ins += ["-i", f"{V}/{k + 1:02}_usta.wav"]; fc += f"[{j + 1}:a]aresample=48000,aformat=channel_layouts=stereo,adelay={int(a * 1000)}|{int(a * 1000)}[v{j}];"; labs += f"[v{j}]"
fc += f"{labs}amix=inputs={len(VS)}:normalize=0,volume=1.6,apad=whole_dur={TOT}[vo];[vo]asplit[vk][vm];[0:a][vk]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[md];[md][vm]amix=inputs=2:normalize=0,loudnorm=I=-15:TP=-1.5:LRA=11[o]"
run(["ffmpeg", "-v", "error", "-y"] + ins + ["-filter_complex", fc, "-map", "[o]", "-ar", "48000", f"{W}/mix.wav"])
run(["ffmpeg", "-v", "error", "-y", "-i", f"{W}/allv.mp4", "-i", f"{W}/mix.wav", "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", f"{W}/sukut_{LANG}.mp4"])
def ts(x): return f"{int(x//3600):02}:{int(x%3600//60):02}:{int(x%60):02},{int(round(x%1*1000)):03}"
open(f"{W}/sukut-{LANG}.srt", "w").write("".join(f"{i+1}\n{ts(a)} --> {ts(a + VL[k])}\n{T['say'][k]}\n\n" for i, (k, a) in enumerate(VS)))
print("starts", starts, "story", round(STORY, 1), "total", round(TOT, 1))
