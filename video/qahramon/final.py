# «Birlik» yakuniy versiyalari (egasi, 2026-10-23): klip.py qoralamasi → fx.py effektlari → naqorat so'zlari (uz/ru/en)
# → avatar (3 s, savol plashkasi) → yakuniy karta (4 s) → 1080×1920, < 30 MB.
# python3 video/qahramon/final.py QORALAMA.mp4 ISH_DIR  → video/final/birlik/{1-telegram-birlik-uz,2-youtube-linkedin-birlik-en,3-instagram-facebook-birlik-ru}.mp4
import subprocess, sys, os, re
sys.path.insert(0, ".claude/skills/video-yig"); from yig import avq_plate
src, W = sys.argv[1], os.path.abspath(sys.argv[2]); os.makedirs(W, exist_ok=True)
Q = "video/qahramon/"; OUT = "video/final/birlik"; os.makedirs(OUT, exist_ok=True)
MUSIC = Q + "music/birlik.mp3"; SONG = 155.4; TAIL = 7.0
def run(c): subprocess.run(c, check=True)
# naqorat so'zlari: sozlar.ass (uz) asosida tarjimalar
TR = {"ru": {"BIRLIK": "ЕДИНСТВО", "YENGILMASDIR\\NHAR QADAMIMIZ!": "НЕПОБЕДИМ\\NКАЖДЫЙ НАШ ШАГ!", "O'N JANGGA\\NKIRSAK HAMKI": "ДАЖЕ ЕСЛИ\\NДЕСЯТЬ БИТВ",
              "KUCHAYUR\\NHAR DAM YURTIMIZ!": "НАША СТРАНА\\NЛИШЬ КРЕПНЕТ!", "HECH QACHON\\NYENGILMAS!": "НИКОГДА\\NНЕ ПОБЕЖДЁН!"},
      "en": {"BIRLIK": "UNITY", "YENGILMASDIR\\NHAR QADAMIMIZ!": "EVERY STEP\\NUNBEATABLE!", "O'N JANGGA\\NKIRSAK HAMKI": "EVEN IN\\NTEN BATTLES",
              "KUCHAYUR\\NHAR DAM YURTIMIZ!": "OUR NATION\\NGROWS STRONGER!", "HECH QACHON\\NYENGILMAS!": "NEVER\\NDEFEATED!"}}
AVQ = {"uz": "Siz-chi?|Sizning qahramoningiz kim?|Izohga yozing!", "ru": "А вы?|Кто ваш герой?|Напишите в комментариях!",
       "en": "And you?|Who is your hero?|Tell us in the comments!"}
NAME = {"uz": "1-telegram-birlik-uz", "en": "2-youtube-linkedin-birlik-en", "ru": "3-instagram-facebook-birlik-ru"}
fx = f"{W}/fx.mp4"
if not os.path.exists(fx): run(["python3", Q + "fx.py", src, fx])
# ovoz: qo'shiq + avatar/karta ostida qo'shiq boshidagi kirish qismi past ovozda, so'nib boradi
if not os.path.exists(f"{W}/mix.wav"): run(["ffmpeg", "-v", "error", "-y", "-i", MUSIC, "-i", MUSIC, "-filter_complex",
     f"[0:a]atrim=0:{SONG},bass=g=3:f=90:w=0.7,extrastereo=m=1.25,asetpts=PTS-STARTPTS[s];"
     f"[1:a]atrim=0:{TAIL},asetpts=PTS-STARTPTS,volume=0.55,afade=t=in:d=0.6,afade=t=out:st={TAIL - 2.5}:d=2.5[t];"
     "[s][t]concat=n=2:v=0:a=1,alimiter=limit=0.95[a]", "-map", "[a]", "-ar", "48000", f"{W}/mix.wav"])
for lang in ("uz", "ru", "en"):
    if os.path.exists(f"{OUT}/{NAME[lang]}.mp4") and "--qayta" not in sys.argv: continue   # tayyori qayta yig'ilmaydi
    ass = open(Q + "sozlar.ass").read()
    for a, b in TR.get(lang, {}).items(): ass = ass.replace("}" + a, "}" + b)
    open(f"{W}/s_{lang}.ass", "w").write(ass)
    run(["ffmpeg", "-v", "error", "-y", "-i", fx, "-vf", f"ass={W}/s_{lang}.ass,scale=1080:1920:flags=lanczos,fps=30,setsar=1,format=yuv420p",
         "-an", "-c:v", "libx264", "-crf", "18", f"{W}/main_{lang}.mp4"])
    avq_plate(AVQ[lang], f"{W}/avq_{lang}.png")
    run(["ffmpeg", "-v", "error", "-y", "-i", "video/avatar.mp4", "-i", f"{W}/avq_{lang}.png", "-filter_complex",
         "[0:v]trim=0:3,setpts=PTS-STARTPTS,scale=1080:1920:flags=lanczos,fps=30,setsar=1[a];[a][1:v]overlay=0:1200:enable='gte(t,0.3)',format=yuv420p[v]",
         "-map", "[v]", "-an", "-c:v", "libx264", "-crf", "18", "-r", "30", f"{W}/av_{lang}.mp4"])
    run(["ffmpeg", "-v", "error", "-y", "-i", f"video/end/end_{lang}.mp4", "-an", "-vf", "fps=30,setsar=1,format=yuv420p", "-c:v", "libx264", "-crf", "18", f"{W}/end_{lang}.mp4"])
    open(f"{W}/seq_{lang}.txt", "w").write("".join(f"file '{W}/{x}_{lang}.mp4'\n" for x in ("main", "av", "end")))
    run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{W}/seq_{lang}.txt", "-c", "copy", f"{W}/all_{lang}.mp4"])
    dur = SONG + TAIL; br = int(26 * 8 * 1024 / dur - 160)
    o = f"{OUT}/{NAME[lang]}.mp4"
    run(["ffmpeg", "-v", "error", "-y", "-i", f"{W}/all_{lang}.mp4", "-c:v", "libx264", "-b:v", f"{br}k", "-pass", "1", "-passlogfile", f"{W}/p_{lang}", "-an", "-f", "null", "/dev/null"])
    run(["ffmpeg", "-v", "error", "-y", "-i", f"{W}/all_{lang}.mp4", "-i", f"{W}/mix.wav", "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-b:v", f"{br}k",
         "-pass", "2", "-passlogfile", f"{W}/p_{lang}", "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", o])
    print(o, f"{os.path.getsize(o) / 1e6:.1f} MB")
