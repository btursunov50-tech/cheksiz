#!/usr/bin/env python3
"""Egasi yuborgan AI rasmlarni tekshirish varag'i (yuzlar yonma-yon, takror fayl, o'lcham).

python3 .claude/skills/rasm-tekshir/tekshir.py RASM1 [RASM2 ...] --ref video/<loyiha>/img/ref_diyor.png \
    [--ref video/<loyiha>/img/s04.png] [--box RASM1=0.2,0.3,0.6,0.55] [--refbox ref_diyor=0.4,0.08,0.75,0.3] \
    [--known video/<loyiha>/img] --sheet <scratchpad>/tekshir.jpg

--box / --refbox: yuz sohasi, rasm kengligi/balandligiga nisbatan (x1,y1,x2,y2), Claude rasmga qarab beradi.
Berilmasa, rasmning yuqori-o'rta qismi olinadi. Natija: varaq (1-qator butun rasmlar, 2-qator yuzlar) va jadval.
"""
import argparse, hashlib, os, sys
from PIL import Image, ImageDraw

def md5(p): return hashlib.md5(open(p, "rb").read()).hexdigest()

def box_of(spec, key):
    for s in spec or []:
        k, v = s.split("=", 1)
        if os.path.basename(key).startswith(k) or key == k:
            return tuple(float(x) for x in v.split(","))
    return None

def main():
    a = argparse.ArgumentParser()
    a.add_argument("images", nargs="+"); a.add_argument("--ref", action="append", default=[])
    a.add_argument("--box", action="append"); a.add_argument("--refbox", action="append")
    a.add_argument("--known", action="append", default=[], help="takrorni qidirish uchun papka(lar)")
    a.add_argument("--sheet", required=True)
    o = a.parse_args()
    known = {}
    for d in o.known:
        for f in sorted(os.listdir(d)):
            p = os.path.join(d, f)
            if os.path.isfile(p): known.setdefault(md5(p), p)
    rows, seen = [], {}
    items = [(p, True) for p in o.ref] + [(p, False) for p in o.images]
    full, faces = [], []
    for p, isref in items:
        im = Image.open(p).convert("RGB"); w, h = im.size
        b = box_of(o.refbox if isref else o.box, p) or (0.2, 0.05, 0.8, 0.45)
        face = im.crop((int(b[0]*w), int(b[1]*h), int(b[2]*w), int(b[3]*h)))
        lab = ("NAMUNA " if isref else "") + os.path.basename(p)[:22]
        full.append((im, lab)); faces.append((face, lab))
        if not isref:
            m = md5(p); dup = seen.get(m) or (known.get(m) if os.path.abspath(known.get(m, p)) != os.path.abspath(p) else None)
            ratio = w / h; fmt = "9:16" if abs(ratio - 9/16) < 0.02 else "1:1" if abs(ratio - 1) < 0.02 else "16:9" if abs(ratio - 16/9) < 0.03 else f"{w}:{h}"
            rows.append((os.path.basename(p), f"{w}×{h}", fmt, m[:8], dup or "-", getattr(Image.open(p), "n_frames", 1)))
            seen[m] = p
    H1, H2 = 420, 300
    def strip(lst, H):
        ims = [(x.resize((max(1, int(x.width*H/x.height)), H)), l) for x, l in lst]
        W = sum(x.width for x, _ in ims) + 10*len(ims)
        s = Image.new("RGB", (W, H + 24), "white"); d = ImageDraw.Draw(s); x0 = 0
        for x, l in ims:
            s.paste(x, (x0, 24)); d.text((x0 + 4, 4), l, fill="black"); x0 += x.width + 10
        return s
    a1, a2 = strip(full, H1), strip(faces, H2)
    sh = Image.new("RGB", (max(a1.width, a2.width), a1.height + a2.height + 10), "white")
    sh.paste(a1, (0, 0)); sh.paste(a2, (0, a1.height + 10))
    if sh.width > 2400: sh = sh.resize((2400, int(sh.height*2400/sh.width)))
    sh.save(o.sheet, quality=88)
    print("| Fayl | O'lcham | Format | md5 | Takror (oldin kelgan) | Kadr |\n|---|---|---|---|---|---|")
    for r in rows: print("| " + " | ".join(str(x) for x in r) + " |")
    print(f"\nVaraq (Read bilan ko'ring): {o.sheet}")

if __name__ == "__main__":
    main()
