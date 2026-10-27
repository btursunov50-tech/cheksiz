# «70 foiz chegirma» — 12 sahna rasm promptlari sahifasi (ChatGPT, 9:16).
# Har promptga kerakli qahramonlarning alohida 9:16 namuna rasmi biriktiriladi (img/ref_usta.png, img/ref_diyor.png); sahifada prompt yonida turadi.
# Ishlatish: python3 video/chegirma/rasm_promptlar.py → video/chegirma/rasmlar.html (+ web/ref_*.webp)
# Rang (egasi, 2026-10-26): Kalamushqir'dan faqat ranglar, bitta kadrda 2–3 ta. Hayajonli joylarda plan + mimika yoziladi (2026-10-26).
# Yorliq, taymer, raqamlar rasmda bo'sh — «-70%», «300 000», «-43%» va h.k. montajda yoziladi.
import html

IMG = {   # egasi yuborgan sahna rasmlari: n → [("s01", "izoh"), ...]
 1: [("s01", "✅ tanlandi (C, bulutli, img/s01.png)")],
 2: [("s02", "✅ tasdiqlandi (B, img/s02.png)")],
 9: [("s09", "✅ tasdiqlandi (img/s09.png)")],
 10: [("s10", "✅ tasdiqlandi (img/s10.png)")],
 11: [("s11", "✅ tasdiqlandi (img/s11.png)")],
 12: [("s12", "✅ tasdiqlandi (img/s12.png)")],
 8: [("s08", "✅ tasdiqlandi (img/s08.png)")],
 7: [("s07", "✅ tasdiqlandi (img/s07.png)")],
 6: [("s06", "✅ tasdiqlandi (tahrirdan keyin, img/s06.png)")],
 5: [("s05", "✅ tasdiqlandi · Nike belgisi tozalandi (img/s05.png)")],
 4: [("s04", "✅ tasdiqlandi (img/s04.png)")],
 3: [("s03", "✅ tasdiqlandi (img/s03.png)")],
}
NOTE = {
 2: "A variantda Diyorning nuri pushti bo'lib qolgan edi (rad). B: moviy nur joyida, yuz namunadek, bir qo'li bannerni ko'rsatadi, ikkinchisida hamyon o'rniga telefon — 4-sahnadagi hamyon bilan kichik farq, sezilmaydi. Krossovkada juda xira belgi.",
 9: "Diyor yuzi namunadek, xotirjam ayyorona tabassum; moviy nur joyida. Do'kondan ko'chaga chiqyapti: bir qo'li hamyonni cho'ntakka qaytaradi, biri telefonda kalkulyator (ekranida raqam yo'q). Orqada bulutli ko'cha, yuzsiz odamlar. Ranglar: yalpiz yashil, bulutli ko'k. Javondagi krossovkalarda kichik Nike chiziqlari bor — orqa fonda, Veo'dan oldin ko'rib chiqiladi.",
 10: "Qiz (o'ylab topilgan): uzun qora o'rim soch, pushti-yalpiz atlas ko'ylak, oq sumka; yonidan ko'rinadi, yuzi qisman, Usta va Diyornikidan butunlay boshqa. Diyor yuzi namunadek, boshini qizga burib «sevib qolgan» qiyofada jilmayadi, qo'lida telefon, moviy nur joyida. Usta yuzi namunadek, ayyorona kulib, o'ng qo'lini Diyorning yelkasiga turtishga ko'targan, chap qo'li belbog'ida. Bulutli ko'cha, nam yo'lak, pushti va yashil vitrinalar.",
 12: "Usta o'ng qo'lida telefon (ekranda pushti yorliq surati va bo'sh pufakchalar), chap qo'li Diyorning yelkasida; Diyor bosh barmog'ini ko'taradi, ikkinchi qo'li cho'ntakda. Ikkala yuz namunadek. Moviy nur sochida, xudida xira. Tepada katta bulutli osmon — @sahiychishopbot uchun joy. Ekran tepasida mayda o'qilmaydigan yozuv — montajda bot suhbati ustiga qo'yiladi.",
 11: "Usta yaqin planda kameraga qaraydi, iliq tabassum; do'ppi, soqol namunadek. Ko'z atrofida yengil chiziqlar — boshqa sahnalardan biroz realistikroq/kattaroq ko'rinadi, lekin o'sha odam. Qo'llar kadrda yo'q. Bir tomonda sariq vitrina nuri, orqada bulutli ko'cha.",
 8: "Usta yuzi namunadek. O'ng qo'lda aniq 3 barmoq (bosh barmoq jimjiloqni ushlagan), chap qo'l pastda; ikkalasi yosh. Tepada 3 belgi: sariq lupa, ko'k o'lchov lentasi, pushti savol belgisi — yozuvsiz. Orqada eshikdan bulutli ko'cha, yuzsiz odamlar. Ranglar: sariq, ko'k, pushti. Lentada o'qilmaydigan mayda chiziqlar — normal.",
 7: "Usta yuzi namunadek; kaftini kameraga ochib «shoshilma» deydi — 5 barmoq, yosh qo'l. Oldinda kassada pushti neon taymer, ekrani bo'sh (montajda «faqat bugun 00:59:59»). Ranglar: pushti, binafsha. Chapdagi krossovkalar juda xira, belgi ko'rinmaydi.",
 6: "Diyor yuzi namunadek: hayron, bir qoshi ko'tarilgan, lablari qisilgan. Qo'llar: chap qo'lda 5 barmoq ochiq, o'ng qo'l ko'rsatkich barmog'i bilan sanaydi — to'g'ri. Binafsha neon oyna, sariq javonlar. Kamchilik: Diyorning nuri moviy emas, binafsharang tusga kirgan (atrofdagi binafsha nurdan) — 2-sahnadagi pushtichalik emas; Tahrirdan keyin (B) nur moviy, qolgan hamma narsa o'zgarmagan. Orqadagi krossovkalar juda xira, belgi ko'rinmaydi.",
 5: "Usta yuzi namunadek, ayyorona tabassum, kameraga qaraydi. Ikki qo'li pushti yorliqni qopqoqdek ko'tarib turibdi, ostidan sariq yorliq ochilgan (bo'sh — montajda «-43%»). Oq krossovkalarda aniq Nike belgisi (yon tomonida va tilida) bor edi — Claude tozaladi. Ranglar: pushti, sariq.",
 4: "Diyor yuzi namunadek: o'ylanib, biroz uyalib yuqoriga qaraydi, og'zi yarim ochiq; moviy nur joyida. Telefonni jinsi cho'ntagiga qaytaradi (2-sahnadagi telefon bilan mos), ikkinchi qo'li sumka tasmasida. Promptda yo'q bo'lsa ham orqada Usta turibdi: qo'llari qovushtirilgan, shubha bilan yon qaraydi, yuzi namunaga mos — 3-sahna bilan uzviy. Ranglar: yalpiz yashil, bulutli ko'k.",
 3: "Usta yuzi namunadek, qo'llari qovushtirilgan (ikkala qo'l), do'kon ichi: yalpiz yashil va sariq javonlar, oynadan bulutli ko'cha va yuzsiz odamlar. Diyor faqat orqasidan, moviy nur sochida. Ranglar: yashil, sariq.",
 1: "4 variant solishtirildi (A, B — quyoshli; C, D — bulutli). C tanlandi: yuz namunaga eng yaqin, orqadagi odamlar soyabon bilan, orqasidan, yuzsiz; yo'lak nam, osmon bulutli. Qo'llar yosh, ikkita. Krossovkadagi xira belgi montajdan oldin tozalanadi.",
}

