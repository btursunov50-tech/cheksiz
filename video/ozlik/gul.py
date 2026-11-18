"""Gravyura uslubidagi gul (atirgul) — siyoh chiziqlari + ingichka qizil neon chet. build2.py effektlari uchun.
rose(h, seed) -> (ink, neon): ink = L massiv (0..1, qorong'ilatish), neon = RGB massiv (0..1, screen)."""
import math, random
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
S = 3  # ichki o'lcham (silliq chiziq uchun)
def _bez(p0, p1, p2, n=40):
    return [((1-t)**2*p0[0]+2*(1-t)*t*p1[0]+t*t*p2[0], (1-t)**2*p0[1]+2*(1-t)*t*p1[1]+t*t*p2[1]) for t in (i/n for i in range(n+1))]
def rose(h=300, seed=1, bloom=1.0):
    rnd = random.Random(seed); w = int(h * .7)
    W, H = w * S, h * S
    ink = Image.new("L", (W, H), 0); neo = Image.new("L", (W, H), 0); fill = Image.new("L", (W, H), 0)
    di, dn, df = ImageDraw.Draw(ink), ImageDraw.Draw(neo), ImageDraw.Draw(fill)
    cx, base = W / 2, H - 2
    hx, hy = cx + rnd.uniform(-.12, .12) * W, H * .26
    stem = _bez((cx, base), (cx + rnd.uniform(-.25, .25) * W, H * .6), (hx, hy + 30 * S))
    di.line(stem, fill=230, width=4 * S)
    for k in range(5):  # tikanlar
        x, y = stem[int(8 + k * 6)]; d = 1 if k % 2 else -1
        di.polygon([(x, y), (x + d * 9 * S, y - 4 * S), (x, y - 7 * S)], fill=230)
    for j, (pos, side) in enumerate(((22, -1), (31, 1))):  # barglar: shakl + tomir + shtrix
        x, y = stem[pos]; L = (.32 + .05 * j) * W; ang = math.radians(-35 if side < 0 else -145)
        tip = (x + math.cos(ang) * L * -side * (1 if side < 0 else -1), y + math.sin(ang) * L)
        tip = (x + side * L * .9, y - L * .45)
        mid = ((x + tip[0]) / 2, (y + tip[1]) / 2)
        nx, ny = -(tip[1] - y), tip[0] - x; nl = math.hypot(nx, ny) or 1; nx, ny = nx / nl * L * .28, ny / nl * L * .28
        up = _bez((x, y), (mid[0] + nx, mid[1] + ny), tip, 24); dn_ = _bez(tip, (mid[0] - nx, mid[1] - ny), (x, y), 24)
        di.line(up + dn_, fill=245, width=3 * S); di.line([(x, y), tip], fill=230, width=2 * S)
        for t in np.linspace(.15, .85, 7):  # shtrixlar
            px, py = x + (tip[0] - x) * t, y + (tip[1] - y) * t
            di.line([(px, py), (px + nx * .7 * math.sin(t * math.pi), py + ny * .7 * math.sin(t * math.pi))], fill=200, width=S + 1)
    R = W * .30 * (.35 + .65 * bloom)
    pet = []  # tashqi gulbarglar
    for i in range(5):
        a = i * 2 * math.pi / 5 + rnd.uniform(-.2, .2) - math.pi / 2
        px, py = hx + math.cos(a) * R * .55, hy + math.sin(a) * R * .45
        pet.append([px - R * .62, py - R * .55, px + R * .62, py + R * .55])
    for b in pet: df.ellipse(b, fill=255)
    df.ellipse([hx - R * .7, hy - R * .6, hx + R * .7, hy + R * .62], fill=255)
    for b in pet: di.arc(b, 160, 380, fill=245, width=3 * S); dn.arc(b, 200, 340, fill=255, width=S + 1)
    for k in range(6):  # ichki spiral
        r = R * (.62 - k * .095)
        if r <= 2: break
        a0 = rnd.uniform(0, 360); di.arc([hx - r, hy - r * .85, hx + r, hy + r * .85], a0, a0 + 250, fill=250, width=3 * S)
        dn.arc([hx - r, hy - r * .85, hx + r, hy + r * .85], a0 + 20, a0 + 200, fill=210, width=S + 1)
    for k in range(14):  # gul ichida shtrix (soya)
        a = rnd.uniform(.2, 2.9); r1, r2 = R * .3, R * .75
        di.line([(hx + math.cos(a) * r1, hy + math.sin(a) * r1 * .8), (hx + math.cos(a + .25) * r2, hy + math.sin(a + .25) * r2 * .8)], fill=110, width=S)
    def arr(im, blur=0):
        im = im.resize((w, h), Image.LANCZOS)
        if blur: im = im.filter(ImageFilter.GaussianBlur(blur))
        return np.asarray(im, np.float32) / 255
    inkA = np.clip(arr(ink) * 1.1, 0, 1)
    f = arr(fill, 1); n0 = arr(neo); g1 = arr(neo, 3)
    red = np.array([1.0, .1, .14], np.float32)
    neon = g1[..., None] * red * .9 + n0[..., None] * red * .9   # faqat ingichka qizil neon chet
    return f * .82, inkA, np.clip(neon, 0, 1)   # (gul rangi alfa, siyoh, neon)
