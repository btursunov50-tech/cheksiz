#!/usr/bin/env python3
"""«Bepul yordamchi»: 15 sahna to'liq kodda — «Bitta tugma» uslubi (sariq qog'oz, siyoh chizgi, neon ko'k/qizil).
TLANG=uz|ru|en python3 video/yordamchi/chiz.py <out_dir> [y01 ...] → <out>/yNN.mp4 (1080x1920, 30 fps, ovozsiz).
Sahna uzunligi = 0.3 + ovoz qatori + 0.5 s (voice/NN_usta.wav)."""
import os, sys, math, subprocess, importlib.util
from PIL import Image, ImageDraw
R = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
spec = importlib.util.spec_from_file_location("tchiz", f"{R}/video/tugma/chiz/chiz.py"); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
W, H, FPS = C.W, C.H, C.FPS; F, INK, INK2, CELL, BLUE, RED = C.F, C.INK, C.INK2, C.CELL, C.BLUE, C.RED
ramp, glow, ctext, box, line, phone, keys = C.ramp, C.glow, C.ctext, C.box, C.line, C.phone, C.keys
GOLD = (240, 170, 60); GREEN = (60, 200, 120)
LANG = os.environ.get("TLANG", "uz")
TX = {  # uz, ru, en
 "stop": ("TO'XTANG!", "СТОП!", "STOP!"), "free": ("Bepul yordamchi", "Бесплатный помощник", "A free helper"),
 "team": ("inson + sun'iy intellekt", "человек + искусственный интеллект", "human + artificial intelligence"),
 "hi": ("Salom! Yordam kerak", "Привет! Нужна помощь", "Hi! I need help"), "voice": ("ovozli xabar", "голосовое", "voice message"),
 "c1": ("Sovg'a yutdingiz!", "Вы выиграли подарок!", "You won a gift!"), "c2": ("Pulingiz ×2", "Деньги ×2", "Your money ×2"),
 "c3": ("Ish: oyiga 490 mln", "Работа: 490 млн/мес", "Job: 490M a month"), "scam": ("ALDOV!", "ОБМАН!", "SCAM!"),
 "set": ("Sozlamalar", "Настройки", "Settings"), "priv": ("Maxfiylik", "Конфиденциальность", "Privacy"),
 "two": ("Bulutli parol", "Облачный пароль", "Two-Step Verification"), "on": ("YOQILDI", "ВКЛЮЧЕНО", "ON"),
 "monthly": ("oyiga atigi", "всего в месяц", "only a month"), "deliv": ("Bepul yetkazish", "Бесплатная доставка", "Free delivery"),
 "real": ("Haqiqatda qancha?", "Сколько на самом деле?", "What you really pay"),
 "wed": ("To'y", "Свадьба", "Wedding"), "w1": ("Zal", "Зал", "Hall"), "w2": ("Osh", "Плов", "Plov"), "w3": ("Libos", "Платье", "Dress"),
 "w4": ("Mashina", "Машина", "Car"), "tot": ("Jami", "Итого", "Total"),
 "bat": ("Batareya holati", "Состояние батареи", "Battery health"), "notif": ("Bildirishnomalar", "Уведомления", "Notifications"),
 "made": ("Ishlab chiqarilgan", "Изготовлено", "Made"), "best": ("Yaroqli", "Годен до", "Best before"),
 "calm": ("Keling, xotirjam gaplashaylik.", "Давайте спокойно поговорим.", "Let's talk calmly."),
 "every": ("har tong", "каждое утро", "every morning"), "tip": ("bepul maslahat", "бесплатный совет", "a free tip"),
 "biz": ("Biznesingiz uchun", "Для вашего бизнеса", "For your business"),
 "s1": ("QR menyu", "QR-меню", "QR menu"), "s2": ("Sayt", "Сайт", "Website"), "s3": ("Bot", "Бот", "Bot"), "s4": ("Video", "Видео", "Video"),
 "easy": ("Bepul · oddiy · tushunarli", "Бесплатно · просто · понятно", "Free · simple · clear"),
}
def T(k): return TX[k][("uz", "ru", "en").index(LANG)]
def new(): return C.PAPER_IM.copy()
def fit(d, s, size, maxw, bold=True):
    while size > 20 and d.textlength(s, font=F(size, bold)) > maxw: size -= 2
    return F(size, bold)
