#!/usr/bin/env python3
"""«O'zligim» 30 s ko'rinish (animatik): tasdiqlangan rasmlar + qo'shiq; 12 kadr/s qotib-qotib harakat (stop-motion), qog'oz «qaynashi»,
sekin kamera, siyoh yonib o'tadigan o'tish. Haqiqiy harakat keyin Veo kliplaridan keladi.
python3 video/ozlik/chiz/animatik.py <out.mp4> [qo'shiq boshlanishi s] [davomiyligi s]"""
import sys, subprocess, numpy as np
from PIL import Image, ImageFilter
R = "video/ozlik"; W, H = 1920, 1080; AF = 12; OF = 24
OUT = sys.argv[1]; SS = float(sys.argv[2]) if len(sys.argv) > 2 else 11.0; DUR = float(sys.argv[3]) if len(sys.argv) > 3 else 30.0
# (rasm, fokus x, y (0..1), zoom boshi, oxiri)
SC = [("s01", .67, .48, 1.00, 1.18), ("s02", .45, .35, 1.10, 1.00), ("s03", .45, .40, 1.00, 1.08), ("s04", .50, .35, 1.08, 1.00),
      ("s05", .55, .40, 1.00, 1.08), ("s06", .45, .40, 1.08, 1.00), ("s07", .50, .40, 1.00, 1.07), ("s08", .50, .45, 1.07, 1.00)]
IM = []
for n, *_ in SC:
    im = Image.open(f"{R}/img/{n}.png").convert("RGB"); s = max(W * 1.2 / im.width, H * 1.2 / im.height)
    IM.append(im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS))
rng = np.random.default_rng(3)
def noise(sc):
    n = rng.random((H // sc + 2, W // sc + 2)).astype(np.float32)
    return np.asarray(Image.fromarray((n * 255).astype(np.uint8)).resize((W, H), Image.BICUBIC), np.float32) / 255.
WIPE = (noise(160) * .75 + noise(30) * .2 + noise(6) * .05); WIPE = (WIPE - WIPE.min()) / (WIPE.max() - WIPE.min())
GRAIN = [noise(2) - .5 for _ in range(3)]
ease = lambda x: x * x * (3 - 2 * x)
def frame(k, u, j):
    """k-sahna, u=0..1 sahna ichida, j=qaynash indeksi"""
    im, (n, fx, fy, z0, z1) = IM[k], SC[k]; z = z0 + (z1 - z0) * ease(u)
    cw = min(im.width, im.height * W / H) / (1.04 * z); ch = cw * H / W
    cx = min(max(fx * im.width, cw / 2 + 3), im.width - cw / 2 - 3); cy = min(max(fy * im.height, ch / 2 + 3), im.height - ch / 2 - 3)
    jx, jy = [(0, 0), (2, -1), (-1, 2)][j]  # qog'oz qaynashi: har kadr 1–2 px siljiydi
    box = (cx - cw / 2 + jx, cy - ch / 2 + jy, cx + cw / 2 + jx, cy + ch / 2 + jy)
    return np.asarray(im.resize((W, H), Image.LANCZOS, box=box), np.float32)
N = len(SC); SD = DUR / N; TR = 0.5
p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(AF), "-i", "-",
                      "-ss", str(SS), "-t", str(DUR), "-i", f"{R}/qoshiq.mp3", "-map", "0:v", "-map", "1:a",
                      "-vf", f"fps={OF}", "-af", f"afade=t=in:d=0.5,afade=t=out:st={DUR - 1.5}:d=1.5",
                      "-c:v", "libx264", "-crf", "20", "-preset", "medium", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest", OUT], stdin=subprocess.PIPE)
for f in range(int(DUR * AF)):
    t = f / AF; k = min(N - 1, int(t / SD)); u = (t - k * SD) / SD; j = f % 3
    A = frame(k, u, j)
    tt = t - (k + 1) * SD + TR  # oxirgi TR soniyada keyingi sahnaga siyoh o'tishi
    if k < N - 1 and tt > 0:
        B = frame(k + 1, 0, j); a = ease(min(1, tt / TR)) * 1.15
        m = np.clip((a - WIPE) / .06, 0, 1)[..., None]
        edge = np.clip(1 - np.abs(a - WIPE) / .05, 0, 1)[..., None] * (0 < a < 1.15)
        A = A * (1 - m) + B * m; A = A * (1 - .75 * edge) + np.array([70, 40, 15], np.float32) * .75 * edge
    A = A * (1 + GRAIN[j][..., None] * .06)
    p.stdin.write(np.clip(A, 0, 255).astype(np.uint8).tobytes())
p.stdin.close(); p.wait(); print(OUT)
