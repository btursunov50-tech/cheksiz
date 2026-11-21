#!/usr/bin/env python3
"""«Bepul yordamchi» rolikni yig'adi (hammasi chiz.py da chizilgan): python3 video/tugma/build.py <work> [uz|ru|en] → <work>/<lang>/tugma_<lang>.mp4 (+ .srt)
Sahnalar: Veo kliplari (clips/*_toza.mp4, s02.mp4) + kodda chizilgan Excel/Word ekranlari (chiz/chiz.py). Ovoz o'zbekcha (voice/01–10), yozuvlar tilga qarab.
Musiqa: Doira and the Robot (Suno, egasi) 8 s dan; MUS / MUS_SS bilan almashtiriladi."""
import os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont
R = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
Q = f"{R}/video/yordamchi"; C = f"{Q}/clips"; V = f"{Q}/voice"
W0 = sys.argv[1]; LANG = sys.argv[2] if len(sys.argv) > 2 else "uz"
W = f"{W0}/{LANG}"; os.makedirs(W, exist_ok=True); CW = f"{W0}/seg"; os.makedirs(CW, exist_ok=True)
def run(c): subprocess.run(c, check=True)
dur = lambda f: float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f], capture_output=True, text=True).stdout)
B = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"; BL = "/usr/share/fonts/opentype/inter/Inter-Black.otf"
F = lambda s, f=B: ImageFont.truetype(f, s)
T_ALL = {"uz": dict(hook='BEPUL YORDAMCHI', say=["To'xtang! Telefoningizda hali ishlatmagan bepul yordamchingiz bor.", "Biz Infinite AI & Me: inson va sun'iy intellekt birga ishlaydigan kichik jamoa.", "Botimiz @sahiychishopbot. Unga oddiy so'z bilan yozing yoki ovozli xabar yuboring.", "Shubhali xabar, «pulingizni ikki barobar qilamiz» degan taklif yoki soxta ish e'loni keldimi? Suratini yuboring: aldov bormi, aytib beradi.", "Telegramingizni o'g'rilardan saqlash uchun bulutli parolni qadamma-qadam yoqishni o'rgatadi.", "«70 foiz chegirma», «oyiga atigi», «bepul yetkazish»? Suratini yuboring: haqiqatda qancha to'lashingizni hisoblaydi.", "To'y xarajatlarini ham bitta ro'yxatga yig'ib, jamini ko'rsatadi.", "Telefoningiz qotyaptimi? Yangisini olishdan oldin batareya holatini tekshirishni o'rgatadi.", "Bildirishnomalar tinchlik bermayaptimi? Qaysilarini o'chirishni ko'rsatadi.", "Konserva yoki sut yorlig'ini yuboring: sanalarni o'qib, nimani tekshirishni aytadi.", "Excel yoki Word'da qotib qoldingizmi? Ekran rasmini yuboring: qaysi tugmani bosishni ko'rsatadi.", 'Jahlingizni chiqargan xabarga xotirjam javob yozishga yordam beradi.', 'Har tong soat beshda kanalimizda bepul maslahat chiqadi.', 'Biznesingiz bormi? Sayt, QR menyu, bot va reklama videosini ham biz qilamiz.', "Yozing: @sahiychishopbot. Oddiy, tushunarli, o'zbek tilida.", "Siz-chi? Botdan birinchi nima so'rardingiz? Izohga yozing!"], avq="Siz-chi?|Botdan birinchi nima so'rardingiz?|Izohga yozing!"),
 "ru": dict(hook='БЕСПЛАТНЫЙ ПОМОЩНИК', say=['Стоп! В вашем телефоне есть бесплатный помощник, которым вы ещё не пользовались.', 'Мы Infinite AI & Me: маленькая команда, где человек и искусственный интеллект работают вместе.', 'Наш бот @sahiychishopbot. Пишите ему простыми словами или отправьте голосовое сообщение.', 'Пришло подозрительное сообщение, предложение «удвоим ваши деньги» или фальшивая вакансия? Пришлите фото: бот скажет, есть ли обман.', 'Он шаг за шагом научит включить облачный пароль, чтобы защитить ваш Telegram от воров.', '«Скидка 70%», «всего в месяц», «бесплатная доставка»? Пришлите фото: бот посчитает, сколько вы заплатите на самом деле.', 'Он соберёт расходы на свадьбу в один список и покажет итог.', 'Телефон тормозит? Прежде чем покупать новый, бот научит проверить состояние батареи.', 'Уведомления не дают покоя? Бот покажет, какие отключить.', 'Пришлите этикетку консервы или молока: бот прочитает даты и скажет, что проверить.', 'Застряли в Excel или Word? Пришлите скриншот: бот покажет, какую клавишу нажать.', 'Он поможет спокойно ответить на сообщение, которое вас разозлило.', 'Каждое утро в пять часов на нашем канале выходит бесплатный совет.', 'У вас есть бизнес? Сайт, QR-меню, бота и рекламное видео тоже делаем мы.', 'Пишите: @sahiychishopbot. Просто и понятно.', 'А вы? О чём вы спросили бы бота первым делом? Напишите в комментариях!'], avq='А вы?|О чём вы спросили бы бота первым делом?|Напишите в комментариях!'),
 "en": dict(hook='A FREE HELPER', say=["Stop! Your phone has a free helper you've never used.", 'We are Infinite AI & Me: a small team where a human and artificial intelligence work together.', 'Our bot is @sahiychishopbot. Write to it in plain words or send a voice message.', "Got a suspicious message, a «we'll double your money» offer or a fake job post? Send a picture: it tells you if it's a scam.", "It teaches you step by step to turn on a cloud password, so thieves can't take your Telegram.", '«70% off», «only a month», «free delivery»? Send a picture: it works out what you really pay.', 'It also adds up wedding costs in one list and shows the total.', 'Is your phone slow? Before you buy a new one, it teaches you to check the battery health.', "Notifications won't leave you alone? It shows which ones to turn off.", 'Send the label of a can or a milk carton: it reads the dates and tells you what to check.', 'Stuck in Excel or Word? Send a screenshot: it shows which key to press.', 'It helps you write a calm reply to a message that made you angry.', 'Every morning at five, our channel posts a free tip.', 'Have a business? We also make websites, QR menus, bots and ad videos.', 'Write to @sahiychishopbot. Simple and clear.', 'And you? What would you ask the bot first? Tell us in the comments!'], avq='And you?|What would you ask the bot first?|Tell us in the comments!')}
