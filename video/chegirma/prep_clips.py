# Kliplarning ishlatiladigan qismini clips/use/ ga kesadi (README.md jadvali), 5-sahnada yorliq tushishini sekinlashtiradi
# (kamera/ramp.py, 5.3–6.6 s, 0.5x), kamera qimirlamagan kliplarga harakat qo'shadi (kamera/harakat.py).
# Ishlatish: python3 video/chegirma/prep_clips.py   (avval build_tl.py)
import os, subprocess
D = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(D, "..", ".."))
C = os.path.join(D, "clips"); U = os.path.join(C, "use"); os.makedirs(U, exist_ok=True)
run = lambda c: subprocess.run(c, check=True)
USE = {  # chiqish nomi: (manba, boshi, oxiri)
    "s01": ("s01_y", 0, 8), "s02": ("s02", 0, 8), "s03": ("s03", 0.3, 5.0), "s04": ("s04", 0, 3.5),
    "s05": ("s05_y", 0, 8), "s06": ("s06", 0, 2.6), "s07": ("s07_y", 0, 8), "s08": ("s08", 0, 8),
    "s09": ("s09", 0, 2.7), "s10": ("s10", 0, 2.4), "s10b": ("s10b", 0, 8), "s10c": ("s10c", 2.3, 5.5),
    "s11": ("s11", 0, 8), "s12": ("s12", 0, 7.6),
}
MOVE = {"s10b": ("pushin", 0.10)}   # Veo kamerani qimirlatmagan (harakat 8.2)
for n, (src, a, b) in USE.items():
    out = os.path.join(U, n + ".mp4")
    run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(C, src + ".mp4"), "-vf", f"trim={a}:{b},setpts=PTS-STARTPTS,fps=24",
         "-an", "-c:v", "libx264", "-preset", "fast", "-crf", "16", out])
    if n == "s05":
        tmp = out + ".tmp.mp4"; os.replace(out, tmp)
        run(["python3", os.path.join(R, ".claude/skills/kamera/ramp.py"), tmp, out, "--a", "5.3", "--b", "6.6", "--slow", "0.5", "--sound", "yoq"])
        os.remove(tmp)
    if n in MOVE:
        mv, am = MOVE[n]; tmp = out + ".tmp.mp4"; os.replace(out, tmp)
        run(["python3", os.path.join(R, ".claude/skills/kamera/harakat.py"), tmp, out, "--move", mv, "--amount", str(am), "--ease"])
        os.remove(tmp)
    print(n, src, (a, b), MOVE.get(n, ""))
