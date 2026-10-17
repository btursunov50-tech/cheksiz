import cv2,numpy as np,subprocess
cap=cv2.VideoCapture('seg00.mp4');W,H=1080,1920
p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r','30','-i','-','-c:v','libx264','-crf','16','-preset','fast','-pix_fmt','yuv420p','seg00b.mp4'],stdin=subprocess.PIPE)
yy,xx=np.mgrid[0:H,0:W]
ell=((((xx-248)/31.0)**2+((yy-690)/33.0)**2)<=1)|((xx>=234)&(xx<=263)&(yy>=606)&(yy<=665))
fe=cv2.GaussianBlur(ell.astype(np.float32),(0,0),3)[...,None]
i=0
while True:
    ok,f=cap.read()
    if not ok: break
    hsv=cv2.cvtColor(f,cv2.COLOR_BGR2HSV)
    h,s,v=cv2.split(hsv)
    m=ell&(h<=35)
    h2=h.copy();h2[m]=103
    s2=s.copy();s2[m]=np.clip(s[m].astype(int)+30,0,255)
    out=cv2.cvtColor(cv2.merge([h2,s2,v]),cv2.COLOR_HSV2BGR).astype(np.float32)
    out=(out*fe+f.astype(np.float32)*(1-fe))
    glow=cv2.GaussianBlur(m.astype(np.float32),(0,0),22)[...,None]*0.6
    out=np.clip(out+glow*np.array([90,60,0],np.float32),0,255).astype(np.uint8)
    p.stdin.write(out.tobytes());i+=1
p.stdin.close();p.wait();print(i)