REFN = {"usta": "Usta", "diyor": "Diyor"}
NEED = {1: ["usta"], 2: ["diyor"], 3: ["usta", "diyor"], 4: ["diyor"], 5: ["usta"], 6: ["diyor"],
        7: ["usta"], 8: ["usta"], 9: ["diyor"], 10: ["usta", "diyor"], 11: ["usta"], 12: ["usta", "diyor"]}
def att(n):
    names = [REFN[k] for k in NEED[n]]
    lst = " and ".join(names)
    return (f"Attach the reference image{'s' if len(names) > 1 else ''} of {lst}. Keep every character exactly as in "
            f"{'their reference images' if len(names) > 1 else 'the reference image'}: the same face, age, hair, beard, clothes and props.")

# Rang palitrasi: har sahnada faqat 2–3 tasi.
COL = {"yellow": "warm golden yellow", "blue": "deep night blue", "red": "rich red", "cyan": "bright cyan-blue",
       "orange": "glowing orange", "teal": "emerald teal"}
COL.update({"sky": "cool cloudy grey-blue", "coral": "hot coral pink", "mint": "fresh mint green", "sun": "bright lemon-sun yellow", "violet": "soft violet"})
UZC = {"sky": "bulutli ko'k", "coral": "pushti-marjon", "mint": "yalpiz yashil", "sun": "limon sariq", "violet": "binafsha", "yellow": "sariq", "blue": "to'q ko'k", "red": "qizil", "cyan": "moviy", "orange": "to'q sariq", "teal": "zumrad"}
def sty(cols):
    c = ", ".join(COL[k] for k in cols[:-1]) + " and " + COL[cols[-1]]
    return (f"Style: the same hand-painted illustration style as the reference images (painterly ink and paint, visible brush texture, "
            f"cinematic soft daylight under a cloudy sky), a little darker and moodier, but still colourful and eye-catching: the coloured signs and shop lights glow against the grey day. Colour rule: the whole frame uses ONLY {len(cols)} main colours: {c}; "
            f"everything else is soft dark neutral shadow. Strong, saturated, glowing colour light, no rainbow, no other bright colours. "
            f"Vertical 9:16. No text, no letters, no numbers, no logos, no watermark, no subtitles.")

U = ("USTA (the calm man about 30 years old with a short jet-black beard, black-and-white Uzbek doppi skullcap, dark embroidered "
     "chapan robe with a red sash; his hands are the young strong hands of a 30-year-old man, smooth skin, no wrinkles, no swollen veins)")
D = ("DIYOR (the naive guy about 20 years old with messy black hair, big innocent eyes, dark blue hoodie, jeans and sneakers, "
     "outlined with a soft cyan-blue glow)")
HANDS = ("Every person has exactly two arms and two hands, every hand clearly belongs to its own arm and shoulder, no hand does two things at once.")
# v3 (egasi): «juda yorug', ozgina qorong'iroq, bulutli bo'lsin».
# v2 (egasi, 2026-10-27): «oldingi videoga o'xshab qoldi» — kunduz, odamlar yuradigan ko'cha, do'konning tashqarisi va ichi, boshqa ranglar.
STREET = ("a busy modern shopping street in Tashkent on a cloudy late afternoon, overcast sky with heavy grey clouds, soft diffused light, the whole scene a little darker and moodier, wet-looking pavement: wide sidewalk, trees, a few passers-by walking past in the background "
          "(small, softly out of focus, seen from the side or back, no clear faces), shop fronts with big glass doors")
SHOP_IN = ("inside a bright modern clothes and sneaker shop: white walls, light wooden shelves with sneakers, racks of jackets and hoodies, "
           "a glass entrance door with the cloudy street and passers-by visible through it, a few shoppers far in the background, softly out of focus, no clear faces")
