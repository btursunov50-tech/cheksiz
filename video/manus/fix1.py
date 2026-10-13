import cv2, numpy as np, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter
cap=cv2.VideoCapture('v1.mp4'); fps=24
K=[(0,629,370.5,1.0),(4.6,634,371,1.02)]
def key(t):
    for (t0,x0,y0,s0),(t1,x1,y1,s1) in zip(K,K[1:]):
        if t<=t1:
            a=(t-t0)/(t1-t0); return x0+(x1-x0)*a,y0+(y1-y0)*a,s0+(s1-s0)*a
    return K[-1][1:]
out=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','720x1280','-r','24','-i','-','-c:v','libx264','-crf','14','-pix_fmt','yuv420p','v1fix.mp4'],stdin=subprocess.PIPE)
n=0
cap2=cv2.VideoCapture('v1.mp4'); cap2.set(cv2.CAP_PROP_POS_FRAMES,29); _,fr=cap2.read(); g0=cv2.cvtColor(fr,cv2.COLOR_BGR2GRAY); T=g0[361:381,604:656]; prev=(630,371)
while n<int(4.6*fps):
    ok,f=cap.read()
    if not ok: break
    t=n/fps; _,_,s=key(t)
    g=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY); x0,y0=int(prev[0])-60,int(prev[1])-35
    R=cv2.matchTemplate(g[y0:y0+70,x0:x0+120],T,cv2.TM_CCOEFF_NORMED); _,mv,_,ml=cv2.minMaxLoc(R)
    if mv>0.5: prev=(x0+ml[0]+26,y0+ml[1]+10)
    cx,cy=prev
    im=Image.fromarray(cv2.cvtColor(f,cv2.COLOR_BGR2RGB))
    w,h=int(29*s),int(10*s)
    col=tuple(int(v) for v in np.median(np.array(im)[int(cy)+10:int(cy)+14,int(cx)-20:int(cx)+20].reshape(-1,3),axis=0))
    m=Image.new('L',im.size,0); ImageDraw.Draw(m).rounded_rectangle([cx-w,cy-h,cx+w,cy+h],radius=6,fill=255); m=m.filter(ImageFilter.GaussianBlur(2))
    im.paste(Image.new('RGB',im.size,col),(0,0),m)
    fnt=ImageFont.truetype('/usr/share/fonts/opentype/inter/Inter-SemiBold.otf',int(18*s))
    d=ImageDraw.Draw(im); tw=d.textlength('tahlili',font=fnt); d.text((cx-tw/2,cy-int(11*s)),'tahlili',font=fnt,fill=(245,245,250))
    out.stdin.write(im.tobytes()); n+=1
out.stdin.close(); out.wait(); print(n)
