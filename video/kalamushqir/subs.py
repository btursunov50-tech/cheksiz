from data import *
def t(x): return f"0:{int(x//60):02}:{x%60:05.2f}"
def st(x): return f"00:{int(x//60):02}:{int(x%60):02},{int(round((x%1)*1000)):03}"
def red(s,ass=True):
    import re
    return re.sub(r"\*(.+?)\*", (r"{\\c&H2B2BFF&}\1{\\c&HFFFFFF&}" if ass else r"\1"), s)
HDR="""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: S,Inter ExtraBold,{fs},&H00FFFFFF,&H00FFFFFF,&H00000000,&HA0000000,-1,0,0,0,100,100,0,0,1,5,3,2,70,70,330,1
Style: T,Inter ExtraBold,120,&H002B2BFF,&H00FFFFFF,&H00000000,&H00000000,-1,0,0,0,100,100,6,0,1,6,0,8,40,40,200,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
for L,TX in (('uz',UZ),('ru',RU),('en',EN)):
    ev=''
    for k,((a,b),s) in enumerate(zip(SEG,TX)):
        nxt=SEG[k+1][0] if k+1<len(SEG) else MAIN
        end=min(nxt-0.05,b+0.6)
        if L=='uz':
            parts=s.split('|'); tot=sum(len(p) for p in parts); tt=a
            for i,p in enumerate(parts):
                d=(b-a)*len(p)/tot; e=end if i==len(parts)-1 else tt+d
                ev+=f"Dialogue: 0,{t(max(0,tt-0.05))},{t(e)},S,,0,0,0,,{{\\fad(80,80)\\fscx92\\fscy92\\t(0,120,\\fscx100\\fscy100)}}{red(p)}\n"; tt+=d
        else:
            ev+=f"Dialogue: 0,{t(max(0,a-0.05))},{t(end)},S,,0,0,0,,{{\\fad(100,100)}}{red(s.replace('|',' '))}\n"
    ev+=f"Dialogue: 1,{t(37.45)},{t(43.6)},T,,0,0,0,,{{\\fad(250,400)\\fscx130\\fscy130\\t(0,600,\\fscx100\\fscy100)\\blur1}}{TITLE[L]}\n"
    fs=72 if L=='uz' else 60
    open(f'sub_{L}.ass','w').write(HDR.replace('{fs}',str(fs))+ev)
    if L!='en' or True:
        open(f'kalamushqir-{L}.srt','w').write(''.join(f"{i+1}\n{st(max(0,a-0.05))} --> {st(min((SEG[i+1][0] if i+1<len(SEG) else MAIN)-0.05,b+0.6))}\n{red(s.replace('|',' '),False)}\n\n" for i,((a,b),s) in enumerate(zip(SEG,TX))))
print('ok')
