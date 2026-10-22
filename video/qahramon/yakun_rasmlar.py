# «Birlik» yakuni — rasm promptlari sahifasi: har promptning yonida ChatGPT'ga biriktiriladigan rasmlar (egasi, 2026-10-22).
# Tartib: Ibn Sino → Beruniy → Jaloliddin → Temur (+1 s) → Ulug'bek → Bahodir (haqiqiy kadr).
import html, os
from PIL import Image
STY = "Cinematic photorealistic film still, vertical 9:16 format, warm golden light, deep soft shadows, gentle film grain, no text, no letters, no watermark."
BG = "Keep the background exactly as in the background image: the river, the sunrise, the old paxsa village and the orchards."
def hero(name, ref, look, keep):
    return (f"Attach the background image and the {name} reference image. Place {name} in the center of the background image, standing on the river bank, "
            f"chest-up to waist-up, {look}. Keep his face exactly as in the reference image, the same person: {keep}. {BG} {STY}")
P = [
 ("F", "Fon (birinchi shuni qiling)", [], "Wide cinematic landscape, no people: a calm river at sunrise in old Uzbekistan, on the far bank an old village of clay paxsa houses with flat roofs, poplar trees and blooming apricot orchards, soft morning mist over the water, the golden sun rising above distant mountains. The middle of the frame stays open, like a stage for a person to stand in front of it. " + STY),
 ("Q1", "Ibn Sino fon oldida", ["fon", "s08_ibnsino_portret"], hero("Ibn Sina", "s08", "holding his book, looking straight into the camera with a calm kind look", "dark black beard, white turban, dark blue robe with gold border")),
 ("Q2", "Beruniy fon oldida", ["fon", "s09_beruniy_portret"], hero("Al-Biruni", "s09", "holding his brass astrolabe, looking straight into the camera with a wise calm look", "grey beard, grey turban, brown robe with scarf")),
 ("Q3", "Jaloliddin fon oldida", ["fon", "q_jaloliddin"], hero("Jaloliddin Manguberdi", "q", "looking straight into the camera with a brave proud look", "short dark beard, steel helmet with plume, scale armour and blue cloak")),
 ("Q4", "Amir Temur fon oldida", ["fon", "q_temur"], hero("Amir Temur", "q", "looking straight into the camera with a strong calm look", "dark beard, golden crown, golden breastplate with red and green jewels, blue robe")),
 ("Q5", "Ulug'bek fon oldida", ["fon", "s02_ulugbek_rasadxona"], hero("Ulugh Beg", "s02", "looking straight into the camera with a calm wise look", "young narrow face, thin upturned black moustache, small pointed black beard, white turban with the green jewel, green and gold robe")),
]
NAMES = {"fon": "F — fon rasmi (siz qilasiz)", "s08_ibnsino_portret": "Ibn Sino", "s09_beruniy_portret": "Beruniy", "q_jaloliddin": "Jaloliddin",
         "q_temur": "Amir Temur", "s02_ulugbek_rasadxona": "Ulug'bek (yangi yuz)"}
os.makedirs("video/qahramon/web", exist_ok=True); e = html.escape; cards = []
for n, name, refs, p in P:
    th = ""
    for r in refs:
        if r == "fon":
            th += '<figure><div class="ph">F</div><figcaption>F — fon (avval qiling)</figcaption></figure>'
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
         "Avval F (fon) rasmini qiling. Keyin har kartadagi rasmlarni (fon + qahramon) ChatGPT'ga biriktirib, promptni qo'ying: "
         "yuz o'zgarmasligi uchun qahramon rasmi albatta biriktiriladi. Rasmni bosib turib saqlab oling.")
head = head[:i] + f'<p class="intro">{e(INTRO)}</p>' + head[j:]
head = head.replace("</style>", ".refs{display:flex;gap:10px;flex-wrap:wrap}.refs figure{margin:0;width:150px}.refs img{width:150px;border-radius:6px;display:block}"
                    ".refs figcaption{font-size:12px;color:var(--muted);margin-top:4px}.ph{width:150px;height:266px;border:2px dashed var(--sun);border-radius:6px;display:grid;place-items:center;font:600 40px var(--display);color:var(--sun)}</style>")
open("video/qahramon/yakun.html", "w").write(head + "\n".join(cards) + open("video/robot/page_tail.html").read())
print(len(P))
