# «Olmos uzuk» — sahna rasmlari uchun ChatGPT promptlari (9:16) → rasmlar.html (Artifact sahifa, nusxa tugmasi, namunalar yonida).
# Uslub (egasi tanladi, 2026-10-30): img/s01_namuna.png — kunduzgi oltin yorug'lik, haqiqiy Toshkent ko'chasi (teleminora), zargarlik oynasi,
# qahramonlar oldingi videolardagidek (ref_usta, ref_diyor), ko'k neon faqat Diyorda. Har promptga 3 namuna: ref_usta, ref_diyor, s01_namuna (uslub).
# Tarix sahnalari (1938 agentlik, 1947 mashinka, gazeta/TV) — eski sepiya-oltin, yuzlar ko'rinmaydi (haqiqiy shaxs yo'q).
# Ishlatish: python3 video/olmos/rasm_promptlar.py
import html, os
D = os.path.dirname(os.path.abspath(__file__))
U = ("USTA (the calm man about 30 years old, NOT older: a fuller, rounder face with full cheeks, smooth young skin with NO wrinkles on the forehead and NO lines around the eyes, "
     "a short neat FULL jet-black beard that evenly covers the cheeks, jaw and chin (not a thin goatee), a neat moustache, a black Uzbek doppi skullcap with white arch embroidery, "
     "a dark embroidered chapan robe with a red sash; young strong hands of a 30-year-old man, smooth skin)")
Dy = ("DIYOR (the naive guy about 20 years old with a round boyish face, big innocent eyes, messy straight jet-black hair (never curly, never brown), "
      "a dark navy blue hoodie, a black backpack, jeans and sneakers, outlined only by a thin bright cyan-blue neon glow along his whole silhouette)")
HANDS = "Every person has exactly two arms and two hands, five fingers on each hand, every hand clearly belongs to its own arm."
STREET = ("a sunny upscale shopping street in Tashkent at golden hour: a luxury jewelry shop with a big clean glass window full of sparkling diamond rings on cream velvet stands, "
          "marble shop front, autumn trees with golden leaves, old street lamps, the Tashkent TV tower in the far background against a clear sky, "
          "a few passers-by far away, small, softly out of focus, seen from the side or back, no clear faces; the shop glass shows only blurred golden reflections, no reflected faces")
COL = {"gold": "warm golden sunlight", "cream": "soft cream white", "navy": "deep navy blue", "cyan": "bright cyan-blue neon", "sepia": "old sepia brown", "red": "deep red"}
def sty(cols, old=False, refs=True):
    c = ", ".join(COL[k] for k in cols[:-1]) + " and " + COL[cols[-1]]
    look = ("an old 1930s-1940s photograph come to life: sepia and warm gold tones, soft film grain" if old else
            "warm natural golden-hour daylight with sparkling highlights, rich and eye-catching")
    src = ("exactly the same style as the attached style reference image (Usta and Diyor at the jewelry window): semi-realistic hand-painted cartoon illustration"
           if refs else "the same style as the attached style reference image: semi-realistic hand-painted cartoon illustration")
    return (f"Style: {src}, {look}. "
            f"Colour rule: the frame uses ONLY {len(cols)} main colours: {c}; everything else is soft neutral shadow. "
            "Vertical 9:16. No text, no letters, no numbers, no logos, no brand names, no watermark, no subtitles.")
REF = {"u": ("Usta", "ref_usta"), "d": ("Diyor", "ref_diyor")}
def att(r):
    s = "Attach the style reference image (s01_namuna) and copy its style, light and colours exactly. "
    if not r: return s + "This image shows no main characters. "
    n = " and ".join(REF[k][0] for k in r)
    return (s + f"Also attach the reference image{'s' if len(r) > 1 else ''} of {n}. Keep {'each character' if len(r) > 1 else 'the character'} exactly as in "
            f"{'their reference images' if len(r) > 1 else 'the reference image'}: the same face, age, hair, beard, clothes and colours. ")
