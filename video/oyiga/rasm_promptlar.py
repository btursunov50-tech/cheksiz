# «Oyiga atigi…» — 11 sahna rasm promptlari sahifasi (ChatGPT, 9:16).
# Har promptga kerakli qahramonlarning alohida 9:16 namuna rasmi biriktiriladi (img/ref_usta.png, img/ref_diyor.png);
# sahifada o'sha namunalar prompt yonida turadi.
# Ishlatish: python3 video/oyiga/rasm_promptlar.py → video/oyiga/rasmlar.html (+ web/ref_*.webp)
# Rang (egasi, 2026-10-26): Kalamushqir'dan faqat ranglar — sariq, ko'k, qizil va ko'zni tortadigan ranglar; bitta kadrda 2–3 ta rang.
import html

IMG = {   # egasi yuborgan sahna rasmlari: n → [("s01", "izoh"), ...]
 1: [("s01", "✅ tasdiqlandi · Apple belgilari tozalandi (img/s01.png)")],
 2: [("s02", "✅ tasdiqlandi · Apple belgilari tozalandi (img/s02.png)")],
 9: [("s09", "✅ tasdiqlandi · Apple belgilari tozalandi (img/s09.png)")],
 10: [("s10", "✅ tasdiqlandi (img/s10.png)")],
 11: [("s11", "✅ tasdiqlandi (img/s11.png)")],
 8: [("s08", "✅ tasdiqlandi (img/s08.png)")],
 7: [("s07", "✅ tasdiqlandi (img/s07.png)")],
 6: [("s06", "✅ tasdiqlandi · Apple belgilari tozalandi (img/s06.png)")],
 5: [("s05", "✅ qabul qilindi (tahrirdan keyin, img/s05.png)")],
 4: [("s04", "✅ tasdiqlandi (img/s04.png)")],
 3: [("s03", "✅ tasdiqlandi (tahrirdan keyin) · Apple belgilari tozalandi (img/s03.png)")],
}
NOTE = {
 # klip izohlari (Veo, 2026-10-26)
 1: "Usta yuzi namunadek (do'ppi, qora soqol, chopon, qizil belbog'), qo'llari yosh, ikki qo'l: biri ko'rsatadi, biri pastda. Sariq yorliq va qizil yorliq bo'sh. Orqada Toshkent teleminorasi. Ranglar: sariq, ko'k, qizil. ChatGPT tahriri belgilarni olib tashlamadi; Claude ularni o'zi tozaladi (OpenCV inpaint). Veo'ga img/s01.png beriladi.",
 3: "Kiyim, do'ppi, lupa, qizil yorliq, ranglar (to'q sariq, qizil) to'g'ri. Xato: ikkala qo'li qari (ajin, bo'rtgan tomirlar, chuqur bo'g'im chiziqlari), yuzida peshona ajinlari va ko'z atrofida chiziqlar — ~40 yoshdek. Tahrirdan keyin: ikkala qo'l yosh (silliq teri, tomir yo'q), yuz namunaga yaqin (qoshini ko'targani uchun peshonada yengil chiziq). 2 ta Apple belgisini Claude tozaladi. Veo'ga img/s03.png beriladi.",
 9: "Diyor yuzi namunadek, xotirjam ayyorona tabassum. Bir qo'li telefonni javonga qo'yadi, biri daftar va qalam ushlagan; nuri yorqin. Ranglar: sariq, ko'k. Vitrinadagi 11 ta Apple belgisi va mayda yozuvni Claude tozaladi.",
 10: "Usta yaqin planda, yuzi namunadek, iliq tabassum. Qo'llari kadrda yo'q. Ranglar: to'q sariq (yuzning bir tomoni), to'q ko'k (orqa fon).",
 11: "Usta o'ng qo'lida telefon (ekran zumrad, oltin yorliq surati va bo'sh xabar pufakchalari, yozuv yo'q), chap qo'li Diyorning yelkasida; Diyor bosh barmog'ini ko'taradi. Ikkala yuz namunadek (Diyor biroz multfilmroq, lekin o'sha qahramon). Qo'llar yosh. Tepada sarlavha uchun bo'sh qorong'i joy bor — montajda katta @sahiychishopbot. Ranglar: ko'k, sariq, zumrad.",
 8: "Usta yuzi namunadek. O'ng qo'lda aniq 3 barmoq ochiq (bosh barmoq jimjiloqni ushlagan), chap qo'l pastda; ikkalasi yosh. Tepada 3 belgi: sariq tanga, ko'k chek (o'qib bo'lmaydigan chiziqlar, harf yo'q), qizil qum soat. Ranglar: sariq, ko'k, qizil.",
 7: "Usta yuzi namunadek. Tarozi: chap pallada kichik oltin ustun (naqd narx), o'ng pallada katta oltin+qizil uyum, o'ng palla pastroq. O'ng qo'li taroziga ishora qiladi, chap qo'li pastda; qo'llar yosh (barmoq bukilganda bo'g'imda oddiy burmalar). Ranglar: sariq, qizil, ko'k. Orqadagi telefonlarda belgi ko'rinmaydi.",
 6: "Diyor yuzi namunadek, bir qo'li boshida, biri telefonda; nuri xira. Ifodasi «uyalib jilmayish» (to'liq uyalgan emas) — Veo promptida uyalib pastga qarashi yoziladi. Sotuvchi: yumaloq yuz, qalin mo'ylov, yashil jilet, yuzi Usta va Diyornikidan butunlay boshqa; yorliqni ikki qo'llab ushlagan, yorliq bo'sh. Ranglar: sariq, ko'k. Pastki javondagi 11 ta Apple belgisi va mayda yozuvni Claude tozaladi.",
 5: "Yuz namunaga yaqin, do'ppi, chopon, belbog' to'g'ri. 2 ta qizil tanga ustun tepasida, ustun telefon qutisidan baland. Ranglar: sariq, qizil. Qutidagi telefonda belgi yo'q. Kamchilik: tangani ushlagan o'ng qo'l va peshtaxtadagi chap qo'lda bo'g'imlar chuqur burishgan, 30 yoshdan qariroq. Tahrirdan keyin (v2) teri biroz silliqlashdi, bo'g'im burmalari kamaydi, lekin to'liq yo'qolmadi — 7-sahnadagi qo'l bilan bir xil darajada, qabul qilindi.",
 4: "Diyor yuzi namunadek (to'zg'igan soch, katta ko'zlar, xudi, sumka, moviy nur). Qo'llar yosh: o'ng qo'lda 5 barmoq ochiq, chap qo'l ko'rsatkich barmog'i bilan sanaydi. Ranglar: ko'k, sariq. Tangalar 12 emas, 11 ta (boshi orqasida bo'shliq) — tomoshabin sanamaydi; Veo'da tangalar birma-bir yonadi, shu yashiradi. Telefon, belgi, yozuv yo'q.",
 2: "Diyor yuzi namunadek (to'zg'igan soch, katta ko'zlar, xudi, moviy nur, sumka tasmasi), telefon ikki qo'lida. Ranglar: sariq, moviy. ChatGPT tahriri belgilarni olib tashlamadi; Claude vitrinadagi belgilarni o'zi tozaladi (OpenCV inpaint), qo'lidagi telefonda belgi yo'q. Veo'ga img/s02.png beriladi.",
}

