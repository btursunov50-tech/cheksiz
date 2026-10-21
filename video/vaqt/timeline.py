# «VAQT» — yig'ish jadvali (/video-yig). Ovoz: ovoz.py → ovoz.flac (qatorlar + hook tik-tik + tanga jiringi + qum shitirlashi).
# Kliplar: h01/t11 = kod/hook.mp4 (0–7.6 / 7.3–9.9), s03r = s03b sekinlashuvli (ramp.py 2.8–3.75, 0.5x),
# xg1–xg5 = oltin xotiralar (kod/xotira_video.py), k14 = kod/epilog.html (kanal + bot havolasi).
LINES = [  # (fayl voice_cut/NN.wav, boshlanishi s, kim: D diktor / V vaqt / B boy / A aziz, matn)
 ("01", 0.4, "D", "Vaqtni sotib olib bo'lmaydi. Lekin sen uni har kuni sotasan."),
 ("02", 8.4, "A", "Bobo, osh tayyor."),
 ("03", 11.4, "B", "Keyin, bolam. Keyin."),
 ("04", 22.4, "V", "Qo'rqma. Olib ketgani kelmadim. Hisobingni ko'rsatgani keldim."),
 ("05", 28.6, "B", "O'tgan yillarimni qaytar, hamma oltinimni ol!"),
 ("06", 36.6, "V", "O'tgan vaqt sotilmaydi. Umr faqat Allohning qo'lida. Men faqat ko'rsataman."),
 ("07", 80.3, "V", "O'ttiz yil."),
 ("08", 82.8, "B", "Bittasini qaytar..."),
 ("09", 85.0, "V", "O'tganini hech kim qaytarolmaydi. Qancha qolganini faqat Alloh biladi. Lekin bugun va hozir hali seniki."),
 ("10", 96.3, "A", "Bobo, osh sovib qoldi."),
 ("11", 99.4, "B", "Hozir, bolam! Hozir!"),
 ("12", 112.3, "D", "O'tgan vaqt qaytmaydi. Shuning uchun — bugun va hozir."),
 ("13", 122.8, "A", "Bobo, bugungi AI maslahati!"),
 ("14", 125.9, "D", "Vaqtingizni bekorga ketkazmang. Har kuni bitta yangi narsa o'rganing. Har tong kanalimizda bepul AI maslahati, savolingizni esa botimizga yozing."),
]
CLINK = [22.23]                                  # tanga polga tegadi (s03r 4.70 s × 1.41)
SAND = [50.0, 56.7, 63.4, 70.7, 80.3]            # xotira qumga aylanadi (egasi: xotiralar 5/3 marta sekin, qum ~2 s)
CUT = [0, 7.6, 15.6, 28.0, 36.0, 45.0, 52.0, 58.7, 65.4, 72.7, 82.3, 95.7, 103.7, 111.7, 119.7, 122.3, 132.7, 140.5]
CLIP = ["h01", "s02", "s03r", "s04", "s05", "xg1", "xg2", "xg3", "xg4", "xg5", "s07b", "s08", "s09", "s10", "t11", "s13", "k14"]
START = {}
BOOM = []
MUSIC_FADE = 5
TEXT = [(113.9, 119.5, "Foyda —\\Nbugun va hozir.", 64, "FFC34D", (560, 820)), (122.4, 124.5, "BUGUN", 120, "FFC34D", (540, 330))]
import json, os, re
_segs = json.load(open(os.path.join(os.path.dirname(__file__), "voice_cut", "segs.json")))
def _subs():
    out = []
    for f, st, who, text in LINES:
        segs = _segs[f]["segs"]; parts = []
        for p in [p.strip() for p in re.findall(r"[^.?!]+[.?!]+", text)] or [text]:
            parts += [q.strip() for q in re.findall(r"[^,]+,|[^,]+$", p)] if len(p) > 45 else [p]
        L = sum(len(p) for p in parts); total = segs[-1][1] - segs[0][0]; acc = 0; i0 = 0
        for k, p in enumerate(parts):
            acc += len(p)
            if k == len(parts) - 1: i1 = len(segs) - 1
            else:
                target = segs[0][0] + total * acc / L
                rng_ = range(i0, len(segs) - 1)   # gap pauzasi katta (gap oxiri) bo'lgan joylar afzal
                big = [j for j in rng_ if segs[j + 1][0] - segs[j][1] > 0.5]
                i1 = min(big or rng_, key=lambda j: abs(segs[j][1] - target))
            out.append((round(st + segs[i0][0], 2), round(st + segs[i1][1] + 0.15, 2), "R" if who == "D" else "O", p))
            i0 = i1 + 1
            if i0 >= len(segs): break
    return out
SUB = _subs()
