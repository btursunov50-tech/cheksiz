import math, subprocess, sys, json
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
from gfx import *
from timeline import *

FF = '/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2'
RAW = '/root/.claude/uploads/82f3e155-e852-5839-900d-40d183fb7b67/481f9a55-____________20MB.mp4'
PREVIEW = '--preview' in sys.argv
OUT = 'video_preview.mp4' if PREVIEW else 'video_noaudio.mp4'

# ---------------- assets ----------------
LOGO = Image.open('assets/logo2.png')
P_SEAL = Image.open('assets/p2_seal.png')
P_ORN = Image.open('assets/p2_orn.png')
P_FAL = Image.open('assets/p2_fal.png')
CLIENT = Image.open('../../images/4.webp').convert('RGBA')
UP = '/root/.claude/uploads/82f3e155-e852-5839-900d-40d183fb7b67/'
V1 = UP + '28370a0c-Entering_traditional_Uzbek_resta__20260929180400.mp4'
V2 = UP + 'eee52136-Entering_traditional_restaurant___20260929180304.mp4'


def load_clip(path, t0, dur, vf, size):
    p = subprocess.run([FF, '-v', 'error', '-ss', str(t0), '-t', str(dur), '-i', path, '-vf', vf + ',fps=25', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True)
    fs = size[0] * size[1] * 3
    return [Image.frombuffer('RGB', size, p.stdout[i:i + fs]).convert('RGBA') for i in range(0, len(p.stdout) - fs + 1, fs)]


REST_V = load_clip(V1, 0.0, 2.3, 'scale=1080:1920:flags=lanczos,unsharp=5:5:0.6', (1080, 1920))
MEAT_V = load_clip(V1, 7.8, 2.1, 'scale=1080:1920:flags=lanczos,unsharp=5:5:0.6', (1080, 1920))
INT_V = load_clip(V2, 0.2, 2.6, 'scale=-2:683:flags=lanczos,crop=894:683', (894, 683))
_cache = {}


def sized(img, key, s):
    s = max(4, int(round(s / 2) * 2))
    k = (key, s)
    if k not in _cache:
        if len(_cache) > 400:
            _cache.clear()
        _cache[k] = img.resize((s, s), Image.LANCZOS)
    return _cache[k]


def ease(t):
    t = max(0.0, min(1.0, t)); return 1 - (1 - t) ** 3


def ease_io(t):
    t = max(0.0, min(1.0, t)); return t * t * (3 - 2 * t)


def paste_c(canvas, img, cx, cy, scale=1.0, alpha=1.0, rot=0):
    if img is None or alpha <= 0.01:
        return
    if rot:
        img = img.rotate(rot, resample=Image.BICUBIC, expand=True)
    if abs(scale - 1) > 0.005:
        img = img.resize((max(1, int(img.width * scale)), max(1, int(img.height * scale))), Image.BICUBIC)
    if alpha < 0.999:
        img = img.copy(); img.putalpha(img.getchannel('A').point(lambda v: int(v * alpha)))
    canvas.alpha_composite(img, (int(cx - img.width / 2), int(cy - img.height / 2)))


def paste_tl(canvas, img, x, y, alpha=1.0):
    if alpha < 0.999:
        img = img.copy(); img.putalpha(img.getchannel('A').point(lambda v: int(v * alpha)))
    canvas.alpha_composite(img, (int(x), int(y)))


def pop(t, dur=0.24):
    """scale, alpha for a pop-in that started t seconds ago"""
    if t < 0:
        return 0, 0
    e = ease(t / dur)
    return 0.9 + 0.1 * e, min(1, t / 0.1)


EV = []
_fired = set()


def fire(key, name, when):
    if key not in _fired:
        _fired.add(key); EV.append((round(when, 3), name))


# plates cache
PL = {}


def P(text, kind='y', **kw):
    k = (text, kind, tuple(sorted(kw.items())))
    if k not in PL:
        PL[k] = plate(text, kind, **kw)
    return PL[k]


TB = {}


def TXT(lines, size=52, **kw):
    k = (tuple(lines), size, tuple(sorted(kw.items())))
    if k not in TB:
        TB[k] = text_block(list(lines), size=size, **kw)
    return TB[k]


Y_Y, Y_W = 1127 + 60, 1127 + 120 + 35 + 55  # plate centers


def plate_at(canvas, text, kind, cy, t, gt):
    s, a = pop(t)
    if a > 0:
        paste_c(canvas, P(text, kind), 540, cy, s, a)
        fire(('pl', text), 'pop', gt - t)


# ---------------- speaker helpers ----------------
def spk_full(fr, zoom=1.0, cx=560, cy=740):
    if zoom <= 1.001:
        return fr.copy()
    w, h = 1080 / zoom, 1920 / zoom
    x0 = min(max(cx - w / 2, 0), 1080 - w); y0 = min(max(cy - h / 2, 0), 1920 - h)
    return fr.resize((1080, 1920), Image.BICUBIC, box=(x0, y0, x0 + w, y0 + h))


def spk_panel(fr):
    return fr.crop((0, 250, 1080, 1272))


CARD_BG = None


def card_bg(w=894, h=683, c0=CREAM, c1=(196, 183, 160, 255)):
    a = np.zeros((h, w, 4), np.uint8)
    t = np.linspace(0, 1, h)[:, None]
    for i in range(4):
        a[..., i] = (c0[i] * (1 - t) + c1[i] * t).astype(np.uint8)
    return Image.fromarray(a, 'RGBA')


CARD_BG = card_bg()
CARD_MASK = rr_mask(894, 683, 45)
CX0, CY0 = 93, 10  # card origin


def split_base(fr):
    cv = Image.new('RGBA', (W, H), (0, 0, 0, 255))
    cv.paste(spk_panel(fr), (0, 898))
    return cv


def put_card(cv, content):
    c = content.copy(); c.putalpha(CARD_MASK)
    cv.alpha_composite(c, (CX0, CY0))


def split_text(cv, lines, t, gt, size=52):
    if t < 0:
        return
    img = TXT(lines, size=size)
    s, a = pop(t)
    cy = 812 if len(lines) == 1 else 812 + (len(lines) - 1) * 0
    paste_c(cv, img, 540, cy + (len(lines) - 1) * 12, s if t < 0.3 else 1, a)


# ---------------- precomputed ----------------
LANT = lantern(190)
STEAM = steam_sprite(420)
_cl = CLIENT.resize((1254, 1254))
BIZ = _cl.crop((0, 40, 1254, 998)).resize((894, 683), Image.LANCZOS)
GLOVE = glove(260)
COIN = coin(140)
CHECK = check_badge(90); CROSS = check_badge(90, cross=True)
CHK60 = check_badge(56); CRS60 = check_badge(56, cross=True)
ICONS = [column_icon(230), hourglass_icon(230), kettlebell_icon(230)]
COMP = competitor_logo(380)
SIGN = lemonmedia_sign(940)
LRING = lemon_ring(188)
VIGN = None


def make_vign():
    yy, xx = np.mgrid[0:H, 0:W]
    r = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H * 0.45) / (H / 2)) ** 2)
    a = np.clip((r - 0.55) * 1.3, 0, 0.75)
    im = np.zeros((H, W, 4), np.uint8); im[..., 3] = (a * 255).astype(np.uint8)
    return Image.fromarray(im, 'RGBA')


