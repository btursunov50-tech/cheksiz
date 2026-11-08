# «G'azabda sukut» — sahna rasmlari uchun ChatGPT promptlari (9:16) → sahnalar.html (Artifact) + rasm_promptlar.txt.
# Qoidalar: /promptlar skill (rasm = harakat boshi, telefon ekranlari bo'sh, 2–3 asosiy rang, Diyor neon chizig'i, yosh dumaloq yuz).
# Ishlatish: python3 video/sukut/rasm_promptlar.py
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", ".claude", "skills", "promptlar")); from sahifa import page
Dy = ("DIYOR (the calm guy about 20 years old with a round boyish young face (NOT an adult man, no sharp jaw, no wrinkles), big expressive brown eyes, "
      "messy straight jet-black hair (never curly, never brown), smooth clear skin without freckles, a dark navy blue hoodie, jeans and sneakers; "
      "a thin bright cyan-blue neon line runs exactly along his whole outer silhouette (hair, face, hoodie, arms, legs) with a soft blue glow; nothing else in the frame has this outline)")
MAN = ("THE ANGRY MAN (a heavy-set Uzbek man about 45 years old, round face with a short grey-black beard and moustache, thick eyebrows, "
       "a dark brown leather jacket over a grey sweater, a black flat cap; no neon outline)")
HANDS = "Every person has exactly two arms and two hands, five fingers on each hand, every hand clearly belongs to its own arm."
NOTXT = "Vertical 9:16. No text, no letters, no numbers, no logos, no brand names, no watermark, no subtitles; every phone screen is plain and blank (glowing, without any text or icons)."
COL = {"amber": "warm amber yellow", "blue": "deep evening blue", "red": "rich red", "teal": "deep teal", "cream": "soft warm cream", "grey": "cool grey", "green": "fresh green"}
def sty(cols):
    c = ", ".join(COL[k] for k in cols[:-1]) + " and " + COL[cols[-1]]
    return ("Style: the same hand-painted semi-realistic cartoon illustration style as the attached reference images (painterly, visible brush texture), "
            f"cinematic soft light, colourful and eye-catching. Colour rule: the whole frame uses ONLY {len(cols)} main colours: {c}; everything else is soft neutral shadow. {NOTXT}")
REFS = {"d": [("web/ref_diyor.webp", "ref_diyor.png"), ("web/ref_diyor2.webp", "ref_diyor2.png")], "m": [("web/ref_man.webp", "ref_man.png (0-rasmdan keyin)")]}
def att(r):
    if not r: return "No reference images are needed. "
    parts = []
    if "d" in r: parts.append("the two reference images of Diyor (keep his face, age, hair, hoodie and the thin cyan-blue neon outline exactly as in them)")
    if "m" in r: parts.append("the reference image of the angry man (keep his face, beard, cap and jacket exactly as in it)")
    return "Attach " + " and ".join(parts) + ". "