REFN = {"usta": "Usta", "diyor": "Diyor"}
NEED = {1: ["usta"], 2: ["diyor"], 3: ["usta"], 4: ["diyor"], 5: ["usta"], 6: ["diyor"],
        7: ["usta"], 8: ["usta"], 9: ["diyor"], 10: ["usta"], 11: ["usta", "diyor"]}
def att(n):
    names = [REFN[k] for k in NEED[n]]
    lst = " and ".join(names)
    return (f"Attach the reference image{'s' if len(names) > 1 else ''} of {lst}. Keep every character exactly as in "
            f"{'their reference images' if len(names) > 1 else 'the reference image'}: the same face, age, hair, beard, clothes and props.")

# Rang palitrasi: har sahnada faqat 2–3 tasi.
COL = {"yellow": "warm golden yellow", "blue": "deep night blue", "red": "rich red", "cyan": "bright cyan-blue",
       "orange": "glowing orange", "teal": "emerald teal"}
UZC = {"yellow": "sariq", "blue": "to'q ko'k", "red": "qizil", "cyan": "moviy", "orange": "to'q sariq", "teal": "zumrad"}
def sty(cols):
    c = ", ".join(COL[k] for k in cols[:-1]) + " and " + COL[cols[-1]]
    return (f"Style: the same hand-painted illustration style as the reference images (painterly ink and paint, visible brush texture, "
            f"cinematic light), but colourful and eye-catching. Colour rule: the whole frame uses ONLY {len(cols)} main colours: {c}; "
            f"everything else is soft dark neutral shadow. Strong, saturated, glowing colour light, no rainbow, no other bright colours. "
            f"Vertical 9:16. No text, no letters, no numbers, no logos, no watermark, no subtitles.")

