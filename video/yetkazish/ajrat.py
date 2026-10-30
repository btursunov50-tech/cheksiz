# Ovozni (ElevenLabs/Narakeet, 2 fayl: Usta 14 gap, Diyor 4 gap) gaplarga ajratib, video tartibida voice/NN_kim.wav qiladi.
# Gap chegaralari: pauzalar + bo'g'in soni (al.py usuli, 2026-10-29). Gap ichidagi 0.45 s dan uzun pauzalar 0.35 s ga qisqartiriladi.
# Ishlatish: python3 video/yetkazish/ajrat.py <usta.wav> <diyor.wav>
import os, re, subprocess, sys, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); V = os.path.join(D, "voice"); os.makedirs(V, exist_ok=True)
for f in os.listdir(V): os.remove(os.path.join(V, f))
USTA, DIYOR = sys.argv[1], sys.argv[2]
# (fayl, boshi, oxiri) — al.py hisobi (Usta) va pauzalar (Diyor)
U = [(0.0, 4.98), (6.13, 8.03), (9.14, 14.18), (15.03, 30.82), (31.7, 42.17), (42.99, 52.77), (53.79, 57.93), (58.77, 69.93),
     (71.1, 73.64), (74.36, 79.01), (80.17, 93.27), (94.34, 102.17), (103.09, 117.96), (119.03, 126.16)]
Dy = [(0.21, 4.37), (4.63, 6.32), (6.65, 9.11), (9.34, 10.68)]
ORDER = ["u1", "d1", "u2", "d2", "u3", "u4", "u5", "d3", "u6", "u7", "u8", "d4", "u9", "u10", "u11", "u12", "u13", "u14"]
def load(f):
    a = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-f", "f32le", "-ac", "1", "-ar", "48000", "-"], capture_output=True).stdout
    return np.frombuffer(a, np.float32).copy()
SR = 48000; A = {"u": load(USTA), "d": load(DIYOR)}
def squeeze(x):
    fr = 480; e = np.sqrt(np.convolve(x ** 2, np.ones(fr) / fr, "same")); sil = e < 10 ** (-40 / 20)
    out, i, n = [], 0, len(x)
    while i < n:
        if sil[i]:
            j = i
            while j < n and sil[j]: j += 1
            keep = min(j - i, int(0.35 * SR)) if 0 < i and j < n else 0   # boshidagi/oxiridagi jimlik olib tashlanadi
            out.append(x[i:i + keep]); i = j
        else:
            j = i
            while j < n and not sil[j]: j += 1
            out.append(x[i:j]); i = j
    return np.concatenate(out)
for k, key in enumerate(ORDER, 1):
    who, idx = key[0], int(key[1:]) - 1
    a, b = (U if who == "u" else Dy)[idx]
    x = squeeze(A[who][int(a * SR):int(b * SR)])
    name = os.path.join(V, f"{k:02}_{'usta' if who == 'u' else 'diyor'}.wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", name], input=x.tobytes(), check=True)
    print(k, key, round(len(x) / SR, 2))
