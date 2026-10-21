#!/usr/bin/env python3
"""Loyiha kliplarini ovoz vaqtiga moslab bitta video qiladi.

python3 .claude/skills/video-yig/yig.py --dir video/robot --work <scratchpad>/robot_build [--n 13] \
    [--music fayl.mp3:boshlanish_s] [--avq "Siz-chi?|Savol matni|Izohga yozing!"] [--lang uz] [--tl en] [--send]

Loyiha papkasida: timeline.py (SUB, CUT, CLIP, START, ixtiyoriy STOP, TEXT — ekrandagi katta yozuvlar, BOOM — qo'shimcha zarba soniyalari, MUSIC_END — musiqa to'xtaydigan soniya, MUSIC_FADE — musiqa avatar/karta ustida davom etib shuncha soniyada so'nadi), clips/<CLIP>.mp4, ovoz (--voice, standart dialog.flac).
Natija: <work>/final_<lang>.mp4 (+ --send bo'lsa 30 MB dan kichik nusxa) va tekshiruv jadvali.
"""
import argparse, importlib.util, os, re, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

HDR = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: S,Inter ExtraBold,64,&H00FFFFFF,&H00FFFFFF,&H00201008,&H90000000,-1,0,0,0,100,100,0,0,1,5,3,2,70,70,300,1
Style: C,Inter ExtraBold,64,&H00FFE600,&H00FFFFFF,&H00301000,&H90000000,-1,0,0,0,100,100,0,0,1,5,3,2,70,70,300,1
Style: X,Inter ExtraBold,190,&H002020FF,&H00FFFFFF,&H00000040,&H80000000,-1,0,0,0,100,100,6,0,1,9,4,5,40,40,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

def run(c): subprocess.run(c, check=True)
def tt(x): return f"0:{int(x//60):02}:{x%60:05.2f}"

