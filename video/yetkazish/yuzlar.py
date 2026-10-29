# Yuz tekshiruvi: har klipdan 0.5 s da bir kadr olinadi, yuzlar (YuNet, ~/.u2net/face_yunet.onnx) qirqiladi va namuna yuzlar bilan
# bitta varaqqa yig'iladi: chapda ref_usta / ref_diyor, keyin vaqt bo'yicha yuzlar. Ishlatish: python3 video/yetkazish/yuzlar.py s01 s02 ... → <out>/yuz_sNN.jpg
import os, sys, cv2, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); C = os.path.join(D, "clips")
OUT = sys.argv[1]; NAMES = sys.argv[2:]
det = cv2.FaceDetectorYN.create(os.path.expanduser("~/.u2net/face_yunet.onnx"), "", (720, 1280), 0.5)
def crops(img, n=3):
    det.setInputSize((img.shape[1], img.shape[0])); _, fs = det.detect(img)
    out = []
    for f in (fs if fs is not None else [])[:n]:
        x, y, w, h = map(int, f[:4]); p = int(0.35 * h)
        c = img[max(0, y - p):y + h + p // 2, max(0, x - p // 2):x + w + p // 2]
        if c.size: out.append(cv2.resize(c, (int(c.shape[1] * 150 / c.shape[0]), 150)))
    return out
refs = []
for r in ("ref_usta", "ref_diyor"):
    im = cv2.imread(os.path.join(D, "img", r + ".png")); refs += crops(cv2.resize(im, (720, 1280)), 1)
for name in NAMES:
    cap = cv2.VideoCapture(os.path.join(C, name + ".mp4")); fps = cap.get(cv2.CAP_PROP_FPS); i = 0; row = list(refs) + [np.full((150, 12, 3), 255, np.uint8)]
    while True:
        ok, f = cap.read()
        if not ok: break
        if i % int(fps / 2) == 0:
            cs = crops(f)
            if cs:
                lab = np.zeros((150, 36, 3), np.uint8); cv2.putText(lab, f"{i / fps:.1f}", (1, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 255), 1)
                row += [lab] + cs
        i += 1
    lines, cur, w = [], [], 0
    for im in row:
        if w + im.shape[1] > 2000 and cur: lines.append(cur); cur, w = [], 0
        cur.append(im); w += im.shape[1]
    lines.append(cur)
    sheet = np.vstack([np.hstack(l + [np.zeros((150, 2000 - sum(i.shape[1] for i in l), 3), np.uint8)]) for l in lines])
    cv2.imwrite(os.path.join(OUT, f"yuz_{name}.jpg"), sheet); print(name, sheet.shape)
