# Diyorning ko'k neon chizig'i (namunadagidek ingichka yorqin moviy kontur + yumshoq nur) — Veo tushirib qoldirganda o'zimiz chizamiz.
# 2-versiya (egasi, 2026-10-29: «bir xil kadrda Ustaga ham o'tib ketgan»): har kadrda
#   odam niqobi (u2net_human_seg) + yuzlar (YuNet) + kim ekani (SFace, ref_usta / ref_diyor bilan solishtiriladi)
#   + Diyorning to'q ko'k xudisi (rang) → watershed bilan Diyor va Usta ajratiladi; teshiklar to'ldiriladi, chegara silliqlanadi,
#   kadrlar orasida o'rtachalanadi (titramasin). Chiziq faqat tashqi konturda, Usta tegib turgan joyda chiziq yo'q.
# Ishlatish: python3 video/yetkazish/neon.py s01 s02 ...  → clips/sNN_n.mp4  (modellar ~/.u2net da)
import os, subprocess, sys, cv2, numpy as np, onnxruntime as ort
D = os.path.dirname(os.path.abspath(__file__)); C = os.path.join(D, "clips"); M = os.path.expanduser("~/.u2net")
SESS = ort.InferenceSession(f"{M}/u2net_human_seg.onnx", providers=["CPUExecutionProvider"]); INP = SESS.get_inputs()[0].name
DET = cv2.FaceDetectorYN.create(f"{M}/face_yunet.onnx", "", (720, 1280), 0.6)
REC = cv2.FaceRecognizerSF.create(f"{M}/face_sface.onnx", "")
# klip: (manba, Diyor bo'lishi mumkin bo'lgan hudud x0,y0,x1,y1 — 720×1280; None = butun kadr)
# s01: Diyor orqada, butun klip davomida xira — niqob ishonchsiz, chiziq chizilmaydi (egasi neon Ustaga o'tmasin dedi)
JOBS = {"s02": ("s02_y", (0, 0, 720, 1000)), "s03": ("s03", (0, 0, 300, 760)), "s07": ("s07", (0, 0, 720, 960)),
        "s11": ("s11", (0, 250, 370, 1000)), "s12": ("s12_y", (360, 60, 720, 800)), "s15": ("s15", (330, 300, 720, 1060))}
CYAN = np.float32([255, 225, 70])   # BGR

def human(f):
    x = cv2.resize(cv2.cvtColor(f, cv2.COLOR_BGR2RGB), (320, 320)).astype(np.float32) / 255
    x = ((x - [0.485, 0.456, 0.406]) / [0.229, 0.224, 0.225]).transpose(2, 0, 1)[None].astype(np.float32)
    m = SESS.run(None, {INP: x})[0][0, 0]; m = (m - m.min()) / (m.max() - m.min() + 1e-6)
    return cv2.resize(m, (f.shape[1], f.shape[0]))

def faces(f):
    DET.setInputSize((f.shape[1], f.shape[0])); _, fs = DET.detect(f)
    return [] if fs is None else list(fs)

def emb(f, face): return REC.feature(REC.alignCrop(f, face))
REF = {}
for k in ("usta", "diyor"):
    im = cv2.resize(cv2.imread(os.path.join(D, "img", f"ref_{k}.png")), (720, 1280)); fs = faces(im)
    REF[k] = emb(im, max(fs, key=lambda z: z[2] * z[3]))
def who(f, face):
    e = emb(f, face); su = REC.match(e, REF["usta"], cv2.FaceRecognizerSF_FR_COSINE); sd = REC.match(e, REF["diyor"], cv2.FaceRecognizerSF_FR_COSINE)
    # soqol: yuzning pastki qismi yuqorisiga qaraganda ancha qorong'i bo'lsa — Usta
    x, y, w, h = map(int, face[:4]); g = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
    lo = g[max(0, y + int(0.7 * h)):y + h, max(0, x):x + w].mean() if h > 10 else 0; up = g[max(0, y + int(0.3 * h)):y + int(0.55 * h), max(0, x):x + w].mean() if h > 10 else 1
    beard = lo < 0.75 * up
    return "usta" if (su - sd) + (0.15 if beard else -0.15) > 0 else "diyor"

