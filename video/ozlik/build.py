#!/usr/bin/env python3
"""«O'zligim» klipini qo'shiq satrlariga qarab yig'adi (16:9). python3 video/ozlik/build.py <work> → <work>/ozlik.mp4
Satr vaqtlari qo'shiqdagi pauzalardan taxminiy topilgan (LINES); egasi tekshirgach tuzatiladi."""
import os, sys, subprocess
from PIL import Image, ImageDraw, ImageFont
R = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")); Q = f"{R}/video/ozlik"; C = f"{Q}/clips"
W0 = sys.argv[1]; os.makedirs(W0, exist_ok=True)
SS = 11.0  # qo'shiqning qayeridan boshlanadi (0–11.7 s jim)
def run(c): subprocess.run(c, check=True)
# (qo'shiq vaqti boshi, oxiri, manba, manbadan boshi, manbadan oxiri)
TL = [(11.0, 18.4, "TITLE", 0, 0), (18.4, 23.0, "s01", 0, 2.9), (23.0, 34.4, "s02", 0, 7.93), (34.4, 39.2, "s03", 0, 4.8), (39.2, 44.0, "s04", 1.5, 6.3),
      (44.0, 50.0, "s05", 0, 6.0), (50.0, 56.0, "s05_v2", 0, 3.8), (56.0, 65.0, "s06", 0, 7.93), (65.0, 76.0, "s07", 0, 7.93), (76.0, 87.0, "s08", 0, 7.93)]
END = TL[-1][1]
LINES = [(23.0, "Men o'zimni izladim, o'zimdan yiroqlarda,"), (29.0, "Seni ko'rdim, ey Haqiqat, ko'z yoshimning bog'larida."),
         (34.5, "Men quyoshni osmondan, oyni tundan so'radim,"), (39.3, "Sen esa qalbimda ekansan, nega bunchalar yo'l yurdim?"),
         (44.0, "Men dengiz deb o'yladim, bir tomchiga zor ekanman,"), (50.0, "Men olamni angladim deb, o'zimdan bexabar ekanman."),
         (56.0, "Mingta kitob o'qib chiqdim, bir satrni anglamadim,"), (61.2, "«O'zingni angla», degan so'zga umrimcha yeta olmadim."),
         (65.5, "Ey ishq, meni yondir, kulimdan gullar unsin,"), (71.0, "Qalbimdagi g'uborlar bir nafasda to'kilsin."),
         (76.5, "Men Senga yetmoq istadim, yo'llarimda adashdim,"), (81.5, "O'zligimdan kechgan kunim, haqiqatga tutashdim.")]
FI = "/usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf"
# sarlavha kartasi: qog'oz + «O'zligim» siyohda
paper = Image.open(f"{Q}/img/s01.png").convert("RGB").resize((1920, 1080)).filter(__import__("PIL.ImageFilter", fromlist=["x"]).GaussianBlur(18))
ov = Image.new("RGB", paper.size, (236, 206, 150)); paper = Image.blend(paper, ov, .55); d = ImageDraw.Draw(paper)
f = ImageFont.truetype(FI, 150); t = "O'zligim"; d.text(((1920 - d.textlength(t, font=f)) / 2, 400), t, font=f, fill=(62, 38, 18))
f2 = ImageFont.truetype(FI, 46); t2 = "she'r va qo'shiq"; d.text(((1920 - d.textlength(t2, font=f2)) / 2, 600), t2, font=f2, fill=(120, 86, 50))
paper.save(f"{W0}/title.png")
X = 0.5
segs = []
for k, (a, b, src, s0, s1) in enumerate(TL):
    d_ = round(b - a + (X if k < len(TL) - 1 else 0), 3); o = f"{W0}/seg{k:02}.mp4"  # o'tish uchun X s ortiqcha
    if src == "TITLE":
        run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-t", str(d_), "-i", f"{W0}/title.png", "-vf",
             f"zoompan=z='1+0.0006*on':d=1:s=1920x1080:fps=24,fade=t=in:d=1.2,format=yuv420p", "-c:v", "libx264", "-crf", "18", "-r", "24", o])
    else:
        L = s1 - s0; fct = d_ / L
        vf = (f"trim={s0}:{s1},setpts={fct:.4f}*(PTS-STARTPTS)," + ("minterpolate=fps=24:mi_mode=mci:mc_mode=aobmc:me_mode=bidir," if fct > 1.03 else "fps=24,") +
              f"trim=0:{d_},setpts=PTS-STARTPTS,scale=1920:1080:flags=lanczos,setsar=1,format=yuv420p")
        run(["ffmpeg", "-v", "error", "-y", "-i", f"{C}/{src}.mp4", "-vf", vf, "-an", "-r", "24", "-c:v", "libx264", "-crf", "18", "-preset", "fast", o])
    segs.append((o, d_))
# yumshoq o'tishlar: i-o'tish satr vaqti TL[i][0] da boshlanadi, sinxron buzilmaydi
args = ["ffmpeg", "-v", "error", "-y"]; fc = []; prev = "0:v"
for o, _ in segs: args += ["-i", o]
for i in range(1, len(segs)):
    off_i = TL[i][0] - SS
    fc.append(f"[{prev}][{i}:v]xfade=transition=fade:duration={X}:offset={off_i:.3f}[x{i}]"); prev = f"x{i}"
run(args + ["-filter_complex", ";".join(fc), "-map", f"[{prev}]", "-c:v", "libx264", "-crf", "18", "-preset", "fast", f"{W0}/v.mp4"])
vt = lambda tsong: tsong - SS
VD = END - SS
# subtitrlar (ASS)
def a(x): return f"0:{int(x // 60):02}:{x % 60:05.2f}"
ass = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: L,Liberation Serif,58,&H00F0FAFF,&H00FFFFFF,&H00123048,&H64000000,-1,-1,0,0,100,100,0,0,1,4,2,2,80,80,70,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
for i, (t0, txt) in enumerate(LINES):
    t1 = LINES[i + 1][0] if i + 1 < len(LINES) else END - 1.0
    ass += f"Dialogue: 0,{a(vt(t0))},{a(vt(t1) - 0.25)},L,,0,0,0,,{{\\fad(300,300)}}{txt}\n"
open(f"{W0}/lyrics.ass", "w").write(ass)
run(["ffmpeg", "-v", "error", "-y", "-i", f"{W0}/v.mp4", "-ss", str(SS), "-i", f"{Q}/qoshiq.mp3", "-filter_complex",
     f"[0:v]subtitles={W0}/lyrics.ass,fade=t=out:st={VD - 1.5:.2f}:d=1.5[v];[1:a]atrim=0:{VD:.2f},afade=t=in:d=0.5,afade=t=out:st={VD - 2.5:.2f}:d=2.5[au]",
     "-map", "[v]", "-map", "[au]", "-t", f"{VD:.2f}", "-c:v", "libx264", "-crf", "20", "-preset", "medium", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", f"{W0}/ozlik.mp4"])
print("video", round(VD, 1), "s")
