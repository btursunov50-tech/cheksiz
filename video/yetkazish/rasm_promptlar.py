# «Bepul yetkazish» — sahna rasmlari uchun ChatGPT promptlari (9:16) → rasmlar.html (Artifact sahifa, nusxa tugmasi, namuna rasmlar yonida).
# Qahramonlar o'sha Usta va Diyor (img/ref_*.png). Har kadrda 2–3 asosiy rang (Kalamushqir ranglari: sariq, ko'k, qizil; egasi qoidasi, 2026-10-26).
# Joy: oldingi ko'cha va do'kondan farqli — eski Toshkent hovlisidagi choyxona supasi, oqshom, tok ostida iliq chiroqlar.
# Tarix sahnalari (2002 ofis, ombor, xarita, shokolad) — 2000-yillar boshi rangi, yuzlar ko'rinmaydi (haqiqiy shaxs yo'q).
# Ishlatish: python3 video/yetkazish/rasm_promptlar.py
import html, os
D = os.path.dirname(os.path.abspath(__file__))
U = ("USTA (the calm man about 30 years old with a fuller face and a short neat full jet-black beard, a black Uzbek doppi skullcap with white arch embroidery, "
     "a dark embroidered chapan robe with a red sash; young strong hands of a 30-year-old man, smooth skin)")
Dy = ("DIYOR (the naive guy about 20 years old with a round boyish face, big innocent eyes, messy straight jet-black hair (never curly, never brown), "
      "a dark navy blue hoodie, a black backpack, jeans and sneakers, outlined only by a thin soft cyan-blue glow)")
HANDS = "Every person has exactly two arms and two hands, five fingers on each hand, every hand clearly belongs to its own arm."
PLACE = ("a cozy courtyard tea terrace in old Tashkent at dusk: a wooden topchan (raised platform) covered with a deep red carpet and cushions, a low table with a blue-and-white teapot and small piyola cups, "
         "a grapevine pergola overhead with warm yellow string lights, whitewashed walls and a carved wooden door, a deep blue evening sky")
COL = {"amber": "warm amber yellow", "blue": "deep evening blue", "red": "rich red", "teal": "deep teal", "white": "clean soft white", "green": "fresh green", "grey": "cool grey"}
def sty(cols, old=False, refs=True):
    c = ", ".join(COL[k] for k in cols[:-1]) + " and " + COL[cols[-1]]
    look = ("an early-2000s memory come to life: slightly faded colours, soft film grain, gentle glow" if old else
            "cinematic warm evening light, colourful and eye-catching")
    src = "the same hand-painted semi-realistic cartoon illustration style as the attached reference images" if refs else "a hand-painted semi-realistic cartoon illustration style"
    return (f"Style: {src} (painterly, visible brush texture), {look}. "
            f"Colour rule: the whole frame uses ONLY {len(cols)} main colours: {c}; everything else is soft dark neutral shadow. "
            "Vertical 9:16. No text, no letters, no numbers, no logos, no brand names, no watermark, no subtitles.")
REF = {"u": ("Usta", "ref_usta"), "d": ("Diyor", "ref_diyor"),}
def att(r):
    if not r: return "No reference images are needed for this image; it shows no main characters. "
    n = " and ".join(REF[k][0] for k in r)
    return (f"Attach the reference image{'s' if len(r) > 1 else ''} of {n}. Keep {'each character' if len(r) > 1 else 'the character'} exactly as in "
            f"{'their reference images' if len(r) > 1 else 'the reference image'}: the same face, age, hair, beard, clothes and colours. ")
