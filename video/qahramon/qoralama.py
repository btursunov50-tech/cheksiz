# Egasi (2026-10-21): boshida Jaloliddin Manguberdi (yuzi, qo'shin, hujum, otning jardan sakrashi), oxirida quyosh botishi. Beruniy qalam chizmasi (xunuk) va ko'k belbog'li karatechi olib tashlandi.
# Qoralama: tanlangan lavhalar reja tartibida + Veo o'rinlari (yozuvli kadr). 720x1280, tepada manba va vaqt yozuvi.
import subprocess, os, sys
R = "video/ref/2026-10-21/"; W = sys.argv[1]; os.makedirs(W, exist_ok=True)
A, B = "A", "B"   # A: o'rtasidan kesish, B: to'liq kadr + xira fon
PLAN = [  # egasi (2026-10-21): MP3 2:35; takrorlanuvchi kadr yo'q; sifati past videolar (ibn_sino, beruniy 360p, davlat_bobonov 480p) olib tashlandi → allomalar Veo'da
 ("jaloliddin.mp4", 2, 5, A, "Kirish 0:00 — Jaloliddin Manguberdi (ustida sarlavha)"),
 ("jaloliddin.mp4", 30, 5, A, "Kirish 0:05 — ot ustida, ortida qo'shin"),
 ("jaloliddin.mp4", 20, 5, A, "1-band 0:10 «Tog'lar yo'l berar bizga» — qilich ko'tarib hujum"),
 ("jaloliddin.mp4", 42, 6, A, "1-band 0:15 «to'siqni yorib, zafar quchib» — ot jardan sakraydi"),
 ("veo", "VEO: Amir Temurning otliq haykali", 6, "2-band 0:20 «Asrlar guvoh bizga»"),
 ("veo", "VEO: Ulug'bek rasadxonasi, yulduzli osmon", 5, "2-band 0:26 «qonimizda olov bor»"),
 ("veo", "VEO: Ibn Sino, «Tib qonuni» kitobi", 4, "2-band 0:31 «Birlashib odimlasak»"),
 ("veo", "VEO: Beruniy, astrolab va osmon", 4, "Ko'tarilish 0:35"),
 ("shoxruxxon_baxtiyorov.mp4", 18, 6, A, "Naqorat 0:39 «Birlik – qudratimiz» — Shoxruxxon: tashlash"),
 ("karate_leshan_67kg.mp4", 10, 6, A, "Naqorat 0:45 «Yengilmasdir» — karate: tepish"),
 ("shoxruxxon_baxtiyorov.mp4", 33, 5, A, "Naqorat 0:51 «Kuchayur yurtimiz» — Shoxruxxon: medal"),
 ("armiya.mp4", 96, 2, A, "Naqorat oxiri — portlash"),
 ("armiya.mp4", 72, 5, A, "3-band 0:58 «Bir tan-u bir jon» — askarlar yuguradi"),
 ("armiya.mp4", 80, 4, A, "3-band 1:03 «boshimiz egilmas» — tog'da askarlar"),
 ("jalolov_dacres.mp4", 23, 5, B, "1:07 «hech qachon yengilmas!» — Jalolov: NOKDAUN (montajda 2x sekin, ~10 s)"),
 ("jalolov_dacres.mp4", 50, 6, B, "1:17 — Jalolov: g'alaba"),
 ("armiya.mp4", 11, 5, A, "Outro 1:23 — raketa uchadi"),
 ("armiya.mp4", 18, 6, A, "Outro — tungi otish"),
 ("shoxruxxon_baxtiyorov.mp4", 0, 6, A, "Outro — Shoxruxxon: tashlash"),
 ("karate_leshan_67kg.mp4", 18, 6, A, "Outro — karate g'olibi"),
 ("armiya.mp4", 0, 5, A, "Outro — parad"),
 ("armiya.mp4", 6, 5, A, "Outro — zirhli mashinalar"),
 ("jalolov_dacres.mp4", 3, 5, B, "Outro — Jalolov ringga chiqadi"),
 ("shoxruxxon_baxtiyorov.mp4", 38, 4, A, "Outro — chempion kamari"),
 ("armiya.mp4", 88, 6, A, "Outro — samolyotlar"),
 ("armiya.mp4", 103, 6, A, "Outro — portlashlar qatori"),
 ("jaloliddin.mp4", 50, 6, A, "Outro — Jaloliddin quyosh botishida daryo bo'yida"),
 ("veo", "VEO: hilpirab turgan O'zbekiston bayrog'i", 6, "Outro oxiri"),
 ("veo", "Yakun: «O'zbekning jasur o'g'li — hech qachon yengilmas!» (kodda)", 5, "Oxirgi zarba 2:30"),
]
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
def esc(t): return t.replace("\\", "\\\\").replace(":", "\\:").replace("'", "’")
lst = []
for i, p in enumerate(PLAN):
    o = f"{W}/{i:02}.mp4"
    if p[0] == "veo":
        _, txt, d, lab = p
        vf = (f"drawtext=fontfile={FONT}:text='{esc(txt)}':fontcolor=0xFFC34D:fontsize=34:x=(w-text_w)/2:y=(h-text_h)/2,"
              f"drawtext=fontfile={FONT}:text='{esc(lab)}':fontcolor=white:fontsize=26:x=20:y=40:box=1:boxcolor=black@0.6:boxborderw=8")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"color=c=0x1a120c:s=720x1280:d={d}:r=30", "-vf", vf,
                        "-c:v", "libx264", "-crf", "26", "-pix_fmt", "yuv420p", o], check=True)
    else:
        f, s, d, m, lab = p
        if m == A:
            base = "scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280"
        else:
            base = ("split[a][b];[a]scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,boxblur=20:2,eq=brightness=-0.15[bg];"
                    "[b]scale=720:-2[fg];[bg][fg]overlay=0:(H-h)/2")
        lab2 = f"{lab}  |  {f} {s}–{s+d} s"
        vf = (base + f",fps=30,drawtext=fontfile={FONT}:text='{esc(lab2)}':fontcolor=white:fontsize=22:x=16:y=40:box=1:boxcolor=black@0.6:boxborderw=8")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(s), "-t", str(d), "-i", R + f, "-filter_complex", vf, "-an",
                        "-c:v", "libx264", "-crf", "26", "-pix_fmt", "yuv420p", o], check=True)
    lst.append(o)
open(f"{W}/list.txt", "w").write("".join(f"file '{os.path.abspath(x)}'\n" for x in lst))
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{W}/list.txt", "-c", "copy", f"{W}/qoralama.mp4"], check=True)
print(sum(p[2] for p in PLAN))
