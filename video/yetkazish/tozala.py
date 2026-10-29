# Veo qo'shgan yozuvlarni tozalaydi: clips/sNN.mp4 → clips/sNN_y.mp4
#  s01: 2.6–3.7 s da pastda chiqqan subtitr harflari — o'rniga 2.45 s dagi toza kadr (kamera harakatiga moslab siljitilgan).
#  s02: telefondagi ko'k tugmaga yozilgan «Usta» — tugma har kadrda rangi bo'yicha topiladi va bir tekis ko'kka bo'yaladi.
#  s10: 5 s dan konfet o'ramlarida chiqqan oq harflar — qizil bilan to'ldiriladi.
# Ishlatish: python3 video/yetkazish/tozala.py [s01 s02]
import os, subprocess, sys, cv2, numpy as np
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "clips")

REF = {}
def s01(f, t):
    # oldingi toza kadr (2.45 s) kamera harakatiga moslab (ORB + affine) siljitiladi va harflar o'rniga qo'yiladi
    if t < 2.5: REF["f"] = f.copy(); return f
    if t > 3.8: return f
    x0, y0, x1, y1 = 230, 1000, 640, 1130
    g0, g1 = cv2.cvtColor(REF["f"], cv2.COLOR_BGR2GRAY), cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
    band = np.zeros(g0.shape, np.uint8); band[850:1280, 100:720] = 255; band[y0:y1, x0:x1] = 0
    o = cv2.ORB_create(1500); k0, d0 = o.detectAndCompute(g0, band); k1, d1 = o.detectAndCompute(g1, band)
    mt = sorted(cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True).match(d0, d1), key=lambda m: m.distance)[:300]
    M, _ = cv2.estimateAffinePartial2D(np.float32([k0[m.queryIdx].pt for m in mt]), np.float32([k1[m.trainIdx].pt for m in mt]), method=cv2.RANSAC)
    if M is None: return f
    w = cv2.warpAffine(REF["f"], M, (f.shape[1], f.shape[0]), borderMode=cv2.BORDER_REFLECT)
    dif = cv2.absdiff(cv2.cvtColor(f[y0:y1, x0:x1], cv2.COLOR_BGR2GRAY), cv2.cvtColor(w[y0:y1, x0:x1], cv2.COLOR_BGR2GRAY))
    h = cv2.cvtColor(f[y0:y1, x0:x1], cv2.COLOR_BGR2HSV)
    m = (((h[..., 2] > 170) & (h[..., 1] < 90)) | (dif > 35)).astype(np.uint8)
    m = cv2.dilate(m, np.ones((13, 13), np.uint8)).astype(np.float32)
    a = cv2.GaussianBlur(m, (11, 11), 0)[..., None]
    f[y0:y1, x0:x1] = (f[y0:y1, x0:x1] * (1 - a) + w[y0:y1, x0:x1] * a).astype(np.uint8)
    return f

def s02(f, t):
    h = cv2.cvtColor(f, cv2.COLOR_BGR2HSV)
    m = cv2.inRange(h, (100, 120, 120), (125, 255, 255)); m[:, 520:] = 0; m[:250] = 0
    n, lab, st, _ = cv2.connectedComponentsWithStats(m)
    best = [k for k in range(1, n) if st[k][4] > 800 and 1.8 < st[k][2] / max(st[k][3], 1) < 8]
    if not best: return f
    k = max(best, key=lambda k: st[k][4]); b = (lab == k).astype(np.uint8)
    b = cv2.morphologyEx(b, cv2.MORPH_CLOSE, np.ones((15, 15), np.uint8))
    hull = cv2.convexHull(max(cv2.findContours(b, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0], key=cv2.contourArea))
    fill = np.zeros(m.shape, np.uint8); cv2.fillPoly(fill, [hull], 1); fill = cv2.erode(fill, np.ones((3, 3), np.uint8))
    col = np.median(f[(lab == k)], axis=0)
    a = cv2.GaussianBlur(fill.astype(np.float32), (5, 5), 0)[..., None]
    return (f * (1 - a) + col * a).astype(np.uint8)

def s10(f, t):
    # 5 s dan konfet o'ramlarida oq harflar paydo bo'ladi — qizil o'ram ustidagi oq piksellar qizil bilan to'ldiriladi
    if t < 4.8: return f
    y0 = 560; roi = f[y0:]; h = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    red = cv2.inRange(h, (0, 120, 80), (12, 255, 255)) | cv2.inRange(h, (170, 120, 80), (179, 255, 255))
    near = cv2.dilate(red, np.ones((15, 15), np.uint8)) > 0
    m = (((h[..., 2] > 120) & (h[..., 1] < 150)) & near).astype(np.uint8) * 255
    m = cv2.dilate(m, np.ones((5, 5), np.uint8))
    f[y0:] = cv2.inpaint(roi, m, 4, cv2.INPAINT_TELEA)
    return f

JOBS = {"s01": s01, "s02": s02, "s10": s10}
for name in (sys.argv[1:] or JOBS):
    src = os.path.join(D, name + ".mp4"); tmp = os.path.join(D, name + "_tmp.mp4")
    c = cv2.VideoCapture(src); fps = c.get(cv2.CAP_PROP_FPS); W, H = int(c.get(3)), int(c.get(4))
    w = cv2.VideoWriter(tmp, cv2.VideoWriter_fourcc(*"mp4v"), fps, (W, H)); i = 0
    while True:
        ok, f = c.read()
        if not ok: break
        w.write(JOBS[name](f, i / fps)); i += 1
    w.release()
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-i", src, "-map", "0:v", "-map", "1:a?", "-c:v", "libx264", "-crf", "16",
                    "-pix_fmt", "yuv420p", "-c:a", "copy", os.path.join(D, name + "_y.mp4")], check=True)
    os.remove(tmp); print(name, "→", name + "_y.mp4")
