#!/usr/bin/env python3
"""AI klipini tekshiradi va tozalaydi (Veo / Vidu / Dreamina / Hailuo / Kling).

python3 .claude/skills/klip-tekshir/tekshir.py KLIP.mp4 --name s16 --out video/robot/clips \
    --src video/robot/img/16_shartnoma.jpg --ref video/robot/img/ref_robot.jpg --ref video/robot/img/ref_odam.jpg

Natija: <out>/<name>.mp4 (720×1280, belgisiz, ovozsiz), kerak bo'lsa <out>/<name>_asl.mp4 (asli),
<sheet> — manba rasm + namunalar + klipning 6 kadri (Read bilan ko'rish uchun), va markdown jadval.
"""
import argparse, json, os, re, shutil, subprocess, sys
from PIL import Image, ImageDraw

# Ma'lum vositalar: o'lcham -> (nom, belgi, crop w:h:x:y). Crop 9:16 ni saqlaydi va belgini chetda qoldiradi.
TOOLS = {
    (720, 1280): ("Veo", "yo'q", None),
    (540, 958): ("Vidu", "«Vidu AI» pastki o'ngda", "496:882:22:0"),
    (704, 1248): ("Dreamina", "«Dreamina AI» pastda + «AI» tepa chapda", "644:1144:30:40"),
    (768, 1344): ("Hailuo", "«MINIMAX · Hailuo AI» pastki o'ngda", "708:1260:30:0"),
}

def sh(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

def probe(f):
    j = json.loads(sh(["ffprobe", "-v", "error", "-print_format", "json", "-show_streams", "-show_format", f]).stdout)
    v = next(s for s in j["streams"] if s["codec_type"] == "video")
    num, den = v["r_frame_rate"].split("/")
    return int(v["width"]), int(v["height"]), float(j["format"]["duration"]), round(float(num) / float(den), 2)

def detect(f, filt, key):
    err = sh(["ffmpeg", "-i", f, "-vf", filt, "-map", "0:v", "-f", "null", "-"]).stderr
    return re.findall(key + r": ([0-9.]+)", err)

def motion(f):
    import numpy as np
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-vf", "fps=4,scale=180:320,format=gray",
                          "-f", "rawvideo", "-"], capture_output=True).stdout
    a = np.frombuffer(raw, np.uint8).reshape(-1, 320, 180).astype(float)
    return round(float(np.abs(np.diff(a, axis=0)).mean()), 1)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("clip"); p.add_argument("--name", required=True); p.add_argument("--out", required=True)
    p.add_argument("--src", help="klip yasalgan rasm"); p.add_argument("--ref", action="append", default=[])
    p.add_argument("--crop", help="qo'lda crop w:h:x:y (noma'lum vosita uchun)")
    p.add_argument("--sheet", default=None)
    a = p.parse_args()
    os.makedirs(a.out, exist_ok=True)
    w, h, dur, fps = probe(a.clip)
    tool, mark, crop = TOOLS.get((w, h), ("noma'lum", "tekshiring", None))
    crop = a.crop or crop
    freeze = detect(a.clip, "freezedetect=n=0.001:d=0.5", "freeze_start")
    black = detect(a.clip, "blackdetect=d=0.2", "black_start")
    mot = motion(a.clip)

    out = os.path.join(a.out, a.name + ".mp4")
    vf = (f"crop={crop}," if crop else "") + "scale=720:1280:flags=lanczos,setsar=1"
    if crop:
        shutil.copy(a.clip, os.path.join(a.out, a.name + "_asl.mp4"))
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", a.clip, "-vf", vf, "-c:v", "libx264", "-crf", "16",
                    "-preset", "slow", "-an", out], check=True)

    # varaq: manba + namunalar | 6 kadr (tozalangan klipdan)
    W, H = 270, 480
    ts = [0.1, dur * .2, dur * .4, dur * .6, dur * .8, max(0, dur - .15)]
    left = [Image.open(x).convert("RGB") for x in ([a.src] if a.src else []) + a.ref]
    sheet = Image.new("RGB", (W * (len(left) + len(ts)), H), "black")
    for i, im in enumerate(left):
        im.thumbnail((W, H)); sheet.paste(im, (i * W, 0))
    tmp = os.path.join(a.out, f".{a.name}_f.png")
    for i, t in enumerate(ts):
        sh(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", out, "-frames:v", "1", "-vf", f"scale={W}:{H}", tmp])
        im = Image.open(tmp).convert("RGB"); d = ImageDraw.Draw(im)
        d.rectangle([0, 0, 60, 22], fill="black"); d.text((5, 5), f"{t:.1f}s", fill="white")
        sheet.paste(im, ((len(left) + i) * W, 0))
    os.remove(tmp)
    sp = a.sheet or os.path.join("/tmp", f"{a.name}_sheet.jpg")
    sheet.save(sp, quality=85)

    print(f"| Nima | Natija |\n|---|---|")
    print(f"| Vosita | {tool} ({w}×{h}, {fps} kadr/s, {dur:.1f} s) |")
    print(f"| Suv belgisi | {mark}" + (f" → kesildi (crop {crop})" if crop else "") + " |")
    print(f"| Qotgan kadr | {'yo' + chr(39) + 'q' if not freeze else ', '.join(freeze) + ' s'} |")
    print(f"| Qora kadr | {'yo' + chr(39) + 'q' if not black else ', '.join(black) + ' s'} |")
    print(f"| Harakat | {mot} (odatda 6–12; 3 dan past = deyarli qimirlamaydi, 20 dan yuqori = kamera tez yuradi) |")
    print(f"| Toza klip | {out} |")
    print(f"| Varaq (Read bilan ko'ring) | {sp} |")
    if tool == "noma'lum":
        print("\nDIQQAT: o'lcham tanish emas — varaqdan belgini toping va --crop bilan qayta ishga tushiring.")

if __name__ == "__main__":
    main()
