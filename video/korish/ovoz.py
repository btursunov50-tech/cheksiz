# Qator fayllarini (voice/NN_*.flac) timeline.VOICE dagi pauzalar bilan bitta ovoz.flac ga yig'adi
# va har qatorni gaplarga bo'lib SUB vaqtlarini chiqaradi (pauzalar silencedetect bilan, 0.45 s dan qisqasi birlashtiriladi).
import re, subprocess, sys
sys.path.insert(0, "video/korish"); from timeline import VOICE
def dur(f): return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f], capture_output=True, text=True).stdout)
def speech(f, d):
    e = subprocess.run(["ffmpeg", "-i", f, "-af", "silencedetect=n=-35dB:d=0.25", "-f", "null", "-"], capture_output=True, text=True).stderr
    sil = list(zip(map(float, re.findall(r"silence_start: ([0-9.]+)", e)), map(float, re.findall(r"silence_end: ([0-9.]+)", e))))
    segs, t = [], 0.0
    for a, b in sil:
        if a > t: segs.append([t, a])
        t = b
    if t < d: segs.append([t, d])
    out = [segs[0]]
    for a, b in segs[1:]:
        if a - out[-1][1] < 0.45: out[-1][1] = b
        else: out.append([a, b])
    return out
t, inputs, fc, SUB = 0.0, [], "", []
for i, (f, gap, who, text) in enumerate(VOICE):
    p = f"video/korish/voice/{f}.flac"; d = dur(p); st = t + gap
    inputs += ["-i", p]; ms = int(st * 1000); fc += f"[{i}:a]aresample=48000,adelay={ms}|{ms}[a{i}];"
    parts = re.findall(r"[^.?!]+[.?!]", text) if who != "x" else [text]
    segs = speech(p, d)
    if len(segs) != len(parts): print("DIQQAT", f, len(segs), len(parts), segs, parts)
    for (a, b), x in zip(segs, parts): SUB.append((round(st + a, 2), round(st + b + 0.15, 2), "R" if who == "D" else "O", x.strip()))
    t = st + d
fc += "".join(f"[a{i}]" for i in range(len(VOICE))) + f"amix=inputs={len(VOICE)}:normalize=0[o]"
subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", fc, "-map", "[o]", "-ac", "1", "video/korish/ovoz.flac"], check=True)
print("oxiri", round(t, 2))
for s in SUB: print(f" {s},")
