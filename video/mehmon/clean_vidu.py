import cv2,numpy as np,subprocess,sys
src,out,subs=sys.argv[1],sys.argv[2],sys.argv[3]=='1'
cap=cv2.VideoCapture(src);W,H=1080,1920
p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r','24','-i','-','-c:v','libx264','-crf','16','-pix_fmt','yuv420p',out],stdin=subprocess.PIPE)
i=0
while True:
    ok,f=cap.read()
    if not ok: break
    if subs:
        roi=f[1340:1480,300:780]
        hsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
        m=((hsv[:,:,2]>200)&(hsv[:,:,1]<60)).astype(np.uint8)*255
        m=cv2.dilate(m,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(19,19)))
        full=np.zeros(f.shape[:2],np.uint8);full[1340:1480,300:780]=m
        f=cv2.inpaint(f,full,9,cv2.INPAINT_TELEA)
        if i==48: cv2.imwrite('cleanchk.png',f[1250:1560,250:830])
    c=f[0:1805,32:1047]
    c=cv2.resize(c,(W,H),interpolation=cv2.INTER_LANCZOS4)
    p.stdin.write(c.tobytes());i+=1
p.stdin.close();p.wait();print(i)