U = ("USTA (the calm man about 30 years old with a short jet-black beard, black-and-white Uzbek doppi skullcap, dark embroidered "
     "chapan robe with a red sash; his hands are the young strong hands of a 30-year-old man, smooth skin, no wrinkles, no swollen veins)")
D = ("DIYOR (the naive guy about 20 years old with messy black hair, big innocent eyes, dark blue hoodie, jeans and sneakers, "
     "outlined with a soft cyan-blue glow)")
HANDS = ("Every person has exactly two arms and two hands, every hand clearly belongs to its own arm and shoulder, no hand does two things at once.")
SHOP = "a small phone shop on an evening street in Tashkent, a glass shop window with phones on shelves"
TAG = ("a big empty price card with nothing written on it (blank, we add the numbers later)")

S = [
 (1, "0–6 s", "Usta: Oyiga atigi yuz ming. Lekin jami qanchaligini hech kim aytmadi.", ["yellow", "blue", "red"],
  f"Wide shot of {SHOP}. In the window hangs {TAG}, huge and glowing warm golden yellow like a sign; under it a tiny red card, also blank. "
  f"{U} stands in front of the window, turned to the camera with a calm, knowing half-smile, one hand pointing at the tiny red card, the other hand relaxed at his side. "
  f"The street around is deep night blue. {HANDS}"),
 (2, "6–12 s", "Diyor: Usta, oyiga atigi yuz ming ekan! Bemalol olaman.", ["yellow", "cyan"],
  f"Medium shot of {D} in front of the glowing golden shop window, overjoyed, mouth open in a big happy smile, eyes shining, holding a new shiny smartphone "
  f"in both hands close to his chest like a treasure. Warm golden light from the window falls on his face; his own cyan-blue glow around him. {HANDS}"),
 (3, "12–17 s", "Usta: Necha oyga? Jami qancha to'laysan?", ["orange", "red"],
  f"Close-up of {U} holding a big round brass magnifying glass in his right hand over the tiny red blank card in the shop window; his left hand rests on the window frame. "
  f"Through the glass the small red card looks large and glows red. Warm orange light from a street lamp on his calm face; he raises one eyebrow. {HANDS}"),
 (4, "17–25 s", "Diyor: Yuz ming… o'n ikki oy… bir million ikki yuz ming.", ["blue", "yellow"],
  f"{D} counts on his fingers, both hands in front of him, lips moving, eyes looking up in surprise. Around his head twelve small glowing golden coins float "
  f"in a circle, one for each finger he counts; they have no writing on them. Deep night blue background. {HANDS}"),
 (5, "25–30 s", "Usta: Bunga boshlang'ich to'lov, xizmat haqi qo'shilsa-chi?", ["yellow", "red"],
  f"On a wooden shop counter stands a tall column of golden coins; {U} calmly places two more glowing red coins on top of it with his right hand, his left hand "
  f"resting on the counter. The column is taller than the phone box lying next to it. Dark background, golden and red light only. {HANDS}"),
 (6, "30–37 s", "Diyor: Sotuvchi faqat oylik to'lovni aytdi. Naqd narxini so'ramabman.", ["yellow", "blue"],
  f"Inside the phone shop. Behind the counter a cheerful SELLER (a fictional Uzbek man about 40, round face, thick black moustache, short hair, white shirt "
  f"and a dark green shop vest; his face is clearly different from Usta and from Diyor) holds {TAG} up in front of his chest with both hands and smiles widely. "
  f"In the foreground {D} scratches the back of his head with one hand, embarrassed, his other hand holding the phone; his cyan glow is dim. "
  f"Warm golden light behind the counter, deep blue shadows in front. {HANDS}"),
 (7, "37–44 s", "Usta: Kichik bo'lingan narx katta summani yashiradi. Ikkalasini yonma-yon qo'y.", ["yellow", "red", "blue"],
  f"A big old brass balance scale stands on the counter. On the left pan a small neat stack of golden coins (the cash price); on the right pan a much bigger pile "
  f"of golden and red coins, so the right pan hangs lower. {U} stands beside it and points at the scale with his right hand, explaining, his left hand at his side. "
  f"Deep blue background. {HANDS}"),
 (8, "44–54 s", "Usta: Uchta savol ber. Naqd narxi qancha? Jami qancha to'layman? Kechiksam nima bo'ladi?", ["yellow", "blue", "red"],
  f"{U} faces the camera and holds up three fingers of his right hand; his left hand at his side. Above his hand float three glowing symbols in a row, "
  f"with no writing on them: a single golden coin, a rolled blue paper receipt, a small red hourglass. Deep night blue background. {HANDS}"),
 (9, "54–58 s", "Diyor: Shoshilmayman. Avval hisoblab ko'raman.", ["cyan", "yellow"],
  f"{D} calmly puts the smartphone back on the glowing shop shelf with one hand and smiles a relaxed, clever smile; his other hand holds a small paper notebook and a pencil. "
  f"His cyan-blue glow is bright and steady again. Warm golden shelf light. {HANDS}"),
 (10, "58–65 s", "Usta: «Oyiga atigi» degandan keyin bitta savol qoladi: oxirida jami qancha?", ["orange", "blue"],
  f"Close-up portrait of {U} looking straight into the camera with a warm, wise smile. Warm orange street-lamp light on one side of his face, deep night blue "
  f"on the other side. His hands are not in the frame."),
 (11, "65–76 s", "Usta: Narx yorlig'i yoki shartnoma suratini botimizga yuboring: @sahiychishopbot…", ["blue", "yellow", "teal"],
  f"Medium shot. {U} holds a smartphone toward the camera with his right hand; the screen glows emerald teal with a chat: a photo of a blank golden price card "
  f"and a few empty message bubbles, no readable text. His left hand rests on the shoulder of {D}, who stands beside him and gives a thumbs up with one hand. "
  f"Warm golden shop light behind them, deep blue shadows. Leave empty dark space in the top third of the frame for a title. {HANDS}"),
]

