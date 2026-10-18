#!/usr/bin/env python3
"""Tayyor VIDEO klipga montajda kamera harakati qo'shadi (faqat videoga; harakatsiz rasmga emas — egasi qoidasi).

python3 .claude/skills/kamera/harakat.py KIRISH.mp4 CHIQISH.mp4 --move pushin [--amount 0.12] [--ease]
Harakatlar:
  pushin / pullout  — sekin yaqinlashish / uzoqlashish (amount = kattalashish ulushi, 0.08–0.2)
  panleft / panright / tiltup / tiltdown — kadr bo'ylab suzish (amount = siljish ulushi)
  shake             — qo'lda olingandek silkinish (amount = kuchi, 0.005–0.02)
  crash             — oxirgi 0.4 s da keskin yaqinlashish (shok, burilish)
  whipout           — oxirgi 0.3 s da yon tomonga tez "qamchi" + xiralashish (keyingi kadrga o'tish)
  rack              — boshida xira, 0.8 s da aniqlashadi (fokus ko'chishi)
Natija 1080×1920, 30 kadr/s, ovozsiz.
"""
import argparse, subprocess

def dur(f):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f],
                                capture_output=True, text=True).stdout)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("inp"); p.add_argument("out")
    p.add_argument("--move", required=True, choices=["pushin", "pullout", "panleft", "panright", "tiltup", "tiltdown",
                                                       "shake", "crash", "whipout", "rack"])
    p.add_argument("--amount", type=float); p.add_argument("--ease", action="store_true", help="silliq boshlanib, silliq tugaydi")
    a = p.parse_args()
    D = dur(a.inp); W, H = 1080, 1920
    u = f"(t/{D:.3f})"
    if a.ease: u = f"(0.5-0.5*cos(PI*t/{D:.3f}))"
    m = a.amount
    base = f"fps=30,scale={W}:{H}:flags=lanczos,setsar=1"
    if a.move in ("pushin", "pullout"):
        m = m or 0.12
        z = f"(1+{m}*{u})" if a.move == "pushin" else f"(1+{m}*(1-{u}))"
        vf = f"{base},scale=w='trunc({W}*{z}/2)*2':h='trunc({H}*{z}/2)*2':eval=frame:flags=bicubic,crop={W}:{H}"
    elif a.move in ("panleft", "panright", "tiltup", "tiltdown"):
        m = m or 0.08; S = 1 + m
        sw, shh = int(W * S) // 2 * 2, int(H * S) // 2 * 2
        dx, dy = sw - W, shh - H
        x = {"panleft": f"{dx}*(1-{u})", "panright": f"{dx}*{u}"}.get(a.move, f"{dx}/2")
        y = {"tiltup": f"{dy}*(1-{u})", "tiltdown": f"{dy}*{u}"}.get(a.move, f"{dy}/2")
        vf = f"{base},scale={sw}:{shh},crop={W}:{H}:'{x}':'{y}'"
    elif a.move == "shake":
        m = m or 0.01; S = 1 + 4 * m
        sw, shh = int(W * S) // 2 * 2, int(H * S) // 2 * 2
        ax, ay = (sw - W) / 2, (shh - H) / 2
        x = f"{ax}+{ax*0.8}*(0.6*sin(t*7.3)+0.4*sin(t*13.1+1))"
        y = f"{ay}+{ay*0.8}*(0.6*sin(t*6.1+2)+0.4*sin(t*11.7))"
        vf = f"{base},scale={sw}:{shh},crop={W}:{H}:'{x}':'{y}'"
    elif a.move == "crash":
        m = m or 0.35; s0 = max(0, D - 0.4)
        z = f"(1+{m}*pow(max(0,(t-{s0:.3f})/0.4),2))"
        vf = f"{base},scale=w='trunc({W}*{z}/2)*2':h='trunc({H}*{z}/2)*2':eval=frame:flags=bicubic,crop={W}:{H}"
    elif a.move == "whipout":
        s0 = max(0, D - 0.3); S = 1.15
        sw, shh = int(W * S) // 2 * 2, int(H * S) // 2 * 2
        x = f"if(lt(t,{s0:.3f}),{(sw-W)//2},min({sw-W},{(sw-W)//2}+{(sw-W)//2}*pow((t-{s0:.3f})/0.3,2)))"
        vf = (f"{base},scale={sw}:{shh},crop={W}:{H}:'{x}':{(shh-H)//2},"
              f"gblur=sigma=40:sigmaV=1:enable='gte(t,{s0+0.05:.3f})'")
    else:  # rack
        vf = f"{base},gblur=sigma=18:enable='lt(t,0.4)',gblur=sigma=9:enable='between(t,0.4,0.6)',gblur=sigma=4:enable='between(t,0.6,0.8)'"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", a.inp, "-vf", vf + ",format=yuv420p", "-an",
                    "-c:v", "libx264", "-crf", "17", "-preset", "medium", a.out], check=True)
    print("ok", a.move, a.out)

if __name__ == "__main__":
    main()
