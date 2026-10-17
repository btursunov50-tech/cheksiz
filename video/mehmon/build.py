import subprocess,re,os
M='/tmp/claude-0/-home-user-cheksiz/2a2cb10c-3170-5137-84c1-a19971a38055/scratchpad/mehmon'
IMG='/home/user/cheksiz/video/mehmon/img'
OFF=1.0
dur=[5.38,2.06,5.56,2.92,4.62,3.35,8.52,1.56,4.54,2.53,5.36,2.19,8.64,2.86,7.10,1.57,8.37,1.98,8.28,1.16,8.77,4.99,6.02,9.03]
st=[];t=0
for d in dur: st.append(t+OFF); t+=d+0.3
MAIN=round(st[-1]+dur[-1]+1.6,2)
who=['D','Y','D','Y','D','Y','D','Y','D','Y','D','Y','D','Y','D','Y','D','Y','D','Y','D','Y','D','D']
txt=["Bugun kechasi eshigingni ikki mehmon taqillatadi.","Ikkitami? Kim ekan?","Birinchisi kichkina. Boshini egib turibdi. Qo'lida qog'oz.","Kirsin. Mehmon otangdek ulug'.","Qog'ozda yozilgan: mijozga noto'g'ri fayl yubording.","Ha... bo'ladi-da. Ertaga tuzataman.","Uning orqasidan ikkinchisi keldi. Katta. Sovuq. Faqat ostonada turmoqchi.","Tursin. Nima bo'pti?","Endi senga pichirlayapti: «Sen doim shunaqasan.»","Balki rostdir...","Endi to'rga o'tib oldi: «Seni ishdan bo'shatishadi.»","Bo'shatishsa-chi? Uydagilarga nima deyman?","Tun. Birinchi mehmon allaqachon uxlab qoldi. Ikkinchisi esa yostig'ing yonida.","Hoy, bu mening uyim-ku! Ketsin!","Ketmaydi. Uni o'zing choyga taklif qilding. Endi u mehmon emas, xo'jayin.","U o'zi kim?","Uning ismi «Men yaramasman». U doim xatoning orqasidan keladi.","Birinchisi-chi? Xato?","Xato haqiqiy mehmon. Uni kutib ol: tan ol, uzr so'ra, tuzat. Ertalab o'zi ketadi.","Ikkinchisi-chi?","Unga uchta savol ber. Aniq nima bo'ldi? Nimani o'zim o'ylab topyapman? Hozir qanday bitta qadam qila olaman?","Rahbarim faqat «faylni qayta yubor» degan edi...","Ana. Fakt shu. Qolgani mehmonning gapi.","Xato hammaning eshigini taqillatadi. Uning sherigini ichkariga kiritish-kiritmaslikni esa o'zing tanlaysan."]
# scenes: (clip, first line index, usable a,b, kb image)
SC=[('s01',0,0,8,'01_eshik'),('s02',1,0,8,'ref_yigit'),('s03',2,0,8,'ref_xato'),('s04',3,0,8,'04_kirsin'),('s05',4,0,7,'05_qogoz'),('s06',5,0,8,'06_xijolat'),('s07',6,0,5,'ref_soya'),('s08',8,0,8,'08_pichirlash'),('s09',10,0,8,'09_torda'),('s10',12,0,6.5,'10_tun'),('s11',13,0,8,'11_ketsin'),('s12',14,0,8,'ref_dono'),('s13',16,0,8,'13_ismi'),('s14',18,0,8,'14_ketadi'),('KB',20,0,0,'ref_dono'),('s15',21,0,8,'15_xabar'),('s16',23,0,8,'16_tong')]
E=['-c:v','libx264','-crf','16','-preset','fast','-pix_fmt','yuv420p','-an','-r','30']
def run(a): subprocess.run(a,check=True)
def kb(img,T,out):
    n=int(round(T*30))
    run(['ffmpeg','-v','error','-y','-loop','1','-i',f'{IMG}/{img}.webp','-vf',f"scale=2160:3840,zoompan=z='1.0+0.06*on/{n}':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2':d={n}:s=1080x1920:fps=30,setsar=1",'-frames:v',str(n)]+E+[out])