# Veo (rasm → video) promptlari, egasi (2026-10-26): har birining boshida kamera harakati; hayajon va mimika joylarida
# yaqin plan + yuz ifodasi aniq yoziladi; qahramonlar aniq harakat qiladi. Qo'shni sahnalarda harakat takrorlanmaydi.
KEEP = ("Keep every character exactly as in the image for the whole clip, also when the camera comes closer: the same face shape, eyes, eyebrows, beard, age, hair, "
        "clothes, colours and props; Usta's doppi keeps its white arch embroidery; Diyor's hoodie stays dark navy blue and his cyan-blue glow stays only a thin outline around him, it never colours his body or clothes. "
        "The same number of arms and hands, exactly five fingers on each hand, young smooth hands; objects stay where they are unless the action moves them, nothing shrinks, melts or disappears. "
        "Keep the background, the colours and the painted illustration style exactly as in the image. "
        "Facial expressions are clear and alive (eyes, eyebrows, cheeks, head movement) but there is no dialogue and no lip-sync: mouths move only slightly, no wide toothy grins. "
        "No new people, no extra objects, no brand logos on phones or boxes, no text, no letters, no numbers, no symbols on cards, screens or paper, no captions, no subtitles, no watermark. Only quiet ambient sound.")
# Egasi (2026-10-26): «rasm bilan solishtir, Veo xato qilmasin». Har prompt o'z rasmidagi kadrdan boshlanadi; birinchi kliplardagi xatolar
# (yaqin planda yuz o'zgarishi, nur butun tanani bo'yashi, yorliqda soxta yozuv, narsa yo'qolishi) KEEP va har sahnada taqiqlangan.
V = {
 1: ("Slow push-in from the medium shot in the image toward Usta, ending in a medium shot from the knees up (not a close-up), the tiny red card still beside him",
     "Usta points at the tiny red card, then slowly turns his head to the camera; his eyes narrow knowingly, one eyebrow lifts and a calm sly half-smile appears. "
     "Rain drops glitter in the golden window light; the big yellow card glows softly. "
     "Both price cards stay blank for the whole clip, with nothing written on them; the small red card stays hanging in the window, Usta never takes it in his hand."),
 2: ("Handheld camera with a light natural bounce, slowly circling a little to the right around Diyor, keeping his whole upper body in frame",
     "Diyor bounces on his toes with joy and hugs the phone to his chest with both hands, then lifts it in front of his chest and looks at it; his eyes go wide and shining, eyebrows jump up, "
     "a big happy smile, his cheeks round with happiness; he never puts the phone to his ear; his cyan-blue outline flickers a little brighter."),
 3: ("Slow rack focus: from the glowing red card seen through the magnifying glass to Usta's face behind it",
     "Usta slowly moves the magnifying glass closer to the red card; the red card grows larger in the lens and stays blank; he squints one eye, raises one eyebrow high "
     "and gives a slow, suspicious little nod; warm orange street-lamp light flickers on his face; his other hand stays on the window frame."),
 4: ("Slow 90-degree orbit around Diyor from his left side to the front, ending in a medium close-up of his face and both hands",
     "Diyor taps his fingers one by one, counting; with every tap one more golden coin in the circle around his head lights up brighter; the coins stay in their circle, they never fall; his lips count silently; "
     "at the end his eyebrows shoot up, his eyes go very wide and his mouth opens slowly in surprise; he freezes with his fingers in the air."),
 5: ("Slow pull-back (dolly out) from the medium shot in the image, ending wide enough that two coin columns fit in the frame with Usta's face above them",
     "speed ramp: Usta lets the glowing red coin go; it falls onto the top of the column in extreme slow motion, turning and catching the light, and lands on the other red coin with a crisp clink; "
     "normal speed resumes; a short burst of golden and red sparks flies up from the top of the column, and on the counter just to the LEFT of the first column (away from the phone box) a SECOND column of golden coins "
     "with red coins on top quickly grows up out of the sparks, coin by coin, until it is as tall as the first one; now two tall columns stand side by side, the total has doubled. "
     "The first column stays exactly the same height and in the same place for the whole clip, it never shrinks, never falls, never disappears; the phone box stays where it is; no coins scatter on the table; the sparks fade quickly. "
     "Usta watches the second column grow, then looks into the camera and raises his eyebrows meaningfully with a small knowing smile, eyes open; his left hand stays on the counter."),
 6: ("Smooth lateral dolly (truck) left from the smiling seller behind the counter to Diyor in the foreground, ending in a medium shot of Diyor",
     "the seller grins and wiggles the big blank golden card toward Diyor; Diyor keeps scratching the back of his head with one hand and holds the phone in the other; his smile fades into an awkward embarrassed smile, "
     "he lowers his eyes to the floor, his cheeks blush pink and he shrugs one shoulder. All colours stay exactly as in the image: no green or teal tint on Diyor, his hoodie stays dark navy blue, "
     "his thin cyan outline only becomes a little fainter."),
 7: ("Slow tilt down from Usta's face to the scale, ending on both pans of the scale with Usta's pointing hand still in frame",
     "the right pan with the big golden and red pile sinks a little lower with a heavy clunk while the left pan with the small stack rises a little; the coins stay on their pans; "
     "Usta moves his pointing finger from the small stack to the big pile and nods slowly with raised eyebrows, a calm serious look; his other hand stays at his side."),
 8: ("Slow arc (orbit) of about 30 degrees to the right around Usta, ending in a medium shot with his raised hand and the three symbols above it",
     "Usta keeps exactly three fingers raised for the whole clip; the golden coin, the blue receipt and the red hourglass pulse brightly one after another, left to right, and stay floating in their places; "
     "the receipt stays blank with only faint lines, no letters; with each pulse Usta gives a small firm nod and his eyebrows lift; at the end he looks straight into the camera with a confident, caring look."),
 9: ("Smooth lateral dolly (truck) right along the shop window, ending in a medium shot of Diyor next to the shelf",
     "Diyor calmly pushes the phone back into its place on the glowing shelf and lets it go, then lowers that hand; he turns his head to the camera with a relaxed, clever smile and a confident little nod, "
     "holding the notebook and pencil in his other hand close to his chest; the phones on the shelf stay plain with no logos; his thin cyan-blue outline becomes bright and steady."),
 10: ("Very slow push-in on Usta's face, ending in a slightly closer head-and-shoulders close-up (never closer than the whole face)",
      "Usta looks straight into the camera, tilts his head slightly, his eyes soften into a warm wise smile, then his eyebrows rise slowly as if asking a question; "
      "the orange street-lamp light flickers gently on one side of his face, deep blue on the other; his face shape, beard and doppi stay exactly as in the image."),
 11: ("Slow dolly out and crane up, ending in a medium wide shot with empty dark space in the top third of the frame",
      "Usta pushes the glowing teal phone a little toward the camera; the screen keeps only the gold card picture and the empty chat bubbles, which pulse softly, no letters appear; "
      "with his other hand he gives Diyor's shoulder a friendly squeeze; Diyor smiles, bounces once and pumps his thumb up; both look into the camera with happy, confident faces."),
}
DUR = {8: "ovoz 10 s: klip 8 s, montajda ~1.25x sekinlashtiraman", 11: "ovoz 11 s: klip 8 s, montajda ~1.4x sekinlashtiraman"}
CAMUZ = {1: "sekin yaqinlashish", 2: "qo'lda, yengil chayqalish", 3: "fokus ko'chishi (lupa → yuz)", 4: "90° aylanish", 5: "sekin uzoqlashish + tanga sekinlashuvi (2 ta ustun)",
         6: "yon tomonga suzish", 7: "yuzdan taroziga pastga burilish", 8: "30° yoy", 9: "vitrina bo'ylab yon tomonga suzish", 10: "juda sekin yaqinlashish (yuz to'liq qoladi)", 11: "uzoqlashib ko'tarilish"}
