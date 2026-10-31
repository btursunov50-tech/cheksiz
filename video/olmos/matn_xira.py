# 8-sahna: Veo gazeta, plakat va kino lentasi yorliqlariga soxta harflar yozgan. Och (qog'oz rangli) yuzalar ichidagi qora harf chiziqlari
# har kadrda topilib, qog'oz rangi bilan to'ldiriladi va yengil xiralashtiriladi — matn o'rnida xira kulrang chiziqlar qoladi, rasmlar (uzuk surati) tegilmaydi.
# Ishlatish: python3 video/olmos/matn_xira.py clips/s08_asl.mp4 clips/s08.mp4
import sys, subprocess, cv2, numpy as np
src, dst = sys.argv[1], sys.argv[2]
c = cv2.VideoCapture(src); fps = c.get(cv2.CAP_PROP_FPS); W, H = int(c.get(3)), int(c.get(4))
tmp = dst + ".tmp.mp4"; w = cv2.VideoWriter(tmp, cv2.VideoWriter_fourcc(*"mp4v"), fps, (W, H))
while True:
    ok, f = c.read()
    if not ok: break
    hsv = cv2.cvtColor(f, cv2.COLOR_BGR2HSV); g = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
    paper = ((hsv[..., 2] > 120) & (hsv[..., 1] < 150) & (hsv[..., 0] < 35)).astype(np.uint8)
    paper = cv2.morphologyEx(paper, cv2.MORPH_CLOSE, np.ones((25, 25), np.uint8))       # harflar orasidagi teshiklar yopiladi
    paper = cv2.morphologyEx(paper, cv2.MORPH_OPEN, np.ones((15, 15), np.uint8))
    bg = cv2.medianBlur(g, 21)
    ink = ((bg.astype(np.int16) - g.astype(np.int16)) > 28).astype(np.uint8) & paper    # qog'ozdan ancha qoraroq ingichka chiziqlar
    n, lab, st, _ = cv2.connectedComponentsWithStats(ink)
    m = np.zeros_like(ink)
    bright = cv2.dilate((hsv[..., 2] > 250).astype(np.uint8), np.ones((9, 9), np.uint8))   # uzuk/olmos yaltirog'i — tegilmaydi
    for k in range(1, n):
        x, y, bw, bh, a = st[k]
        big_ok = y + bh < 260 and bh < 80                                                # tepadagi plakat sarlavhasi — katta harflar
        if (bh < 45 or big_ok) and a < 2500:
            comp = lab[y:y + bh, x:x + bw] == k
            if bright[y:y + bh, x:x + bw][comp].mean() < 0.05: m[lab == k] = 1            # harf o'lchamidagi qora bo'laklar (surat, uzuk emas)
    if m.any():
        m = cv2.dilate(m, np.ones((5, 5), np.uint8))
        fill = cv2.inpaint(f, m * 255, 5, cv2.INPAINT_TELEA)
        fill = cv2.GaussianBlur(fill, (0, 0), 2.5)
        a = cv2.GaussianBlur(cv2.dilate(m, np.ones((9, 9), np.uint8)).astype(np.float32), (11, 11), 0)[..., None]
        f = (f * (1 - a) + fill * a).astype(np.uint8)
    # tepa o'ngdagi plakat yorlig'i (katta soxta harflar): butun och yuzasi qattiq xiralashtiriladi
    top = np.zeros_like(paper); top[:300, 480:] = 1
    sign = cv2.dilate(paper & top, np.ones((15, 15), np.uint8))
    if sign.any():
        a = cv2.GaussianBlur(sign.astype(np.float32), (21, 21), 0)[..., None]
        f = (f * (1 - a) + cv2.GaussianBlur(f, (0, 0), 9) * a).astype(np.uint8)
    w.write(f)
w.release()
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", dst], check=True)
import os; os.remove(tmp)