# (raqam, ovoz qatori, plan, ranglar, namunalar, eski uslubmi, sahna)
S = [
 ("1", "Usta: «Bepul yetkazish bepul emas. Uning pulini baribir to'laysan.»", "Close-up, head and shoulders, slight push-in framing", ["amber", "blue", "red"], "ud", False,
  f"{PLACE}. {U} sits on the topchan in the foreground and looks straight into the camera with a calm, knowing half-smile, one eyebrow slightly raised, as if about to reveal a secret. "
  f"Behind him, softly out of focus, {Dy} sits cross-legged on the red carpet, bent over his smartphone, its screen lighting his face blue."),
 ("2", "Diyor: «Usta, shampun oldim, yetkazish yigirma ming ekan… bepul bo'larkan!»", "Medium close-up, slightly low angle", ["amber", "blue"], "d", False,
  f"{PLACE}, softly blurred behind. {Dy} holds his smartphone up toward the viewer with one hand, excited, eyes bright, eyebrows raised, a big eager grin; "
  "his other hand points at the screen. The screen shows a simple online shopping cart: two product cards with small pictures (a shampoo bottle and a box) and an empty blue button, no letters or numbers."),
 ("3", "Usta: «O'sha qirq minglik narsa senga kerakmi?» — Diyor: «Unchalik emas… lekin bepul-ku!»", "Over-the-shoulder medium close-up: Diyor's shoulder and messy hair blurred in the foreground, focus on Usta", ["amber", "red"], "ud", False,
  f"{PLACE}. {U} pours tea into a piyola and looks at Diyor over it with one eyebrow raised high and a small amused smile, head tilted a little, asking a simple sharp question. "
  f"{Dy} is seen from behind, only his shoulder, hood and the back of his head in the foreground, out of focus."),
 ("4", "Usta: «Jim, Diyor. Qara. 2002-yil, Amerika.»", "Medium shot", ["amber", "blue", "grey"], "u", False,
  f"{U} on the topchan raises his open palm calmly like «be quiet and watch». Behind him the warm courtyard dissolves from right to left into an early-2000s American office: "
  "rows of desks with bulky old CRT computer monitors, cardboard boxes stacked high, cool grey-blue office light, the old part softly grainy like an old video."),
 ("5", "Usta: «Dunyodagi eng katta onlayn do'kon bepul yetkazishni 99 dollardan 49 dollarga, ikki oydan keyin 25 dollarga tushirdi.»", "Wide shot from a slightly high angle", ["grey", "blue", "amber"], "", True,
  "An early-2000s open-plan office of an online store: rows of desks with bulky CRT monitors showing simple coloured bar charts that go up, a big wall whiteboard with three arrows pointing down step by step (no writing), "
  "behind a glass wall a warehouse with cardboard boxes on conveyor belts. Several office workers in 2000s shirts are seen from behind or far away, faces not visible; they are not real people."),
 ("6", "Usta: «Odamlar chegaraga yetish uchun savatga yana narsa qo'shdi…»", "Medium shot, shallow depth of field", ["amber", "blue"], "", True,
  "A warehouse packing table: open cardboard delivery boxes on a moving conveyor belt; into each box several hands (only hands and sleeves visible, from the sides of the frame) keep adding small extra things: "
  "a candle, socks, a mug, a keychain, a chocolate bar, so the boxes overflow. Warm amber lamps above, deep blue shadows."),
 ("7", "Diyor: «Bizni sanashgan ekan-da?!»", "Extreme close-up, push-in framing on the face", ["amber", "blue"], "d", False,
  f"{PLACE}, blurred warm string lights behind. {Dy} in total shock: eyes very wide, eyebrows shot up high, mouth open, one hand frozen halfway to his mouth, "
  "his smartphone in the other hand, its blue light on his chin."),
 ("8", "Usta: «Faqat Fransiyada yetkazish uchun bir frank, ya'ni yigirma sent olishgan. U yerda sotuv deyarli o'smagan.»", "Top-down close shot of a table, simple and clear like an explainer picture", ["amber", "blue", "green"], "", False,
  "An old paper map of Western Europe lies on a dark blue table, without any names or letters. Over several countries small glowing green arrows rise up. Over France (clearly shaped, in the middle of the map) "
  "the arrow is flat and grey, and a single small old coin lies on France. Warm amber desk lamp light. Clean, simple, easy to understand at one glance."),
 ("9", "Usta: «Narxni nolga tushirishgan zahoti, u yerda ham sotuv o'sib ketdi.»", "The same top-down close shot of the table", ["amber", "blue", "green"], "", False,
  "The same old paper map of Western Europe on the dark blue table, without any names or letters. Now the coin over France is gone, and over France a big glowing green arrow shoots up, brighter than all the others; "
  "the small green arrows over the other countries also rise. Warm amber desk lamp light. Clean, simple, easy to understand at one glance."),
 ("10", "Usta: «Olimlar sinab ko'rgan: qimmat shokoladni ko'pchilik tanlagan. Arzonini ‘bepul’ qilishgan zahoti — hamma bepuliga o'tgan.»", "Close-up at table height", ["amber", "red", "blue"], "", False,
  "A small wooden table with two plates: on the left a fancy round chocolate truffle on a small gold dish, on the right a plain little wrapped chocolate on a simple red paper napkin. "
  "Many hands of different people (only hands and sleeves, coming from the edges of the frame) all reach eagerly toward the plain little chocolate on the right; nobody reaches for the truffle. "
  "Deep blue background, warm amber light. No labels, no brand names, no letters."),
 ("11", "Diyor: «Demak, ‘bepul’ so'zi miyani aldaydi?» — Usta: «Aldamaydi. Shoshiltiradi.»", "Medium two-shot at eye level", ["amber", "blue", "red"], "ud", False,
  f"{PLACE}. {Dy} looks thoughtfully at the shopping cart on his smartphone, lips pushed to one side, eyebrows knitted. {U} sits next to him and gently taps his own temple with one finger, "
  "explaining with a calm smile."),
 ("12", "Usta: «Hisobla: yigirma ming tejading, qirq ming sarflading.»", "Close-up over Usta's shoulder on the phone", ["amber", "blue"], "ud", False,
  f"{PLACE}. {U} holds Diyor's smartphone and points at its screen with one finger; the screen shows the simple shopping cart with two product cards and an empty blue area for the total (no letters or numbers). "
  f"{Dy} leans in from the side, his face half visible, eyebrows raised, realising his mistake."),
 ("13", "Usta: «Uchta qoida…»", "Slightly low-angle medium shot", ["amber", "blue", "red"], "u", False,
  f"{PLACE}. {U} raises exactly three fingers. Above his hand float three glowing neon symbols in a row: a shopping cart (amber), a calendar (blue), "
  "a question mark (red). The symbols have no letters or numbers. Calm confident look into the camera."),
 ("14", "Usta: «Ular senga yetkazishni emas, ‘tekin’ degan tuyg'uni sotadi. Har gal so'ra: bundan kim foyda ko'radi?»", "Close-up, head and shoulders", ["amber", "blue"], "u", False,
  f"{PLACE}, the warm string lights softly blurred behind. {U} looks straight into the camera with a wise, warm, slightly serious face, "
  "eyes soft, a calm small smile; the warm light on one side of his face, the blue evening sky on the other."),
 ("15", "Usta: «Savatingizdagi narsalarni va yetkazish shartini botimizga yozing: @sahiychishopbot…»", "Medium-wide shot with the sky in the top third", ["amber", "blue", "red"], "ud", False,
  f"{PLACE}, the deep blue evening sky at the top. {U} holds a smartphone toward the viewer: its screen shows a simple chat with empty grey and blue speech bubbles (no letters) "
  f"and a small shopping cart symbol. His other hand rests on Diyor's shoulder. {Dy} sits next to him smiling with his mouth closed and gives a thumbs up."),
]
e = html.escape
def prompt(n, shot, cols, refs, old, scene):
    hands = "" if n in ("8", "9") else HANDS + " "
    return f"Vertical 9:16 image, {shot}. {att(refs)}Scene: {scene} {hands}{sty(cols, old, bool(refs))}"
