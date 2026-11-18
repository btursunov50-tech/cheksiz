#!/usr/bin/env python3
"""«O'zligim» yakuniy 3 versiya: build2.py natijasidan (fx.mp4) + avatar + yakuniy karta + so'zlar (uz/ru/en) + bot chaqiruvi.
python3 video/ozlik/final.py <work>  → video/final/ozligim/ (1-telegram-ozligim-uz.mp4, 2-youtube-linkedin-ozligim-en.mp4, 3-instagram-facebook-ozligim-ru.mp4, *.srt)"""
import os, sys, ast, subprocess
from concurrent.futures import ThreadPoolExecutor
from PIL import Image, ImageDraw, ImageFont
R = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")); Q = f"{R}/video/ozlik"; W0 = sys.argv[1]
OUT = f"{R}/video/final/ozligim"; os.makedirs(OUT, exist_ok=True)
def run(c): subprocess.run(c, check=True)
src = open(f"{Q}/build2.py").read()
def _grab(a, name):
    i = src.index("[", a); depth = 0
    for j in range(i, len(src)):
        depth += src[j] == "["; depth -= src[j] == "]"
        if depth == 0: return src[i:j + 1]
UZ = ast.literal_eval(_grab(src.index("LY = ["), "LY")); LINES = ast.literal_eval(_grab(src.index("LINES = ["), "LINES"))
RU = ["Я искал себя вдали от самого себя,", "Я увидел Тебя, о Истина, в садах моих слёз.",
      "Я спрашивал о Тебе солнце в небе и луну в ночи,", "а Ты был в моём сердце — зачем же я прошёл столько дорог?",
      "Я думал, что я — море, а сам жаждал одной капли,", "думал, что познал мир, а себя так и не узнал.",
      "Я прочёл тысячу книг, но не понял одной строки:", "«Познай себя» — всю жизнь я не мог дорасти до этих слов.",
      "О любовь, сожги меня, пусть из сердца прорастут цветы,", "пусть пыль с моей души осыплется в один миг.",
      "Я хотел дойти до Тебя, но сбился с пути,", "а в день, когда отказался от своего «я», соединился с Истиной.",
      "О сердце, в тебе спрятана тысяча и одна вселенная,", "в день, когда ты познаешь себя, откроется твоя тайная дверь.",
      "Я думал, это любовь, а это было желание моего эго,", "я ждал верности от другого, а сам был неверен.",
      "Я искал вину в мире и считал себя чистым,", "не глядя в зеркало, называл себя правым.",
      "Я бился головой о камень, жаловался стенам,", "ища Истину в небе, я отдалился от своего сердца.",
      "Кто не может победить себя, для того тысяча побед — мираж,", "победивший своё эго — величайший победитель.",
      "Свеча горит и гаснет, но свет остаётся в памяти,", "человек уходит, а слово его остаётся в следах добра.",
      "Зачем ты копил богатство? Однажды оно выпадет из рук.", "Пусть останутся твоя доброта и доброе имя на пройденных дорогах.",
      "Прости, человек, преврати свой гнев в любовь,", "смени тьму в сердце на крупицу света.",
      "Ты гость в этом мире, не притязай на вечность,", "пока не пришла смерть, человек, не потеряй себя.", "Эй! Эй!"]
EN = ["I searched for myself far away from myself,", "I saw You, O Truth, in the gardens of my tears.",
      "I asked the sun in the sky and the moon in the night,", "but You were in my heart. Why did I walk so far?",
      "I thought I was the sea, yet I longed for a single drop,", "I thought I understood the world, yet I did not know myself.",
      "I read a thousand books, yet missed a single line:", "\"Know yourself.\" All my life I could not reach those words.",
      "O love, set me on fire, let flowers grow from my heart,", "let the dust on my soul fall away in one breath.",
      "I wanted to reach You, but I lost my way,", "and the day I let go of my ego, I touched the Truth.",
      "O heart, a thousand and one worlds are hidden in you,", "the day you know yourself, your secret door will open.",
      "I thought it was love, but it was only my ego's desire,", "I expected loyalty from others, yet I was unfaithful.",
      "I looked for blame in the world and called myself pure,", "without looking in the mirror, I called myself right.",
      "I beat my head against the stone, I cried to the walls,", "searching the sky for the Truth, I drifted from my own heart.",
      "For one who cannot conquer himself, a thousand victories are a mirage;", "the one who conquers his ego is the greatest victor.",
      "A candle burns and fades, but its light stays in memory,", "a person leaves, but his words remain in the traces of good.",
      "Why did you hoard wealth? One day it will slip from your hands.", "Let your kindness and good name remain on the roads you have walked.",
      "Forgive, O man, turn your anger into love,", "exchange the darkness in your heart for a grain of light.",
      "You are a guest in this world, do not claim eternity,", "before death comes, O man, do not lose yourself.", "Hey! Hey!"]