# (raqam, ovoz qatori, plan, ranglar, namunalar, eski uslubmi, sahna)
S = [
 ("2", "Diyor: «Usta, to'yga olmos uzuk olaman! Sevgilimga olmos uzukni berib, sevgim qanchalik kuchli ekanini isbotlayman! Lekin pulim yetmaydi, kredit olaman!»", "Medium close-up, slightly low angle", ["gold", "navy", "cyan"], "d", False,
  f"{STREET}, softly blurred behind. {Dy} stands proudly in front of the jewelry window, one hand on his chest, chin up, eyes shining with excitement and a big confident grin; "
  "his other hand holds up a smartphone toward the viewer showing a simple loan app screen: a big blue button and a progress bar, no letters or numbers."),
 ("2b", "Diyor (davomi, xayolida): «…sevgim qanchalik kuchli ekanini isbotlayman!» — to'y orzusi", "Wide shot, slightly low angle, dreamy", ["gold", "cream", "cyan"], "d", False,
  "Diyor's daydream of his wedding: a grand Uzbek wedding hall glowing with golden chandeliers, white flowers and gold-embroidered suzani drapes, guests far away and blurred. "
  f"{Dy}, now in a dark suit with a white shirt (same face, same messy hair, same cyan neon outline), kneels proudly on one knee in the centre and holds up a small open ring box with a HUGE sparkling diamond ring that glows like a star. "
  "In front of him stands his bride in a white Uzbek wedding dress with a long veil and a gold-embroidered cape, seen from the side and slightly from behind, her face mostly hidden by the veil; she is a fictional person. "
  "The whole picture has a soft dreamy glow and sparkles at the edges, like a dream."),
 ("3", "Usta: «Diyor, kim aytdi sevgi olmosda deb?» — Diyor: «Hamma biladi-ku! Kinoda ham, reklamada ham.»", "Over-the-shoulder medium close-up: Diyor's shoulder and messy hair blurred in the foreground, focus on Usta", ["gold", "cream"], "ud", False,
  f"{STREET}. {U} stands by the jewelry window with his arms folded, one eyebrow raised high, a small amused smile, head tilted a little, asking a simple sharp question. "
  f"{Dy} is seen from behind in the foreground, only his shoulder, hood and the back of his head, out of focus."),
 ("4", "Usta: «Diyor, eshit. 1938-yil, Amerika.»", "Medium shot", ["gold", "sepia", "navy"], "u", False,
  f"{U} on the sunny Tashkent street raises his open palm calmly like «listen». Behind him the golden street dissolves from right to left into an old sepia picture: "
  "a 1938 American city street with tall brick buildings, old cars, men in long coats and hats, an old billboard frame with no writing, softly grainy like an old photograph."),
 ("5", "Usta (kadr ortidan): «Dunyodagi eng katta olmos kompaniyasi reklama agentligini yollaydi. Vazifa: odamlar olmosni sevgi belgisi deb o'ylasin.»", "Wide shot from a slightly high angle", ["sepia", "gold"], "", True,
  "A 1938 advertising agency meeting room: five men in 1930s suits around a long wooden table; in the centre of the table one big sparkling diamond lies on a small black velvet cushion, "
  "glowing brighter than everything else. Sketches of a heart and a ring are pinned on a board (drawings only, no writing). The men are seen from behind or their faces are in shadow; they are not real people."),
 ("6", "Usta (kadr ortidan): «1947-yil. Bitta shior yoziladi: ‘Olmos — abadiy’. Keyin bu asrning eng mashhur reklama shiori deb tan olindi.»", "Close-up of hands and a typewriter, shallow depth of field", ["sepia", "gold"], "", True,
  "Late at night in a 1947 office: a woman's hands with a simple wristwatch type on an old black typewriter under a warm desk lamp; a sheet of paper in the typewriter shows one blurred line, not readable; "
  "a coffee cup and a small open ring box with a diamond ring on the desk. Only hands and sleeves are visible, no face."),
 ("7", "Diyor: «Yo'q, mumkin emas! Shiormi?!»", "Extreme close-up, push-in framing on the face", ["gold", "navy", "cyan"], "d", False,
  f"{STREET}, blurred golden background. {Dy} in total shock: eyes very wide, eyebrows shot up high, mouth open, both hands on his cheeks, the cyan neon outline glowing around his hair and hands."),
 ("8", "Usta (kadr ortidan): «Televizorda, gazetada, kinoda — har joyda: uzuk olmosli bo'lsin, deyishdi. Keyinroq reklama aytdi: uzukka ikki oylik maoshingni sarfla.»", "Medium shot, a composed collage", ["sepia", "gold", "red"], "", True,
  "A vintage collage on a wooden table: an old 1950s television set showing a woman's hand with a diamond ring, a stack of old newspapers with a large ring photo (text blurred, not readable), "
  "an old cinema poster with a couple and a sparkling ring (no writing), a red velvet ring box. No faces, no readable text."),
 ("9", "Usta: «Sen sevgi sotib olmayapsan. Kredit sotib olyapsan.»", "Close-up over Usta's shoulder on the phone", ["gold", "navy", "cyan"], "ud", False,
  f"{STREET}. {U} holds Diyor's smartphone and points at its screen with one finger; the screen shows a simple loan chart with a long row of monthly blocks going far to the right (no letters or numbers). "
  f"{Dy} leans in from the side, eyebrows raised, slowly realising, mouth slightly open."),
 ("10", "Diyor: «Demak, sevgilim olmosni emas, meni xohlaydi?» — Usta: «Inshaalloh.»", "Medium two-shot at eye level", ["gold", "navy", "cyan"], "ud", False,
  f"{STREET}. {Dy} turns away from the jewelry window toward Usta with a shy hopeful smile, one hand scratching the back of his head. {U} smiles warmly with his mouth closed and puts a hand on Diyor's shoulder."),
 ("10b", "Usta: «Inshaalloh.» — haqiqiy to'y (kreditsiz, sodda uzuk)", "Medium-wide shot at eye level, warm and joyful", ["gold", "cream", "red"], "d", False,
  "A warm, joyful real Uzbek wedding evening in a cosy family courtyard: a long table with plov, bread and fruit, string lights and flowers, relatives far away clapping, blurred and seen from the side. "
  f"{Dy} in a dark suit (same face, same messy hair, same cyan neon outline) stands next to his bride and smiles shyly and happily; he gently holds her hand, and on her finger there is a simple thin gold ring with a tiny stone, not a huge diamond. "
  "The bride wears a white Uzbek wedding dress with a veil and a gold-embroidered cape, she smiles softly, her face partly hidden by the veil; she is a fictional person. Real happiness, no luxury."),
 ("11", "Usta: «Uchta savol. Bu uzukni kreditsiz ola olasanmi? To'ydan keyin necha oy to'laysan? Sevgiling bilan birga gaplashdingmi?»", "Slightly low-angle medium shot", ["gold", "cream", "cyan"], "u", False,
  f"{STREET}. {U} raises exactly three fingers. Above his hand float three glowing symbols in a row: a ring, a calculator and two hands in a handshake, "
  "in soft golden and cyan light. The symbols have no letters or numbers. Calm confident look into the camera."),
 ("12", "Usta: «Ular senga tosh emas, ‘sevgi shu narxda’ degan tuyg'uni sotadi. Har gal so'ra: bundan kim foyda ko'radi?»", "Close-up, head and shoulders", ["gold", "navy"], "u", False,
  f"{STREET}, the golden sun and the jewelry window softly blurred behind. {U} looks straight into the camera with a wise, warm, slightly serious face, eyes soft, a calm small smile; the low sun lights one side of his face."),
 ("13", "Usta: «To'y xarajatlaringiz ro'yxatini botimizga yozing: @sahiychishopbot…»", "Medium-wide shot with the sky and the TV tower in the top third", ["gold", "cream", "cyan"], "ud", False,
  f"{STREET}, the TV tower and clear sky at the top. {U} holds a smartphone toward the viewer: its screen shows a simple chat with empty grey and blue speech bubbles and a small ring icon (no letters). "
  f"His other hand rests on Diyor's shoulder. {Dy} stands next to him smiling with his mouth closed and gives a thumbs up."),
]
e = html.escape
def prompt(n, shot, cols, refs, old, scene):
    hands = "" if n in ("5", "8") else HANDS + " "
    return f"Vertical 9:16 image, {shot}. {att(refs)}Scene: {scene} {hands}{sty(cols, old, bool(refs))}"
