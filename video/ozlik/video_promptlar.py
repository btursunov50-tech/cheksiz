# «O'zligim» — Veo video promptlari (16:9, 8 s) → sahnalar.html. Rasm = harakatning boshi; yo'nalish aniq, teskarisi taqiqlangan.
# «halo» so'zi yozilmaydi (Veo halqa chizadi), «no ring above any head».
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", ".claude", "skills", "promptlar")); from sahifa import page, VEO_NEG
STYLE = ("The flat hand-drawn ink illustration style on warm paper stays exactly the same in every frame, like a living storybook drawing; it never turns into a photo, 3D or a different style. "
         "Alisher keeps the soft white outline glow hugging his silhouette edges in every frame; nobody has a ring, circle or ring of light above or around the head at any moment. "
         "The small neon accents (the cyan-blue crescent moon, the red tulip and any glowing light already in the image) stay small and contained and never spread.")
KEEP = "Keep every person exactly as in the image for the whole clip: the same face, age, beard or no beard, embroidered doppi cap, clothes and colours{x}; faces never change into other people."
SIL = "Silent video: no audio, no voices, no music. Nobody speaks; mouths stay closed or only smile."
S = [
 ("1", "s01", "Juda sekin push-in yo'l bo'ylab, bolaga qarab", "Uzoqdagi bola kameraga qarab yura boshlaydi va kattarib keladi; gullagan daraxtdan barglar uchadi",
  "Very slow push-in along the road toward the boy. The small boy far away starts walking toward the camera with small steady steps and comes closer, getting bigger in the frame; he only walks forward and never turns back. White blossom petals drift slowly from the old tree, the grass sways gently, the blue crescent moon glows softly.", ""),
 ("2", "s02", "Sekin pull-back (kamera orqaga yuradi, bola u bilan birga keladi)", "Bola kameraga qarab yuradi, atrofga qaraydi; orqasida ko'z yoshi tushgan joyda yangi gullar unib chiqadi",
  "Slow pull-back as the boy walks toward the camera, keeping him at the same size. He walks forward step by step, turning his head left and right as if searching, a tear rolling down his cheek. Behind him, along his path on the road, small ink flowers sprout and open one after another where he has stepped. He never walks backward.", ""),
 ("3", "s03", "Sekin crane up (kamera pastdan yuqoriga ko'tariladi)", "O'smir osmonga qo'l cho'zadi; chapda quyosh tog' ortiga botadi, o'ngda ko'k oy chiqib yorqinlashadi",
  "Slow crane up from the road toward the sky. The teenager slowly reaches his open hand higher toward the sky, looking from the setting sun to the moon with a longing face. The ink-drawn sun on the left slowly sinks behind the hills while the blue crescent moon on the right rises a little and glows brighter. His hand only moves up, never down.", ""),
 ("4", "s04", "Juda sekin push-in yuziga", "Ko'ksidagi ko'k nur sekin kuchayadi; u ko'ksiga qarab hayron, keyin iliq jilmayadi",
  "Very slow push-in toward his face and chest. The small blue light under his hand on his chest slowly grows brighter and pulses gently like a heartbeat, light shining softly through his fingers. He looks down at it with quiet surprise, then his face softens into a warm smile and he closes his eyes for a moment. Blossoms drift down slowly behind him.", ""),
 ("5", "s05", "Sekin truck chapga (kamera yon tomonga suriladi)", "Yigit qirg'oq bo'ylab yuradi, kaftidagi tomchiga qaraydi; orqada to'lqinlar urilib, ko'pik sochiladi",
  "Slow truck to the left alongside him. The young man walks slowly along the shore toward the camera, holding the single glowing blue drop in his open palm and looking at it with wonder; the big waves behind him rise, curl and crash softly into foam again and again. The drop stays in his palm and never falls.", ""),
 ("6", "s06", "Statik (kamera qimirlamaydi)", "Varaqlar havoda uchib aylanadi; u kitobdagi qizil chiziqqa qarab, boshini sekin chayqaydi va kitobni varaqlaydi",
  "Static camera, zero camera movement. Loose pages float and swirl slowly in the air above him. He turns one page of the big book with his free hand, looks at the single glowing red line, frowns, rubs his temple and slowly shakes his head, puzzled. The book pages show only unreadable wavy strokes, no letters.", ""),
 ("7", "s07", "Sekin pull-back, ikkalasi kameraga qarab yuradi", "Ikkalasi qo'l ushlashib yuradi, bir-biriga qarab jilmayadi; ko'ksidagi qizil yurak urib yonadi; oyoq ostidan gullar unadi",
  "Slow pull-back as the couple walks hand in hand toward the camera. They glance at each other and smile shyly; the red heart glowing on his chest beats softly; behind their steps small ink flowers sprout on the road; leaves of the summer tree sway in the breeze. They keep holding hands for the whole clip.", ", and Zebo's oval face, two long black braids, headscarf and ikat dress exactly as in the image"),
 ("8", "s08", "Juda sekin pull-back (kamera orqaga, ikkalasi kichrayadi)", "Qo'llar ajraladi; Alisher o'ng yo'ldan uzoqlashib ketadi, Zebo lolani ko'ksiga bosib, chap yo'lda yig'lab qoladi",
  "Very slow pull-back. Their fingertips slip apart and do not touch again. Alisher turns and walks away along the right path with his head down, getting smaller in the distance; he never turns back and never comes back. Zebo stays standing at the start of the left path, pressing the red tulip to her chest, a tear running down her cheek, watching him go. Leaves fall slowly from the tree.", ", and Zebo's face, braids, headscarf and ikat dress exactly as in the image"),
]
def prompt(n, img, cam, what, p, x):
    return f"Horizontal 16:9 video, 8 seconds, from the attached image. {p} {STYLE} {KEEP.format(x=x)} {SIL}\n{VEO_NEG}"
cards = [dict(num=n, title=f"{n}-sahna — video, 16:9 (yotiq), 8 s", shot=f"web/{img}.webp", shotcap=f"img/{img}.png — Veo'ga shuni yuklang",
              whatlbl="Nima bo'ladi", what=what, cam=cam, prompt=prompt(n, img, cam, what, p, x)) for n, img, cam, what, p, x in S]
page("O'zligim video sahnalari", "«O'zligim» <em>video sahnalari</em>",
     "8 ta klip, hammasi 16:9 (yotiq), 8 soniya, ovozsiz. Veo'da Format: 16:9 ni tanlang, chapdagi rasmni (yangi uslubdagisi tayyor bo'lsa, shuni) yuklang va promptni qo'ying.",
     cards, os.path.join(D, "sahnalar.html"))
print(len(S))
