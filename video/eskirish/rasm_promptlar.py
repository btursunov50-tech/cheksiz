# «Telefoning eskirmagan» — sahna rasmlari uchun ChatGPT promptlari (9:16) → rasmlar.html (Artifact sahifa, nusxa tugmasi, namuna rasmlar yonida).
# Qahramonlar «70 foiz chegirma» dagi o'sha Usta va Diyor (img/ref_*.png). Har kadrda 2–3 asosiy rang (egasi qoidasi, 2026-10-26).
# Joy: chegirma'dagi yomg'irli do'kon ko'chasidan farqli — Toshkentda kuzgi oqshom, oltin quyosh, sariq chinorlar.
# Tarix sahnalari (Jeneva 1924, laboratoriya, sud) sepiya + qahrabo rang, yuzlar xira (haqiqiy shaxs yo'q).
# Ishlatish: python3 video/eskirish/rasm_promptlar.py
import html, os
D = os.path.dirname(os.path.abspath(__file__))
U = ("USTA (the calm man about 30 years old with a fuller face and a short neat full jet-black beard, a black Uzbek doppi skullcap with white arch embroidery, "
     "a dark embroidered chapan robe with a red sash; young strong hands of a 30-year-old man, smooth skin)")
Dy = ("DIYOR (the naive guy about 20 years old with a round boyish face, big innocent eyes, messy straight jet-black hair (never curly, never brown), "
      "a dark navy blue hoodie, a black backpack, jeans and sneakers, outlined only by a thin soft cyan-blue glow)")
HANDS = "Every person has exactly two arms and two hands, five fingers on each hand, every hand clearly belongs to its own arm."
STREET = ("a quiet tree-lined street in Tashkent on an autumn evening at golden hour: tall plane trees with yellow leaves, low warm sun, long soft shadows, "
          "a wide sidewalk with fallen leaves, a park bench, a few passers-by far away, small, softly out of focus, seen from the side or back, no clear faces")
# Egasi (2026-10-28): 7-sahnadan boshlab joy boshqa — orqada Toshkent teleminorasi.
STREET2 = ("a wide pedestrian embankment along a calm canal in Tashkent on an autumn evening at golden hour, with the Tashkent TV tower clearly visible in the background, drawn exactly like the attached TV tower reference photo: three long straight slanted concrete legs that lean inward like a tripod and meet a narrow steel lattice shaft, a large round disc-shaped observation pod about a third of the way up, a slimmer lattice section above it with short side antenna arms, a second smaller round pod higher up, and a thin spire on top; the whole tower glows with warm golden-orange lights against the evening sky; neat lamp posts along the embankment, a few young trees with yellow leaves, low warm sun, a few passers-by far away, small, softly out of focus, seen from the side or back, no clear faces")
COL = {"amber": "warm amber gold", "teal": "deep teal", "navy": "night navy blue", "sepia": "old sepia brown", "red": "signal red",
       "white": "clean soft white", "mint": "fresh mint green"}
def sty(cols, old=False, refs=True):
    c = ", ".join(COL[k] for k in cols[:-1]) + " and " + COL[cols[-1]]
    look = ("an old 1920s photograph come to life: sepia tones, soft film grain, warm glowing light bulbs as the only bright accents" if old else
            "cinematic warm golden-hour light, colourful and eye-catching")
    src = "the same hand-painted semi-realistic cartoon illustration style as the attached reference images" if refs else "a hand-painted semi-realistic cartoon illustration style"
    return (f"Style: {src} (painterly, visible brush texture), {look}. "
            f"Colour rule: the whole frame uses ONLY {len(cols)} main colours: {c}; everything else is soft dark neutral shadow. "
            "Vertical 9:16. No text, no letters, no numbers, no logos, no brand names, no watermark, no subtitles.")
REF = {"u": ("Usta", "ref_usta"), "d": ("Diyor", "ref_diyor"), "t": ("the Tashkent TV tower", "ref_teleminora")}
def att(r):
    if not r: return "No reference images are needed for this image; it shows no main characters. "
    if r == "t": return "Attach the reference photo of the Tashkent TV tower. "
    tv = "t" in r; r = r.replace("t", "")
    if tv and not r: return "Attach the reference photo of the Tashkent TV tower. "
    n = " and ".join(REF[k][0] for k in r)
    return (f"Attach the reference image{'s' if len(r) > 1 else ''} of {n}. Keep {'each character' if len(r) > 1 else 'the character'} exactly as in "
            f"{'their reference images' if len(r) > 1 else 'the reference image'}: the same face, age, hair, beard, clothes and colours. "
            + ("Also attach the reference photo of the Tashkent TV tower and draw the tower in the background exactly in that shape (only its shape; keep the painted style and the scene's colours). " if tv else ""))
