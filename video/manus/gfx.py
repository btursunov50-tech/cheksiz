import subprocess, math, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from data import LB
W,H,FPS=1080,1920,30
FX='/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf'; FB='/usr/share/fonts/opentype/inter/Inter-Bold.otf'
F=lambda p,s: ImageFont.truetype(p,s)
GOLD=(245,205,100); WHITE=(255,255,255); SOFT=(200,205,220); RED=(235,70,70); GREEN=(60,200,120)
def bg():
    im=Image.new('RGB',(W,H),(10,12,22)); d=ImageDraw.Draw(im)
    for y in range(H):
        t=y/H; c=(int(10+12*t),int(12+8*t),int(22+30*(1-abs(t-.5)*2)))
        d.line([(0,y),(W,y)],fill=c)
    try:
        m=Image.open('/home/user/cheksiz/video/mark.png').convert('RGBA'); m=m.resize((700,int(700*m.height/m.width)))
        a=m.split()[3].point(lambda v:int(v*0.07)); m.putalpha(a); im.paste(m,((W-m.width)//2,1080),m)
    except Exception as e: print(e)
    return im
BG=bg()
def ease(x): x=max(0,min(1,x)); return 1-(1-x)**3
def ctext(d,y,t,font,fill,alpha=1.0,maxw=860):
    s=font.size
    while d.textlength(t,font=font)>maxw and s>24: s-=2; font=ImageFont.truetype(font.path,s)
    x=(W-d.textlength(t,font=font))/2
    col=tuple(int(c*alpha+ (10)*(1-alpha)) for c in fill)
    d.text((x,y),t,font=font,fill=col)
def money(v):
    return "$"+f"{int(v):,}".replace(","," ")
def render(name,dur,draw):
    p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-c:v','libx264','-crf','16','-pix_fmt','yuv420p',name],stdin=subprocess.PIPE)
    for i in range(int(round(dur*FPS))):
        t=i/FPS; im=BG.copy(); d=ImageDraw.Draw(im); draw(d,t,im); p.stdin.write(im.tobytes())
    p.stdin.close(); p.wait()
def pop(t,t0): return ease((t-t0)/0.35)
for L,lb in LB.items():
    def g1(d,t,im):
        a=pop(t,0.1); ctext(d,330-40*(1-a),"META",F(FX,150),WHITE,a)
        v=2_000_000_000*ease((t-0.6)/2.8); a2=pop(t,0.6)
        ctext(d,560,money(v),F(FX,104),GOLD,a2)
        ctext(d,700,lb['g1a'],F(FB,40),SOFT,pop(t,1.2))
        a3=pop(t,2.6); ctext(d,810,"↓",F(FX,80),SOFT,a3); ctext(d,910,"MANUS",F(FX,130),WHITE,a3)
        if t>5.1:
            a4=pop(t,5.1); w=840; x0=(W-w)//2; y0=1110
            d.rounded_rectangle([x0,y0,x0+w,y0+120],radius=60,fill=tuple(int(c*a4+10*(1-a4)) for c in GREEN))
            ctext(d,y0+28,lb['g1b'],F(FX,58),WHITE)
    render(f'g1_{L}.mp4',7.9,g1)
    def g2(d,t,im):
        x=190; d.line([(x,380),(x,1230)],fill=(80,85,110),width=6)
        for k,(t0,(dt,tx),col,mark) in enumerate([(0.3,lb['d1'],GOLD,"✓"),(4.3,lb['d2'],RED,"✕")]):
            a=pop(t,t0)
            if a<=0: continue
            y=430+k*430
            d.ellipse([x-24,y-24+20,x+24,y+24+20],fill=tuple(int(c*a+10*(1-a)) for c in col))
            fa=F(FX,64); d.text((x+70,y-20),dt,font=fa,fill=tuple(int(c*a+10*(1-a)) for c in col))
            fb=F(FB,52); s=52
            while d.textlength(tx,font=fb)>700 and s>30: s-=2; fb=F(FB,s)
            d.text((x+70,y+70),tx,font=fb,fill=tuple(int(c*a+10*(1-a)) for c in WHITE))
            if k==1 and t>t0+0.6:
                b=pop(t,t0+0.6); r=int(70*(0.6+0.4*b)); cx,cy=W//2,y+260; col=tuple(int(c*b+10*(1-b)) for c in RED)
                d.line([(cx-r,cy-r),(cx+r,cy+r)],fill=col,width=22); d.line([(cx-r,cy+r),(cx+r,cy-r)],fill=col,width=22)
    render(f'g2_{L}.mp4',7.7,g2)
    def g3(d,t,im):
        ctext(d,330,lb['o1'],F(FX,64),GOLD,pop(t,0.1))
        v=500_000_000*ease((t-0.4)/2.4); ctext(d,520,money(v)+"+",F(FX,112),WHITE,pop(t,0.4))
        ctext(d,670,lb['o2'],F(FB,52),SOFT,pop(t,0.8))
        ctext(d,860,lb['o3'],F(FX,66),GREEN,pop(t,2.6))
        ctext(d,980,lb['o4'],F(FB,40),SOFT,pop(t,3.4))
    render(f'g3_{L}.mp4',6.6,g3)
    # label plates for screen scenes
    def plate(name,lines):
        im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im); y=150
        for t,f,col in lines:
            s=f.size
            while d.textlength(t,font=f)>840 and s>26: s-=2; f=F(f.path,s)
            tw=d.textlength(t,font=f); x=(W-tw)/2
            d.rounded_rectangle([x-30,y-12,x+tw+30,y+s+22],radius=26,fill=(8,10,18,215))
            d.text((x,y),t,font=f,fill=col+(255,)); y+=s+60
        im.save(name)
    plate(f'lb_agent1_{L}.png',[(lb['agent'][0]+"  ×",F(FX,62),(170,170,180))])
    plate(f'lb_agent2_{L}.png',[(lb['agent'][0]+"  ×",F(FX,62),(170,170,180)),(lb['agent'][1],F(FX,84),GOLD)])
    plate(f'lb_task_{L}.png',[(lb['task'],F(FX,56),WHITE)])
    plate(f'lb_out_{L}.png',[(lb['task'],F(FX,56),WHITE),(lb['out'],F(FX,60),GOLD)])
    plate(f'lb_cred_{L}.png',[(lb['cred'],F(FX,56),WHITE),(lb['cred2'],F(FB,46),GOLD)])
    plate(f'lb_tip_{L}.png',[(lb['tip'],F(FX,58),GOLD)])
    plate(f'lb_end_{L}.png',[(lb['end'][0],F(FX,58),WHITE),(lb['end'][1],F(FX,76),GOLD)])
print('ok')