SIGN = "a huge blank hot coral pink sale banner with nothing written on it (we add «-70%» later)"
OLD = "a small blank white card with a thin coral line crossed through it (the old price, written later)"
NEW = "a big blank lemon-yellow price card (the new price, written later)"
PEOPLE = "Background passers-by are small, blurred and faceless; only Usta and Diyor are in focus."

S = [
 (1, "0–6 s", "Usta: Bu 70 foizlik chegirma 70 foiz emas. To'lashdan oldin hisoblang.", ["coral", "sky", "sun"],
  f"Wide shot, slightly low angle, OUTSIDE the shop. {STREET}. Over the shop entrance hangs {SIGN}; next to the door, on a stand, {OLD} and {NEW} above a pair of white sneakers. "
  f"{U} stands on the sidewalk next to the entrance, turned to the camera with a calm, knowing half-smile, the index finger of his right hand pointing up at the coral banner, his left hand relaxed. "
  f"Cloudy grey-blue sky, soft dim daylight, no direct sun. {PEOPLE} {HANDS}"),
 (2, "6–12 s", "Diyor: Usta, qarang! Uch yuz ming edi, bir yuz yetmish ming bo'libdi! Hozir olmasam, yutqazaman!", ["coral", "sun"],
  f"Close-up, eye level, OUTSIDE on the cloudy sidewalk. {D} rushes toward the shop door, overjoyed: eyes wide and shining, eyebrows high, a huge open grin; one hand points at the coral sale banner, "
  f"the other pulls a wallet out of his hoodie pocket. Coral banner light and the warm lemon glow of the shop window on his face; the street with blurred passers-by behind him. {PEOPLE} {HANDS}"),
 (3, "12–17 s", "Usta: Bu narsani chegirmani ko'rishdan oldin ham qidirayotgan edingmi?", ["mint", "sun"],
  f"Over-the-shoulder shot INSIDE the shop, just past the entrance: from behind {D} (we see only his messy hair, shoulder and cyan glow, no face) toward {U}, who stands calm with folded arms "
  f"between racks of hoodies, one eyebrow slightly raised, asking quietly. {SHOP_IN}. Fresh mint green shelves and lemon-yellow light. {PEOPLE} {HANDS}"),
 (4, "17–21 s", "Diyor: Yo'q… Chegirmani ko'rib qoldim.", ["mint", "sky"],
  f"Close-up INSIDE the shop. {D} frozen next to a wall of sneakers, the wallet half out of his pocket, his smile gone, mouth slightly open, eyes looking up and to the side as he thinks, "
  f"a little embarrassed. Mint green shelves, cool grey-blue daylight from the street door behind him. {PEOPLE} {HANDS}"),
 (5, "21–29 s", "Usta: Hisoblaylik. Uch yuz mingdan bir yuz o'ttiz ming tushgan. Bu yetmish emas, qirq uch foiz.", ["coral", "sun"],
  f"Medium close-up INSIDE the shop at the sneaker stand. {U} lifts a big blank coral pink sale tag up with both hands like a lid; underneath it on the stand a smaller blank lemon-yellow card is revealed, glowing "
  f"(we write «-43%» on it later). Usta looks at the camera over the tag with a calm, slightly amused face. {SHOP_IN}. {PEOPLE} {HANDS}"),
 (6, "29–32 s", "Diyor: Unda nega yetmish deb yozishgan?", ["violet", "sun"],
  f"Medium shot INSIDE the shop near a full-length mirror. {D} counts on his fingers, confused: one eyebrow up, head tilted, lips pressed; soft violet light from a neon strip on the shop wall, "
  f"lemon-yellow card glowing behind him. {PEOPLE} {HANDS}"),
 (7, "32–38 s", "Usta: Katta raqam ko'zni, taymer qo'lni shoshiltiradi. Kerakli narsa shoshilishni talab qilmaydi.", ["coral", "violet"],
  f"Close-up INSIDE the shop: a glowing coral pink digital countdown timer on the cash desk, its display blank with no digits (we write «faqat bugun 00:59:59» later); "
  f"behind it, slightly out of focus, {U} raises a calm open palm, saying «slow down». Coral and soft violet light only. {PEOPLE} {HANDS}"),
 (8, "38–48 s", "Usta: Uchta tekshiruv: boshqa do'kondagi narxi qancha? O'lchami, sifati, kafolati bir xilmi? Va shu mahsulot senga kecha ham kerakmidi?", ["sky", "sun", "coral"],
  f"Medium shot INSIDE the shop by the glass door; the cloudy street with blurred passers-by is visible behind him. {U} faces the camera and holds up three fingers of his right hand; his left hand at his side. "
  f"Above his hand float three glowing symbols in a row with no writing: a lemon-yellow magnifying glass, a sky blue measuring tape, a coral question mark. {PEOPLE} {HANDS}"),
 (9, "48–53 s", "Diyor: Demak, avval hisoblayman, keyin olaman.", ["mint", "sky"],
  f"Medium shot, Diyor walking OUT of the shop through the glass door onto the cloudy street. {D} puts his wallet back into his hoodie pocket with one hand and smiles a relaxed, clever smile, a small confident nod; "
  f"his other hand holds his phone showing a plain calculator screen with no digits. Mint green shop sign light and a cloudy grey-blue sky; passers-by blurred on the street. {PEOPLE} {HANDS}"),
 (10, "53–66 s", "Diyor qizga qarab qoladi. Usta: Hoy-hoy, Diyor! Sen do'konda chegirma qidiryapsanmi yoki ko'chada kelin? — Diyor: Yo'q, usta... men... hisoblayapman! — Usta: Ko'zing narxda bo'lsin, ukam. Avval hisob, keyin kelin!", ["coral", "mint", "sky"],
  f"Medium-wide shot OUTSIDE on the cloudy sidewalk in front of the shop. In the foreground on the right a fictional young Uzbek woman about 22 years old walks past to the right, seen from the side and three-quarter back, "
  f"her face only partly visible: very long glossy black hair in one long braid down her back, an elegant modest long-sleeved Uzbek atlas (ikat) dress with a coral and mint pattern, a small handbag; she looks ahead and does not notice anyone. "
  f"In the middle {D} has stopped dead with his phone in one hand, his head turned after her, staring with a dreamy, love-struck face: eyebrows raised, eyes soft and wide, mouth slightly open, a goofy smile; his other hand hangs loose. "
  f"Right behind him {U} leans in with an amused, mock-strict face, one eyebrow high, a knowing smile, his right hand raised about to tap Diyor on the shoulder, his left hand on his own sash. "
  f"Cloudy grey-blue sky, wet pavement, the coral shop banner glowing. Other passers-by are small, blurred and faceless. {HANDS}"),
 (11, "66–71 s", "Usta: Xaridni foiz emas, ehtiyoj hal qilsin.", ["sun", "sky"],
  f"Close-up portrait OUTSIDE on the street, eye level. {U} looks straight into the camera with a warm, wise smile; warm lemon light from a shop window on one side of his face, cool cloudy grey-blue daylight on the other, "
  f"the busy street softly blurred. His hands are not in the frame. {PEOPLE}"),
 (12, "71–81 s", "Usta: Chegirma yorlig'ini suratga olib botimizga yuboring: @sahiychishopbot. Haqiqiy foizni hisoblab, nimani tekshirishni aytib beradi.", ["sky", "sun", "mint"],
  f"Medium shot OUTSIDE on the sidewalk in front of the shop. {U} holds a smartphone toward the camera with his right hand; the screen glows mint green with a chat: a photo of a blank coral sale tag and a few empty message bubbles, "
  f"no readable text. His left hand rests on the shoulder of {D}, who stands beside him and gives a thumbs up with one hand. Cloudy grey-blue sky, soft dim daylight, blurred passers-by. "
  f"Leave empty cloudy sky in the top third of the frame for a title. {PEOPLE} {HANDS}"),
]

