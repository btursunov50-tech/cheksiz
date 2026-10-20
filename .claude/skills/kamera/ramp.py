#!/usr/bin/env python3
"""Sekinlashuv + zarba ovozi (egasi, 2026-10-20): narsa tushayotganda kadr sekinlashadi,
yerga tekkanda ovoz chiqadi, keyin oddiy tezlik qaytadi.
  python3 ramp.py KIRISH.mp4 CHIQISH.mp4 --a 1.2 --b 2.4 --slow 0.3 [--sound tanga|zarba|yoq]
a..b oralig'i (asl klip soniyalari) `slow` marta tezlikda o'ynaydi (0.3 = ~3.3 baravar sekin, minterpolate bilan silliq).
b = yerga tekkan payt: shu yerda ovoz qo'yiladi. Klipning o'z ovozi olib tashlanadi (sekinlashganda buziladi)."""
import argparse, subprocess, tempfile, os
p = argparse.ArgumentParser()
p.add_argument('inp'); p.add_argument('out')
p.add_argument('--a', type=float, required=True); p.add_argument('--b', type=float, required=True)
p.add_argument('--slow', type=float, default=0.3)
p.add_argument('--sound', default='tanga', choices=['tanga', 'zarba', 'yoq'])
o = p.parse_args()
fps = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v', '-show_entries', 'stream=r_frame_rate',
                      '-of', 'csv=p=0', o.inp], capture_output=True, text=True).stdout.strip()
num, den = map(int, fps.split('/')); f = round(num / den) or 30
k = 1 / o.slow
v = (f"[0:v]split=3[v1][v2][v3];"
     f"[v1]trim=0:{o.a},setpts=PTS-STARTPTS[p1];"
     f"[v2]trim={o.a}:{o.b},setpts=(PTS-STARTPTS)*{k},minterpolate=fps={f}:mi_mode=mci:mc_mode=aobmc:vsbmc=1[p2];"
     f"[v3]trim=start={o.b},setpts=PTS-STARTPTS[p3];"
     f"[p1][p2][p3]concat=n=3:v=1:a=0,fps={f},format=yuv420p[v]")
hit = o.a + (o.b - o.a) * k
dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', o.inp],
                           capture_output=True, text=True).stdout) + (o.b - o.a) * (k - 1)
# tanga: metall jiringlash (bir-biriga mos kelmaydigan obertonlar) + mayda sakrashlar; zarba: past gumburlash
snd = {
    'tanga': "0.35*(sin(2*PI*2870*t)+0.7*sin(2*PI*4410*t)+0.5*sin(2*PI*6130*t)+0.4*sin(2*PI*1630*t))*exp(-5*t)"
             "+0.25*(sin(2*PI*3100*t)+0.6*sin(2*PI*4820*t))*exp(-9*(t-0.22))*gte(t,0.22)"
             "+0.15*(sin(2*PI*3300*t))*exp(-12*(t-0.37))*gte(t,0.37)",
    'zarba': "0.9*sin(2*PI*55*t)*exp(-4*t)+0.2*(random(0)-0.5)*exp(-25*t)",
}
cmd = ['ffmpeg', '-loglevel', 'error', '-y', '-i', o.inp]
if o.sound != 'yoq':
    cmd += ['-f', 'lavfi', '-i', f"aevalsrc='{snd[o.sound]}':s=48000:d=2.5"]
    a = (f";[1:a]adelay={int(hit*1000)}|{int(hit*1000)},apad,atrim=0:{dur:.2f},alimiter=limit=0.9[a]")
    cmd += ['-filter_complex', v + a, '-map', '[v]', '-map', '[a]', '-c:a', 'aac']
else:
    cmd += ['-filter_complex', v, '-map', '[v]', '-an']
cmd += ['-c:v', 'libx264', '-crf', '18', '-pix_fmt', 'yuv420p', o.out]
subprocess.run(cmd, check=True)
print(f"tayyor: {o.out}  zarba ovozi {hit:.2f} s da, uzunligi ~{dur:.1f} s")
