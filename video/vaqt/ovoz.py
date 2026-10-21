# timeline.LINES dagi qatorlarni (voice_cut/NN.wav) o'z vaqtiga qo'yadi + hook tovushi (tik-tik, zarba), tanga jiringi, qum shitirlashi → ovoz.flac
import subprocess, sys
sys.path.insert(0, "video/vaqt"); import timeline as tl
T = tl.CUT[-1]
inp, fc, lab = [], "", []
for i, (f, st, who, text) in enumerate(tl.LINES):
    inp += ["-i", f"video/vaqt/voice_cut/{f}.wav"]; ms = int(st * 1000)
    fc += f"[{i}:a]aresample=48000,adelay={ms}|{ms}[a{i}];"; lab.append(f"[a{i}]")
hook = "0.5*sin(2*PI*2200*t)*exp(-60*mod(t,0.45))*lt(t,3.6)+0.9*sin(2*PI*48*t)*exp(-2.2*(t-3.4))*gte(t,3.4)"
clink = ("0.35*(sin(2*PI*2870*t)+0.7*sin(2*PI*4410*t)+0.5*sin(2*PI*6130*t)+0.4*sin(2*PI*1630*t))*exp(-5*t)"
         "+0.25*(sin(2*PI*3100*t)+0.6*sin(2*PI*4820*t))*exp(-9*(t-0.22))*gte(t,0.22)+0.15*sin(2*PI*3300*t)*exp(-12*(t-0.37))*gte(t,0.37)")
n = len(tl.LINES)
fc += f"aevalsrc='{hook}':s=48000:d=7[hk];"; lab.append("[hk]")
for j, c in enumerate(tl.CLINK):
    ms = int(c * 1000); fc += f"aevalsrc='{clink}':s=48000:d=2.5,adelay={ms}|{ms}[c{j}];"; lab.append(f"[c{j}]")
for j, s in enumerate(tl.SAND):
    ms = int(s * 1000)
    fc += (f"anoisesrc=d=2.6:c=pink:a=0.25:r=48000,bandpass=f=4000:w=3000,afade=t=in:d=0.4,afade=t=out:st=1.6:d=1.0,"
           f"adelay={ms}|{ms}[s{j}];"); lab.append(f"[s{j}]")
fc += "".join(lab) + f"amix=inputs={len(lab)}:normalize=0,atrim=0:{T}[o]"
subprocess.run(["ffmpeg", "-v", "error", "-y", *inp, "-filter_complex", fc, "-map", "[o]", "-ac", "1", "video/vaqt/ovoz.flac"], check=True)
print("ovoz.flac", T, "s")
for s in tl.SUB: print(s)