T = T_ALL[LANG]
N = 16
VL = [dur(f"{V}/{i:02}_usta.wav") for i in range(1, N + 1)]
CH = f"{W0}/chiz_{LANG}"
if not all(os.path.exists(f"{CH}/y{i:02}.mp4") for i in range(1, N)):
    subprocess.run(["python3", f"{Q}/chiz.py", CH], check=True, env=dict(os.environ, TLANG=LANG))
P = 0.3
SEG = [("c", f"y{i:02}", 0, None) for i in range(1, N)]
segs, lens = [], []
for k, (kind, name, ss, d) in enumerate(SEG):
    src = f"{C}/{name}.mp4" if kind == "v" else f"{CH}/{name}.mp4"; L = dur(src) - ss; d = d or L
    o = f"{CW}/{k:02}_{name}_{d}" + (f"_{LANG}" if kind == "c" else "") + ".mp4"  # chizilgan sahnalar tilga qarab
    if not os.path.exists(o):
        f = max(1.0, d / L)
        vf = (f"setpts={f:.4f}*(PTS-STARTPTS)," + ("minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:me_mode=bidir," if f > 1.02 else "fps=30,") +
              f"trim=0:{d},setpts=PTS-STARTPTS,scale=1080:1920:flags=lanczos,setsar=1,format=yuv420p")
        run(["ffmpeg", "-v", "error", "-y", "-ss", str(ss), "-i", src, "-vf", vf, "-an", "-r", "30", "-c:v", "libx264", "-crf", "18", "-preset", "fast", o])
    segs.append(o); lens.append(d)
starts, t = [], 0
for d in lens: starts.append(round(t, 2)); t += d
STORY = t
# ovoz qatorlari: (qator, boshlanishi)
VS = [(k, starts[k] + P) for k in range(N - 1)]
open(f"{W}/seq.txt", "w").write("".join(f"file '{x}'\n" for x in segs))
run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{W}/seq.txt", "-c", "copy", f"{W}/story.mp4"])
cine = f"{W0}/cine_story_{LANG}.mp4"
if not os.path.exists(cine): run(["bash", f"{R}/video/cine.sh", f"{W}/story.mp4", cine, " ".join(str(c) for c in starts[1:])])
def wrap(d, text, font, maxw):
    ls, cur = [], ""
    for w_ in text.split():
        t_ = (cur + " " + w_).strip()
        if d.textlength(t_, font=font) <= maxw: cur = t_
        else: ls.append(cur); cur = w_
    return ls + [cur]
def txtpng(path, text, size, col, font=B, box=(0, 0, 0, 160)):
    im = Image.new("RGBA", (1080, 400), (0, 0, 0, 0)); d = ImageDraw.Draw(im); f = F(size, font); ls = wrap(d, text, f, 940)
    h = len(ls) * (size + 14) + 30
    if box[3]: d.rounded_rectangle([40, 0, 1040, h], radius=26, fill=box)
    y = 16
    for l in ls: d.text(((1080 - d.textlength(l, font=f)) / 2, y), l, font=f, fill=col, stroke_width=2, stroke_fill="black"); y += size + 14
    im.save(path)
def chunks(text, n=8):  # uzun gapni bo'laklarga (vaqt so'z soniga qarab)
    ws = text.split(); out = []
    while ws:
        k = min(len(ws), n)
        for j in range(k, max(3, k - 4), -1):
            if ws[j - 1][-1] in ".,:?!": k = j; break
        out.append(" ".join(ws[:k])); ws = ws[k:]
    return out
