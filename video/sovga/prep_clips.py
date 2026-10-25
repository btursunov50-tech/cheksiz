# timeline.CLIP_USE bo'laklarini clips/use/sNN.mp4 ga yig'adi (bir nechta bo'lak bo'lsa ketma-ket ulanadi).
# Ishlatish: python3 video/sovga/prep_clips.py
import os, runpy, subprocess
D = os.path.dirname(os.path.abspath(__file__))
U = runpy.run_path(os.path.join(D, "timeline.py"))["CLIP_USE"]
os.makedirs(os.path.join(D, "clips", "use"), exist_ok=True)
for n, seg in sorted(U.items()):
    seg = seg if isinstance(seg, list) else [seg]
    src = os.path.join(D, "clips", f"s{n:02}.mp4"); out = os.path.join(D, "clips", "use", f"s{n:02}.mp4")
    f = "".join(f"[0:v]trim={a}:{b},setpts=PTS-STARTPTS[v{i}];" for i, (a, b) in enumerate(seg))
    f += "".join(f"[v{i}]" for i in range(len(seg))) + f"concat=n={len(seg)}:v=1:a=0[v]"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-filter_complex", f, "-map", "[v]", "-an",
                    "-c:v", "libx264", "-preset", "fast", "-crf", "16", "-r", "24", out], check=True)
    print(n, seg)
