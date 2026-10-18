# «Ko'rish bor» — sahna rasmlari uchun promptlar sahifasi: har sahnada biriktiriladigan namuna rasmlar yonida.
import html
from PIL import Image
STYLE = ("Cinematic film still, vertical 9:16, shot on 35mm, low-key lighting, cold blue-grey color grade with deep blacks, "
         "one warm light source, light haze, fine film grain, realistic skin texture.")
Y1 = ("THE FIRST GUY: a fictional Uzbek young man about 22, slim, short black hair with a clean fade on the sides, light black stubble, "
      "sharp dark eyes, plain black hoodie.")
Y2 = ("THE SECOND GUY: a fictional Uzbek man about 30, broad-shouldered strong build, short neat black hair, short well-groomed black beard, "
      "long black wool coat over a plain black crew-neck sweater.")
K1 = "Keep THE FIRST GUY exactly as in the attached reference image: same face, hair, stubble and black hoodie."
K2 = "Keep THE SECOND GUY exactly as in the attached reference image: same face, beard, hair, coat and sweater."
END = "No text, no letters, no logos, no watermark, no subtitles."
S = [
 (1, "Telefon nuri", "0:00–0:03", "Yuz ming ko'rish, brat!", ["ref_y1", "joy_garaj"],
  "Close-up portrait, vertical 9:16. Almost total darkness in an old garage at night. THE FIRST GUY holds his smartphone close to his face and looks at the screen with a proud, cocky half-smile; the only light is the cold blue-white glow of the phone screen lighting his face from below, everything around him falls into deep black shadow, the screen itself faces him and is not visible to the camera. "
  + Y1 + " Cinematic film still, vertical 9:16, shot on 35mm, extreme low-key lighting, cold blue-grey color grade with deep blacks, fine film grain, realistic skin texture. " + K1 + " " + END),
 (2, "2-yigit soyadan chiqadi", "0:03–0:07", "Yuz ming ko'rish. Nechta odam sotib oldi?", ["ref_y2", "joy_garaj"],
  "Medium shot, vertical 9:16, slightly low angle. In a dark old garage at night, THE SECOND GUY steps out of deep shadow into the edge of the light from a single bare bulb hanging above: half of his face and body still in darkness, the other half lit warm from above, one foot forward mid-step, calm heavy serious gaze straight ahead, no smile. Behind him the rusty metal shutter door fades into black. "
  + Y2 + " Black trousers, black boots. " + STYLE + " " + K2 + " " + END),
 (3, "Telefonni tushiradi", "0:07–0:09", "(BOOM, jimlik)", ["ref_y1", "joy_garaj"],
  "Medium close-up, vertical 9:16. In a dark old garage at night, THE FIRST GUY slowly lowers his smartphone to chest height; his proud smile is gone, his face is serious and a little lost, he looks ahead at someone off-camera. The phone screen glow now lights only his hands and the bottom of his chin, a single bare bulb far behind him makes a soft warm rim light on his hair and shoulders, deep shadows around. "
  + Y1 + " " + STYLE + " " + K1 + " " + END),
 (4, "«Shovqin»", "0:09–0:16", "Nol. Demak, bu savdo emas. Shovqin.", ["ref_y2", "joy_garaj"],
  "Close-up, vertical 9:16, low angle looking slightly up at THE SECOND GUY's face, which gives him quiet power. He looks straight into the camera, calm and cold, no smile, eyes steady, jaw relaxed; a single bare bulb above and behind him makes a warm rim light on his hair and the edge of his beard, the front of his face lit softly, the background is the dark ceiling and rusty beams of an old garage fading into black. "
  + Y2 + " " + STYLE + " " + K2 + " Leave the lower third of the frame darker and simple for on-screen text. " + END),
 (5, "Trend ekranlar", "0:16–0:32", "Trend seni ko'rsatadi. Lekin sotmaydi...", [],
  "Vertical 9:16. A dark room filled with a wall of many glowing smartphone screens floating in black space at different distances, each screen showing a different blurred short vertical video: young people dancing, a person laughing, a cat jumping, colorful lights, fast motion blur on every screen; the faces on the screens are tiny, blurred and unrecognizable. Bright saturated screen colors stand out against the cold dark background, the screens are slightly tilted in different directions like a chaotic social media feed. Cinematic film still, vertical 9:16, shot on 35mm, low-key lighting, cold blue-grey color grade with deep blacks, glow and light bloom from the screens, fine film grain. No readable text, no letters, no app logos, no icons, no watermark, no subtitles."),
 ("6a", "Choyxonada suhbat", "0:34–0:40", "Odamni yig'ish oson. Ushlab qolish qiyin.", ["ref_y1", "ref_y2", "joy_choyxona", "05b_ofitsiant"],
  "Medium two-shot, vertical 9:16, eye level across a low wooden choyxona table at night. THE FIRST GUY and THE SECOND GUY sit facing each other at the table, seen in three-quarter view; THE SECOND GUY leans slightly forward with his forearms on the table and talks calmly and seriously, THE FIRST GUY listens with a doubtful, thoughtful look. On the table: a white teapot with a blue cotton-boll pattern, two piyola tea bowls and a round non bread. A single warm lamp hanging above the table lights them, the rest of the dim choyxona fades into blue-grey darkness with soft blurred carved wooden pillars and empty tapchan, no other people. "
  + Y1 + " " + Y2 + " " + STYLE + " " + K1 + " " + K2 + " Same choyxona, table and lamp as in the attached choyxona images. " + END),
 ("6b", "Piyola", "0:40–0:46", "Ishingni ko'rsatmasang, u tomoshabin. Mijoz emas.", ["ref_y2", "joy_choyxona"],
  "Close-up, vertical 9:16, slightly low angle. THE SECOND GUY sits at the low wooden choyxona table and slowly puts his piyola tea bowl down on the table, looking ahead at someone off-camera with a calm heavy look, no smile; a thin wisp of steam rises from the tea below his chin and never covers his face; in the foreground, out of focus, the white teapot with a blue cotton-boll pattern. A single warm hanging lamp lights his face from the side, the background is the dark blurred choyxona in blue-grey shadow. "
  + Y2 + " " + STYLE + " " + K2 + " " + END),
 (7, "Non — «Ko'rsat»", "0:46–0:52", "Mahsulotni ko'rsat.", [],
  "Close-up, vertical 9:16. Inside a dark traditional Uzbek bakery at night, the hands of a baker in rolled-up white sleeves pull a freshly baked round Uzbek non bread out of the glowing mouth of a clay tandir oven; the bread is golden-brown with a stamped pattern in the middle and sesame seeds, a little steam rises from it. The orange glow of the tandir is the only warm light and makes the bread the brightest thing in the frame, everything around falls into deep blue-grey shadow. Only the hands and forearms are visible, no face. "
  + "Cinematic film still, vertical 9:16, shot on 35mm, low-key lighting, cold blue-grey color grade with deep blacks, the product is the only warm bright element, light haze, fine film grain, realistic texture. Leave the lower third of the frame darker and simple for on-screen text. " + END),
 (8, "Tikuvchi — «Ayt»", "0:52–0:58", "Foydasini ayt.", [],
  "Close-up, vertical 9:16. In a dark small tailor's workshop at night, the hands of a tailor, a yellow measuring tape hanging over one wrist, pull a finished seam of a dark blue wool jacket tight between both hands to show how strong and even the stitching is; an old black sewing machine with its small warm lamp is beside the hands. The little sewing-machine lamp is the only warm light and makes the fabric and the neat stitches the brightest thing in the frame, everything around falls into deep blue-grey shadow. Only the hands and forearms are visible, no face. "
  + "Cinematic film still, vertical 9:16, shot on 35mm, low-key lighting, cold blue-grey color grade with deep blacks, the product is the only warm bright element, light haze, fine film grain, realistic texture. Leave the lower third of the frame darker and simple for on-screen text. " + END),
 (9, "Gulchi — «Isbotla»", "0:58–1:05", "Boshqalardan farqini isbotla. Ko'rish ishonchga aylanadi. Ishonch buyurtmaga.", [],
  "Close-up, vertical 9:16. In a dark small flower shop at night, across a wooden counter, the hands of a florist hand over a fresh bouquet of deep red roses and white chrysanthemums tied with a simple ribbon into the open hands of a customer; tiny water drops shine on the petals. A single warm lamp above the counter is the only warm light and makes the bouquet the brightest thing in the frame, buckets of flowers behind fade into deep blue-grey shadow. Only hands and forearms are visible, no faces. "
  + "Cinematic film still, vertical 9:16, shot on 35mm, low-key lighting, cold blue-grey color grade with deep blacks, the product is the only warm bright element, light haze, fine film grain, realistic texture. Leave the lower third of the frame darker and simple for on-screen text. " + END),
 (10, "Bitta surat", "1:05–1:14", "Operator shart emas. Katta kamera shart emas. Bitta surat. To'g'ri gap. Tamom.", ["ref_y1", "joy_garaj"],
  "Medium close-up, vertical 9:16, from slightly behind and to the side of THE FIRST GUY. In the dark old garage at night he holds his smartphone with both hands and takes a photo of a fresh round golden non bread lying on an old wooden crate right under the single bare bulb; his face in three-quarter view is focused, with a small satisfied half-smile; the phone screen faces the camera and shows the same bread as a sharp, bright, simple photo with no text and no icons. Warm light from the bulb on the bread and on his hair, deep blue shadows around, the rusty shutter door behind fades into black. "
  + Y1 + " " + STYLE + " " + K1 + " " + END),
 (11, "«Ishingni ko'rsat»", "1:15–1:19", "Shovqin qilma. Ishingni ko'rsat.", ["ref_y1", "ref_y2", "joy_garaj"],
  "Medium shot, vertical 9:16, eye level. THE FIRST GUY and THE SECOND GUY stand side by side in the dark old garage at night under the single bare bulb and look straight into the camera, calm and confident, no smile; THE SECOND GUY stands a little in front with his hands in his coat pockets, THE FIRST GUY stands at his shoulder holding his smartphone down by his side with the screen dark. Warm light from the bulb above on their hair and shoulders, cold blue shadows, the rusty metal shutter door and stacked tires behind them fade into black. "
  + Y1 + " " + Y2 + " Black trousers, black boots for THE SECOND GUY. " + STYLE + " " + K1 + " " + K2 + " Leave the lower third of the frame darker and simple for on-screen text. " + END),
]
NAMES = {"ref_y1": "1-yigit (belgisiz)", "ref_y2": "2-yigit", "ref_qiz": "Ofitsiant qiz", "joy_garaj": "Garaj", "joy_choyxona": "Choyxona",
         "05b_ofitsiant": "5b-sahna (stol)"}
