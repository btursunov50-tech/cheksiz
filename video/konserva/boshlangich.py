# Konserva: rad etilgan Veo klipining kadridan toza BOSHLANG'ICH RASM yasaydi (yozuv, odam, yorliq olib tashlanadi, fon xira bokeh bo'ladi).
# Veo'ga «Frames to video» da shu rasm birinchi kadr qilib beriladi, shunda u boshqa joy chizmaydi. Ishlatish: python3 boshlangich.py <raw klip papkasi>
import cv2, numpy as np, onnxruntime as ort, subprocess, sys, os
RAW = sys.argv[1]; D = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(D, "img"); os.makedirs(OUT, exist_ok=True)
sess = ort.InferenceSession(os.path.expanduser("~/.u2net/isnet-general-use.onnx"), providers=["CPUExecutionProvider"])
def frame(clip, t):
    p = f"/tmp/_f_{clip}.png"; subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", os.path.join(RAW, clip + ".mp4"), "-frames:v", "1", p], check=True); return cv2.imread(p)
def mask(img):
    x = cv2.resize(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), (1024, 1024)).astype(np.float32) / 255.0
    x = (x - 0.5)[None].transpose(0, 3, 1, 2).astype(np.float32)
    m = sess.run(None, {sess.get_inputs()[0].name: x})[0][0, 0]; m = (m - m.min()) / (m.max() - m.min() + 1e-6)
    return cv2.resize(m, (img.shape[1], img.shape[0]))
def bokeh(img, keep, sigma=28):
    bg = cv2.GaussianBlur(img, (0, 0), sigma); k = cv2.GaussianBlur(keep.astype(np.float32), (0, 0), 3)[..., None]
    return (img * k + bg * (1 - k)).astype(np.uint8)
def rect(h, w, x0, y0, x1, y1):
    m = np.zeros((h, w), np.float32); m[y0:y1, x0:x1] = 1; return m
# 4: banka + ochilgan yorliq, fon xira
im = frame("s04", 0.2); h, w = im.shape[:2]
gear = np.zeros((h, w), np.uint8); cv2.circle(gear, (384, 624), 62, 255, -1); im = cv2.inpaint(im, gear, 12, cv2.INPAINT_TELEA)
k = (mask(im) > 0.5).astype(np.float32)
k[:200, :] = 0
cv2.imwrite(os.path.join(OUT, "s04.png"), bokeh(im, np.maximum(k, rect(*im.shape[:2], 0, 880, 720, 1280))))
# 5: banka yolg'iz (belgi va olov o'chiriladi), fon xira
im = frame("s05", 3.5); h, w = im.shape[:2]
sym = np.zeros((h, w), np.uint8); cv2.circle(sym, (360, 330), 205, 255, -1)
clean = cv2.inpaint(im, sym, 25, cv2.INPAINT_TELEA)
k = (mask(clean) > 0.5).astype(np.float32); k[:600, :] = 0
cv2.imwrite(os.path.join(OUT, "s05.png"), bokeh(clean, np.maximum(k, rect(h, w, 0, 1000, 720, 1280))))
# 8: yorliqsiz oddiy kumush banka, fon xira (yorliq o'rni yuqori va pastki qatordagi rangdan vertikal silliq to'ldiriladi)
im = frame("s08", 0.3); h, w = im.shape[:2]
y0, y1, x0, x1 = 800, 1095, 255, 535
top = im[y0 - 6:y0 - 2, x0:x1].mean(axis=0); bot = im[y1 + 2:y1 + 6, x0:x1].mean(axis=0)
for y in range(y0, y1):
    a_ = (y - y0) / (y1 - y0); im[y, x0:x1] = (top * (1 - a_) + bot * a_).astype(np.uint8)
im[y0:y1, x0:x1] = cv2.GaussianBlur(im[y0:y1, x0:x1], (0, 0), 6)
k = (mask(im) > 0.4).astype(np.float32); k[:700, :] = 0
k = np.maximum(k, rect(h, w, 0, 1010, 720, 1280))
cv2.imwrite(os.path.join(OUT, "s08.png"), bokeh(im, k, 30))
# 9b: ikki stakan sut, fon xira (stakan kontur maskasi)
im = frame("s09b", 1.2); h, w = im.shape[:2]
k = (mask(im) > 0.45).astype(np.float32)
box = np.maximum(rect(h, w, 125, 550, 362, 1195), rect(h, w, 405, 550, 665, 1195)); k = np.minimum(np.maximum(k, 0), box)
k = np.maximum(k, rect(h, w, 0, 1000, 720, 1280)); k[560:1000, 362:405] = 0
cv2.imwrite(os.path.join(OUT, "s09b.png"), bokeh(im, k, 30))
print("tayyor", os.listdir(OUT))
