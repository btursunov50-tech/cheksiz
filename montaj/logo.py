"""Fictional lawyer logo: round seal, heraldic falcon facing right, oriental ornament ring, arc text."""
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W = 2000
C = W // 2
GOLD = (201, 162, 39, 255)
GOLD_D = (150, 115, 20, 255)
BORD = (90, 26, 26, 255)
F = 'fonts/'


def ring(d, r, w, col):
    d.ellipse([C - r, C - r, C + r, C + r], outline=col, width=w)


def disk(d, r, col):
    d.ellipse([C - r, C - r, C + r, C + r], fill=col)


def polar(r, a):
    return C + r * math.cos(a), C + r * math.sin(a)


def rot(pts, a, cx=0, cy=0):
    ca, sa = math.cos(a), math.sin(a)
    return [(cx + x * ca - y * sa, cy + x * sa + y * ca) for x, y in pts]


def ornament(d, r0, r1, n=28):
    """Central-Asian style band: lozenges + paired curls + dots."""
    rm = (r0 + r1) / 2
    h = (r1 - r0) / 2
    for i in range(n):
        a = 2 * math.pi * i / n
        # lozenge (radial diamond)
        pts = [(0, -h * 0.85), (h * 0.34, 0), (0, h * 0.85), (-h * 0.34, 0)]
        pts = [(y, x) for x, y in pts]  # radial orientation
        pts = rot(pts, a)
        pts = [(C + rm * math.cos(a) + x, C + rm * math.sin(a) + y) for x, y in pts]
        d.polygon(pts, fill=GOLD)
        # small inner diamond cut
        pts2 = [(0, -h * 0.35), (h * 0.13, 0), (0, h * 0.35), (-h * 0.13, 0)]
        pts2 = rot([(y, x) for x, y in pts2], a)
        pts2 = [(C + rm * math.cos(a) + x, C + rm * math.sin(a) + y) for x, y in pts2]
        d.polygon(pts2, fill=BORD)
        # curls between lozenges (two arcs = ram-horn motif)
        b = a + math.pi / n
        cx, cy = polar(rm, b)
        rr = h * 0.42
        for s in (-1, 1):
            ox, oy = polar(rm + s * h * 0.30, b)
            box = [ox - rr, oy - rr, ox + rr, oy + rr]
            deg = math.degrees(b)
            if s < 0:
                d.arc(box, deg - 70, deg + 70, fill=GOLD, width=14)
            else:
                d.arc(box, deg + 110, deg + 250, fill=GOLD, width=14)
        dx, dy = polar(rm, b)
        d.ellipse([dx - 9, dy - 9, dx + 9, dy + 9], fill=GOLD)


def arc_text(img, text, r, font, col, center_deg=-90, spacing=1.0, bottom=False):
    d = ImageDraw.Draw(img)
    widths = [font.getlength(ch) * spacing for ch in text]
    total = sum(widths)
    ang_total = total / r
    a = math.radians(center_deg) - (ang_total / 2 if not bottom else -ang_total / 2)
    for ch, w in zip(text, widths):
        step = w / r
        mid = a + (step / 2 if not bottom else -step / 2)
        sz = int(font.size * 1.6)
        tile = Image.new('RGBA', (sz, sz), (0, 0, 0, 0))
        ImageDraw.Draw(tile).text((sz / 2, sz / 2), ch, font=font, fill=col, anchor='mm')
        deg = math.degrees(mid) + 90 if not bottom else math.degrees(mid) - 90
        tile = tile.rotate(-deg, resample=Image.BICUBIC)
        x, y = polar(r, mid)
        img.alpha_composite(tile, (int(x - sz / 2), int(y - sz / 2)))
        a += step if not bottom else -step


