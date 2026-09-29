"""Graphic helpers and static assets for the lemonmedia lawyer-logo reel."""
import math, random
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

W, H = 1080, 1920
F = 'fonts/'
YEL = (255, 218, 0, 255)
WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)
CREAM = (209, 198, 175, 255)
CREAM_D = (192, 178, 156, 255)
GOLD = (201, 162, 39, 255)
BORD = (90, 26, 26, 255)
GREEN = (43, 182, 115, 255)
RED = (229, 57, 53, 255)
MARK = (224, 32, 27, 255)
NAVY = (31, 42, 68, 255)

_fc = {}


def font(name, size):
    k = (name, size)
    if k not in _fc:
        _fc[k] = ImageFont.truetype(F + name, size)
    return _fc[k]


def rrect(w, h, r, fill, ss=3):
    im = Image.new('RGBA', (w * ss, h * ss), (0, 0, 0, 0))
    ImageDraw.Draw(im).rounded_rectangle([0, 0, w * ss - 1, h * ss - 1], r * ss, fill=fill)
    return im.resize((w, h), Image.LANCZOS)


def rr_mask(w, h, r, ss=3):
    im = Image.new('L', (w * ss, h * ss), 0)
    ImageDraw.Draw(im).rounded_rectangle([0, 0, w * ss - 1, h * ss - 1], r * ss, fill=255)
    return im.resize((w, h), Image.LANCZOS)


def shadow(img, blur=30, off=(0, 8), alpha=0.35, pad=60):
    w, h = img.size
    out = Image.new('RGBA', (w + pad * 2, h + pad * 2), (0, 0, 0, 0))
    a = img.getchannel('A').point(lambda v: int(v * alpha))
    sh = Image.new('RGBA', img.size, (0, 0, 0, 255))
    sh.putalpha(a)
    out.alpha_composite(sh, (pad + off[0], pad + off[1]))
    out = out.filter(ImageFilter.GaussianBlur(blur))
    out.alpha_composite(img, (pad, pad))
    return out, pad


# ---------- subtitle plates ----------
def plate(text, kind='y', size=62, maxw=1000):
    fill = YEL if kind == 'y' else WHITE
    fname = 'Rubik-600.ttf' if kind == 'y' else 'Rubik-500.ttf'
    hgt = 120 if kind == 'y' else 110
    padx = 40
    while True:
        f = font(fname, size)
        tw = f.getlength(text)
        if tw + 2 * padx <= maxw or size <= 40:
            break
        size -= 2
        hgt = int(hgt * 0.97)
    w = int(tw + 2 * padx)
    im = rrect(w, hgt, 22, fill)
    d = ImageDraw.Draw(im)
    d.text((w / 2, hgt / 2 + 2), text, font=f, fill=BLACK, anchor='mm')
    return im


def text_block(lines, size=52, fname='Rubik-500.ttf', fill=WHITE, lh=1.2, shadow_a=0):
    f = font(fname, size)
    ws = [f.getlength(l) for l in lines]
    w = int(max(ws)) + 20
    lh_px = int(size * lh)
    h = lh_px * len(lines) + 20
    im = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    for i, l in enumerate(lines):
        d.text((w / 2, 10 + lh_px * i + lh_px / 2), l, font=f, fill=fill, anchor='mm')
    if shadow_a:
        sh = Image.new('RGBA', (w + 40, h + 40), (0, 0, 0, 0))
        a = im.getchannel('A').point(lambda v: int(v * shadow_a))
        s2 = Image.new('RGBA', im.size, (0, 0, 0, 255)); s2.putalpha(a)
        sh.alpha_composite(s2, (20, 22))
        sh = sh.filter(ImageFilter.GaussianBlur(6))
        sh.alpha_composite(im, (20, 20))
        return sh
    return im