# Veo (rasm → video) promptlari (egasi, 2026-10-27): har biri o'z rasmidagi kadrdan DAVOM etadi (orqaga qaytmaydi, harakat
# yo'nalishi saqlanadi), gapiradigan qahramon gapiradi (lab + jag'), tinglovchi og'zi yopiq, orqa fonda odamlar yurishda davom etadi,
# har birida bitta kamera harakati (qo'shnilarda takrorlanmaydi), hayajonli joylarda mimika batafsil.
KEEP = ("Continue exactly from the attached image: same place, same light, same characters in the same positions; every movement continues "
        "forward in the direction it already has in the image and never reverses, nobody walks back or re-enters the frame. "
        "Keep every character exactly as in the image for the whole clip, also when the camera comes closer: the same face, eyes, eyebrows, beard, age, hair, clothes and colours; "
        "Usta's doppi keeps its white arch embroidery; Diyor's hoodie stays dark navy blue and his cyan-blue glow stays only a thin outline, it never colours his body; "
        "Diyor keeps his round boyish face, big eyes and messy straight jet-black hair, never curly and never brown; Usta keeps his fuller face and short neat full black beard and never looks older or thinner. "
        "Exactly two arms, two hands and five fingers on each hand per person, young smooth hands; objects stay where they are unless the action moves them, nothing shrinks, melts or disappears. "
        "Background passers-by stay small, blurred and faceless and keep walking steadily in their own direction the whole clip; light drizzle and reflections on the wet pavement. "
        "Keep the painted illustration style, the cloudy light and the colours exactly as in the image. "
        "The character who speaks in this scene talks naturally for the whole clip: lips and jaw move as in real speech, with matching small head and hand gestures; "
        "everyone else keeps the mouth closed. The dialogue is spoken in Uzbek exactly as written below, in a natural Tashkent accent; no subtitles and no on-screen text. "
        "Clothes stay plain with no print or writing. No new people in focus, no extra objects, no brand logos on shoes, phones or bags, no text, no letters, no numbers on signs, cards, screens or timers, no watermark. Only quiet street or shop ambience.")
