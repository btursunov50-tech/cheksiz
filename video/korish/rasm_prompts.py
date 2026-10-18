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
]
NAMES = {"ref_y1": "1-yigit (belgisiz)", "ref_y2": "2-yigit", "ref_qiz": "Ofitsiant qiz", "joy_garaj": "Garaj", "joy_choyxona": "Choyxona"}
if __name__ == "__main__":
    for r in NAMES:
        im = Image.open(f"video/korish/img/{r}.jpg"); im.thumbnail((360, 640)); im.save(f"video/korish/web/{r}.webp", quality=80)
    e = html.escape; cards = []
    for n, name, t, voice, refs, p in S:
        thumbs = "".join(f'<figure><img src="web/{r}.webp" alt="{e(NAMES[r])}"><figcaption>{e(NAMES[r])}</figcaption></figure>' for r in refs) \
                 or '<p class="none">Namuna kerak emas</p>'
        cards.append(f'''<article class="card" id="s{n}">
<header><span class="num">{n}</span><h2>{e(name)}</h2><span class="dur">9:16 · rasm</span><span class="dur">{t}</span></header>
<p class="voice"><span class="lbl">Ovoz</span>{e(voice)}</p>
<p class="lbl">Shu rasmlarni biriktiring</p><div class="refs">{thumbs}</div>
<p class="lbl">Rasm prompti (ChatGPT, 9:16)</p>
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
