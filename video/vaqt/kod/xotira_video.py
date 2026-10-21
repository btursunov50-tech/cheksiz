# Veo xotira klipi → oltin xotira: oltin rang (duotone), porlash, vinyetka; boshida konturlar yonib so'nadi,
# oxirida kadr yuqoridan qumga aylanib to'kiladi.  python3 xotira_video.py KIRISH.mp4 CHIQISH.mp4 BOSHI DAVOMI
import cv2, numpy as np, sys, subprocess, os, tempfile
src, out, t0, D = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4])
cap = cv2.VideoCapture(src); F = cap.get(cv2.CAP_PROP_FPS) or 24
cap.set(cv2.CAP_PROP_POS_MSEC, t0 * 1000)
W, H = 720, 1280
dark = np.array([10, 18, 32]) / 255; gold = np.array([90, 200, 255]) / 255; light = np.array([200, 240, 255]) / 255
yy, xx = np.mgrid[:H, :W]
vig = (0.35 + 0.65 * (1 - np.clip(((xx - W / 2) / (W * 0.75)) ** 2 + ((yy - H / 2) / (H * 0.7)) ** 2, 0, 1)))[..., None]
rng = np.random.default_rng(7)
noise = cv2.GaussianBlur(rng.random((H, W)).astype(np.float32), (0, 0), 6); noise = (noise - noise.min()) / (noise.max() - noise.min())
dis = 0.55 * noise + 0.45 * (yy / H)                      # qumga aylanish tartibi: yuqoridan, dog'-dog'
P = 60000; pi = rng.integers(0, H * W, P); py, px = pi // W, pi % W; pd = dis[py, px]; pv = rng.random(P)
E = lambda u: float(np.clip(u, 0, 1)) ** 2 * (3 - 2 * float(np.clip(u, 0, 1)))
tmp = tempfile.mkdtemp(); n = int(D * F); DS = 1.2           # oxirgi 1.2 s qumga aylanadi
for k in range(n):
    ok, fr = cap.read()
    if not ok: break
    t = k / F
    im = cv2.resize(fr, (W, H)).astype(np.float32) / 255
    g = cv2.cvtColor((im * 255).astype(np.uint8), cv2.COLOR_BGR2GRAY).astype(np.float32) / 255
    g = np.clip((g - 0.05) * 1.25, 0, 1) ** 0.9
    duo = np.where(g[..., None] < 0.6, dark + (gold - dark) * (g[..., None] / 0.6), gold + (light - gold) * ((g[..., None] - 0.6) / 0.4)) * 0.85
    duo = duo + np.clip(cv2.GaussianBlur(duo, (0, 0), 18) - 0.45, 0, 1) * 0.8
    duo *= vig
    a_in = E(t / 0.5)                                       # 0.5 s da qorong'idan ochiladi, konturlar yonib so'nadi
    if t < 1.0:
        e = cv2.Canny(cv2.GaussianBlur((g * 255).astype(np.uint8), (0, 0), 3), 30, 70).astype(np.float32) / 255
        glow = cv2.GaussianBlur(e, (0, 0), 4) * 1.3
        duo = duo * a_in + (e[..., None] * light + glow[..., None] * gold) * (1 - E(t / 1.0))
    dz = E((t - (D - DS)) / DS)
    if dz > 0:
        alive = (dis > dz * 1.05).astype(np.float32)[..., None]
        duo = duo * alive
        tt = np.clip((t - (D - DS)) - pd * DS, 0, None)
        sx = (px + np.sin(pv * 20 + t * 3) * 10 * tt).astype(int); sy = (py + (120 + 260 * pv) * tt * tt * 1.6 + 30 * tt).astype(int)
        m = (pd < dz * 1.05) & (sx >= 0) & (sx < W - 1) & (sy >= 0) & (sy < H - 1) & (tt < 2)
        c = im[py[m], px[m]] * 0 + gold * 1.1
        duo[sy[m], sx[m]] = np.maximum(duo[sy[m], sx[m]], c); duo[sy[m] + 1, sx[m]] = np.maximum(duo[sy[m] + 1, sx[m]], c * 0.8)
    duo += (rng.random((H, W, 1)) - 0.5) * 0.035
    cv2.imwrite(f"{tmp}/{k:04d}.jpg", (np.clip(duo, 0, 1) * 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 92])
subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(F), "-i", f"{tmp}/%04d.jpg", "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", out], check=True)
