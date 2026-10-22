# «Birlik» klipi qoralamasi: music/birlik.mp3 (2:35, 143.5 BPM) zarblariga moslangan.
# Egasi (2026-10-22): bir kadr ikki marta qo'yilmaydi; Bahodir: qora chopon (1:02), nokaut (1:07), yakunda g'alaba portreti;
# yakunda 2 sahna: tarix qahramonlari (5 ramka) va bugungi qahramonlar (3 ramka); Veo o'rinlari hozircha yozuvli kadr.
import subprocess, os, sys, json
import numpy as np
R = "video/ref/2026-10-21/"; W = sys.argv[1]; os.makedirs(W, exist_ok=True)
MUSIC = "video/qahramon/music/birlik.mp3"; END = 155.4
VEO = {}   # tayyor Veo kliplari: kalit -> fayl
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
A, B = "A", "B"
PLAN = [  # (boshlanish s, tur, ma'lumot, yozuv)
 (0.0,   "veo", "tong", "VEO: tog'lar ortidan quyosh chiqadi + sarlavha"),
 (10.0,  "clip", ("jaloliddin.mp4", 20, A), "«Tog'lar yo'l berar bizga» — Jaloliddin hujumga"),
 (15.0,  "clip", ("jaloliddin.mp4", 42, A), "«to'siqni yorib, zafar quchib» — ot sakraydi"),
 (20.2,  "clip", ("temur_taxt.mp4", 57, B), "«Asrlar guvoh bizga» — Ko'ragoniy tamgasi"),
 (25.2,  "clip", ("temur_taxt.mp4", 82.7, A, 1.3), "«qonimizda olov bor» — Amir Temur"),
 (30.2,  "veo", "ulugbek", "VEO: Ulug'bek rasadxonasi"),
 (34.4,  "veo", "ibnsino", "VEO: Ibn Sino kitob ustida"),
 (36.9,  "veo", "beruniy", "VEO: Beruniy astrolab bilan"),
 (39.2,  "clip", ("shoxruxxon_baxtiyorov.mp4", 18, A), "Naqorat «Birlik – qudratimiz» — Shoxruxxon"),
 (44.2,  "clip", ("karate_leshan_67kg.mp4", 10, A), "«Yengilmasdir har qadamimiz» — karate"),
 (49.2,  "clip", ("shoxruxxon_baxtiyorov.mp4", 33, A), "«Kuchayur har dam yurtimiz» — medal"),
 (54.2,  "veo", "qollar", "VEO: birlik — qo'llar ustma-ust"),
 (58.0,  "clip", ("armiya.mp4", 72, A), "«Bir tan-u bir jon» — askarlar"),
 (62.3,  "clip", ("jalolov_dacres.mp4", 0.0, B, 2.6), "«Mag'rur boshimiz egilmas» — Bahodir qora choponda sahnadan chiqadi (sekin)"),
 (67.3,  "clip", ("jalolov_dacres.mp4", 13.8, B, 2.0), "«hech qachon yengilmas!» — zarba, yiqiladi, yotadi (2x sekin)"),
 (77.3,  "clip", ("armiya.mp4", 80, A), "tog'da askarlar"),
 (82.3,  "clip", ("jaloliddin.mp4", 2, A), "Jaloliddin Manguberdi"),
 (87.3,  "veo", "registon", "VEO: Registon, mushaklar"),
 (93.1,  "clip", ("shoxruxxon_baxtiyorov.mp4", 0, A), "Shoxruxxon: tashlash"),
 (98.1,  "clip", ("karate_leshan_67kg.mp4", 22.4, A, 2.6), "karate g'olibi qo'lini ko'taradi (sekin)"),
 (103.9, "multi", [("sohibqiron_treyler.mp4", 4.0, 1.8), ("sohibqiron_treyler.mp4", 7.4, 1.5), ("sohibqiron_treyler.mp4", 25.0, 1.8)], "Jang 1: bayroqli qo'shin, gulxanlar"),
 (109.7, "multi", [("sohibqiron_treyler.mp4", 27.6, 1.4), ("sohibqiron_treyler.mp4", 33.0, 2.0), ("sohibqiron_treyler.mp4", 35.0, 1.9), ("sohibqiron_treyler.mp4", 42.0, 1.0)], "Jang 2: fillar, otliqlar, olov"),
 (114.7, "clip", ("armiya.mp4", 54, A), "zirhli kolonna"),
 (120.5, "veo", "yoshlar", "VEO: yoshlar cho'qqida bayroq ko'taradi"),
 (125.5, "clip", ("armiya.mp4", 88, A), "samolyotlar"),
 (128.4, "hist", [("temur_taxt.mp4", 79.8, "AMIR TEMUR", 1.4), ("jaloliddin.mp4", 62.0, "JALOLIDDIN MANGUBERDI", 1.0),
                  ("veo", 0, "IBN SINO"), ("veo", 0, "ABU RAYHON BERUNIY"), ("veo", 0, "MIRZO ULUG'BEK")], "Tarix qahramonlari: 3 s turadi, qumga aylanadi"),
 (143.4, "alive", ("jalolov_dacres.mp4", 4.3, "BAHODIR JALOLOV", 1.8), "Bahodir: qora choponda, qo'li tepada (tirik — qum emas, qorong'ilashadi)"),
 (147.4, "final", None, "VEO: bayroq + yakuniy yozuv"),
]
def esc(t): return t.replace("\\", "\\\\").replace(":", "\\:").replace("'", "’")
def run(c): subprocess.run(c, check=True)
beats = np.load("video/qahramon/music/beats.npy")
st = [0.0] + [float(beats[np.abs(beats - p[0]).argmin()]) for p in PLAN[1:]]
used = {}
def note(src, a, b): used.setdefault(src, []).append((a, b))
def tag(s0, lab):
    if os.environ.get("TAG") != "1": return "null"
    return f"drawtext=fontfile={FONT}:text='{esc(f'{int(s0//60)}:{s0%60:04.1f}  {lab}')}':fontcolor=white:fontsize=20:x=16:y=40:box=1:boxcolor=black@0.6:boxborderw=8"
