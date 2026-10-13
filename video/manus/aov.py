import subprocess, sys
from PIL import Image, ImageDraw, ImageFont
from data import LB
W,H=1080,1920
FX='/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf'; FB='/usr/share/fonts/opentype/inter/Inter-Bold.otf'
F=lambda p,s: ImageFont.truetype(p,s)
def ease(x): x=max(0,min(1,x)); return 1-(1-x)**3
for L,lb in LB.items():
    rd=subprocess.Popen(['ffmpeg','-v','error','-i','a_base.mp4','-vf','tpad=stop_mode=clone:stop_duration=0.2','-t','7.9','-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
    wr=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','1080x1920','-r','30','-i','-','-c:v','libx264','-crf','16','-pix_fmt','yuv420p',f'a_{L}.mp4'],stdin=subprocess.PIPE)
    n=0
    while True:
        b=rd.stdout.read(W*H*3)
        if len(b)<W*H*3: break
        t=n/30; im=Image.frombytes('RGB',(W,H),b).convert('RGBA'); ov=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(ov)
        a=ease((t-0.3)/0.4)
        if a>0:
            d.rounded_rectangle([90,600,990,890],radius=40,fill=(8,10,20,int(200*a)))
            def c(y,txt,f,col):
                tw=d.textlength(txt,font=f); d.text(((W-tw)/2,y),txt,font=f,fill=col+(int(255*a),))
            c(625,"META",F(FX,64),(255,255,255))
            v=int(2_000_000_000*ease((t-0.6)/2.6)); c(705,"$"+f"{v:,}".replace(","," "),F(FX,96),(245,205,100))
            c(825,lb['g1a'],F(FB,34),(200,205,220))
        g=ease((t-5.1)/0.35)
        if g>0:
            f=F(FX,56); tx=lb['g1b']; tw=d.textlength(tx,font=f); x0=(W-tw)/2-50
            d.rounded_rectangle([x0,925,x0+tw+100,1035],radius=55,fill=(60,200,120,int(240*g)))
            d.text((x0+50,948),tx,font=f,fill=(255,255,255,int(255*g)))
        im.alpha_composite(ov); wr.stdin.write(im.convert('RGB').tobytes()); n+=1
    wr.stdin.close(); wr.wait(); print(L,n)