LY = {"uz": UZ, "ru": RU, "en": EN}
CTA = {"uz": ("O'z she'ringizdan qo'shiq va klip qilmoqchimisiz?", "She'ringizni yuboring: bot ma'nosini tushuntiradi va AI bilan qanday qilishni bosqichma-bosqich o'rgatadi"),
       "ru": ("Хотите песню и клип из своего стихотворения?", "Отправьте стих: бот объяснит смысл и пошагово научит, как сделать это с ИИ"),
       "en": ("Want a song and a clip from your own poem?", "Send your poem: the bot explains its meaning and teaches you step by step how to make it with AI")}
FINT = {"ru": "«O'zingni angla» — «Познай себя». Ты гость в этом мире.", "en": "\"O'zingni angla\" means \"Know yourself.\" You are a guest in this world."}
ASK = {"uz": ("Siz-chi?", "O'zingizni qachon", "angladingiz?", "Izohga yozing!"), "ru": ("А вы?", "Когда вы", "поняли себя?", "Напишите в комментариях!"),
       "en": ("And you?", "When did you first", "truly know yourself?", "Tell us in the comments!")}
T_CUT, AV_D, END_D, TOTAL = 198.5, 4.0, 4.5, 207.0
FB = "/usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf"; FS = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"
def a_(x): return f"0:{int(x // 60):02}:{x % 60:05.2f}"
def s_(x): ms = int(round(x * 1000)); return f"{ms // 3600000:02}:{ms // 60000 % 60:02}:{ms // 1000 % 60:02},{ms % 1000:03}"
def build(L):
    # avatar (16:9): xira fon + avatar chapda + savol plashkasi o'ngda
    p = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0)); d = ImageDraw.Draw(p)
    d.rounded_rectangle([900, 300, 1840, 780], 36, fill=(18, 10, 12, 205), outline=(255, 60, 80, 255), width=4)
    q = ASK[L]; y = 340
    for i, (t, sz, col) in enumerate(((q[0], 70, (255, 214, 120)), (q[1], 62, (255, 255, 255)), (q[2], 62, (255, 255, 255)), (q[3], 54, (255, 90, 110)))):
        f = ImageFont.truetype(FB, sz); d.text((1370 - d.textlength(t, font=f) / 2, y), t, font=f, fill=col); y += sz + (34 if i in (0, 2) else 16)
    p.save(f"{W0}/plate_{L}.png")
    run(["ffmpeg", "-v", "error", "-y", "-i", f"{R}/video/avatar.mp4", "-loop", "1", "-i", f"{W0}/plate_{L}.png", "-filter_complex",
         f"[0:v]trim=0:{AV_D},setpts=PTS-STARTPTS,fps=24,split[a][b];[a]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,boxblur=40:2,eq=brightness=-0.18[bg];"
         f"[b]scale=-2:1000[fg];[bg][fg]overlay=x=200:y=40[v0];[v0][1:v]overlay=0:0:shortest=1,fade=t=in:d=0.4,format=yuv420p[v]",
         "-map", "[v]", "-t", str(AV_D), "-r", "24", "-c:v", "libx264", "-crf", "16", f"{W0}/av_{L}.mp4"])
    run(["ffmpeg", "-v", "error", "-y", "-i", f"{R}/video/end/end_{L}.mp4", "-filter_complex",
         f"[0:v]fps=24,tpad=stop_mode=clone:stop_duration=1,trim=0:{END_D},setpts=PTS-STARTPTS,split[a][b];[a]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,boxblur=40:2,eq=brightness=-0.25[bg];"
         f"[b]scale=-2:1080[fg];[bg][fg]overlay=x=(W-w)/2:y=0,fade=t=in:d=0.3,format=yuv420p[v]", "-map", "[v]", "-t", str(END_D), "-r", "24", "-c:v", "libx264", "-crf", "16", f"{W0}/end_{L}.mp4"])
    # so'zlar + bot chaqiruvi
    hdr = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: L,Liberation Serif,{56 if L == 'uz' else 52},&H00E6F4FF,&H00FFFFFF,&H00101828,&H78000000,-1,-1,0,0,100,100,0,0,1,3.5,2,2,90,90,64,1
