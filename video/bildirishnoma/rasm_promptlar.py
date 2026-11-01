# «Telefon jiringlaydi» — sahna rasmlari uchun ChatGPT promptlari (9:16) → rasmlar.html (Artifact sahifa, nusxa tugmasi, namunalar yonida).
# Uslub (egasi tanlagan, olmos): img/s01_namuna.png — kunduzgi oltin yorug'lik, haqiqiy Toshkent ko'chasi (teleminora), zargarlik oynasi,
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
STREET = ("the busy Malika bazaar in Tashkent, the big electronics and phone market, in warm golden-hour light: long lanes of small kiosks and counters with phones, cases, chargers, headphones and laptops on shelves "
          "(no readable signs, no brand logos), colourful awnings, bundles of hanging cables, a few cool neon-blue hanging lamps, shoppers and sellers far away, small, softly out of focus, seen from the side or back, no clear faces")
COL = {"gold": "warm golden sunlight", "cream": "soft cream white", "navy": "deep navy blue", "cyan": "bright cyan-blue neon", "sepia": "old sepia brown", "red": "deep red"}
def sty(cols, old=False, refs=True):
    c = ", ".join(COL[k] for k in cols[:-1]) + " and " + COL[cols[-1]]
    look = ("an old 1930s-1940s photograph come to life: sepia and warm gold tones, soft film grain" if old else
            "warm natural golden-hour daylight with sparkling highlights, rich and eye-catching")
    src = ("exactly the same style as the attached style reference image (Usta and Diyor on the golden street): semi-realistic hand-painted cartoon illustration"
           if refs else "the same style as the attached style reference image: semi-realistic hand-painted cartoon illustration")
    return (f"Style: {src}, {look}. "
            f"Colour rule: the frame uses ONLY {len(cols)} main colours: {c}; everything else is soft neutral shadow. "
            "Vertical 9:16. No text, no letters, no numbers, no logos, no brand names, no watermark, no subtitles.")
REF = {"u": ("Usta", "ref_usta"), "d": ("Diyor", "ref_diyor")}
def att(r):
    s = "Attach the style reference image (s01_namuna) and copy its style, light and colours exactly. For the Malika bazaar background also attach the bazaar reference image (s01) and keep the same bazaar look. "
    if not r: return s + "This image shows no main characters. "
    n = " and ".join(REF[k][0] for k in r)
    return (s + f"Also attach the reference image{'s' if len(r) > 1 else ''} of {n}. Keep {'each character' if len(r) > 1 else 'the character'} exactly as in "
            f"{'their reference images' if len(r) > 1 else 'the reference image'}: the same face, age, hair, beard, clothes and colours. ")
