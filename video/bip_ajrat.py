# Manus ovozi (bitta WAV, qatorlar orasida 1000 Hz BIP) → <loyiha>/voice/NN_kim.wav; har qatorning o'rtacha ovoz balandligi (Hz) ham chiqadi.
# Ishlatish: python3 video/bip_ajrat.py <wav> <voice papka> <diyor qatorlari, vergul bilan>
import os, sys, subprocess, numpy as np
SRC, OUT, DY = sys.argv[1], sys.argv[2], {int(k) for k in sys.argv[3].split(",") if k}
os.makedirs(OUT, exist_ok=True)
for f in os.listdir(OUT): os.remove(os.path.join(OUT, f))
sr = 48000
x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", SRC, "-ac", "1", "-ar", str(sr), "-f", "f32le", "-"], capture_output=True).stdout, np.float32)
win, hop = 2400, 480; ref = np.exp(-2j * np.pi * 1000 * np.arange(win) / sr); tone = []
for i in range(0, len(x) - win, hop):
    w = x[i:i + win]; e = np.sqrt((w ** 2).mean()) + 1e-9
    tone.append(e > 0.01 and abs((w * ref).sum()) / win * 2 / (e * 1.414) > 0.85)
beeps, prev = [], False
for k, t in enumerate(tone):
    if t and not prev: s = k * hop
    if not t and prev: beeps.append((s, k * hop + win))
    prev = t
edges = [0] + [b for a in beeps for b in a] + [len(x)]
segs = [(edges[2 * i], edges[2 * i + 1]) for i in range(len(beeps) + 1)]
env = np.convolve(np.abs(x), np.ones(480) / 480, "same")
def pitch(y):
    y = y[::3]; r = sr // 3; ps = []
    for i in range(0, len(y) - 1024, 800):
        w = y[i:i + 1024]
        if np.sqrt((w ** 2).mean()) < 0.02: continue
        w = w - w.mean(); c = np.correlate(w, w, "full")[1023:]; lo, hi = r // 300, r // 70; k = lo + np.argmax(c[lo:hi])
        if c[k] > 0.4 * c[0]: ps.append(r / k)
    return round(float(np.median(ps)), 0) if ps else 0
for n, (a, b) in enumerate(segs, 1):
    v = np.where(env[a:b] > 0.004)[0]
    a2, b2 = a + max(0, v[0] - 2400), a + min(b - a, v[-1] + 4800)
    who = "diyor" if n in DY else "usta"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", SRC, "-af", f"atrim=start_sample={a2}:end_sample={b2},asetpts=PTS-STARTPTS",
                    os.path.join(OUT, f"{n:02}_{who}.wav")], check=True)
    print(n, who, round((b2 - a2) / sr, 2), "s", pitch(x[a2:b2]), "Hz")
