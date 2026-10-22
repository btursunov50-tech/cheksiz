# «Birlik» klipi — Veo uchun 11 ta matn→video prompti (9:16, 8 s), sahifa: veo.html
import html
END = ("Vertical 9:16, 8 seconds, cinematic photorealistic film look, warm golden light with deep shadows, gentle film grain, "
       "smooth natural motion that fills all 8 seconds. No text, no letters, no captions, no logos, no watermark. No music, ambient sound only.")
UZ_FLAG = ("the national flag of Uzbekistan exactly: three horizontal stripes from top to bottom light blue, white, green, separated by two thin red lines, "
           "and in the top left of the blue stripe a white crescent moon and twelve small white stars")
IBN = "IBN SINA: a wise Central Asian physician about 45 years old, dark neat beard, white turban, dark blue robe with a simple gold border, calm kind eyes"
BER = "AL-BIRUNI: a Central Asian scholar about 55 years old, grey beard, light grey turban, brown wool robe, thoughtful look"
ULU = "ULUGH BEG: a Timurid prince-astronomer about 40 years old, short black beard, white turban with a small gold jewel, rich green and gold silk robe"
S = [
 ("1", "Tog'lar ortidan quyosh", "0:00–0:10", "Kirish. Oxiriga sarlavhani o'zim yozaman.",
  "Slow crane up from a dark valley to the mountain ridge, ending on a wide view of the sun rising. Dawn over the snowy Tian Shan mountains of Uzbekistan: the first rays of the sun break over the peaks, golden light floods the valleys, morning mist flows slowly between the hills, a lone eagle glides across the sky."),
 ("2", "Ulug'bek rasadxonasi", "0:30–0:34", "«Birlashib odimlasak...»",
  "Slow push-in from the entrance toward the astronomer, ending in a medium shot. Night inside the 15th-century Ulugh Beg observatory in Samarkand: a giant curved marble meridian arc goes down into the ground, oil lamps glow, through the open roof a sky full of bright stars turns slowly. " + ULU + " stands by the arc and measures a star with a brass instrument, then writes in a big book."),
 ("3", "Ibn Sino kitob ustida", "0:34–0:37", "Tez kadr (3 s ishlatiladi).",
  "Rack focus: the shot starts focused on the flame of an oil lamp in the foreground, then the focus slowly shifts to the scholar's face. Night in a medieval Bukhara study full of manuscripts and medicine jars. " + IBN + " writes in a thick handwritten book with a reed pen, stops and looks up thoughtfully. The pages show only blurred unreadable lines."),
 ("4", "Beruniy astrolab bilan", "0:37–0:39", "Tez kadr (2 s ishlatiladi).",
  "Slow 90-degree orbit around the scholar, low angle, ending with the setting sun behind him. Evening on a rocky mountain top above a valley: " + BER + " holds up a large brass astrolabe and looks through it at the horizon, the wind moves his robe, the sky is orange and purple."),
 ("5", "Birlik: qo'llar ustma-ust", "0:54–0:58", "«Bir tan-u bir jon...» oldidan.",
  "Locked-off top-down camera, then a slow gentle push-in at the end. Hands of different people are placed one on top of another in the center of the frame: an old man's wrinkled hand, a woman's hand with a thin bracelet, a young athlete's strong hand with tape on the fingers, a soldier's hand in a fingerless glove, a child's small hand on top. Warm golden sunlight from the side, dark blurred background."),
 ("6", "Registon, mushaklar", "1:27–1:33", "Bayram kechasi.",
  "Slow crane up from the crowd to a wide view of the whole square. Night at the Registan square in Samarkand: the three illuminated madrasas glow gold and turquoise, colourful fireworks burst in the sky above the domes, a large crowd of happy people in silhouette raise their hands, some wave " + UZ_FLAG + "."),
 ("7", "Yoshlar cho'qqida bayroq ko'taradi", "2:00–2:05", "Kelajak.",
  "Drone shot: a slow orbit around the summit, ending with the climbers in the center against the sunrise. A young man and a young woman in modern mountain jackets reach a snowy mountain summit at sunrise and raise together " + UZ_FLAG + " on a pole; the flag unfurls in the strong wind, clouds below them."),
 ("8", "Ibn Sino portreti (qumga aylanadi)", "2:11–2:14", "Yakundagi tarix qahramonlari: 3 s turadi, qolganini o'zim qilaman.",
  "Locked-off static camera with a very slow push-in, full figure, centered, the person stands still facing the camera. " + IBN + " stands in the arched doorway of a medieval Bukhara library, holding a closed book to his chest; he breathes calmly, blinks and slowly lifts his eyes to the camera; a light wind moves his robe. Soft golden light from the side, dark background."),
 ("9", "Beruniy portreti (qumga aylanadi)", "2:14–2:17", "Xuddi 8-sahna uslubida.",
  "Locked-off static camera with a very slow push-in, full figure, centered, the person stands still facing the camera. " + BER + " stands on a rocky hilltop at dusk holding a brass astrolabe at his side; he breathes calmly, blinks and slowly lifts his eyes to the camera; the wind moves his robe. Warm sunset light from the side."),
 ("10", "Ulug'bek portreti (qumga aylanadi)", "2:17–2:20", "Xuddi 8-sahna uslubida.",
  "Locked-off static camera with a very slow push-in, full figure, centered, the person stands still facing the camera. " + ULU + " stands in front of the turquoise tiled portal of a Samarkand madrasa at night under a starry sky; he breathes calmly, blinks and slowly lifts his eyes to the camera; a light wind moves his robe. Soft golden lamp light."),
 ("11", "Bayroq (yakun)", "2:27–2:35", "Ustiga «O'zbekning jasur o'g'li — hech qachon yengilmas!» yozuvini o'zim qo'yaman.",
  "Slow push-in toward the flag, ending with the flag filling most of the frame, slight slow motion. " + UZ_FLAG[0].upper() + UZ_FLAG[1:] + " waves proudly on a tall flagpole in the strong wind against a golden sunrise sky, the domes of the Registan are silhouetted far below. The flag must be exactly correct: light blue, white and green stripes, thin red lines, crescent and twelve stars."),
]
KEEP = "Keep every person exactly as in the image for the whole clip: same face, beard, turban and clothes."
STILL = "He keeps standing still on the same spot for the whole clip, does not walk and does not leave the frame, full figure always visible."
I2V = {  # rasm tayyor bo'lgan sahnalar: rasm -> video prompti
 "6": ("s06_registon", "Slow crane up from the crowd over the waving flags toward the madrasas, ending wide on the fireworks above the domes. Fireworks keep bursting in many colours and sparkle down slowly, the crowd cheers and waves the flags of Uzbekistan in the wind, the madrasa lights glow. Keep the flags exactly as in the image: light blue, white and green stripes with thin red lines, white crescent and twelve stars."),
 "7": ("s07_yoshlar", "Slow drone orbit around the summit from left to right, ending with the two climbers centered against the rising sun. The young man and woman hold the flagpole together, the flag of Uzbekistan unfurls and waves strongly in the wind, they smile and look up at it, clouds drift slowly below. Keep the flag exactly as in the image. Keep both people exactly as in the image for the whole clip."),
 "8": ("s08_ibnsino_portret", "Locked-off static camera with a very slow push-in toward him, full figure always in frame. Ibn Sina stands calmly in the doorway of the library holding the book to his chest; he breathes slowly, blinks, and lifts his eyes to the camera with a calm proud look; the lamp flames flicker softly behind him. " + STILL + " " + "Keep IBN SINA exactly as in the image for the whole clip: same face, dark beard, white turban, dark blue robe."),
 "10": ("s10_ulugbek_portret", "Locked-off static camera with a very slow push-in toward him, full figure always in frame. Ulugh Beg stands calmly in front of the madrasa under the starry night sky, hands folded; he breathes slowly, blinks and lifts his eyes to the camera with a calm proud look; the lanterns flicker softly, the stars twinkle. " + STILL + " " + "Keep ULUGH BEG exactly as in the image for the whole clip: same face, short black beard, turban with the jewel, green and gold robe."),
 "11": ("s11_bayroq", "Slow push-in toward the flag with slight slow motion, ending with the flag filling most of the frame. The flag of Uzbekistan waves proudly and smoothly in the strong wind, the sun sets slowly behind the city, the Registan lights glow below, warm clouds drift. Keep the flag exactly as in the image for the whole clip: light blue, white and green stripes with thin red lines, white crescent and twelve white stars."),
 "9": ("s09_beruniy_portret", "Locked-off static camera with a very slow push-in toward him, full figure always in frame. Al-Biruni stands calmly on the hilltop holding the astrolabe; he breathes slowly, blinks and looks into the camera with a wise calm look; the wind gently moves his robe and scarf, the sun sets slowly behind the mountains. " + STILL + " " + "Keep AL-BIRUNI exactly as in the image for the whole clip: same face, grey beard, grey turban, brown robe."),
}
from PIL import Image
e = html.escape; cards = []
for n, name, t, note, p in S:
    img = ""
    if n in I2V:
        f, p = I2V[n]
        im = Image.open(f"video/qahramon/img/{f}.jpg"); im.thumbnail((420, 746)); im.save(f"video/qahramon/web/{f}.webp", quality=80)
        img = f'<div class="media"><img src="web/{f}.webp" alt="{e(name)}"></div><p class="lbl">✅ Rasm tayyor — Veo\'ga shu rasmni yuklang</p>'
    else:
        img = '<p class="wait">⏳ Rasm hali yo\'q (rasm prompti chatda). Rasm kelgach, prompt «rasm → video» ga almashadi.</p>'
    full = p + " " + END
    cards.append(f'''<article class="card" id="s{n}">
<header><span class="num">{n}</span><h2>{e(name)}</h2><span class="dur">9:16 (tik), 8 s</span><span class="dur">{t}</span></header>
{img}<div class="txt"><p class="voice"><span class="lbl">Klipdagi joyi</span>{e(note)}</p>
<p class="lbl vid">🎬 Veo prompti — 9:16 (tik), 8 s</p><pre id="v{n}">{e(full)}</pre>
<button type="button" class="copy" data-t="v{n}">Nusxa olish</button></div>
</article>''')
head = open("video/robot/page_head.html").read()
head = head.replace("<title>Robot bilan choy sahnalari</title>", "<title>Birlik klipi Veo</title>")
head = head.replace("«Robot bilan bir piyola choy» sahnalari", "«Birlik» klipi — Veo promptlari")
i = head.index('<p class="intro">'); j = head.index('</p>', i) + 4
head = head[:i] + ('<p class="intro">Avval ChatGPT\'da rasm, keyin shu rasmdan Veo\'da video. Rasmi tayyor sahnalarda rasm va «rasm → video» prompti turibdi. Veo\'da formatni 9:16, uzunlikni 8 s qiling va «Nusxa olish» bilan promptni qo\'ying. '
                   'Yozuvlar, sarlavha, ismlar va qum effektini o\'zim qo\'shaman. 8–10 portretlar bir xil uslubda: odam qimirlamay turadi, faqat nafas oladi va kameraga qaraydi.</p>') + head[j:]
head = head.replace("</style>", ".vid{color:var(--sun)}.wait{margin:0;padding:10px 12px;border:1px dashed var(--sun);border-radius:6px;color:var(--sun)}</style>")
open("video/qahramon/veo.html", "w").write(head + "\n".join(cards) + open("video/robot/page_tail.html").read())
print(len(S))