# (raqam, ovoz qatori, plan, ranglar, namunalar, eski uslubmi, sahna)
S = [
 ("1", "Usta: «Telefoning eskirmagan. Balki faqat batareyasi charchagandir.»", "Medium shot at eye level", ["amber", "teal", "navy"], "ud", False,
  f"{STREET}. {Dy} stands on the left, frowning angrily at the frozen smartphone in his hand, the phone screen dark and blank. {U} stands next to him on the right, "
  "turned toward the viewer with a calm knowing half-smile, one eyebrow slightly raised, as if about to share a secret."),
 ("2", "Diyor: «Usta, telefonim qotyapti… Nasiyaga yangisini olaman!»", "Close-up, slightly low angle", ["amber", "navy"], "d", False,
  f"{STREET}, softly blurred behind. {Dy} shakes his smartphone in one raised hand in frustration, the screen dark and frozen; his other hand is open in the air; "
  "eyebrows drawn together, lips pressed, cheeks puffed with annoyance."),
 ("3", "Usta: «Diyor, kim aytdi…?» — Diyor: «Hamma biladi-ku!»", "Over-the-shoulder medium close-up: Diyor's shoulder and messy hair blurred in the foreground, focus on Usta", ["amber", "teal"], "ud", False,
  f"{STREET}. {U} looks at Diyor with one eyebrow raised high and a small amused smile, arms folded, head tilted a little, asking a sharp simple question. "
  f"{Dy} is seen from behind, only his shoulder, hood and the back of his head in the foreground, out of focus."),
 ("4", "Usta: «Jim, Diyor. Qara. Jeneva, 1924-yil, dekabr.»", "Medium shot", ["amber", "sepia", "navy"], "u", False,
  f"{U} on the autumn street raises his open palm calmly like «be quiet and watch». Behind him the golden street dissolves from right to left into an old sepia picture: "
  "a 1920s European city by a lake in winter, old trams, men in long coats and hats, gas street lamps, the old part softly grainy like an old photograph."),
 ("5", "Usta: «Dunyodagi eng katta lampochka zavodlari kelishib oldi: … ming soatdan ortiq yonmasin.»", "Wide shot from a slightly high angle", ["sepia", "amber"], "", True,
  "A dark 1920s meeting hall with tall windows and heavy curtains. Seven businessmen in 1920s three-piece suits sit around a long polished table; "
  "rows of glowing incandescent light bulbs stand on the table in front of them. Their faces are in deep shadow or turned away, no recognizable faces, they are not real people. "
  "One man in the middle pushes a paper across the table, two others shake hands over it."),
 ("6", "Usta: «Undan oldin 2500 soatgacha yonardi. Uzoqroq yonadiganini chiqargan zavod jarima to'lardi.»", "Medium shot, shallow depth of field", ["sepia", "amber"], "", True,
  "An old 1920s testing laboratory: long wooden racks with dozens of glowing light bulbs in rows, an old wall clock, a clipboard with blank paper. "
  "In the foreground one bulb has just gone dark among the glowing ones. A technician in a white coat is seen only from behind, writing on the clipboard."),
 ("6b", "Diyor: «Ataylab-a?!»", "Extreme close-up, push-in framing on the face", ["amber", "navy"], "d", False,
  f"{STREET}, blurred golden background. {Dy} in total shock: eyes very wide, eyebrows shot up high, mouth open, one hand frozen halfway to his mouth, "
  "the golden light on one side of his face."),
 ("7", "Usta: «2017-yil. Eng mashhur telefon kompaniyalaridan biri bir sirni tan oldi.» — Diyor: «Qanaqa sir?»", "Medium two-shot at eye level", ["amber", "teal", "navy"], "udt", False,
  f"{STREET2}. {U} gently takes the smartphone from Diyor's hand and holds it up between them, looking at it seriously. {Dy} leans in, curious, eyebrows raised. "
  "The phone screen is dark and blank, with no logo on the back of the phone."),
 ("8", "Usta: «Batareyasi eskirgan telefonlarni o'zi sekinlashtirib qo'ygan…»", "Close-up of an object, simple and clear like an explainer picture", ["teal", "red", "navy"], "", False,
  "A plain smartphone with no logo floats in the centre against a soft dark navy background. On its screen a big simple battery symbol is almost empty with a small red level, "
  "and a cute cartoon snail crawls slowly across the screen, leaving a shiny trail. Clean, simple, easy to understand at one glance."),
 ("9", "Usta: «Odamlar ‘telefonim eskirdi’ deb, yangisini sotib olgan…»", "Wide shot, slightly high angle", ["amber", "teal", "white"], "", False,
  "A busy modern phone shop counter at evening: several people (seen from the back or side, no clear faces) hand over their old phones and walk away with new white phone boxes. "
  "In the front, a big basket full of old smartphones that still look perfectly fine. No logos on the boxes or phones."),
 ("10", "Usta: «…yarim milliard dollargacha to'lashga rozi bo'ldi. Fransiyada 25 million yevro jarima.»", "Low-angle close-up", ["amber", "sepia", "navy"], "", False,
  "A wooden judge's gavel striking a sound block on a dark wooden desk, frozen at the moment of impact, small dust in warm light; beside it neat stacks of banknotes "
  "and a closed old smartphone with a cracked battery icon on its dark screen. No readable text on the money (blurred), no flags."),
 ("11", "Diyor: «Demak, mening telefonim ham eskirmagan…?» — Usta: «Bo'lishi mumkin.»", "Medium close-up", ["amber", "teal"], "udt", False,
  f"{STREET2}. {Dy} holds his smartphone in both hands and looks down at it with slowly growing hope: soft eyes, a small hopeful smile, head tilted. "
  f"{U} stands just behind his shoulder, slightly out of focus, smiling warmly with his mouth closed."),
 ("12", "Diyor: «Kechir, eski do'stim… sen aybsiz ekansan!» — Usta: «Quchoqlama, batareyasini tekshir!»", "Medium two-shot", ["amber", "teal", "navy"], "udt", False,
  f"{STREET2}. Comedy moment: {Dy} hugs his smartphone tightly to his chest with both hands, eyes closed, a guilty loving smile. {U} next to him laughs, "
  "eyes crinkled, pointing at the phone with one finger in a friendly scolding way."),
 ("13", "Usta: «Uchta tekshiruv: batareya holati? Xotira to'lmaganmi? Batareya almashtirish qancha?»", "Slightly low-angle medium shot", ["amber", "teal", "mint"], "ut", False,
  f"{STREET2}. {U} raises exactly three fingers. Above his hand float three glowing neon symbols in a row: a battery (amber), a memory chip (teal), "
  "a wrench (mint green). The symbols have no letters or numbers. Calm confident look into the camera."),
 ("14", "Usta: «Ular senga telefon emas, ‘eskirding’ degan tuyg'uni sotadi…»", "Close-up, head and shoulders", ["amber", "navy"], "ut", False,
  f"{STREET2}, the golden sun and yellow leaves softly blurred behind. {U} looks straight into the camera with a wise, warm, slightly serious face, "
  "eyes soft, a calm small smile; the low sun lights one side of his face."),
 ("15", "Usta: «Botimizga modelini yozing: @sahiychishopbot…»", "Medium-wide shot with the sky in the top third", ["amber", "teal", "navy"], "udt", False,
  f"{STREET2}, the evening sky at the top. {U} holds a smartphone toward the viewer: its screen shows a simple chat with empty grey and teal speech bubbles (no letters) "
  f"and a small battery symbol. His other hand rests on Diyor's shoulder. {Dy} stands next to him smiling with his mouth closed and gives a thumbs up."),
]
e = html.escape
def prompt(n, shot, cols, refs, old, scene):
    hands = "" if n == "8" else HANDS + " "
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
page = f"""<title>Telefoning eskirmagan sahnalari</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Manrope:wght@400;600&family=JetBrains+Mono:wght@400&display=swap">
<style>
/* Layout: one column of scene cards; golden-hour palette (single dark theme, deliberately). */
:root{{--bg:#0f1116;--card:#181b23;--line:#2c3140;--fg:#eef0f5;--muted:#a7b0c4;--gold:#f2b544;--teal:#1f8a8a;--navy:#22305a;--sepia:#8a6a45;--red:#d8423a;--mint:#5fd3a6;
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
.sw-amber{{background:var(--gold);color:#111}} .sw-teal{{background:var(--teal)}} .sw-navy{{background:var(--navy)}} .sw-sepia{{background:var(--sepia)}} .sw-red{{background:var(--red)}} .sw-white{{background:#eee;color:#111}} .sw-mint{{background:var(--mint);color:#111}}
pre{{margin:0;white-space:pre-wrap;word-break:break-word;font-family:var(--mono);font-size:12.5px;line-height:1.6;background:var(--bg);border:1px solid var(--line);border-radius:6px;padding:12px;user-select:all}}
.copy{{align-self:flex-start;font:600 15px var(--body);color:#111;background:var(--gold);border:0;border-radius:8px;padding:10px 18px;cursor:pointer}}
.copy.done{{background:var(--mint)}} .copy:focus-visible{{outline:2px solid var(--fg);outline-offset:2px}}
</style>
<div class="wrap">
<h1>«Telefoning eskirmagan» <em>rasmlari</em></h1>
<p class="intro">16 ta rasm, hammasi 9:16. Har biri uchun ChatGPT'da yangi chat oching, chapdagi namuna rasm(lar)ni biriktiring, «Nusxa olish» bilan promptni qo'ying. 5, 6, 8, 9, 10-sahnalarda Usta va Diyor yo'q — namuna kerak emas. Raqamlar, belgilar va yozuvlarni montajda o'zimiz qo'yamiz.</p>
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
