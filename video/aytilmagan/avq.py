from PIL import Image,ImageDraw,ImageFont
from data import AVQ
FB='/usr/share/fonts/opentype/inter/Inter-Bold.otf'; F=lambda s:ImageFont.truetype(FB,s)
for L in ('uz','ru','en'):
    im=Image.new('RGBA',(1080,440),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.rounded_rectangle([50,10,1030,430],radius=36,fill=(10,12,18,225)); d.rounded_rectangle([50,10,1030,24],radius=8,fill=(240,200,110))
    a,b,c=AVQ[L]; f1=F(80); d.text(((1080-d.textlength(a,font=f1))/2,55),a,font=f1,fill='white')
    f2=F(52); w=b.split(' '); lines=[];cur=''
    for x in w:
        s=(cur+' '+x).strip()
        if d.textlength(s,font=f2)<=940: cur=s
        else: lines.append(cur);cur=x
    lines.append(cur); y=165
    for l in lines: d.text(((1080-d.textlength(l,font=f2))/2,y),l,font=f2,fill=(255,236,160)); y+=64
    f3=F(56); d.text(((1080-d.textlength(c,font=f3))/2,y+18),c,font=f3,fill='white')
    im.save(f'avq_{L}.png'); print(L,len(lines))
