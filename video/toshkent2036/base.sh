#!/usr/bin/env bash
# Builds the base (no subtitles) from available clips src/c1..c8 using CUTS/OFFS in texts.py.
set -e
N=${1:-8}
python3 - "$N" <<'PY'
import sys,subprocess,os; from texts import CUTS,OFFS
n=int(sys.argv[1]); parts=[]
os.makedirs('seg',exist_ok=True)
for i in range(n):
    src=f'src/c{i+1}.mp4' if i!=3 else 'src/c4c.mp4'
    d=CUTS[i+1]-CUTS[i]
    subprocess.run(['ffmpeg','-v','error','-y','-ss',str(OFFS[i]),'-t',f'{d:.3f}','-i',src,'-vf','scale=1080:1920:flags=lanczos,fps=30,setsar=1','-c:v','libx264','-crf','17','-preset','medium','-pix_fmt','yuv420p','-an',f'seg/s{i}.mp4'],check=True)
    parts.append(f"file 's{i}.mp4'\n")
open('seg/list.txt','w').write(''.join(parts))
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','seg/list.txt','-c','copy','seg/raw.mp4'],check=True)
print(' '.join(f'{c}' for c in CUTS[1:n]))
PY
