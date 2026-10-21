# Har qator: boshi/oxiridagi jimlik kesiladi, 0.45 s dan uzun pauza 0.45 s ga qisqartiriladi; VAQT qatorlariga yengil aks-sado.
# Natija: voice_cut/NN.wav va har qatordagi gap bo'laklari (SUB uchun) — segs.json
import re, subprocess, json, sys
FILES = ["01_diktor","02_aziz","03_hojiboy","04_vaqt","05_hojiboy","06_vaqt","07_vaqt_ottiz","08_hojiboy","09_vaqt","10_aziz","11_hojiboy","12_diktor","13_aziz","14_diktor"]
def dur(f): return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f],capture_output=True,text=True).stdout)
def speech(f):
    d = dur(f)
    e = subprocess.run(["ffmpeg","-i",f,"-af","silencedetect=n=-38dB:d=0.2","-f","null","-"],capture_output=True,text=True).stderr
    st = list(map(float, re.findall(r"silence_start: ([0-9.]+)", e))); en = list(map(float, re.findall(r"silence_end: ([0-9.]+)", e)))
    if len(en) < len(st): en.append(d)
    segs, t = [], 0.0
    for a, b in zip(st, en):
        if a > t + 0.05: segs.append([t, a])
        t = b
    if t < d - 0.05: segs.append([t, d])
    return segs
out = {}
for f in FILES:
    src = f"video/vaqt/voice/{f}.flac"; segs = speech(src)
    parts, fc, t, new = [], "", 0.0, []
    for i, (a, b) in enumerate(segs):
        a0, b0 = max(0, a - 0.06), b + 0.08
        fc += f"[0:a]atrim={a0:.3f}:{b0:.3f},asetpts=PTS-STARTPTS[p{i}];"
        if i:
            g = min(0.45, max(0.05, a0 - (segs[i-1][1] + 0.08)))
            fc += f"aevalsrc=0:d={g:.3f}:s=48000[g{i}];"; parts.append(f"[g{i}]"); t += g
        parts.append(f"[p{i}]"); new.append([round(t + 0.06, 2), round(t + (b0 - a0) - 0.08, 2)]); t += b0 - a0
    n = len(parts)
    chain = "aresample=48000" + (",aecho=0.8:0.6:70|140:0.22|0.12,lowpass=f=7000" if "vaqt" in f else "")
    fc += "".join(parts) + f"concat=n={n}:v=0:a=1,{chain}[o]"
    subprocess.run(["ffmpeg","-v","error","-y","-i",src,"-filter_complex",fc,"-map","[o]","-ac","1",f"video/vaqt/voice_cut/{f[:2]}.wav"],check=True)
    out[f[:2]] = {"dur": round(dur(f"video/vaqt/voice_cut/{f[:2]}.wav"), 2), "segs": new}
    print(f, round(dur(src),2), "->", out[f[:2]]["dur"], new)
json.dump(out, open("video/vaqt/voice_cut/segs.json","w"), indent=0)