def falcon(size=1000, col=GOLD):
    """Heraldic falcon, wings displayed, head in profile with beak to the RIGHT."""
    s = size / 100.0
    k = 4
    im = Image.new('RGBA', (size * k, size * k), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    P = lambda pts: [(x * s * k, y * s * k) for x, y in pts]
    cut = (0, 0, 0, 0)
    for side in (-1, 1):
        m = lambda pts: [(50 + side * (x - 50), y) for x, y in pts]
        # wing silhouette: rising top edge, serrated feather tips at the bottom/outer edge
        wing = [(46, 44), (40, 34), (30, 25), (18, 17), (6, 12), (3, 15),
                (8, 19), (2, 22), (9, 26), (3, 30), (11, 33), (6, 37), (15, 39),
                (11, 44), (21, 44), (19, 49), (29, 48), (30, 53), (38, 50), (44, 52)]
        d.polygon(P(m(wing)), fill=col)
        # feather separation lines
        for (x0, y0), (x1, y1) in [((40, 44), (9, 19)), ((40, 46), (10, 27)), ((41, 48), (12, 35)),
                                   ((42, 49), (17, 42)), ((43, 50), (26, 47))]:
            d.line(P(m([(x0, y0), (x1, y1)])), fill=cut, width=int(1.1 * s * k))
        # talons
        d.line(P(m([(46, 66), (40, 74)])), fill=col, width=int(3.2 * s * k))
        for t in (-4, 0, 4):
            d.line(P(m([(40, 74), (40 + t * 0.8 - 2, 79)])), fill=col, width=int(1.6 * s * k))
    # body
    d.ellipse(P([(40, 36), (60, 72)]), fill=col)
    # tail fan with notches
    d.polygon(P([(45, 66), (55, 66), (62, 88), (58, 86), (55, 90), (50, 87), (45, 90), (42, 86), (38, 88)]), fill=col)
    # neck
    d.polygon(P([(44, 42), (47, 30), (53, 26), (59, 28), (58, 38), (55, 44)]), fill=col)
    # head (profile, facing right)
    d.ellipse(P([(46, 14), (60, 28)]), fill=col)
    # hooked beak
    d.polygon(P([(58, 17), (66, 18), (70, 22), (69, 26), (66, 23), (59, 24)]), fill=col)
    # eye + brow cut
    d.ellipse(P([(54.2, 18.2), (57.2, 21.2)]), fill=cut)
    d.line(P([(59, 24), (66, 23)]), fill=cut, width=int(0.8 * s * k))
    # chest feather scallops
    for i in range(4):
        y = 44 + i * 6
        d.arc(P([(44, y - 2), (56, y + 6)]), 20, 160, fill=cut, width=int(1.1 * s * k))
    return im.resize((size, size), Image.LANCZOS)


def build(path='assets/logo.png'):
    img = Image.new('RGBA', (W, W), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    R = W * 0.49
    disk(d, R, BORD)
    ring(d, int(R * 0.985), int(W * 0.018), GOLD)
    ring(d, int(R * 0.935), int(W * 0.006), GOLD)
    # text band 0.78-0.92
    font = ImageFont.truetype(F + 'CormorantSC-700.ttf', int(W * 0.085))
    arc_text(img, 'АДВОКАТ РАХИМОВ', R * 0.845, font, GOLD, center_deg=-90, spacing=1.08)
    # bottom of text band: stars / dots
    for k in range(-3, 4):
        a = math.radians(90 + k * 9)
        x, y = polar(R * 0.855, a)
        rr = W * 0.012 if k % 2 == 0 else W * 0.007
        d.ellipse([x - rr, y - rr, x + rr, y + rr], fill=GOLD)
    ring(d, int(R * 0.765), int(W * 0.007), GOLD)
    ornament(d, R * 0.60, R * 0.745, n=26)
    ring(d, int(R * 0.585), int(W * 0.007), GOLD)
    f = falcon(int(R * 1.05))
    img.alpha_composite(f, (int(C - f.width / 2), int(C - f.height / 2 + R * 0.02)))
    img.save(path)
    return img


def build_parts():
    """3 separate elements: seal contour, falcon, ornament ring."""
    R = W * 0.49
    seal = Image.new('RGBA', (W, W), (0, 0, 0, 0))
    d = ImageDraw.Draw(seal)
    ring(d, int(R * 0.985), int(W * 0.018), GOLD)
    ring(d, int(R * 0.935), int(W * 0.006), GOLD)
    font = ImageFont.truetype(F + 'CormorantSC-700.ttf', int(W * 0.085))
    arc_text(seal, 'АДВОКАТ РАХИМОВ', R * 0.845, font, GOLD, center_deg=-90, spacing=1.08)
    seal.save('assets/part_seal.png')
    orn = Image.new('RGBA', (W, W), (0, 0, 0, 0))
    d = ImageDraw.Draw(orn)
    disk(d, R * 0.77, BORD)
    disk(d, R * 0.58, (0, 0, 0, 0))
    ring(d, int(R * 0.765), int(W * 0.007), GOLD)
    ornament(d, R * 0.60, R * 0.745, n=26)
    ring(d, int(R * 0.585), int(W * 0.007), GOLD)
    # clear center
    m = Image.new('L', (W, W), 255)
    ImageDraw.Draw(m).ellipse([C - R * 0.57, C - R * 0.57, C + R * 0.57, C + R * 0.57], fill=0)
    orn.putalpha(Image.composite(orn.getchannel('A'), Image.new('L', (W, W), 0), m))
    orn.save('assets/part_ornament.png')
    f = falcon(int(R * 1.05))
    fal = Image.new('RGBA', (W, W), (0, 0, 0, 0))
    fal.alpha_composite(f, (int(C - f.width / 2), int(C - f.height / 2)))
    fal.save('assets/part_falcon.png')


if __name__ == '__main__':
    import os
    os.makedirs('assets', exist_ok=True)
    im = build()
    build_parts()
    prev = Image.new('RGBA', (W, W), (209, 198, 175, 255))
    prev.alpha_composite(im)
    prev.convert('RGB').resize((700, 700), Image.LANCZOS).save('preview_logo.png')