def pop(t, t0, d=.35): return ramp(t, t0, d)
def bubble(d, x0, y0, x1, y1, fill, col=INK): d.rounded_rectangle((x0, y0, x1, y1), 30, fill=fill, outline=col, width=4)
def bot_tag(im, y=1520, sz=76):
    d = ImageDraw.Draw(im); h = "@sahiychishopbot"; f = F(sz, True); tw = d.textlength(h, font=f)
    d.rounded_rectangle(((W - tw) / 2 - 40, y - 20, (W + tw) / 2 + 40, y + sz + 44), 30, fill=(250, 236, 200), outline=INK, width=5); ctext(d, W / 2, y + 6, h, f)
    glow(im, lambda g, c: g.rounded_rectangle(((W - tw) / 2 - 40, y - 20, (W + tw) / 2 + 40, y + sz + 44), 30, outline=c, width=7), BLUE, 18)
def fade_in(im, lay, a):
    if a <= 0: return
    if a < 1: lay.putalpha(lay.getchannel("A").point(lambda v: int(v * a)))
    im.alpha_composite(lay)
def layer(): L = Image.new("RGBA", (W, H), (0, 0, 0, 0)); return L, ImageDraw.Draw(L)

def y01(t):  # telefon + chiroq + TO'XTANG
    im = new()
    def scr(g, x0, y0, x1, y1):
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2 - 40
        g.ellipse((cx - 90, cy - 120, cx + 90, cy + 60), outline=INK, width=6); g.rectangle((cx - 45, cy + 60, cx + 45, cy + 120), outline=INK, width=6)
        for k in range(3): g.line((cx - 40, cy + 80 + k * 18, cx + 40, cy + 80 + k * 18), fill=INK, width=4)
    phone(im, 330, 560, fn=scr)
    a = pop(t, .6)
    if a > 0: glow(im, lambda g, c: g.ellipse((W / 2 - 90, 920 - 120, W / 2 + 90, 920 + 60), outline=c + (int(255 * a),), width=10), GOLD, 30, 3)
    d = ImageDraw.Draw(im)
    if t >= .3:
        s = min(1, (t - .3) / .25); f = fit(ImageDraw.Draw(im), T("stop"), int(130 * (0.6 + .4 * s)), 980)
        glow(im, lambda g, c: ctext(g, W / 2, 200, T("stop"), f, c), RED, 14)
    if t >= 1.6: ctext(ImageDraw.Draw(im), W / 2, 1270, T("free"), fit(d, T("free"), 66, 940))
    return im

def person(d, cx, base, col=INK):
    d.ellipse((cx - 55, base - 420, cx + 55, base - 310), outline=col, width=6)
    d.line((cx, base - 310, cx, base - 120), fill=col, width=7); d.line((cx, base - 120, cx - 60, base), fill=col, width=7); d.line((cx, base - 120, cx + 60, base), fill=col, width=7)
def robot(d, cx, base, col=INK):
    d.rounded_rectangle((cx - 70, base - 430, cx + 70, base - 310), 18, outline=col, width=6); d.line((cx, base - 430, cx, base - 480), fill=col, width=5); d.ellipse((cx - 12, base - 500, cx + 12, base - 476), outline=col, width=5)
    for ex in (-30, 30): d.ellipse((cx + ex - 12, base - 390, cx + ex + 12, base - 366), fill=BLUE)
    d.rounded_rectangle((cx - 80, base - 300, cx + 80, base - 110), 20, outline=col, width=6); d.line((cx - 40, base - 110, cx - 40, base), fill=col, width=7); d.line((cx + 40, base - 110, cx + 40, base), fill=col, width=7)