V = {
 1: ("Slow push-in from the wide shot in the image to a medium shot of Usta from the knees up, the pink banner still above him",
     "USTA SPEAKS to the camera with a calm, knowing half-smile, his raised index finger taps twice toward the pink banner, then he turns his eyes to the viewer and lifts one eyebrow. "
     "Behind him on the left the passers-by with umbrellas keep walking away down the street. The banner, the yellow card and the white card stay blank."),
 2: ("Handheld camera with a light natural bounce, slow push-in to a medium close-up of Diyor, keeping his whole upper body in frame",
     "DIYOR SPEAKS fast and excited: eyes wide and shining, eyebrows jumping up, a huge open grin, cheeks round; he jabs his pointing finger toward the pink banner twice, "
     "bounces once on his toes and shakes the phone in his other hand with joy. He stays in place in front of the window and does not walk away. People in the background keep walking."),
 3: ("Slow rack focus: starts on the back of Diyor's messy hair in the foreground, focus moves to Usta behind him and stays on Usta",
     "USTA SPEAKS quietly, arms still folded, he tilts his head a little, raises one eyebrow and gives a small knowing smile, as if asking a simple but sharp question. "
     "Diyor in the foreground stays still and silent, only his hair moves slightly. Through the glass door behind Usta the passers-by keep walking on the cloudy street."),
 4: ("Slow push-in on Diyor's face, ending in a close-up of his face with Usta still visible behind him",
     "DIYOR SPEAKS slowly and a little embarrassed: his smile is gone, his eyes look up and to the side, he swallows, his eyebrows draw together; "
     "he finishes pushing the phone into his jeans pocket and grips his backpack strap. Behind him Usta keeps his arms folded, mouth closed, and gives a slow small nod. "
     "Outside the window people keep walking."),
 5: ("Low-angle shot, slow crane up from the sneakers on the table to Usta's face above the pink tag",
     "USTA SPEAKS slowly, stressing each number with small nods: he lifts the blank pink tag a little higher with both hands like a lid, so the blank yellow card under it glows brighter; "
     "at the end, with a slightly amused smile, speed ramp: he lets the pink tag go and it falls flat onto the table in slow motion, landing with a soft slap, then normal speed resumes. "
     "Both cards stay blank. Shoppers in the background keep moving slowly."),
 6: ("Slow 60-degree orbit around Diyor from the left to the front, the violet mirror passing behind him",
     "DIYOR SPEAKS, confused and a little indignant: he taps each finger of his open hand with his other index finger, counting, then stops, tilts his head, "
     "raises one eyebrow high and opens his hands slightly as if asking «why?». His reflection in the mirror moves with him exactly. Shoppers in the background walk slowly."),
 7: ("Rack focus from the glowing pink timer on the counter in the foreground to Usta behind it, then a very slight push-in on Usta",
     "USTA SPEAKS calmly and warmly: he keeps his open palm toward the camera like «slow down», then slowly lowers the hand while still talking, with a soft reassuring smile. "
     "The timer only pulses with a soft pink glow, its screen stays blank with no digits. Blurred shoppers keep walking behind him."),
 8: ("Slow 30-degree arc to the right around Usta, ending in a medium shot with his raised hand and the three symbols above it",
     "USTA SPEAKS clearly, a short pause between three questions: he keeps exactly three fingers up; the yellow magnifying glass, the blue measuring tape and the pink question mark "
     "pulse brightly one after another, left to right, and with each pulse he gives a small firm nod; at the end he looks straight into the camera with a caring look. "
     "The symbols stay in place and have no letters. Through the glass door behind him people keep walking on the wet street."),
 9: ("Smooth tracking shot moving backward in front of Diyor as he walks out of the shop toward the camera, keeping him in a medium shot",
     "DIYOR SPEAKS, relaxed and pleased with himself: he keeps walking forward out of the door onto the wet sidewalk, never turning back to the shop; "
     "he finishes sliding the wallet into his hoodie pocket and lifts the phone with the plain calculator a little, with a clever smile and a confident small nod. "
     "The calculator screen shows no digits. Passers-by on the right keep walking."),
 10: ("Starts static, then a slow push-in on Usta and Diyor after the girl has walked out of the frame on the right",
      "The girl keeps walking forward to the right with calm steps and walks out of the frame on the right; she never turns around, never comes back and never looks at the men. "
      "Diyor's head slowly follows her, he stares dreamily with a love-struck goofy smile and soft wide eyes, forgetting the phone in his hand. "
      "Then USTA SPEAKS with a laugh and taps Diyor on the shoulder; Diyor startles, turns to Usta, his cheeks blush, and DIYOR SPEAKS fast and flustered, waving the phone; "
      "then USTA SPEAKS again, laughing, wagging his index finger at Diyor in a friendly scolding way, and Diyor scratches the back of his head with an embarrassed grin. "
      "Other passers-by keep walking in the background."),
 11: ("Very slow push-in on Usta's face, ending in a head-and-shoulders close-up (never closer than the whole face)",
      "USTA SPEAKS warmly to the camera: a calm wise smile, his eyes soften, he gives one slow nod on the last word. The yellow shop window light flickers gently on one side of his face; "
      "behind him the street lights glow and passers-by keep walking in the blur."),
 12: ("Slow dolly out and crane up, ending in a medium wide shot with the large cloudy sky filling the top third of the frame",
      "USTA SPEAKS to the viewer in a friendly inviting way, pushing the glowing phone a little toward the camera; the chat bubbles on the screen pulse softly and stay empty with no letters; "
      "his other hand gives Diyor's shoulder a friendly squeeze. Diyor smiles with his mouth closed, nods twice and pumps his thumb up. People keep walking in the background."),
}
CAMUZ = {1: "sekin yaqinlashish", 2: "qo'lda, yengil chayqalish + yaqinlashish", 3: "fokus ko'chishi: Diyor sochidan Ustaga", 4: "yuzga sekin yaqinlashish",
         5: "pastdan tepaga ko'tarilish + yorliq sekin tushadi", 6: "60° aylanish", 7: "fokus ko'chishi: taymerdan Ustaga", 8: "30° yoy",
         9: "orqaga yurib kuzatish (Diyor kameraga qarab yuradi)", 10: "qotib turadi, qiz chiqib ketgach ikkalasiga yaqinlashish", 11: "yuzga juda sekin yaqinlashish",
         12: "uzoqlashib ko'tarilish (tepada osmon)"}
