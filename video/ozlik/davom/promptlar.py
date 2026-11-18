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
IMG7 = ("Horizontal 16:9 image. Use the two attached images as references: keep exactly the drawing style, colours and landscape of the first image "
        "(detailed engraved ink etching on warm sepia-gold paper with fine hatching, swirling dark ink sky, a big glowing setting sun with a lone tree on the hill on the right, "
        "a winding bright neon green glowing path through the hills), and keep the same little boy as in both images (about 7 years old, short messy brown hair, "
        "simple brown rough-cloth short-sleeved tunic with a rope belt, brown trousers, small leather shoes). "
        "Now the boy is FAR AWAY on the green path, very small in the frame, just in front of the sun, walking TOWARD the viewer: we see his front, his face turned to us, "
        "one foot stepping forward. The green path starts at the bottom of the frame near the viewer and winds back to him and the sun. Wide shot, the camera low near the path. "
        "Only 2–3 colours: sepia gold, dark ink brown, neon green. No ring or circle of light above or behind his head, no glow outline around him, no text, no letters, no watermark.")
VID7 = ("Slow steady dolly back (the camera moves backward at the boy's walking speed, low near the path). The small boy walks along the glowing green path from the sun "
        "TOWARD the camera, step by step, arms swinging; he always walks forward to us and never turns back or walks away. As he comes closer he grows bigger in the frame "
        "until he is a medium shot from the knees up. He looks around with curious, searching eyes (left, right, then up at the sky), as if looking for something he lost. "
        "Tiny green sparkles rise from the path where he steps; the ink lines of the swirling sky slowly turn; the sun stays behind him.")
def prompt(n, img, cam, what, p):
    return f"Horizontal 16:9 video, 8 seconds, from the attached image (this image is the first frame). {p} {STYLE} {KEEP} {SIL}\n{VEO_NEG}"
cards0 = [dict(num=n, title=f"{n}-davom — video, 16:9 (yotiq), 8 s", shot=f"web/{img}.webp", shotcap=f"davom/{img}.jpg — shuni yuklang (JPG chatda)",
              whatlbl="Nima bo'ladi", what=what, cam=cam, prompt=prompt(n, img, cam, what, p)) for n, img, cam, what, p in S]
cards = [dict(num="7a", title="7a — rasm (ChatGPT), 16:9 (yotiq): bola quyosh tomondan keladi", refs=[("web/ref_manzara.webp", "ref_manzara.jpg — 1-rasm (uslub, manzara)"), ("web/ref_bola.webp", "ref_bola.jpg — 2-rasm (bolaning yuzi)")],
              whatlbl="Nima bo'ladi", what="Klip boshi: kichkina bola uzoqda, quyosh oldida, yashil yo'lda turibdi, yuzi bizga qaragan — kameraga qarab yura boshlaydi. ChatGPT'ga ikkala rasmni biriktiring.", prompt=IMG7),
         dict(num="7b", title="7b — video, 16:9 (yotiq), 8 s: bola kameraga qarab yuradi", shot=None,
              whatlbl="Nima bo'ladi", what="0:00–0:08 kirish. 7a rasmini yuklang: bola yashil yo'ldan quyosh tomondan bizga qarab yuradi, kattalashib boradi, atrofga «nimanidir izlayotgandek» qaraydi.",
              cam="Sekin dolly back — kamera bola yurishi tezligida orqaga yuradi", prompt=f"Horizontal 16:9 video, 8 seconds, from the attached image (this image is the first frame). {VID7} {STYLE} " + KEEP.replace("curly or grey hair, beard, the same brown embroidered robe", "short messy brown hair, the same brown tunic with a rope belt") + f" {SIL}\n{VEO_NEG}")] + [c for c in cards0 if c["num"] == "3"][:0]
page("O'zligim davomi", "«O'zligim» <em>davomi va oxiri</em>",
     "GPT bilan qilingan kliplarning oxirgi kadrlaridan davom klipi. Yangi: 7a (rasm) va 7b (video) — klip boshida bola quyosh tomondan kameraga qarab keladi. Sham (g26) va ko'zgu (g24) bajarildi. Google Vids yoki Veo'da Format 16:9, chapdagi kadrni yuklang (asl fayllar chatda), «Nusxa olish» bilan promptni qo'ying.",
     cards, os.path.join(D, "sahnalar.html"))
print(len(S))