FILL = np.array([.55, .04, .07], np.float32)  # to'q qizil (gravyura gulbargi)
def put(fr, spr, x0, y0, a=1.0):
    f, ink, ne = spr; h, w = ink.shape
    ys, xs = max(0, -y0), max(0, -x0); y1, x1 = min(h, fr.shape[0] - y0), min(w, fr.shape[1] - x0)
    if y1 <= ys or x1 <= xs: return
    sl = fr[y0 + ys:y0 + y1, x0 + xs:x0 + x1]; f, ink, ne = f[ys:y1, xs:x1, None] * a, ink[ys:y1, xs:x1, None] * a, ne[ys:y1, xs:x1] * a
    sl[:] = sl * (1 - f) + FILL * f; sl *= (1 - ink * .9); sl[:] = 1 - (1 - sl) * (1 - ne)
if __name__ == "__main__":
    import sys
    bg = Image.open(sys.argv[1]).convert("RGB").resize((1920, 1080)); fr = np.asarray(bg, np.float32) / 255
    for i, (x, hh) in enumerate(((1120, 250), (1330, 330), (1560, 280), (1780, 380))):
        spr = rose(hh, i + 3); h, w = spr[1].shape; put(fr, spr, x - w // 2, 1080 - h - 20)
    Image.fromarray((fr * 255).astype(np.uint8)).resize((960, 540)).save(sys.argv[2])

def petal(sz=26, rot=0.0):
    W = sz * 2 * S; f = Image.new("L", (W, W), 0); i = Image.new("L", (W, W), 0); n = Image.new("L", (W, W), 0)
    c = W / 2; pts = [(c + math.cos(t) * sz * S * .9 * (1 + .35 * math.cos(t)), c + math.sin(t) * sz * S * .5) for t in np.linspace(0, 2 * math.pi, 50)]
    ImageDraw.Draw(f).polygon(pts, fill=255); ImageDraw.Draw(i).line(pts + [pts[0]], fill=230, width=S + 1)
    ImageDraw.Draw(i).line([(c - sz * S * .5, c), (c + sz * S * .7, c)], fill=140, width=S); ImageDraw.Draw(n).line(pts + [pts[0]], fill=200, width=S)
    f, i, n = (im.rotate(rot, resample=Image.BICUBIC).resize((sz * 2, sz * 2), Image.LANCZOS) for im in (f, i, n))
    F = np.asarray(f, np.float32) / 255; I = np.asarray(i, np.float32) / 255; N = np.asarray(n.filter(ImageFilter.GaussianBlur(1.5)), np.float32) / 255
    return F * .85, I, np.clip(N[..., None] * np.array([1, .1, .14], np.float32), 0, 1)