# (raqam, ovoz qatori, plan, ranglar, namunalar, eski uslubmi, sahna)
S = [
 ("1", "Usta: «Telefoning jiringlaganda sen telefonni emas, telefon seni boshqaradi.»", "Medium shot at eye level", ["gold", "navy", "cyan"], "ud", False,
  f"{STREET}. {Dy} stands on the right bent over his smartphone, completely absorbed, its screen lighting his face blue, small round notification bubbles (no letters) floating up from the screen like soap bubbles. "
  f"{U} stands on the left, turned toward the viewer, with a calm knowing half-smile and one eyebrow raised, a hand lightly pointing at Diyor's phone."),
 ("2", "Diyor: «Usta, bir daqiqa, xabar keldi!»", "Close-up, slightly low angle", ["gold", "navy", "cyan"], "d", False,
  f"{STREET}, softly blurred behind. {Dy} reaches one hand eagerly toward the viewer as if grabbing the phone, eyes wide and bright, eyebrows raised, a guilty excited smile; "
  "in his other hand a smartphone glows with a few floating round bubbles (no letters)."),
 ("3", "Usta: «Diyor, eshit. 2006-yil, Amerika.»", "Medium shot", ["gold", "sepia", "navy"], "u", False,
  f"{U} in the Malika bazaar raises his open palm calmly like «listen». Behind him the golden bazaar dissolves from right to left into an old sepia picture: "
  "a 2006 open-plan office with bulky CRT monitors, cluttered desks and cables, soft grain like an old photograph."),
 ("4", "Usta (kadr ortidan): «Bir muhandis cheksiz aylantirishni o'ylab topdi: sahifa tugamaydi, pastga tushaverasan.»", "Close-up over the desk, shallow depth of field", ["sepia", "gold"], "", True,
  "A 2006 office desk late in the evening: an engineer's hands (only hands and sleeves, no face) type on a clunky keyboard in front of a bulky CRT monitor that shows a long web page of simple coloured blocks (no letters); "
  "a desk lamp, a cup of coffee, a stack of papers with blurred sketches. Warm sepia and gold, soft grain."),
 ("5", "Usta: «Sahifa tugasa, to'xtaysan. Tugamasa, to'xtamaysan.»", "Centred symmetrical shot looking down an endless tunnel", ["navy", "cyan", "gold"], "", False,
  "A surreal view: an endless vertical river of identical picture cards (each a blank rounded rectangle with a tiny coloured square, no text) flowing downward through a dark phone-shaped tunnel that never ends, "
  "glowing cyan edges and warm golden sparks, deep navy background. Clean, graphic and easy to read at a glance."),
 ("6", "Usta: «Keyinchalik u shu ixtirosidan afsuslanishini ochiq aytdi.»", "Medium shot of a desk with an empty chair, window on the left", ["sepia", "navy", "gold"], "", True,
  "A rainy night in the same office: rain runs down the big window, city lights blurred outside; on the desk a laptop is closed, the desk lamp glows low, a cold coffee cup beside it, the office chair pushed back and empty. "
  "Nobody is in the picture. Quiet, regretful mood, sepia and navy with a little gold."),
 ("7", "Diyor (kadr ortidan): «Ilovalar bizni ataylab ushlab turadimi?!»", "Extreme close-up of a phone screen, shallow depth of field", ["navy", "cyan", "gold"], "", False,
  "A smartphone seen straight on, its dark screen exploding with hundreds of round glowing notification bubbles in only two colours: bright cyan and warm gold bursting out toward the viewer, "
  "each bubble with a tiny blank icon, no letters, no numbers. Deep navy background, dramatic and eye-catching."),
 ("8", "Usta: «Bir tadqiqotga ko'ra, kuniga qirq oltitaga yaqin bildirishnoma.»", "Medium close-up of an analogue gauge", ["navy", "cyan", "gold"], "", False,
  "A big old brass analogue counter-gauge standing on a dark table, its needle swinging high, with a tall pile of glowing notification bubbles stacked beside it up to the top of the frame; "
  "the gauge dial has marks but no digits or letters. Navy background with cyan and golden glow."),
 ("9", "Usta: «Ilovalar sening e'tiboring bilan pul topadi…»", "Close-up, symmetrical", ["navy", "gold", "cyan"], "", False,
  "A giant stylised eye in the centre whose iris reflects a glowing smartphone screen; from the eye a stream of shiny golden coins pours down into an open hand-held purse at the bottom (only hands, no face). "
  "Deep navy background, golden coins, cyan reflections. No text."),
 ("10", "Usta: «Uchta qoida. Keraksiz bildirishnomani o'chir. Kechasi tinch rejimni yoq. Ilovani ochishdan oldin so'ra: nega ochyapman?»", "Flat-lay, centred, three symbols in a row", ["navy", "cyan", "gold"], "", False,
  "Three big round glowing switches in a row on a dark navy surface, each with a simple icon: a bell with a diagonal slash (cyan), a crescent moon (gold), a question mark (cyan). "
  "Soft glow around each, small sparkles. No letters or numbers."),
 ("11", "Diyor: «Telefon jim, men tinch!»", "Medium shot, eye level", ["gold", "navy", "cyan"], "ud", False,
  f"{STREET}. {Dy} slides his smartphone into his hoodie pocket with a relieved, peaceful smile, shoulders relaxed, eyes closed for a second. "
  f"{U} stands beside him smiling warmly with his mouth closed and puts a hand on Diyor's shoulder."),
 ("12", "Usta: «Ular senga ilovani emas, ‘o'tkazib yuboraman’ degan qo'rquvni sotadi. Har gal so'ra: bundan kim foyda ko'radi?»", "Close-up, head and shoulders", ["gold", "navy"], "u", False,
  f"{STREET}, the warm light and the hanging blue lamps softly blurred behind. {U} looks straight into the camera with a wise, warm, slightly serious face, eyes soft, a calm small smile; the low sun lights one side of his face."),
 ("13", "Usta: «Qaysi bildirishnomani o'chirishni bilmasangiz, ilova nomini botimizga yozing: @sahiychishopbot…»", "Medium-wide shot with the sky and the market roof and sky in the top third", ["gold", "cream", "cyan"], "ud", False,
  f"{STREET}, the market roof and the warm evening sky at the top. {U} holds a smartphone toward the viewer: its screen shows a simple chat with empty grey and blue speech bubbles and a small bell-with-slash icon (no letters). "
  f"His other hand rests on Diyor's shoulder. {Dy} stands next to him smiling with his mouth closed and gives a thumbs up."),
]
e = html.escape
def prompt(n, shot, cols, refs, old, scene):
    hands = "" if n in ("5", "7", "8", "9", "10") else HANDS + " "
    return f"Vertical 9:16 image, {shot}. {att(refs)}Scene: {scene} {hands}{sty(cols, old, bool(refs))}"
