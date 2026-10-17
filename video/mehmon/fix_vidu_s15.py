import cv2,numpy as np,random,math,subprocess,sys
cap=cv2.VideoCapture('in.mp4');fps=cap.get(5)
W,H=720,1280
out=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r',str(fps),'-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','17','-r','24','out.mp4'],stdin=subprocess.PIPE)
random.seed(5)
parts=[[random.uniform(120,620),random.uniform(650,1250),random.uniform(2,4.5),random.uniform(-.3,.3),random.uniform(-1.2,-.4),random.uniform(0,6.3)] for _ in range(26)]
i=0;dbg=None
while True:
    ok,f=cap.read()
    if not ok: break
    hsv=cv2.cvtColor(f,cv2.COLOR_BGR2HSV)
    V=hsv[:,:,2].astype(np.float32);S=hsv[:,:,1]
    loc=cv2.blur(V,(31,31))
    dark=(V<70).astype(np.uint8)
    closed=cv2.morphologyEx(dark,cv2.MORPH_CLOSE,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(21,21)))
    dfrac=cv2.blur(dark.astype(np.float32),(17,17))
    m=((closed==1)&(dark==0)&(V>60)&(S<130)&(dfrac>0.25)).astype(np.uint8)
    reg=np.zeros_like(m);reg[640:1130,120:560]=1
    Hh=hsv[:,:,0]
    navy=((Hh>=95)&(Hh<=135)&(S>80)&(V>35)).astype(np.float32)
    skin=((Hh<=25)&(S>35)&(S<190)&(V>70)).astype(np.float32)
    nearcup=cv2.blur(navy,(45,45))>0.06
    nearface=cv2.blur(skin,(19,19))>0.22
    reg[760:900,330:420]=0  # quloq atrofi
    m=m*reg*(~nearcup).astype(np.uint8)*(~nearface).astype(np.uint8)
    m=cv2.morphologyEx(m,cv2.MORPH_CLOSE,np.ones((5,5),np.uint8))
    mf=m.astype(np.float32)
    glow=cv2.GaussianBlur(mf,(0,0),6)*0.9+cv2.GaussianBlur(mf,(0,0),2)*0.8
    br=0.75+0.25*math.sin(i/fps*2*math.pi/2.5)   # sekin "nafas"
    neon=np.array([255,167,51],np.float32)  # chiroq rangi (H=103)        # BGR ko'k-moviy
    g=f.astype(np.float32)
    core=mf[...,None]
    g=g*(1-core*0.85)+core*0.85*neon*br
    g=g+np.clip(glow,0,1)[...,None]*neon*0.55*br
    # zarrachalar
    lay=np.zeros_like(g)
    for q in parts:
        x=q[0]+q[3]*i;y=(q[1]+q[4]*i-650)%600+650;a=0.5+0.5*math.sin(q[5]+i/6)
        cv2.circle(lay,(int(x),int(y)),int(q[2]),(255,167,51),-1)
        lay_a=a
    lay=cv2.GaussianBlur(lay,(0,0),2.2)
    g=np.clip(g+lay*0.8,0,255).astype(np.uint8)
    if i==48: dbg=g.copy(); dm=m.copy()
    # suv belgisini kesib tashlash: chap-yuqori 1015x1805 (watermark y>=1855)
    c=g[0:1805,32:1047]
    c=cv2.resize(c,(W,H),interpolation=cv2.INTER_AREA)
    out.stdin.write(c.tobytes());i+=1
out.stdin.close();out.wait()
cv2.imwrite('dbg.jpg',cv2.resize(dbg[600:1350,80:640],None,fx=0.8,fy=0.8))
cv2.imwrite('mask.jpg',cv2.resize(dm[600:1350,80:640]*255,None,fx=0.5,fy=0.5))
print(i)
