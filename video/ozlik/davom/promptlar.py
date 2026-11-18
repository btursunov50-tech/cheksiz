# «O'zligim» davomi va oxiri — GPT kliplarining oxirgi kadrlaridan (k1–k4) Veo promptlari, 16:9, 8 s → sahnalar.html
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", ".claude", "skills", "promptlar")); from sahifa import page, VEO_NEG
STYLE = ("Keep exactly the same look as the attached image for the whole clip: a detailed engraved ink etching on warm sepia-gold paper with fine cross-hatching, dramatic swirling sky, "
         "the glowing neon green path; it never turns into a photo, 3D render or a different style, and the camera never cuts to a new scene. "
         "There is never any ring or circle of light above or behind anyone's head.")
KEEP = "Keep every person exactly as in the image: the same face, curly or grey hair, beard, the same brown embroidered robe; faces never change into other people."
SIL = "Silent video: no audio, no voices, no music; nobody speaks."
S = [
 ("3", "k3", "Sekin push-in bobo yelkasi ortidan, oxirida sekin tilt up (kamera osmonga qaraydi)",
  "«Bir sham yonib so'nar ekan, nur qolur xotirada» — bobo o'sha qoyada orqasi bilan turibdi. Uning oldidagi tekis toshda katta oq sham o'zi paydo bo'lib, qizil neon olov bilan yonadi (shamning chetlari ham ingichka qizil neon). Bobo unga jim qaraydi. Keyin olov shamdan uzilib, osmonga uchib ketadi; sham esa qizil uchqunlarga aylanib, yo'qoladi. Toshda hech narsa qolmaydi.",
  "Slow push-in over the old man's shoulder; he stays standing on the same rock with his back to us, leaning on his wooden stick, exactly as in the image, and never walks away. On the flat rock right in front of him, slightly to the right, a large tall white candle slowly appears by itself, as big as his knee, standing alone on the stone. Its flame lights up as a bright neon red flame, and a thin neon red glowing line traces the edges of the candle; soft red light falls on the rocks and on the hem of his robe. The old man looks down at the candle quietly and slowly bows his head a little. Then the red flame lifts off the wick, floats up and flies higher and higher into the sunset sky, leaving a thin trail of red sparks; the camera tilts up slowly to follow it. At the same time the candle itself breaks into tiny red glowing sparks from top to bottom and disappears completely; the rock in front of him stays empty. The only neon colours are this red and the green path; no other glow."),
]
def prompt(n, img, cam, what, p):
    return f"Horizontal 16:9 video, 8 seconds, from the attached image (this image is the first frame). {p} {STYLE} {KEEP} {SIL}\n{VEO_NEG}"
cards = [dict(num=n, title=f"{n}-davom — video, 16:9 (yotiq), 8 s", shot=f"web/{img}.webp", shotcap=f"davom/{img}.jpg — shuni yuklang (JPG chatda)",
              whatlbl="Nima bo'ladi", what=what, cam=cam, prompt=prompt(n, img, cam, what, p)) for n, img, cam, what, p in S]
page("O'zligim davomi", "«O'zligim» <em>davomi va oxiri</em>",
     "GPT bilan qilingan kliplarning oxirgi kadrlaridan davom klipi. Qolgan sahna: 3 — yangi sham (k3 kadridan). 2 — ko'zgu bajarildi (g24). Google Vids yoki Veo'da Format 16:9, chapdagi kadrni yuklang (asl fayllar chatda), «Nusxa olish» bilan promptni qo'ying.",
     cards, os.path.join(D, "sahnalar.html"))
print(len(S))