cards = []
for n, voice, shot, cols, refs, old, scene in S:
    if n in ("1", "2", "3", "4", "5"): continue
    p = prompt(n, shot, cols, refs, old, scene)
    th = '<figure class="ref"><img src="web/s01_namuna.webp" alt="uslub namunasi"><figcaption>s01_namuna.png (uslub)</figcaption></figure>' + "".join(f'<figure class="ref"><img src="web/{REF[k][1]}.webp" alt="{REF[k][0]} namunasi"><figcaption>{REF[k][1]}.png</figcaption></figure>' for k in refs)
    sw = "".join(f'<span class="sw sw-{c}">{c}</span>' for c in cols)
    cards.append(f"""<article class="card"><header><span class="num">{n}</span><h2>{n}-sahna — rasm, 9:16 (tik)</h2><span class="dur">{e(shot.split(',')[0])}</span></header>
<div class="row"><div class="refs"><p class="rh">ChatGPT'ga biriktiring:</p>{th}</div>
<div class="txt"><span class="lbl">Ovoz</span><p class="voice">{e(voice)}</p><div class="sws">{sw}</div>
<pre id="p{n}">{e(p)}</pre><button class="copy" data-t="p{n}">Nusxa olish</button></div></div></article>""")
page = f"""<title>Telefon jiringlaydi rasmlari</title>
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
<h1>«Telefon jiringlaydi» <em>rasmlari</em></h1>
<p class="intro"><b>Tayyor: 1, 3, 4, 5. 2-sahna — tahrir (pastda).</b> Malika bozori namunasi: <b>s01.png</b>. Qolgan rasmlar, hammasi 9:16. <b>Qahramonli sahnalarga s01.png ni ham biriktiring</b> (fon va uslub). Uslub — <b>s01_namuna</b> (oltin soat; qahramonli sahnalar — Malika bozori, elektronika va telefon bozori). Qahramonlar faqat 1, 2, 3, 11, 12, 13-sahnada; 4–10-sahnalar — tasvirlar (odam yo'q, 4 va 6 — eski sepia surat). Har biri uchun ChatGPT'da yangi chat oching, chapdagi namunalarni biriktiring (uslub + kerak bo'lsa qahramonlar), «Nusxa olish» bilan promptni qo'ying. Yozuv va raqamlarni montajda qo'yamiz.</p>
<article class="card"><header><span class="num">2</span><h2>2-sahna — tahrir, 9:16 (tik)</h2><span class="dur">qo'l va telefon</span></header>
<div class="row"><div class="refs"><p class="rh">Rasm chiqqan chatda:</p></div>
<div class="txt"><span class="lbl">Ovoz</span><p class="voice">Diyor: «Usta, bir daqiqa, xabar keldi!»</p>
<pre id="p2e">Edit this image: keep everything exactly the same (Diyor's face, hair, hoodie, backpack, neon outline, the bazaar, the light, the bubbles, style, vertical 9:16). Fix only two things: (1) the hand stretched toward the viewer must have exactly five fingers: thumb, index, middle, ring and little finger, all clearly visible and natural; (2) the smartphone in his other hand must have a completely plain black back with ONE small camera lens and NO logo, NO apple symbol and no brand mark of any kind.</pre><button class="copy" data-t="p2e">Nusxa olish</button></div></div></article>
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
