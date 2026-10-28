# 9-klip: savatdagi ko'k telefon orqasida Veo/Hailuo chizgan olma logotipini har kadrda topib, inpaint bilan o'chiradi.
# Logotip = ko'k korpus ichidagi kichik oq-kulrang ixcham dog'. Ishlatish: python3 video/eskirish/logo_ochir.py IN.mp4 OUT.mp4
import sys, subprocess, os, cv2, numpy as np
inp, out = sys.argv[1], sys.argv[2]
c = cv2.VideoCapture(inp); fps = c.get(5); W, H = int(c.get(3)), int(c.get(4))
w = cv2.VideoWriter(out + ".tmp.mp4", cv2.VideoWriter_fourcc(*"mp4v"), fps, (W, H)); n = 0
while True:
    ok, f = c.read()
    if not ok: break
    hsv = cv2.cvtColor(f, cv2.COLOR_BGR2HSV)
    blue = ((hsv[..., 0] > 95) & (hsv[..., 0] < 125) & (hsv[..., 1] > 60) & (hsv[..., 2] > 60)).astype(np.uint8)
    blue = cv2.morphologyEx(blue, cv2.MORPH_CLOSE, np.ones((25, 25), np.uint8))
    nb, lb, sb, _ = cv2.connectedComponentsWithStats(blue); body = np.zeros_like(blue)
    for k in range(1, nb):
        if sb[k][4] > 2500: body[lb == k] = 1                      # katta ko'k telefon korpusi
    white = ((hsv[..., 1] < 70) & (hsv[..., 2] > 150)).astype(np.uint8) * body      # oq logotip
    g = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY).astype(np.float32); bg = cv2.medianBlur(g.astype(np.uint8), 41).astype(np.float32)
    dark = ((bg - g > 35) & (hsv[..., 1] < 120)).astype(np.uint8) * cv2.erode(body, np.ones((15, 15), np.uint8))   # qora-kulrang logotip
    white = np.maximum(white, dark)
    nw, lw, sw, _ = cv2.connectedComponentsWithStats(white); m = np.zeros_like(white)
    for k in range(1, nw):
        x, y, ww, hh, a = sw[k]
        if 15 < a < 3000 and 0.5 < hh / max(ww, 1) < 2.2: m[lw == k] = 1
    if m.any():
        f = cv2.inpaint(f, cv2.dilate(m, np.ones((9, 9), np.uint8)) * 255, 7, cv2.INPAINT_TELEA); n += 1
    w.write(f)
w.release()
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", out + ".tmp.mp4", "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", out], check=True)
os.remove(out + ".tmp.mp4"); print(out, "logotip o'chirilgan kadrlar:", n)
