import cv2, numpy as np, sys, os, subprocess
src, out = sys.argv[1], sys.argv[2]
W,H,F,D=720,1280,30,6.2
im=cv2.resize(cv2.imread(src),(W,H)).astype(np.float32)/255
g=cv2.cvtColor((im*255).astype(np.uint8),cv2.COLOR_BGR2GRAY).astype(np.float32)/255
g=np.clip((g-0.05)*1.25,0,1)**0.9
dark=np.array([10,18,32])/255; gold=np.array([90,200,255])/255; light=np.array([200,240,255])/255
duo=np.where(g[...,None]<0.6, dark+(gold-dark)*(g[...,None]/0.6), gold+(light-gold)*((g[...,None]-0.6)/0.4))*0.85
bl=cv2.GaussianBlur(duo,(0,0),18); duo=duo+np.clip(bl-0.45,0,1)*0.8
yy,xx=np.mgrid[:H,:W]; v=1-np.clip(((xx-W/2)/(W*0.75))**2+((yy-H/2)/(H*0.7))**2,0,1); duo*= (0.35+0.65*v[...,None])
# katta konturlar
b=cv2.GaussianBlur((g*255).astype(np.uint8),(0,0),3); e=cv2.Canny(b,30,70)
n,lab,st,_=cv2.connectedComponentsWithStats(e,8); keep=np.isin(lab,[i for i in range(1,n) if st[i,4]>150]).astype(np.float32)
rng=np.random.default_rng(5)
order=(xx/W*0.5+yy/H*0.5)+rng.random((H,W))*0.08          # chizish tartibi (diagonal)
noise=cv2.GaussianBlur(rng.random((H,W)).astype(np.float32),(0,0),6); noise=(noise-noise.min())/(noise.max()-noise.min())
dis=0.55*noise+0.45*(yy/H)
P=70000
pi=rng.integers(0,H*W,P); py,px=pi//W,pi%W; pc=duo[py,px]; pd=dis[py,px]; pv=rng.random(P)
os.makedirs(out+'_f',exist_ok=True)
E=lambda u: np.clip(u,0,1)**2*(3-2*np.clip(u,0,1))
for k in range(int(D*F)):
    t=k/F; fr=np.zeros((H,W,3),np.float32); fr[:]=dark*0.6
    dr=E(t/1.3)                                   # 0–1.3 s chiziq chiziladi
    lm=keep*(order<dr*1.05)
    ph=E((t-1.0)/1.0)                              # 1–2 s rasm ochiladi
    dz=E((t-3.4)/2.0)                              # 3.4–5.1 s qumga aylanadi
    alive=(dis>dz*1.05).astype(np.float32) if dz>0 else 1
    z=1+0.04*min(t,3.4)/3.4                        # sekin push-in
    M=cv2.getRotationMatrix2D((W/2,H/2),0,z)
    img=cv2.warpAffine(duo,M,(W,H)); lmz=cv2.warpAffine(lm,M,(W,H))
    glow=cv2.GaussianBlur(lmz,(0,0),4)*1.3+cv2.GaussianBlur(lmz,(0,0),12)
    lay=img*ph+lmz[...,None]*light*(1-0.5*ph)+glow[...,None]*gold*(0.9-0.5*ph)
    fr=fr*(1-ph*0) + lay*(alive[...,None] if dz>0 else 1)
    if dz>0:
        go=pd<dz*1.05; tt=np.clip((t-3.4)-pd*2.0,0,None)
        sx=(px+np.sin(pv*20+t*3)*12*tt).astype(int); sy=(py+ (120+260*pv)*tt*tt*1.6 + 30*tt).astype(int)
        ok=go&(sx>=0)&(sx<W)&(sy>=0)&(sy<H)&(tt<2.5)
        c=pc[ok]*1.2+gold*0.5
        for dx,dy in ((0,0),(1,0),(0,1),(1,1)):
            fr[np.clip(sy[ok]+dy,0,H-1),np.clip(sx[ok]+dx,0,W-1)]=np.maximum(fr[np.clip(sy[ok]+dy,0,H-1),np.clip(sx[ok]+dx,0,W-1)],c)
    fr+=(rng.random((H,W,1))-0.5)*0.04
    cv2.imwrite(f'{out}_f/{k:04d}.jpg',(np.clip(fr,0,1)*255).astype(np.uint8))
subprocess.run(['ffmpeg','-loglevel','error','-y','-framerate',str(F),'-i',f'{out}_f/%04d.jpg','-c:v','libx264','-crf','20','-pix_fmt','yuv420p',out],check=True)
