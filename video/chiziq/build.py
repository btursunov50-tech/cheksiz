# «Bitta chiziq»: 3 klipni ulaydi (cine + whoosh), Veo ambient ovozini (clips/*.m4a, /klip-tekshir ovozni olib tashlaydi) saqlaydi, oxirida avatar + yakuniy karta.
# python3 video/chiziq/build.py <ishchi papka>
import os, subprocess, sys
sys.path.insert(0, ".claude/skills/video-yig"); from yig import avq_plate
B = os.path.abspath(sys.argv[1]); os.makedirs(B, exist_ok=True)
R = lambda c: subprocess.run(c, check=True)
CL = ["c1", "c2a", "c2b"]
dur = lambda f: float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f], capture_output=True, text=True).stdout)
parts, cuts, t = [], [], 0.0
for n in CL:
    f = f"video/chiziq/clips/{n}.mp4"; o = f"{B}/{n}.mp4"; d = dur(f)
    R(["ffmpeg", "-v", "error", "-y", "-i", f, "-i", f"video/chiziq/clips/{n}.m4a", "-map", "0:v", "-map", "1:a", "-shortest", "-vf", "fps=30,scale=1080:1920:flags=lanczos,setsar=1,format=yuv420p",
       "-af", "aresample=48000", "-ac", "2", "-c:v", "libx264", "-crf", "18", "-c:a", "aac", "-b:a", "192k", o])
    parts.append(o); t += d; cuts.append(round(t, 2))
cuts = cuts[:-1]; T = t
open(f"{B}/l.txt", "w").write("".join(f"file '{p}'\n" for p in parts))
R(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{B}/l.txt", "-c", "copy", f"{B}/raw.mp4"])
R(["bash", "video/cine.sh", f"{B}/raw.mp4", f"{B}/cine.mp4", " ".join(map(str, cuts))])
R(["ffmpeg", "-v", "error", "-y", "-i", f"{B}/raw.mp4", "-vn", "-af", "volume=6dB", "-ar", "48000", "-ac", "2", f"{B}/amb.wav"])
R(["bash", "video/sfx.sh", f"{B}/amb.wav", f"{B}/amb_sfx.wav", " ".join(map(str, cuts))])
avq_plate("Siz-chi?|Do'koningizni odamlar ko'ryaptimi?|Izohga yozing!", f"{B}/avq.png")
R(["ffmpeg", "-v", "error", "-y", "-i", "video/avatar.mp4", "-i", f"{B}/avq.png", "-filter_complex",
   "[0:v]trim=0:3,setpts=PTS-STARTPTS,scale=1080:1920,fps=30,setsar=1[a];[a][1:v]overlay=0:1200:enable='gte(t,0.3)',format=yuv420p[v]",
   "-map", "[v]", "-c:v", "libx264", "-crf", "20", "-r", "30", f"{B}/av.mp4"])
R(["ffmpeg", "-v", "error", "-y", "-i", f"{B}/cine.mp4", "-c:v", "libx264", "-crf", "20", "-r", "30", "-an", f"{B}/main.mp4"])
open(f"{B}/s.txt", "w").write(f"file '{B}/main.mp4'\nfile '{B}/av.mp4'\nfile '{os.path.abspath('video/end/end_uz.mp4')}'\n")
R(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{B}/s.txt", "-c", "copy", f"{B}/allv.mp4"])
R(["ffmpeg", "-v", "error", "-y", "-i", f"{B}/allv.mp4", "-i", f"{B}/amb_sfx.wav", "-filter_complex",
   f"[1:a]afade=t=out:st={T-1.5}:d=1.5,apad=pad_dur=7,loudnorm=I=-16:TP=-1.5[a]", "-map", "0:v", "-map", "[a]",
   "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", f"{B}/chiziq_uz.mp4"])
print("cuts", cuts, "T", round(T, 2))
