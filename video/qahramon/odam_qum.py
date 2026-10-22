# Faqat odamning o'zi qumga aylanib yerga oqib tushadi, orqa fon joyida qoladi (egasi, 2026-10-22).
# Odam fondan rembg (u2net_human_seg) bilan ajratiladi; odam o'rni atrofidan to'ldiriladi (inpaint); qum oyog'i ostida uyum bo'ladi.
# python3 odam_qum.py KIRISH.mp4 CHIQISH.mp4 [turish_s=3] [oqish_s=5]
import cv2, numpy as np, sys, subprocess
from rembg import remove, new_session
src, out = sys.argv[1], sys.argv[2]
T0 = float(sys.argv[3]) if len(sys.argv) > 3 else 3.0; TD = float(sys.argv[4]) if len(sys.argv) > 4 else 5.0
sess = new_session("u2net_human_seg")
cap = cv2.VideoCapture(src); F = cap.get(cv2.CAP_PROP_FPS) or 30; W, H = 720, 1280
frames = []
while True:
    ok, fr = cap.read()
    if not ok: break
    frames.append(cv2.resize(fr, (W, H)))
N = len(frames)
def fill(fr, md):
    # har qatorda bo'shliq chap va o'ng tomondagi teksturaning ko'zgu nusxasi bilan to'ldiriladi, chegarasi yumshatiladi
    out = fr.copy(); Hh, Ww = md.shape
    for y in np.nonzero(md.any(axis=1))[0]:
        row = np.nonzero(md[y])[0]; a, b = row.min(), row.max() + 1; w = b - a
        L = fr[y, max(0, a - w):a][::-1]; R = fr[y, b:min(Ww, b + w)][::-1]
        if len(L) < w: L = np.concatenate([L, np.repeat(L[-1:] if len(L) else fr[y, b:b+1], w - len(L), 0)])
        if len(R) < w: R = np.concatenate([np.repeat(R[:1] if len(R) else fr[y, a-1:a], w - len(R), 0), R])
        wt = np.linspace(0, 1, w)[:, None]
        out[y, a:b] = (L[:w] * (1 - wt) + R[-w:] * wt).astype(fr.dtype)
    sm = cv2.GaussianBlur(out, (0, 0), 3); m3 = cv2.GaussianBlur(md.astype(np.float32), (0, 0), 4)[..., None]
    return (out * (1 - m3 * 0.5) + sm * m3 * 0.5).astype(fr.dtype)
def mask(fr):
    a = remove(cv2.cvtColor(fr, cv2.COLOR_BGR2RGB), session=sess, only_mask=True)
    return (np.array(a) > 128).astype(np.uint8)
k0 = min(N - 1, int(T0 * F)); M0 = mask(frames[k0])         # odam shakli oqish boshlanishida
ys, xs = np.nonzero(M0); ground = min(int(np.percentile(ys, 99.5)), H - 90)
rng = np.random.default_rng(5); yy, xx = np.mgrid[:H, :W]
noise = cv2.GaussianBlur(rng.random((H, W)).astype(np.float32), (0, 0), 5); noise = (noise - noise.min()) / (noise.max() - noise.min())
top, bot = ys.min(), ys.max()
dis = np.clip(0.6 * (yy - top) / max(1, bot - top) + 0.4 * noise, 0, 1)   # boshidan oyog'iga qarab, dog'-dog'
# zarrachalar: odam piksellari (har 2-piksel)
sel = (M0[::2, ::2] > 0); py, px = np.nonzero(sel); py, px = py * 2, px * 2
col = frames[k0][py, px].astype(np.float32); ta = T0 + TD * 0.7 * dis[py, px]
vx = rng.normal(0, 7, len(py)); g = 320 + rng.random(len(py)) * 260
land_y = ground - rng.random(len(py)) * 6
sand = np.array([120, 172, 205], np.float32)                       # qum rangi (BGR)
pile = np.zeros((H, W, 3), np.float32); pa = np.zeros((H, W), np.float32); landed = np.zeros(len(py), bool)
p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", str(F), "-i", "-",
                      "-c:v", "libx264", "-crf", "19", "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
for k in range(N):
    t = k / F; fr = frames[k].astype(np.float32)
    if t < T0:
        img = fr
    else:
        m = mask(frames[k]) if k % 2 == 0 or k == k0 else m
        md = cv2.dilate(m, np.ones((15, 15), np.uint8))
        bg = fill(frames[k], md).astype(np.float32)
        prog = (t - T0) / (TD * 0.7)
        alive = ((m > 0) & (dis > prog)).astype(np.float32)[..., None]
        alive = cv2.GaussianBlur(alive, (3, 3), 0)[..., None] if alive.ndim == 2 else alive
        img = bg * (1 - alive) + fr * alive
        dt = t - ta; act = dt > 0
        y = py + 0.5 * g * np.clip(dt, 0, None) ** 2; x = px + vx * np.clip(dt, 0, None)
        newl = act & ~landed & (y >= land_y)
        if newl.any():   # yerga tushganlar uyumga qo'shiladi (oyoq ostida, bir oz yoyilib)
            lx = np.clip((x[newl] + rng.normal(0, 9, newl.sum())).astype(int), 0, W - 1)
            ly = np.clip((land_y[newl] - rng.random(newl.sum()) * 4).astype(int), 0, H - 1)
            c = col[newl] * 0.2 + sand * 0.8
            np.add.at(pa, (ly, lx), 1); pile[ly, lx] = c
            landed |= newl
        fl = act & ~landed
        fx = np.clip(x[fl].astype(int), 0, W - 2); fy = np.clip(y[fl].astype(int), 0, H - 2)
        c = col[fl] * 0.35 + sand * 0.65
        img[fy, fx] = c; img[fy + 1, fx] = c * 0.9; img[fy, fx + 1] = c * 0.9
        # uyum: tushgan qum oyoq ostida yumshoq tepalik bo'lib o'sadi
        cnt = cv2.GaussianBlur(pa.sum(axis=0).astype(np.float32)[None, :], (0, 0), 10)[0]
        hgt = np.sqrt(cnt) * 7.0
        if hgt.max() > 1:
            ysurf = ground - hgt; inside = (yy >= ysurf[None, :]) & (yy <= ground + 4) & (hgt[None, :] > 1)
            shade = np.clip(0.75 + (ground - yy) / 120.0, 0.7, 1.05)[..., None]
            grain = rng.random((H, W, 1)) * 0.2 + 0.9
            hm = cv2.GaussianBlur(inside.astype(np.float32), (5, 5), 0)[..., None]
            img = img * (1 - hm) + (sand * shade * grain) * hm
    p.stdin.write(np.clip(img, 0, 255).astype(np.uint8).tobytes())
p.stdin.close(); p.wait()
