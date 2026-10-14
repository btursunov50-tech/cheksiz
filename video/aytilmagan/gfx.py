from PIL import Image,ImageDraw,ImageFont,ImageFilter
from data import NOTE,AVQ
FB='/usr/share/fonts/opentype/inter/Inter-Bold.otf'
F=lambda s:ImageFont.truetype(FB,s)
def fit(d,t,sz,mw):
    while d.textlength(t,font=F(sz))>mw and sz>20: sz-=2
    return F(sz)
for L in ('uz','ru','en'):
    for k,(txt,kind) in enumerate(zip(NOTE[L],('tag','book','gold'))):
        im=Image.new('RGBA',(1080,300),(0,0,0,0));d=ImageDraw.Draw(im)
        if kind=='gold':
            d.rounded_rectangle([60,40,1020,260],40,fill=(12,10,8,200));d.rounded_rectangle([60,40,1020,54],8,fill=(240,200,110,255))
            f=fit(d,txt,78,880);d.text(((1080-d.textlength(txt,font=f))/2,115),txt,font=f,fill=(255,214,110,255))
        else:
            # paper note
            sh=Image.new('RGBA',im.size,(0,0,0,0));ImageDraw.Draw(sh).rounded_rectangle([150,70,930,250],18,fill=(0,0,0,150))
            im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(12)))
            d.rounded_rectangle([140,60,920,240],18,fill=(244,232,205,245),outline=(150,110,60,255),width=4)
            f=fit(d,txt,66,700);d.text(((1060-d.textlength(txt,font=f))/2,118),txt,font=f,fill=(70,40,20,255))
        im.save(f'note{k+1}_{L}.png')
    im=Image.new('RGBA',(1080,380),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.rounded_rectangle([50,10,1030,370],radius=36,fill=(10,12,18,225)); d.rounded_rectangle([50,10,1030,24],radius=8,fill=(240,200,110))
    for s,sz,y,c in zip(AVQ[L],(80,52,56),(60,175,265),((255,255,255,255),(255,236,160,255),(255,255,255,255))):
        ff=fit(d,s,sz,930); d.text(((1080-d.textlength(s,font=ff))/2,y),s,font=ff,fill=c)
    im.save(f'avq_{L}.png')
