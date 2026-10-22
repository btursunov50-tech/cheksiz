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
e = html.escape; cards = []
for n, name, t, note, p in S:
    full = p + " " + END
    cards.append(f'''<article class="card" id="s{n}">
<header><span class="num">{n}</span><h2>{e(name)}</h2><span class="dur">9:16 (tik), 8 s</span><span class="dur">{t}</span></header>
<div class="txt"><p class="voice"><span class="lbl">Klipdagi joyi</span>{e(note)}</p>
<p class="lbl vid">🎬 Veo prompti — 9:16 (tik), 8 s</p><pre id="v{n}">{e(full)}</pre>
<button type="button" class="copy" data-t="v{n}">Nusxa olish</button></div>
</article>''')
head = open("video/robot/page_head.html").read()
head = head.replace("<title>Robot bilan choy sahnalari</title>", "<title>Birlik klipi Veo</title>")
head = head.replace("«Robot bilan bir piyola choy» sahnalari", "«Birlik» klipi — Veo promptlari")
i = head.index('<p class="intro">'); j = head.index('</p>', i) + 4
head = head[:i] + ('<p class="intro">11 ta klip, hammasi matndan video (rasm kerak emas). Veo\'da formatni 9:16, uzunlikni 8 s qiling va «Nusxa olish» bilan promptni qo\'ying. '
                   'Yozuvlar, sarlavha, ismlar va qum effektini o\'zim qo\'shaman. 8–10 portretlar bir xil uslubda: odam qimirlamay turadi, faqat nafas oladi va kameraga qaraydi.</p>') + head[j:]
head = head.replace("</style>", ".vid{color:var(--sun)}</style>")
open("video/qahramon/veo.html", "w").write(head + "\n".join(cards) + open("video/robot/page_tail.html").read())
print(len(S))