# (raqam, sarlavha, plan, ranglar, namunalar, sahna, ovoz/izoh)
S = [
 ("0", "Namuna: avtobusdagi odam — 9:16 (tik)", "Full-body character reference sheet, plain soft background", ["grey", "amber", "cream"], "",
  f"A character reference image: {MAN} standing in a neutral pose, facing the viewer, arms relaxed, a stern but ordinary face, plain light background, full body visible.",
  "2 va 7-sahnada shu odam chiqadi — avval shuni yasang, keyin 2 va 7 ga biriktiring"),
 ("1", "1-sahna — 9:16 (tik)", "Close-up over the shoulder onto the phone, Diyor's face in profile", ["blue", "red", "cream"], "d",
  f"Night, a small room lit only by a phone. {Dy} sits hunched over his smartphone, eyebrows pulled down in anger, jaw tight, lips pressed; "
  "his thumb hovers about one centimetre ABOVE the glowing blank phone screen, about to press send, not touching it yet. The phone screen is plain and blank (no text). A faint red glow from the screen on his face.",
  "«To'xtang! Shu izohga javob yozishdan oldin buni ko'ring.» — barmoq hali tegmagan (harakat boshi)"),
 ("2", "2-sahna — 9:16 (tik)", "Medium two-shot inside a city bus, eye level", ["amber", "blue", "grey"], "dm",
  f"Inside a city bus in the evening, warm interior lights, blurred city lights through the windows. {MAN} stands facing Diyor, mouth open, starting to shout, one hand raised; "
  f"{Dy} stands holding the overhead rail, looking at the man calmly, eyes open, face relaxed, just about to take a slow breath. Other passengers are blurred in the background.",
  "«G'azab kelganda jim turish — kuchsizlik emas, kuch.» — odam baqira boshlaydi, Diyor hali xotirjam"),
 ("3", "3-sahna — 9:16 (tik)", "Medium shot across an office desk", ["teal", "amber", "cream"], "d",
  f"A small bright office. A young male colleague in a white shirt leans on Diyor's desk with a mocking smirk and one raised eyebrow, arms crossed; "
  f"{Dy} sits at the desk with a laptop (screen blank) and looks up at him with a neutral face, just before smiling.",
  "«Hasadga tabassum bilan javob bering.» — hamkasbi kinoya qiladi, Diyor hali jilmaymagan"),
 ("4", "4-sahna — 9:16 (tik)", "Close-up from the side, phone and face", ["blue", "red", "cream"], "d",
  f"A park bench in the late afternoon. {Dy} holds his smartphone with both hands and is typing fast with both thumbs, frowning; the phone screen glows plain and blank (no text). "
  "Autumn leaves on the ground.",
  "«Qo'zg'atuvchiga javob bermaslik — aql.» — hali yozyapti (keyin to'xtatib, telefonni ag'daradi)"),
 ("5", "5-sahna — 9:16 (tik)", "Wide shot of a teahouse terrace, slightly high angle", ["amber", "red", "teal"], "d",
  "An open-air Uzbek teahouse terrace in autumn: two wooden topchans (raised platforms) covered with red carpets and cushions, low tables with blue-and-white teapots and piyola cups, a grapevine pergola with yellow leaves, warm lantern light. "
  "On the near topchan two middle-aged men in sweaters argue heatedly, one waving his hands in the air, the other pointing his finger at him; one of them turns toward Diyor and gestures at him as if saying «you tell him!». "
  f"{Dy} sits cross-legged at the edge of the same topchan holding a piyola of tea, looking at them, just about to smile and put his right hand on his chest. The second topchan in the background is empty.",
  "«Befoyda bahsdan o'z vaqtida chiqing.» — uni bahsga chaqirishdi, hali o'rnidan turmagan"),
 ("6", "6-sahna — 9:16 (tik)", "Medium shot, slightly low angle toward the boss", ["grey", "blue", "amber"], "d",
  "A manager's office with a big desk and a window with city lights. A strict middle-aged boss in a grey suit stands behind the desk, leaning forward with both fists on the desk, shouting, a sheet of paper in one fist; "
  f"{Dy} stands in front of the desk, back straight, hands calmly together in front of him, face calm and attentive.",
  "«Bosim ostida xotirjam bo'ling.» — rahbar baqiryapti, Diyor xotirjam"),
 ("7", "7-sahna — 9:16 (tik)", "Medium two-shot at the bus stop, eye level", ["amber", "blue", "cream"], "dm",
  f"An evening bus stop on an autumn street with warm street lights. {MAN} stands facing Diyor, looking down a little, embarrassed; "
  f"{Dy} faces him and has just started to raise his right hand to offer a handshake, his hand still low, a kind small smile.",
  "«Kechira olgan odam — g'olib.» — Diyor qo'l uzata boshlaydi (hali qisishmagan)"),
 ("8", "8-sahna — 9:16 (tik)", "Medium shot, warm home interior", ["amber", "red", "cream"], "d",
  "A cosy Uzbek home in the evening: a low table with a red patterned tablecloth, bread, a teapot and piyola cups, warm lamp light. A kind elderly mother in a headscarf sits at the table smiling softly. "
  f"{Dy} has just come in; he is putting his smartphone face down on a shelf by the door with one hand, looking toward his mother with a warm face.",
  "«Bugun bitta odamni kechiring.» — telefonni qo'yyapti (keyin onasiga choy quyadi)"),
]
def prompt(n, shot, cols, refs, scene):
    hands = HANDS + " " if n != "0" else ""
    return f"Vertical 9:16 image, {shot}. {att(refs)}Scene: {scene} {hands}{sty(cols)}"
cards = []
for n, title, shot, cols, refs, scene, note in S:
    r = sum((REFS[k] for k in refs), [])
    cards.append(dict(num=n, title=title, shot=None, refs=r, whatlbl="Gap / izoh", what=note, prompt=prompt(n, shot, cols, refs, scene)))
page("G'azabda sukut sahnalari", "«G'azabda sukut» <em>rasmlari</em>",
     "Avval 0 (avtobusdagi odam namunasi), keyin 1–8. Har biri uchun ChatGPT'da yangi chat oching, chapdagi namunalarni biriktiring, «Nusxa olish» bilan promptni qo'ying. Telefon ekranlari bo'sh chiziladi: yozuvlarni montajda o'zim qo'yaman. Har rasm — harakatning boshi.",
     cards, os.path.join(D, "sahnalar.html"))
open(os.path.join(D, "rasm_promptlar.txt"), "w").write("\n\n".join(f"### {n}\n" + prompt(n, sh, c, r, sc) for n, t, sh, c, r, sc, no in S))
print(len(S), "prompt")