DUR = {5: "ovoz ~7 s", 8: "ovoz ~9 s: montajda ~1.15x sekinlashadi", 10: "qayta yasang: oldingi klipda Veo Diyor sochini jingalak qildi; faqat qiz o'tib ketadigan 0–2.5 s olinadi, gaplar 10b va 10c da", 12: "ovoz ~9 s: ~1.15x"}
# 10-klipda (2026-10-27) Veo qizni orqaga qaytardi — 2.5 s dan keyingisi ishlatilmaydi. Hazil gaplari ikkita yangi klipga bo'lindi;
# boshlang'ich rasm: 10-klipning 2.2-soniyasi (qiz chiqib ketgan, Usta qo'li Diyor yelkasida) → img/s10b.png
# 10b/10c ning birinchi rasmi (10-klip kadri) xato chiqdi: Veo 10-klipda Diyor sochini jingalak, Usta yuzini ozg'in va qari qilgan edi.
# Yangi boshlang'ich rasm tasdiqlangan s10.png dan ChatGPT tahriri bilan olindi (qiz olib tashlangan), egasi 2026-10-27 yubordi → img/s10b.png ✅
EDIT10B = ("Edit the attached image of scene 10, vertical 9:16, medium shot. Keep everything exactly the same: the same street, the same cloudy evening light, the same coral pink and mint shop windows, "
  "the same camera framing and the same painted illustration style. Only one change: the girl in the atlas dress has already walked away. Remove her completely and fill her place with the "
  "continuing wet street, the trees and a few small, blurred, faceless passers-by walking away. "
  f"{U} stays exactly as in the image and as in the attached Usta reference image: the same fuller face, short neat full black beard, age about 30; his hand rests on Diyor's shoulder, "
  "a sly laughing smile, eyes crinkled. "
  f"{D} stays exactly as in the image and as in the attached Diyor reference image: round boyish face, big innocent eyes, messy straight jet-black hair (not curly, not brown), "
  "phone in his hand; he still gazes dreamily to the right where the girl went, with a love-struck goofy smile and slightly pink cheeks. "
  "Only three main colours: coral pink, mint green and night blue. "
  f"{HANDS} Exactly five fingers on each hand. Clothes plain with no print. No text, no letters, no numbers, no logos, no watermark.")
EXTRA = {10: [
 ("10b", "s10b", "ovoz ~6.5 s", "Usta: Hoy-hoy, Diyor! Sen do'konda chegirma qidiryapsanmi yoki ko'chada kelin? — Diyor: Yo'q, usta... men... hisoblayapman!",
  "ikkalasiga sekin yaqinlashish (beldan yuqori)",
  "Slow push-in from the two-shot in the image to a medium shot of Usta and Diyor from the waist up",
  "The girl has already left the frame on the right and never comes back; nobody new enters the frame. Diyor keeps gazing dreamily to the right with a goofy love-struck smile. "
  "USTA SPEAKS with a laugh: he leans toward Diyor, his hand on Diyor's shoulder gives two friendly pats, his eyes crinkle, eyebrows raised playfully, a wide teasing grin. "
  "Then Diyor startles, his head turns quickly from the right to Usta, eyes wide, cheeks blushing pink, and DIYOR SPEAKS fast and flustered, stammering, "
  "shaking his head and waving the phone in his hand; Usta keeps grinning with his mouth closed while Diyor talks. Passers-by keep walking in the background.",
  [("Usta", "USTA_V", "Hoy-hoy, Diyor! Sen do'konda chegirma qidiryapsanmi yoki ko'chada kelin?"), ("Diyor", "DIYOR_V", "Yo'q, usta... men... hisoblayapman!")]),
 ("10c", "s10b", "ovoz ~4 s", "Usta: Ko'zing narxda bo'lsin, ukam. Avval hisob, keyin kelin!",
  "chapga yoy bo'ylab Usta yuziga yaqinlashish (kulgan yuz)",
  "Slow arc to the left, ending in a medium close-up of Usta's laughing face, with Diyor's embarrassed face at the edge of the frame",
  "In the first second Diyor turns his head from the right to Usta, then looks down shyly. USTA SPEAKS, laughing warmly: eyes crinkled, cheeks lifted, a broad kind smile; "
  "he wags his index finger at Diyor in a friendly scolding way, then taps his own temple twice as if saying «think first». Diyor scratches the back of his head with an embarrassed grin, "
  "mouth closed, cheeks pink, eyes down. The girl never comes back. Passers-by keep walking in the background.",
  [("Usta", "USTA_V", "Ko'zing narxda bo'lsin, ukam. Avval hisob, keyin kelin!")]),
]}
FILE = {5: "s05.png (Nike belgisi tozalangan)"}
def vp(n):
    cam, act = V[n]
    return f"Vertical 9:16, 8 seconds. Start from the attached image of scene {n}. Camera: {cam}. Action: {act} {KEEP}"

# Egasi (2026-10-27): «matnni o'zbekcha ber Veo'ga» — Veo labni aynan shu so'zlarga moslashi uchun gap promptga o'zbekcha yoziladi.
# Ovozni baribir Manus'dagi dialog.wav dan qo'yamiz (seriyada ovozlar bir xil qolishi uchun); Veo ovozi faqat lab harakati uchun.
USTA_V = "a calm deep warm male voice of about 30-35"
DIYOR_V = "a lighter young male voice of about 22"
SAY = {
 1: [("Usta", USTA_V, "Bu yetmish foizlik chegirma yetmish foiz emas. To'lashdan oldin hisoblang.")],
 2: [("Diyor", DIYOR_V, "Usta, qarang! Uch yuz ming edi, bir yuz yetmish ming bo'libdi! Hozir olmasam, yutqazaman!")],
 3: [("Usta", USTA_V, "Bu narsani chegirmani ko'rishdan oldin ham qidirayotgan edingmi?")],
 4: [("Diyor", DIYOR_V, "Yo'q... Chegirmani ko'rib qoldim.")],
 5: [("Usta", USTA_V, "Hisoblaylik. Uch yuz mingdan bir yuz o'ttiz ming tushgan. Bu yetmish emas, qirq uch foiz.")],
 6: [("Diyor", DIYOR_V, "Unda nega yetmish deb yozishgan?")],
 7: [("Usta", USTA_V, "Katta raqam ko'zni, taymer qo'lni shoshiltiradi. Kerakli narsa shoshilishni talab qilmaydi.")],
 8: [("Usta", USTA_V, "Uchta tekshiruv. Boshqa do'kondagi narxi qancha? O'lchami, sifati, kafolati bir xilmi? Va shu mahsulot senga kecha ham kerakmidi?")],
 9: [("Diyor", DIYOR_V, "Demak, avval hisoblayman, keyin olaman.")],
 10: [("Usta", USTA_V, "Hoy-hoy, Diyor! Sen do'konda chegirma qidiryapsanmi yoki ko'chada kelin?"),
      ("Diyor", DIYOR_V, "Yo'q, usta... men... hisoblayapman!"),
      ("Usta", USTA_V, "Ko'zing narxda bo'lsin, ukam. Avval hisob, keyin kelin!")],
 11: [("Usta", USTA_V, "Xaridni foiz emas, ehtiyoj hal qilsin.")],
 12: [("Usta", USTA_V, "Chegirma yorlig'ini suratga olib botimizga yuboring: sahiychi shop bot. Haqiqiy foizni hisoblab, nimani tekshirishni aytib beradi.")],
}
def dial(n):
    return " ".join(f'{w} says in Uzbek, in {v}: "{t}"' for w, v, t in SAY[n])
