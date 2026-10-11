import re
from data import *
def t(x): return f"0:{int(x//60):02}:{x%60:05.2f}"
def st(x): return f"00:{int(x//60):02}:{int(x%60):02},{int(round((x%1)*1000)):03}"
red=lambda s,a=True: re.sub(r"\*(.+?)\*", (r"{\\c&H4AD2FF&}\1{\\c&HFFFFFF&}" if a else r"\1"), s)
HDR="""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: S,Inter ExtraBold,{fs},&H00FFFFFF,&H00FFFFFF,&H00201008,&H90000000,-1,0,0,0,100,100,0,0,1,5,3,2,70,70,300,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
def nxt(k): return SEG[k+1][0] if k+1<len(SEG) else MAIN
ev=''
for k,((a,b),s) in enumerate(zip(SEG,UZ)):
    end=min(nxt(k)-0.05,b+0.6); parts=s.split('|'); tot=sum(len(p) for p in parts); tt=a
    for i,p in enumerate(parts):
        d=(b-a)*len(p)/tot; e=end if i==len(parts)-1 else tt+d
        ev+=f"Dialogue: 0,{t(max(0,tt-0.05))},{t(e)},S,,0,0,0,,{{\\fad(80,80)\\fscx92\\fscy92\\t(0,120,\\fscx100\\fscy100)}}{red(p)}\n"; tt+=d
open('sub_uz.ass','w').write(HDR.replace('{fs}','70')+ev)
open('dadam-uz.srt','w').write(''.join(f"{i+1}\n{st(max(0,a-0.05))} --> {st(min(nxt(i)-0.05,b+0.6))}\n{red(s.replace('|',' '),False)}\n\n" for i,((a,b),s) in enumerate(zip(SEG,UZ))))
for L,TX in (('ru',RU),('en',EN)):
    ev='';srt=''
    for i,((f,l),s) in enumerate(zip(GR,TX)):
        a=SEG[f][0]; b=SEG[l][1]; end=min(nxt(l)-0.05,b+0.7)
        ev+=f"Dialogue: 0,{t(max(0,a-0.05))},{t(end)},S,,0,0,0,,{{\\fad(100,100)}}{red(s)}\n"
        srt+=f"{i+1}\n{st(max(0,a-0.05))} --> {st(end)}\n{red(s,False)}\n\n"
    open(f'sub_{L}.ass','w').write(HDR.replace('{fs}','58')+ev); open(f'dadam-{L}.srt','w').write(srt)
print('ok')
