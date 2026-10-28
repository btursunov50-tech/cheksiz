# 8-klip: Veo batareyani to'ldirib qo'ydi (ma'noga zid). 0-kadrdagi deyarli bo'sh batareyani har kadrga
# (telefon harakatiga moslab, ORB + affin) qayta yopishtiradi va qizil bo'lakni 2 marta sekin miltillatadi.
# Ishlatish: python3 video/eskirish/batareya.py clips/s08.mp4 clips/s08_y.mp4
import sys, subprocess, cv2, numpy as np
inp, out = sys.argv[1], sys.argv[2]
c = cv2.VideoCapture(inp); fps = c.get(5); fr = []
while True:
    ok, f = c.read()
    if not ok: break
    fr.append(f)
f0 = fr[0]; H, W = f0.shape[:2]
B = (160, 345, 495, 520)                       # batareya (0-kadrda)
mk = np.full((H, W), 255, np.uint8); mk[B[1]:B[3], B[0]:B[2]] = 0; mk[620:1100, 100:720] = 0   # batareya va shilliqqurt chiqarilgan
orb = cv2.ORB_create(3000); bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
k0, d0 = orb.detectAndCompute(cv2.cvtColor(f0, cv2.COLOR_BGR2GRAY), mk)
patch = np.zeros((H, W), np.float32); patch[B[1]:B[3], B[0]:B[2]] = 1; patch = cv2.GaussianBlur(patch, (31, 31), 0)
redm = np.zeros((H, W), np.float32); redm[365:500, 185:260] = 1; redm = cv2.GaussianBlur(redm, (15, 15), 0)
w = cv2.VideoWriter(out + ".tmp.mp4", cv2.VideoWriter_fourcc(*"mp4v"), fps, (W, H)); M = np.eye(2, 3, dtype=np.float32)
for i, f in enumerate(fr):
    k1, d1 = orb.detectAndCompute(cv2.cvtColor(f, cv2.COLOR_BGR2GRAY), mk)
    if d1 is not None and len(k1) > 20:
        mt = sorted(bf.match(d0, d1), key=lambda m: m.distance)[:400]
        if len(mt) > 20:
            A, inl = cv2.estimateAffinePartial2D(np.float32([k0[m.queryIdx].pt for m in mt]), np.float32([k1[m.trainIdx].pt for m in mt]), method=cv2.RANSAC)
            if A is not None: M = 0.6 * A.astype(np.float32) + 0.4 * M
    t = i / fps
    blink = 1 - 0.45 * max(0, np.sin(np.pi * (t - 2.0) / 0.8)) * (2.0 < t < 2.8) - 0.45 * max(0, np.sin(np.pi * (t - 5.0) / 0.8)) * (5.0 < t < 5.8)
    src = f0.astype(np.float32) * (1 - redm[..., None] * (1 - blink))
    ws = cv2.warpAffine(src, M, (W, H)); wm = cv2.warpAffine(patch, M, (W, H))[..., None]
    w.write((f * (1 - wm) + ws * wm).astype(np.uint8))
w.release()
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", out + ".tmp.mp4", "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", out], check=True)
import os; os.remove(out + ".tmp.mp4"); print(out)
