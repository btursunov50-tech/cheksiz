# Tayyor videoda bir-biriga o'xshash kadrlarni topadi (ko'z bilan emas, dastur bilan): har 0.25 s da kadr «izi» (dHash),
# turli sahnalardagi juda o'xshash juftlar chiqariladi.  python3 takror.py VIDEO.mp4 kesimlar.json
import cv2, json, sys, numpy as np
cap = cv2.VideoCapture(sys.argv[1]); fps = cap.get(cv2.CAP_PROP_FPS)
cuts = [c[0] for c in json.load(open(sys.argv[2]))] + [1e9]
def seg(t): return max(i for i, c in enumerate(cuts) if c <= t)
H = []; k = 0; step = int(round(fps / 4))
while True:
    ok, fr = cap.read()
    if not ok: break
    if k % step == 0:
        g = cv2.cvtColor(cv2.resize(fr, (17, 16)), cv2.COLOR_BGR2GRAY).astype(int)
        H.append((k / fps, (g[:, 1:] > g[:, :-1]).flatten()))
    k += 1
found = {}
for i in range(len(H)):
    ti, hi = H[i]
    if hi.mean() < 0.05 or hi.mean() > 0.95: continue   # qora/bir xil kadr
    for j in range(i + 1, len(H)):
        tj, hj = H[j]
        if tj - ti < 3: continue
        si, sj = seg(ti), seg(tj)
        if si == sj: continue
        d = (hi != hj).mean()
        if d < float(sys.argv[3] if len(sys.argv) > 3 else 0.12):
            key = (si, sj)
            if key not in found or d < found[key][2]: found[key] = (ti, tj, d)
for (si, sj), (ti, tj, d) in sorted(found.items(), key=lambda x: x[1][0]):
    print(f"o'xshash: {int(ti//60)}:{ti%60:04.1f} (sahna {si}) ~ {int(tj//60)}:{tj%60:04.1f} (sahna {sj})  farq {d:.2f}")
print("tekshirildi:", len(H), "kadr")