ov, srt = [], []
txtpng(f"{W}/hook.png", T["hook"], 104, (255, 60, 70), font=BL, box=(0, 0, 0, 0)); pass  # hook: 1-sahnaning o'zida katta «TO'XTANG!» bor
n = 0
for k, a in VS:
    parts = chunks(T["say"][k]); tot = sum(len(p.split()) for p in parts); t0 = a
    for p in parts:
        d_ = VL[k] * len(p.split()) / tot; n += 1
        txtpng(f"{W}/sub{n}.png", p, 52, "white")
        if k != N - 2: ov.append((f"sub{n}.png", 1450, t0, t0 + d_ - 0.03))  # 15-qator: bot kartasida yozuv o'zi bor
        srt.append((t0, t0 + d_, p)); t0 += d_
args = ["ffmpeg", "-v", "error", "-y", "-i", cine]; fc = []; prev = "0:v"
for i, (png, y, a, b) in enumerate(ov, 1):
    args += ["-i", f"{W}/{png}"]; fc.append(f"[{prev}][{i}:v]overlay=0:{y}:enable='between(t,{a:.2f},{b:.2f})'[o{i}]"); prev = f"o{i}"
run(args + ["-filter_complex", ";".join(fc) + f";[{prev}]format=yuv420p[v]", "-map", "[v]", "-c:v", "libx264", "-crf", "20", "-r", "30", f"{W}/main_v.mp4"])
sys.path.insert(0, f"{R}/.claude/skills/video-yig"); from yig import avq_plate
avq_plate(T["avq"], f"{W}/avq.png"); AV = round(0.3 + VL[N - 1] + 0.8, 2)
run(["ffmpeg", "-v", "error", "-y", "-i", f"{R}/video/avatar.mp4", "-i", f"{W}/avq.png", "-filter_complex",
     f"[0:v]split[p][q];[q]reverse[r];[p][r]concat=n=2:v=1,trim=0:{AV},setpts=PTS-STARTPTS,scale=1080:1920:flags=lanczos,fps=30,setsar=1[a];[a][1:v]overlay=0:1200:enable='gte(t,0.3)',format=yuv420p[v]",
     "-map", "[v]", "-c:v", "libx264", "-crf", "20", "-r", "30", f"{W}/av.mp4"])
open(f"{W}/seq2.txt", "w").write("".join(f"file '{x}'\n" for x in [f"{W}/main_v.mp4", f"{W}/av.mp4", f"{R}/video/end/end_{LANG}.mp4"]))
run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{W}/seq2.txt", "-c", "copy", f"{W}/allv.mp4"])
END = 4.0; TOT = STORY + AV + END; VS.append((N - 1, STORY + 0.3))
M = os.environ.get("MUS", f"{R}/video/robot/music/doira_and_the_robot.mp3")  # egasi tanladi (A), 2026-11-10
run(["ffmpeg", "-v", "error", "-y", "-ss", os.environ.get("MUS_SS", "8"), "-t", str(TOT + 1), "-i", M, "-filter_complex",
     f"[0:a]afade=t=in:d=1.5,afade=t=out:st={TOT - 3}:d=3,volume=0.7,aresample=48000,aformat=channel_layouts=stereo,atrim=0:{TOT}[a]", "-map", "[a]", "-ar", "48000", f"{W}/mus.wav"])
run(["bash", f"{R}/video/sfx.sh", f"{W}/mus.wav", f"{W}/mix0.wav", " ".join(str(c) for c in starts[1:])])
ins = ["-i", f"{W}/mix0.wav"]; fcs = ""; labs = ""
for j, (k, a) in enumerate(VS):
    ins += ["-i", f"{V}/{k + 1:02}_usta.wav"]; fcs += f"[{j + 1}:a]aresample=48000,aformat=channel_layouts=stereo,adelay={int(a * 1000)}|{int(a * 1000)}[v{j}];"; labs += f"[v{j}]"
fcs += f"{labs}amix=inputs={len(VS)}:normalize=0,volume=1.6,apad=whole_dur={TOT}[vo];[vo]asplit[vk][vm];[0:a][vk]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[md];[md][vm]amix=inputs=2:normalize=0,loudnorm=I=-15:TP=-1.5:LRA=11[o]"
run(["ffmpeg", "-v", "error", "-y"] + ins + ["-filter_complex", fcs, "-map", "[o]", "-ar", "48000", f"{W}/mix.wav"])
run(["ffmpeg", "-v", "error", "-y", "-i", f"{W}/allv.mp4", "-i", f"{W}/mix.wav", "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", f"{W}/yordamchi_{LANG}{os.environ.get('TAG', '')}.mp4"])
def ts(x): return f"{int(x//3600):02}:{int(x%3600//60):02}:{int(x%60):02},{int(round(x%1*1000)):03}"
srt.append((STORY + 0.3, STORY + 0.3 + VL[N - 1], T["say"][N - 1]))
open(f"{W}/yordamchi-{LANG}.srt", "w").write("".join(f"{i+1}\n{ts(a)} --> {ts(b)}\n{t_}\n\n" for i, (a, b, t_) in enumerate(srt)))
print("starts", starts, "story", round(STORY, 1), "total", round(TOT, 1))
for k, a in VS: print(k + 1, round(a, 2), "->", round(a + VL[k], 2))