def card(o, d, txt, s0, lab):
    run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"color=c=0x1a120c:s=720x1280:d={d:.3f}:r=30", "-vf",
         f"drawtext=fontfile={FONT}:text='{esc(txt)}':fontcolor=0xFFC34D:fontsize=30:x=(w-text_w)/2:y=(h-text_h)/2," + tag(s0, lab),
         "-c:v", "libx264", "-crf", "24", "-pix_fmt", "yuv420p", o])
def piece(src, cs, d, m, o, k=1.0, extra=""):
    srcd = d / k; note(src, cs, cs + srcd)
    dl = "delogo=x=440:y=505:w=410:h=80," if "temur_taxt" in src else ""
    base = dl + ("scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280" if m == A else
            "split[a][b];[a]scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,boxblur=20:2,eq=brightness=-0.15[bg];[b]scale=720:-2[fg];[bg][fg]overlay=0:(H-h)/2")
    slow = f",setpts={k}*PTS,minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:vsbmc=1" if k > 1 else ""
    run(["ffmpeg", "-v", "error", "-y", "-ss", str(cs), "-t", f"{srcd + 0.1:.3f}", "-i", R + src, "-filter_complex",
         base + slow + f",fps=30,trim=duration={d:.3f},setpts=PTS-STARTPTS" + extra, "-an", "-c:v", "libx264", "-crf", "24", "-pix_fmt", "yuv420p", o])
def frames(o, d, cells, s0, lab, step):
    # oltin ramkali kataklar; har biri step s keyin paydo bo'ladi; ichida jonli kadr (yoki Veo o'rni)
    inp = ["-f", "lavfi", "-i", f"color=c=0x140c07:s=720x1280:d={d:.3f}:r=30"]; fc = ""; last = "0:v"
    for i, (cell, (x, y, w, h)) in enumerate(cells):
        src, cs, name = cell[:3]; k = cell[3] if len(cell) > 3 else 1.0
        if src == "veo":
            inp += ["-f", "lavfi", "-i", f"color=c=0x2a1c12:s={w}x{h}:d={d:.3f}:r=30"]
            fc += f"[{i+1}:v]drawtext=fontfile={FONT}:text='VEO':fontcolor=0xFFC34D:fontsize=26:x=(w-text_w)/2:y=(h-text_h)/2,setpts=PTS-STARTPTS[c{i}];"
        else:
            note(src, cs, cs + d / k); inp += ["-ss", str(cs), "-t", f"{d / k + 0.1:.3f}", "-i", R + src]
            sl = f",setpts={k}*PTS,minterpolate=fps=30:mi_mode=mci" if k > 1 else ",setpts=PTS-STARTPTS"
            fc += f"[{i+1}:v]scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h}{sl},fps=30[c{i}];"
        t0 = i * step
        fc += (f"[c{i}]drawbox=x=0:y=0:w=iw:h=ih:color=0xFFC34D:t=6,drawbox=x=8:y=8:w=iw-16:h=ih-16:color=0x8a5a1a:t=2,"
               f"drawtext=fontfile={FONT}:text='{esc(name)}':fontcolor=0xFFC34D:fontsize=24:x=(w-text_w)/2:y=h-44:box=1:boxcolor=black@0.55:boxborderw=6,"
               f"fade=t=in:st={t0}:d=0.3:alpha=1,format=yuva420p,setpts=PTS+0/TB[f{i}];[{last}][f{i}]overlay={x}:{y}:enable='gte(t,{t0})'[o{i}];")
        last = f"o{i}"
    fc += f"[{last}]" + tag(s0, lab) + ",format=yuv420p[v]"
    run(["ffmpeg", "-v", "error", "-y", *inp, "-filter_complex", fc, "-map", "[v]", "-t", f"{d:.3f}", "-c:v", "libx264", "-crf", "24", o])
