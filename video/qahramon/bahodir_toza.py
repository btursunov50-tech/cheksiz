# Bahodir kadridan (jalolov_dacres.mp4, 3.9–6.3 s) siljuvchi «@OPER_UZ» belgisini o'chiradi (egasi, 2026-10-22: "yozuv qolmasin").
# Belgi har kadrda 2.4 px tepaga siljiydi: o'rni matchTemplate bilan topiladi, joyi 22 kadr narigi (belgi boshqa joyda turgan)
# kadrdan, phaseCorrelate bilan tekislab olinadi. Ishlatish: python3 bahodir_toza.py KADRLAR_DIR TEMPLATE_POS.npy OUT_DIR
import cv2, numpy as np, glob, sys
src, posf, out = sys.argv[1:4]
fs = sorted(glob.glob(src + '/*.png')); F = [cv2.imread(p).astype(np.float32) for p in fs]; n = len(F)
P = np.load(posf); ys = P[:, 2].copy(); k = np.polyfit(np.arange(40, 58), ys[40:58], 1)
for i in range(58, n): ys[i] = np.polyval(k, i)   # oxirida belgi xiralashadi — chiziqli davom
x0, w, h, pad, D = 216, 212, 36, 6, 22
def g(a): return cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
for i in range(n):
    y = int(round(ys[i])); j = i + D if i < D else i - D; yj = int(round(ys[j]))
    r0, r1 = max(0, y - 110), min(640, y + 150)
    A, B = g(F[i]).copy(), g(F[j]).copy()
    for Z in (A, B):
        for yy in (y, yj): Z[max(0, yy - pad):yy + h + pad, x0 - pad:x0 + w + pad] = np.nan
    A, B = A[r0:r1, 120:560], B[r0:r1, 120:560]; A = np.nan_to_num(A, nan=np.nanmean(A)); B = np.nan_to_num(B, nan=np.nanmean(B))
    (dx, dy), _ = cv2.phaseCorrelate(B.astype(np.float32), A.astype(np.float32), cv2.createHanningWindow(A.shape[::-1], cv2.CV_32F))
    Wj = cv2.warpAffine(F[j], np.float32([[1, 0, dx], [0, 1, dy]]), (640, 640), borderMode=cv2.BORDER_REFLECT)
    M = np.zeros(F[i].shape[:2], np.float32); M[max(0, y - pad):y + h + pad, x0 - pad:x0 + w + pad] = 1
    M = cv2.GaussianBlur(M, (0, 0), 4)[..., None]
    cv2.imwrite(out + '/%04d.png' % (i + 1), (F[i] * (1 - M) + Wj * M).clip(0, 255).astype(np.uint8))
