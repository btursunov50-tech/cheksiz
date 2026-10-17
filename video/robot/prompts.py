# 22 ta rasm prompti (9:16), namunalar: img/ref_robot.jpg, img/ref_odam.jpg
ROBOT = ("THE ROBOT: a friendly humanoid robot with a polished silver chrome body and smooth rounded shapes, a rounded helmet-like head "
 "with a large glossy black face visor showing ONLY two smooth glowing blue curved eye arcs like a gentle smile and no mouth, no other lights on the visor, round ear discs with warm orange "
 "glowing rings on both sides of the head, a small gold infinity symbol on the center of its chest, wearing a round black velvet doppi "
 "skullcap with a band of white embroidered arch patterns. It is NOT a skeleton and NOT a Terminator: no skull face, no red eyes, "
 "no other clothes unless this prompt says so.")
MAN = ("THE MAN: a fictional Uzbek man about 35 years old, short slightly wavy black hair, a short trimmed black stubble beard and moustache, "
 "kind tired brown eyes with smile lines, wearing a light-blue cotton shirt with an open collar and sleeves rolled up to the forearms, "
 "dark charcoal trousers, a small lavash shop owner, ordinary everyday look.")
CHOY = ("PLACE: an open wooden choyxona terrace at sunset, carved wooden pillars and railing, a hanging brass lantern, warm string-light bulbs, "
 "a large plane tree, in the far background a blue-domed madrasa and a tall brick minaret glowing against an orange sunset sky, a raised "
 "supa covered with red-and-navy patterned Uzbek carpets and cushions, a low carved wooden table with a blue-and-white Uzbek teapot, "
 "piyola tea bowls and a round golden patir non bread with sesame.")
SHOP = ("PLACE: a small busy lavash fast-food shop in an Uzbek city in the evening, steel counter, a cash register, a menu board without readable text, "
 "warm light.")
KITCHEN = ("PLACE: the kitchen table of the same small lavash shop, stainless steel surface, containers of sliced meat, tomatoes, cucumbers and "
 "a squeeze bottle of white garlic sauce.")
COOK = "THE COOK: a young Uzbek cook about 20 with short black hair, a white cotton cap, a plain white T-shirt under a white apron, thin black nitrile gloves."
STYLE = ("Photorealistic cinematic film still, vertical 9:16, shot on 35mm, shallow depth of field, warm golden light, gentle teal-and-amber "
 "color grade, natural skin texture, realistic chrome reflections.")
KEEP = {"ref_odam + 06_sousiz": "Keep THE MAN exactly as in the first attached reference image (same face, same age about 35, same slim face shape, same neat slightly wavy hair, beard, light-blue shirt and trousers; do not make him older or heavier) and THE COOK exactly as in the second attached image (same face, white cap, white T-shirt, white apron, black gloves).",
 "11_maktab": "The student is the same boy as in the attached image, now grown up: same face shape, eyes and black hair.",
 "06_sousiz": "Keep THE COOK and the kitchen exactly as in the attached image: same face, cap, T-shirt, apron, black gloves, steel table and food containers.",
 "ref_robot": "Keep THE ROBOT exactly as in the attached reference image: same chrome body, visor with only two smooth blue eye arcs and no mouth, orange ear rings, gold infinity symbol and doppi.",
 "ref_odam": "Keep THE MAN exactly as in the attached reference image: same face, hair, beard, light-blue shirt and trousers.",
 "ref_robot + ref_odam": "Keep THE ROBOT and THE MAN exactly as in the two attached reference images: the robot's chrome body, visor with only two smooth blue eye arcs and no mouth, orange ear rings, gold infinity symbol and doppi; the man's face, hair, beard, light-blue shirt and trousers."}
END = "No text, no letters, no logos, no watermark, no subtitles."

