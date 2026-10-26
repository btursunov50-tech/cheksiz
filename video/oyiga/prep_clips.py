# timeline.CLIP_USE bo'laklarini clips/use/sNN.mp4 ga kesadi, MOVE dagi kliplarga kamera harakati qo'shadi,
# 11-klip tepasidagi qora tasmani gradient bilan yumshatadi va dialog_fx.wav (ovoz + COIN jiringi) yasaydi.
# Ishlatish: python3 video/oyiga/prep_clips.py
import os, runpy, subprocess
D = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(D, "..", ".."))
tl = runpy.run_path(os.path.join(D, "timeline.py"))
U = os.path.join(D, "clips", "use"); os.makedirs(U, exist_ok=True)
run = lambda c: subprocess.run(c, check=True)
for n, (a, b) in sorted(tl["CLIP_USE"].items()):
    src = os.path.join(D, "clips", f"s{n:02}.mp4"); out = os.path.join(U, f"s{n:02}.mp4")
    vf = f"trim={a}:{b},setpts=PTS-STARTPTS"
    if n == 11:  # tepada 0→480 px qoradan shaffofga o'tadigan soya
        vf += ",split[x][y];[y]format=yuva420p,geq=lum=0:cb=128:cr=128:a='255*clip(1-Y/480\,0\,1)'[g];[x][g]overlay"
    run(["ffmpeg", "-v", "error", "-y", "-i", src, "-filter_complex", f"[0:v]{vf}[v]", "-map", "[v]", "-an",
         "-c:v", "libx264", "-preset", "fast", "-crf", "16", "-r", "24", out])
    if n in tl.get("MOVE", {}):
        mv, am = tl["MOVE"][n]; tmp = out + ".tmp.mp4"; os.replace(out, tmp)
        run(["python3", os.path.join(R, ".claude/skills/kamera/harakat.py"), tmp, out, "--move", mv, "--amount", str(am), "--ease"])
        os.remove(tmp)
    print(n, (a, b), tl.get("MOVE", {}).get(n, ""))
# tanga jiringi (kamera/ramp.py dagi «tanga» tovushi)
snd = ("0.35*(sin(2*PI*2870*t)+0.7*sin(2*PI*4410*t)+0.5*sin(2*PI*6130*t)+0.4*sin(2*PI*1630*t))*exp(-5*t)"
       "+0.25*(sin(2*PI*3100*t)+0.6*sin(2*PI*4820*t))*exp(-9*(t-0.22))*gte(t,0.22)"
       "+0.15*(sin(2*PI*3300*t))*exp(-12*(t-0.37))*gte(t,0.37)")
ins = []; fc = ""
for i, t in enumerate(tl.get("COIN", [])):
    ins += ["-f", "lavfi", "-t", "1.2", "-i", f"aevalsrc='{snd}':s=24000"]
    fc += f"[{i+1}:a]volume=0.5,adelay={int(t*1000)}:all=1[c{i}];"
k = len(tl.get("COIN", []))
fc += "[0:a]" + "".join(f"[c{i}]" for i in range(k)) + f"amix=inputs={k+1}:normalize=0:duration=first[a]"
run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(D, "dialog.wav")] + ins + ["-filter_complex", fc, "-map", "[a]", os.path.join(D, "dialog_fx.wav")])
print("dialog_fx.wav")
