#!/usr/bin/env python3
"""«O'zligim» — GPT kliplaridan (gpt/g01…g26) qo'shiq bo'yicha 16:9 klip. python3 video/ozlik/build2.py <work> → <work>/ozlik2.mp4
Qo'shiq: qoshiq_final.mp3 (asl qo'shiq 0:10 dan, 1.05x, bass/stereo, 3:27). Satr vaqtlari mid/side vokal energiyasidan taxminiy (LINES);
egasi tekshirgach tuzatiladi. Kodda qo'shiladigan effektlar (qizil neon, gullar, uchqunlar, oxiri) — effects()."""
import os, sys, subprocess, math, random
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
R = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")); Q = f"{R}/video/ozlik"; G = f"{Q}/gpt"
W0 = sys.argv[1]; os.makedirs(W0, exist_ok=True)
W, H, FPS = 1920, 1080, 24
def run(c): subprocess.run(c, check=True)
SONG = f"{Q}/qoshiq_final.mp3"; END = 207.0
# (boshi qo'shiqda, manba, manbadan boshi, oxiri) — oxiri = keyingi qatorning boshi
TL = [(0.0, "g03", 0, 7.93), (8.5, "g02", 0, 7.93),
      (16.5, "g04", 0, 4.0), (21.5, "g04", 4.0, 7.93), (26.5, "g01", 0, 7.93), (31.5, "g08", 0, 7.93),
      (37.0, "g06", 2.5, 7.93), (41.5, "g05", 2.0, 7.93), (46.0, "g12", 0, 4.5), (50.5, "g14", 0, 3.8), (54.5, "g13", 0, 3.6),
      (58.0, "g10", 0, 4.0), (63.5, "g09", 0, 7.93), (69.0, "g10", 4.0, 7.93), (74.0, "g13", 3.6, 7.93), (80.0, "g11", 2.3, 7.93),
      (84.5, "g07", 0, 2.5), (88.0, "g14", 5.4, 7.93), (91.0, "g06", 0, 2.5), (94.5, "g12", 4.5, 7.93),
      (100.0, "g18", 0, 7.93), (113.0, "g24_kozgu", 0, 3.6), (119.5, "g17", 0, 7.93), (131.0, "g24_kozgu", 3.6, 8.0),
      (137.5, "g16", 0, 3.5), (141.0, "g26_sham2", 0, 7.93), (149.0, "g16", 3.5, 7.93), (152.5, "g20", 3.5, 7.93),
      (156.0, "g15", 0.6, 7.93), (162.5, "g19", 0, 6.0), (168.5, "g21", 0, 6.0), (174.5, "g23_oyga", 8.3, 16.0),
      (182.0, "g01", 3.0, 7.93), (188.0, "g22_tomoshabinga", 1.2, 8.0), (195.0, "END", 0, 0)]
LY = ["Men o'zimni izladim, o'zimdan yiroqlarda,", "Seni ko'rdim, ey Haqiqat, ko'z yoshimning bog'larida.",
      "Men quyoshni osmondan, oyni tundan so'radim,", "Sen esa qalbimda ekansan, nega bunchalar yo'l yurdim?",
      "Men dengiz deb o'yladim, bir tomchiga zor ekanman,", "Men olamni angladim deb, o'zimdan bexabar ekanman.",
      "Mingta kitob o'qib chiqdim, bir satrni anglamadim,", "«O'zingni angla», degan so'zga umrimcha yeta olmadim.",
      "Ey ishq, meni yondir, kulimdan gullar unsin,", "Qalbimdagi g'uborlar bir nafasda to'kilsin.",
      "Men Senga yetmoq istadim, yo'llarimda adashdim,", "O'zligimdan kechgan kunim, haqiqatga tutashdim.",
      "Ey qalb, sening ichingda ming bir olam yashirin,", "Sen o'zingni anglagan kun ochilar sirli eshiging.",
      "Men muhabbat deb o'yladim, nafsim ekan istagim,", "Birovdan vafo kutardim, o'zim esa bevafo.",
      "Aybni dunyodan izlab, o'zimni pok sanadim,", "Ko'zgularga boqmay turib, o'zimni haq deb atadim.",
      "Toshga urdim boshimni, devorlarga zorlandim,", "Haqni izlab osmonga, o'z qalbimdan ayrildim.",
      "Kimki o'zin yenga olmas, ming g'alaba — sarobdir,", "Nafsini yenggan inson — eng buyuk g'olibdir.",
      "Bir sham yonib so'nar ekan, nur qolur xotirada,", "Inson ketar, so'zi qolar, yaxshilikning izida.",
      "Mol-dunyoni yig'ding nega, bir kun qolur qo'llardan,", "Mehring qolsin, yaxshi noming, o'tib ketgan yo'llardan.",
      "Kechir, inson, g'azabingni muhabbatga aylantir,", "Qalbdagi qorong'ulikni bir zarra nurga almashtir."]