# ---------- icons ----------
def check_badge(d=90, col=GREEN, cross=False):
    ss = 4
    im = Image.new('RGBA', (d * ss, d * ss), (0, 0, 0, 0))
    dr = ImageDraw.Draw(im)
    dr.ellipse([0, 0, d * ss - 1, d * ss - 1], fill=RED if cross else col)
    s = d * ss
    wdt = int(s * 0.11)
    if cross:
        dr.line([(s * .3, s * .3), (s * .7, s * .7)], fill=WHITE, width=wdt)
        dr.line([(s * .7, s * .3), (s * .3, s * .7)], fill=WHITE, width=wdt)
    else:
        dr.line([(s * .27, s * .52), (s * .44, s * .68), (s * .74, s * .34)], fill=WHITE, width=wdt, joint='curve')
    return im.resize((d, d), Image.LANCZOS)


def glove(size=300):
    """White cartoon glove with red cuff, index finger pointing LEFT."""
    ss = 3
    S = size * ss
    im = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    u = S / 100
    ol = (25, 25, 25, 255)
    ow = int(2.2 * u)

    def rr(x0, y0, x1, y1, r, fill):
        d.rounded_rectangle([x0 * u, y0 * u, x1 * u, y1 * u], r * u, fill=fill, outline=ol, width=ow)
    # cuff
    rr(72, 34, 96, 72, 5, (215, 30, 35, 255))
    # palm
    rr(40, 32, 78, 74, 14, WHITE)
    # folded fingers
    for i, y in enumerate((46, 56, 64)):
        rr(30, y, 52, y + 10, 5, WHITE)
    # index finger pointing left
    rr(4, 34, 56, 46, 6, WHITE)
    # thumb
    rr(44, 24, 62, 38, 7, WHITE)
    # cuff stripes
    d.line([(78 * u, 40 * u), (78 * u, 66 * u)], fill=ol, width=int(1.2 * u))
    return im.resize((size, size), Image.LANCZOS)


def coin(d=110):
    ss = 4
    s = d * ss
    im = Image.new('RGBA', (s, s), (0, 0, 0, 0))
    dr = ImageDraw.Draw(im)
    dr.ellipse([0, 0, s - 1, s - 1], fill=(176, 128, 20, 255))
    dr.ellipse([s * .07, s * .07, s * .93, s * .93], fill=(242, 190, 45, 255))
    dr.ellipse([s * .15, s * .15, s * .85, s * .85], outline=(196, 145, 25, 255), width=int(s * .03))
    f = ImageFont.truetype(F + 'Rubik-700.ttf', int(s * .5))
    dr.text((s * .53, s / 2), 'Р', font=f, fill=(160, 110, 10, 255), anchor='mm')
    dr.rectangle([s * .30, s * .60, s * .60, s * .66], fill=(160, 110, 10, 255))
    dr.ellipse([s * .22, s * .16, s * .42, s * .28], fill=(255, 235, 150, 140))
    return im.resize((d, d), Image.LANCZOS)


