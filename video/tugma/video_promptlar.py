# «Bitta tugma» — Veo video promptlari (9:16, 8 s) → sahnalar.html + video_promptlar.txt.
# Hikoyachi formati: faqat 6-sahnada Malika ukasiga gapiradi (lablari qimirlaydi), qolganlarida og'iz yopiq. 3, 4, 5, 7-sahnalar va 6-sahnaning Word qismi kodda chiziladi.
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", ".claude", "skills", "promptlar")); from sahifa import page, VEO_NEG
STYLE = ("The hand-drawn sepia ink sketch style on warm yellow parchment paper stays exactly the same in every frame (fine brown ink lines and cross-hatching, "
         "a soft white glow halo around the main characters); it never turns into a photo, 3D or a different style. The neon accents stay small and contained, "
         "they never spread over faces, clothes or the table: the small neon cyan-blue core inside the desk lamp glass, the neon blue moon in the window, "
         "the neon red calculator buttons and the thin neon blue lines on the laptop screen.")
KEEP = ("Keep every person exactly as in the image for the whole clip: Malika's round kind face, dark hair in a neat low bun, small earrings, knitted cardigan "
        "and floral blouse{x}; faces must not change into other people; the same shop, shelves, lamp and props in the same places.")
SIL = "Silent video: no audio at all, no voices, no sound effects, no music."
QUIET = "Malika keeps her mouth closed in this clip (only the narrator speaks in the final video)."
S = [
 ("1", "s01", "Juda sekin push-in: charchagan yuziga yaqinlashadi",
  "Malika kalkulyatorni bir necha marta bosadi, daftarga qaraydi, peshonasini ishqalab og'ir xo'rsinadi, boshini sekin chayqaydi",
  "Very slow push-in toward Malika's tired face. She keeps pressing the calculator buttons with her right index finger, three or four slow taps, glances down at the open ledger, then rubs her forehead with her left hand and lets out a heavy sigh, her shoulders dropping; she shakes her head slowly. Her eyelids are heavy, eyebrows pulled together. The lamp core flickers very softly. The ledger stays open, the tea cup and the receipts stay where they are.", ""),
 ("2", "s02", "Yengil qo'l kamerasi (handheld), juda oz tebranadi",
  "Qo'li klaviatura ustida titraydi, tegishga jur'at qilmaydi, qo'lini ko'ksiga tortib, orqaga suyanadi va yutinadi",
  "Gentle handheld camera with a very slight nervous drift, staying over the shoulder framing. Malika's right hand hovers above the keyboard, her fingers tremble a little, she almost touches a key but pulls her hand back to her chest; she leans back slightly, swallows, her eyebrows rise higher, eyes wide and unsure, lips slightly parted. The thin blue grid lines on the dark laptop screen pulse very faintly. The laptop screen stays dark with only blank grid lines, no text appears.", ""),
 ("4-5", "s_qoshimcha", "Sekin pull-back (orqaga uzoqlashadi)",
  "Xursand jilmayib ekranga qaraydi, barmoqlari bilan yengil yozadi, mamnun bosh irg'aydi (Excel sahnalari orasida qisqa javob kadri)",
  "Slow pull-back. Malika smiles happily at the laptop screen, her eyes shining, cheeks lifted; she lightly taps two keys with her right hand, then gives a small satisfied nod and relaxes her shoulders, still smiling. The laptop screen stays dark with only thin blank blue grid lines, no text appears.", ""),
 ("6", "s06", "Sekin push-in ikkalasiga",
  "Malika ekranni ko'rsatib, ukasiga xotirjam tushuntiradi (lablari qimirlaydi); ukasi engashib qaraydi, ko'zlari kattalashadi, umid bilan jilmayib bosh irg'aydi",
  "Slow push-in toward both of them. Malika keeps pointing at the laptop screen and calmly explains something to her brother, her lips and jaw moving naturally as if talking, with a kind smile and small hand gestures toward the screen. Her brother leans in closer to look, still holding the empty folder with both hands; his worried face slowly changes: eyebrows relax, eyes widen with interest, and a small hopeful smile appears, he nods twice. He keeps his mouth closed. The laptop screen stays dark with only thin blank blue rectangles, no text appears.", ", and the brother's young face, short black hair and plain sweater exactly as in the image"),
 ("8", "s08", "Sekin pull-back va biroz yuqoriga (crane up)",
  "Noutbuk qopqog'ini oxirigacha yopadi (ko'k chiziq yo'qoladi), choydan ho'plab, derazadagi tongga qarab jilmayadi",
  "Slow pull-back with a slight crane up. Malika slowly closes the laptop lid all the way with her left hand, the last thin blue line of light disappears; the lid stays closed and she never opens it again. She lifts the cup of hot tea, takes a calm sip, steam rising softly, and looks toward the morning sun in the window with a warm, proud smile, eyes slightly narrowed with joy. The ledger and the calculator stay pushed to the edge of the counter.", ""),
]
def prompt(n, img, cam, what, p, x):
    talk = "" if n == "6" else QUIET + " "
    return f"Vertical 9:16 video, 8 seconds, from the attached image. {p} {talk}{STYLE} {KEEP.format(x=x)} {SIL}\n{VEO_NEG}"
cards = [dict(num=n, title=f"{n}-sahna — video, 9:16 (tik), 8 s", shot=f"web/{img}.webp", shotcap=f"img/{img}.png — Veo'ga shuni yuklang",
              whatlbl="Nima bo'ladi", what=what, cam=cam, prompt=prompt(n, img, cam, what, p, x)) for n, img, cam, what, p, x in S]
page("Bitta tugma sahnalari", "«Bitta tugma» <em>video sahnalari</em>",
     "5 ta klip, hammasi 9:16 (tik), 8 soniya. Veo'da har biri uchun chapdagi rasmni yuklang va «Nusxa olish» bilan promptni qo'ying. Excel va Word ekranlari (Alt+=, Ctrl+T, Ctrl+E, Word namunasi, PDF), bot va avatar kodda chiziladi, ular uchun klip kerak emas.",
     cards, os.path.join(D, "sahnalar.html"))
open(os.path.join(D, "video_promptlar.txt"), "w").write("\n\n".join(f"### {x[0]}\n" + prompt(*x) for x in S))
print(len(S), "video prompt")