cards = []
for n, voice, shot, cols, refs, old, scene in S:
    p = prompt(n, shot, cols, refs, old, scene)
    th = "".join(f'<figure class="ref"><img src="web/{REF[k][1]}.webp" alt="{REF[k][0]} namunasi"><figcaption>{REF[k][1]}.png</figcaption></figure>' for k in refs) or '<p class="rh">Namuna kerak emas</p>'
    sw = "".join(f'<span class="sw sw-{c}">{c}</span>' for c in cols)
    cards.append(f"""<article class="card"><header><span class="num">{n}</span><h2>{n}-sahna — rasm, 9:16 (tik)</h2><span class="dur">{e(shot.split(',')[0])}</span></header>
<div class="row"><div class="refs"><p class="rh">ChatGPT'ga biriktiring:</p>{th}</div>
<div class="txt"><span class="lbl">Ovoz</span><p class="voice">{e(voice)}</p><div class="sws">{sw}</div>
<pre id="p{n}">{e(p)}</pre><button class="copy" data-t="p{n}">Nusxa olish</button></div></div></article>""")
page = f"""<title>Bepul yetkazish sahnalari</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Manrope:wght@400;600&family=JetBrains+Mono:wght@400&display=swap">
<style>
/* Layout: one column of scene cards; golden-hour palette (single dark theme, deliberately). */
:root{{--bg:#0f1116;--card:#181b23;--line:#2c3140;--fg:#eef0f5;--muted:#a7b0c4;--gold:#f2b544;--teal:#1f8a8a;--navy:#22305a;--blue:#2f5fb3;--grey:#8a93a6;--green:#4cc36b;--red:#d8423a;--mint:#5fd3a6;
--display:"Cormorant Garamond",Georgia,serif;--body:"Manrope",system-ui,sans-serif;--mono:"JetBrains Mono",ui-monospace,monospace;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font-family:var(--body);font-size:15px;line-height:1.55;margin:0}}
.wrap{{max-width:780px;margin:0 auto;padding:28px 16px 60px;display:grid;gap:22px}}
h1{{font-family:var(--display);font-weight:700;font-size:clamp(30px,6vw,44px);margin:0;line-height:1.1}} h1 em{{font-style:normal;color:var(--gold)}}
.intro{{color:var(--muted);margin:0;max-width:64ch}}
.card{{display:grid;gap:14px;background:var(--card);border:1px solid var(--line);border-radius:8px;padding:16px}}
header{{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}} .num{{font-family:var(--mono);color:var(--gold);font-size:14px}}
h2{{font-family:var(--display);font-weight:700;font-size:26px;margin:0}}
.dur{{font-size:12px;letter-spacing:.06em;text-transform:uppercase;border:1px solid var(--line);border-radius:99px;padding:2px 10px;color:var(--muted)}}
.row{{display:grid;grid-template-columns:150px minmax(0,1fr);gap:16px;align-items:start}}
@media (max-width:560px){{.row{{grid-template-columns:minmax(0,1fr)}} .refs{{grid-template-columns:repeat(2,minmax(0,120px))}}}}
.refs{{display:grid;grid-template-columns:minmax(0,1fr);gap:8px;align-content:start}} .rh{{grid-column:1/-1;margin:0;font-size:12px;color:var(--muted)}}
.ref{{margin:0;display:grid;gap:4px}} .ref img{{width:100%;border-radius:4px;display:block;border:1px solid var(--line)}}
.ref figcaption{{font-size:12px;color:var(--muted);font-family:var(--mono)}}
.txt{{min-width:0;display:flex;flex-direction:column;gap:8px}} .lbl{{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}}
.voice{{margin:0;font-style:italic}} .sws{{display:flex;gap:6px;flex-wrap:wrap}}
.sw{{font-size:12px;padding:2px 9px;border-radius:99px;color:#fff;font-weight:600}}
.sw-amber{{background:var(--gold);color:#111}} .sw-teal{{background:var(--teal)}} .sw-navy{{background:var(--navy)}} .sw-blue{{background:var(--blue)}} .sw-grey{{background:var(--grey);color:#111}} .sw-green{{background:var(--green);color:#111}} .sw-red{{background:var(--red)}} .sw-white{{background:#eee;color:#111}} .sw-mint{{background:var(--mint);color:#111}}
pre{{margin:0;white-space:pre-wrap;word-break:break-word;font-family:var(--mono);font-size:12.5px;line-height:1.6;background:var(--bg);border:1px solid var(--line);border-radius:6px;padding:12px;user-select:all}}
.copy{{align-self:flex-start;font:600 15px var(--body);color:#111;background:var(--gold);border:0;border-radius:8px;padding:10px 18px;cursor:pointer}}
.copy.done{{background:var(--mint)}} .copy:focus-visible{{outline:2px solid var(--fg);outline-offset:2px}}
</style>
<div class="wrap">
<h1>«Bepul yetkazish» <em>rasmlari</em></h1>
<p class="intro">15 ta rasm, hammasi 9:16. Har biri uchun ChatGPT'da yangi chat oching, chapdagi namuna rasm(lar)ni biriktiring, «Nusxa olish» bilan promptni qo'ying. 5, 6, 8, 9, 10-sahnalarda Usta va Diyor yo'q — namuna kerak emas. Raqamlar va yozuvlarni (99 → 49 → 25 $, 20 000 / 40 000, @sahiychishopbot) montajda o'zimiz qo'yamiz.</p>
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
open(os.path.join(D, "rasmlar.html"), "w").write(page)
open(os.path.join(D, "rasm_promptlar.txt"), "w").write("\n\n".join(f"### {n}\n" + prompt(n, sh, c, r, o, sc) for n, v, sh, c, r, o, sc in S))
print(len(S), "rasm")
