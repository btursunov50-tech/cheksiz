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
IMG7 = ("Horizontal 16:9 image. Use the attached image as the reference: keep exactly its drawing style, colours and landscape (detailed engraved ink etching on warm sepia-gold paper "
        "with fine hatching, swirling dark ink sky, a big glowing setting sun with a lone tree on the hill on the right, a plain winding sepia dirt path through the hills) "
        "and the same little boy (about 7 years old, short messy brown hair, simple brown rough-cloth tunic, brown trousers, small leather shoes). "
        "Remove the boy from the front: now he is FAR AWAY on the plain dirt path, very small in the frame, just in front of the sun, walking TOWARD the viewer: "
        "we see his front, his face turned to us, one foot stepping forward. The path is plain sepia ink with no green colour and no glow anywhere. "
        "The path starts at the bottom left of the frame near the viewer and winds back to him and the sun. Wide shot, the camera low near the path. "
        "Only 2 colours: sepia gold and dark ink brown. No ring or circle of light above or behind his head, no glow outline around him, no text, no letters, no watermark.")
VID7 = ("Slow steady push-in toward the path while the small boy walks along the plain sepia dirt path from the sun TOWARD the camera, step by step, arms swinging; "
        "he always walks forward to us and never turns back or walks away. As he comes closer he grows bigger in the frame. In the last two seconds he reaches the camera "
        "on the LEFT side of the frame, slows down and stops in a close-up from the chest up, his body on the left third of the frame, then lowers his head and looks down "
        "sadly with his eyes almost closed, exactly like the second attached reference image; behind him on the right the empty winding path, the hills and the sun with the lone tree. "
        "The path stays plain sepia with no green colour and no glow; the ink lines of the swirling sky slowly turn.")
def prompt(n, img, cam, what, p):
    return f"Horizontal 16:9 video, 8 seconds, from the attached image (this image is the first frame). {p} {STYLE} {KEEP} {SIL}\n{VEO_NEG}"
cards0 = [dict(num=n, title=f"{n}-davom — video, 16:9 (yotiq), 8 s", shot=f"web/{img}.webp", shotcap=f"davom/{img}.jpg — shuni yuklang (JPG chatda)",
              whatlbl="Nima bo'ladi", what=what, cam=cam, prompt=prompt(n, img, cam, what, p)) for n, img, cam, what, p in S]
cards = [dict(num="7a", title="7a — rasm (ChatGPT), 16:9 (yotiq): bola quyosh tomondan keladi", refs=[("web/ref_bola.webp", "ref_bola.jpg — biriktiring (uslub, manzara, bola)")],
              whatlbl="Nima bo'ladi", what="Klip boshi: kichkina bola uzoqda, quyosh oldida, yashil rangsiz oddiy yo'lda, yuzi bizga qaragan — kameraga qarab yura boshlaydi. ChatGPT'ga ref_bola.jpg ni biriktiring.", prompt=IMG7),
         dict(num="7b", title="7b — video, 16:9 (yotiq), 8 s: bola kameraga qarab yuradi", shot=None, refs=[("web/ref_oxiri.webp", "ref_oxiri.jpg — 2-rasm: klip shu kadr bilan tugaydi (keyingi klip g04 boshi)")],
              whatlbl="Nima bo'ladi", what="0:00–0:08 kirish. 1-rasm: 7a rasmi (boshlang'ich kadr), 2-rasm: ref_oxiri.jpg. Bola yashil rangsiz yo'ldan quyosh tomondan bizga qarab yuradi, kattalashib, kadrning chap tomonida to'xtaydi va boshini egib pastga qaraydi — keyingi klip (g04) aynan shu kadrdan boshlanadi.",
              cam="Sekin push-in, oxirida bola yaqin planda (close-up) chapda to'xtaydi", prompt=f"Horizontal 16:9 video, 8 seconds. The first attached image is the first frame; the second attached image shows how the last frame must look. {VID7} {STYLE} " + KEEP.replace("curly or grey hair, beard, the same brown embroidered robe", "short messy brown hair, the same brown tunic with a rope belt") + f" {SIL}\n{VEO_NEG}")] + [c for c in cards0 if c["num"] == "3"][:0]
page("O'zligim davomi", "«O'zligim» <em>davomi va oxiri</em>",
     "GPT bilan qilingan kliplarning oxirgi kadrlaridan davom klipi. Yangi: 7a (rasm) va 7b (video) — klip boshida bola quyosh tomondan kameraga qarab keladi. Sham (g26) va ko'zgu (g24) bajarildi. Google Vids yoki Veo'da Format 16:9, chapdagi kadrni yuklang (asl fayllar chatda), «Nusxa olish» bilan promptni qo'ying.",
     cards, os.path.join(D, "sahnalar.html"))
print(len(S))