def y02(t):  # ∞ + inson va robot qo'l berishadi
    im = new(); d = ImageDraw.Draw(im)
    a = pop(t, 0)
    glow(im, lambda g, c: (g.ellipse((300, 180, 560, 400), outline=c + (int(255 * a),), width=16), g.ellipse((520, 180, 780, 400), outline=c + (int(255 * a),), width=16)), GOLD, 18)
    d = ImageDraw.Draw(im); ctext(d, W / 2, 450, "Infinite AI & Me", F(76, True))
    if t >= .8: ctext(d, W / 2, 560, T("team"), fit(d, T("team"), 46, 960, False), INK2)
    base = 1450; k = ramp(t, 1.2, 1.4)
    person(d, 300, base); robot(d, 780, base)
    hx = 300 + 60 + (W / 2 - 360) * k; rx = 780 - 80 - (780 - 80 - W / 2) * k
    d.line((300, base - 260, hx, base - 220), fill=INK, width=7); d.line((780, base - 250, rx, base - 220), fill=INK, width=7)
    if k >= 1: glow(im, lambda g, c: g.ellipse((W / 2 - 40, base - 260, W / 2 + 40, base - 180), outline=c, width=7), BLUE, 16)
    return im

def y03(t):  # chat + mikrofon + bot nomi
    im = new()
    def scr(g, x0, y0, x1, y1):
        if t >= .5: bubble(g, x1 - 330, y0 + 50, x1 - 20, y0 + 150, (214, 176, 112)); g.text((x1 - 310, y0 + 80), T("hi"), font=fit(g, T("hi"), 30, 270), fill=INK)
        if t >= 2.0:
            bubble(g, x1 - 330, y0 + 190, x1 - 20, y0 + 290, (214, 176, 112))
            for i in range(14): hh = 12 + 30 * abs(math.sin(i * 1.3 + t * 6)); g.line((x1 - 230 + i * 14, y0 + 240 - hh / 2, x1 - 230 + i * 14, y0 + 240 + hh / 2), fill=INK, width=5)
            g.ellipse((x1 - 315, y0 + 210, x1 - 255, y0 + 270), outline=INK, width=4); g.text((x1 - 300, y0 + 300), T("voice"), font=F(24), fill=INK2)
    phone(im, 330, 360, fn=scr)
    if t >= 1.0: bot_tag(im, 1300)
    return im

def card(d, x0, y0, w, h, txt, seed):
    box(d, x0, y0, x0 + w, y0 + h, 4, INK, 1, fill=(250, 238, 206), seed=seed); d.text((x0 + 24, y0 + h / 2 - 26), txt, font=fit(d, txt, 46, w - 48), fill=INK)
def y04(t):  # shubhali xabarlar → ALDOV!
    im = new(); d = ImageDraw.Draw(im)
    for i, k in enumerate(("c1", "c2", "c3")):
        if t >= .4 + i * 1.6: card(d, 120, 360 + i * 300, 840, 200, T(k), 40 + i)
    if t >= 6.4:  # qizil muhr kartalar ustida
        a = pop(t, 6.4, .3); L, g = layer(); f = F(150, True); tw = g.textlength(T("scam"), font=f)
        g.rounded_rectangle((W / 2 - tw / 2 - 40, 560, W / 2 + tw / 2 + 40, 800), 30, outline=RED, width=12); ctext(g, W / 2, 590, T("scam"), f, RED)
        L = L.rotate(-12, center=(W / 2, 680)); fade_in(im, L, a)
    return im

def y05(t):  # qulf + qadamlar
    im = new(); d = ImageDraw.Draw(im)
    closed = t >= 4.2; cx, cy = W / 2, 520
    d.rounded_rectangle((cx - 150, cy, cx + 150, cy + 230), 30, fill=(214, 176, 112), outline=INK, width=7)
    sh = 0 if closed else -60
    d.arc((cx - 100, cy - 170 + sh, cx + 100, cy + 30 + sh), 180, 360, fill=INK, width=18); d.line((cx - 100, cy - 70 + sh, cx - 100, cy + (0 if closed else -40)), fill=INK, width=18); d.line((cx + 100, cy - 70 + sh, cx + 100, cy), fill=INK, width=18)
    d.ellipse((cx - 22, cy + 80, cx + 22, cy + 124), fill=INK)
    for i, k in enumerate(("set", "priv", "two")):
        if t >= .8 + i * 1.0:
            y = 900 + i * 150; card(d, 160, y, 760, 110, f"{i + 1}. {T(k)}", 50 + i)
            if i < 2: ctext(d, W / 2, y + 108, "↓", F(40, True), INK2)
    if closed:
        glow(im, lambda g, c: g.rounded_rectangle((cx - 150, cy, cx + 150, cy + 230), 30, outline=c, width=8), BLUE, 18)
        d = ImageDraw.Draw(im); ctext(d, W / 2, 1380, T("on"), F(80, True), (30, 140, 90))
    return im

