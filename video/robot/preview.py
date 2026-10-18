# 1–10-sahna ko'rib chiqish versiyasi: kliplar ovoz vaqtiga moslanadi, ovoz + Dutar's Whisper + uz subtitr.
import subprocess, os, sys
B = sys.argv[1]  # ish papkasi
os.makedirs(B, exist_ok=True)
CUT = [0, 8.0, 13.3, 19.5, 27.8, 37.3, 44.5, 48.1, 56.2, 59.5, 71.3]
CLIP = ["s01", "s02", "s03", "s04", "s05", "s06", "s07", "s08", "s09", "s10"]
START = [0, 0, 0, 0, 0, 0, 0, 0, 1.4, 0]   # klipning qayeridan boshlanadi
R = 0  # robot / odam subtitr rangi
SUB = [  # (boshi, oxiri, kim, matn)  R=robot, O=odam
 (0.1, 4.5, "R", "Do'koningdan har kuni pul oqib ketyapti."), (5.0, 7.8, "R", "Sen esa buni ko'rmaysan."),
 (8.3, 12.8, "O", "Qanaqa pul? Men seni faqat rasm va video uchun ishlataman."),
 (13.5, 18.9, "R", "Rasm yaxshi. Lekin meni rasm uchun o'ylab topishmagan."),
 (19.8, 27.4, "R", "1956-yili olimlar so'rashdi: mashina odamning aqliy ishini qila oladimi?"),
 (28.1, 32.9, "R", "Sen kun bo'yi kassaga, telefonga, mijozga qaraysan."), (33.5, 36.5, "R", "Oshpaz stoliga esa hech kim qaramaydi."),
 (37.5, 39.9, "R", "Bitta lavash sousiz ketdi."), (40.5, 41.9, "R", "Mijoz indamadi."), (42.1, 44.2, "R", "Lekin qaytib kelmadi."),
 (44.8, 47.7, "O", "Nazoratchi yollaymanmi? Unga oylik kerak."),
 (48.4, 51.9, "R", "Bitta kichik kamera. U faqat stolni ko'radi."), (52.4, 55.7, "R", "Go'sht, sabzavot, sous."),
 (56.5, 57.5, "R", "To'xtang."), (57.6, 59.0, "R", "Sous hali qo'shilmadi."),
 (59.8, 61.2, "O", "Faqat lavash uchunmi?"), (61.4, 62.7, "R", "Yo'q."),
 (62.9, 67.5, "R", "Eng qimmat ish qo'l bilan emas, bosh bilan qilinadi."), (68.2, 71.0, "R", "Shifokor, yurist."),
]
def run(c): subprocess.run(c, check=True)
parts = []
for i, c in enumerate(CLIP):
    d = CUT[i+1] - CUT[i]; f = f"video/robot/clips/{c}.mp4"; o = f"{B}/p{i+1:02}.mp4"
    k = max(1.0, d / (8 - START[i]))
    vf = f"trim=start={START[i]},setpts=PTS-STARTPTS"
    if k > 1.0: vf += f",setpts={k:.4f}*PTS,minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:vsbmc=1"
    vf += f",fps=30,scale=1080:1920:flags=lanczos,trim=duration={d:.3f},setsar=1,format=yuv420p"
    run(["ffmpeg","-v","error","-y","-i",f,"-vf",vf,"-an","-c:v","libx264","-preset","fast","-crf","18",o]); parts.append(o)
open(f"{B}/list.txt","w").write("".join(f"file '{os.path.abspath(p)}'\n" for p in parts))
run(["ffmpeg","-v","error","-y","-f","concat","-safe","0","-i",f"{B}/list.txt","-c","copy",f"{B}/raw.mp4"])
cuts = " ".join(str(x) for x in CUT[1:-1])
run(["bash","video/cine.sh",f"{B}/raw.mp4",f"{B}/cine.mp4",cuts])
T = CUT[-1]
run(["ffmpeg","-v","error","-y","-i","video/robot/dialog.flac","-af",f"atrim=0:{T},afade=t=out:st={T-0.4}:d=0.4,aresample=48000","-ac","2",f"{B}/voice.wav"])
run(["bash","video/sfx.sh",f"{B}/voice.wav",f"{B}/voice_sfx.wav",cuts])
M = "/root/.claude/uploads/2a2cb10c-3170-5137-84c1-a19971a38055/f9a598fd-Dutar_s_Whisper.mp3"
run(["ffmpeg","-v","error","-y","-i",f"{B}/voice_sfx.wav","-ss","197","-i",M,"-filter_complex",
  f"[1:a]atrim=0:{T},asetpts=PTS-STARTPTS,afade=t=in:d=1.5,afade=t=out:st={T-2}:d=2,volume=0.55,aresample=48000[m];"
  "[0:a]asplit[v][sc];[m][sc]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[md];"
  "[v][md]amix=inputs=2:normalize=0,loudnorm=I=-15:TP=-1.5:LRA=11[a]","-map","[a]","-ar","48000",f"{B}/mix.wav"])
def tt(x): return f"0:{int(x//60):02}:{x%60:05.2f}"
hdr = open("/tmp/claude-0/-home-user-cheksiz/2a2cb10c-3170-5137-84c1-a19971a38055/scratchpad/aytilmagan/sub_uz.ass").read().split("[Events]")[0]
ev = "".join(f"Dialogue: 0,{tt(a)},{tt(b)},{'C' if w=='R' else 'S'},,0,0,0,,{{\\fad(150,150)}}{t}\n" for a, b, w, t in SUB)
open(f"{B}/sub_uz.ass","w").write(hdr + "[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n" + ev)
run(["ffmpeg","-v","error","-y","-i",f"{B}/cine.mp4","-i",f"{B}/mix.wav","-vf",f"subtitles={B}/sub_uz.ass",
     "-c:v","libx264","-preset","medium","-crf","21","-c:a","aac","-b:a","160k","-shortest","-movflags","+faststart",f"{B}/robot_1-10_korib_chiqish.mp4"])