def vp(n):
    cam, act = V[n]
    return f"Vertical 9:16, 8 seconds. Start from the attached image of scene {n}. Camera: {cam}. Action: {act} Dialogue: {dial(n)} {KEEP}"

# 10-sahna qayta (egasi, 2026-10-27: «qiz ko'rinmay qolgan»): eski klipda qiz 1 s da chiqib ketadi. Endi qizning alohida rasmi (ChatGPT)
# va Veo «Ingredients to video» (3 ta namuna: qiz, Usta, Diyor) bilan qiz ~5 s ko'rinadigan yangi klip.
GIRL_IMG = ("Vertical 9:16 character reference image, full body from head to shoes, standing, three-quarter view toward the viewer, "
  "on a plain soft light-grey studio background with nothing else in the image. A fictional young Uzbek woman of about 20-22 (an invented character, not a real person): "
  "long thick black hair in one long braid falling over her shoulder, a gentle oval face, warm brown eyes, a soft natural smile, light natural make-up. "
  "She wears a long modest Uzbek atlas (ikat) dress with long sleeves, the coral pink and mint green zigzag pattern exactly like the girl's dress in the attached scene image, "
  "a small white leather shoulder bag and simple flat shoes. The same painted illustration style as the attached scene image: semi-realistic cartoon painting, soft even light. "
  "Her face must look clearly different from the two men in the attached image. Exactly two arms and two hands, five fingers on each hand. "
  "Modest and family-friendly. No text, no letters, no logos, no watermark.")
GIRL_VEO = ("Vertical 9:16, 8 seconds. Use the three attached reference images: the GIRL in the atlas dress, USTA and DIYOR. "
  "Keep each of them exactly as in their own reference image for the whole clip: the same face, age, hair, clothes and colours; the girl's face stays clearly different from the men. "
  "Scene: a busy modern shopping street in Tashkent on a cloudy rainy evening, wet pavement with pink and mint reflections, bright coral pink and mint green shop windows on the left, "
  "small blurred faceless passers-by walking in the background, light drizzle. Painted semi-realistic cartoon illustration style; only three main colours: coral pink, mint green and night blue. "
  "Camera: starts on a medium-wide shot, then a slow pan to the right following the girl, and ends on a medium shot of Usta and Diyor. "
  "Action: Usta and Diyor stand side by side in front of the shop window on the left, Usta's hand resting on Diyor's shoulder, Diyor holds his phone. "
  "The girl enters from the left edge and walks slowly and calmly to the right along the sidewalk in front of them, seen in profile, her long braid swinging gently; "
  "she looks ahead, never looks at the men, never stops and never turns back; at about 5 seconds she walks out of the frame on the right and never comes back. "
  "Diyor's head slowly turns to follow her: his eyes go soft and wide, eyebrows raised, a goofy love-struck smile, cheeks turning pink, he forgets the phone in his hand. "
  "Usta notices, his eyes move from Diyor to the girl and back, and he gives a slow sly smile. Nobody speaks: all mouths stay closed, no dialogue. "
  "Diyor's hair stays messy straight jet-black, never curly or brown, with only a thin cyan-blue glow outline; Usta keeps his fuller face and short neat full black beard and never looks older or thinner; "
  "Usta's doppi keeps its white arch embroidery. Exactly two arms and five fingers on each hand per person. Clothes plain with no print or writing. "
  "No text, no letters, no logos, no subtitles, no watermark. Only quiet rainy street ambience.")
def ref(src, cap): return f'<figure class="ref"><img src="web/{src}.webp" alt="{e(cap)}"><figcaption>{e(cap)}</figcaption></figure>'

