from data import *
def t(x): return f"0:{int(x//60):02}:{x%60:05.2f}"
def st(x): return f"00:{int(x//60):02}:{int(x%60):02},{int(round((x%1)*1000)):03}"
HDR="""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: S,Inter ExtraBold,{fs},&H00FFFFFF,&H00FFFFFF,&H00201008,&H90000000,-1,0,0,0,100,100,0,0,1,5,3,2,70,70,300,1
Style: C,Inter ExtraBold,{fs},&H00FFE600,&H00FFFFFF,&H00301000,&H90000000,-1,-1,0,0,100,100,0,0,1,5,3,2,70,70,300,1
Style: R,Inter ExtraBold,{fs},&H005050FF,&H00FFFFFF,&H00000030,&H90000000,-1,-1,0,0,100,100,0,0,1,5,3,2,70,70,300,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
for L,TX,fs in (('uz',UZ,68),('ru',RU,64),('en',EN,64)):
    ev='';srt=''
    for i,((a,b,s),x) in enumerate(zip(SEG,TX)):
        ev+=f"Dialogue: 0,{t(a)},{t(b)},{s},,0,0,0,,{{\\fad(150,150)\\fscx92\\fscy92\\t(0,150,\\fscx100\\fscy100)}}{x}\n"
        srt+=f"{i+1}\n{st(a)} --> {st(b)}\n{x}\n\n"
    a,b=LAST_T; srt+=f"{len(SEG)+1}\n{st(a)} --> {st(b)}\n{LAST[L]}\n\n"
    open(f'sub_{L}.ass','w').write(HDR.replace('{fs}',str(fs))+ev); open(f'nusxa-{L}.srt','w').write(srt)
print('ok')
