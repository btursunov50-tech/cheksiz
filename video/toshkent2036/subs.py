import sys; from texts import *
def t(x): return f"0:{int(x//60):02}:{x%60:05.2f}"
def st(x): return f"00:{int(x//60):02}:{int(x%60):02},{int(round((x%1)*1000)):03}"
for L in SUB:
    hdr=f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: S,Inter,58,&H00FFFFFF,&H00FFFFFF,&H64000000,&H64000000,-1,0,0,0,100,100,0,0,3,14,0,2,90,90,230,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    ev=''.join(f"Dialogue: 0,{t(max(0,a-0.1))},{t(b+0.25)},S,,0,0,0,,{{\\fad(150,150)}}{s}\n" for (a,b),s in zip(LINES,SUB[L]))
    open(f'sub_{L}.ass','w').write(hdr+ev)
    open(f'toshkent2036-{L}.srt','w').write(''.join(f"{i+1}\n{st(max(0,a-0.1))} --> {st(b+0.25)}\n{s}\n\n" for i,((a,b),s) in enumerate(zip(LINES,SUB[L]))))
print('ok')
