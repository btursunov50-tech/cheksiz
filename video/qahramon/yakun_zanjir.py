# «Birlik» yakuni (egasi, 2026-10-22): bitta qir tepasi, qahramonlar ketma-ket — kamera boshiga yaqinlashadi, qahramon boshini o'ngga buradi,
# kamera keskin o'ngga o'tadi. Ibn Sino → Beruniy → Jaloliddin → Amir Temur (+1 s) → Ulug'bek → Bahodir (haqiqiy kadr) → bayroq.
# Keraksiz kadrlar kesiladi (Veo'da qahramon o'girilib yurib ketadi, Beruniyda ikkinchi odam chiqadi — LAVHALAR.md).
# Ishlatish: python3 video/qahramon/yakun_zanjir.py OUT_DIR  → OUT_DIR/yakun.mp4 (qo'shiq bilan) va yakun_v.mp4 (ovozsiz)
import subprocess, sys, os
import numpy as np
W = sys.argv[1]; os.makedirs(W, exist_ok=True)
C = "video/qahramon/clips/"; R = "video/ref/2026-10-21/"; MUSIC = "video/qahramon/music/birlik.mp3"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
beats = np.load("video/qahramon/music/beats.npy")
def snap(t): return float(beats[np.abs(beats - t).argmin()])
T0, TB, TF, END = snap(128.4), snap(143.4), snap(147.4), 155.4   # klip.py dagi o'rinlar
WHIP = 0.3
# (klip, oxiri s, Veo'ning o'z whip pani bormi, ism, nisbiy uzunlik)
# Oxirlari kadrma-kadr tekshirilgan (egasi: "keraksiz kadr qolmasin"): Veo'ning o'z whip panida orqa tomon / begona manzara chiqadi,
# shuning uchun hammasi bosh burilgach kesiladi va o'tish oxirgi kadrdan yasaladi (kadr o'ralmaydi, ikkinchi odam ko'rinmaydi).
HER = [("y1", 5.4, False, "IBN SINO", 1.0), ("y2", 4.3, False, "ABU RAYHON BERUNIY", 1.0), ("y3", 5.0, False, "JALOLIDDIN MANGUBERDI", 1.0),
       ("y4", 5.8, False, "AMIR TEMUR", 1.4), ("y5", 6.0, False, "MIRZO ULUG'BEK", 1.0)]
def run(c): subprocess.run(c, check=True)
def esc(t): return t.replace(":", "\\:").replace("'", "’")
def name(t, d): return (f"drawtext=fontfile={FONT}:text='{esc(t)}':fontcolor=0xFFC34D:fontsize=40:x=(w-text_w)/2:y=h-200:box=1:boxcolor=black@0.45:boxborderw=12"
                        f":alpha='if(lt(t,0.3),t/0.3,if(gt(t,{d - 0.8:.2f}),max(0,({d - 0.5:.2f}-t)/0.3),1))'")
enc = ["-an", "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p", "-r", "30"]
tot = TB - T0; unit = tot / sum(h[4] for h in HER); parts = []
for i, (k, end, own, nm, rel) in enumerate(HER):
    d = unit * rel; body = d if own else d - WHIP; a = end - body
    p = f"{W}/h{i}.mp4"
    run(["ffmpeg", "-v", "error", "-y", "-ss", f"{a:.3f}", "-t", f"{body:.3f}", "-i", C + k + ".mp4", "-vf", f"fps=30,{name(nm, body)}", *enc, p]); parts.append(p)
    if not own:   # o'zimizning whip pan: oxirgi kadr kattalashib o'ngga suriladi va gorizontal xiralashadi
        q = f"{W}/h{i}w.mp4"; fr = f"{W}/h{i}.png"
        run(["ffmpeg", "-v", "error", "-y", "-ss", f"{end - 0.04:.3f}", "-i", C + k + ".mp4", "-frames:v", "1", fr])
        run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-t", f"{WHIP:.3f}", "-i", fr, "-vf",
             f"fps=30,scale=1008:1792,crop=720:1280:x='144+144*t/{WHIP}':y=256,avgblur=sizeX=55:sizeY=1,eq=brightness=0.04", *enc, q]); parts.append(q)
# Bahodir: haqiqiy kadr (qora chopon, sekin), Veo'dagi kabi o'ngdan xiralik bilan kiradi, keyin bayroqqa o'tadi
db = TF - TB; k = 1.8
# bahodir_toza.mp4 = jalolov_dacres.mp4 3.9–6.3 s, siljib yuruvchi «@OPER_UZ» belgisi har kadrda topilib o'chirilgan (egasi, 2026-10-22)
run(["ffmpeg", "-v", "error", "-y", "-ss", "0.1", "-t", f"{db / k + 0.1:.3f}", "-i", C + "bahodir_toza.mp4", "-filter_complex",
     "split[a][b];[a]scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,boxblur=20:2,eq=brightness=-0.15[bg];[b]scale=720:-2[fg];[bg][fg]overlay=0:(H-h)/2,"
     f"setpts={k}*PTS,minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:vsbmc=1,trim=duration={db:.3f},setpts=PTS-STARTPTS,"
     f"{name('BAHODIR JALOLOV', db)},drawtext=fontfile={FONT}:text='Manba\\: DAZN, @OPER_UZ':fontcolor=white@0.75:fontsize=18:x=(w-text_w)/2:y=h-46",
     *enc, f"{W}/bah.mp4"]); parts.append(f"{W}/bah.mp4")
df = END - TF
run(["ffmpeg", "-v", "error", "-y", "-i", C + "v11.mp4", "-vf", f"fps=30,tpad=stop_mode=clone:stop_duration=2,trim=duration={df:.3f},fade=t=in:d=0.5,fade=t=out:st={df - 1.2:.2f}:d=1.2",
     *enc, f"{W}/bayroq.mp4"]); parts.append(f"{W}/bayroq.mp4")
open(f"{W}/l.txt", "w").write("".join(f"file '{os.path.abspath(p)}'\n" for p in parts))
run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{W}/l.txt", "-c", "copy", f"{W}/yakun_v.mp4"])
run(["ffmpeg", "-v", "error", "-y", "-i", f"{W}/yakun_v.mp4", "-ss", f"{T0:.3f}", "-t", f"{END - T0:.3f}", "-i", MUSIC, "-filter_complex",
     "[1:a]bass=g=3,extrastereo=m=1.3,afade=t=in:d=0.3,afade=t=out:st=" + f"{END - T0 - 1.5:.2f}:d=1.5[a]", "-map", "0:v", "-map", "[a]",
     "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", f"{W}/yakun.mp4"])
print(f"yakun: {T0:.2f}–{END} s ({END - T0:.1f} s), qahramonlar {tot:.1f} s, Bahodir {db:.1f} s, bayroq {df:.1f} s")