def y06(t):  # -70%, oyiga atigi, bepul yetkazish → haqiqatda qancha?
    im = new(); d = ImageDraw.Draw(im)
    tags = [("−70%", RED), (f"{T('monthly')} 100 000", INK), (T("deliv"), INK)]
    for i, (s, col) in enumerate(tags):
        if t >= .3 + i * 1.3:
            y = 300 + i * 280; box(d, 160, y, 920, y + 190, 5, INK, 1, fill=(250, 236, 200), seed=60 + i)
            d.ellipse((190, y + 75, 230, y + 115), outline=INK, width=4); d.text((260, y + 60), s, font=fit(d, s, 64, 640), fill=col)
    if t >= 4.6:
        a = pop(t, 4.6); ctext(d, W / 2, 1100, "↓", F(80, True))
        L, g = layer(); box(g, 120, 1210, 960, 1380, 6, INK, 1, fill=(214, 176, 112), seed=70); ctext(g, W / 2, 1255, T("real"), fit(g, T("real"), 66, 800)); fade_in(im, L, a)
        if t >= 5.4: glow(im, lambda g, c: g.rectangle((120, 1210, 960, 1380), outline=c, width=7), BLUE, 16)
    return im

def y07(t):  # to'y ro'yxati → jami
    im = new(); d = ImageDraw.Draw(im); C.title(d, T("wed"), 160, 90)
    box(d, 170, 330, 910, 1330, 5, INK, 1, fill=CELL, seed=80)
    for i, k in enumerate(("w1", "w2", "w3", "w4")):
        if t >= .3 + i * .5:
            y = 400 + i * 160; d.text((220, y), T(k), font=F(54), fill=INK)
            for j in range(5): d.ellipse((560 + j * 60, y + 30, 572 + j * 60, y + 42), fill=INK2)
    if t >= 2.6:
        line(d, (200, 1060), (880, 1060), 5); d.text((220, 1110), T("tot"), font=F(64, True), fill=INK)
        glow(im, lambda g, c: g.text((620, 1100), "∑ = ?", font=F(80, True), fill=c), RED, 12)
    return im

def y08(t):  # batareya
    im = new()
    lvl = max(.78, 1 - .22 * ramp(t, .4, 1.6))
    def scr(g, x0, y0, x1, y1):
        cx = (x0 + x1) / 2; bx0, by0, bx1, by1 = cx - 90, y0 + 120, cx + 90, y0 + 500
        g.rounded_rectangle((bx0, by0, bx1, by1), 20, outline=INK, width=7); g.rectangle((cx - 35, by0 - 30, cx + 35, by0), fill=INK)
        top = by1 - 12 - (by1 - by0 - 24) * lvl; g.rectangle((bx0 + 14, top, bx1 - 14, by1 - 14), fill=GREEN)
    phone(im, 330, 300, fn=scr); d = ImageDraw.Draw(im)
    if t >= 2.4:
        s = f"{T('bat')}: 78%"; ctext(d, W / 2, 1220, s, fit(d, s, 60, 960))
        glow(im, lambda g, c: g.rectangle((90, 1200, 990, 1310), outline=c, width=6), BLUE, 14)
    return im

def bell(g, cx, cy, s=1.0, col=INK, ang=0):
    pts = [(cx - 110 * s, cy + 90 * s), (cx - 90 * s, cy - 20 * s), (cx - 60 * s, cy - 100 * s), (cx, cy - 130 * s), (cx + 60 * s, cy - 100 * s), (cx + 90 * s, cy - 20 * s), (cx + 110 * s, cy + 90 * s)]
    r = math.radians(ang); pts = [(cx + (x - cx) * math.cos(r) - (y - cy) * math.sin(r), cy + (x - cx) * math.sin(r) + (y - cy) * math.cos(r)) for x, y in pts]
    g.line(pts + [pts[0]], fill=col, width=9, joint="curve"); g.ellipse((cx - 22 * s, cy + 100 * s, cx + 22 * s, cy + 144 * s), outline=col, width=7)
