# Video promptlari (rasm -> video, 9:16, 8 s) va sahnalar sahifasi
import html, os
from PIL import Image
KEEP_R = ("Keep THE ROBOT exactly as in the image for the whole clip: same polished chrome body, black visor with only two blue "
 "eye arcs and no mouth, orange glowing ear rings, gold infinity symbol on the chest and black doppi with white arch embroidery. "
 "Do not change its shape or colors.")
END = ("Vertical 9:16, 8 seconds, realistic cinematic motion, calm natural pace, the motion fills all 8 seconds. No text, no captions, "
 "no subtitles, no watermark, no logos, no new objects or people. No speech, no lip movement, no music, ambient sound only.")
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
]
def full(p): return p + " " + END
if __name__ == "__main__":
    md = ["# «Robot bilan bir piyola choy» — video promptlari (rasm → video, Veo / Kling / Vidu)", "",
          "Har bir klip 9:16, 8 s. Sahna vaqti qisqaroq bo'lsa, klipning bir qismi olinadi; uzunroq bo'lsa (4-sahna, 11 s) minterpolate bilan sekinlashtiriladi.", ""]
    cards = []
    for f, n, name, dur, voice, p in V:
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
