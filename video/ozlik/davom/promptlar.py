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
 ("2", "k2", "Juda sekin push-in uning yuziga (yon tomondan)",
  "«Ko'zgularga boqmay turib… Nafsini yenggan inson — eng buyuk g'olib» — u qoya ustida o'ngga, vodiyga qarab turibdi. Uning oldida, o'ng tomonda toshlar orasidan katta ko'zgu ko'tariladi; aksi — mag'rur, qizil neon chiziqli boy odam (zarbof to'n). U qo'lini ko'ksiga qo'yadi, ko'ksida yashil nur yonadi; qizil aks shishadek yorilib, qizil kulga aylanib uchib ketadi; ko'zguda xotirjam o'zi qoladi.",
  "Very slow push-in from the side toward the man's face; he stays standing on the rocks in profile, facing right toward the valley, exactly as in the image. Slowly, on the right side in front of him, a tall old standing mirror in a carved stone frame rises up out of the rocks, its glass turned toward him, so we see his reflection at an angle. In the mirror his reflection is a proud, cold rich version of himself in a heavy gold-embroidered robe, its outline traced by a thin neon red glowing line, with a cold arrogant smirk. The real man looks straight into the mirror, calm and brave, and slowly places his hand flat on his chest; a soft neon green light starts to glow under his hand. The red reflection cracks like glass and crumbles into red ash that blows away to the right in the wind; now the mirror shows only his own calm face and the green light on his chest. He takes one deep breath and his shoulders relax. The mirror never shows any text and the man never walks away."),
]
def prompt(n, img, cam, what, p):
    return f"Horizontal 16:9 video, 8 seconds, from the attached image (this image is the first frame). {p} {STYLE} {KEEP} {SIL}\n{VEO_NEG}"
cards = [dict(num=n, title=f"{n}-davom — video, 16:9 (yotiq), 8 s", shot=f"web/{img}.webp", shotcap=f"davom/{img}.jpg — shuni yuklang (JPG chatda)",
              whatlbl="Nima bo'ladi", what=what, cam=cam, prompt=prompt(n, img, cam, what, p)) for n, img, cam, what, p in S]
page("O'zligim davomi", "«O'zligim» <em>davomi va oxiri</em>",
     "GPT bilan qilingan kliplarning oxirgi kadrlaridan davom klipi. Qolgan sahna: 2 — ko'zgu (k2 kadridan). Google Vids yoki Veo'da Format 16:9, chapdagi kadrni yuklang (asl fayllar chatda), «Nusxa olish» bilan promptni qo'ying.",
     cards, os.path.join(D, "sahnalar.html"))
print(len(S))
