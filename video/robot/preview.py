# Ko'rib chiqish versiyasi: kliplar ovoz vaqtiga moslanadi (timeline.py), ovoz + musiqa + uz subtitr + STOP.
import subprocess, os, sys
B = sys.argv[1]  # ish papkasi; 2-argument: nechta sahna (standart 22)
os.makedirs(B, exist_ok=True)
sys.path.insert(0, "video/robot")
from timeline import SUB, MUSIC, CUT as CUTALL, CLIP as CLIPALL, START as ST
REUSE = os.environ.get("REUSE") == "1"  # tayyor cine.mp4 ni qayta ishlatish (faqat ovoz/subtitr o'zgarsa)
N = int(sys.argv[2]) if len(sys.argv) > 2 else 22   # nechta sahna
CUT = CUTALL[:N+1]; CLIP = CLIPALL[:N]; START = [ST.get(i+1, 0) for i in range(N)]
SUB = [x for x in SUB if x[0] < CUT[-1]]
def run(c): subprocess.run(c, check=True)
parts = []
for i, c in enumerate(CLIP if not REUSE else []):
    d = CUT[i+1] - CUT[i]; f = f"video/robot/clips/{c}.mp4"; o = f"{B}/p{i+1:02}.mp4"
    k = max(1.0, d / (8 - START[i]))
    vf = f"trim=start={START[i]},setpts=PTS-STARTPTS"
    if k > 1.0: vf += f",setpts={k:.4f}*PTS,minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:vsbmc=1"
    vf += f",fps=30,scale=1080:1920:flags=lanczos,trim=duration={d:.3f},setsar=1,format=yuv420p"
    run(["ffmpeg","-v","error","-y","-i",f,"-vf",vf,"-an","-c:v","libx264","-preset","fast","-crf","18",o]); parts.append(o)
if not REUSE: open(f"{B}/list.txt","w").write("".join(f"file '{os.path.abspath(p)}'\n" for p in parts))
if not REUSE: run(["ffmpeg","-v","error","-y","-f","concat","-safe","0","-i",f"{B}/list.txt","-c","copy",f"{B}/raw.mp4"])
cuts = " ".join(str(x) for x in CUT[1:-1])
if not REUSE: run(["bash","video/cine.sh",f"{B}/raw.mp4",f"{B}/cine.mp4",cuts])
T = CUT[-1]
run(["ffmpeg","-v","error","-y","-i","video/robot/dialog.flac","-af",f"atrim=0:{T},afade=t=out:st={T-0.4}:d=0.4,aresample=48000","-ac","2",f"{B}/voice.wav"])
run(["bash","video/sfx.sh",f"{B}/voice.wav",f"{B}/voice_sfx.wav",cuts])
# musiqa qatlami: har bir qism o'z joyiga, 2 s yumshoq o'tish bilan
ins=["-i",f"{B}/voice_sfx.wav"]; fc=""; lab=""
for j,(mf,ms,t0,t1) in enumerate(MUSIC):
    if t0 >= T: continue
    t1=min(t1,T); d=t1-t0; ins+=["-ss",str(ms),"-i",f"video/robot/music/{mf}"]
    fi=0 if t0==0 else 2; fo=2 if t1<T else 2
    fc+=f"[{j+1}:a]atrim=0:{d},asetpts=PTS-STARTPTS,afade=t=in:d={fi or 0.01},afade=t=out:st={d-fo}:d={fo},aresample=48000,aformat=channel_layouts=stereo,adelay={int(t0*1000)}|{int(t0*1000)}[m{j}];"
    lab+=f"[m{j}]"
n=lab.count("[")
run(["ffmpeg","-v","error","-y",*ins,"-filter_complex",
  fc+f"{lab}amix=inputs={n}:normalize=0,volume=0.5[m];"
  "[0:a]asplit[v][sc];[m][sc]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[md];"
  "[v][md]amix=inputs=2:normalize=0,loudnorm=I=-15:TP=-1.5:LRA=11[a]","-map","[a]","-ar","48000",f"{B}/mix.wav"])
def tt(x): return f"0:{int(x//60):02}:{x%60:05.2f}"
hdr = open("/tmp/claude-0/-home-user-cheksiz/2a2cb10c-3170-5137-84c1-a19971a38055/scratchpad/aytilmagan/sub_uz.ass").read().split("[Events]")[0]
ev = "".join(f"Dialogue: 0,{tt(a)},{tt(b)},{'C' if w=='R' else 'S'},,0,0,0,,{{\\fad(150,150)}}{t}\n" for a, b, w, t in SUB)
hdr = hdr.replace("[Events]", "") + "Style: X,Inter ExtraBold,190,&H002020FF,&H00FFFFFF,&H00000040,&H80000000,-1,0,0,0,100,100,6,0,1,9,4,5,40,40,0,1\n\n"
ev += "Dialogue: 1,0:00:56.45,0:00:59.40,X,,0,0,0,,{\\pos(540,1060)\\fad(80,200)\\fscx140\\fscy140\\t(0,180,\\fscx100\\fscy100)}STOP\n"
open(f"{B}/sub_uz.ass","w").write(hdr + "[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n" + ev)
run(["ffmpeg","-v","error","-y","-i",f"{B}/cine.mp4","-i",f"{B}/mix.wav","-vf",f"subtitles={B}/sub_uz.ass",
     "-c:v","libx264","-preset","medium","-crf","21","-c:a","aac","-b:a","160k","-shortest","-movflags","+faststart",f"{B}/robot_korib_chiqish.mp4"])
