# Video promptlari (rasm -> video, 9:16, 8 s) va sahnalar sahifasi
import html, os
from PIL import Image
KEEP_R = ("Keep THE ROBOT exactly as in the image for the whole clip: same polished chrome body, black visor with only two blue "
 "eye arcs and no mouth, orange glowing ear rings, gold infinity symbol on the chest and black doppi with white arch embroidery. "
 "Do not change its shape or colors.")
KEEP_M = ("Keep THE MAN exactly as in the image for the whole clip: same face, hair, beard, light-blue shirt and dark trousers. "
 "He does not speak, his mouth stays closed.")
END = ("Vertical 9:16, 8 seconds, realistic cinematic motion, calm natural pace, the motion fills all 8 seconds. No text, no captions, "
 "no subtitles, no watermark, no logos, no new objects or people, no fire or flames, no lightning, no sparks, no flashes of light, no comic speed lines, no smoke. No speech, no lip movement, no music, ambient sound only.")
V = [
 ("01_choy", 1, "Robot choy ichadi", "8 s", "Do'koningdan har kuni pul oqib ketyapti. Sen esa buni ko'rmaysan.",
  "Animate this image. Slow gentle push-in toward THE ROBOT. The robot slowly lifts the piyola closer to its visor as if sipping tea, then lowers it a little; steam keeps curling up from the tea; its blue eye arcs blink once softly. String lights twinkle, plane tree leaves sway in a light breeze, the lantern glows, the sunset sky and the madrasa stay unchanged. " + KEEP_R),
 ("03_kinoya", 3, "Robot kinoya bilan", "3 s", "Rasm yaxshi. Lekin meni rasm uchun o'ylab topishmagan.",
  "Animate this image. Very slow push-in. THE ROBOT slowly tilts its head a little more to one side in a friendly ironic way, its blue eye arcs blink once, the hand holding the piyola rests on its knee, steam rises from the tea. Leaves and string lights move gently. " + KEEP_R),
 ("04_olimlar", 4, "1956 olimlar", "11 s", "1956-yili olimlar so'rashdi: mashina odamning aqliy ishini qila oladimi?",
  "Animate this black-and-white archival photo. The scientist at the chalkboard keeps writing with chalk, the seated men watch and one nods slowly, the man with the notebook writes; the tape reels on the computer cabinets turn slowly and small panel lights blink. Subtle film grain, slight flicker and a gentle handheld documentary camera drift. The whole clip stays black-and-white. The chalk marks stay abstract scribbles, never readable letters. Keep every person's face and clothes as in the image."),
 ("05_kassa", 5, "Do'konda kassa", "7 s", "Sen kun bo'yi kassaga, telefonga, mijozga qaraysan. Oshpaz stoliga esa hech kim qaramaydi.",
  "Animate this image. Slight handheld camera. THE MAN listens to his phone with a tired, busy look, holding the card terminal while the customer taps the bank card, then he glances at the queue. In the background THE COOK keeps wrapping lavash and nobody watches him. Keep THE MAN exactly as in the image for the whole clip: same face, neat black hair, short black beard and light-blue shirt; keep THE COOK the same. The man does not speak, his mouth stays closed."),
 ("06_sousiz", 6, "Sousiz lavash", "6 s", "Bitta lavash sousiz ketdi. Mijoz indamadi. Lekin qaytib kelmadi.",
  "Animate this image. Steady camera with a slight push-in on the hands. THE COOK wraps the lavash with meat and vegetables without adding any sauce; the white sauce bottle stays untouched on the counter. In the background the customer walks out of the door with the paper-wrapped lavash. Keep THE COOK exactly as in the image for the whole clip: same face, white cap, white T-shirt, white apron and black gloves."),
 ("02_telefon", 2, "Yigit telefonda", "5 s", "Qanaqa pul? Men seni faqat rasm va video uchun ishlataman.",
  "Animate this image. Almost static camera with a very slight drift. THE MAN scrolls his phone with his thumb and keeps a careless half-smile. In the blurred foreground THE ROBOT slowly turns its head a little toward the man and its blue eye arcs blink once. Leaves and string lights move gently. No steam, no smoke and no fog anywhere in the frame; the man's face and hair stay sharp and fully visible for the whole clip. " + KEEP_M + " " + KEEP_R),
 ("07_oylanadi", 7, "Yigit o'ylanadi", "6 s", "Nazoratchi yollaymanmi? Unga oylik kerak.",
  "Animate this image. Very slow push-in toward THE MAN's face. He slowly rubs his chin and beard with his hand, thinking hard, his worried eyes move slightly to the side and back, he exhales calmly. Steam rises from the piyola, leaves and string lights move gently, the sunset stays unchanged. " + KEEP_M),
 ("08_kamera", 8, "Kamera", "7 s", "Bitta kichik kamera. U faqat stolni ko'radi. Go'sht, sabzavot, sous.",
  "Animate this image. Slow push-in toward the white dome camera on the ceiling. A tiny red light on the camera body blinks steadily, the lens inside the dome turns slightly and points straight down at the table. Below, out of focus, THE COOK keeps arranging meat, tomatoes and cucumbers on the lavash with his gloved hands; the sauce bottle stays untouched. Keep THE COOK, the camera and the kitchen exactly as in the image for the whole clip."),
 ("09_xato", 9, "Xato ushlandi", "4 s", "To'xtang. Sous hali qo'shilmadi.",
  "Animate this image. Fixed top-down security-camera view, the camera does not move. THE COOK's gloved hands start to fold the lavash, then stop and freeze in place just before wrapping it, as if he suddenly noticed something; the white sauce bottle stays on the counter. Slight wide-angle security-camera look. Keep THE COOK, the lavash and the food exactly as in the image for the whole clip; the lavash has no sauce on it."),
 ("10_ikkalasi", 10, "Ikkalasi supada", "10 s", "Faqat lavash uchunmi? / Yo'q. Eng qimmat ish qo'l bilan emas, bosh bilan qilinadi.",
  "Animate this image. Slow gentle push-in on both characters. THE ROBOT keeps its raised chrome index finger up and moves it slightly as if starting an important explanation, its other hand rests near the piyola on the table, its blue eye arcs blink once. THE MAN leans a little forward with a curious smile and listens. Leaves and string lights move gently. No steam, no smoke and no fog anywhere in the frame; both faces stay sharp and fully visible for the whole clip. " + KEEP_M + " " + KEEP_R),
 ("11_maktab", 11, "Shifokor yo'li: maktab", "9 s", "Avval tug'ilishi kerak. Keyin maktab.",
  "Animate this image. Slow gentle push-in toward the boy. The boy, resting his cheek on his hand, slowly moves his finger across the illustration of the heart in the big anatomy book and smiles a little with curiosity, then turns his eyes to the next picture. Warm sunbeams come through the window and tiny dust particles float in the light; the classmates in the blurred background move slightly at their desks. Keep the boy exactly as in the image for the whole clip: same face, black hair and white school shirt. The book pages stay as pictures with no readable letters. The boy does not speak."),
 ("12_institut", 12, "Shifokor yo'li: institut", "5 s", "Keyin institut. Keyin yillar davomida amaliyot.",
  "Animate this image. Slow push-in toward the student. The tired young medical student keeps writing notes with his pen, then rubs his eyes with one hand and turns a page of the thick medical book, still determined. The desk lamp glow flickers very slightly, the wall clock's minute hand moves a little, the night city lights twinkle outside the window. Keep the student exactly as in the image for the whole clip: same young clean-shaven face, short black hair and white coat. The book pages stay as pictures with no readable letters. He does not speak."),
 ("13_qabul", 13, "Qabulda", "11 s", "Sen esa uning oldiga yigirma daqiqaga kirasan. Va o'sha yillarning hammasi uchun to'laysan.",
  "Animate this image. Slow push-in toward the doctor. The experienced doctor listens carefully to the elderly patient, nods slowly and writes a few words on the clipboard; the patient seen from behind moves his hands a little while talking. The minute hand of the large wall clock moves forward noticeably, a feeling of limited time. Keep the doctor and the patient exactly as in the image for the whole clip: same faces, grey hair and beard, white coat and clothes. Nobody's lips move."),
 ("14_soraydi", 14, "Yigit so'raydi", "3 s", "AI-shifokor arzonroqmi?",
  "Animate this image. Very slow push-in toward THE MAN. He holds the piyola near his mouth, raises his eyebrows with a curious hopeful look toward the robot off-screen, then lowers the piyola a little and waits for an answer. Leaves and string lights move gently, the sunset stays unchanged. " + KEEP_M),
 ("15_robot_shifokor", 15, "Robot-shifokor", "10 s", "Men tahlilingni oddiy tilda tushuntiraman. Shifokorga qanday savol berishni aytaman. Kechasi soat uchda ham.",
  "Animate this image. Slow push-in toward THE ROBOT. THE ROBOT in its white doctor's coat holds the smartphone with the lab charts toward the man and gently gestures with its open other hand as if explaining step by step, its blue eye arcs blink once. In the foreground THE MAN, seen from behind, listens and slowly nods with his hand on his chin. The wall clock stays at 3 o'clock, the night city lights twinkle in the window, the lamp glows warmly. The phone screen shows only blurred charts with no readable text. " + KEEP_R + " The white coat and stethoscope stay the same."),
 ("16_shartnoma", 16, "Shartnoma", "8 s", "Shartnoma qoralamasi. Qiyin so'zlarni tushuntirish. Ijara shartnomasida yashirin jarimani topish. Bir necha daqiqada.",
  "Animate this image. Slow push-in toward the contract. THE ROBOT's chrome finger slowly slides along the highlighted paragraph and stops on it, the yellow highlight glows a little brighter. THE MAN leans closer with his hand on his chin and nods slowly as he understands. Steam rises gently from the piyola, the sunset stays unchanged. The printed lines stay blurred and unreadable, no letters. " + KEEP_M + " " + KEEP_R),
 ("17_hayron", 17, "Yigit hayron", "2 s", "Unda shifokor bilan yurist kerak emasmi?",
  "Animate this image. Almost static camera. THE MAN leans back in surprise with his open palms raised, shrugs a little and looks at the robot with a puzzled expression. In the blurred foreground the robot's chrome arm moves slightly. Leaves and string lights move gently. " + KEEP_M + " " + KEEP_R),
 ("18_jiddiy", 18, "Robot jiddiy", "11 s", "Kerak. Mening javoblarimni kimdir tekshirishi kerak. Ayniqsa ish murakkab bo'lsa. Yoki xato juda qimmat bo'lsa.",
  "Animate this image. Very slow push-in toward THE ROBOT's face. THE ROBOT sits still and serious, its flat blue eye lines glow steadily and dim slightly once, it nods slowly one time, its chrome hand stays resting on the table next to the teapot. Steam rises gently from the piyola, string lights and leaves move softly, the sunset stays unchanged. Keep THE ROBOT exactly as in the image for the whole clip: same polished chrome body, black visor with only two flat blue eye lines and no mouth, orange glowing ear rings, gold infinity symbol on the chest and black doppi with white arch embroidery. Do not change its shape or colors."),
 ("19_ehtiyot", 19, "Yigit ehtiyot", "7 s", "Kamera, tahlillar, shartnomalar... Telefonimga, pullarimga kirib olmaysanmi?",
  "Animate this image. Handheld camera with a subtle nervous drift, staying on THE MAN at the same distance. He holds his smartphone tighter against his chest with both hands, glances suspiciously at the robot and narrows his eyes a little. In the blurred foreground the robot's head stays still and its orange ear ring glows softly. Leaves and string lights move gently. " + KEEP_M + " " + KEEP_R),
 ("20_vada", 20, "Robot va'da", "6 s", "Men parol so'ramayman. Parolingni so'ragan «AI»dan qoch. U AI emas, firibgar.",
  "Animate this image. Slow 20-degree orbit around THE ROBOT from left to right, ending on a frontal medium close-up of the robot. THE ROBOT keeps its right chrome hand flat on its chest just below the gold infinity symbol, tilts its head slightly forward in a sincere promise, its blue eye arcs blink once. The gold infinity symbol stays fully visible, clean and not bent for the whole clip. THE MAN's shoulder in the blurred foreground moves slightly. Leaves and string lights move gently. " + KEEP_R),
 ("21_kulgu", 21, "Kulgu", "7 s", "Unda oshpazni bo'shatamanmi? / Yo'q. Men lavash o'ray olmayman. Oshpaz qo'l, men ko'z.",
  "Animate this image. Slow pull-back that ends on a wide shot of both characters at the table. THE MAN laughs warmly while pouring tea from the blue-and-white teapot into the piyola that THE ROBOT holds out; the tea stream flows naturally into the bowl. THE ROBOT raises its other open hand as if saying it cannot cook, its blue eye arcs blink happily. Leaves and string lights move gently, the sunset glows. " + KEEP_M + " " + KEEP_R),
 ("22_kameraga", 22, "Kameraga", "5 s", "Sizda ham do'kon bormi? (ekranda: Botdan so'rang: @sahiychishopbot · Do'koningizga AI qanday yordam beradi?)",
  "Animate this image. Slow push-in toward THE ROBOT. THE ROBOT looks straight into the camera and moves its open chrome hand toward the viewer in a friendly inviting gesture, its blue eye arcs blink once. THE MAN in the blurred background smiles and lifts his piyola a little. Leaves and string lights move gently, the sunset glows. Keep the empty space at the top and bottom of the frame clear for on-screen text. " + KEEP_R),
]
def full(p): return p + " " + END
if __name__ == "__main__":
    md = ["# «Robot bilan bir piyola choy» — video promptlari (rasm → video, Veo / Kling / Vidu)", "",
          "Har bir klip 9:16, 8 s. Sahna vaqti qisqaroq bo'lsa, klipning bir qismi olinadi; uzunroq bo'lsa (4-sahna, 11 s) minterpolate bilan sekinlashtiriladi.", ""]
    cards = []
    for f, n, name, dur, voice, p in sorted(V, key=lambda v: v[1]):
        im = Image.open(f"video/robot/img/{f}.jpg"); im.thumbnail((600, 1100)); im.save(f"video/robot/web/{f}.webp", quality=82)
        md += [f"## {n}. {name} — 9:16 (tik), 8 s (sahna {dur})", f"Rasm: `img/{f}.jpg`", f"Ovoz: {voice}", "", "```", full(p), "```", ""]
        e = html.escape
        cards.append(f'''<article class="card" id="s{n}">
<div class="media"><img src="web/{f}.webp" alt="{n}-sahna: {e(name)}" loading="lazy"></div>
<div class="txt">
<header><span class="num">{n}</span><h2>{e(name)}</h2><span class="dur">9:16 · 8 s</span><span class="dur">sahna {dur}</span></header>
<p class="voice"><span class="lbl">Ovoz</span>{e(voice)}</p>
<p class="lbl">Video prompti (Veo / Kling / Vidu)</p>
<pre id="p{n}">{e(full(p))}</pre>
<button type="button" class="copy" data-t="p{n}">Nusxa olish</button>
</div></article>''')
    open("video/robot/VIDEO.md", "w").write("\n".join(md))
    page = open("video/robot/page_head.html").read() + "\n".join(cards) + open("video/robot/page_tail.html").read()
    open("video/robot/sahnalar.html", "w").write(page)
