# Kliplarning ishlatiladigan qismini clips/use/ ga kesadi (README.md jadvali). 8-klipga sekin yaqinlashish qo'shiladi (Veo kam qimirlatgan).
# Ishlatish: python3 video/eskirish/prep_clips.py   (keyin build_tl.py, keyin /video-yig)
import os, subprocess
D = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(D, "..", ".."))
C = os.path.join(D, "clips"); U = os.path.join(C, "use"); os.makedirs(U, exist_ok=True)
run = lambda c: subprocess.run(c, check=True)
USE = {  # chiqish: (manba, boshi, oxiri)
    "s01": ("s01", 0, 5.5), "s02": ("s02", 0, 8), "s03": ("s03_sd", 0, 3.5), "s04": ("s04_sd", 0, 4.33),
    "s05": ("s05", 0, 8), "s06": ("s06", 0, 4.5), "s06b": ("s06b", 0, 3), "s07": ("s07", 0, 6.5),
    "s08": ("s08_y", 0, 8), "s09": ("s09_y", 0, 4.7), "s10": ("s10", 0, 6), "s11": ("s11", 0, 5.5),
    "s12": ("s12", 0, 8), "s13": ("s13", 0, 8), "s14": ("s14", 0, 8), "s15": ("s15", 0, 8),
}
MOVE = {"s08": ("pushin", 0.10)}
for n, (src, a, b) in USE.items():
    out = os.path.join(U, n + ".mp4")
    run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(C, src + ".mp4"), "-vf",
         f"trim={a}:{b},setpts=PTS-STARTPTS,scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,setsar=1,fps=24",
         "-an", "-c:v", "libx264", "-preset", "fast", "-crf", "16", out])
    if n in MOVE:
        mv, am = MOVE[n]; tmp = out + ".tmp.mp4"; os.replace(out, tmp)
        run(["python3", os.path.join(R, ".claude/skills/kamera/harakat.py"), tmp, out, "--move", mv, "--amount", str(am), "--ease"])
        os.remove(tmp)
    print(n, src, (a, b), MOVE.get(n, ""))