Style: C,Liberation Serif,58,&H0078D6FF,&H00FFFFFF,&H00101020,&H96000000,-1,-1,0,0,100,100,0,0,1,4,2,8,120,120,70,1
Style: B,Inter,92,&H00FFFFFF,&H00FFFFFF,&H003C28FF,&H96000000,-1,0,0,0,100,100,0,0,1,6,3,2,80,80,150,1
Style: S,Liberation Serif,44,&H00FFFFFF,&H00FFFFFF,&H00101828,&H96000000,-1,-1,0,0,100,100,0,0,1,3,2,8,160,160,190,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    ev = ""; srt = []
    for t0, t1, li in LINES:
        ev += f"Dialogue: 0,{a_(t0 - 0.15)},{a_(t1 - 0.1)},L,,0,0,0,,{{\\fad(250,250)}}{LY[L][li]}\n"; srt.append((t0 - 0.15, t1 - 0.1, LY[L][li]))
    c1, c2 = CTA[L]
    ev += f"Dialogue: 1,{a_(184.8)},{a_(190.3)},C,,0,0,0,,{{\\fad(300,300)}}{c1}\n"
    ev += f"Dialogue: 1,{a_(185.3)},{a_(190.3)},S,,0,0,0,,{{\\fad(300,300)}}{c2}\n"
    ev += f"Dialogue: 1,{a_(185.6)},{a_(190.3)},B,,0,0,0,,{{\\fad(300,300)}}@sahiychishopbot\n"
    if L in FINT: ev += f"Dialogue: 0,{a_(192.8)},{a_(197.8)},L,,0,0,0,,{{\\fad(300,300)}}{FINT[L]}\n"
    open(f"{W0}/final_{L}.ass", "w").write(hdr + ev)
    open(f"{OUT}/ozligim-{L}.srt", "w").write("".join(f"{i + 1}\n{s_(a)} --> {s_(b)}\n{t}\n\n" for i, (a, b, t) in enumerate(srt)))
    name = {"uz": "1-telegram-ozligim-uz", "en": "2-youtube-linkedin-ozligim-en", "ru": "3-instagram-facebook-ozligim-ru"}[L]
    fc = (f"[0:v]trim=0:{T_CUT},setpts=PTS-STARTPTS[m];[1:v]setpts=PTS-STARTPTS[av];[2:v]setpts=PTS-STARTPTS[en];[m][av][en]concat=n=3:v=1:a=0,"
          f"subtitles={W0}/final_{L}.ass,fade=t=in:d=1.0,fade=t=out:st={TOTAL - 0.8}:d=0.8,format=yuv420p[v];[3:a]atrim=0:{TOTAL},afade=t=out:st={TOTAL - 2.5}:d=2.5[au]")
    run(["ffmpeg", "-v", "error", "-y", "-i", f"{W0}/fx.mp4", "-i", f"{W0}/av_{L}.mp4", "-i", f"{W0}/end_{L}.mp4", "-i", f"{Q}/qoshiq_final.mp3",
         "-filter_complex", fc, "-map", "[v]", "-map", "[au]", "-t", str(TOTAL), "-c:v", "libx264", "-crf", "17", "-preset", "fast", "-c:a", "aac", "-b:a", "192k", f"{W0}/full_{L}.mp4"])
    # 30 MB dan kichik: HEVC 1080p 2-pass
    vb = "1020k"; pl = f"{W0}/pass_{L}"
    run(["ffmpeg", "-v", "error", "-y", "-i", f"{W0}/full_{L}.mp4", "-c:v", "libx265", "-b:v", vb, "-x265-params", f"pass=1:stats={pl}.log:log-level=error", "-preset", "medium", "-an", "-f", "mp4", "/dev/null"])
    run(["ffmpeg", "-v", "error", "-y", "-i", f"{W0}/full_{L}.mp4", "-c:v", "libx265", "-b:v", vb, "-x265-params", f"pass=2:stats={pl}.log:log-level=error", "-preset", "medium",
         "-tag:v", "hvc1", "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", f"{OUT}/{name}.mp4"])
    print(L, os.path.getsize(f"{OUT}/{name}.mp4") // 1024 // 1024, "MB", flush=True)
with ThreadPoolExecutor(3) as ex: list(ex.map(build, ["uz", "ru", "en"]))