def y09(t):  # qo'ng'iroqcha → o'chirish
    im = new(); d = ImageDraw.Draw(im); off = t >= 2.4
    ang = 0 if off else 14 * math.sin(t * 22)
    bell(d, W / 2, 600, 1.6, INK2 if off else INK, ang)
    if not off: d.ellipse((W / 2 + 90, 360, W / 2 + 220, 490), fill=RED); ctext(d, W / 2 + 155, 395, "46", F(56, True), (255, 255, 255))
    else: line(d, (W / 2 - 220, 380), (W / 2 + 220, 860), 14, RED)
    ctext(d, W / 2, 1000, T("notif"), fit(d, T("notif"), 64, 900))
    x0, y0 = W / 2 - 140, 1130; k = ramp(t, 2.0, .4)
    d.rounded_rectangle((x0, y0, x0 + 280, y0 + 130), 65, fill=(BLUE if k < .5 else (190, 170, 140)), outline=INK, width=6)
    kx = x0 + 215 - 150 * k; d.ellipse((kx - 52, y0 + 13, kx + 52, y0 + 117), fill=(250, 240, 215), outline=INK, width=5)
    return im

def y10(t):  # konserva va sut, ikki sana
    im = new(); d = ImageDraw.Draw(im)
    d.rectangle((170, 420, 470, 820), fill=(214, 176, 112), outline=INK, width=6); d.ellipse((170, 390, 470, 450), fill=(232, 204, 150), outline=INK, width=6); d.arc((170, 790, 470, 850), 0, 180, fill=INK, width=6)
    d.polygon([(620, 470), (760, 380), (900, 470)], fill=(240, 232, 214), outline=INK); d.rectangle((620, 470, 900, 860), fill=(246, 240, 226), outline=INK, width=6)
    for i, (k, dt) in enumerate((("made", "12.03.2026"), ("best", "12.09.2027"))):
        if t >= .5 + i * 1.2:
            y = 1000 + i * 190; box(d, 120, y, 960, y + 150, 4, INK, 1, fill=(250, 238, 206), seed=90 + i)
            d.text((150, y + 45), T(k) + ":", font=fit(d, T(k) + ":", 46, 420, False), fill=INK2); d.text((600, y + 40), dt, font=F(52, True), fill=INK)
            if t >= 2.4 + i * .6: glow(im, lambda g, c, y=y: g.rectangle((120, y, 960, y + 150), outline=c, width=6), BLUE, 12); d = ImageDraw.Draw(im)
    return im

def y11(t):  # Excel + Alt + =
    im = new(); d = ImageDraw.Draw(im); C.title(d, "Excel / Word", 160, 80)
    S = C.Sheet(cw=(100, 430, 350), rh=90, rows=6); S.y0 = 330; S.grid(d, 1.0, "AB")
    for r in range(2, 5): S.put(d, 2, r, f"{(r * 7 + 3) * 1000:,}".replace(",", " "), right=True)
    if t >= 2.6: glow(im, lambda g, c: S.put(g, 2, 5, "72 000", col=c, bold=True, right=True), RED, 10)
    keys(im, t, ["Alt", "="], .8, 2.2, 1000)
    return im

def y12(t):  # g'azabli xabar → xotirjam javob
    im = new(); d = ImageDraw.Draw(im)
    bubble(d, 120, 300, 760, 620, (250, 210, 190), RED)
    for k in range(3):
        pts = [(170 + i * 50, 400 + k * 70 + (20 if i % 2 else -20)) for i in range(11)]; d.line(pts, fill=RED, width=6)
    d.text((680, 300), "!!!", font=F(90, True), fill=RED)
    if t >= 1.6:
        a = pop(t, 1.6); L, g = layer(); bubble(g, 160, 780, 960, 1060, (220, 240, 250), BLUE)
        f = fit(g, T("calm"), 56, 740); ctext(g, 560, 890, T("calm"), f); fade_in(im, L, a)
        if t >= 2.4: glow(im, lambda g, c: g.rounded_rectangle((160, 780, 960, 1060), 30, outline=c, width=6), BLUE, 14)
    return im

