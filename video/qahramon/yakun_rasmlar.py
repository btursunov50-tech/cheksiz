# «Birlik» yakuni — rasm promptlari sahifasi: har promptning yonida ChatGPT'ga biriktiriladigan rasmlar (egasi, 2026-10-22).
# Tartib: Ibn Sino → Beruniy → Jaloliddin → Temur (+1 s) → Ulug'bek → Bahodir (haqiqiy kadr).
import html, os
from PIL import Image
STY = "Cinematic photorealistic film still, vertical 9:16 format, warm golden light, deep soft shadows, gentle film grain, no text, no letters, no watermark."
BG = ("Use the landscape image as the place: the same river with morning mist, the old clay paxsa village, the blooming apricot orchards, the poplars, "
      "the mountains and the rising sun, but seen from high above, from the top of a hill, so the whole valley spreads wide and deep behind him.")
def hero(name, ref, look, keep):
    # Egasi (2026-10-22): GPT'dagi Ibn Sino qir tepasida (y1_ibnsino_qir_gpt) yoqdi — hamma qahramon aynan shu joyda, shu kadrda turadi
    # (whip pan zanjiri uchun fon bir xil bo'lishi kerak).
    return (f"Attach the Ibn Sina hilltop image and the {name} reference image. Use the Ibn Sina hilltop image only for the place and the framing: "
            f"the same grassy hill, the same valley below with the winding river, the clay village, the blooming orchards and poplars, the same mountains, "
            f"the same golden sunrise and morning haze, the same camera height and angle. Ibn Sina is not in this picture: in his place stands {name}, "
            f"seen from the knees up, in the same spot and the same size in the frame, {look}. "
            f"Keep his face exactly as in the {name} reference image, the same person: {keep}. {STY}")
FIX1 = ("Attach the Ibn Sina hilltop image and the Ibn Sina portrait reference image. Keep the hilltop image exactly the same: the hill, the valley, the river, "
        "the village, the sunrise, his pose, the book, the white turban and the dark blue robe with gold border, the light and the framing. "
        "Change only his face so it is exactly the face from the portrait reference image, the same person: a fuller dark black beard and moustache, "
        "a slightly broader face, a serious calm look, no smile. " + STY)
P = [
 ("Q1", "Ibn Sino — faqat yuzini tuzatish", ["y1_ibnsino_qir_gpt", "s08_ibnsino_portret"], FIX1),
 ("Q2", "Beruniy qir tepasida", ["y1_ibnsino_qir_gpt", "s09_beruniy_portret"], hero("Al-Biruni", "s09", "holding his brass astrolabe, looking straight into the camera with a wise calm look", "grey beard, grey turban, brown robe with scarf")),
 ("Q3", "Jaloliddin qir tepasida", ["y1_ibnsino_qir_gpt", "q_jaloliddin"], hero("Jaloliddin Manguberdi", "q", "looking straight into the camera with a brave proud look", "short dark beard, steel helmet with plume, scale armour and blue cloak")),
 ("Q4", "Amir Temur qir tepasida", ["y1_ibnsino_qir_gpt", "q_temur"], hero("Amir Temur", "q", "looking straight into the camera with a strong calm look", "dark beard, golden crown, golden breastplate with red and green jewels, blue robe")),
 ("Q5", "Ulug'bek qir tepasida", ["y1_ibnsino_qir_gpt", "s02_ulugbek_rasadxona"], hero("Ulugh Beg", "s02", "looking straight into the camera with a calm wise look", "young narrow face, thin upturned black moustache, small pointed black beard, white turban with the green jewel, green and gold robe")),
]
NAMES = {"y1_ibnsino_qir_gpt": "Ibn Sino qir tepasida (GPT, sizga yoqqan)", "fon": "F — fon rasmi (siz qilasiz)", "s08_ibnsino_portret": "Ibn Sino", "s09_beruniy_portret": "Beruniy", "q_jaloliddin": "Jaloliddin",
         "q_temur": "Amir Temur", "s02_ulugbek_rasadxona": "Ulug'bek (yangi yuz)"}
os.makedirs("video/qahramon/web", exist_ok=True); e = html.escape; cards = []
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
         "Joy: GPT'dagi Ibn Sino qir tepasida (sizga yoqqan) — hamma qahramon aynan shu joyda turadi. Har kartadagi 2 rasmni ChatGPT'ga biriktirib, promptni qo'ying: "
         "yuz o'zgarmasligi uchun qahramon rasmi albatta biriktiriladi. Rasmni bosib turib saqlab oling.")
head = head[:i] + f'<p class="intro">{e(INTRO)}</p>' + head[j:]
head = head.replace("</style>", ".refs{display:flex;gap:10px;flex-wrap:wrap}.refs figure{margin:0;width:auto}.refs img{width:150px;border-radius:6px;display:block}"
                    ".refs figcaption{font-size:12px;color:var(--muted);margin-top:4px}.ph{width:150px;height:266px;border:2px dashed var(--sun);border-radius:6px;display:grid;place-items:center;font:600 40px var(--display);color:var(--sun)}</style>")
open("video/qahramon/yakun.html", "w").write(head + "\n".join(cards) + open("video/robot/page_tail.html").read())
print(len(P))