VIGN = make_vign()
_m = np.zeros((H, W), np.float32)
_m[:560] = 1.0
_m[560:760] = np.linspace(1, 0, 200)[:, None]
CTA_MASK = Image.fromarray((_m * 255).astype(np.uint8), 'L')


def tag(text, ok=True):
    f = font('Rubik-600.ttf', 40)
    tw = int(f.getlength(text))
    w, h = tw + 56 + 40 + 14, 76
    im = rrect(w, h, 38, WHITE)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([1, 1, w - 2, h - 2], 38, outline=GREEN if ok else RED, width=5)
    d.text((28, h / 2 + 2), text, font=f, fill=BLACK, anchor='lm')
    b = CHK60 if ok else CRS60
    im.alpha_composite(b, (w - 14 - 56, (h - 56) // 2))
    return im


TAG_R, TAG_Z = tag('РЕСТОРАН', True), tag('ЗАЩИТА', False)
LOGO_S420, _ = shadow(LOGO.resize((420, 420), Image.LANCZOS), blur=20, alpha=0.6, pad=40)


def card_small(content, w, h, bg=CREAM, r=36):
    c = rrect(w, h, r, bg)
    paste_c(c, content, w / 2, h / 2)
    return c


LCARD = card_small(sized(LOGO, 'logo', 360), 400, 400)
RCARD = card_small(COMP, 400, 400, bg=WHITE)
WCARD = rrect(858, 585, 45, WHITE)
paste_c(WCARD, sized(LOGO, 'logo', 500), 429, 292)
SCARD = rrect(606, 465, 40, CREAM)
paste_c(SCARD, sized(LOGO, 'logo', 420), 303, 232)
SCARD_S, SCARD_PAD = shadow(SCARD)
WCARD_S, WCARD_PAD = shadow(WCARD)

# falcon head / beak offsets relative to logo centre (fraction of logo size)
HEAD = (0.10, -0.20)
BEAK = (0.156, -0.194)


def draw_path(cv, pts, frac, width=12, col=MARK, off=(0, 0)):
    n = max(2, int(len(pts) * max(0.0, min(1.0, frac))))
    if frac <= 0:
        return
    ss = 2
    layer = Image.new('RGBA', (W * ss // 2, H * ss // 2), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    q = [((x + off[0]), (y + off[1])) for x, y in pts[:n]]
    d.line(q, fill=col, width=width, joint='curve')
    r = width / 2
    for x, y in (q[0], q[-1]):
        d.ellipse([x - r, y - r, x + r, y + r], fill=col)
    cv.alpha_composite(layer)


CIRCLE_PTS = hand_ellipse(CX0 + 447, CY0 + 341, 312, 300, rot=-0.12)
ULINE_PTS = hand_arc(CX0 + 447, CY0 + 341, 286, 32, 148)


# ---------------- scenes ----------------
def scene_of(k):
    return {0: 1, 1: 2, 2: 3, 3: 3, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8, 10: 9, 11: 10, 12: 10, 13: 10,
            14: 11, 15: 11, 16: 12, 17: 12, 18: 13, 19: 14, 20: 15, 21: 15, 22: 16, 23: 17}[k]


FIRST = {}
for k in range(len(CF)):
    FIRST.setdefault(scene_of(k), k)


def rel(k, f):
    """seconds since start of clip k at output frame f"""
    return (f - O[k]) / FPS


def render(fr, k, f):
    sc = scene_of(k)
    gt = f / FPS
    st = (f - O[FIRST[sc]]) / FPS
    lt = rel(k, f)
    if f == O[FIRST[sc]] and sc not in (1,):
        fire(('sc', sc), 'whoosh', gt)

    if sc == 1:  # A1: speaker + yellow plate + small logo card
        cv = spk_full(fr, 1.0 + 0.05 * st / 1.48).convert('RGBA')
        plate_at(cv, 'Это не логотип адвоката', 'y', Y_Y, st + 0.12, gt)
        e = ease(st / 0.24 + 0.2)
        y = 1303 + (1 - e) * 330
        paste_tl(cv, SCARD_S, 237 - SCARD_PAD, y - SCARD_PAD)
        return cv

    if sc in (2, 3):  # split with logo card
        cv = split_base(fr)
        content = CARD_BG.copy()
        z = 600 * (1 + 0.06 * min(st, 1.5) / 1.5) if sc == 2 else 600
        paste_c(content, sized(LOGO, 'logo', z), 447, 341)
        put_card(cv, content)
        if sc == 2:
            split_text(cv, ['это герб, которого нет'], st, gt)
        else:
            t2, t3, t4 = rel(2, f) - 0.04, rel(3, f), rel(4, f)
            if t2 >= 0:
                draw_path(cv, CIRCLE_PTS, t2 / 0.36, width=13)
                fire('circle', 'scribble', gt - t2)
            if t3 >= 0:
                e = ease(t3 / 0.22)
                bob = 8 * math.sin(max(0, t3 - 0.22) * 9) * math.exp(-max(0, t3 - 0.22) * 3)
                tipx, tipy = CX0 + 447 + 36 + (1 - e) * 450 + bob, CY0 + 341 - 52 + (1 - e) * 120
                paste_tl(cv, GLOVE, tipx - 10, tipy - 104)
                fire('glove', 'click', gt - t3 + 0.2)
            if t4 >= 0:
                draw_path(cv, ULINE_PTS, t4 / 0.3, width=12)
                fire('uline', 'scribble', gt - t4)
            words = 'Печать,' if k == 2 else ('Печать, сокол,' if k == 3 else 'Печать, сокол, орнамент')
            split_text(cv, [words], st, gt)
        return cv

    if sc == 4:  # black: 3 parts separate + checks
        cv = Image.new('RGBA', (W, H), (0, 0, 0, 255))
        e = ease_io(st / 0.45)
        xs = [190, 540, 890]
        s = 560 + (300 - 560) * e
        for i, part in enumerate((P_SEAL, P_FAL, P_ORN)):
            x = 540 + (xs[i] - 540) * e
            m = 1 + 0.35 * e if i == 1 else 1
            paste_c(cv, sized(part, ('p', i), s * m), x, 800)
        for i in range(3):
            tt = st - (0.6 + 0.4 * i)
            sc_, a = pop(tt)
            if a > 0:
                paste_c(cv, CHECK, xs[i], 1010, sc_, a)
                fire(('chk', i), 'pop', gt - tt)
        split = TXT(['Каждый элемент', 'по отдельности — нормально'], size=58)
        s_, a = pop(st)
        paste_c(cv, split, 540, 1230, s_, a)
        return cv

    if sc == 5:  # parts fly back together -> full logo
        cv = Image.new('RGBA', (W, H), (0, 0, 0, 255))
        e = ease_io(st / 0.4)
        xs = [190, 540, 890]
        if e < 1:
            s = 300 + (560 - 300) * e
            for i, part in enumerate((P_SEAL, P_FAL, P_ORN)):
                x = xs[i] + (540 - xs[i]) * e
                y = 800 + (760 - 800) * e
                m = 1 + 0.35 * (1 - e) if i == 1 else 1
                paste_c(cv, sized(part, ('p', i), s * m), x, y)
        else:
            paste_c(cv, sized(LOGO, 'logo', 560), 540, 760)
        plate_at(cv, 'Вместе — это вывеска', 'y', Y_Y, st, gt)
        return cv

    if sc == 6:  # restaurant (real footage) + our crest as the sign
        i = min(len(REST_V) - 1, f - O[7])
        cv = REST_V[i].copy()
        p = st / 2.12
        ls = 330 + 120 * p
        glow = Image.new('L', (W, H), 0)
        gy = 330 - 60 * p
        ImageDraw.Draw(glow).ellipse([540 - ls * 0.75, gy - ls * 0.75, 540 + ls * 0.75, gy + ls * 0.75], fill=170)
        cv.paste(Image.new('RGBA', (W, H), (255, 190, 90, 255)), (0, 0), glow.filter(ImageFilter.GaussianBlur(45)))
        paste_c(cv, sized(LOGO, 'logo', ls), 540, gy)
        plate_at(cv, 'Вместе — это вывеска', 'y', Y_Y, 1.0, gt)
        plate_at(cv, 'тематического ресторана', 'w', Y_W, st, gt)
        return cv

    if sc == 7:  # meat / shashlik footage
        i = min(len(MEAT_V) - 1, f - O[8])
        cv = MEAT_V[i].copy()
        plate_at(cv, 'где подают', 'w', Y_Y, st, gt)
        plate_at(cv, 'баранину по-восточному', 'y', Y_W, st - 0.5, gt)
        fire('ding', 'ding', O[8] / FPS + 1.2)
        return cv

    if sc == 8:  # A close-up, punch-in on "смешное"
        zoom = 1.12 if lt < 0.92 else 1.24
        if abs(lt - 0.92) < 0.021:
            fire('punch', 'pop', gt)
        cv = spk_full(fr, zoom, cy=700).convert('RGBA')
        plate_at(cv, 'И знаешь,', 'y', Y_Y, st, gt)
        plate_at(cv, 'что самое смешное?', 'w', Y_W, st - 0.42, gt)
        return cv

    if sc == 9:  # split: retro businessman
        cv = split_base(fr)
        z = 1 + 0.05 * st / 3.4
        content = BIZ.resize((894, 683), Image.BICUBIC, box=(447 - 447 / z, 341 - 341 / z, 447 + 447 / z, 341 + 342 / z))
        put_card(cv, content)
        lines = ['клиент с делом на миллион'] if st < 1.9 else ['клиент с делом на миллион', 'ищет это ощущение']
        img = TXT(tuple(lines), size=52)
        s_, a = pop(st) if st < 1.9 else pop(st - 1.9)
        paste_c(cv, img, 540, 812 + (len(lines) - 1) * 18, s_ if len(lines) == 1 else 1, 1)
        return cv

    if sc == 10:  # black: 3 icons on their words
        cv = Image.new('RGBA', (W, H), (0, 0, 0, 255))
        xs = [190, 540, 890]
        labels = ['серьёзность', 'старину', 'вес']
        for i in range(3):
            tt = (f - O[11 + i]) / FPS
            s_, a = pop(tt, 0.2)
            if a > 0:
                paste_c(cv, ICONS[i], xs[i], 820, s_, a)
                paste_c(cv, TXT((labels[i],), size=46), xs[i], 1010, 1, a)
                fire(('ic', i), 'pop', gt - tt)
        return cv

    if sc == 11:  # A2: top text + white card from bottom
        cv = spk_full(fr, 1.0).convert('RGBA')
        t14 = rel(14, f)
        e = ease(t14 / 0.3)
        paste_tl(cv, WCARD_S, 110 - WCARD_PAD, 1160 + (1 - e) * 800 - WCARD_PAD)
        l1 = TXT(('Ты дал ему это,',), size=64, shadow_a=0.6)
        s_, a = pop(t14)
        paste_c(cv, l1, 540, 230, s_, a)
        if k == 15:
            t15 = rel(15, f)
            l2 = TXT(('но дал в форме,',), size=64, shadow_a=0.6)
            s_, a = pop(t15)
            paste_c(cv, l2, 540, 312, s_, a)
            fire('l2', 'pop', gt - t15)
        return cv

    if sc == 12:  # split: logo + tags
        cv = split_base(fr)
        content = INT_V[min(len(INT_V) - 1, f - O[16])].copy()
        content.alpha_composite(Image.new('RGBA', content.size, (0, 0, 0, 70)))
        paste_c(content, LOGO_S420, 447, 290)
        tr = rel(16, f) - 0.9
        tz = rel(17, f) - 0.3
        s_, a = pop(tr)
        if a > 0:
            paste_c(content, TAG_R, 235, 618, s_, a); fire('tagr', 'pop', gt - tr)
        s_, a = pop(tz)
        if a > 0:
            paste_c(content, TAG_Z, 660, 618, s_, a); fire('tagz', 'pop', gt - tz)
        put_card(cv, content)
        lines = ('которая работает на ресторан,',) if k == 16 else ('которая работает на ресторан,', 'не на защиту')
        img = TXT(lines, size=50)
        if k == 16:
            s_, a = pop(st)
            paste_c(cv, img, 540, 812, s_, a)
        else:
            paste_c(cv, img, 540, 830)
        return cv

    if sc in (13, 14):  # zoom on falcon, arrow right; then coins go left
        cv = split_base(fr)
        content = CARD_BG.copy()
        e = ease_io((f - O[18]) / FPS / 0.5)
        Ls = 600 + (1100 - 600) * e
        tgt = (380 - HEAD[0] * 1100, 300 - HEAD[1] * 1100)
        cx = 447 + (tgt[0] - 447) * e
        cy = 341 + (tgt[1] - 341) * e
        paste_c(content, sized(LOGO, 'logo', Ls), cx, cy)
        ta = (f - O[18]) / FPS - 0.55
        if ta >= 0:
            bx, by = cx + BEAK[0] * Ls + 30, cy + BEAK[1] * Ls
            L = int(20 + (360 - 20) * ease(ta / 0.25))
            ar = arrow(360)
            ar = ar.crop((0, 0, L, ar.height)) if L < 360 else ar
            paste_tl(content, ar, bx, by - ar.height / 2)
            fire('arR', 'click', gt - ta)
        put_card(cv, content)
        if sc == 13:
            split_text(cv, ['сокол смотрит вправо'], st, gt)
        else:
            tl = st - 0.05
            if tl >= 0:
                L = int(40 + (760 - 40) * ease(tl / 0.3))
                ar = arrow(760, left=True)
                ar = ar.crop((ar.width - L, 0, ar.width, ar.height))
                paste_tl(cv, ar, CX0 + 820 - L, CY0 + 470 - ar.height / 2)
                fire('arL', 'click', gt - tl)
            for i in range(3):
                tc = st - (0.3 + 0.32 * i)
                x0 = 900 - i * 10
                if tc < 0:
                    paste_c(cv, COIN, x0 - i * 0, CY0 + 590 + (i - 1) * 0, 0.0 if tc < -0.25 else ease((tc + 0.25) / 0.25), 1)
                    continue
                x = x0 + (-160 - x0) * (ease_io(tc / 0.6) ** 1.4)
                paste_c(cv, COIN, x, CY0 + 590, 1, 1, rot=tc * 400)
                fire(('coin', i), 'coin', gt - tc)
            split_text(cv, ['деньги клиента уходят влево'], st, gt)
        return cv

    if sc == 15:  # comparison: our crest vs competitor
        cv = split_base(fr)
        t20 = rel(20, f)
        eL = ease(t20 / 0.25)
        dimL = ease((t20 - 2.26) / 0.2)
        lc = LCARD
        if dimL > 0:
            lc = LCARD.copy()
            ov = Image.new('RGBA', lc.size, (0, 0, 0, int(140 * dimL)))
            ov.putalpha(ImageChops_mul(lc.getchannel('A'), int(140 * dimL)))
            lc.alpha_composite(ov)
        paste_c(cv, lc, 300 - (1 - eL) * 500, 380, 1, 1, rot=8)
        eR = ease((t20 - 0.12) / 0.3)
        popR = 0
        if k == 21:
            tp = rel(21, f) - 0.86
            if tp >= 0:
                popR = 0.08 * math.sin(min(1, tp / 0.3) * math.pi) + 0.04 * min(1, tp / 0.3)
        if eR > 0:
            paste_c(cv, RCARD, 790 + (1 - eR) * 500, 390, 1 + popR, 1, rot=-8)
        for i in range(3):
            tc = t20 - (0.2 + 0.15 * i)
            if 0 <= tc <= 0.5:
                p = ease_io(tc / 0.5)
                x = -80 + (790 + 80) * p
                y = 390 - 160 * math.sin(p * math.pi)
                paste_c(cv, COIN, x, y, 1 - 0.5 * p, 1 - max(0, p - 0.8) * 5, rot=tc * 500)
                fire(('coin2', i), 'coin', gt - tc)
        if dimL > 0:
            s_, a = pop(t20 - 2.26)
            paste_c(cv, CROSS, 440, 540, s_ * 1.2, a)
            fire('xL', 'pop', gt - (t20 - 2.26))
        if k == 21:
            tp = rel(21, f) - 0.86
            s_, a = pop(tp)
            if a > 0:
                paste_c(cv, CHECK, 930, 560, s_ * 1.2, a)
                fire('vR', 'pop', gt - tp)
        if k == 20:
            lines = ('к адвокату, чей логотип',) if t20 < 1.2 else ('к адвокату, чей логотип', 'не пытается быть гербом,')
            img = TXT(lines, size=50)
            s_, a = pop(t20) if t20 < 1.2 else (1, 1)
            paste_c(cv, img, 540, 812 + (len(lines) - 1) * 16, s_, a)
        else:
            split_text(cv, ['а пытается быть понятным'], rel(21, f), gt)
        return cv

    if sc == 16:
        cv = spk_full(fr, 1.10 + 0.02 * st / 1.4, cy=720).convert('RGBA')
        plate_at(cv, 'Ты выиграл по эстетике,', 'y', Y_Y, st, gt)
        return cv

    if sc == 17:
        cv = spk_full(fr, 1.20 + 0.07 * st / 2.4, cy=700).convert('RGBA')
        plate_at(cv, 'Ты выиграл по эстетике,', 'y', Y_Y, 1.0, gt)
        plate_at(cv, 'проиграл по заявке от клиента', 'w', Y_W, st, gt)
        return cv
    raise ValueError(sc)


def ImageChops_mul(a, v):
    return a.point(lambda x: x * v // 255)


# ---------------- CTA & END ----------------
def render_cta(frames, i):
    n = len(frames)
    seq = [j // 2 for j in range(n * 2)]
    seq = seq + seq[::-1]
    src = frames[seq[i % len(seq)]]
    z = 1.8 + 0.04 * i / CTA_FRAMES
    w, h = 1080 / z, 1920 / z
    cx, cy = 560, 770
    x0, y0 = cx - w / 2, cy - h / 2
    cv = src.resize((W, H), Image.BICUBIC, box=(x0, y0, x0 + w, y0 + h))
    cv = cv.filter(ImageFilter.UnsharpMask(3, 60, 2)).convert('RGBA')
    bl = cv.filter(ImageFilter.GaussianBlur(28))
    cv.paste(bl, (0, 0), CTA_MASK)
    cv.alpha_composite(VIGN)
    t = i / FPS
    gt = (CTA_START + i) / FPS
    d = ImageDraw.Draw(cv)
    Wl = 4
    L = 210
    for (x, y, dx, dy) in [(60, 60, 1, 1), (1020, 60, -1, 1), (60, 1860, 1, -1), (1020, 1860, -1, -1)]:
        d.line([(x, y), (x + dx * L, y)], fill=WHITE, width=Wl)
        d.line([(x, y), (x, y + dy * L)], fill=WHITE, width=Wl)
    d.rounded_rectangle([120, 100, 206, 140], 6, outline=WHITE, width=4)
    d.rectangle([206, 110, 212, 130], fill=WHITE)
    d.rectangle([127, 107, 180, 133], fill=WHITE)
    fr_ = font('Rubik-400.ttf', 52)
    if (i // 12) % 2 == 0:
        d.ellipse([815, 114, 849, 148], fill=(255, 30, 30, 255))
    d.text((865, 131), 'REC', font=fr_, fill=WHITE, anchor='lm')
    d.text((108, 1790), '4K 60FPS', font=fr_, fill=WHITE, anchor='lm')
    d.text((972, 1790), 'HD', font=fr_, fill=WHITE, anchor='rm')
    bx0, by0, bx1, by1 = 413, 690, 668, 1110
    bl = 55
    for (x, y, dx, dy) in [(bx0, by0, 1, 1), (bx1, by0, -1, 1), (bx0, by1, 1, -1), (bx1, by1, -1, -1)]:
        d.line([(x, y), (x + dx * bl, y)], fill=(255, 255, 255, 220), width=3)
        d.line([(x, y), (x, y + dy * bl)], fill=(255, 255, 255, 220), width=3)
    s_, a = pop(t, 0.3)
    paste_c(cv, SIGN, 540, 330, s_, a)
    for txt, kind, cy_, dt, sz in (('Хотите проверить свой логотип?', 'y', 1305, 0.15, 54),
                                   ('Напишите в комментариях слово РАЗБОР', 'w', 1428, 0.3, 48)):
        tt = t - dt
        s_, a = pop(tt)
        if a > 0:
            paste_c(cv, P(txt, kind, size=sz, maxw=1010), 540, cy_, s_, a)
            fire(('cta', txt), 'pop', gt - tt)
    fire('cta', 'whoosh', CTA_START / FPS)
    return cv


END_BASE = Image.new('RGBA', (W, H), (0, 0, 0, 255))
paste_c(END_BASE, LRING, 540, 862)
_d = ImageDraw.Draw(END_BASE)
_d.text((540, 1062), 'Ведение соцсетей | lemonmedia', font=font('Manrope-500.ttf', 54), fill=WHITE, anchor='mm')
_d.text((540, 1153), '@lemon.logo', font=font('Manrope-500.ttf', 38), fill=(122, 122, 122, 255), anchor='mm')


def render_end(i):
    a = min(1, i / 6)
    cv = Image.new('RGBA', (W, H), (0, 0, 0, 255))
    cv = Image.blend(cv, END_BASE, a)
    fire('end', 'whoosh', END_START / FPS)
    return cv


# ---------------- whip pan ----------------
def whip(arr, shift, blur):
    a = np.roll(arr, shift, axis=1).astype(np.float32)
    if blur > 1:
        k = int(blur)
        c = np.cumsum(np.pad(a, ((0, 0), (k, k), (0, 0)), mode='edge'), axis=1)
        a = (c[:, 2 * k:] - c[:, :-2 * k]) / (2 * k)
        a = a[:, :W]
    return np.clip(a, 0, 255).astype(np.uint8)


WHIP_OUT = {-3: (-90, 30), -2: (-260, 80), -1: (-560, 150)}
WHIP_IN = {0: (560, 150), 1: (260, 80), 2: (90, 30)}


# ---------------- main loop ----------------
def main():
    dec = subprocess.Popen([FF, '-v', 'error', '-i', RAW, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
    scale = '540:960' if PREVIEW else '1080:1920'
    enc = subprocess.Popen([FF, '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', '1080x1920', '-r', str(FPS), '-i', '-',
                            '-vf', f'scale={scale}:flags=lanczos', '-c:v', 'libx264', '-preset', 'veryfast' if PREVIEW else 'slow',
                            '-crf', '23' if PREVIEW else '16', '-pix_fmt', 'yuv420p', OUT], stdin=subprocess.PIPE)
    fsz = 1080 * 1920 * 3
    clip_of = {}
    for k, (a, b) in enumerate(CF):
        for n in range(a, b):
            clip_of[n] = k
    cta_frames = []
    last = None
    n = 0
    step = 3 if PREVIEW else 1
    while True:
        buf = dec.stdout.read(fsz)
        if len(buf) < fsz:
            break
        if CTA_SRC[0] <= n < CTA_SRC[1]:
            cta_frames.append(Image.frombuffer('RGB', (1080, 1920), buf))
        if n in clip_of:
            k = clip_of[n]
            f = O[k] + (n - CF[k][0])
            fr = Image.frombuffer('RGB', (1080, 1920), buf)
            last = (fr, k)
            emit(enc, render(fr, k, f), f)
        n += 1
    fr, k = last
    for h in range(HOLD):
        emit(enc, render(fr, 23, SPEECH_FRAMES + h), SPEECH_FRAMES + h)
    for i in range(CTA_FRAMES):
        emit(enc, render_cta(cta_frames, i), CTA_START + i)
    for i in range(END_FRAMES):
        emit(enc, render_end(i), END_START + i)
    enc.stdin.close(); enc.wait()
    json.dump(sorted(EV), open('events.json', 'w'), ensure_ascii=False)
    print('frames', TOTAL, 'events', len(EV))


def emit(enc, cv, f):
    arr = np.asarray(cv.convert('RGB'))
    for b in WHIPS:
        if f - b in WHIP_OUT:
            s, bl = WHIP_OUT[f - b]; arr = whip(arr, s, bl)
        if f - b in WHIP_IN:
            s, bl = WHIP_IN[f - b]; arr = whip(arr, s, bl)
    enc.stdin.write(np.ascontiguousarray(arr).tobytes())
    if f % 100 == 0:
        print('frame', f, flush=True)


if __name__ == '__main__':
    main()
