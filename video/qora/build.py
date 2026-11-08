#!/usr/bin/env python3
"""«Qora kvadrat» so'zsiz rolikni yig'adi (ko'rib chiqish versiyasi, uz).
python3 video/qora/build.py <work_dir>   → <work>/qora_uz.mp4
Musiqa (egasi 2026-11-08: «o'zingda borini harakat va vaziyatga moslab qo'y»):
 1–9 sahna: «Curious Unease» (egasining Suno treki) — qiziqish → ochko'zlik; 10-sahnada so'nadi, shamol ovozi;
 10b dan oxirigacha: «Nocturnal Tension» (egasining Suno treki) — qorong'i, og'ir; avatar va karta ustida so'nadi.
"""
import os, subprocess, sys, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
R = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
Q = f"{R}/video/qora"; C = f"{Q}/clips"
W = sys.argv[1]; os.makedirs(W, exist_ok=True)
def run(c): subprocess.run(c, check=True)
B = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"; BL = "/usr/share/fonts/opentype/inter/Inter-Black.otf"
if not os.path.exists(BL): BL = B
F = lambda s, f=B: ImageFont.truetype(f, s)
# (klip, boshi, davomiyligi)
SC = [("s01", 0, 5.5), ("s02_v2", 0, 5.0), ("s03_v2", 0, 5.0), ("s04", 3.5, 4.4), ("s05_v2", 0, 4.5), ("s06", 0, 5.0),
      ("s07", 0, 5.0), ("s07b_v2", 0, 5.0), ("s08_cut", 0, 3.9), ("s09", 0, 5.0), ("s10", 0.5, 6.0), ("s10b", 0, 5.0), ("s11", 0, 7.9)]
OYAT, BOT, END = 9.0, 5.0, 4.0  # egasi: oyatga +2 s
V = f"{Q}/voice"; dur = lambda f: float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f],capture_output=True,text=True).stdout)
VL1, VL2, VL3 = dur(f"{V}/l1.wav"), dur(f"{V}/l2.wav"), dur(f"{V}/l3.wav")
AV = round(0.3 + VL3 + 0.8, 2)  # avatar faqat 3-qatorni aytadi (egasi 2026-11-08)
# 1) kliplar
segs = []
for i, (c, s, d) in enumerate(SC):
    o = f"{W}/c{i:02}.mp4"
    run(["ffmpeg", "-v", "error", "-y", "-ss", str(s), "-t", str(d), "-i", f"{C}/{c}.mp4", "-vf",
         "scale=1080:1920:flags=lanczos,fps=30,setsar=1,format=yuv420p", "-an", "-c:v", "libx264", "-crf", "18", "-preset", "fast", o])
    segs.append(o)
# 2) oyat kartasi: qora fon, katta qizil olovli harflar, yengil miltillash
def wrap(d, text, font, maxw):
    lines, cur = [], ""
    for w_ in text.split():
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=font) <= maxw: cur = t
        else: lines.append(cur); cur = w_
    return lines + [cur]
