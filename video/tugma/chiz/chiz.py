#!/usr/bin/env python3
"""«Bitta tugma»: Excel/Word sahnalari kodda — sariq qog'oz, siyoh chizgi, neon ko'k (tanlangan) va qizil (bosilgan tugma).
python3 video/tugma/chiz/chiz.py <out_dir> [s03 s04 s05 s06w s07 s09]  → <out>/<sahna>.mp4 (1080x1920, 30 fps, ovozsiz)"""
import os, sys, math, random, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W, H, FPS = 1080, 1920, 30
INK = (66, 42, 22); INK2 = (120, 88, 55); PAPER = (240, 214, 160); CELL = (246, 228, 188)
BLUE = (40, 200, 255); RED = (255, 52, 64)
FD = "/usr/share/fonts/truetype/dejavu/"
def F(s, b=False, m=False): return ImageFont.truetype(FD + ("DejaVuSansMono.ttf" if m else ("DejaVuSerif-Bold.ttf" if b else "DejaVuSerif.ttf")), s)
def _paper():
    rng = np.random.default_rng(5); base = np.zeros((H, W, 3), np.float32); base[:] = PAPER
    for sc, a in ((8, 26), (40, 18)):
        n = rng.random((H // sc + 1, W // sc + 1)).astype(np.float32)
        n = np.asarray(Image.fromarray((n * 255).astype(np.uint8)).resize((W, H), Image.BICUBIC), np.float32) / 255.
        base += (n[..., None] - .5) * a
    yy, xx = np.mgrid[0:H, 0:W]; v = ((xx - W / 2) / W) ** 2 + ((yy - H / 2) / H) ** 2
    base *= (1 - .6 * v)[..., None]
    return Image.fromarray(np.clip(base, 0, 255).astype(np.uint8)).convert("RGBA")
PAPER_IM = _paper()
ease = lambda x: 0 if x <= 0 else 1 if x >= 1 else x * x * (3 - 2 * x)
ramp = lambda t, a, d: ease((t - a) / d)
def line(d, a, b, w=3, col=INK, p=1.0, seed=0):
    if p <= 0: return
    r = random.Random(hash((round(a[0]), round(a[1]), round(b[0]), round(b[1]), seed)))
    (x0, y0), (x1, y1) = a, b; N = max(8, int(math.hypot(x1 - x0, y1 - y0) / 25)); pts = []
    for i in range(int(N * p) + 1):
        t = i / N; pts.append((x0 + (x1 - x0) * t + r.uniform(-1.3, 1.3), y0 + (y1 - y0) * t + r.uniform(-1.3, 1.3)))
    if len(pts) > 1: d.line(pts, fill=col, width=w, joint="curve")
def box(d, x0, y0, x1, y1, w=3, col=INK, p=1.0, fill=None, seed=0):
    if fill: d.rectangle((x0, y0, x1, y1), fill=fill)
    for a, b in (((x0, y0), (x1, y0)), ((x1, y0), (x1, y1)), ((x1, y1), (x0, y1)), ((x0, y1), (x0, y0))): line(d, a, b, w, col, p, seed)
def hatch(d, x0, y0, x1, y1, col=INK2, step=14, w=1):
    for k in range(int(x0 - (y1 - y0)), int(x1), step):
        a = (max(x0, k), y0 + max(0, x0 - k)); b = (min(x1, k + (y1 - y0)), y0 + min(y1 - y0, x1 - k))
        if a[0] < b[0]: d.line((a, b), fill=col, width=w)
def glow(im, fn, col, r=16, k=2):
    g = Image.new("RGBA", im.size, (0, 0, 0, 0)); fn(ImageDraw.Draw(g), col)
    a = g.getchannel("A").filter(ImageFilter.GaussianBlur(r)).point(lambda v: min(255, v * k))
    bl = Image.new("RGBA", im.size, col[:3] + (0,)); bl.putalpha(a)
    im.alpha_composite(bl); im.alpha_composite(g)
def ctext(d, cx, y, s, f, col=INK): d.text((cx - d.textlength(s, font=f) / 2, y), s, font=f, fill=col)
def key(im, x, y, lab, pressed=False, w=230, h=170):
    d = ImageDraw.Draw(im); dy = 10 if pressed else 0
    d.rounded_rectangle((x + 6, y + 14, x + w + 6, y + h + 14), 26, fill=(150, 112, 70))
    d.rounded_rectangle((x, y + dy, x + w, y + h + dy), 26, fill=(248, 230, 190), outline=INK, width=5)
    f = F(74 if len(lab) < 4 else 60, True); bb = d.textbbox((0, 0), lab, font=f)
    d.text((x + w / 2 - (bb[2] + bb[0]) / 2, y + dy + h / 2 - (bb[3] + bb[1]) / 2), lab, font=f, fill=INK)
    if pressed: glow(im, lambda g, c: g.rounded_rectangle((x, y + dy, x + w, y + h + dy), 26, outline=c, width=8), RED, 20)
def keys(im, t, labels, t0, t1, y=1500):
    """tugmalar t0 dan ko'rinadi, t1–t1+0.45 bosiladi"""
    if t < t0: return
    a = ramp(t, t0, .3); n = len(labels); kw = 230; gap = 110; tot = n * kw + (n - 1) * gap; x = (W - tot) / 2
    lay = Image.new("RGBA", im.size, (0, 0, 0, 0)); pr = t1 <= t <= t1 + .45
    for i, lb in enumerate(labels):
        key(lay, x + i * (kw + gap), y, lb, pr)
        if i < n - 1: ctext(ImageDraw.Draw(lay), x + i * (kw + gap) + kw + gap / 2, y + 40, "+", F(80, True))
    if a < 1: lay.putalpha(lay.getchannel("A").point(lambda v: int(v * a)))
    im.alpha_composite(lay)
def title(d, s, y=120, sz=80): ctext(d, W / 2, y, s, F(sz, True))
def window(d, x0, y0, x1, y1, name, p=1.0):
    box(d, x0, y0, x1, y1, 5, INK, p, fill=CELL if p >= 1 else None, seed=1)
    if p >= 1:
        d.rectangle((x0 + 3, y0 + 3, x1 - 3, y0 + 74), fill=(220, 188, 130)); line(d, (x0, y0 + 76), (x1, y0 + 76), 4)
        d.text((x0 + 26, y0 + 14), name, font=F(42, True), fill=INK)
        for i in range(3): d.ellipse((x1 - 50 - i * 46, y0 + 26, x1 - 26 - i * 46, y0 + 50), outline=INK, width=3)
# ---------- Excel jadvali ----------
class Sheet:
    def __init__(s, x0=90, y0=520, cw=(110, 400, 300), rh=104, rows=8): s.x0, s.y0, s.cw, s.rh, s.rows = x0, y0, cw, rh, rows
    def cx(s, c): return s.x0 + sum(s.cw[:c])
    def cell(s, c, r): return (s.cx(c), s.y0 + r * s.rh, s.cx(c + 1), s.y0 + (r + 1) * s.rh)
    def grid(s, d, p=1.0, cols="ABC"):
        x1 = s.cx(len(s.cw)); ys = [s.y0, s.y0 + 70] + [s.y0 + 70 + k * s.rh for k in range(1, s.rows)]; y1 = ys[-1]
        d.rectangle((s.x0, s.y0, x1, y1), fill=CELL)
        d.rectangle((s.x0, s.y0, x1, s.y0 + 70), fill=(226, 196, 140)); d.rectangle((s.x0, s.y0, s.x0 + s.cw[0], y1), fill=(226, 196, 140))
        for r, y in enumerate(ys): line(d, (s.x0, y), (x1, y), 3, INK, p, r)
        for c in range(len(s.cw) + 1): line(d, (s.cx(c), s.y0), (s.cx(c), y1), 3, INK, p, 10 + c)
        if p >= 1:
            for c, L in enumerate(cols[:len(s.cw) - 1]): ctext(d, (s.cx(c + 1) + s.cx(c + 2)) / 2, s.y0 + 12, L, F(40, True), INK2)
            for r in range(1, s.rows): ctext(d, s.x0 + s.cw[0] / 2, s.y0 + 70 + (r - 1) * s.rh + 28, str(r), F(38, True), INK2)
    def put(s, d, c, r, txt, col=INK, bold=False, right=False, sz=46):
        x0, y0, x1, y1 = s.rc(c, r)
        f = F(sz, bold); x = x1 - 22 - d.textlength(txt, font=f) if right else x0 + 20
        d.text((x, y0 + (s.rh - sz) / 2 - 6), txt, font=f, fill=col)
    def rc(s, c, r):  # haqiqiy katak chegarasi (sarlavha qatori 70 px)
        x0, _, x1, _ = s.cell(c, r); y0 = s.y0 + 70 + (r - 1) * s.rh; return (x0, y0, x1, y0 + s.rh)
def fbar(d, txt, y=410, col=INK):
    box(d, 90, y, 990, y + 80, 3, INK, 1, fill=CELL, seed=3); d.text((110, y + 16), "fx", font=F(40, True), fill=INK2)
    line(d, (180, y + 8), (180, y + 72), 3); d.text((205, y + 16), txt, font=F(42, False, True), fill=col)
def s03(t):  # Alt + = (6.4 s)
    im = PAPER_IM.copy(); d = ImageDraw.Draw(im); title(d, "Excel")
    S = Sheet(cw=(100, 430, 350), rh=100, rows=8); S.y0 = 400
    items = [("Non", "12 000"), ("Sut", "9 500"), ("Choy", "24 000"), ("Shakar", "15 000"), ("Guruch", "31 000")]
    S.grid(d, ramp(t, 0, 1.0), "AB")
    if t >= 1.0:
        S.put(d, 1, 1, "Mahsulot", bold=True); S.put(d, 2, 1, "Narx", bold=True, right=True)
        for i, (a, b) in enumerate(items):
            if t > 1.0 + i * .12: S.put(d, 1, i + 2, a); S.put(d, 2, i + 2, b, right=True)
    tot = S.rc(2, 7); fr = ""
    if t > 2.0:
        glow(im, lambda g, c: g.rectangle(tot, outline=c, width=7), BLUE, 14); d = ImageDraw.Draw(im)
        S.put(d, 1, 7, "Jami", bold=True)
    if 3.2 <= t < 4.0:
        fr = "=SUM(B2:B6)"; rr = (S.rc(2, 2)[0], S.rc(2, 2)[1], S.rc(2, 6)[2], S.rc(2, 6)[3])
        glow(im, lambda g, c: g.rectangle(rr, outline=c, width=4), BLUE, 8, 1); d = ImageDraw.Draw(im)
        S.put(d, 2, 7, fr, col=BLUE, sz=34, right=True)
    if t >= 4.0:
        a = ramp(t, 4.0, .35); fr = "=SUM(B2:B6)"
        glow(im, lambda g, c: S.put(g, 2, 7, "91 500", col=c + (int(255 * a),), bold=True, right=True, sz=52), RED, 10); d = ImageDraw.Draw(im)
    fbar(d, fr, 290)
    keys(im, t, ["Alt", "="], 2.4, 3.0, 1190)
    return im
def s04(t):  # Ctrl + T (5.8 s)
    im = PAPER_IM.copy(); d = ImageDraw.Draw(im); title(d, "Excel")
    S = Sheet(cw=(100, 430, 350), rh=100, rows=7); S.y0 = 330
    rows = [("Mijoz", "Qarz"), ("Aziz", "150 000"), ("Dilnoza", "80 000"), ("Jasur", "210 000"), ("Malika", "45 000"), ("Sardor", "120 000")]
    S.grid(d, 1.0, "AB")
    a = ramp(t, 2.6, .8)
    if a > 0:  # jadval: sarlavha ko'k chiziqli, yo'l-yo'l qatorlar
        for r in range(2, 7):
            if r % 2 == 0:
                x0, y0, x1, y1 = S.rc(1, r); x1 = S.rc(2, r)[2]
                if a >= 1 or (r - 2) / 5 < a: hatch(d, x0 + 4, y0 + 4, x1 - 4, y1 - 4, (205, 170, 115), 12, 2)
        hx0, hy0, _, hy1 = S.rc(1, 1); hx1 = S.rc(2, 1)[2]
        d.rectangle((hx0 + 3, hy0 + 3, hx1 - 3, hy1 - 3), fill=(214, 176, 112))
    for i, (x, y) in enumerate(rows):
        S.put(d, 1, i + 1, x, bold=(i == 0)); S.put(d, 2, i + 1, y, bold=(i == 0), right=(i > 0))
    if a > 0:
        hx0, hy0, _, hy1 = S.rc(1, 1); hx1 = S.rc(2, 6)[2]; yb = S.rc(2, 6)[3]
        glow(im, lambda g, c: g.rectangle((hx0, hy0, hx1, yb), outline=c + (int(255 * a),), width=6), BLUE, 14)
        d = ImageDraw.Draw(im)
        for c in (1, 2):  # filtr tugmachalari ▼
            x0, y0, x1, y1 = S.rc(c, 1); bx = x1 - 64
            d.rectangle((bx, y0 + 26, bx + 46, y0 + 72), fill=CELL, outline=INK, width=3); d.polygon([(bx + 10, y0 + 40), (bx + 36, y0 + 40), (bx + 23, y0 + 60)], fill=INK)
    if t >= 0.6: glow(im, lambda g, c: g.rectangle(S.rc(1, 2), outline=c, width=5), BLUE, 8, 1)
    keys(im, t, ["Ctrl", "T"], 1.2, 2.2, 1080)
    return im
def s05(t):  # Ctrl + E (8.8 s)
    im = PAPER_IM.copy(); d = ImageDraw.Draw(im); title(d, "Excel")
    S = Sheet(cw=(90, 500, 300), rh=100, rows=7); S.y0 = 330
    names = [("Aziz Karimov", "Aziz"), ("Dilnoza Rahimova", "Dilnoza"), ("Jasur Toshev", "Jasur"), ("Malika Yusupova", "Malika"), ("Sardor Aliyev", "Sardor")]
    S.grid(d, 1.0, "AB"); S.put(d, 1, 1, "Ism Familiya", bold=True); S.put(d, 2, 1, "Ism", bold=True)
    for i, (n, _) in enumerate(names): S.put(d, 1, i + 2, n, sz=42)
    typed = "Aziz"[:max(0, min(4, int((t - 1.0) / .22) + 1))] if t >= 1.0 else ""
    if t < 4.6: glow(im, lambda g, c: g.rectangle(S.rc(2, 2) if t < 2.4 else S.rc(2, 3), outline=c, width=6), BLUE, 10); d = ImageDraw.Draw(im)
    if typed: S.put(d, 2, 2, typed + ("|" if t < 2.0 and int(t * 4) % 2 == 0 else ""), sz=42)
    if t >= 4.6:
        for i, (_, s) in enumerate(names[1:]):
            a = ramp(t, 4.6 + i * .25, .3)
            if a > 0: glow(im, lambda g, c, i=i, s=s: S.put(g, 2, i + 3, s, col=c + (int(255 * a),), sz=42, bold=True), BLUE, 8, 1)
        d = ImageDraw.Draw(im)
        if t > 6.2:  # «o'zi to'ldirdi» belgisi
            x0, y0, x1, y1 = S.rc(2, 6); glow(im, lambda g, c: g.line([(x1 - 70, y1 + 50), (x1 - 45, y1 + 80), (x1 + 5, y1 + 20)], fill=c, width=9), RED, 10)
    keys(im, t, ["Ctrl", "E"], 2.6, 3.8, 1080)
    return im
def s06w(t):  # Word: Fayl → Yaratish → «Резюме» → namuna (8.6 s)
    im = PAPER_IM.copy(); d = ImageDraw.Draw(im); title(d, "Word")
    window(d, 70, 240, 1010, 1390, "Hujjat 1 – Word", 1.0)
    # menyu
    d.text((110, 340), "Fayl", font=F(48, True), fill=INK); d.text((290, 344), "Bosh sahifa", font=F(40), fill=INK2)
    if 0.6 <= t < 1.6: glow(im, lambda g, c: g.rectangle((96, 332, 236, 400), outline=c, width=6), BLUE, 12); d = ImageDraw.Draw(im)
    if t >= 1.4:  # Fayl paneli
        d.rectangle((90, 420, 990, 1370), fill=(232, 204, 150)); line(d, (90, 420), (990, 420), 3)
        items = ["Yaratish", "Ochish", "Saqlash", "Chop etish"]
        for i, it in enumerate(items): d.text((130, 460 + i * 90), it, font=F(46, i == 0), fill=INK)
        d.text((130, 840), "(File → New / Файл → Создать)", font=F(30), fill=INK2)
        if 1.9 <= t < 3.0: glow(im, lambda g, c: g.rectangle((112, 450, 400, 526), outline=c, width=6), BLUE, 12); d = ImageDraw.Draw(im)
    if t >= 2.8:  # qidiruv + namunalar
        d.rectangle((90, 420, 990, 1370), fill=CELL); line(d, (90, 420), (990, 420), 3)
        box(d, 140, 460, 940, 550, 4, INK, 1, fill=(250, 236, 200), seed=4)
        q = "Резюме"[:max(0, min(6, int((t - 3.0) / .16) + 1))] if t >= 3.0 else ""
        d.text((170, 478), "Qidiruv:", font=F(40), fill=INK2); d.text((360, 474), q, font=F(46, True), fill=INK)
        if t >= 4.2:
            for i in range(3):
                x = 150 + i * 280; y = 620; a = ramp(t, 4.2 + i * .15, .3)
                if a <= 0: continue
                box(d, x, y, x + 230, y + 320, 3, INK, a, fill=(252, 240, 210), seed=20 + i)
                if a >= 1:
                    d.ellipse((x + 20, y + 24, x + 80, y + 84), outline=INK, width=3)
                    for k in range(7): line(d, (x + 20, y + 110 + k * 28), (x + 210 - (k % 3) * 40, y + 110 + k * 28), 2, INK2, 1, 30 + i * 10 + k)
            if t >= 5.2: glow(im, lambda g, c: g.rectangle((430, 620, 660, 940), outline=c, width=7), BLUE, 14); d = ImageDraw.Draw(im)
            d.text((150, 980), "Tayyor namunani tanlang", font=F(40, True), fill=INK)
    if t >= 6.0:  # ochilgan namuna
        a = ramp(t, 6.0, .5); pg = Image.new("RGBA", im.size, (0, 0, 0, 0)); g = ImageDraw.Draw(pg)
        g.rectangle((150, 420, 930, 1370), fill=(252, 242, 214), outline=INK, width=4)
        g.text((200, 450), "Ism Familiya", font=F(60, True), fill=INK); g.text((200, 525), "+998 __ ___ __ __", font=F(36), fill=INK2)
        sec = [("Ish joylari", 3), ("Ma'lumoti", 2), ("Nima qila olaman", 3)]; y = 610
        for nm, k in sec:
            g.text((200, y), nm, font=F(44, True), fill=INK); g.line((200, y + 60, 880, y + 60), fill=RED, width=3); y += 90
            for j in range(k): g.line((220, y + j * 46, 860 - j * 90, y + j * 46), fill=INK2, width=3)
            y += k * 46 + 24
        pg.putalpha(pg.getchannel("A").point(lambda v: int(v * a))); im.alpha_composite(pg)
        if t > 6.8: glow(im, lambda g, c: g.rectangle((150, 420, 930, 1370), outline=c, width=6), BLUE, 16)
    return im
def phone(im, x, y, w=420, h=820, fn=None):
    d = ImageDraw.Draw(im); d.rounded_rectangle((x, y, x + w, y + h), 50, fill=(70, 50, 34), outline=INK, width=5)
    d.rounded_rectangle((x + 22, y + 60, x + w - 22, y + h - 60), 20, fill=CELL)
    d.rounded_rectangle((x + w / 2 - 50, y + 24, x + w / 2 + 50, y + 38), 7, fill=INK)
    if fn: fn(d, x + 22, y + 60, x + w - 22, y + h - 60)
def s07(t):  # Saqlash → PDF → telefon (6.0 s)
    im = PAPER_IM.copy(); d = ImageDraw.Draw(im); title(d, "Word")
    if t < 3.0:
        window(d, 70, 260, 1010, 1260, "Saqlash", 1.0)
        d.text((120, 420), "Fayl nomi:", font=F(40), fill=INK2); d.text((360, 416), "Ism_Familiya", font=F(44, True), fill=INK)
        d.text((120, 520), "Turi:", font=F(40), fill=INK2)
        opts = ["Word hujjati (.docx)", "PDF (.pdf)"]
        box(d, 120, 580, 960, 680, 3, INK, 1, fill=(250, 236, 200), seed=5)
        if t < 1.0: d.text((150, 600), opts[0], font=F(44), fill=INK)
        else:
            for i, o in enumerate(opts): d.rectangle((120, 680 + i * 100, 960, 780 + i * 100), fill=(250, 236, 200), outline=INK, width=3); d.text((150, 700 + i * 100), o, font=F(44, i == 1), fill=INK)
            if t >= 1.6:
                glow(im, lambda g, c: g.rectangle((120, 780, 960, 880), outline=c, width=7), RED, 14); d = ImageDraw.Draw(im)
        box(d, 700, 1150, 960, 1250, 4, INK, 1, fill=(214, 176, 112), seed=6); ctext(d, 830, 1168, "Saqlash", F(44, True))
        if 2.3 <= t < 3.0: glow(im, lambda g, c: g.rectangle((700, 1150, 960, 1250), outline=c, width=7), BLUE, 12)
    else:  # fayl telefonga uchadi
        k = ramp(t, 3.0, 1.2); px, py = 330, 300
        def scr(g, x0, y0, x1, y1):
            if k >= 1:
                g.rectangle((x0 + 20, y0 + 30, x1 - 20, y1 - 30), fill=(252, 242, 214), outline=INK, width=3)
                g.text((x0 + 40, y0 + 50), "Ism Familiya", font=F(34, True), fill=INK)
                for j in range(9): g.line((x0 + 40, y0 + 120 + j * 44, x1 - 40 - (j % 3) * 50, y0 + 120 + j * 44), fill=INK2, width=3)
        phone(im, px, py, fn=scr); d = ImageDraw.Draw(im)
        if k < 1:
            fx = 160 + (px + 110 - 160) * k; fy = 900 + (py + 300 - 900) * k; s = 1 - .3 * k
            d.rectangle((fx, fy, fx + 200 * s, fy + 260 * s), fill=(252, 242, 214), outline=INK, width=4)
            glow(im, lambda g, c: g.text((fx + 30 * s, fy + 90 * s), "PDF", font=F(int(64 * s), True), fill=c), RED, 10)
        else:
            glow(im, lambda g, c: g.rounded_rectangle((px, py, px + 420, py + 820), 50, outline=c, width=6), BLUE, 16)
            d = ImageDraw.Draw(im); ctext(d, W / 2, 1180, "Har qanday telefonda bir xil", F(48, True))
    return im
def s09(t):  # bot kartasi (9.0 s)
    im = PAPER_IM.copy(); d = ImageDraw.Draw(im)
    ctext(d, W / 2, 200, "Excel yoki Word'da", F(68, True)); ctext(d, W / 2, 290, "qotib qoldingizmi?", F(68, True))
    def chat(g, x0, y0, x1, y1):
        if t >= 1.0:  # mijoz: ekran rasmi
            g.rounded_rectangle((x1 - 250, y0 + 40, x1 - 20, y0 + 220), 18, fill=(214, 176, 112), outline=INK, width=3)
            for r in range(4): g.line((x1 - 235, y0 + 70 + r * 36, x1 - 35, y0 + 70 + r * 36), fill=INK, width=2)
            for c in range(3): g.line((x1 - 235 + c * 66, y0 + 60, x1 - 235 + c * 66, y0 + 200), fill=INK, width=2)
        if t >= 2.4:
            g.rounded_rectangle((x0 + 18, y0 + 260, x1 - 50, y0 + 640), 22, fill=(250, 238, 206), outline=INK, width=3)
            lines = ["1. Katakni tanlang", "2. Alt + = bosing", "3. Enter bosing"]
            for j, s in enumerate(lines):
                if t >= 2.6 + j * .5: g.text((x0 + 36, y0 + 300 + j * 110), s, font=F(28, True), fill=INK)
    phone(im, 330, 430, fn=chat); d = ImageDraw.Draw(im)
    ctext(d, W / 2, 1300, "Ekran rasmini yuboring:", F(50, True)); ctext(d, W / 2, 1370, "qadamma-qadam ko'rsatadi", F(50))
    h = "@sahiychishopbot"; f = F(76, True); tw = d.textlength(h, font=f); y = 1480
    d.rounded_rectangle(((W - tw) / 2 - 40, y - 20, (W + tw) / 2 + 40, y + 120), 30, fill=(250, 236, 200), outline=INK, width=5); ctext(d, W / 2, y + 6, h, f)
    glow(im, lambda g, c: g.rounded_rectangle(((W - tw) / 2 - 40, y - 20, (W + tw) / 2 + 40, y + 120), 30, outline=c, width=7), BLUE, 18)
    return im
SC = {"s03": (s03, 6.9), "s04": (s04, 6.0), "s05": (s05, 6.8), "s06w": (s06w, 8.6), "s07": (s07, 6.4), "s09": (s09, 9.4)}
if __name__ == "__main__":
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    for name in (sys.argv[2:] or list(SC)):
        fn, dur = SC[name]
        p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                              "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p", f"{out}/{name}.mp4"], stdin=subprocess.PIPE)
        for i in range(int(dur * FPS)): p.stdin.write(fn(i / FPS).convert("RGB").tobytes())
        p.stdin.close(); p.wait(); print(name, dur)