def y13(t):  # tong, choy, kanal
    im = new(); d = ImageDraw.Draw(im); k = ramp(t, 0, 2.2)
    cy = 820 - 260 * k
    glow(im, lambda g, c: g.ellipse((W / 2 - 150, cy - 150, W / 2 + 150, cy + 150), fill=c), GOLD, 40, 2); d = ImageDraw.Draw(im)
    d.rectangle((0, 820, W, 1000), fill=(232, 204, 150)); line(d, (0, 820), (W, 820), 5)
    d.rounded_rectangle((W / 2 - 110, 860, W / 2 + 110, 970), 30, fill=(250, 240, 215), outline=INK, width=5)
    for i in range(3): d.arc((W / 2 - 60 + i * 40, 800, W / 2 - 20 + i * 40, 860), 200, 340, fill=INK2, width=4)
    ctext(d, W / 2, 1050, "05:00", F(130, True)); s = f"{T('every')} · {T('tip')}"; ctext(d, W / 2, 1220, s, fit(d, s, 52, 960, False), INK2)
    if t >= 1.6: ctext(d, W / 2, 1340, "t.me/infinite_ai_and_me", F(52, True), (40, 110, 170))
    return im

def y14(t):  # biznes: QR, sayt, bot, video
    im = new(); d = ImageDraw.Draw(im)
    for i in range(8): d.rectangle((140 + i * 100, 260, 240 + i * 100, 360), fill=(RED if i % 2 else (250, 236, 200)), outline=INK, width=3)
    d.rectangle((160, 360, 920, 700), fill=CELL, outline=INK, width=6); d.rectangle((460, 480, 620, 700), outline=INK, width=5)
    ctext(d, W / 2, 380, T("biz"), fit(d, T("biz"), 54, 700))
    for i, k in enumerate(("s1", "s2", "s3", "s4")):
        if t >= .4 + i * .8:
            x = 130 + (i % 2) * 430; y = 820 + (i // 2) * 330
            box(d, x, y, x + 390, y + 280, 5, INK, 1, fill=(250, 238, 206), seed=100 + i)
            if k == "s1":
                for a in range(3):
                    for b in range(3):
                        if (a + b) % 2 == 0 or a == b: d.rectangle((x + 30 + a * 40, y + 30 + b * 40, x + 64 + a * 40, y + 64 + b * 40), fill=INK)
            elif k == "s2": d.rectangle((x + 30, y + 30, x + 170, y + 150), outline=INK, width=4); d.line((x + 30, y + 60, x + 170, y + 60), fill=INK, width=4)
            elif k == "s3": d.rounded_rectangle((x + 40, y + 40, x + 160, y + 140), 16, outline=INK, width=5); d.ellipse((x + 70, y + 75, x + 90, y + 95), fill=BLUE); d.ellipse((x + 110, y + 75, x + 130, y + 95), fill=BLUE)
            else: d.polygon([(x + 70, y + 40), (x + 70, y + 150), (x + 160, y + 95)], fill=RED)
            d.text((x + 30, y + 190), T(k), font=fit(d, T(k), 52, 330), fill=INK)
    return im

def y15(t):  # katta bot nomi
    im = new(); d = ImageDraw.Draw(im)
    def scr(g, x0, y0, x1, y1):
        bubble(g, x0 + 18, y0 + 60, x1 - 60, y0 + 180, (250, 238, 206)); bubble(g, x0 + 80, y0 + 220, x1 - 18, y0 + 320, (214, 176, 112))
    phone(im, 330, 260, fn=scr)
    bot_tag(im, 1180, 84)
    if t >= 1.0: d = ImageDraw.Draw(im); ctext(d, W / 2, 1400, T("easy"), fit(d, T("easy"), 54, 980, False), INK2)
    return im

SC = {f"y{i:02}": globals()[f"y{i:02}"] for i in range(1, 16)}
def vdur(i): return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f"{R}/video/yordamchi/voice/{i:02}_usta.wav"], capture_output=True, text=True).stdout)
def dur(name): return round(0.3 + vdur(int(name[1:])) + 0.5, 2)
if __name__ == "__main__":
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    for name in (sys.argv[2:] or list(SC)):
        fn, d_ = SC[name], dur(name)
        p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                              "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p", f"{out}/{name}.mp4"], stdin=subprocess.PIPE)
        for i in range(int(d_ * FPS)): p.stdin.write(fn(i / FPS).convert("RGB").tobytes())
        p.stdin.close(); p.wait(); print(name, d_, flush=True)