OY = "Ko'paytirish (mol-dunyo, bola-chaqa yoki obro'da bir-biringizdan o'zishga intilish) sizlarni g'aflatda qoldirdi!"
fd = f"{W}/oyat"; os.makedirs(fd, exist_ok=True)
base = Image.new("RGB", (1080, 1920), (6, 4, 6)); dd = ImageDraw.Draw(base)
fo = F(78, BL); lines = wrap(dd, OY, fo, 940); lh = 98
y0 = 960 - len(lines) * lh // 2 - 40
txt = Image.new("L", (1080, 1920), 0); dt = ImageDraw.Draw(txt)
for k, l in enumerate(lines): dt.text(((1080 - dt.textlength(l, font=fo)) / 2, y0 + k * lh), l, font=fo, fill=255)
src = "Takosur surasi, 1–2"; fs = F(44); ys = y0 + len(lines) * lh + 50
glow1 = txt.filter(ImageFilter.GaussianBlur(18)); glow2 = txt.filter(ImageFilter.GaussianBlur(5))
for i in range(int(OYAT * 30)):
    t = i / 30; a = min(1, t / 0.8) * (0.92 + 0.08 * math.sin(t * 9) * math.sin(t * 3.7))
    im = base.copy()
    for g, col, k in ((glow1, (255, 70, 0), 1.0), (glow2, (255, 140, 20), 0.9)):
        im.paste(Image.new("RGB", im.size, col), (0, 0), g.point(lambda v: int(v * k * a)))
    grad = Image.new("RGB", (1080, 1920)); gd = ImageDraw.Draw(grad)
    for yy in range(1920): gd.line([(0, yy), (1080, yy)], fill=(255, max(120, 230 - max(0, yy - y0) // 6), 40))
    im.paste(grad, (0, 0), txt.point(lambda v: int(v * a)))
    d2 = ImageDraw.Draw(im); d2.text(((1080 - d2.textlength(src, font=fs)) / 2, ys), src, font=fs, fill=(int(220 * min(1, max(0, t - 1))), int(200 * min(1, max(0, t - 1))), int(190 * min(1, max(0, t - 1)))))
    im.save(f"{fd}/f{i:04}.jpg", quality=92)
run(["ffmpeg", "-v", "error", "-y", "-framerate", "30", "-i", f"{fd}/f%04d.jpg", "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", f"{W}/oyat.mp4"])
segs.append(f"{W}/oyat.mp4")
# 3) bot kartasi
im = Image.new("RGB", (1080, 1920), (8, 12, 26)); d = ImageDraw.Draw(im)
L1 = ["«Pulingizni bir haftada", "ikki barobar qilamiz»", "degan xabar keldimi?"]
y = 560
for l in L1: d.text(((1080 - d.textlength(l, font=F(64))) / 2, y), l, font=F(64), fill=(255, 255, 255)); y += 84
L2 = ["Skrinshotini yuboring:", "aldovni ko'rsatadi"]
y += 60
for l in L2: d.text(((1080 - d.textlength(l, font=F(54))) / 2, y), l, font=F(54), fill=(170, 220, 255)); y += 72
h = "@sahiychishopbot"; fh = F(76, BL); tw = d.textlength(h, font=fh)
y += 70; d.rounded_rectangle([(1080 - tw) / 2 - 40, y - 20, (1080 + tw) / 2 + 40, y + 130], radius=30, fill=(30, 160, 230))
d.text(((1080 - tw) / 2, y), h, font=fh, fill="white")
im.save(f"{W}/bot.png")
run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-t", str(BOT), "-i", f"{W}/bot.png", "-vf",
     "zoompan=z='1+0.0006*on':d=1:s=1080x1920:fps=30,fade=t=in:d=0.4,format=yuv420p", "-c:v", "libx264", "-crf", "18", f"{W}/bot.mp4"])
segs.append(f"{W}/bot.mp4")
# 4) birlashtirish + cine
open(f"{W}/seq.txt", "w").write("".join(f"file '{s}'\n" for s in segs))
run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{W}/seq.txt", "-c", "copy", f"{W}/story.mp4"])
cuts, t = [], 0
for _, _, d_ in SC: t += d_; cuts.append(round(t, 2))
cuts.append(round(t + OYAT, 2)); STORY = t + OYAT + BOT
run(["bash", f"{R}/video/cine.sh", f"{W}/story.mp4", f"{W}/cine.mp4", " ".join(str(c) for c in cuts)])
# 5) yozuvlar: hook (0.2–2.6 s, tepada), narx (1-sahna)
def txtpng(path, lines, size, col, box=True):
    im = Image.new("RGBA", (1080, 400), (0, 0, 0, 0)); d = ImageDraw.Draw(im); f = F(size, BL); y = 20
    for l in lines:
        w_ = d.textlength(l, font=f)
        if box: d.rounded_rectangle([(1080 - w_) / 2 - 28, y - 10, (1080 + w_) / 2 + 28, y + size + 22], radius=20, fill=(0, 0, 0, 170))
        d.text(((1080 - w_) / 2, y), l, font=f, fill=col); y += size + 40
    im.save(path)
txtpng(f"{W}/hook.png", ["BU RASMNI", "CHOP ETMANG!"], 88, (255, 60, 60))
txtpng(f"{W}/narx.png", ["Kazimir Malevich «Qora kvadrat»", "1 000 000 $ (2002)"], 50, (255, 230, 150))
run(["ffmpeg", "-v", "error", "-y", "-i", f"{W}/cine.mp4", "-i", f"{W}/hook.png", "-i", f"{W}/narx.png", "-filter_complex",
     "[0:v][1:v]overlay=0:150:enable='between(t,0.2,3.6)'[a];[a][2:v]overlay=0:1250:enable='between(t,3.0,5.4)',format=yuv420p[v]",
     "-map", "[v]", "-c:v", "libx264", "-crf", "20", "-preset", "medium", "-r", "30", f"{W}/main_v.mp4"])
# 6) avatar (savol plashkasi; ovoz hali yo'q) + yakuniy karta
sys.path.insert(0, f"{R}/.claude/skills/video-yig"); from yig import avq_plate
avq_plate("Siz-chi?|Qora kvadrat topsangiz, nima qilardingiz?|Izohga yozing!", f"{W}/avq.png")
run(["ffmpeg", "-v", "error", "-y", "-i", f"{R}/video/avatar.mp4", "-i", f"{W}/avq.png", "-filter_complex",
     f"[0:v]split[p][q];[q]reverse[r];[p][r]concat=n=2:v=1,trim=0:{AV},setpts=PTS-STARTPTS,scale=1080:1920:flags=lanczos,fps=30,setsar=1[a];[a][1:v]overlay=0:1200:enable='gte(t,0.3)',format=yuv420p[v]",
     "-map", "[v]", "-c:v", "libx264", "-crf", "20", "-r", "30", f"{W}/av.mp4"])
open(f"{W}/seq2.txt", "w").write("".join(f"file '{s}'\n" for s in [f"{W}/main_v.mp4", f"{W}/av.mp4", f"{R}/video/end/end_uz.mp4"]))
run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{W}/seq2.txt", "-c", "copy", f"{W}/allv.mp4"])
TOT = STORY + AV + END
# 7) ovoz: musiqa 2 qism + shamol + sfx
s10 = sum(d_ for _, _, d_ in SC[:10]); s10b = s10 + SC[10][2]
M1 = f"{R}/video/robot/music/curious_unease.mp3"; M2 = f"{R}/video/korish/music/Nocturnal_Tension.mp3"
run(["ffmpeg", "-v", "error", "-y",
     "-i", M1, "-i", M2,
     "-f", "lavfi", "-t", str(SC[10][2] + 2), "-i", "anoisesrc=c=brown:a=0.6,lowpass=f=900,highpass=f=120,tremolo=f=0.4:d=0.6",
     "-filter_complex",
     f"[0:a]atrim=0:{s10 + 1.5},asetpts=PTS-STARTPTS,afade=t=out:st={s10 - 0.5}:d=2,volume=0.9[m1];"
     f"[1:a]atrim=0:{TOT - s10b + 0.5},asetpts=PTS-STARTPTS,afade=t=in:d=1.5,afade=t=out:st={TOT - s10b - 3}:d=3,adelay={int(s10b * 1000)}|{int(s10b * 1000)},volume=0.8[m2];"
     f"[2:a]afade=t=in:d=0.8,afade=t=out:st={SC[10][2] + 0.5}:d=1.5,adelay={int(s10 * 1000)}|{int(s10 * 1000)},volume=0.9[w];"
     f"[m1][m2][w]amix=inputs=3:normalize=0,apad=whole_dur={TOT},atrim=0:{TOT}[a]",
     "-map", "[a]", "-ar", "48000", "-ac", "2", f"{W}/mus.wav"])
run(["bash", f"{R}/video/sfx.sh", f"{W}/mus.wav", f"{W}/mix0.wav", " ".join(str(c) for c in cuts)])
a2 = sum(d_ for _, _, d_ in SC[:12]) + 0.3; a3 = STORY + 0.3  # 2-qator seyf sahnasi (11) boshida, 3-qator avatarda
run(["ffmpeg", "-v", "error", "-y", "-i", f"{W}/mix0.wav", "-i", f"{V}/l1.wav", "-i", f"{V}/l2.wav", "-i", f"{V}/l3.wav", "-filter_complex",
     f"[1:a]aresample=48000,aformat=channel_layouts=stereo,adelay=300|300[v1];[2:a]aresample=48000,aformat=channel_layouts=stereo,adelay={int(a2*1000)}|{int(a2*1000)}[v2];"
     f"[3:a]aresample=48000,aformat=channel_layouts=stereo,adelay={int(a3*1000)}|{int(a3*1000)}[v3];[v1][v2][v3]amix=inputs=3:normalize=0,volume=1.6,apad=whole_dur={TOT}[vo];"
     "[vo]asplit[vk][vm];[0:a][vk]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[md];[md][vm]amix=inputs=2:normalize=0,loudnorm=I=-15:TP=-1.5:LRA=11[o]",
     "-map", "[o]", "-ar", "48000", f"{W}/mix.wav"])
run(["ffmpeg", "-v", "error", "-y", "-i", f"{W}/allv.mp4", "-i", f"{W}/mix.wav", "-map", "0:v", "-map", "1:a", "-c:v", "copy",
     "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", f"{W}/qora_uz.mp4"])
print("cuts", cuts, "story", round(STORY, 1), "total", round(TOT, 1))
