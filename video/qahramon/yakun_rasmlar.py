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
# Rasmlar tayyor (egasi tasdiqladi, 2026-10-22): y1..y5. Endi Veo video promptlari — boshlang'ich kadr = shu rasm.
def vid(name, start, look, keep, extra=""):
    return (f"Vertical 9:16, 8 seconds. Camera: a slow steady push-in from the knees-up framing to a close-up of his head and shoulders (0 to 5 s), "
            f"then at about 6 s a fast whip pan to the right with strong motion blur, the clip ends inside the blur of golden valley light. "
            f"Action: {name} stands still on the hilltop, {start}, looking straight into the camera with {look}. {extra}"
            f"At about 4.5 s he slowly turns his head to the right side of the frame and looks to the right, as if passing his gaze to the next hero, "
            f"and the camera follows his look with the whip pan. His robe moves gently in the morning wind, mist drifts slowly over the river below, "
            f"the sun glows behind the mountains. Keep {name} exactly as in the image for the whole clip: the same face, {keep}. "
            f"Keep the background exactly as in the image. No new people, no extra objects, no text, no captions, no watermark. Realistic cinematic film look.")
V = [
 ("V1", "Ibn Sino", "y1_ibnsino_qir_yuz", "8 s", vid("Ibn Sina", "holding his book against his chest", "a calm kind look",
   "full dark black beard, white turban with a long tail, dark blue robe with gold border, brown book")),
 ("V2", "Beruniy", "y2_beruniy_qir", "8 s", vid("Al-Biruni", "holding his brass astrolabe", "a wise calm look",
   "white-grey beard, cream turban, brown robe with gold border, cream scarf, brass astrolabe")),
 ("V3", "Jaloliddin", "y3_jaloliddin_qir", "8 s", vid("Jaloliddin Manguberdi", "his hand on the hilt of his sword", "a brave proud look",
   "short dark beard, dark steel helmet, fur collar, scale armour, dark blue cloak")),
 ("V4", "Amir Temur (montajda 1 s uzunroq)", "y4_temur_qir", "8 s", vid("Amir Temur", "his hand on the hilt of his sword", "a strong calm look",
   "full black beard, golden crown with white plume, golden breastplate with red and green jewels, blue and gold robe, red sleeves")),
 ("V5", "Ulug'bek (oxirgi; keyin Bahodir — haqiqiy kadr)", "y5_ulugbek_qir", "8 s", vid("Ulugh Beg", "holding his golden astrolabe", "a calm wise look",
   "young narrow face, thin upturned black moustache, small pointed black beard, white turban with green band and green jewel, dark green robe with gold embroidery",
   "At the start he is looking up at the sky; in the first second he lowers his gaze to the camera. ")),
]
os.makedirs("video/qahramon/web", exist_ok=True); e = html.escape; cards = []
for n, name, img, dur, p in V:
    im = Image.open(f"video/qahramon/img/{img}.jpg"); im.thumbnail((360, 640)); im.save(f"video/qahramon/web/{img}_ref.webp", quality=82)
    cards.append(f'''<article class="card" id="{n}">
<header><span class="num">{n}</span><h2>{e(name)}</h2><span class="dur">9:16 (tik), {dur}</span></header>
<p class='lbl'>📎 Veo'ga boshlang'ich kadr qilib shu rasmni yuklang</p><div class='refs'><figure><img src="web/{img}_ref.webp" alt="{e(name)}"><figcaption>{e(name)} — tasdiqlangan rasm</figcaption></figure></div>
<div class="txt"><p class="lbl">🎬 Video prompt (Veo, rasm → video)</p><pre id="p{n}">{e(p)}</pre>
<button type="button" class="copy" data-t="p{n}">Nusxa olish</button></div></article>''')
head = open("video/robot/page_head.html").read()
head = head.replace("<title>Robot bilan choy sahnalari</title>", "<title>Birlik yakuni videolari</title>")
head = head.replace("«Robot bilan bir piyola choy» sahnalari", "«Birlik» yakuni — video promptlar")
i = head.index('<p class="intro">'); j = head.index('</p>', i) + 4
INTRO = ("Tartib: Ibn Sino → Beruniy → Jaloliddin → Amir Temur (1 s ko'proq) → Ulug'bek → Bahodir (haqiqiy kadr). "
         "5 rasm ham tayyor ✅. Har kartada: rasmni Veo'ga boshlang'ich kadr qilib yuklang, o'lchamni 9:16 qiling, promptni qo'ying. "
         "Kamera qahramon boshiga yaqinlashadi, u boshini o'ngga buradi, kamera keskin o'ngga o'tadi — montajda keyingi qahramonga ulayman.")
head = head[:i] + f'<p class="intro">{e(INTRO)}</p>' + head[j:]
head = head.replace("</style>", ".refs{display:flex;gap:10px;flex-wrap:wrap}.refs figure{margin:0;width:auto}.refs img{width:150px;border-radius:6px;display:block}"
                    ".refs figcaption{font-size:12px;color:var(--muted);margin-top:4px}.ph{width:150px;height:266px;border:2px dashed var(--sun);border-radius:6px;display:grid;place-items:center;font:600 40px var(--display);color:var(--sun)}</style>")
open("video/qahramon/yakun.html", "w").write(head + "\n".join(cards) + open("video/robot/page_tail.html").read())
print(len(V))
