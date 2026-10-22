# Effektlar (egasi, 2026-10-22): zarbga sakrash (zoom punch), nokautda silkinish, eng kuchli zarbda oq chaqnash,
# jang kadrlarida uchqunlar, naqorat so'zlari animatsiyasi; musiqa: bass +3 dB, stereo kengroq.
# python3 fx.py KIRISH.mp4 CHIQISH.mp4
import cv2, numpy as np, subprocess, sys, os
src, out = sys.argv[1], sys.argv[2]
cap = cv2.VideoCapture(src); F = cap.get(cv2.CAP_PROP_FPS); W, H = 720, 1280; N = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
PUNCH = [39.2, 41.3, 44.4, 46.9, 49.1, 52.0, 54.1, 98.1, 101.9, 103.9, 105.7, 109.5, 111.9, 115.1, 118.7, 121.9]  # kuchli zarblar
SHAKE = [(67.4, 69.6, 14), (109.5, 114.6, 6)]          # nokaut (zarba, yiqilish), jang 2
FLASH = [108.6, 67.8]                                   # eng kuchli zarb, nokaut zarbasi
SPARK = []   # egasi (2026-10-22): qorga o'xshagan uchqunlar kerak emas
rng = np.random.default_rng(3); NP = 160
P = np.c_[rng.random(NP) * W, rng.random(NP) * H, rng.random(NP) * 0.6 + 0.4, rng.random(NP) * 6.28, rng.random(NP)]
def env(t, t0, a=0.03, r=0.22): return 0 if t < t0 - a else (min(1, (t - t0 + a) / a) if t < t0 else np.exp(-(t - t0) / r))
p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", str(F), "-i", "-",
                      "-c:v", "libx264", "-crf", "19", "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
for k in range(N):
    ok, fr = cap.read()
    if not ok: break
    t = k / F; img = fr
    z = 1 + 0.07 * max(env(t, x) for x in PUNCH)                       # zarbga sakrash
    dx = dy = 0
    for a, b, amp in SHAKE:
        if a <= t <= b:
            e = amp * (1 - (t - a) / (b - a)) ** 0.5
            dx, dy = e * np.sin(t * 61), e * np.cos(t * 47)
    if z > 1.001 or dx or dy:
        M = cv2.getRotationMatrix2D((W / 2, H / 2), 0, z); M[0, 2] += dx; M[1, 2] += dy
        img = cv2.warpAffine(img, M, (W, H), borderMode=cv2.BORDER_REFLECT)
    if any(a <= t <= b for a, b in SPARK):                               # uchqunlar
        lay = np.zeros_like(img, dtype=np.float32)
        for x0, y0, sp, ph, s in P:
            y = (y0 - t * 260 * sp) % H; x = (x0 + np.sin(t * 2 + ph) * 30) % W
            c = (60, 150 + 80 * s, 255); r = 1 + int(2 * s)
            cv2.circle(lay, (int(x), int(y)), r, c, -1, cv2.LINE_AA)
        lay = lay + cv2.GaussianBlur(lay, (0, 0), 4) * 1.5
        img = np.clip(img.astype(np.float32) + lay * 0.8, 0, 255).astype(np.uint8)
    fl = max(env(t, x, 0.02, 0.18) for x in FLASH)                     # oq chaqnash
    if fl > 0.01: img = cv2.addWeighted(img, 1 - fl * 0.85, np.full_like(img, 255), fl * 0.85, 0)
    p.stdin.write(img.tobytes())
p.stdin.close(); p.wait()