# (boshi, satr raqami) — taxminiy; 162.5–186 naqarot takrori deb olindi
LINES = [(16.5, 0), (21.5, 1), (26.5, 2), (31.5, 3), (37.0, 4), (41.5, 5), (46.0, 6), (50.5, 7),
         (58.0, 8), (63.5, 9), (69.0, 10), (74.0, 11), (80.0, 12), (84.5, 13),
         (100.0, 14), (105.0, 15), (110.0, 16), (115.0, 17), (120.0, 18), (125.0, 19), (131.0, 20), (136.0, 21),
         (141.0, 22), (146.0, 23), (151.0, 24), (156.0, 25), (162.5, 8), (168.0, 9), (174.0, 10), (180.0, 11),
         (188.0, 26), (194.0, 27)]
LEND = {13: 89.0, 25: 162.0, 29: 186.0, 31: 202.0}  # bo'limlar oxiri (indeks LINES ichida)
FB = "/usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf"
X = 0.4
# ---------- 1) kliplar → bo'laklar ----------
segs = []
for k, (a, src, s0, s1) in enumerate(TL):
    b = TL[k + 1][0] if k + 1 < len(TL) else END
    d = round(b - a + (X if k < len(TL) - 1 else 0), 3); o = f"{W0}/s{k:02}.mp4"
    if src == "END":
        run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"color=c=black:s={W}x{H}:r={FPS}:d={d}", "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", o])
    elif not os.path.exists(o):
        L = s1 - s0; f = d / L
        vf = (f"trim={s0}:{s1},setpts={f:.4f}*(PTS-STARTPTS)," + ("minterpolate=fps=24:mi_mode=mci:mc_mode=aobmc:me_mode=bidir," if f > 1.03 else "fps=24,") +
              f"trim=0:{d},setpts=PTS-STARTPTS,scale={W}:{H}:flags=lanczos,setsar=1,format=yuv420p")
        run(["ffmpeg", "-v", "error", "-y", "-i", f"{G}/{src}.mp4", "-vf", vf, "-an", "-r", str(FPS), "-c:v", "libx264", "-crf", "17", "-preset", "fast", o])
        print(k, src, f"{f:.2f}x", flush=True)
    segs.append(o)
args = ["ffmpeg", "-v", "error", "-y"]; fc = []; prev = "0:v"
for o in segs: args += ["-i", o]
for i in range(1, len(segs)):
    tr = "fadewhite" if TL[i][1] == "END" else "fade"
    fc.append(f"[{prev}][{i}:v]xfade=transition={tr}:duration={X}:offset={TL[i][0]:.3f}[x{i}]"); prev = f"x{i}"