# Tayyor rasmlar: sahna -> img/ fayli (sahifada «Tayyor» belgisi bilan ko'rsatiladi).
DONE = {1: "01_telefon", 2: "02_yigit2", 3: "03_tushiradi", 4: "04_shovqin", 5: "05_trend", "6a": "06a_suhbat", "6b": "06b_piyola"}
if __name__ == "__main__":
    for r in list(NAMES) + list(DONE.values()):
        im = Image.open(f"video/korish/img/{r}.jpg"); im.thumbnail((360, 640)); im.save(f"video/korish/web/{r}.webp", quality=80)
    e = html.escape; cards = []
    for n, name, t, voice, refs, p in S:
        thumbs = "".join(f'<figure><img src="web/{r}.webp" alt="{e(NAMES[r])}"><figcaption>{e(NAMES[r])}</figcaption></figure>' for r in refs) \
                 or '<p class="none">Namuna kerak emas</p>'
        done = f'<p class="lbl">✅ Tayyor rasm</p><div class="refs"><figure><img src="web/{DONE[n]}.webp" alt="tayyor"></figure></div>' if n in DONE else ""
        cards.append(f'''<article class="card" id="s{n}">
<header><span class="num">{n}</span><h2>{e(name)}</h2><span class="dur">9:16 · rasm</span><span class="dur">{t}</span></header>
<p class="voice"><span class="lbl">Ovoz</span>{e(voice)}</p>
<p class="lbl">Shu rasmlarni biriktiring</p><div class="refs">{thumbs}</div>
{done}<p class="lbl">Rasm prompti (ChatGPT, 9:16)</p>
<pre id="p{n}">{e(p)}</pre>
<button type="button" class="copy" data-t="p{n}">Nusxa olish</button>
</article>''')
    head = open("video/robot/page_head.html").read()
    head = head.replace("<title>Robot bilan choy sahnalari</title>", "<title>Ko'rish bor sahnalari</title>")
    head = head.replace("«Robot bilan bir piyola choy» sahnalari", "«Ko'rish bor. Pul yo'q.» — sahna rasmlari")
    head = head.replace(head[head.index('<p class="intro">'):head.index('</p>', head.index('<p class="intro">')) + 4],
        '<p class="intro">Har bir sahna: biriktiriladigan namuna rasmlar (rasmni bosib saqlang), ovoz qatori va rasm prompti. ChatGPT\'da formatni 9:16 qiling, namunalarni biriktiring, «Nusxa olish» bilan promptni qo\'ying.</p>')
    head = head.replace("</style>", ".refs{display:flex;gap:10px;flex-wrap:wrap}.refs figure{margin:0;width:120px}.refs img{width:120px;border-radius:6px;display:block}"
                        ".refs figcaption{font-size:12px;color:var(--muted);margin-top:4px}.none{color:var(--muted);margin:0}</style>")
    open("video/korish/rasmlar.html", "w").write(head + "\n".join(cards) + open("video/robot/page_tail.html").read())
