# Klipdagi rangli yuzaga (yorliq, karta, taymer, telefon ekrani) yozuv yozadi: yuza har kadrda rangi bo'yicha topiladi,
# yozuv uning 4 burchagiga egilib yopishadi va faqat o'sha rangli piksellarga chiziladi (ustidan o'tgan qo'l/narsa yozuvni yopadi).
# Ishlatish: python3 video/chegirma/yuza.py   (pastdagi JOBS bo'yicha clips/sNN.mp4 → clips/sNN_y.mp4)
import os, subprocess, sys, cv2, numpy as np
from PIL import Image, ImageDraw, ImageFont
D = os.path.dirname(os.path.abspath(__file__))
FONT = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"

# yuza: hsv quyi/yuqori chegara, 1-kadrdagi taxminiy joy (x, y, w, h), yozuvlar [(boshi, oxiri, qatorlar, rang)]
# qator: matn; "~" bilan boshlansa — kichik va ustidan chizilgan (eski narx)
JOBS = {
    "s01": [
        dict(lo=(160, 100, 120), hi=(179, 255, 255), box=(288, 0, 408, 404), texts=[(0, 99, ["-70%"], (255, 250, 210))]),
        dict(lo=(20, 120, 180), hi=(38, 255, 255), box=(496, 602, 207, 179), texts=[(0, 99, ["170 000"], (200, 20, 60))]),
        dict(lo=(0, 0, 215), hi=(179, 40, 255), box=(462, 776, 183, 141), texts=[(0, 99, ["300 000"], (90, 90, 100))]),
    ],
    "s05": [
        dict(lo=(20, 120, 180), hi=(38, 255, 255), box=(326, 701, 328, 160), texts=[
            (0, 5.5, ["~300 000", "170 000"], (200, 20, 60)),
            (5.5, 99, ["-43%"], (200, 20, 60))]),
        dict(lo=(160, 120, 120), hi=(179, 255, 255), box=(222, 418, 498, 294), texts=[
            (0, 99, ["-70%"], (255, 250, 210))]),
    ],
    "s07": [
        dict(lo=(150, 80, 180), hi=(179, 255, 255), box=(185, 665, 450, 120), inner=(28, 10, 30), texts=[
            (0, 99, ["TIMER"], (255, 120, 190))]),
    ],
    "s12": [
        dict(lo=(55, 60, 120), hi=(90, 255, 255), box=(75, 415, 75, 150), roi=(55, 380, 260, 660), close=15, cover=(150, 235, 200), texts=[
            (0, 7.65, ["~300 000", "170 000", "-43%"], (190, 20, 60))]),  # 7.7 s dan Veo kadrni almashtiradi — ishlatilmaydi
    ],
}

def order(p):
    s, d = p.sum(1), np.diff(p, axis=1).ravel()
    return np.array([p[s.argmin()], p[d.argmin()], p[s.argmax()], p[d.argmax()]], np.float32)

def match(prev, new):  # burchaklarni oldingi kadrdagiga eng yaqin tartibda (yorliq aylanganda sakramasin)
    best = min(range(4), key=lambda k: np.linalg.norm(np.roll(new, k, 0) - prev, axis=1).sum())
    return np.roll(new, best, 0)

def timer(t0, t):
    m, sec = divmod(max(0, int(t0[0]) * 60 + int(t0[1]) - int(t)), 60)
    return f"00:{m:02}:{sec:02}"

