from PIL import Image,ImageDraw,ImageFont,ImageFilter
from data import BUBBLE,ADVICE,AVQ
FB='/usr/share/fonts/opentype/inter/Inter-Bold.otf'; FS='/usr/share/fonts/opentype/inter/Inter-SemiBold.otf'
F=lambda p,s:ImageFont.truetype(p,s)
def wrap(d,t,f,mw):
    L=[];cur=''
    for x in t.split():
        s=(cur+' '+x).strip()
        if d.textlength(s,font=f)<=mw: cur=s
        else: L.append(cur);cur=x
    return L+[cur]
def fit(d,t,p,sz,mw):
    while d.textlength(t,font=F(p,sz))>mw and sz>20: sz-=2
    return F(p,sz)
for L in ('uz','ru','en'):
    # mother's question as a chat bubble
    im=Image.new('RGBA',(1080,560),(0,0,0,0));d=ImageDraw.Draw(im)
    f=F(FS,58);lines=wrap(d,BUBBLE[L][1],f,720); bh=70+len(lines)*72+50
    sh=Image.new('RGBA',im.size,(0,0,0,0));ImageDraw.Draw(sh).rounded_rectangle([150,96,1010,96+bh],40,fill=(0,0,0,170))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(14)))
    d.text((170,22),BUBBLE[L][0],font=F(FB,44),fill=(140,255,150,255))
    d.rounded_rectangle([140,86,1000,86+bh],40,fill=(220,255,200,250))
    d.polygon([(960,86+bh-40),(1030,86+bh+6),(940,86+bh-4)],fill=(220,255,200,250))
    y=131
    for l in lines: d.text((185,y),l,font=f,fill=(20,40,20,255)); y+=72
    for dx in (0,22): d.line([(880+dx,86+bh-48),(895+dx,86+bh-33),(925+dx,86+bh-68)],fill=(40,170,70,255),width=7)
    im.save(f'ov_savol_{L}.png')
    # final advice
    im=Image.new('RGBA',(1080,420),(0,0,0,0));d=ImageDraw.Draw(im)
    d.rounded_rectangle([60,20,1020,400],40,fill=(12,10,8,200));d.rounded_rectangle([60,20,1020,34],8,fill=(240,200,110,255))
    for t,sz,y,c in zip(ADVICE[L],(76,104,76),(70,165,290),((255,255,255,255),(255,214,110,255),(255,255,255,255))):
        ff=fit(d,t,FB,sz,900);d.text(((1080-d.textlength(t,font=ff))/2,y),t,font=ff,fill=c)
    im.save(f'ov_maslahat_{L}.png')
    # avatar plate
    im=Image.new('RGBA',(1080,380),(0,0,0,0));d=ImageDraw.Draw(im)
    d.rounded_rectangle([50,10,1030,370],radius=36,fill=(10,12,18,225)); d.rounded_rectangle([50,10,1030,24],radius=8,fill=(240,200,110))
    for s,sz,y,c in zip(AVQ[L],(80,62,56),(60,170,265),((255,255,255,255),(255,236,160,255),(255,255,255,255))):
        ff=fit(d,s,FB,sz,920); d.text(((1080-d.textlength(s,font=ff))/2,y),s,font=ff,fill=c)
    im.save(f'avq_{L}.png')
