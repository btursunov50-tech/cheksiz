# eskirish_dialog.wav (Manus, bitta fayl) → voice/NN_kim.wav: 1000 Hz BIP signallari bo'yicha 21 qatorga ajratadi, chetdagi jimlikni kesadi.
# Ishlatish: python3 video/eskirish/ajrat.py
import os, subprocess, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); SRC = os.path.join(D, "eskirish_dialog.wav"); sr = 48000
x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", SRC, "-ac", "1", "-ar", str(sr), "-f", "f32le", "-"], capture_output=True).stdout, np.float32)
win, hop = 2400, 480; ref = np.exp(-2j * np.pi * 1000 * np.arange(win) / sr)
tone = []
for i in range(0, len(x) - win, hop):
    w = x[i:i + win]; e = np.sqrt((w ** 2).mean()) + 1e-9
    tone.append(e > 0.01 and abs((w * ref).sum()) / win * 2 / (e * 1.414) > 0.85)
beeps, prev = [], False
for k, t in enumerate(tone):
    if t and not prev: s = k * hop
    if not t and prev: beeps.append((s, k * hop + win))
    prev = t
WHO = {2: "diyor", 4: "diyor", 8: "diyor", 10: "diyor", 14: "diyor", 16: "diyor"}
edges = [0] + [b for a in beeps for b in a] + [len(x)]
segs = [(edges[2 * i], edges[2 * i + 1]) for i in range(len(beeps) + 1)]
env = np.convolve(np.abs(x), np.ones(480) / 480, "same")
out = []
for n, (a, b) in enumerate(segs, 1):
    v = np.where(env[a:b] > 0.004)[0]
    a2, b2 = a + max(0, v[0] - 2400), a + min(b - a, v[-1] + 4800)
    f = os.path.join(D, "voice", f"{n:02}_{WHO.get(n, 'usta')}.wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", SRC, "-af", f"atrim=start_sample={a2}:end_sample={b2},asetpts=PTS-STARTPTS", f], check=True)
    out.append((n, round((b2 - a2) / sr, 2)))
print(len(beeps), "signal;", out)
