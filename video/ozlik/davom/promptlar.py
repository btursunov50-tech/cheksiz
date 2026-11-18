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
 ("1", "k1", "Sekin kuzatib boruvchi kamera (tracking) orqasidan",
  "«Men muhabbat deb o'yladim, nafsim ekan istagim… Aybni dunyodan izlab…» — u Zeboni qoldirib ketadi; oyog'i ostidagi yashil yo'l oltin tangalarga aylanadi, to'ni qimmat zarbof bo'ladi, soyasi qizil neon bilan kattalashadi. Zebo ortda xiralashadi.",
  "Slow tracking shot following the man from behind as he keeps walking away along the path, never turning back. With every step the glowing green path under his feet turns into a road of shiny gold coins; his plain brown robe slowly becomes a heavy gold-embroidered rich robe with a fur collar; his shadow on the ground grows longer and darker with a soft neon red glow inside it. On the left the girl stays standing where she is, crying, and slowly fades into the sepia background. Gold coins clink and roll under his boots."),
 ("2", "k2", "Juda sekin push-in uning yuziga",
  "«Ko'zgularga boqmay turib… Nafsini yenggan inson — eng buyuk g'olib» — oldida tosh orasidan katta ko'zgu ko'tariladi; aksi — mag'rur, qizil neon soyali boy odam; u qo'lini ko'ksiga qo'yadi, qizil aks yorilib kulga aylanadi, ko'zguda xotirjam o'zi qoladi, ko'ksida yashil nur.",
  "Very slow push-in toward the man's face. In front of him a tall old standing mirror in a carved stone frame rises slowly out of the rocks. In the mirror his reflection is a proud, cold rich version of himself in a gold robe, outlined with a neon red glow, smirking. The man looks straight into the mirror, calm and brave, and places his right hand flat on his chest; a soft neon green light starts to glow under his hand. The red reflection cracks like glass and crumbles into red ash that blows away in the wind; now the mirror shows only his own calm face with the green light on his chest. He takes one deep breath."),
 ("3", "k3", "Sekin aylanib o'tish (orbit) chap tomondan oldiga",
  "«Bir sham yonib so'nar ekan, nur qolur xotirada» — chol kaftida kichik sham yoqadi; olov biroz yonib, sekin o'chadi; u bosib o'tgan izlarda nur nuqtalari qoladi, u esa yo'l bo'ylab sekin ketadi.",
  "Slow orbit from behind the old man around to his side. He raises one hand holding a small lit candle with a warm golden flame; the flame burns quietly for a moment, then flickers and slowly goes out, leaving a thin curl of smoke. He lowers the candle with a peaceful smile and starts walking slowly down toward the green path, leaning on his stick; behind him, in every footprint he leaves, a tiny point of warm golden light stays glowing on the ground. He never turns back."),
 ("4", "k4", "Sekin crane up (kamera yuqoriga ko'tariladi) va oldinga",
  "Oxiri: «Kechir, inson, g'azabingni muhabbatga aylantir… bir zarra nurga almashtir» — yashil yo'l tobora yorqinlashadi, undan nur zarralari osmonga ko'tariladi, quyosh bitta yorqin nuqtaga aylanadi, butun kadr iliq nurga yutiladi.",
  "Slow crane up and forward over the courtyard toward the sunset. The glowing green path grows brighter and brighter; tiny particles of light rise from it like fireflies into the sky; leaves of the big tree drift slowly in the warm wind; the setting sun shrinks into one single brilliant point of light, and in the last two seconds the whole engraved drawing gently dissolves into soft warm golden light. No people appear."),
]
def prompt(n, img, cam, what, p):
    return f"Horizontal 16:9 video, 8 seconds, from the attached image (this image is the first frame). {p} {STYLE} {KEEP} {SIL}\n{VEO_NEG}"
cards = [dict(num=n, title=f"{n}-davom — video, 16:9 (yotiq), 8 s", shot=f"web/{img}.webp", shotcap=f"davom/{img}.png — Veo'ga shuni yuklang",
              whatlbl="Nima bo'ladi", what=what, cam=cam, prompt=prompt(n, img, cam, what, p)) for n, img, cam, what, p in S]
page("O'zligim davomi", "«O'zligim» <em>davomi va oxiri</em>",
     "GPT bilan qilingan kliplarning oxirgi kadrlaridan 4 ta davom klipi. Veo'da Format 16:9, chapdagi kadrni yuklang (asl fayllar chatda), «Nusxa olish» bilan promptni qo'ying.",
     cards, os.path.join(D, "sahnalar.html"))
print(len(S))