lst = []
for i, p in enumerate(PLAN):
    s0 = st[i]; d = (st[i + 1] if i + 1 < len(PLAN) else END) - s0; o = f"{W}/{i:02}.mp4"; kind, data, lab = p[1], p[2], p[3]
    if kind == "veo":
        card(o, d, lab, s0, lab) if data not in VEO else None
    elif kind == "clip":
        src, cs, m = data[:3]; k = data[3] if len(data) > 3 else 1.0
        piece(src, cs, d, m, o, k, "," + tag(s0, lab))
    elif kind == "multi":
        tot = sum(x[2] for x in data); parts = []
        for j, (src, cs, dd) in enumerate(data):
            pj = f"{W}/{i:02}_{j}.mp4"; piece(src, cs, d * dd / tot, B if "jalolov" in src else A, pj, d / tot, "," + tag(s0, lab)); parts.append(pj)
        open(f"{W}/m{i}.txt", "w").write("".join(f"file '{os.path.abspath(x)}'\n" for x in parts))
        run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{W}/m{i}.txt", "-c", "copy", o])
    elif kind == "gallery":
        cells = [(data[1], (30, 70, 320, 400)), (data[0], (190, 450, 340, 460)), (data[2], (370, 70, 320, 400)),
                 (data[3], (30, 900, 320, 340)), (data[4], (370, 900, 320, 340))]
        frames(o, d, cells, s0, lab, 0.6)
    elif kind == "heroes":
        cells = [(cell, (60, 70 + j * 390, 600, 360)) for j, cell in enumerate(data)]
        frames(o, d, cells, s0, lab, 0.8)
    elif kind == "hist":
        hs = []
        for j, cell in enumerate(data):
            hj = f"{W}/{i:02}_h{j}.mp4"; src, cs, name = cell[:3]; k = cell[3] if len(cell) > 3 else 1.0
            nm = f",drawtext=fontfile={FONT}:text='{esc(name)}':fontcolor=0xFFC34D:fontsize=40:x=(w-text_w)/2:y=h-200:box=1:boxcolor=black@0.45:boxborderw=12"
            if src == "veo":
                run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "color=c=0x2a1c12:s=720x1280:d=3.9:r=30", "-vf",
                     f"drawtext=fontfile={FONT}:text='VEO portret':fontcolor=0xFFC34D:fontsize=34:x=(w-text_w)/2:y=(h-text_h)/2" + nm,
                     "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p", hj])
            else:
                piece(src, cs, 3.9, A, hj, k, nm)
            hs.append(hj)
        run(["python3", "video/qahramon/qum_ketma.py", f"{W}/{i:02}_hist.mp4", *hs])
        run(["ffmpeg", "-v", "error", "-y", "-i", f"{W}/{i:02}_hist.mp4", "-vf", f"trim=duration={d:.3f},setpts=PTS-STARTPTS,tpad=stop_mode=clone:stop_duration=1," + tag(s0, lab) + f",trim=duration={d:.3f}",
             "-c:v", "libx264", "-crf", "24", "-pix_fmt", "yuv420p", o])
    elif kind == "alive":
        src, cs, name, k = data
        nm = f",drawtext=fontfile={FONT}:text='{esc(name)}':fontcolor=0xFFC34D:fontsize=40:x=(w-text_w)/2:y=h-200:box=1:boxcolor=black@0.45:boxborderw=12"
        piece(src, cs, d, B, o, k, nm + f",fade=t=out:st={d - 0.7:.2f}:d=0.7," + tag(s0, lab))
    elif kind == "final":
        card(o, d, "O'zbekning jasur o'g'li —\\nhech qachon yengilmas!", s0, lab)
    lst.append(o)
bad = []
for src, r in used.items():
    r.sort()
    for (a1, b1), (a2, b2) in zip(r, r[1:]):
        if a2 < b1 - 0.05: bad.append((src, (round(a1, 1), round(b1, 1)), (round(a2, 1), round(b2, 1))))
print("TAKROR:", bad if bad else "yo'q")
open(f"{W}/list.txt", "w").write("".join(f"file '{os.path.abspath(x)}'\n" for x in lst))
run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{W}/list.txt", "-i", MUSIC, "-map", "0:v", "-map", "1:a", "-af", "bass=g=3:f=90:w=0.7,extrastereo=m=1.25,alimiter=limit=0.95",
     "-c:v", "libx264", "-crf", "25", "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", f"{W}/klip_qoralama.mp4"])
json.dump([(round(a, 2), p[1], p[3]) for a, p in zip(st, PLAN)], open(f"{W}/kesimlar.json", "w"), ensure_ascii=False, indent=0)
print("ok")
