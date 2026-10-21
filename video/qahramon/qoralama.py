# Qoralama: tanlangan lavhalar reja tartibida + Veo o'rinlari (yozuvli kadr). 720x1280, tepada manba va vaqt yozuvi.
import subprocess, os, sys
R = "video/ref/2026-10-21/"; W = sys.argv[1]; os.makedirs(W, exist_ok=True)
A, B = "A", "B"   # A: o'rtasidan kesish, B: to'liq kadr + xira fon
PLAN = [
 ("veo", "VEO: tong, tog'lar ortidan quyosh chiqadi", 4, "Kirish 0:00–0:10"),
 ("veo", "VEO: Registon, ustida oltin sarlavha", 4, "Kirish"),
 ("armiya.mp4", 0, 6, A, "1-band 0:10 «Tog'lar yo'l berar bizga» — Armiya: parad"),
 ("armiya.mp4", 6, 5, A, "1-band — Armiya: zirhli mashinalar"),
 ("veo", "VEO: Amir Temurning otliq haykali", 4, "2-band 0:20 «Asrlar guvoh bizga»"),
 ("ibn_sino.mp4", 0, 6, B, "2-band — Ibn Sino portreti"),
 ("beruniy.mp4", 24, 6, B, "2-band — Beruniy va globus"),
 ("veo", "VEO: Ulug'bek rasadxonasi, yulduzli osmon", 4, "2-band «qonimizda olov bor»"),
 ("beruniy.mp4", 120, 5, B, "Ko'tarilish 0:30 — osmon sferasi"),
 ("shoxruxxon_baxtiyorov.mp4", 18, 6, A, "Naqorat 0:39 «Birlik – qudratimiz» — Shoxruxxon: tashlash"),
 ("davlat_bobonov.mp4", 0, 6, A, "Naqorat — Davlat Bobonov"),
 ("karate_leshan_67kg.mp4", 10, 6, A, "Naqorat «Yengilmasdir har qadamimiz» — Karate: tepish"),
 ("shoxruxxon_baxtiyorov.mp4", 33, 6, A, "Naqorat «Kuchayur har dam yurtimiz» — Shoxruxxon: medal"),
 ("armiya.mp4", 72, 5, A, "3-band 0:58 «Bir tan-u bir jon» — askarlar yuguradi"),
 ("armiya.mp4", 80, 5, A, "3-band «boshimiz egilmas» — tog'da askarlar"),
 ("jalolov_dacres.mp4", 13, 5, B, "1:07 «hech qachon yengilmas!» — Jalolov: NOKDAUN"),
 ("jalolov_dacres.mp4", 23, 5, B, "Nokdaun yaqindan (sekinlashuv montajda)"),
 ("jalolov_dacres.mp4", 50, 6, B, "Jalolov: g'alaba"),
 ("armiya.mp4", 88, 6, A, "Outro — samolyotlar"),
 ("karate_leshan_67kg.mp4", 18, 6, A, "Outro — karate g'olibi"),
 ("davlat_bobonov.mp4", 496, 6, A, "Outro — Bobonov medal bilan"),
 ("shoxruxxon_baxtiyorov.mp4", 37, 5, A, "Outro — chempion kamari"),
 ("armiya.mp4", 103, 6, A, "Outro — portlashlar qatori"),
 ("veo", "VEO: hilpirab turgan O'zbekiston bayrog'i", 4, "Outro"),
 ("veo", "Yakun: «O'zbekning jasur o'g'li — hech qachon yengilmas!» (kodda)", 4, "Oxirgi zarba"),
 ("veo", "ZAXIRA lavhalar (rejada yo'q, kerak bo'lsa)", 3, "Zaxira"),
 ("armiya.mp4", 2, 5, A, "Zaxira — Armiya: samolyot, vertolyot"),
 ("armiya.mp4", 10, 6, A, "Zaxira — raketa uchadi"),
 ("armiya.mp4", 18, 6, A, "Zaxira — tungi otish"),
 ("armiya.mp4", 54, 6, A, "Zaxira — zirhli kolonna"),
 ("ibn_sino.mp4", 32, 6, B, "Zaxira — Ibn Sino: Kitob ash-Shifo"),
 ("beruniy.mp4", 12, 6, B, "Zaxira — Beruniy chizmasi"),
 ("beruniy.mp4", 504, 6, B, "Zaxira — tog' balandligi chizmasi"),
 ("jalolov_dacres.mp4", 3, 5, B, "Zaxira — Jalolov ringga chiqadi"),
 ("shoxruxxon_baxtiyorov.mp4", 0, 6, A, "Zaxira — Shoxruxxon: 1-tashlash"),
 ("karate_leshan_67kg.mp4", 0, 5, A, "Zaxira — karate: chiqish"),
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