segs=[];cuts=[]
for k,(c,li,a,b,img) in enumerate(SC):
    s0=0 if k==0 else st[li]
    s1=st[SC[k+1][1]] if k+1<len(SC) else MAIN
    T=round(s1-s0,3); out=f'seg{k:02}.mp4'
    if c=='KB': kb(img,T,out)
    else:
        L=b-a; f=f'{M}/clips/{c}.mp4'
        if T<=L:
            run(['ffmpeg','-v','error','-y','-ss',str(a),'-t',str(T),'-i',f,'-vf','scale=1080:1920:flags=lanczos,setsar=1,fps=30']+E+[out])
        elif T<=L/0.8:
            fac=T/L
            run(['ffmpeg','-v','error','-y','-ss',str(a),'-t',str(L),'-i',f,'-vf',f'setpts={fac}*PTS,scale=1080:1920:flags=lanczos,setsar=1,fps=30','-t',str(T)]+E+[out])
        else:
            Lv=L/0.8
            run(['ffmpeg','-v','error','-y','-ss',str(a),'-t',str(L),'-i',f,'-vf','setpts=1.25*PTS,scale=1080:1920:flags=lanczos,setsar=1,fps=30','-t',str(Lv)]+E+['p1.mp4'])
            kb(img,T-Lv,'p2.mp4')
            open('pl.txt','w').write("file 'p1.mp4'\nfile 'p2.mp4'\n")
            run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','pl.txt','-c','copy',out])
    segs.append(out)
    if k: cuts.append(round(s0,2))
    print(k,c,T)
open('segs.txt','w').write(''.join(f"file '{s}'\n" for s in segs))
run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','segs.txt','-c','copy','raw.mp4'])
open('cuts.txt','w').write(' '.join(map(str,cuts)))
# subtitles
def tt(x): return f"0:{int(x//60):02}:{x%60:05.2f}"
def srt(x): return f"00:{int(x//60):02}:{int(x%60):02},{int(round((x%1)*1000)):03}"
HDR=open(f'{M}/../aytilmagan/sub_uz.ass').read().split('[Events]')[0]
HDR=HDR.replace('Style: O,','Style: Q,Inter ExtraBold,58,&H00FFE600,&H00FFFFFF,&H00301000,&H90000000,-1,0,0,0,100,100,0,0,1,4,3,8,80,80,190,1\nStyle: O,')
ev='';sr='';n=1
for i,x in enumerate(txt):
    parts=[p.strip() for p in re.split(r'(?<=[.?!»])\s+(?=[A-ZÀ-ÿ«OUQ])',x) if p.strip()]
    # merge very short parts
    m=[]
    for p in parts:
        if m and len(m[-1])+len(p)<34: m[-1]+=' '+p
        else: m.append(p)
    tot=sum(len(p) for p in m); a=st[i]
    for p in m:
        d=dur[i]*len(p)/tot; b=a+d
        sty='C' if who[i]=='D' else 'S'
        ev+=f"Dialogue: 0,{tt(a)},{tt(b-0.05)},{sty},,0,0,0,,{{\\fad(120,120)}}{p}\n"
        sr+=f"{n}\n{srt(a)} --> {srt(b-0.05)}\n{p}\n\n"; n+=1; a=b
# three questions (top)
q=["1. Aniq nima bo'ldi?","2. Nimani o'zim o'ylab topyapman?","3. Hozir qanday bitta qadam qila olaman?"]
qs=[st[20]+dur[20]*0.27,st[20]+dur[20]*0.5,st[20]+dur[20]*0.78]
qend=st[22]+dur[22]
body=''
for j in range(3):
    lines='\\N'.join(q[:j+1])
    a=qs[j]; b=qs[j+1] if j<2 else qend
    ev+=f"Dialogue: 1,{tt(a)},{tt(b)},Q,,0,0,0,,{{\\fad({200 if True else 0},{150 if j==2 else 0})}}{lines}\n"
open('sub_uz.ass','w').write(HDR+'[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n'+ev)
open('ikki-mehmon-uz.srt','w').write(sr)
print('MAIN',MAIN,'cuts',cuts)