e = html.escape
cards = []
for n, t, voice, cols, scene in S:
    f = IMG[n][0][0]
    if n == 10:  # yangi 10-sahna: 1) qiz rasmi (ChatGPT), 2) Veo «Ingredients to video»
        cards.append(f"""<article class="card"><header><span class="num">10</span><h2>10-sahna, 1-qadam — qizning rasmi (ChatGPT), 9:16 (tik)</h2><span class="dur">yangi</span></header>
<div class="row"><div class="refs"><p class="rh">ChatGPT'ga biriktiring (yangi chat):</p>{ref("s10", "s10.png (ko'ylak va uslub uchun)")}</div>
<div class="txt"><span class="lbl">Nima uchun</span><p class="voice">Eski klipda qiz 1 soniyada chiqib ketadi, deyarli ko'rinmaydi. Avval qizning alohida rasmi yasaladi, keyin Veo'da uchala namuna bilan yangi klip.</p>
<pre id="g10">{e(GIRL_IMG)}</pre><button class="copy" data-t="g10">Nusxa olish</button></div></div></article>""")
        cards.append(f"""<article class="card"><header><span class="num">10</span><h2>10-sahna, 2-qadam — Veo «Ingredients to video», 9:16 (tik), 8 s</h2><span class="dur">2.4 s → ~6 s</span></header>
<div class="row"><div class="refs"><p class="rh">Veo'ga 3 ta rasm biriktiring:</p><p class="rh">1) 1-qadamdagi qiz rasmi</p>{ref("ref_usta", "ref_usta.png")}{ref("ref_diyor", "ref_diyor.png")}</div>
<div class="txt"><span class="lbl">Ovoz</span><p class="voice">Gap yo'q: qiz o'tib ketadi, Diyor qarab qoladi, Usta sezib jilmayadi. Keyin 10b sahnasi davom etadi.</p>
<span class="lbl">Kamera: o'ngga sekin burilib qizni kuzatish, oxiri Usta va Diyorda</span>
<pre id="v10">{e(GIRL_VEO)}</pre><button class="copy" data-t="v10">Nusxa olish</button></div></div></article>""")
        for k, f2, d2, voice2, camuz2, cam2, act2, say2 in EXTRA.get(n, []):
            dl = " ".join(f'{w} says in Uzbek, in {globals()[v]}: "{t2}"' for w, v, t2 in say2)
            pr = f"Vertical 9:16, 8 seconds. Start from the attached image. Camera: {cam2}. Action: {act2} Dialogue: {dl} {KEEP}"
            cards.append(f"""<article class="card"><header><span class="num">{k}</span><h2>{k}-sahna — 9:16 (tik), 8 s</h2><span class="dur">✅ klip bor</span></header>
<div class="row"><figure class="sc"><img src="web/{f2}.webp" alt="{k}-sahna rasmi"><figcaption>Veo'ga: s10b.png</figcaption></figure>
<div class="txt"><span class="lbl">Ovoz</span><p class="voice">{e(voice2)}</p>
<span class="lbl">Kamera: {e(camuz2)} · {e(d2)}</span>
<pre id="v{k}">{e(pr)}</pre><button class="copy" data-t="v{k}">Nusxa olish</button></div></div></article>""")
        continue
    cards.append(f"""<article class="card"><header><span class="num">{n:02d}</span><h2>{n}-sahna — 9:16 (tik), 8 s</h2><span class="dur">{t}</span></header>
<div class="row"><figure class="sc"><img src="web/{f}.webp" alt="{n}-sahna rasmi"><figcaption>Veo'ga: {e(FILE.get(n, f + ".png"))}</figcaption></figure>
<div class="txt"><span class="lbl">Ovoz</span><p class="voice">{e(voice)}</p>
<span class="lbl">Kamera: {e(CAMUZ[n])}{(" · " + e(DUR[n])) if n in DUR else ""}</span>
<pre id="v{n}">{e(vp(n))}</pre><button class="copy" data-t="v{n}">Nusxa olish</button></div></div></article>""")
    for k, f2, d2, voice2, camuz2, cam2, act2, say2 in EXTRA.get(n, []):
        dl = " ".join(f'{w} says in Uzbek, in {globals()[v]}: "{t2}"' for w, v, t2 in say2)
        pr = f"Vertical 9:16, 8 seconds. Start from the attached image. Camera: {cam2}. Action: {act2} Dialogue: {dl} {KEEP}"
        cards.append(f"""<article class="card"><header><span class="num">{k}</span><h2>{k}-sahna — 9:16 (tik), 8 s</h2><span class="dur">yangi</span></header>
<div class="row"><figure class="sc"><img src="web/{f2}.webp" alt="{k}-sahna rasmi"><figcaption>Veo'ga: s10b.png (✅ qizsiz, yuzlar namunadek)</figcaption></figure>
<div class="txt"><span class="lbl">Ovoz</span><p class="voice">{e(voice2)}</p>
<span class="lbl">Kamera: {e(camuz2)} · {e(d2)}</span>
<pre id="v{k}">{e(pr)}</pre><button class="copy" data-t="v{k}">Nusxa olish</button></div></div></article>""")

page = f"""<title>70 foiz chegirma sahnalari</title>
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
.sw-sky{{background:#5ab8f0}} .sw-coral{{background:#ff5e7e;color:var(--fg)}} .sw-mint{{background:#4fd6a0}} .sw-sun{{background:#ffe14d}} .sw-violet{{background:#9b7bff;color:var(--fg)}}
.sw-cyan{{background:var(--cyan)}} .sw-orange{{background:var(--orange)}} .sw-teal{{background:var(--teal)}}
.row{{display:grid;grid-template-columns:200px minmax(0,1fr);gap:16px;align-items:start}}
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
<h1>«70 foiz chegirma» <em>sahnalari</em></h1>
<p class="intro">12 ta rasm tayyor. Har sahna uchun: Veo'da «Frames to video» ni oching, chapdagi rasmni yuklang, o'lchamni 9:16 va 8 s qiling, «Nusxa olish» bilan promptni qo'ying. Har prompt rasmdan davom etadi: harakat orqaga qaytmaydi, gapirayotgan qahramonning labi qimirlaydi, orqadagi odamlar yurishda davom etadi. Raqam va yozuvlarni montajda o'zimiz qo'yamiz.</p>
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
open("video/chegirma/rasmlar.html", "w").write(page)
print(len(S), "sahna")
