#!/usr/bin/env python3
"""Tasdiqlangan rasmni loyihaga saqlaydi: img/<nom>.png + web/<nom>.webp (sahifa uchun 360 px).
python3 .claude/skills/rasm-tekshir/saqla.py RASM video/<loyiha> s07 [--blur x1,y1,x2,y2]  (blur: yuzni xiralashtirish, nisbiy)"""
import os, sys
from PIL import Image, ImageFilter, ImageDraw
src, proj, name = sys.argv[1:4]
im = Image.open(src).convert("RGB")
if "--blur" in sys.argv:
    x1, y1, x2, y2 = (float(v) for v in sys.argv[sys.argv.index("--blur") + 1].split(","))
    w, h = im.size; m = Image.new("L", im.size, 0)
    ImageDraw.Draw(m).ellipse((x1*w, y1*h, x2*w, y2*h), fill=255)
    im = Image.composite(im.filter(ImageFilter.GaussianBlur(14)), im, m.filter(ImageFilter.GaussianBlur(40)))
os.makedirs(f"{proj}/img", exist_ok=True); os.makedirs(f"{proj}/web", exist_ok=True)
im.save(f"{proj}/img/{name}.png"); t = im.copy(); t.thumbnail((360, 640)); t.save(f"{proj}/web/{name}.webp", quality=82)
print(f"saqlandi: {proj}/img/{name}.png, {proj}/web/{name}.webp")
