"""13-sahna: Veo telefon ekraniga «Usta» yozuvi va oddiy qo'ng'iroq chizdi. Ekran ichini toza kadr (4.8 s) bilan almashtiradi,
telefon siljishini ekran atrofidagi (qo'l + ramka) halqa bo'yicha kuzatadi. Ishlatish: python3 telefon_yoz.py kirish.mp4 chiqish.mp4"""
import cv2, numpy as np, subprocess, sys
src, dst = sys.argv[1], sys.argv[2]
REF_T, END_T = 4.8, 4.3
SX0, SY0, SX1, SY1 = 120, 590, 205, 802      # ekran ichi (to'liq o'lchamda)
RX0, RY0, RX1, RY1 = 95, 565, 235, 835       # kuzatish oynasi (ekran + ramka + qo'l)
cap = cv2.VideoCapture(src); fps = cap.get(cv2.CAP_PROP_FPS)
fr = []
while True:
    ok, f = cap.read()
    if not ok: break
    fr.append(f)
ref = fr[int(REF_T * fps)]
def ring(f):
    g = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY).astype(np.float32)[RY0:RY1, RX0:RX1]
    g = cv2.GaussianBlur(g, (3, 3), 0)
    g[SY0 - RY0 - 6:SY1 - RY0 + 6, SX0 - RX0 - 6:SX1 - RX0 + 6] = g.mean()   # ekran ichi hisobga olinmaydi
    return g * np.outer(np.hanning(g.shape[0]), np.hanning(g.shape[1])).astype(np.float32)
rr = ring(ref)
mask = np.zeros(ref.shape[:2], np.float32); mask[SY0:SY1, SX0:SX1] = 1
mask = cv2.GaussianBlur(mask, (0, 0), 3)[..., None]
out = []
for i, f in enumerate(fr):
    t = i / fps
    if t < END_T:
        (dx, dy), _ = cv2.phaseCorrelate(rr, ring(f))
        M = np.float32([[1, 0, dx], [0, 1, dy]])
        w = cv2.warpAffine(ref, M, (f.shape[1], f.shape[0]), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
        mk = cv2.warpAffine(mask, M, (f.shape[1], f.shape[0]))[..., None] if mask.ndim == 2 else cv2.warpAffine(mask[..., 0], M, (f.shape[1], f.shape[0]))[..., None]
        f = (f * (1 - mk) + w * mk).astype(np.uint8)
    out.append(f)
h, w_ = out[0].shape[:2]
p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{w_}x{h}", "-r", str(fps), "-i", "-",
                      "-i", src, "-map", "0:v", "-map", "1:a?", "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", "-c:a", "copy", "-shortest", dst], stdin=subprocess.PIPE)
for f in out: p.stdin.write(f.tobytes())
p.stdin.close(); p.wait(); print("tayyor", dst, len(out), "kadr")