def vp(n):
    cam, act = V[n]
    return f"Vertical 9:16, 8 seconds. Start from the attached image of scene {n}. Camera: {cam}. Action: {act} {KEEP}"

e = html.escape
cards = []
for n, t, voice, cols, scene in S:
    p = f"{att(n)} Scene {n}, vertical 9:16. {scene} {sty(cols)}"
    refs = "".join(f'<figure class="ref"><img src="web/ref_{k}.webp" alt="{REFN[k]} namunasi"><figcaption>ref_{k}.png</figcaption></figure>' for k in NEED[n])
    sw = "".join(f'<span class="sw sw-{k}">{UZC[k]}</span>' for k in cols)
    imgs = "".join(f'<figure class="sc"><img src="web/{f}.webp" alt="{n}-sahna, {e(c)}"><figcaption>{e(c)}</figcaption></figure>' for f, c in IMG.get(n, []))
    got = (f'<div class="scenes">{imgs}</div>' + (f'<p class="note">{e(NOTE[n])}</p>' if n in NOTE else "")) if imgs else ""
    cards.append(f"""<article class="card"><header><span class="num">{n:02d}</span><h2>{n}-sahna — 9:16 (tik)</h2><span class="dur">{t}</span><span class="sws">{sw}</span></header>{got}
<div class="txt"><span class="lbl">Ovoz</span><p class="voice">{e(voice)}</p>
<span class="lbl">Kamera: {e(CAMUZ[n])}</span>
<span class="lbl">Veo prompti (9:16, 8 s) — Veo'ga yuqoridagi rasmni yuklang{(" · " + e(DUR[n])) if n in DUR else ""}</span>
<pre id="v{n}">{e(vp(n))}</pre><button class="copy" data-t="v{n}">Nusxa olish</button></div></article>""")