R, M, B = "ref_robot", "ref_odam", "ref_robot + ref_odam"
S = [
 ("Robot choy ichadi", "0–8 s", "Do'koningdan har kuni pul oqib ketyapti. Sen esa buni ko'rmaysan.", R,
  "Close-up of THE ROBOT sitting cross-legged on the supa, holding a piyola of tea with both hands near its visor as if about to sip, steam rising from the tea, calm mysterious mood.", [ROBOT, CHOY]),
 ("Odam telefonda", "8–13 s", "Qanaqa pul? Men seni faqat rasm va video uchun ishlataman.", B,
  "Medium shot of THE MAN sitting on the supa looking down at his smartphone with a careless half-smile, THE ROBOT out of focus in the foreground on the right edge of the frame.", [MAN, ROBOT, CHOY]),
 ("Robot kinoya bilan", "13–16 s", "Rasm yaxshi. Lekin meni rasm uchun o'ylab topishmagan.", R,
  "Medium close-up of THE ROBOT tilting its head slightly to one side, holding the piyola on its knee, a gentle ironic friendly look.", [ROBOT, CHOY]),
 ("1956 olimlar", "16–27 s", "1956-yili olimlar so'rashdi: mashina odamning aqliy ishini qila oladimi?", "namuna kerak emas",
  "Black-and-white 1950s documentary-style photo: a group of scientists in suits and thin ties standing around a large early room-sized computer with reels of magnetic tape and blinking panels, one of them writing equations on a chalkboard.", "BW"),
 ("Do'konda kassa", "28–35 s", "Sen kun bo'yi kassaga, telefonga, mijozga qaraysan. Oshpaz stoliga esa hech kim qaramaydi.", "ref_odam + 06_sousiz",
  "THE MAN stands behind the counter, busy and distracted, holding his phone to his ear with one hand and with the other hand holding a small card payment terminal toward a customer who taps a bank card, his eyes on the short queue with a slightly tired but kind face, not angry, not looking at the camera, no cash and no banknotes anywhere, in the blurred background THE COOK wraps lavash at a kitchen table that nobody is watching.", [MAN, COOK, SHOP]),
 ("Sousiz lavash", "35–41 s", "Bitta lavash sousiz ketdi. Mijoz indamadi. Lekin qaytib kelmadi.", "namuna kerak emas",
  "Close-up of THE COOK's gloved hands wrapping a lavash with meat and vegetables but no sauce, the squeeze bottle of white garlic sauce standing untouched, in the soft background a customer walking out of the door with a paper-wrapped lavash.", [COOK, KITCHEN]),
 ("Odam o'ylanadi", "42–48 s", "Nazoratchi yollaymanmi? Unga oylik kerak.", M,
  "Close-up of THE MAN on the supa rubbing his beard with one hand, thinking hard, worried eyes, a piyola of tea in front of him.", [MAN, CHOY]),
 ("Kamera", "48–55 s", "Bitta kichik kamera. U faqat stolni ko'radi. Go'sht, sabzavot, sous.", "06_sousiz",
  "Low-angle close-up looking up at a small white dome camera mounted on a short steel bracket on the ceiling directly above the kitchen table, its lens pointing straight down at the table, the camera sharp in the upper half of the frame; below it, out of focus, the steel table with meat, vegetables, the sauce bottle and THE COOK's gloved hands working. A clearly different angle from a normal view of the cook, the camera is the hero of the shot, empty space at the top for overlays.", [COOK, KITCHEN]),
 ("Xato ushlandi", "55–59 s", "To'xtang. Sous hali qo'shilmadi.", "06_sousiz",
  "Top-down view from the ceiling camera onto the stainless steel table: an open lavash with meat, tomatoes and cucumbers but no sauce, THE COOK's gloved hands frozen just before wrapping it, the squeeze bottle of white garlic sauce beside it, slight wide-angle security-camera look.", [COOK, KITCHEN]),
 ("Ikkalasi supada", "60–70 s", "Faqat lavash uchunmi? / Yo'q. Eng qimmat ish qo'l bilan emas, bosh bilan qilinadi.", B,
  "Two-shot on the supa: THE MAN on the left leaning forward curiously, THE ROBOT on the right putting its piyola down on the low table and raising one finger as if starting an important explanation. Both the same human size.", [MAN, ROBOT, CHOY]),
 ("Shifokor yo'li: maktab", "71–80 s", "Avval tug'ilishi kerak. Keyin maktab.", "namuna kerak emas",
  "Warm nostalgic scene: an Uzbek schoolboy about 9 years old in a white shirt sitting at a wooden school desk in a sunny classroom, reading a large illustrated book about the human body, a toy stethoscope next to him.", []),
 ("Shifokor yo'li: institut", "80–85 s", "Keyin institut. Keyin yillar davomida amaliyot.", "11_maktab",
  "A young Uzbek medical student about 21 years old, clean-shaven with no beard and no stubble, short neat black hair, slim youthful face, in a white coat, studying late at night at a desk with tall stacks of thick medical books and an anatomy model, a desk lamp glowing, a wall clock showing a late hour, tired but determined. Through the window: a quiet Uzbek city at night with low apartment blocks and a few lit windows, no skyscrapers.", []),
 ("Qabulda", "85–96 s", "Sen esa uning oldiga yigirma daqiqaga kirasan. Va o'sha yillarning hammasi uchun to'laysan.", "namuna kerak emas",
  "A modest doctor's office: an experienced Uzbek doctor about 55 in a white coat listening to a patient across a desk, a large round wall clock clearly visible between them, a feeling of limited time.", []),
 ("Odam so'raydi", "97–99 s", "AI-shifokor arzonroqmi?", M,
  "Medium close-up of THE MAN on the supa raising his eyebrows with a curious hopeful look, holding a piyola halfway to his mouth.", [MAN, CHOY]),
 ("Robot-shifokor", "99–109 s", "Men tahlilingni oddiy tilda tushuntiraman... Kechasi soat uchda ham.", R,
  "Night scene in a cozy Uzbek apartment, a window with city lights, a wall clock showing 3 o'clock. THE ROBOT wears a white doctor's coat over its chrome body (the doppi stays on its head) and holds a smartphone showing blurred lab result charts, explaining gently, warm lamp light.", [ROBOT]),
 ("Shartnoma", "110–118 s", "Shartnoma qoralamasi... Ijara shartnomasida yashirin jarimani topish.", R,
  "Close-up of a printed rental contract lying on the low carved choyxona table next to a piyola and a pen, THE ROBOT's chrome finger pointing at one paragraph, the paragraph softly highlighted in yellow light, the printed lines blurred and unreadable.", [ROBOT, CHOY]),
 ("Odam hayron", "118–122 s", "Unda shifokor bilan yurist kerak emasmi?", M,
  "Medium shot of THE MAN on the supa leaning back in surprise, open palms raised, puzzled expression.", [MAN, CHOY]),
 ("Robot jiddiy", "122–133 s", "Kerak. Mening javoblarimni kimdir tekshirishi kerak...", R,
  "Close-up of THE ROBOT, serious and honest, for this shot only its blue eye arcs are flat straight lines, slightly dimmed, not smiling, one chrome hand resting on the table next to the teapot.", [ROBOT, CHOY]),
 ("Odam ehtiyot", "134–138 s", "Telefonimga, pullarimga kirib olmaysanmi?", B,
  "Close-up of THE MAN on the supa pulling his smartphone toward his chest with both hands, giving a suspicious cautious look toward THE ROBOT, who is out of focus at the edge of the frame.", [MAN, ROBOT, CHOY]),
 ("Robot va'da", "138–144 s", "Men parol so'ramayman. Parolingni so'ragan «AI»dan qoch. U AI emas, firibgar.", R,
  "Medium shot of THE ROBOT placing its right chrome hand on its chest over the gold infinity symbol, a sincere promise gesture, THE MAN's shoulder in light-blue shirt out of focus in the foreground.", [ROBOT, CHOY]),
 ("Kulgu", "144–153 s", "Unda oshpazni bo'shatamanmi? / Yo'q. Men lavash o'ray olmayman. Oshpaz qo'l, men ko'z.", B,
  "Wide shot of THE MAN and THE ROBOT on the supa laughing together, THE ROBOT holding up an empty open hand as if saying it cannot cook, THE MAN pouring tea from the blue-and-white teapot into the robot's piyola, warm friendly mood. Both the same human size.", [MAN, ROBOT, CHOY]),
 ("Kameraga", "153–157 s", "Sizda ham do'kon bormi? Izohga «LAVASH AI» deb yozing.", B,
  "THE ROBOT turns and looks straight into the camera with a friendly open-hand gesture toward the viewer, THE MAN smiling softly out of focus behind it, centered composition with empty space at the bottom for text.", [ROBOT, MAN, CHOY]),
]
def prompt(s):
    name, t, voice, ref, act, parts = s
    keep = [KEEP[ref]] if ref in KEEP else []
    if parts == "BW":
        return " ".join([act, "Authentic black-and-white archival photograph, vertical 9:16, heavy film grain, soft focus edges, 1950s vintage look, no color.", END])
    out = " ".join([act] + parts + [STYLE] + keep + [END])
    if name == "Robot jiddiy":
        out = out.replace("two smooth glowing blue curved eye arcs like a gentle smile", "two glowing blue eyes")
        out = out.replace("visor with only two smooth blue eye arcs and no mouth", "visor with only two blue eyes and no mouth")
    return out
if __name__ == "__main__":
    out = ["# «Robot bilan bir piyola choy» — 22 ta rasm prompti (ChatGPT, 9:16)", "",
           "Namunalar: `img/ref_robot.jpg`, `img/ref_odam.jpg` (har promptda qaysini biriktirish yozilgan). Ovoz: `dialog.flac` (157.5 s), vaqtlar taxminiy.", ""]
    for i, s in enumerate(S, 1):
        out += [f"## {i}. {s[0]} — 9:16 (tik), {s[1]}", f"Ovoz: {s[2]}", f"Biriktiring: {s[3]}", "", "```", prompt(s), "```", ""]
    open("video/robot/PROMPTS.md", "w").write("\n".join(out))
