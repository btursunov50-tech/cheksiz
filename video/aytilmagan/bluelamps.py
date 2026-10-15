import cv2,numpy as np,sys
from lamps import L
def ss(x,a,b): t=np.clip((x-a)/(b-a),0,1); return t*t*(3-2*t)
def interp(kf,t):
    if t<kf[0][0]-0.15 or t>kf[-1][0]+0.15: return None
    if t<=kf[0][0]: return kf[0][1:]
    for a,b in zip(kf,kf[1:]):
        if a[0]<=t<=b[0]:
            u=(t-a[0])/(b[0]-a[0]); return tuple(x+(y-x)*u for x,y in zip(a[1:],b[1:]))
    return kf[-1][1:]
def recolor(img,ells):
    H,W=img.shape[:2]; reg=np.zeros((H,W),np.float32)
    for cx,cy,rx,ry in ells:
        cv2.ellipse(reg,(int(cx),int(cy)),(int(rx*1.15),int(ry*1.15)),0,0,360,1,-1)
    if reg.max()==0: return img
    reg=cv2.GaussianBlur(reg,(0,0),25)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV).astype(np.float32)
    h,s,v=hsv[...,0],hsv[...,1],hsv[...,2]
    warm=((h<=38)|(h>=170)).astype(np.float32)
    w=np.clip(reg*ss(v,110,205)*warm,0,1)
    core=ss(v,235,252)*reg
    out=hsv.copy()
    out[...,0]=h*(1-w)+101*w
    out[...,1]=s*(1-w)+np.maximum(s,190)*w*(1-0.75*core)
    out[...,2]=np.clip(v*(1-w)+np.minimum(255,v*1.05)*w,0,255)
    res=cv2.cvtColor(out.astype(np.uint8),cv2.COLOR_HSV2BGR).astype(np.float32)
    bright=(ss(v,215,250)*reg*warm)
    glow=(cv2.GaussianBlur(bright,(0,0),18)*0.55+cv2.GaussianBlur(bright,(0,0),60)*0.9)[...,None]*np.array([255,170,40],np.float32)*0.5
    return np.clip(res+glow,0,255).astype(np.uint8)
if __name__=='__main__':
    k=int(sys.argv[1]); src=f'p{k}.mp4'; dst=f'b{k}.mp4'
    cap=cv2.VideoCapture(src); fps=cap.get(5); W=int(cap.get(3));H=int(cap.get(4))
    vw=cv2.VideoWriter(dst,cv2.VideoWriter_fourcc(*'mp4v'),fps,(W,H)); i=0
    while True:
        ok,f=cap.read()
        if not ok: break
        t=i/fps; ells=[e for e in (interp(kf,t) for kf in L.get(k,[])) if e]
        vw.write(recolor(f,ells)); i+=1
    vw.release()