def card(lines, color, W, H):
    if lines[0].startswith("{T}"):
        im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im); s = lines[0][3:]
        cell = W / len(s); f = ImageFont.truetype(FONT, int(min(H * 0.8, cell * 1.45)))
        for k, ch in enumerate(s):
            x0, y0, x1, y1 = d.textbbox((0, 0), ch, font=f)
            d.text((k * cell + (cell - (x1 - x0)) / 2 - x0, (H - (y1 - y0)) / 2 - y0), ch, font=f, fill=color + (255,))
        return np.array(im)
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    big = [l for l in lines if not l.startswith("~")]; n = len(lines)
    sz = int(min(H / (n * 0.95 if n > 1 else 0.8), W / max(0.75 * len(max(big, key=len)), 1)))
    y = (H - sum((sz * 0.6 if l.startswith("~") else sz) for l in lines) * 1.05) / 2
    for l in lines:
        small = l.startswith("~"); t = l.lstrip("~"); f = ImageFont.truetype(FONT, int(sz * (0.6 if small else 1)))
        x0, y0, x1, y1 = d.textbbox((0, 0), t, font=f); x = (W - (x1 - x0)) / 2 - x0
        d.text((x, y - y0), t, font=f, fill=color + (230 if small else 255,))
        if small: d.line([(x + x0 - 6, y + (y1 - y0) / 2), (x + x1 + 6, y + (y1 - y0) / 2)], fill=color + (255,), width=max(3, sz // 14))
        y += (y1 - y0) * 1.25
    return np.array(im)

def run(name, jobs):
    src = os.path.join(D, "clips", f"{name}.mp4"); tmp = os.path.join(D, "clips", f"{name}_y_noaudio.mp4")
    c = cv2.VideoCapture(src); fps = c.get(cv2.CAP_PROP_FPS); W, H = int(c.get(3)), int(c.get(4))
    w = cv2.VideoWriter(tmp, cv2.VideoWriter_fourcc(*"mp4v"), fps, (W, H))
    st = [dict(box=j["box"], q=None, a0=j["box"][2] * j["box"][3]) for j in jobs]; i = 0
    while True:
        ok, f = c.read()
        if not ok: break
        t = i / fps; i += 1; hsv = cv2.cvtColor(f, cv2.COLOR_BGR2HSV); out = f.astype(np.float32)
        for j, s in zip(jobs, st):
            m = cv2.morphologyEx(cv2.inRange(hsv, j["lo"], j["hi"]), cv2.MORPH_CLOSE, np.ones((j.get("close", 9),) * 2, np.uint8))
            if j.get("roi"): x0, y0, x1, y1 = j["roi"]; r = np.zeros_like(m); r[y0:y1, x0:x1] = 1; m = m * r
            n, lab, stats, _ = cv2.connectedComponentsWithStats(m)
            x, y, bw, bh = s["box"]; best, bo = 0, 0
            for k in range(1, n):  # oldingi joy bilan eng ko'p ustma-ust tushgan bo'lak
                a, b, cw, ch, area = stats[k]
                ov = max(0, min(x + bw, a + cw) - max(x, a)) * max(0, min(y + bh, b + ch) - max(y, b))
                if area > max(0.15 * bw * bh, 0.2 * s["a0"]) and ov > bo: best, bo = k, ov
            if not best:  # yuza tez uchib ketdi (yorliq tushmoqda): eng katta mos bo'lak
                cand = [k for k in range(1, n) if 0.3 * s["a0"] < stats[k][4] < 3 * s["a0"]]
                if not cand: continue
                best = max(cand, key=lambda k: stats[k][4]); s["q"] = None
            s["box"] = tuple(stats[best][:4]); mk = (lab == best).astype(np.uint8)
            if j.get("inner"):  # ramka (taymer): yozuv ramka ichidagi qorong'i to'rtburchakka, eski raqamlar bo'yab yopiladi
                raw = cv2.inRange(hsv, j["lo"], j["hi"])
                cs, hier = cv2.findContours(raw, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
                cx, cy = x + bw / 2, y + bh / 2; good = []
                for k, h in enumerate(cs):
                    if hier[0][k][3] < 0 or cv2.contourArea(h) < 0.3 * s["a0"]: continue
                    (rx, ry), (rw, rh), _ = cv2.minAreaRect(h); rw, rh = max(rw, rh), min(rw, rh)
                    if cv2.contourArea(h) > 0.8 * rw * rh and 2.2 < rw / max(rh, 1) < 6: good.append((np.hypot(rx - cx, ry - cy), h))
                if not good: continue
                hole = min(good, key=lambda g: g[0])[1]
                mk = np.zeros_like(mk); cv2.drawContours(mk, [hole], -1, 1, -1); s["box"] = cv2.boundingRect(hole)
            if j.get("cover"):  # butun yuza (telefon ekrani) bir rangga bo'yaladi, ustiga yozuv
                rect = cv2.boxPoints(cv2.minAreaRect(max(cv2.findContours(mk, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0], key=cv2.contourArea)))
                mk = np.zeros_like(mk); cv2.fillPoly(mk, [rect.astype(np.int32)], 1)
            cnt = max(cv2.findContours(mk, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0], key=cv2.contourArea)
            q = order(cv2.boxPoints(cv2.minAreaRect(cnt)).astype(np.float32))
            q = q if s["q"] is None else match(s["q"], q)
            s["q"] = q if s["q"] is None else 0.6 * q + 0.4 * s["q"]  # titramasin
            txt = next((tx for tx in j["texts"] if tx[0] <= t < tx[1]), None)
            if not txt: continue
            if txt[2][0] == "TIMER": txt = (txt[0], txt[1], ["{T}" + timer((59, 59), t)], txt[3])
            q = s["q"]; tw = int(np.linalg.norm(q[1] - q[0])); th = int(np.linalg.norm(q[3] - q[0]))
            if tw < 20 or th < 20: continue
            img = card(txt[2], txt[3], tw * 2, th * 2)
            pad = 0.1; F = np.float32([[pad, pad], [1 - pad, pad], [1 - pad, 1 - pad], [pad, 1 - pad]])  # chetidan 10% ichkarida
            P = np.float32([[0, 0], [1, 0], [1, 1], [0, 1]]) * [tw * 2, th * 2]
            Q = q[0] + F[:, :1] * (q[1] - q[0]) + F[:, 1:] * (q[3] - q[0])
            Mx = cv2.getPerspectiveTransform(P.astype(np.float32), Q.astype(np.float32))
            wr = cv2.warpPerspective(img, Mx, (W, H), flags=cv2.INTER_LINEAR)
            mm = cv2.dilate(mk, np.ones((5, 5), np.uint8))[..., None]
            if j.get("inner") or j.get("cover"):
                fill = cv2.GaussianBlur(mm[..., 0].astype(np.float32), (9, 9), 0)[..., None]
                out = out * (1 - fill) + np.float32((j.get("inner") or j["cover"])[::-1]) * fill
            a = wr[..., 3:4] / 255.0 * mm
            out = out * (1 - a) + wr[..., [2, 1, 0]].astype(np.float32) * a
        w.write(np.clip(out, 0, 255).astype(np.uint8))
    w.release()
    dst = os.path.join(D, "clips", f"{name}_y.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", tmp, "-i", src, "-map", "0:v", "-map", "1:a?", "-c:v", "libx264",
                    "-crf", "16", "-pix_fmt", "yuv420p", "-c:a", "copy", dst], check=True)
    os.remove(tmp); print(dst)

for name in (sys.argv[1:] or JOBS):
    run(name, JOBS[name])