run(args + ["-filter_complex", ";".join(fc), "-map", f"[{prev}]", "-c:v", "libx264", "-crf", "17", "-preset", "fast", f"{W0}/base.mp4"])
# ---------- 2) effektlar (qizil neon, gullar, uchqunlar, oxiri) ----------
RED = (255, 40, 60); ROSE = (255, 90, 120); GOLD = (255, 200, 110)
def neon(draw_fn, size=(W, H), col=RED, glow=14, core=.65):
    m = Image.new("L", size, 0); draw_fn(ImageDraw.Draw(m)); m = np.asarray(m, np.float32) / 255
    g1 = np.asarray(Image.fromarray((m * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(glow)), np.float32) / 255
    g2 = np.asarray(Image.fromarray((m * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(glow / 3)), np.float32) / 255
    c = np.array(col, np.float32) / 255
    out = g1[..., None] * c * 1.6 + g2[..., None] * c * 1.2 + m[..., None] * (c * (1 - core) + core)
    return np.clip(out, 0, 1)
def textlayer(txt, fs, y, col=RED, glow=16, width=6):
    f = ImageFont.truetype(FB, fs)
    def fn(d):
        tw = d.textlength(txt, font=f); d.text(((W - tw) / 2, y), txt, font=f, fill=255, stroke_width=0)
    return neon(fn, col=col, glow=glow), f
def flower(cx, base_y, hgt, petal, rot=0):
    def fn(d):
        top = base_y - hgt
        pts = [(cx + 18 * math.sin(t / 8), base_y - t * hgt / 40) for t in range(41)]
        d.line(pts, fill=255, width=4)
        d.line([(cx, base_y - hgt * .45), (cx - 40, base_y - hgt * .6)], fill=255, width=3)
        d.line([(cx + 4, base_y - hgt * .3), (cx + 46, base_y - hgt * .42)], fill=255, width=3)
        tx, ty = pts[-1]
        for j in range(6):
            a = rot + j * math.pi / 3; px, py = tx + petal * .8 * math.cos(a), ty + petal * .8 * math.sin(a)
            d.ellipse([px - petal * .55, py - petal * .55, px + petal * .55, py + petal * .55], outline=255, width=4)
        d.ellipse([tx - petal * .3, ty - petal * .3, tx + petal * .3, ty + petal * .3], fill=255)
    return fn
def heart(cx, cy, s):
    def fn(d):
        pts = [(cx + s * 16 * math.sin(t) ** 3, cy - s * (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t))) for t in np.linspace(0, 2 * math.pi, 120)]
        d.line(pts + [pts[0]], fill=255, width=6)
    return fn
print("effects…", flush=True)
TITLE, _ = textlayer("O'zligim", 170, 360, col=RED, glow=20)
SUB, _ = textlayer("she'r va qo'shiq", 52, 590, col=GOLD, glow=8)
ANGLA, _ = textlayer("«O'zingni angla»", 120, 150, col=RED, glow=18)
FIN, _ = textlayer("O'zingni angla", 160, 400, col=RED, glow=24)
FIN2, _ = textlayer("Kechir, inson, g'azabingni muhabbatga aylantir", 46, 620, col=GOLD, glow=6)
def shadow(layer, r=28, k=.55): m = layer.max(2); return np.asarray(Image.fromarray((np.clip(m * 2, 0, 1) * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(r)), np.float32) / 255 * k
SH_T, SH_A, SH_S = shadow(TITLE), shadow(ANGLA), shadow(SUB, 14, .5)
rng = random.Random(7)
FLW = [(x, 1030, rng.randint(160, 300), rng.randint(22, 36), rng.random()) for x in (180, 420, 1500, 1740, 300, 1620)]
FLC = [neon(flower(x, by, h, p, r), col=ROSE if i % 2 else RED, glow=12) for i, (x, by, h, p, r) in enumerate(FLW)]
HEART = neon(heart(960, 420, 9), col=RED, glow=22)
EMB = [(rng.uniform(300, 1620), rng.uniform(0, 1), rng.uniform(.6, 1.6), rng.uniform(2, 5)) for _ in range(70)]
PET = [(rng.uniform(0, W), rng.uniform(0, 1), rng.uniform(.5, 1.2), rng.uniform(10, 20), rng.uniform(0, 6.28)) for _ in range(40)]
def sm(x): x = min(max(x, 0), 1); return x * x * (3 - 2 * x)
def wipe(layer, p):  # chapdan o'ngga yozilish
    if p >= 1: return layer
    o = layer.copy(); o[:, int(W * p):] = 0; return o
def flick(t, t0):  # neon yonishi: 0.6 s miltillab yonadi
    u = t - t0
    if u < 0: return 0
    if u > .6: return 1
    return [0, .8, .1, 1, .3, 1, .9, 1][int(u / .6 * 8) % 8]
def particles(t, t0, dur, col, n_items, kind):
    m = Image.new("L", (W, H), 0); d = ImageDraw.Draw(m); u = (t - t0) / dur
    for (x, ph, sp, r, *rest) in n_items:
        if kind == "ember":
            y = H - ((ph + u * sp) % 1) * H * .9; xx = x + 30 * math.sin(t * 2 + ph * 9)
            d.ellipse([xx - r, y - r, xx + r, y + r], fill=255)
        else:  # gul bargi tushadi
            y = ((ph + u * sp * .5) % 1) * (H + 80) - 40; xx = (x + 60 * math.sin(t + ph * 7)) % W; a = rest[0] + t
            d.ellipse([xx - r, y - r * .5, xx + r, y + r * .5], fill=200)
    return neon(lambda dd: dd.bitmap((0, 0), m, fill=255), col=col, glow=5, core=.15)
def effects(t):
    L = []
    if 1.0 <= t < 8.3:  # sarlavha
        a = flick(t, 1.0) * (1 - sm((t - 7.3) / 1.0)); L += [("d", (SH_T + SH_S) * sm((t - 1.0) / .5) * (1 - sm((t - 7.3) / 1.0))), TITLE * a, SUB * sm((t - 2.2) / 1.0) * (1 - sm((t - 7.3) / 1.0))]
    if 22.0 <= t < 26.9:  # «ko'z yoshimning bog'larida» — qizil neon gullar unadi
        for i, F in enumerate(FLC):
            g = sm((t - 22.0 - i * .35) / 1.6); fo = 1 - sm((t - 26.0) / .9)
            if g > 0:
                o = F.copy(); cut = int(H - (H - 650) * g - 50); o[:max(0, cut)] = 0; L.append(o * fo)
    if 51.2 <= t < 54.9:  # «O'zingni angla» qizil neon yozuv
        a = 1 - sm((t - 54.2) / .7); L += [("d", wipe(SH_A[..., None], sm((t - 51.2) / 1.4))[..., 0] * a), wipe(ANGLA, sm((t - 51.2) / 1.4)) * a]
    if 58.0 <= t < 63.9:  # «Ey ishq, meni yondir» — yurak + uchqunlar, keyin gullar
        a = sm((t - 58.3) / 1.0) * (1 - sm((t - 63.0) / .9)) * (.85 + .15 * math.sin(t * 6))
        L += [HEART * a, particles(t, 58.0, 6.0, RED, EMB, "ember") * a]
        for i, F in enumerate(FLC[:4]):
            g = sm((t - 60.5 - i * .3) / 1.4)
            if g > 0: o = F.copy(); o[:max(0, int(H - (H - 650) * g - 50))] = 0; L.append(o * a)
    if 162.5 <= t < 188.4:  # naqarot takrori — sekin tushayotgan qizil barglar
        a = sm((t - 162.5) / 2) * (1 - sm((t - 187.4) / 1.0)) * .55; L.append(particles(t, 162.5, 25, ROSE, PET, "petal") * a)
    if t >= 195.6:  # OXIRI: qora fon, qizil neon «O'zingni angla», barglar
        a = flick(t, 196.6) * (1 - sm((t - 205.2) / 1.6))
        L += [wipe(FIN, sm((t - 196.6) / 1.6)) * a, FIN2 * sm((t - 199.0) / 1.2) * (1 - sm((t - 205.2) / 1.6)),
              particles(t, 195.6, 12, ROSE, PET, "petal") * sm((t - 197) / 1.5) * (1 - sm((t - 205.2) / 1.6)) * .8]
    return L
dec = subprocess.Popen(["ffmpeg", "-v", "error", "-i", f"{W0}/base.mp4", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                        "-c:v", "libx264", "-crf", "17", "-preset", "fast", "-pix_fmt", "yuv420p", f"{W0}/fx.mp4"], stdin=subprocess.PIPE)
n = 0; FS = W * H * 3
while True:
    buf = dec.stdout.read(FS)
    if len(buf) < FS: break
    t = n / FPS; L = effects(t)
    if L:
        fr = np.frombuffer(buf, np.uint8).reshape(H, W, 3).astype(np.float32) / 255
        for l in L:
            if isinstance(l, tuple): fr = fr * (1 - l[1][..., None])  # soya (qorong'ilatish)
            else: fr = 1 - (1 - fr) * (1 - np.clip(l, 0, 1))  # screen
        buf = (fr * 255).astype(np.uint8).tobytes()
    enc.stdin.write(buf); n += 1
enc.stdin.close(); enc.wait(); dec.wait(); print("frames", n, flush=True)
# ---------- 3) so'zlar (ASS) + qo'shiq ----------
def a_(x): return f"0:{int(x // 60):02}:{x % 60:05.2f}"
ass = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: L,Liberation Serif,56,&H00E6F4FF,&H00FFFFFF,&H00101828,&H78000000,-1,-1,0,0,100,100,0,0,1,3.5,2,2,90,90,64,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
for i, (t0, li) in enumerate(LINES):
    t1 = LEND.get(i, LINES[i + 1][0] - 0.25 if i + 1 < len(LINES) else END - 2)
    ass += f"Dialogue: 0,{a_(t0 - 0.15)},{a_(t1)},L,,0,0,0,,{{\\fad(250,250)}}{LY[li]}\n"
open(f"{W0}/lyrics_uz.ass", "w").write(ass)
run(["ffmpeg", "-v", "error", "-y", "-i", f"{W0}/fx.mp4", "-i", SONG, "-filter_complex",
     f"[0:v]subtitles={W0}/lyrics_uz.ass,fade=t=in:d=1.0,fade=t=out:st={END - 1.2}:d=1.2[v];[1:a]atrim=0:{END},afade=t=out:st={END - 2.5}:d=2.5[au]",
     "-map", "[v]", "-map", "[au]", "-t", str(END), "-c:v", "libx264", "-crf", "19", "-preset", "medium", "-c:a", "aac", "-b:a", "192k",
     "-movflags", "+faststart", f"{W0}/ozlik2.mp4"])
print("ok", END)
