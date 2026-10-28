# Ko'chadagi fonuslar (chiroq shishasi) yorug'ligini ko'k neonga bo'yaydi (egasi, 2026-10-28).
# Nomzodlar: yorqin, issiq rangli, ixcham bo'laklar; --skip bilan noto'g'ri topilganlar (quyosh, barglar) chiqariladi.
# Ishlatish: python3 video/eskirish/fonus.py img/s13.png OUT.png [--show SHEET.jpg] [--skip 3,7] [--roi x0,y0,x1,y1 ...]
import argparse, cv2, numpy as np
p = argparse.ArgumentParser(); p.add_argument("inp"); p.add_argument("out"); p.add_argument("--show")
p.add_argument("--skip", default=""); p.add_argument("--only", default=""); p.add_argument("--vmin", type=int, default=215)
p.add_argument("--roi", action="append", default=[]); p.add_argument("--glass", action="append", default=[], help="cx,cy,hw,hh: fonus shishasi (ellips), aniq o'lchangan"); p.add_argument("--lamp", action="append", default=[], help="cx,cy,r: shu doira ichidagi yorug' joy bo'yaladi (avtomatik qidiruv o'chadi)"); p.add_argument("--amin", type=int, default=25); p.add_argument("--amax", type=int, default=9000)
a = p.parse_args()
img = cv2.imread(a.inp); H, W = img.shape[:2]; f = img.astype(np.float32)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
m = ((hsv[..., 2] >= a.vmin) & (hsv[..., 0] < 40)).astype(np.uint8)
if a.roi:
    r = np.zeros_like(m)
    for q in a.roi:
        x0, y0, x1, y1 = map(int, q.split(",")); r[y0:y1, x0:x1] = 1
    m = m * r
m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
n, lab, st, cen = cv2.connectedComponentsWithStats(m)
skip = {int(x) for x in a.skip.split(",") if x}; only = {int(x) for x in a.only.split(",") if x}
cand = []
for k in range(1, n):
    x, y, w, h, ar = st[k]
    if not (a.amin <= ar <= a.amax): continue
    if ar / (w * h) < 0.5 or not (0.5 < h / max(w, 1) < 2.2) or ar > 500: continue   # faqat ixcham mayda chiroq nuqtalari (dog' emas)
    cand.append(k)
# Egasi (2026-10-28, 2-urinish): «bittasini qil, bittasini qilma, faqat fonus ichi bo'lsin, shuvab tashlama»:
# fonuslar navbatma-navbat (1-si bo'yaladi, 2-si yo'q ...), faqat fonus ichidagi yorug' shisha, atrofga nur yoyilmaydi.
keep = np.zeros((H, W), np.float32); sheet = img.copy()
V = hsv[..., 2].astype(np.float32) / 255
if (a.lamp or a.glass) and not a.roi: cand = []
for i, q in enumerate(a.lamp):                       # qo'lda berilgan taxminiy joy atrofida aniq shisha qidiriladi
    cx, cy, r = map(int, q.split(","))
    R = int(r * 1.8); x0, y0, x1, y1 = max(0, cx - R), max(0, cy - R), min(W, cx + R), min(H, cy + R)
    win = hsv[y0:y1, x0:x1]
    best, bd = None, 1e9
    for thr in (235, 220, 205, 190):                   # eng yorqin, ixcham, issiq bo'lak — fonus shishasi
        bm = ((win[..., 2] >= thr) & (win[..., 0] < 40)).astype(np.uint8)
        nn, ll, ss, cc = cv2.connectedComponentsWithStats(bm)
        for k in range(1, nn):
            bx, by, bw, bh, ba = ss[k]
            if ba < 0.04 * r * r or bw > 2.2 * r or bh > 2.6 * r or ba / (bw * bh) < 0.35: continue
            d = np.hypot(cc[k][0] + x0 - cx, cc[k][1] + y0 - cy) - 0.02 * ba
            if d < bd: bd, best = d, (ll == k)
        if best is not None: break
    if best is None:
        cv2.circle(sheet, (cx, cy), r, (0, 0, 255), 2); continue
    m1 = np.zeros((H, W), np.uint8); m1[y0:y1, x0:x1] = best.astype(np.uint8)
    cs, _ = cv2.findContours(m1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE); cv2.drawContours(m1, cs, -1, 1, -1)   # teshiklarni to'ldirish
    keep = np.maximum(keep, m1.astype(np.float32) * np.clip((V - 0.45) / 0.3, 0.35, 1))
    cv2.drawContours(sheet, cs, -1, (0, 255, 0), 2)
for q in a.glass:                                    # aniq o'lchangan shisha: faqat ellips ichidagi yorug' joy
    cx, cy, hw, hh = map(int, q.split(","))
    e1 = np.zeros((H, W), np.float32); cv2.ellipse(e1, (cx, cy), (hw, hh), 0, 0, 360, 1, -1)
    e1 = cv2.GaussianBlur(e1, (5, 5), 0)
    keep = np.maximum(keep, e1 * np.clip((V - 0.4) / 0.3, 0.3, 1))
    cv2.ellipse(sheet, (cx, cy), (hw, hh), 0, 0, 360, (0, 255, 0), 2)
cand = sorted(cand, key=lambda k: (st[k][0], st[k][1]))   # uzoqdagilar chapdan o'ngga, navbatma-navbat
for i, k in enumerate(cand, 1):
    x, y, w, h, ar = st[k]
    use = (i in only) if only else (i not in skip and i % 2 == 1)
    cv2.rectangle(sheet, (x - 3, y - 3), (x + w + 3, y + h + 3), (0, 255, 0) if use else (0, 0, 255), 2)
    if use: keep[lab == k] = np.clip((V[lab == k] - 0.62) / 0.25, 0, 1)
core = cv2.GaussianBlur(keep, (3, 3), 0)
halo = cv2.GaussianBlur(keep, (0, 0), 3) * 0.25
w = np.clip(np.maximum(core, halo), 0, 1)[..., None]
L = f.mean(2, keepdims=True) / 255
tint = np.clip(np.array([255., 200., 70.]) * np.power(L, 0.6) * 1.35, 0, 255)
white = np.clip((L - 0.9) / 0.1, 0, 1) * core[..., None]
tint = tint * (1 - white) + np.array([255., 240., 210.]) * white
out = f * (1 - w) + tint * w
cv2.imwrite(a.out, out.astype(np.uint8))
if a.show: cv2.imwrite(a.show, np.hstack([cv2.resize(sheet, (470, 836)), cv2.resize(out.astype(np.uint8), (470, 836))]))
print(len(cand), "nomzod")