page = f"""<title>Oyiga atigi sahnalari</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Manrope:wght@400;600&family=JetBrains+Mono:wght@400&display=swap">
<style>
/* Layout: one column of scene cards; night shop window look in the video's own palette (single dark theme, deliberately). */
:root{{--bg:#0d1018;--card:#161b27;--line:#2a3347;--fg:#eef0f5;--muted:#a7b0c4;--gold:#f4c430;--blue:#3d6bd6;--red:#e0433a;--cyan:#5fd0ff;--orange:#f08a24;--teal:#1fb89a;
--display:"Cormorant Garamond",Georgia,serif;--body:"Manrope",system-ui,sans-serif;--mono:"JetBrains Mono",ui-monospace,monospace;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font-family:var(--body);font-size:15px;line-height:1.55}}
.wrap{{max-width:780px;margin:0 auto;padding-block:28px 60px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:grid;gap:22px}}
h1{{font-family:var(--display);font-weight:700;font-size:clamp(30px,6vw,44px);margin:0;line-height:1.1;text-wrap:balance}}
h1 em{{font-style:normal;color:var(--gold)}}
.intro{{color:var(--muted);margin:0;max-width:64ch}}
.card{{display:grid;gap:14px;background:var(--card);border:1px solid var(--line);border-radius:8px;padding:16px}}
header{{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}}
.num{{font-family:var(--mono);color:var(--gold);font-size:14px}}
h2{{font-family:var(--display);font-weight:700;font-size:26px;margin:0}}
.dur{{font-size:12px;letter-spacing:.06em;text-transform:uppercase;border:1px solid var(--line);border-radius:99px;padding:2px 10px;color:var(--muted)}}
.sws{{display:flex;gap:6px;flex-wrap:wrap}}
.sw{{font-size:12px;padding:2px 9px;border-radius:99px;color:var(--bg);font-weight:600}}
.sw-yellow{{background:var(--gold)}} .sw-blue{{background:var(--blue);color:var(--fg)}} .sw-red{{background:var(--red);color:var(--fg)}}
.sw-cyan{{background:var(--cyan)}} .sw-orange{{background:var(--orange)}} .sw-teal{{background:var(--teal)}}
.row{{display:grid;grid-template-columns:150px minmax(0,1fr);gap:16px;align-items:start}}
@media (max-width:560px){{.row{{grid-template-columns:minmax(0,1fr)}} .refs{{grid-template-columns:repeat(2,minmax(0,120px))}}}}
.refs{{display:grid;grid-template-columns:minmax(0,1fr);gap:8px;align-content:start}} .rh{{grid-column:1/-1;margin:0;font-size:12px;color:var(--muted)}}
.ref{{margin:0;display:grid;gap:4px}} .ref img{{width:100%;border-radius:4px;display:block;border:1px solid var(--line)}}
.ref figcaption{{font-size:12px;color:var(--muted);font-family:var(--mono)}}
.scenes{{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px}}
.sc{{margin:0;display:grid;gap:6px}} .sc img{{width:100%;border-radius:4px;display:block;border:1px solid var(--line)}}
.sc figcaption{{font-size:12px;color:var(--muted)}} .note{{margin:0;font-size:13px;color:var(--gold)}}
.txt{{min-width:0;display:flex;flex-direction:column;gap:8px}}
.lbl{{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}}
.voice{{margin:0;font-style:italic}}
pre{{margin:0;white-space:pre-wrap;word-break:break-word;font-family:var(--mono);font-size:12.5px;line-height:1.6;background:var(--bg);border:1px solid var(--line);border-radius:6px;padding:12px;user-select:all}}
.copy{{align-self:flex-start;font:600 15px var(--body);color:var(--bg);background:var(--gold);border:0;border-radius:8px;padding:10px 18px;cursor:pointer}}
.copy.done{{background:var(--cyan)}} .copy:focus-visible{{outline:2px solid var(--fg);outline-offset:2px}}
</style>
<div class="wrap">
<h1>«Oyiga atigi…» <em>sahnalari</em></h1>
<p class="intro">Rasmlar tayyor. Endi har sahna uchun: Veo'da «Frames to video» ni oching, shu kartadagi rasmni yuklang (belgilari tozalangan .png fayl), o'lchamni 9:16 qiling va «Nusxa olish» bilan promptni qo'ying (8 s). Har promptning boshida kamera harakati bor, hayajonli joylarda yuz ifodasi yozilgan. Rasm promptlari repoda saqlanadi (rasm_promptlar.py). Narx va raqamlarni montajda o'zimiz yozamiz.</p>
{''.join(cards)}
</div>
<script>
document.querySelectorAll('.copy').forEach(b=>b.addEventListener('click',()=>{{
 const pre=document.getElementById(b.dataset.t);const t=pre.textContent;
 const ok=()=>{{b.textContent='Nusxa olindi';b.classList.add('done');setTimeout(()=>{{b.textContent='Nusxa olish';b.classList.remove('done')}},1800)}};
 const sel=()=>{{const r=document.createRange();r.selectNodeContents(pre);const s=getSelection();s.removeAllRanges();s.addRange(r);b.textContent='Belgilandi, nusxa oling'}};
 try{{navigator.clipboard.writeText(t).then(ok,sel)}}catch(e){{sel()}}
}}));
</script>
"""
open("video/oyiga/rasmlar.html", "w").write(page)
print(len(S), "sahna")
