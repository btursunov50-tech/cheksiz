# «Birlik» yakuni — rasm promptlari sahifasi: har promptning yonida ChatGPT'ga biriktiriladigan rasmlar (egasi, 2026-10-22).
# Tartib: Ibn Sino → Beruniy → Jaloliddin → Temur (+1 s) → Ulug'bek → Bahodir (haqiqiy kadr).
import html, os
from PIL import Image
STY = "Cinematic photorealistic film still, vertical 9:16 format, warm golden light, deep soft shadows, gentle film grain, no text, no letters, no watermark."
BG = ("Use the landscape image as the place: the same river with morning mist, the old clay paxsa village, the blooming apricot orchards, the poplars, "
      "the mountains and the rising sun, but seen from high above, from the top of a hill, so the whole valley spreads wide and deep behind him.")
def hero(name, ref, look, keep):
    # Egasi (2026-10-22): odam qir tepasida, kamera pastroqdan — orqa fon (vodiy, qishloq, tog', quyosh) ko'p ko'rinsin.
    return (f"Attach the landscape image and the {name} reference image. {name} stands on the grassy top of a high hill above the valley, "
            f"seen waist-up from a slightly low camera angle, placed in the lower third of the vertical frame, {look}. "
            f"Below and behind him the valley opens wide: the river winding through it, the village and orchards far down, the mountains and the golden sunrise at the top of the frame, soft morning haze between the layers. "
            f"Keep his face exactly as in the reference image, the same person: {keep}. {BG} {STY}")
P = [
 ("F", "Fon (kerak emas: siz yuborgan manzara ishlatiladi)", [], "Wide cinematic landscape, no people: a calm river at sunrise in old Uzbekistan, on the far bank an old village of clay paxsa houses with flat roofs, poplar trees and blooming apricot orchards, soft morning mist over the water, the golden sun rising above distant mountains. The middle of the frame stays open, like a stage for a person to stand in front of it. " + STY),
 ("Q1", "SINOV — Ibn Sino qir tepasida", ["fon", "s08_ibnsino_portret"], hero("Ibn Sina", "s08", "holding his book, looking straight into the camera with a calm kind look", "dark black beard, white turban, dark blue robe with gold border")),
 ("Q2", "Beruniy fon oldida", ["fon", "s09_beruniy_portret"], hero("Al-Biruni", "s09", "holding his brass astrolabe, looking straight into the camera with a wise calm look", "grey beard, grey turban, brown robe with scarf")),
 ("Q3", "Jaloliddin fon oldida", ["fon", "q_jaloliddin"], hero("Jaloliddin Manguberdi", "q", "looking straight into the camera with a brave proud look", "short dark beard, steel helmet with plume, scale armour and blue cloak")),
 ("Q4", "Amir Temur fon oldida", ["fon", "q_temur"], hero("Amir Temur", "q", "looking straight into the camera with a strong calm look", "dark beard, golden crown, golden breastplate with red and green jewels, blue robe")),
 ("Q5", "Ulug'bek fon oldida", ["fon", "s02_ulugbek_rasadxona"], hero("Ulugh Beg", "s02", "looking straight into the camera with a calm wise look", "young narrow face, thin upturned black moustache, small pointed black beard, white turban with the green jewel, green and gold robe")),
]
NAMES = {"fon": "F — fon rasmi (siz qilasiz)", "s08_ibnsino_portret": "Ibn Sino", "s09_beruniy_portret": "Beruniy", "q_jaloliddin": "Jaloliddin",
         "q_temur": "Amir Temur", "s02_ulugbek_rasadxona": "Ulug'bek (yangi yuz)"}
os.makedirs("video/qahramon/web", exist_ok=True); e = html.escape; cards = []
P = [x for x in P if x[0] == "Q1"]  # sinov: avval Ibn Sino, o'xshasa qolganlari
for n, name, refs, p in P:
    th = ""
    for r in refs:
        if r == "fon":
            im = Image.open("video/qahramon/img/fon_vodiy.jpg"); im.thumbnail((360, 640)); im.save("video/qahramon/web/fon_vodiy_ref.webp", quality=82)
            th += '<figure><img src="web/fon_vodiy_ref.webp" alt="Manzara" style="width:260px"><figcaption>Manzara (siz yuborgan)</figcaption></figure>'
        else:
            im = Image.open(f"video/qahramon/img/{r}.jpg"); im.thumbnail((360, 640)); im.save(f"video/qahramon/web/{r}_ref.webp", quality=82)
            th += f'<figure><img src="web/{r}_ref.webp" alt="{e(NAMES[r])}"><figcaption>{e(NAMES[r])}</figcaption></figure>'
    att = (f"<p class='lbl'>📎 ChatGPT'ga shu {len(refs)} ta rasmni biriktiring</p><div class='refs'>{th}</div>" if refs
           else '<p class="lbl">📎 Rasm biriktirish shart emas</p>')
    cards.append(f'''<article class="card" id="{n}">
<header><span class="num">{n}</span><h2>{e(name)}</h2><span class="dur">9:16 (tik)</span></header>
{att}<div class="txt"><p class="lbl">🖼 Rasm prompti (ChatGPT)</p><pre id="p{n}">{e(p)}</pre>
<button type="button" class="copy" data-t="p{n}">Nusxa olish</button></div></article>''')
head = open("video/robot/page_head.html").read()
head = head.replace("<title>Robot bilan choy sahnalari</title>", "<title>Birlik yakuni rasmlari</title>")
head = head.replace("«Robot bilan bir piyola choy» sahnalari", "«Birlik» yakuni — rasmlar")
i = head.index('<p class="intro">'); j = head.index('</p>', i) + 4
INTRO = ("Tartib: Ibn Sino → Beruniy → Jaloliddin → Amir Temur (1 s ko'proq) → Ulug'bek → Bahodir (haqiqiy kadr). "
         "Sinov: avval faqat Ibn Sino. Kartadagi 2 rasmni (manzara + Ibn Sino) ChatGPT'ga biriktirib, promptni qo'ying: "
         "yuz o'zgarmasligi uchun qahramon rasmi albatta biriktiriladi. Rasmni bosib turib saqlab oling.")
head = head[:i] + f'<p class="intro">{e(INTRO)}</p>' + head[j:]
head = head.replace("</style>", ".refs{display:flex;gap:10px;flex-wrap:wrap}.refs figure{margin:0;width:auto}.refs img{width:150px;border-radius:6px;display:block}"
                    ".refs figcaption{font-size:12px;color:var(--muted);margin-top:4px}.ph{width:150px;height:266px;border:2px dashed var(--sun);border-radius:6px;display:grid;place-items:center;font:600 40px var(--display);color:var(--sun)}</style>")
open("video/qahramon/yakun.html", "w").write(head + "\n".join(cards) + open("video/robot/page_tail.html").read())
print(len(P))
