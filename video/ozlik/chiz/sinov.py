#!/usr/bin/env python3
"""«O'zligim» 15 s sinov (16:9): qog'ozda siyoh yo'l chiziladi, bola uzoqdan kameraga yurib keladi va kattarib boradi; 11.7 s da birinchi satr siyohda yoziladi.
python3 video/ozlik/chiz/sinov.py <out.mp4>"""
import sys, math, random, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W, H, FPS, DUR = 1920, 1080, 30, 15.0
INK = (62, 40, 20); INK2 = (125, 92, 58); BLUE = (40, 200, 255); RED = (255, 60, 70)
FD = "/usr/share/fonts/truetype/dejavu/"
def F(s, b=False, i=False): return ImageFont.truetype(("/usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf" if i else FD + ("DejaVuSerif-Bold.ttf" if b else "DejaVuSerif.ttf")), s)
rng = np.random.default_rng(7); base = np.zeros((H, W, 3), np.float32); base[:] = (238, 210, 156)
for sc, a in ((6, 24), (30, 20), (120, 16)):
    n = rng.random((H // sc + 1, W // sc + 1)).astype(np.float32)
    base += (np.asarray(Image.fromarray((n * 255).astype(np.uint8)).resize((W, H), Image.BICUBIC), np.float32)[..., None] / 255. - .5) * a
yy, xx = np.mgrid[0:H, 0:W]; base *= (1 - .55 * (((xx - W / 2) / W) ** 2 + ((yy - H / 2) / H) ** 2) * 1.6)[..., None]
PAPER = Image.fromarray(np.clip(base, 0, 255).astype(np.uint8)).convert("RGBA")
ease = lambda x: 0 if x <= 0 else 1 if x >= 1 else x * x * (3 - 2 * x)
def wline(d, a, b, w, col, p=1.0, seed=0, jit=1.6):
    if p <= 0: return
    r = random.Random(seed); (x0, y0), (x1, y1) = a, b; N = max(6, int(math.hypot(x1 - x0, y1 - y0) / 18)); pts = []
    for i in range(int(N * p) + 1):
        t = i / N; pts.append((x0 + (x1 - x0) * t + r.uniform(-jit, jit), y0 + (y1 - y0) * t + r.uniform(-jit, jit)))
    if len(pts) > 1: d.line(pts, fill=col, width=w, joint="curve")
def glow(im, fn, col, r=18, k=2.2):
    g = Image.new("RGBA", im.size, (0, 0, 0, 0)); fn(ImageDraw.Draw(g))
    a = g.getchannel("A").filter(ImageFilter.GaussianBlur(r)).point(lambda v: min(255, int(v * k)))
    bl = Image.new("RGBA", im.size, col + (0,)); bl.putalpha(a); im.alpha_composite(bl); im.alpha_composite(g)
VP = (960, 455)
def scene(t, d, im):
    p = ease(t / 2.2)  # yo'l chiziladi
    for k, (x, s) in enumerate(((560, 1), (1360, 2))):
        wline(d, (x, H), (VP[0] + (x - 960) * .04, VP[1]), 5, INK, p, s)
    for i in range(14):  # yo'l ustidagi shtrixlar
        f = (i + .5) / 14; y = VP[1] + (H - VP[1]) * f ** 1.6
        if p > f: hw = 18 + 380 * f ** 1.6; wline(d, (960 - hw * .6, y), (960 - hw * .2, y + 4), 2, INK2, 1, 40 + i)
    q = ease((t - 1.0) / 2.0)  # tepaliklar va daraxtlar
    if q > 0:
        for k, (x0, x1, h) in enumerate(((0, 760, 70), (1160, 1920, 90), (420, 1500, 40))):
            pts = [(x0 + (x1 - x0) * i / 40, VP[1] - h * math.sin(math.pi * i / 40) + random.Random(k * 100 + i).uniform(-3, 3)) for i in range(int(41 * q))]
            if len(pts) > 1: d.line(pts, fill=INK, width=3)
        for k, (x, s) in enumerate(((300, 1.0), (1650, 1.2), (180, .7), (1780, .8))):
            if q > .3 + k * .1:
                b = VP[1] + 20 * s; d.line((x, b + 160 * s, x, b - 10), fill=INK, width=int(6 * s))
                for j in range(30):
                    r_ = random.Random(k * 50 + j); a = r_.uniform(0, 6.28); rr = r_.uniform(20, 90) * s
                    d.arc((x + math.cos(a) * rr - 30 * s, b - 80 * s + math.sin(a) * rr * .7 - 20 * s, x + math.cos(a) * rr + 30 * s, b - 80 * s + math.sin(a) * rr * .7 + 20 * s), 0, 300, fill=INK2, width=2)
    m = ease((t - 2.0) / 1.5)  # neon ko'k oy
    if m > 0:
        def moon(g):
            mk = Image.new("L", (140, 140), 0); md = ImageDraw.Draw(mk); md.ellipse((10, 10, 130, 130), fill=int(255 * m)); md.ellipse((48, -4, 168, 116), fill=0)
            g.bitmap((1620, 200), mk, fill=BLUE + (255,))
        glow(im, moon, BLUE, 22)
def boy(im, t):
    if t < 2.6: return
    u = (t - 2.6) / (DUR - 2.6); p = u ** 1.35
    fy = VP[1] + 18 + (920 - VP[1] - 18) * p; s = .10 + .62 * p; cx = 960 + 40 * math.sin(u * 2.2)
    ph = t * 5.2; a = math.sin(ph); bob = abs(math.cos(ph)) * 10 * s
    L = Image.new("RGBA", im.size, (0, 0, 0, 0)); g = ImageDraw.Draw(L)
    S = lambda v: v * s
    g.ellipse((cx - S(110), fy - S(18), cx + S(110), fy + S(18)), fill=(90, 60, 30, 90))  # soya
    for side, sg in ((-1, a), (1, -a)):  # oyoqlar (old tomonga yurish: ko'tariladi/tushadi)
        lift = max(0, sg) * S(40); x = cx + side * S(38)
        g.line((x, fy - S(230) - bob, x + side * S(4), fy - lift), fill=INK, width=max(2, int(S(34))))
        g.ellipse((x - S(30), fy - lift - S(18), x + S(30) + side * S(6), fy - lift + S(10)), fill=(70, 46, 26))
    top = fy - S(470) - bob
    g.polygon([(cx - S(70), top + S(120)), (cx + S(70), top + S(120)), (cx + S(105), fy - S(200) - bob), (cx - S(105), fy - S(200) - bob)], fill=(214, 172, 108), outline=INK)  # to'n
    for i in range(6): g.line((cx - S(60) + i * S(24), top + S(140), cx - S(80) + i * S(32), fy - S(210) - bob), fill=INK2, width=max(1, int(S(4))))
    g.line((cx - S(95), fy - S(270) - bob, cx + S(95), fy - S(270) - bob), fill=(150, 40, 40), width=max(2, int(S(14))))  # belbog'
    for side, sg in ((-1, -a), (1, a)):  # qo'llar
        sx = cx + side * S(72); sy = top + S(140); ex = sx + side * S(30); ey = sy + S(170) + sg * S(28)
        g.line((sx, sy, ex, ey), fill=(205, 165, 105), width=max(2, int(S(30)))); g.ellipse((ex - S(18), ey - S(14), ex + S(18), ey + S(20)), fill=(236, 200, 150), outline=INK)
    hx, hy, hr = cx, top + S(60), S(66)  # bosh
    g.ellipse((hx - hr, hy - hr, hx + hr, hy + hr), fill=(240, 206, 156), outline=INK, width=max(1, int(S(5))))
    g.chord((hx - hr - S(4), hy - hr - S(10), hx + hr + S(4), hy + hr * .5), 180, 360, fill=(48, 30, 16))  # soch
    g.rounded_rectangle((hx - hr * .95, hy - hr * 1.15, hx + hr * .95, hy - hr * .55), radius=S(20), fill=(30, 30, 60), outline=INK)  # do'ppi
    for k in range(4): g.line((hx - hr * .7 + k * hr * .45, hy - hr * 1.05, hx - hr * .6 + k * hr * .45, hy - hr * .65), fill=(230, 230, 230), width=max(1, int(S(4))))
    for side in (-1, 1): g.ellipse((hx + side * S(24) - S(7), hy + S(4), hx + side * S(24) + S(7), hy + S(18)), fill=INK)
    g.arc((hx - S(18), hy + S(18), hx + S(18), hy + S(40)), 20, 160, fill=INK, width=max(1, int(S(4))))
    al = L.getchannel("A"); edge = al.filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.GaussianBlur(4))
    halo = Image.new("RGBA", im.size, (255, 250, 235, 0)); halo.putalpha(edge.point(lambda v: int(v * .8)))  # oq chet nuri (qog'oz qirqimi)
    im.alpha_composite(halo); im.alpha_composite(L)
LYR = "Men o'zimni izladim, o'zimdan yiroqlarda,"
def lyric(im, t, t0=11.7):
    if t < t0: return
    k = ease((t - t0) / 2.4); f = F(62, i=True); d = ImageDraw.Draw(im)
    tw = d.textlength(LYR, font=f); x0 = (W - tw) / 2; y = 70
    L = Image.new("RGBA", im.size, (0, 0, 0, 0)); ImageDraw.Draw(L).text((x0, y), LYR, font=f, fill=INK)
    m = Image.new("L", im.size, 0); ImageDraw.Draw(m).rectangle((0, 0, x0 + tw * k, H), fill=255)
    L.putalpha(Image.composite(L.getchannel("A"), Image.new("L", im.size, 0), m)); im.alpha_composite(L)
    if k > .2: glow(im, lambda g: g.line((x0, y + 86, x0 + tw * k, y + 86), fill=RED + (255,), width=3), RED, 8, 1.5)
out = sys.argv[1]
p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                      "-ss", "0", "-t", str(DUR), "-i", sys.argv[2], "-map", "0:v", "-map", "1:a", "-af", f"afade=t=out:st={DUR - 1.2}:d=1.2",
                      "-c:v", "libx264", "-crf", "20", "-preset", "fast", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-shortest", out], stdin=subprocess.PIPE)
for i in range(int(DUR * FPS)):
    t = i / FPS; im = PAPER.copy(); d = ImageDraw.Draw(im); scene(t, d, im); boy(im, t); lyric(im, t)
    p.stdin.write(im.convert("RGB").tobytes())
p.stdin.close(); p.wait()
