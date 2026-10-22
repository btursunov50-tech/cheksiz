# Tarix qahramonlari ketma-ketligi (egasi, 2026-10-22): har biri 3 s turadi, oxirgi 0.9 s qumga aylanib to'kiladi,
# ostidan keyingisi paydo bo'ladi; oxirgisi qorong'ilikka to'kiladi.  python3 qum_ketma.py CHIQISH.mp4 klip1.mp4 klip2.mp4 ...
import cv2, numpy as np, sys, subprocess, tempfile
out, clips = sys.argv[1], sys.argv[2:]
W, H, F, T, DS = 720, 1280, 30, 3.0, 0.9
caps = [cv2.VideoCapture(c) for c in clips]
def read(cap):
    ok, fr = cap.read()
    return cv2.resize(fr, (W, H)).astype(np.float32) / 255 if ok else None
rng = np.random.default_rng(11); yy, xx = np.mgrid[:H, :W]
noise = cv2.GaussianBlur(rng.random((H, W)).astype(np.float32), (0, 0), 7); noise = (noise - noise.min()) / (noise.max() - noise.min())
dis = 0.55 * noise + 0.45 * (yy / H)                     # yuqoridan, dog'-dog' qumga aylanadi
P = 50000; pi = rng.integers(0, H * W, P); py, px = pi // W, pi % W; pd = dis[py, px]; pv = rng.random(P)
sand = np.array([90, 175, 230]) / 255                       # qum rangi (BGR)
E = lambda u: float(np.clip(u, 0, 1)) ** 2 * (3 - 2 * float(np.clip(u, 0, 1)))
tmp = tempfile.mkdtemp(); k = 0; cur = [None] * len(caps)
for i in range(len(clips)):
    n = int(T * F)
    for f in range(n):
        t = f / F
        a = read(caps[i]); cur[i] = a if a is not None else cur[i]; fr = cur[i].copy()
        dz = E((t - (T - DS)) / DS)
        if dz > 0:
            nxt = None
            if i + 1 < len(caps):
                b = read(caps[i + 1]); cur[i + 1] = b if b is not None else cur[i + 1]; nxt = cur[i + 1]
            bg = nxt if nxt is not None else np.zeros_like(fr)
            alive = (dis > dz * 1.05).astype(np.float32)[..., None]
            src = fr.copy(); fr = fr * alive + bg * (1 - alive)
            tt = np.clip((t - (T - DS)) - pd * DS, 0, None)
            sx = (px + np.sin(pv * 20 + t * 3) * 10 * tt).astype(int); sy = (py + (140 + 300 * pv) * tt * tt * 2 + 40 * tt).astype(int)
            m = (pd < dz * 1.05) & (sx >= 0) & (sx < W - 1) & (sy >= 0) & (sy < H - 1) & (tt < 1.5)
            c = src[py[m], px[m]] * 0.5 + sand * 0.6
            fr[sy[m], sx[m]] = c; fr[sy[m] + 1, sx[m]] = c * 0.8
        cv2.imwrite(f"{tmp}/{k:05d}.jpg", (np.clip(fr, 0, 1) * 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 92]); k += 1
    if i + 1 < len(caps):   # keyingi klip o'z vaqtidan davom etadi (qum paytida boshlangan)
        pass
subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(F), "-i", f"{tmp}/%05d.jpg", "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p", out], check=True)
