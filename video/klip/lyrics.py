import json
UZ=["Kunduzimdan ketdi halovat,","Hali-beri o'ziga kelmaydi.","Dard bo'lsa ham ozorlarimga,","Yuragingni qaytib bermayman.",
"Bo'ldi, bari tamom, xo'p, deya,","Ketar bo'lsang, kimnidir suya,","Qolsam hamki hajringda kuya,","Yuragingni qaytib bermayman.",
"So'ra, mendan jonim sengadir,","Sog'inchlarim sabrim yengadir.","Alishsang ham meni kimgadir,","Yuragingni qaytib bermayman.",
"Dilga faqat hijron tutsang ham,","O'zgalardan mehr kutsang ham,","Kunlar kelib tashlab ketsang ham,","Yuragingni qaytib bermayman.",
"Sevgim qalbda jo'sh urar shahdli,","Bil, turaman so'zimda ahdli.","Qilmasang ham sen meni baxtli,","Yuragingni qaytib bermayman."]
RU=["Покой ушёл из моих дней,","и никак не вернётся.","Пусть даже это причиняет боль,","твоё сердце я не верну.",
"«Всё, конец», — скажешь ты,","уходишь — полюби кого-то другого,","пусть я сгорю в разлуке с тобой,","твоё сердце я не верну.",
"Спроси: моя душа — твоя,","тоска сильнее терпения.","Даже если променяешь меня на кого-то,","твоё сердце я не верну.",
"Даже если даришь сердцу лишь разлуку,","даже если ждёшь любви от других,","даже если однажды бросишь меня,","твоё сердце я не верну.",
"Любовь в груди кипит и бьётся,","знай: я держу своё слово.","Даже если счастья мне не дашь,","твоё сердце я не верну."]
EN=["Peace has left my days,","and it won't come back any time soon.","Even if it only brings me pain,","I won't give your heart back.",
"\"That's it, it's over,\" you say,","if you're leaving, go love someone else,","even if I'm left burning, missing you,","I won't give your heart back.",
"Ask me: my soul belongs to you,","my longing is stronger than my patience.","Even if you trade me for someone else,","I won't give your heart back.",
"Even if you give my heart only parting,","even if you seek love from others,","even if one day you leave me,","I won't give your heart back.",
"My love burns strong in my heart,","know that I keep my word.","Even if you never make me happy,","I won't give your heart back."]
# (start, line index); estimated from vocal-band energy dips, 2:06 = line 13 confirmed by the owner
T=[(21.0,0),(26.0,1),(31.0,2),(36.0,3),(40.5,4),(46.0,5),(51.0,6),(56.0,7),(61.5,8),(66.5,9),(71.5,10),(76.5,11),
   (81.5,12),(86.5,13),(91.5,14),(96.5,15),
   (121.0,12),(126.0,13),(131.5,14),(137.0,15),
   (141.5,16),(146.5,17),(151.5,18),(156.5,19),
   (162.5,6),(167.5,15),(172.5,6),(177.5,15),
   (182.5,6),(187.5,15),(192.5,6),(197.5,15)]  # 2:42 = outro, confirmed by the owner
ENDS={15:102.0,19:161.5,31:203.0}
cues=[]
for k,(s,i) in enumerate(T):
    nxt=T[k+1][0] if k+1<len(T) else 203.0
    e=min(nxt-0.25, s+5.6) if k not in ENDS else ENDS[k]
    if k==15: e=102.0
    if k==19: e=161.5
    cues.append((s-0.2,e,i))
json.dump(cues,open('cues.json','w'))
def ts(x): h=int(x//3600);m=int(x%3600//60);s=x%60; return f"{h:02}:{m:02}:{int(s):02},{int(round((s%1)*1000)):03}".replace(",1000",",999")
def asst(x): m=int(x//60); s=x%60; return f"0:{m:02}:{s:05.2f}"
for L,LY in (('uz',UZ),('ru',RU),('en',EN)):
    open(f'klip-{L}.srt','w').write(''.join(f"{n+1}\n{ts(s)} --> {ts(e)}\n{LY[i]}\n\n" for n,(s,e,i) in enumerate(cues)))
def ass(name,W,H,size,marginv,LY,offset=0,maxt=None):
    hdr=f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: S,Inter,{size},&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,-1,0,0,0,100,100,0,0,1,{max(2,size//16)},1,2,60,60,{marginv},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    ev=''
    for s,e,i in cues:
        if maxt and s>=maxt: continue
        if maxt: e=min(e,maxt)
        ev+=f"Dialogue: 0,{asst(s)},{asst(e)},S,,0,0,0,,{{\\fad(200,200)}}{LY[i]}\n"
    open(name,'w').write(hdr+ev)
ass('full_en.ass',1280,720,40,40,EN)
for L,LY in (('uz',UZ),('ru',RU),('en',EN)):
    ass(f'short_{L}.ass',1080,1920,52,560,LY,maxt=52)   # bottom margin 560 -> text sits just under the 16:9 picture
print(len(cues))