cards = []
for n, voice, shot, cols, refs, old, scene in S:
    if n in ("2", "3", "4"): continue
    p = prompt(n, shot, cols, refs, old, scene)
    th = '<figure class="ref"><img src="web/s01_namuna.webp" alt="uslub namunasi"><figcaption>s01_namuna.png (uslub)</figcaption></figure>' + "".join(f'<figure class="ref"><img src="web/{REF[k][1]}.webp" alt="{REF[k][0]} namunasi"><figcaption>{REF[k][1]}.png</figcaption></figure>' for k in refs)
    sw = "".join(f'<span class="sw sw-{c}">{c}</span>' for c in cols)
    cards.append(f"""<article class="card"><header><span class="num">{n}</span><h2>{n}-sahna — rasm, 9:16 (tik)</h2><span class="dur">{e(shot.split(',')[0])}</span></header>
<div class="row"><div class="refs"><p class="rh">ChatGPT'ga biriktiring:</p>{th}</div>
<div class="txt"><span class="lbl">Ovoz</span><p class="voice">{e(voice)}</p><div class="sws">{sw}</div>
<pre id="p{n}">{e(p)}</pre><button class="copy" data-t="p{n}">Nusxa olish</button></div></div></article>""")
page = f"""<title>Olmos uzuk rasmlari</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Manrope:wght@400;600&family=JetBrains+Mono:wght@400&display=swap">
<style>
/* Layout: one column of scene cards; golden-hour palette (single dark theme, deliberately). */
:root{{--bg:#0f1116;--card:#181b23;--line:#2c3140;--fg:#eef0f5;--muted:#a7b0c4;--gold:#f2b544;--teal:#1f8a8a;--navy:#22305a;--cream:#efe6d2;--navy:#22305a;--cyan:#3fd0ff;--sepia:#8a6a45;--red:#b8323a;--red:#d8423a;--mint:#5fd3a6;
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
.sw-amber{{background:var(--gold);color:#111}} .sw-teal{{background:var(--teal)}} .sw-navy{{background:var(--navy)}} .sw-gold{{background:var(--gold);color:#111}} .sw-cream{{background:var(--cream);color:#111}} .sw-cyan{{background:var(--cyan);color:#111}} .sw-sepia{{background:var(--sepia)}} .sw-red{{background:var(--red)}} .sw-white{{background:#eee;color:#111}} .sw-mint{{background:var(--mint);color:#111}}
pre{{margin:0;white-space:pre-wrap;word-break:break-word;font-family:var(--mono);font-size:12.5px;line-height:1.6;background:var(--bg);border:1px solid var(--line);border-radius:6px;padding:12px;user-select:all}}
.copy{{align-self:flex-start;font:600 15px var(--body);color:#111;background:var(--gold);border:0;border-radius:8px;padding:10px 18px;cursor:pointer}}
.copy.done{{background:var(--mint)}} .copy:focus-visible{{outline:2px solid var(--fg);outline-offset:2px}}
</style>
<div class="wrap">
<h1>«Olmos uzuk» <em>rasmlari</em></h1>
<p class="intro"><b>Tayyor: 1, 2, 3, 4.</b> Yangi: <b>2b</b> (Diyorning to'y orzusi — katta olmos) va <b>10b</b> (haqiqiy to'y — sodda uzuk, «Inshaalloh»). Qolgan rasmlar, hammasi 9:16. Har biri uchun ChatGPT'da yangi chat oching, chapdagi <b>uchala</b> namunani biriktiring (uslub + qahramonlar), «Nusxa olish» bilan promptni qo'ying. 5, 6, 8-sahnalarda qahramonlar yo'q — faqat uslub namunasi. Raqam va yozuvlarni (1938, 1947, «OLMOS — ABADIY», @sahiychishopbot) montajda qo'yamiz.</p>

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
