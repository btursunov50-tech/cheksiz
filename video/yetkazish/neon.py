# Diyorning ko'k neon chizig'ini (namunadagidek: ingichka yorqin moviy chiziq + yumshoq nur) kliplarga o'zimiz chizamiz — Veo uni tushirib qoldiradi.
# Odam niqobi: u2net_human_seg (~/.u2net, onnxruntime). Diyor 1-kadrdagi qutidan topiladi, keyin har kadrda optik oqim + watershed bilan
# kuzatiladi (Usta bilan tegib tursa ham ajraladi). Ishlatish: python3 video/yetkazish/neon.py s02 s07 ...  → clips/sNN_n.mp4
import os, subprocess, sys, cv2, numpy as np, onnxruntime as ort
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "clips")
SESS = ort.InferenceSession(os.path.expanduser("~/.u2net/u2net_human_seg.onnx"), providers=["CPUExecutionProvider"])
INP = SESS.get_inputs()[0].name
# klip: (manba, aniq Diyor turgan ichki quti, Diyor bo'lishi mumkin bo'lgan hudud) — 720×1280, 1-kadr bo'yicha
JOBS = {
    "s01": ("s01_y", (480, 450, 680, 700), (380, 350, 720, 880)),
    "s02": ("s02_y", (250, 150, 600, 700), (0, 0, 720, 960)),
    "s03": ("s03", (0, 100, 200, 900), (0, 0, 330, 1280)),
    "s07": ("s07", (150, 200, 600, 1100), (0, 0, 720, 1280)),
    "s11": ("s11", (60, 300, 300, 700), (0, 150, 390, 900)),
    "s12": ("s12", (520, 250, 700, 650), (430, 120, 720, 800)),
}
CYAN = np.float32([255, 225, 70])   # BGR

def human(f):
    x = cv2.resize(cv2.cvtColor(f, cv2.COLOR_BGR2RGB), (320, 320)).astype(np.float32) / 255
    x = ((x - [0.485, 0.456, 0.406]) / [0.229, 0.224, 0.225]).transpose(2, 0, 1)[None].astype(np.float32)
    m = SESS.run(None, {INP: x})[0][0, 0]
    m = (m - m.min()) / (m.max() - m.min() + 1e-6)
    return cv2.resize(m, (f.shape[1], f.shape[0]))

def box(b, H=1280, W=720):
    r = np.zeros((H, W), np.uint8); x0, y0, x1, y1 = b; r[y0:y1, x0:x1] = 1; return r

def seg(f, hm, sure, roi):
    # watershed: 1 = fon, 2 = Diyor (aniq), 3 = boshqa odam / Diyor hududidan tashqari
    hb = (hm > 0.5).astype(np.uint8); k = np.ones((9, 9), np.uint8)
    mk = np.zeros(hb.shape, np.int32)
    mk[cv2.erode(1 - hb, k) > 0] = 1
    mk[cv2.erode(hb & (1 - roi), k) > 0] = 3
    mk[(cv2.erode(sure, k) > 0) & (hb > 0)] = 2
    cv2.watershed(f, mk)
    return ((mk == 2) & (hb > 0) & (roi > 0)).astype(np.uint8)

def warp(prev, prev_g, g):
    flow = cv2.calcOpticalFlowFarneback(g, prev_g, None, 0.5, 3, 25, 3, 5, 1.2, 0)
    H, W = g.shape; gx, gy = np.meshgrid(np.arange(W), np.arange(H))
    return cv2.remap(prev, (gx + flow[..., 0]).astype(np.float32), (gy + flow[..., 1]).astype(np.float32), cv2.INTER_NEAREST)

def glow(f, m, hm=None, roi=None):
    H, W = m.shape
    soft = cv2.GaussianBlur(m.astype(np.float32), (7, 7), 0)
    core = np.clip(cv2.GaussianBlur(cv2.dilate(m, np.ones((5, 5), np.uint8)).astype(np.float32), (5, 5), 0) - soft, 0, 1)
    halo = cv2.GaussianBlur(np.clip(cv2.dilate(m, np.ones((17, 17), np.uint8)).astype(np.float32) - soft, 0, 1), (31, 31), 0)
    edge = np.ones((H, W), np.float32); edge[:4] = edge[-4:] = 0; edge[:, :4] = edge[:, -4:] = 0   # kadr chetida chiziq yo'q
    edge = cv2.GaussianBlur(edge, (9, 9), 0)
    if hm is not None:   # boshqa odam yoki Diyor hududi chegarasiga tegadigan joyda chiziq yo'q (Usta ustida, gilamda to'g'ri chiziq bo'lmasin)
        far = ((hm > 0.5) & (cv2.dilate(m, np.ones((25, 25), np.uint8)) == 0)).astype(np.uint8)   # boshqa odam (Diyordan uzoqdagi odam piksellari)
        far = cv2.morphologyEx(far, cv2.MORPH_OPEN, np.ones((15, 15), np.uint8))
        other = cv2.dilate(far, np.ones((31, 31), np.uint8))
        edge *= 1 - cv2.GaussianBlur(other.astype(np.float32), (15, 15), 0)
    if roi is not None:
        edge *= cv2.GaussianBlur(cv2.erode(roi, np.ones((41, 41), np.uint8)).astype(np.float32), (21, 21), 0)
    a = ((core * 1.6 + halo * 0.55) * edge)[..., None]
    out = f.astype(np.float32) + a * CYAN * 0.85
    return np.clip(out, 0, 255).astype(np.uint8)

for name in (sys.argv[1:] or JOBS):
    src, inner, area = JOBS[name]; roi = box(area)
    c = cv2.VideoCapture(os.path.join(D, src + ".mp4")); fps = c.get(cv2.CAP_PROP_FPS); W, H = int(c.get(3)), int(c.get(4))
    tmp = os.path.join(D, name + "_n_tmp.mp4"); w = cv2.VideoWriter(tmp, cv2.VideoWriter_fourcc(*"mp4v"), fps, (W, H))
    prev = prev_g = None
    while True:
        ok, f = c.read()
        if not ok: break
        hm = human(f); g = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
        sure = box(inner) if prev is None else warp(prev, prev_g, g)
        m = seg(f, hm, sure, roi)
        if prev is not None and m.sum() < 0.5 * prev.sum(): m = warp(prev, prev_g, g)
        w.write(glow(f, m, hm, roi)); prev, prev_g = m, g
    w.release()
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", os.path.join(D, name + "_n.mp4")], check=True)
    os.remove(tmp); print(name, "→", name + "_n.mp4")