def box(face, s=1.0):
    x, y, w, h = face[:4]; cx, cy = x + w / 2, y + h / 2
    return int(cx - w * s / 2), int(cy - h * s / 2), int(cx + w * s / 2), int(cy + h * s / 2)

def segment(f, hm, prev, roi):
    H, W = hm.shape; hb = (hm > 0.5).astype(np.uint8); k9 = np.ones((9, 9), np.uint8)
    hsv = cv2.cvtColor(f, cv2.COLOR_BGR2HSV)
    navy = (cv2.inRange(hsv, (100, 60, 25), (130, 255, 170)) > 0) & (hb > 0) & (roi > 0)
    mk = np.zeros((H, W), np.int32); mk[cv2.erode(1 - hb, k9) > 0] = 1
    mk[(cv2.erode(hb, k9) > 0) & (cv2.dilate(roi, np.ones((41, 41), np.uint8)) == 0)] = 3   # hududdan tashqaridagi odam — Diyor emas
    fs = faces(f); roles = [(who(f, z), z) for z in fs if z[2] > 25]
    has_u = False
    for r, z in roles:
        x0, y0, x1, y1 = box(z, 0.8)
        if r == "usta":
            has_u = True; mk[max(0, y0):y1, max(0, x0):x1] = 3
            bx0, by0, bx1, by1 = box(z, 1.0)   # Usta tanasi: yuz ostidagi to'q-ko'k bo'lmagan odam piksellari
            band = np.zeros((H, W), bool); band[by1:min(H, by1 + int(4 * (by1 - by0))), max(0, bx0 - int(0.6 * (bx1 - bx0))):bx1 + int(0.6 * (bx1 - bx0))] = True
            mk[band & (hb > 0) & ~navy & (cv2.erode(hb, k9) > 0)] = 3
        elif roi[int(min(H - 1, z[1] + z[3] / 2)), int(min(W - 1, z[0] + z[2] / 2))]:
            mk[max(0, y0):y1, max(0, x0):x1] = 2
    nv = cv2.morphologyEx(navy.astype(np.uint8), cv2.MORPH_OPEN, np.ones((7, 7), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(nv)
    for j in range(1, n):
        if st[j][4] > 1500: mk[(lab == j) & (mk != 3)] = 2
    if prev is not None:   # oldingi kadrdagi Diyor ichki qismi ham urug'
        core = cv2.erode((prev > 0.5).astype(np.uint8), np.ones((25, 25), np.uint8)) > 0
        mk[core & (mk == 0) & (hb > 0)] = 2
    if not (mk == 2).any(): return np.zeros((H, W), np.float32), np.zeros((H, W), np.uint8)
    if not has_u and not (mk == 3).any():   # Diyor yolg'iz — butun odam
        m = hb.astype(np.float32); return m, np.zeros((H, W), np.uint8)
    cv2.watershed(f, mk)
    dm = ((mk == 2) & (hb > 0) & (cv2.dilate(roi, np.ones((41, 41), np.uint8)) > 0)).astype(np.uint8); um = ((mk == 3) & (hb > 0)).astype(np.uint8)
    n, lab, st, _ = cv2.connectedComponentsWithStats(dm)   # faqat katta bo'laklar, teshiklar to'ldiriladi
    keep = np.zeros_like(dm)
    for j in range(1, n):
        if st[j][4] > 2000: keep[lab == j] = 1
    cs, _ = cv2.findContours(keep, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE); keep = np.zeros_like(keep); cv2.drawContours(keep, cs, -1, 1, -1)
    keep = (cv2.GaussianBlur(keep.astype(np.float32), (51, 51), 0) > 0.5).astype(np.uint8)   # siniq chegara silliqlanadi
    return keep.astype(np.float32), um

def solidity(m):
    mb = (m > 0.5).astype(np.uint8); cs, _ = cv2.findContours(mb, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not cs: return 0.0
    c = max(cs, key=cv2.contourArea); h = cv2.contourArea(cv2.convexHull(c))
    return cv2.contourArea(c) / h if h else 0.0

def glow(f, m, um, hm=None, k=1.0):
    H, W = m.shape; mb = (m > 0.5).astype(np.uint8)
    soft = cv2.GaussianBlur(mb.astype(np.float32), (7, 7), 0)
    core = np.clip(cv2.GaussianBlur(cv2.dilate(mb, np.ones((5, 5), np.uint8)).astype(np.float32), (5, 5), 0) - soft, 0, 1)
    halo = cv2.GaussianBlur(np.clip(cv2.dilate(mb, np.ones((17, 17), np.uint8)).astype(np.float32) - soft, 0, 1), (31, 31), 0)
    edge = np.ones((H, W), np.float32); edge[:4] = edge[-4:] = 0; edge[:, :4] = edge[:, -4:] = 0
    edge = cv2.GaussianBlur(edge, (9, 9), 0)
    if um.any():   # Usta ustida va unga tegib turgan joyda chiziq yo'q
        edge *= 1 - cv2.GaussianBlur(cv2.dilate(um, np.ones((21, 21), np.uint8)).astype(np.float32), (21, 21), 0)
    if hm is not None:   # chiziq faqat Diyor bilan fon chegarasida (ichki siniq chiziqlar, stol/odam chegarasida yo'q)
        bg = (hm < 0.3).astype(np.uint8)
        edge *= cv2.GaussianBlur(cv2.dilate(bg, np.ones((15, 15), np.uint8)).astype(np.float32), (15, 15), 0)
    a = ((core * 1.6 + halo * 0.55) * edge * k)[..., None]
    return np.clip(f.astype(np.float32) + a * CYAN * 0.85, 0, 255).astype(np.uint8)

for name in (sys.argv[1:] or JOBS):
    src, rb = JOBS[name]
    roi = np.ones((1280, 720), np.uint8)
    if rb: roi[:] = 0; roi[rb[1]:rb[3], rb[0]:rb[2]] = 1
    c = cv2.VideoCapture(os.path.join(C, src + ".mp4")); fps = c.get(cv2.CAP_PROP_FPS); W, H = int(c.get(3)), int(c.get(4))
    tmp = os.path.join(C, name + "_n_tmp.mp4"); w = cv2.VideoWriter(tmp, cv2.VideoWriter_fourcc(*"mp4v"), fps, (W, H))
    prev = None; kk = 1.0
    while True:
        ok, f = c.read()
        if not ok: break
        hm = human(f); m, um = segment(f, hm, prev, roi)
        if prev is not None:
            if m.sum() < 0.4 * prev.sum(): m = prev * 0.9   # bir kadrda yo'qolib qolsa — oldingisi
            m = 0.35 * m + 0.65 * prev                        # titramasin
        um = um | ((hm > 0.5) & (roi == 0)).astype(np.uint8)
        m = m * cv2.dilate(roi, np.ones((41, 41), np.uint8)).astype(np.float32)
        # Diyor xira (fokusdan tashqari) bo'lsa niqob yuzini kesib o'tadi — shakl notekis bo'lsa chiziq so'nadi
        tgt = 0.0   # Diyor yuzi topilmasa (xira yoki orqasi bilan) — chiziq yo'q
        for z in faces(f):   # Diyor yuzi niqob ichida bo'lmasa (xira kadr, niqob yuzni kesib o'tgan) — chiziq so'nadi
            x0, y0, x1, y1 = box(z, 0.9); cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
            if z[2] < 25 or not roi[min(H - 1, max(0, cy)), min(W - 1, max(0, cx))] or who(f, z) != "diyor": continue
            fr = (m[max(0, y0):y1, max(0, x0):x1] > 0.5).mean() if y1 > y0 and x1 > x0 else 0
            tgt = float(np.clip((fr - 0.7) / 0.2, 0, 1)); break
        kk = 0.7 * kk + 0.3 * tgt
        w.write(glow(f, m, um, hm, kk)); prev = m
    w.release()
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", os.path.join(C, name + "_n.mp4")], check=True)
    os.remove(tmp); print(name, "→", name + "_n.mp4")
