import re
from langs import EN,RU,Q,AVQ
src=open('build.py').read()
ns={}
exec(src.split("# scenes:")[0].split("IMG=")[0]+"\n",ns)  # M
exec("OFF=1.0\n"+re.search(r"dur=\[.*?\]",src).group(0)+"\nst=[];t=0\nfor d in dur: st.append(t+OFF); t+=d+0.3\n",ns)
txt=eval(re.search(r"txt=(\[.*?\])\n",src,re.S).group(1)); who=eval(re.search(r"who=(\[.*?\])",src).group(1))
st,dur=ns['st'],ns['dur']
TX={'uz':txt,'en':EN,'ru':RU}
def tt(x): return f"0:{int(x//60):02}:{x%60:05.2f}"
def srt(x): return f"00:{int(x//60):02}:{int(x%60):02},{int(round((x%1)*1000)):03}"
HDR0=open('/tmp/claude-0/-home-user-cheksiz/2a2cb10c-3170-5137-84c1-a19971a38055/scratchpad/aytilmagan/sub_uz.ass').read().split('[Events]')[0]
for L in ('uz','en','ru'):
    fs=64 if L=='uz' else 60
    HDR=re.sub(r'(Style: [SCFO],Inter ExtraBold,)\d+',lambda m:m.group(1)+str(fs),HDR0)
    HDR=HDR.replace('Style: O,','Style: Q,Inter ExtraBold,56,&H00FFE600,&H00FFFFFF,&H00301000,&H90000000,-1,0,0,0,100,100,0,0,1,4,3,8,80,80,190,1\nStyle: O,')
    ev='';sr='';n=1
    for i,x in enumerate(TX[L]):
        parts=[p.strip() for p in re.split(r'(?<=[.?!»"])\s+(?=[A-ZА-ЯЁ«"0-9])',x) if p.strip()]
        m=[]
        for p in parts:
            if m and len(m[-1])+len(p)<34: m[-1]+=' '+p
            else: m.append(p)
        tot=sum(len(p) for p in m); a=st[i]
        for p in m:
            b=a+dur[i]*len(p)/tot; sty='C' if who[i]=='D' else 'S'
            ev+=f"Dialogue: 0,{tt(a)},{tt(b-0.05)},{sty},,0,0,0,,{{\\fad(120,120)}}{p}\n"
            sr+=f"{n}\n{srt(a)} --> {srt(b-0.05)}\n{p}\n\n"; n+=1; a=b
    q=Q[L]; qs=[st[20]+dur[20]*0.27,st[20]+dur[20]*0.5,st[20]+dur[20]*0.78]; qend=st[22]+dur[22]
    for j in range(3):
        b=qs[j+1] if j<2 else qend
        ev+=f"Dialogue: 1,{tt(qs[j])},{tt(b)},Q,,0,0,0,,{{\\fad(200,{150 if j==2 else 0})}}{'\\N'.join(q[:j+1])}\n"
    open(f'sub_{L}.ass','w').write(HDR+'[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n'+ev)
    open(f'ikki-mehmon-{L}.srt','w').write(sr)
# avatar plates
from PIL import Image,ImageDraw,ImageFont
FB='/usr/share/fonts/opentype/inter/Inter-Bold.otf'; F=lambda s:ImageFont.truetype(FB,s)
for L,(a,b,c) in AVQ.items():
    im=Image.new('RGBA',(1080,440),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.rounded_rectangle([50,10,1030,430],radius=36,fill=(10,12,18,225)); d.rounded_rectangle([50,10,1030,24],radius=8,fill=(240,200,110))
    f1=F(80); d.text(((1080-d.textlength(a,font=f1))/2,55),a,font=f1,fill='white')
    f2=F(52); w=b.split(' '); lines=[];cur=''
    for x in w:
        s=(cur+' '+x).strip()
        if d.textlength(s,font=f2)<=940: cur=s
        else: lines.append(cur);cur=x
    lines.append(cur); y=165
    for l in lines: d.text(((1080-d.textlength(l,font=f2))/2,y),l,font=f2,fill=(255,236,160)); y+=64
    f3=F(56); d.text(((1080-d.textlength(c,font=f3))/2,y+18),c,font=f3,fill='white')
    im.save(f'avq_{L}.png')
print('ok')