def arrow(length, col=YEL, width=26, head=60, left=False):
    ss = 3
    L, Hh = length * ss, head * 2 * ss
    im = Image.new('RGBA', (L, Hh), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    cy = Hh / 2
    d.rounded_rectangle([0, cy - width * ss / 2, L - head * ss * 0.9, cy + width * ss / 2], width * ss / 2, fill=col)
    d.polygon([(L - head * ss * 1.3, cy - head * ss * 0.8), (L, cy), (L - head * ss * 1.3, cy + head * ss * 0.8)], fill=col)
    im = im.resize((length, head * 2), Image.LANCZOS)
    return ImageOps.mirror(im) if left else im


def column_icon(s=240, col=WHITE):
    ss = 3; S = s * ss; u = S / 100
    im = Image.new('RGBA', (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.polygon([(10 * u, 24 * u), (50 * u, 6 * u), (90 * u, 24 * u)], fill=col)
    d.rectangle([12 * u, 26 * u, 88 * u, 32 * u], fill=col)
    for x in (18, 36, 54, 72):
        d.rectangle([(x + 1) * u, 35 * u, (x + 9) * u, 82 * u], fill=col)
    d.rectangle([10 * u, 85 * u, 90 * u, 91 * u], fill=col)
    d.rectangle([6 * u, 93 * u, 94 * u, 98 * u], fill=col)
    return im.resize((s, s), Image.LANCZOS)


def hourglass_icon(s=240):
    ss = 3; S = s * ss; u = S / 100
    im = Image.new('RGBA', (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    g = (212, 160, 23, 255)
    d.ellipse([2 * u, 2 * u, 98 * u, 98 * u], outline=g, width=int(6 * u))
    d.rectangle([30 * u, 18 * u, 70 * u, 23 * u], fill=g)
    d.rectangle([30 * u, 77 * u, 70 * u, 82 * u], fill=g)
    glass = (235, 235, 240, 255)
    d.polygon([(34 * u, 24 * u), (66 * u, 24 * u), (53 * u, 50 * u), (66 * u, 76 * u), (34 * u, 76 * u), (47 * u, 50 * u)], fill=glass)
    sand = (240, 190, 40, 255)
    d.polygon([(40 * u, 32 * u), (60 * u, 32 * u), (51 * u, 47 * u), (49 * u, 47 * u)], fill=sand)
    d.polygon([(50 * u, 58 * u), (63 * u, 75 * u), (37 * u, 75 * u)], fill=sand)
    d.line([(50 * u, 49 * u), (50 * u, 70 * u)], fill=sand, width=int(1.5 * u))
    return im.resize((s, s), Image.LANCZOS)


def kettlebell_icon(s=240, col=WHITE):
    ss = 3; S = s * ss; u = S / 100
    im = Image.new('RGBA', (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.ellipse([12 * u, 30 * u, 88 * u, 98 * u], fill=col)
    d.rounded_rectangle([26 * u, 6 * u, 74 * u, 44 * u], 18 * u, outline=col, width=int(9 * u))
    f = ImageFont.truetype(F + 'Rubik-700.ttf', int(20 * u))
    d.text((50 * u, 68 * u), '100', font=f, fill=(0, 0, 0, 255), anchor='mm')
    return im.resize((s, s), Image.LANCZOS)


# ---------- competitor logo ----------
def competitor_logo(s=400):
    ss = 3; S = s * ss; u = S / 100
    im = Image.new('RGBA', (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    lw = int(2.2 * u)
    # shield
    d.polygon([(50 * u, 8 * u), (72 * u, 15 * u), (70 * u, 40 * u), (50 * u, 55 * u), (30 * u, 40 * u), (28 * u, 15 * u)],
              outline=NAVY, width=lw)
    # scales inside
    d.line([(50 * u, 18 * u), (50 * u, 44 * u)], fill=NAVY, width=lw)
    d.line([(38 * u, 23 * u), (62 * u, 23 * u)], fill=NAVY, width=lw)
    for x in (38, 62):
        d.line([(x * u, 23 * u), ((x - 5) * u, 33 * u)], fill=NAVY, width=int(1.2 * u))
        d.line([(x * u, 23 * u), ((x + 5) * u, 33 * u)], fill=NAVY, width=int(1.2 * u))
        d.chord([(x - 6) * u, 29 * u, (x + 6) * u, 38 * u], 0, 180, fill=NAVY)
    d.line([(44 * u, 45 * u), (56 * u, 45 * u)], fill=NAVY, width=lw)
    f1 = ImageFont.truetype(F + 'Rubik-600.ttf', int(12 * u))
    f2 = ImageFont.truetype(F + 'Rubik-400.ttf', int(7 * u))
    d.text((50 * u, 70 * u), 'КОРОЛЁВ', font=f1, fill=NAVY, anchor='mm')
    d.line([(30 * u, 79 * u), (70 * u, 79 * u)], fill=NAVY, width=int(0.8 * u))
    d.text((50 * u, 87 * u), 'ЮРИСТ  ·  ЗАЩИТА', font=f2, fill=NAVY, anchor='mm')
    return im.resize((s, s), Image.LANCZOS)


# ---------- retro businessman (b/w) ----------
def businessman(w=894, h=683, seed=3):
    ss = 2
    S = (w * ss, h * ss)
    im = Image.new('RGB', S, (0, 0, 0))
    # radial studio backdrop
    yy, xx = np.mgrid[0:S[1], 0:S[0]]
    r = np.sqrt(((xx - S[0] * 0.5) / S[0]) ** 2 + ((yy - S[1] * 0.42) / S[1]) ** 2)
    bg = np.clip(185 - r * 260, 40, 200).astype(np.uint8)
    im = Image.fromarray(np.stack([bg] * 3, -1))
    d = ImageDraw.Draw(im)
    u = S[1] / 100
    cx = S[0] * 0.5
    suit = (38, 38, 40)
    # shoulders / suit
    d.rounded_rectangle([cx - 30 * u, 44 * u, cx + 30 * u, 120 * u], 12 * u, fill=suit)
    # shirt V + tie
    d.polygon([(cx - 8 * u, 44 * u), (cx + 8 * u, 44 * u), (cx, 66 * u)], fill=(235, 235, 235))
    d.polygon([(cx - 2.2 * u, 47 * u), (cx + 2.2 * u, 47 * u), (cx + 3 * u, 64 * u), (cx, 68 * u), (cx - 3 * u, 64 * u)], fill=(15, 15, 15))
    # lapels
    d.polygon([(cx - 8 * u, 44 * u), (cx - 16 * u, 46 * u), (cx - 3 * u, 74 * u)], fill=(58, 58, 62))
    d.polygon([(cx + 8 * u, 44 * u), (cx + 16 * u, 46 * u), (cx + 3 * u, 74 * u)], fill=(58, 58, 62))
    # neck + head
    d.rectangle([cx - 5 * u, 36 * u, cx + 5 * u, 46 * u], fill=(170, 170, 170))
    d.ellipse([cx - 10 * u, 14 * u, cx + 10 * u, 40 * u], fill=(190, 190, 190))
    d.ellipse([cx - 11.5 * u, 24 * u, cx - 8.5 * u, 31 * u], fill=(170, 170, 170))
    d.ellipse([cx + 8.5 * u, 24 * u, cx + 11.5 * u, 31 * u], fill=(170, 170, 170))
    # face hints
    d.line([(cx - 5 * u, 25 * u), (cx - 2 * u, 25 * u)], fill=(60, 60, 60), width=int(0.8 * u))
    d.line([(cx + 2 * u, 25 * u), (cx + 5 * u, 25 * u)], fill=(60, 60, 60), width=int(0.8 * u))
    d.line([(cx - 3 * u, 33 * u), (cx + 3 * u, 33 * u)], fill=(90, 90, 90), width=int(0.7 * u))
    # fedora
    d.ellipse([cx - 19 * u, 15 * u, cx + 19 * u, 21 * u], fill=(25, 25, 27))
    d.rounded_rectangle([cx - 11 * u, 4 * u, cx + 11 * u, 18 * u], 4 * u, fill=(25, 25, 27))
    d.rectangle([cx - 11 * u, 13 * u, cx + 11 * u, 16 * u], fill=(70, 70, 70))
    # arm + briefcase (right side of image)
    d.rounded_rectangle([cx + 22 * u, 50 * u, cx + 32 * u, 86 * u], 5 * u, fill=suit)
    d.rounded_rectangle([cx + 16 * u, 84 * u, cx + 50 * u, 110 * u], 2 * u, fill=(55, 42, 32))
    d.rounded_rectangle([cx + 28 * u, 79 * u, cx + 38 * u, 86 * u], 2 * u, outline=(30, 25, 20), width=int(1.3 * u))
    d.rectangle([cx + 16 * u, 90 * u, cx + 50 * u, 91.5 * u], fill=(90, 70, 50))
    # pocket square
    d.polygon([(cx - 22 * u, 58 * u), (cx - 15 * u, 58 * u), (cx - 18 * u, 54 * u)], fill=(225, 225, 225))
    im = im.resize((w, h), Image.LANCZOS).convert('L')
    a = np.asarray(im).astype(np.float32)
    rng = np.random.default_rng(seed)
    a += rng.normal(0, 9, a.shape)
    yy, xx = np.mgrid[0:h, 0:w]
    vig = 1 - 0.55 * (((xx - w / 2) / (w / 2)) ** 2 + ((yy - h / 2) / (h / 2)) ** 2) / 2
    a = np.clip(a * vig, 0, 255).astype(np.uint8)
    return Image.fromarray(a).convert('RGBA')


# ---------- lemon marks ----------
def lemon_shape(w, h, col, angle=-18):
    ss = 4
    im = Image.new('RGBA', (w * ss * 2, h * ss * 2), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    cx, cy = w * ss, h * ss
    d.ellipse([cx - w * ss * .5, cy - h * ss * .5, cx + w * ss * .5, cy + h * ss * .5], fill=col)
    # pointed tips
    d.polygon([(cx + w * ss * .42, cy - h * ss * .22), (cx + w * ss * .62, cy - h * ss * .02), (cx + w * ss * .42, cy + h * ss * .2)], fill=col)
    d.polygon([(cx - w * ss * .42, cy - h * ss * .2), (cx - w * ss * .6, cy + h * ss * .04), (cx - w * ss * .42, cy + h * ss * .22)], fill=col)
    im = im.rotate(-angle, resample=Image.BICUBIC)
    bb = im.getbbox()
    im = im.crop(bb)
    return im.resize((max(1, im.width // ss), max(1, im.height // ss)), Image.LANCZOS)


def lemon_ring(d=188):
    im = Image.new('RGBA', (d, d), (0, 0, 0, 0))
    ss = 4
    big = Image.new('RGBA', (d * ss, d * ss), (0, 0, 0, 0))
    ImageDraw.Draw(big).ellipse([0, 0, d * ss - 1, d * ss - 1], fill=(253, 195, 1, 255))
    big = big.resize((d, d), Image.LANCZOS)
    im.alpha_composite(big)
    inner = lemon_shape(int(d * 0.58), int(d * 0.48), (30, 30, 30, 255), angle=-20)
    im.alpha_composite(inner, ((d - inner.width) // 2, (d - inner.height) // 2))
    return im


def lemonmedia_sign(width=940):
    """Yellow lemon + DARK wordmark with warm glow (like the neon wall sign)."""
    f = font('Rubik-500.ttf', 150)
    txt = 'lemonmedia'
    tw = int(f.getlength(txt))
    lem = lemon_shape(170, 140, (252, 200, 0, 255), angle=-12)
    gap = 20
    Wd = lem.width + gap + tw + 80
    Hd = 260
    base = Image.new('RGBA', (Wd, Hd), (0, 0, 0, 0))
    d = ImageDraw.Draw(base)
    d.text((40 + lem.width + gap, Hd / 2 + 8), txt, font=f, fill=(43, 43, 43, 255), anchor='lm')
    base.alpha_composite(lem, (40, (Hd - lem.height) // 2))
    a = base.getchannel('A')
    glow = Image.new('RGBA', base.size, (255, 196, 60, 0))
    ga = a.filter(ImageFilter.MaxFilter(15)).filter(ImageFilter.GaussianBlur(14)).point(lambda v: min(255, int(v * 1.25)))
    glow.putalpha(ga)
    glow2 = Image.new('RGBA', base.size, (255, 230, 150, 0))
    glow2.putalpha(a.filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(4)))
    out = Image.new('RGBA', base.size, (0, 0, 0, 0))
    out.alpha_composite(glow)
    out.alpha_composite(glow2)
    out.alpha_composite(base)
    sc = width / out.width
    return out.resize((width, int(out.height * sc)), Image.LANCZOS)


# ---------- restaurant facade ----------
def restaurant_bg(logo):
    ss = 1
    im = Image.new('RGBA', (W, H), (0, 0, 0, 255))
    a = np.zeros((H, W, 3), np.float32)
    t = np.linspace(0, 1, H)[:, None]
    top = np.array([12, 10, 40]); mid = np.array([48, 28, 70])
    a[:] = (top * (1 - t) + mid * t)[:, None, :].reshape(H, 1, 3)
    im = Image.fromarray(a.astype(np.uint8)).convert('RGBA')
    d = ImageDraw.Draw(im)
    rng = random.Random(4)
    for _ in range(70):
        x, y = rng.randint(0, W), rng.randint(0, 300)
        r = rng.choice([1, 1, 2])
        d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 255, 255, rng.randint(80, 200)))
    # facade
    fac_top = 300
    d.rectangle([0, fac_top, W, 1760], fill=(112, 62, 38, 255))
    # brick hint lines
    for y in range(fac_top + 140, 1760, 44):
        d.line([(0, y), (W, y)], fill=(98, 52, 32, 255), width=3)
        off = 0 if (y // 44) % 2 else 45
        for x in range(off, W, 90):
            d.line([(x, y), (x, y + 44)], fill=(98, 52, 32, 255), width=3)
    # tile band (turquoise/white lozenges)
    d.rectangle([0, fac_top, W, fac_top + 110], fill=(20, 104, 124, 255))
    for x in range(-30, W + 60, 60):
        d.polygon([(x, fac_top + 55), (x + 30, fac_top + 15), (x + 60, fac_top + 55), (x + 30, fac_top + 95)], fill=(236, 226, 196, 255))
        d.polygon([(x + 18, fac_top + 55), (x + 30, fac_top + 38), (x + 42, fac_top + 55), (x + 30, fac_top + 72)], fill=(200, 60, 40, 255))
    d.rectangle([0, fac_top + 110, W, fac_top + 124], fill=(190, 140, 60, 255))
    # arch doorway (warm light)
    ax0, ax1, ay_top, ay_bot = 300, 780, 1260, 1760
    arch = Image.new('L', (W, H), 0)
    ad = ImageDraw.Draw(arch)
    ad.rectangle([ax0, ay_top + 160, ax1, ay_bot], fill=255)
    ad.pieslice([ax0, ay_top, ax1 + 0, ay_top + 480], 180, 360, fill=255)
    ad.polygon([(ax0 + 90, ay_top + 60), ((ax0 + ax1) / 2, ay_top - 70), (ax1 - 90, ay_top + 60)], fill=255)
    frame = arch.filter(ImageFilter.MaxFilter(41))
    tile = Image.new('RGBA', (W, H), (20, 104, 124, 255))
    im.paste(tile, (0, 0), frame)
    grad = np.zeros((H, W, 3), np.float32)
    tt = np.clip((np.arange(H)[:, None] - ay_top) / (ay_bot - ay_top), 0, 1)
    c0 = np.array([255, 214, 120]); c1 = np.array([230, 120, 30])
    grad[:] = (c0 * (1 - tt) + c1 * tt).reshape(H, 1, 3)
    im.paste(Image.fromarray(grad.astype(np.uint8)).convert('RGBA'), (0, 0), arch)
    # interior silhouettes: lattice
    d = ImageDraw.Draw(im)
    for x in range(ax0 + 60, ax1, 70):
        d.line([(x, ay_top + 250), (x, ay_bot)], fill=(200, 95, 25, 120), width=4)
    # warm light spill on ground
    d.rectangle([0, 1760, W, H], fill=(38, 24, 18, 255))
    spill = Image.new('L', (W, H), 0)
    ImageDraw.Draw(spill).ellipse([200, 1700, 880, 1980], fill=150)
    spill = spill.filter(ImageFilter.GaussianBlur(60))
    im.paste(Image.new('RGBA', (W, H), (255, 170, 60, 255)), (0, 0), spill)
    # logo sign with glow + wall plate
    glow = Image.new('L', (W, H), 0)
    ImageDraw.Draw(glow).ellipse([540 - 330, 760 - 330, 540 + 330, 760 + 330], fill=200)
    glow = glow.filter(ImageFilter.GaussianBlur(70))
    im.paste(Image.new('RGBA', (W, H), (255, 190, 80, 255)), (0, 0), glow)
    lg = logo.resize((560, 560), Image.LANCZOS)
    im.alpha_composite(lg, (540 - 280, 760 - 280))
    # string lights
    d = ImageDraw.Draw(im)
    pts = [(x, 470 + 60 * math.sin(math.pi * x / W)) for x in range(0, W + 1, 12)]
    d.line(pts, fill=(40, 30, 20, 255), width=3)
    return im


def lantern(h=180):
    ss = 3; S = (int(h * 0.6) * ss, h * ss); u = S[1] / 100
    im = Image.new('RGBA', S, (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    cx = S[0] / 2
    d.line([(cx, 0), (cx, 14 * u)], fill=(30, 30, 30, 255), width=int(1.5 * u))
    d.polygon([(cx - 14 * u, 22 * u), (cx + 14 * u, 22 * u), (cx + 6 * u, 14 * u), (cx - 6 * u, 14 * u)], fill=(150, 110, 40, 255))
    d.rounded_rectangle([cx - 18 * u, 22 * u, cx + 18 * u, 82 * u], 10 * u, fill=(255, 190, 70, 255), outline=(150, 110, 40, 255), width=int(3 * u))
    for x in (-8, 0, 8):
        d.line([(cx + x * u, 24 * u), (cx + x * u, 80 * u)], fill=(200, 120, 30, 255), width=int(1.3 * u))
    d.polygon([(cx - 14 * u, 82 * u), (cx + 14 * u, 82 * u), (cx, 96 * u)], fill=(150, 110, 40, 255))
    return im.resize((S[0] // ss, S[1] // ss), Image.LANCZOS)


# ---------- plov kazan ----------
def plov_bg():
    rng = np.random.default_rng(7)
    a = np.zeros((H, W, 3), np.float32)
    yy, xx = np.mgrid[0:H, 0:W]
    wood = 60 + 18 * np.sin(yy / 23.0 + np.sin(xx / 150.0) * 2) + rng.normal(0, 4, (H, W))
    a[..., 0] = wood * 1.0; a[..., 1] = wood * 0.62; a[..., 2] = wood * 0.38
    r = np.sqrt(((xx - W / 2) / W) ** 2 + ((yy - 820) / H) ** 2)
    a *= np.clip(1.25 - r * 1.1, 0.3, 1)[..., None]
    im = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).convert('RGBA')
    d = ImageDraw.Draw(im)
    cx, cy, R = 540, 800, 500
    # kazan shadow + body + rim
    sh = Image.new('L', (W, H), 0)
    ImageDraw.Draw(sh).ellipse([cx - R - 10, cy - R + 30, cx + R + 30, cy + R + 50], fill=200)
    im.paste(Image.new('RGBA', (W, H), (0, 0, 0, 255)), (0, 0), sh.filter(ImageFilter.GaussianBlur(30)))
    d.ellipse([cx - R, cy - R, cx + R, cy + R], fill=(22, 22, 24, 255))
    d.ellipse([cx - R + 14, cy - R + 14, cx + R - 14, cy + R - 14], outline=(80, 80, 86, 255), width=6)
    # handles
    for s in (-1, 1):
        d.rounded_rectangle([cx + s * (R - 10) - 40, cy - 40, cx + s * (R - 10) + 40, cy + 40], 20, fill=(30, 30, 32, 255))
    # rice bed
    Rr = R - 55
    d.ellipse([cx - Rr, cy - Rr, cx + Rr, cy + Rr], fill=(214, 150, 60, 255))
    ss = 2
    big = Image.new('RGBA', (W * ss, H * ss), (0, 0, 0, 0))
    bd = ImageDraw.Draw(big)
    pal = [(236, 186, 96), (244, 204, 130), (222, 160, 70), (250, 218, 150), (205, 140, 55)]
    for _ in range(9000):
        rr = Rr * math.sqrt(rng.random()); th = rng.random() * 2 * math.pi
        x, y = cx + rr * math.cos(th), cy + rr * math.sin(th)
        ang = rng.random() * math.pi
        L = 9 + rng.random() * 5
        c = pal[rng.integers(len(pal))]
        bd.line([((x - L / 2 * math.cos(ang)) * ss, (y - L / 2 * math.sin(ang)) * ss),
                 ((x + L / 2 * math.cos(ang)) * ss, (y + L / 2 * math.sin(ang)) * ss)], fill=c + (255,), width=5 * ss)
    # carrot strips
    for _ in range(260):
        rr = Rr * 0.95 * math.sqrt(rng.random()); th = rng.random() * 2 * math.pi
        x, y = cx + rr * math.cos(th), cy + rr * math.sin(th)
        ang = rng.random() * math.pi; L = 26 + rng.random() * 20
        bd.line([((x - L / 2 * math.cos(ang)) * ss, (y - L / 2 * math.sin(ang)) * ss),
                 ((x + L / 2 * math.cos(ang)) * ss, (y + L / 2 * math.sin(ang)) * ss)], fill=(232, 112, 30, 255), width=7 * ss)
    # chickpeas
    for _ in range(40):
        rr = Rr * 0.9 * math.sqrt(rng.random()); th = rng.random() * 2 * math.pi
        x, y = cx + rr * math.cos(th), cy + rr * math.sin(th)
        bd.ellipse([(x - 9) * ss, (y - 9) * ss, (x + 9) * ss, (y + 9) * ss], fill=(226, 196, 130, 255), outline=(180, 140, 80, 255), width=2 * ss)
    # meat chunks (centre)
    for i in range(11):
        th = i * 2 * math.pi / 11 + 0.3
        rad = 165 + 25 * (i % 2)
        x, y = cx + rad * math.cos(th), cy + rad * math.sin(th)
        pts = [(x + 72 * math.cos(k * 0.7 + i) * (0.7 + 0.3 * rng.random()), y + 58 * math.sin(k * 0.7 + i) * (0.7 + 0.3 * rng.random())) for k in range(9)]
        bd.polygon([(px * ss, py * ss) for px, py in pts], fill=(104, 54, 28, 255))
        pts2 = [(px * 0.6 + x * 0.4 - 10, py * 0.6 + y * 0.4 - 12) for px, py in pts]
        bd.polygon([(px * ss, py * ss) for px, py in pts2], fill=(150, 84, 44, 255))
        bd.ellipse([(x - 22) * ss, (y - 26) * ss, (x + 2) * ss, (y - 14) * ss], fill=(196, 130, 80, 255))
    # garlic head
    for k in range(8):
        th = k * math.pi / 4
        x, y = cx + 22 * math.cos(th), cy + 22 * math.sin(th)
        bd.ellipse([(x - 26) * ss, (y - 26) * ss, (x + 26) * ss, (y + 26) * ss], fill=(238, 224, 200, 255), outline=(200, 180, 150, 255), width=2 * ss)
    bd.ellipse([(cx - 20) * ss, (cy - 20) * ss, (cx + 20) * ss, (cy + 20) * ss], fill=(245, 234, 214, 255))
    big = big.resize((W, H), Image.LANCZOS)
    im.alpha_composite(big)
    # glossy highlight
    hl = Image.new('L', (W, H), 0)
    ImageDraw.Draw(hl).ellipse([cx - 300, cy - 380, cx + 120, cy - 120], fill=60)
    im.paste(Image.new('RGBA', (W, H), (255, 240, 200, 255)), (0, 0), hl.filter(ImageFilter.GaussianBlur(60)))
    return im


def steam_sprite(s=420):
    im = Image.new('L', (s, s), 0)
    ImageDraw.Draw(im).ellipse([s * .2, s * .2, s * .8, s * .8], fill=255)
    im = im.filter(ImageFilter.GaussianBlur(s * .12))
    out = Image.new('RGBA', (s, s), (255, 255, 255, 0))
    out.putalpha(im)
    return out


def red_path(points, frac, width=12, col=MARK):
    """Return list of points for progressive drawing."""
    n = max(2, int(len(points) * max(0.0, min(1.0, frac))))
    return points[:n]


def hand_ellipse(cx, cy, rx, ry, rot=-0.15, turns=1.08, n=160, seed=1):
    rng = random.Random(seed)
    pts = []
    for i in range(n):
        t = turns * 2 * math.pi * i / (n - 1) - 2.0
        wob = 1 + 0.025 * math.sin(3 * t + 0.5) + 0.02 * (i / n)
        x = rx * wob * math.cos(t); y = ry * wob * math.sin(t)
        xr = x * math.cos(rot) - y * math.sin(rot); yr = x * math.sin(rot) + y * math.cos(rot)
        pts.append((cx + xr, cy + yr))
    return pts


def hand_arc(cx, cy, r, a0, a1, n=90):
    pts = []
    for i in range(n):
        a = math.radians(a0 + (a1 - a0) * i / (n - 1))
        rr = r * (1 + 0.02 * math.sin(i / 7))
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return pts