def avq_plate(text, path):
    a, b, c = text.split("|")
    F = lambda s: ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-Bold.otf", s)
    im = Image.new("RGBA", (1080, 440), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([50, 10, 1030, 430], radius=36, fill=(10, 12, 18, 225))
    d.rounded_rectangle([50, 10, 1030, 24], radius=8, fill=(240, 200, 110))
    d.text(((1080 - d.textlength(a, font=F(80))) / 2, 55), a, font=F(80), fill="white")
    lines, cur = [], ""
    for x in b.split():
        s = (cur + " " + x).strip()
        if d.textlength(s, font=F(52)) <= 940: cur = s
        else: lines.append(cur); cur = x
    lines.append(cur); y = 165
    for l in lines: d.text(((1080 - d.textlength(l, font=F(52))) / 2, y), l, font=F(52), fill=(255, 236, 160)); y += 64
    d.text(((1080 - d.textlength(c, font=F(56))) / 2, y + 18), c, font=F(56), fill="white")
    im.save(path)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--dir", required=True); p.add_argument("--work", required=True)
    p.add_argument("--n", type=int); p.add_argument("--voice", default="dialog.flac")
    p.add_argument("--music"); p.add_argument("--music-vol", type=float, default=0.5)
    p.add_argument("--avq"); p.add_argument("--lang", default="uz"); p.add_argument("--send", action="store_true")
    p.add_argument("--reuse", action="store_true", help="tayyor cine.mp4 ni qayta ishlatish")
    p.add_argument("--tl", help="tarjima: timeline_<tl>.py dagi SUB/TEXT timeline.py ustidan yoziladi (masalan en, ru)")
    a = p.parse_args()
    B = os.path.abspath(a.work); os.makedirs(B, exist_ok=True)
    spec = importlib.util.spec_from_file_location("tl", os.path.join(a.dir, "timeline.py"))
    tl = importlib.util.module_from_spec(spec); spec.loader.exec_module(tl)
    if a.tl:
        sp2 = importlib.util.spec_from_file_location("tl2", os.path.join(a.dir, f"timeline_{a.tl}.py"))
        t2 = importlib.util.module_from_spec(sp2); sp2.loader.exec_module(t2)
        for k in ("SUB", "TEXT", "STOP"):
            if hasattr(t2, k): setattr(tl, k, getattr(t2, k))
    N = a.n or len(tl.CLIP); CUT = tl.CUT[:N + 1]; T = CUT[-1]; START = getattr(tl, "START", {})
    cuts = " ".join(str(x) for x in CUT[1:-1])

    if not a.reuse:
        parts = []
        for i in range(N):
            d = CUT[i + 1] - CUT[i]; s0 = START.get(i + 1, 0)
            f = os.path.join(a.dir, "clips", tl.CLIP[i] + ".mp4"); o = f"{B}/p{i+1:02}.mp4"
            dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f],
                                       capture_output=True, text=True).stdout)
            k = max(1.0, d / (dur - s0))
            if k > 1.8: print(f"DIQQAT: {i+1}-sahna klipi {k:.2f} marta sekinlashadi (1.8 dan ko'p) — yangi klip so'rang")
            vf = f"trim=start={s0},setpts=PTS-STARTPTS"
            if k > 1.0: vf += f",setpts={k:.4f}*PTS,minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:vsbmc=1"
            vf += f",fps=30,scale=1080:1920:flags=lanczos,trim=duration={d:.3f},setsar=1,format=yuv420p"
            run(["ffmpeg", "-v", "error", "-y", "-i", f, "-vf", vf, "-an", "-c:v", "libx264", "-preset", "fast", "-crf", "18", o])
            parts.append(o)
        open(f"{B}/list.txt", "w").write("".join(f"file '{x}'\n" for x in parts))
        run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{B}/list.txt", "-c", "copy", f"{B}/raw.mp4"])
        run(["bash", f"{ROOT}/video/cine.sh", f"{B}/raw.mp4", f"{B}/cine.mp4", cuts])

    run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(a.dir, a.voice), "-af",
         f"atrim=0:{T},afade=t=out:st={T-0.4}:d=0.4,aresample=48000", "-ac", "2", f"{B}/voice.wav"])
    boom = " ".join(str(x) for x in getattr(tl, "BOOM", []) if x < T)
    run(["bash", f"{ROOT}/video/sfx.sh", f"{B}/voice.wav", f"{B}/voice_sfx.wav", (cuts + " " + boom).strip()])
    if a.music:
        mf, ms = a.music.rsplit(":", 1); ME = min(T, getattr(tl, "MUSIC_END", T)); fo = 0.3 if ME < T else 2
        TT = T  # MUSIC_FADE: musiqa avatar va yakuniy karta ustida davom etib, oxirgi shuncha soniyada sekin so'nadi
        if ME == T and getattr(tl, "MUSIC_FADE", 0) and a.avq: TT = T + 7; ME = TT; fo = tl.MUSIC_FADE
        run(["ffmpeg", "-v", "error", "-y", "-i", f"{B}/voice_sfx.wav", "-ss", ms, "-i", mf, "-filter_complex",
             f"[1:a]atrim=0:{ME},asetpts=PTS-STARTPTS,afade=t=in:d=1.5,afade=t=out:st={ME-fo}:d={fo},apad=whole_dur={TT},volume={a.music_vol},aresample=48000,aformat=channel_layouts=stereo[m];"
             f"[0:a]apad=whole_dur={TT},asplit[v][sc];[m][sc]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[md];"
             "[v][md]amix=inputs=2:normalize=0,loudnorm=I=-15:TP=-1.5:LRA=11[a]", "-map", "[a]", "-ar", "48000", f"{B}/mix.wav"])
    else:
        run(["ffmpeg", "-v", "error", "-y", "-i", f"{B}/voice_sfx.wav", "-af", "loudnorm=I=-15:TP=-1.5:LRA=11", "-ar", "48000", f"{B}/mix.wav"])

    ev = "".join(f"Dialogue: 0,{tt(s)},{tt(e)},{'C' if w=='R' else 'S'},,0,0,0,,{{\\fad(150,150)}}{x}\n"
                 for s, e, w, x in tl.SUB if s < T)
    stop = getattr(tl, "STOP", None)
    if stop and stop[0] < T:
        ev += f"Dialogue: 1,{tt(stop[0])},{tt(stop[1])},X,,0,0,0,,{{\\pos(540,1060)\\fad(80,200)\\fscx140\\fscy140\\t(0,180,\\fscx100\\fscy100)}}STOP\n"
    for tx in getattr(tl, "TEXT", []):  # ekrandagi katta yozuvlar: (boshi, oxiri, matn, o'lcham[, rang "RRGGBB"[, (x, y)]])
        s0, e0, x, sz = tx[:4]; col = tx[4] if len(tx) > 4 else None; pos = tx[5] if len(tx) > 5 else (540, 1250)
        c = f"\\1c&H{col[4:6]}{col[2:4]}{col[0:2]}&\\3c&H0A1420&" if col else ""  # rang berilsa kontur to'q jigarrang
        if s0 < T:
            ev += f"Dialogue: 1,{tt(s0)},{tt(e0)},X,,0,0,0,,{{\\pos({pos[0]},{pos[1]})\\fs{sz}{c}\\fad(80,200)\\fscx130\\fscy130\\t(0,180,\\fscx100\\fscy100)}}{x}\n"
    open(f"{B}/sub.ass", "w").write(HDR + ev)
    run(["ffmpeg", "-v", "error", "-y", "-i", f"{B}/cine.mp4", "-vf", f"ass={B}/sub.ass,format=yuv420p",
         "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-r", "30", "-an", f"{B}/main_v.mp4"])

    seq = [f"{B}/main_v.mp4"]; tail = 0
    if a.avq:
        avq_plate(a.avq, f"{B}/avq.png")
        run(["ffmpeg", "-v", "error", "-y", "-i", f"{ROOT}/video/avatar.mp4", "-i", f"{B}/avq.png", "-filter_complex",
             "[0:v]trim=0:3,setpts=PTS-STARTPTS,scale=1080:1920:flags=lanczos,fps=30,setsar=1[a];[a][1:v]overlay=0:1200:enable='gte(t,0.3)',format=yuv420p[v]",
             "-map", "[v]", "-c:v", "libx264", "-crf", "20", "-r", "30", f"{B}/av.mp4"])
        seq.append(f"{B}/av.mp4"); tail += 3
        seq.append(f"{ROOT}/video/end/end_{a.lang}.mp4"); tail += 4
    open(f"{B}/seq.txt", "w").write("".join(f"file '{x}'\n" for x in seq))
    run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{B}/seq.txt", "-c", "copy", f"{B}/allv.mp4"])
    run(["ffmpeg", "-v", "error", "-y", "-i", f"{B}/allv.mp4", "-i", f"{B}/mix.wav", "-filter_complex",
         f"[1:a]apad=pad_dur={tail}[a]", "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k",
         "-shortest", "-movflags", "+faststart", f"{B}/final_{a.lang}.mp4"])
    F = f"{B}/final_{a.lang}.mp4"

    # tekshiruv
    err = lambda vf: subprocess.run(["ffmpeg", "-i", F, "-vf", vf, "-map", "0:v", "-f", "null", "-"], capture_output=True, text=True).stderr
    fr = re.findall(r"freeze_start: ([0-9.]+)", err("freezedetect=n=0.001:d=0.6"))
    bl = re.findall(r"black_start: ([0-9.]+)", err("blackdetect=d=0.2"))
    si = re.findall(r"silence_start: ([0-9.]+)", subprocess.run(["ffmpeg", "-i", F, "-af", "silencedetect=n=-45dB:d=1.5", "-map", "0:a", "-f", "null", "-"],
                                                                 capture_output=True, text=True).stderr)
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", F], capture_output=True, text=True).stdout)
    ts = [dur * k / 12 for k in range(1, 12)]
    W, H = 216, 384; sheet = Image.new("RGB", (W * 6, H * 2), "black")
    for i, t in enumerate(ts):
        run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", F, "-frames:v", "1", "-vf", f"scale={W}:{H}", f"{B}/_f.png"])
        im = Image.open(f"{B}/_f.png"); ImageDraw.Draw(im).text((5, 5), f"{t:.1f}s", fill="white")
        sheet.paste(im, ((i % 6) * W, (i // 6) * H))
    sheet.save(f"{B}/sheet.jpg", quality=85)
    out = F
    if a.send:
        out = f"{B}/send_{a.lang}.mp4"; br = min(6000, int((26 * 8 * 1024) / dur - 160))
        run(["ffmpeg", "-v", "error", "-y", "-i", F, "-c:v", "libx264", "-b:v", f"{br}k", "-pass", "1", "-passlogfile", f"{B}/pl", "-an", "-f", "null", "/dev/null"])
        run(["ffmpeg", "-v", "error", "-y", "-i", F, "-c:v", "libx264", "-b:v", f"{br}k", "-pass", "2", "-passlogfile", f"{B}/pl", "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", out])
    no = "yo'q"
    print(f"| Nima | Natija |\n|---|---|\n| Uzunlik | {dur:.1f} s ({N} sahna{', avatar + yakuniy karta' if tail else ''}) |")
    print(f"| Qotgan kadr | {no if not fr else ', '.join(fr)} |\n| Qora kadr | {no if not bl else ', '.join(bl) + ' (yakuniy karta fade-in bo`lishi mumkin)'} |")
    print(f"| Ovozsiz joy | {no if not si else ', '.join(si) + (' (musiqasiz avatar/karta — normal)' if not a.music else '')} |\n| Fayl | {out} ({os.path.getsize(out)/1e6:.1f} MB) |\n| Varaq | {B}/sheet.jpg |")

if __name__ == "__main__":
    main()
