# Ko'chadagi fonuslar (chiroq shishasi) yorug'ligini ko'k neonga bo'yaydi (egasi, 2026-10-28).
# Nomzodlar: yorqin, issiq rangli, ixcham bo'laklar; --skip bilan noto'g'ri topilganlar (quyosh, barglar) chiqariladi.
# Ishlatish: python3 video/eskirish/fonus.py img/s13.png OUT.png [--show SHEET.jpg] [--skip 3,7] [--roi x0,y0,x1,y1 ...]
import argparse, cv2, numpy as np
p = argparse.ArgumentParser(); p.add_argument("inp"); p.add_argument("out"); p.add_argument("--show")
p.add_argument("--skip", default=""); p.add_argument("--only", default=""); p.add_argument("--vmin", type=int, default=215)
p.add_argument("--roi", action="append", default=[]); p.add_argument("--lamp", action="append", default=[], help="cx,cy,r: shu doira ichidagi yorug' joy bo'yaladi (avtomatik qidiruv o'chadi)"); p.add_argument("--amin", type=int, default=25); p.add_argument("--amax", type=int, default=9000)
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
    if ar / (w * h) < 0.3 or not (0.3 < h / max(w, 1) < 4): continue
    cand.append(k)
# Egasi (2026-10-28, 2-urinish): «bittasini qil, bittasini qilma, faqat fonus ichi bo'lsin, shuvab tashlama»:
# fonuslar navbatma-navbat (1-si bo'yaladi, 2-si yo'q ...), faqat fonus ichidagi yorug' shisha, atrofga nur yoyilmaydi.
keep = np.zeros((H, W), np.float32); sheet = img.copy()
V = hsv[..., 2].astype(np.float32) / 255
if a.lamp and not a.roi: cand = []
for i, q in enumerate(a.lamp):                       # qo'lda berilganlar: tartib bo'yicha 0, 2, 4 ... bo'yaladi
    cx, cy, r = map(int, q.split(","))
    use = True   # egasi (2026-10-28, 3): katta fonuslar hammasi ko'k, navbatma-navbat faqat zich qatorlarda
    cv2.circle(sheet, (cx, cy), r, (0, 255, 0) if use else (0, 0, 255), 2)
    if use:
        c = np.zeros((H, W), np.float32); cv2.circle(c, (cx, cy), int(r * 0.8), 1, -1)
        keep = np.maximum(keep, c * np.clip((V - 0.62) / 0.25, 0, 1))
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
