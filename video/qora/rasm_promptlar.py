# «Qora kvadrat» — so'zsiz rolik, sahna rasmlari uchun ChatGPT promptlari (9:16) → rasmlar.html (Artifact, nusxa tugmasi, Diyor namunasi yonida).
# Ranglar (egasi, 2026-11-06, «Kalamushqir»dek faqat ranglar): qorong'ilik + ko'k neon + yonib turgan qizil; har kadrda 2–3 asosiy rang.
# Diyor: video/yetkazish/img/ref_diyor.png (bu yerda img/ref_diyor.png). Ishlatish: python3 video/qora/rasm_promptlar.py
import html, os
D = os.path.dirname(os.path.abspath(__file__))
Dy = ("DIYOR (the naive guy about 20 years old with a round boyish face, big expressive eyes, messy straight jet-black hair (never curly, never brown), smooth clear skin without freckles, a soft young face (not older, no sharp jaw), "
      "a dark navy blue hoodie, jeans and sneakers; a thin bright cyan-blue neon line runs exactly along his whole outer silhouette (hair, face, hoodie, arms, legs) with a soft blue glow; "
      "nothing else in the frame has this outline)")
HANDS = "Diyor has exactly two arms and two hands, five fingers on each hand, every hand clearly belongs to its own arm."
BSQ = ("Kazimir Malevich's famous painting «Black Square» (1915): a large, slightly uneven black square on a white canvas border, "
       "the black paint covered with a fine web of cracks (craquelure), in a simple thin wooden museum frame")
SQ = ("the printed sheet (a plain white A4 paper with a printed copy of " + BSQ + "; the black square on the paper is a real bottomless hole of absolute black depth "
      "with a faint glowing red light far inside)")
ROOM = "Diyor's small bedroom at night: a desk with a computer monitor and a small home printer, posters-free dark walls, the only light comes from the screen"
COL = {"dark": "deep night darkness (near-black navy)", "cyan": "electric cyan-blue neon", "red": "glowing neon red", "gold": "warm gold"}
def sty(cols, old=False, refs=True):
    c = ", ".join(COL[k] for k in cols[:-1]) + " and " + COL[cols[-1]]
    src = "the same hand-painted semi-realistic cartoon illustration style as the attached reference image" if refs else "a hand-painted semi-realistic cartoon illustration style"
    return (f"Style: {src} (painterly, visible brush texture), cinematic night lighting, strong contrast, glowing neon light, dark and mysterious but colourful and eye-catching. "
            f"Colour rule: the whole frame uses ONLY {len(cols)} main colours: {c}; everything else is soft dark neutral shadow. "
            "Vertical 9:16. No text, no letters, no numbers, no logos, no brand names, no watermark, no subtitles.")
REF = {"d": ("Diyor", "ref_diyor"), "1": ("1-sahna rasmi", "s01"), "4": ("4-sahna rasmi", "s04")}
def att(r):
    if not r: return "No reference images are needed for this image; it shows no main characters. "
    t = "Attach the reference image of Diyor"
    if "1" in r and "4" in r: t += ", the approved scene 1 image and the approved scene 4 image (the same Diyor with the same round boyish young face and look; he is NOT an adult man, keep the face young and round even with a strong expression)"
    elif "1" in r: t += " and the approved scene 1 image (the same Diyor with the same face and look)"
    return (t + ". Keep the character exactly as in the reference image: the same face, age, hair, clothes, colours and the thin cyan-blue neon outline. ")
# (raqam, nima bo'ladi (ovoz yo'q), plan, ranglar, namunalar, -, sahna)
S = [
 ("1", "Xona, kecha: Diyor Google'da rasm qidiradi, oltin ramkadagi qora kvadrat kartinani ko'rib qoladi. Tovush: klaviatura", "Medium close-up from beside the monitor, face and screen both visible", ["dark", "cyan", "red"], "d", False,
  f"{ROOM}. {Dy} sits at the desk, his face lit by the monitor. The screen (seen at an angle) shows an image search results page: a search bar at the top, a grid of small picture thumbnails, and on the right a large preview of " + BSQ + ", "
  "with an empty white rectangular label strip under the preview (left blank on purpose, the price is added later in editing); no logos, no readable words. "
  "Diyor leans toward the screen: eyes wide open, eyebrows raised high, lips slightly parted in a fascinated half-smile, one hand on the mouse."),
 ("2", "Rasmni printerdan chiqaradi, varaqni ko'tarib qaraydi: kvadrat ichida nimadir to'lqinlanadi. Tovush: printer", "Medium shot, slightly low angle", ["dark", "cyan", "red"], "d1", False,
  f"{ROOM}, the small printer on the desk still has a faint glow. {Dy} holds {SQ} up in front of him with both hands at eye level and studies it, head tilted to one side, "
  "curious and amazed: eyebrows slightly raised (not frowning, not angry), eyes wide, lips slightly parted. The black square seems to ripple like dark water, and a faint red glow from inside it lights his face from below."),
 ("3", "Barmog'ini tegizadi, barmoq kvadrat ichiga kirib ketadi. Tovush: past «vuuu»", "Extreme close-up insert at desk level, shallow depth of field", ["dark", "cyan", "red"], "d1", False,
  f"{SQ} lies flat on the desk. Diyor's index finger (his hand with the cyan neon outline) has sunk into the black square up to the second knuckle and simply disappears inside, "
  "with soft red light rippling around the finger like rings on water; the desk under the paper is solid and empty. Behind, strongly blurred and out of focus (shallow depth of field), Diyor's face with the same round boyish young face as in scene 1: eyes huge, mouth open in surprise."),
 ("4", "Qo'lini tirsagigacha tiqadi, stol ostidan chiqmaydi. Kuladi. Tovush: sirli ovoz", "Medium wide shot showing the desk top and the empty space under the desk", ["dark", "cyan", "red"], "d", False,
  f"{ROOM}. {Dy} has pushed his whole forearm up to the elbow into the black square of {SQ}, which lies on the desk; under the desk there is clearly nothing, no hand comes out. "
  "Red light glows around his arm where it enters the paper. He laughs with delight: eyes sparkling, wide open-mouth grin, head thrown back a little."),
 ("5", "Oshxona: varaqni muzlatkichga yopishtiradi, eshikni ochmay qo'lini kiritib muzqaymoq oladi (egasi: muzlatkichda issiq somsa bo'lmaydi). Tovush: «chik»", "Medium shot, eye level", ["dark", "cyan", "red"], "d1", False,
  f"A small dark kitchen at night. The tall fridge is closed; {SQ} is taped on the fridge door with two strips of tape. {Dy} stands next to the fridge; his right arm is still half inside the black square on the fridge door, "
  "and he is pulling it back out holding a frosty ice cream cone, cold mist and tiny frost crystals floating around it (clearly straight from the cold freezer, nothing hot, no steam). "
  "Cheeky grin, one eyebrow raised, eyes glancing at the camera like he got away with something."),
 ("6", "Kuzgi ko'cha, kecha: kapyushonini tortib, varaqni bankomatga yopishtiradi, pul chiqaradi. Tovush: shamol, barglar", "Medium shot from a slight distance, low angle", ["dark", "cyan", "red"], "d14", False,
  f"An empty autumn street at night with fallen red leaves on the wet pavement and one street lamp. {Dy} with his hood pulled up over his head stands at a plain grey cash machine built into a wall "
  f"(no logos, its small screen glows red). {SQ[0].upper()+SQ[1:]} is taped on the front of the machine; his arm reaches into the black square and pulls out a thick stack of banknotes (plain, no readable print). "
  "He glances nervously over his shoulder with his round young face: eyes wide and watchful, eyebrows slightly raised, lips pressed together."),
 ("7", "Yana va yana oladi. Yaqin kadr: ochko'z tabassum (yuz 4-sahnadagidek yosh qolishi kerak). Tovush: yurak urishi", "Medium close-up at eye level (not from below), slow push-in framing", ["dark", "cyan", "red"], "d14", False,
  f"The same night street, softly blurred behind with the street lamp and falling red leaves. {Dy} hugs a big pile of banknote stacks to his chest, more notes sticking out of his hoodie pockets; "
  "a soft red glow comes from the money and from the side, his face stays evenly lit (no harsh light from below). "
  "His face is exactly the round boyish young face of the attached scene 4 image, only the expression changes: a greedy look, eyes glittering and a little too wide, "
  "a wide closed-mouth grin pulling up one corner more than the other. He looks like a cheeky 20-year-old, not an adult man: no wrinkles, no long face, no heavy jaw."),
 ("7b", "YANGI (egasi): Diyor bank binosi oldiga keladi, tepada oltin rangli katta BANK yozuvi. U yozuvga qarab qoladi, keyin bino burchagidan orqa tomonga o'tadi. Tovush: shamol, qadam", "Wide shot, low angle from the street", ["dark", "cyan", "gold"], "d14", False,
  "A grand bank building at night on an autumn street: tall stone columns, heavy closed doors, wet pavement with fallen red leaves. Above the entrance the word BANK in big glowing gold 3D letters (exactly these four letters, B-A-N-K, spelled correctly). "
  f"{Dy} with his hood pulled up, banknotes sticking out of his hoodie pockets, stands in front of the building seen from behind at three-quarters, looking up at the gold BANK letters, "
  "his head tilted, one hand already pointing toward a dark narrow side alley at the corner of the building that leads to the back."),
 ("8", "Bank orqasi: varaqni seyf xonasi devoriga yopishtirib, butun tanasi bilan ichiga sudralib kiradi. Musiqa tezlashadi", "Wide shot, low angle at ground level", ["dark", "cyan", "red"], "d", False,
  "The back wall of a massive bank building at night: thick smooth grey concrete, a heavy round steel vault door seen at the far end, a few fallen red leaves blowing on the ground. "
  f"{SQ[0].upper()+SQ[1:]} is taped low on the wall. {Dy} is crawling head-first into the black square: his head, shoulders and arms are already inside and gone, only his legs and sneakers stick out of the paper, "
  "red light glowing around the edges of the square."),
 ("9", "Seyf ichida: pul dastalari, oltin. Quchog'ini to'ldirib, quvonchdan aylanadi. Tovush: tanga jaranglashi", "Wide shot inside the vault, slightly high angle", ["dark", "cyan", "gold"], "d", False,
  f"Inside a closed steel bank vault: tall metal shelves full of banknote bundles and stacked gold bars. On one steel wall a square opening (the hole of the paper seen from inside) shows the dark street outside. "
  f"{Dy} spins around in the middle with his arms overflowing with money and gold bars, notes flying around him, eyes closed in pure joy, a huge open-mouthed laugh. His cyan neon outline lights the gold."),
 ("10", "Tashqarida kuzgi shamol: varaqning burchaklari ko'chadi, varaq uchib ketadi. Tovush: shamol", "Close-up on the wall, wind blowing from the left", ["dark", "red", "cyan"], "", False,
  "The same back wall of the bank at night, thick grey concrete. A strong autumn wind blows red fallen leaves across the frame. "
  f"The taped paper with the black square ({SQ.split('(',1)[1]} is peeling off the wall: the tape has come loose, two corners lift and flap in the wind, the paper is about to fly away. "
  "A cold blue street light from the side, nobody in the frame."),
 ("10b", "Varaq barglar bilan uchib, ko'lmakka tushadi, qora rang suvda eriydi (sekin kadr)", "Top-down close-up of a puddle", ["dark", "red", "cyan"], "", False,
  "A dark rain puddle on the night pavement with a few red fallen leaves floating in it, reflecting a cold blue street light. "
  "A white sheet of paper lies soaked in the puddle; its printed black square is dissolving into the water in slow black and red swirls of ink, the printed frame and the cracks are blurring. Nobody in the frame."),
 ("11", "Seyf ichida qorong'i: teshik yo'q, tekis temir devor. Faqat neon chizig'i yonadi. Pul tushib ketadi, devorni uradi", "Close-up, eye level, very dark", ["dark", "cyan", "red"], "d14", False,
  f"Inside the closed steel bank vault in near-total darkness. The square opening is gone: the steel wall is completely smooth and closed. {Dy} presses both palms flat against the cold wall; "
  "banknotes slip from under his arms and fall to the floor. The only light in the frame is his own thin cyan-blue neon outline, and a tiny red emergency light far behind. "
  "His same round boyish young face (as in the attached scene 4 image, not an adult) is full of fear: eyes wide and wet, eyebrows pulled up and together, mouth open, breath fogging in the cold air."),
]
e = html.escape
def prompt(n, shot, cols, refs, old, scene):
    hands = HANDS + " " if refs else ""
    st = sty(cols, old, bool(refs))
    if n == "7b": st = st.replace("No text, no letters, no numbers,", "No other text or letters anywhere except the gold word BANK, no numbers,")
    return f"Vertical 9:16 image, {shot}. {att(refs)}Scene: {scene} {hands}{st}"
cards = []
for n, voice, shot, cols, refs, old, scene in S:
    p = prompt(n, shot, cols, refs, old, scene)
    ok = os.path.exists(os.path.join(D, "web", f"s{int(''.join(ch for ch in n if ch.isdigit())):02d}{''.join(ch for ch in n if ch.isalpha())}.webp"))
    okf = f"s{int(''.join(ch for ch in n if ch.isdigit())):02d}{''.join(ch for ch in n if ch.isalpha())}"
    th = (f'<figure class="ref"><img src="web/{okf}.webp" alt="{n}-sahna tasdiqlangan rasm"><figcaption>Tasdiqlandi: img/{okf}.png</figcaption></figure>' if ok else "") + "".join(f'<figure class="ref"><img src="web/{REF[k][1]}.webp" alt="{REF[k][0]} namunasi"><figcaption>{REF[k][1]}.png</figcaption></figure>' for k in refs) or '<p class="rh">Namuna kerak emas</p>'
    sw = "".join(f'<span class="sw sw-{c}">{c}</span>' for c in cols)
    cards.append(f"""<article class="card"><header><span class="num">{n}</span><h2>{n}-sahna — rasm, 9:16 (tik)</h2><span class="dur">{e(shot.split(',')[0])}</span></header>
<div class="row"><div class="refs"><p class="rh">ChatGPT'ga biriktiring:</p>{th}</div>
<div class="txt"><span class="lbl">Nima bo'ladi</span><p class="voice">{e(voice)}</p><div class="sws">{sw}</div>
<pre id="p{n}">{e(p)}</pre><button class="copy" data-t="p{n}">Nusxa olish</button></div></div></article>""")
page = f"""<title>Qora kvadrat sahnalari</title>
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
.sw-dark{{background:#1a2238}} .sw-cyan{{background:#18b8e8;color:#111}} .sw-gold{{background:var(--gold);color:#111}} .sw-amber{{background:var(--gold);color:#111}} .sw-teal{{background:var(--teal)}} .sw-navy{{background:var(--navy)}} .sw-blue{{background:var(--blue)}} .sw-grey{{background:var(--grey);color:#111}} .sw-green{{background:var(--green);color:#111}} .sw-red{{background:var(--red)}} .sw-white{{background:#eee;color:#111}} .sw-mint{{background:var(--mint);color:#111}}
pre{{margin:0;white-space:pre-wrap;word-break:break-word;font-family:var(--mono);font-size:12.5px;line-height:1.6;background:var(--bg);border:1px solid var(--line);border-radius:6px;padding:12px;user-select:all}}
.copy{{align-self:flex-start;font:600 15px var(--body);color:#111;background:var(--gold);border:0;border-radius:8px;padding:10px 18px;cursor:pointer}}
.copy.done{{background:var(--mint)}} .copy:focus-visible{{outline:2px solid var(--fg);outline-offset:2px}}
</style>
<div class="wrap">
<h1>«Qora kvadrat» <em>rasmlari</em></h1>
<p class="intro">12 ta rasm, hammasi 9:16 (tik). Har biri uchun ChatGPT'da yangi chat oching, chapdagi Diyor namunasini biriktiring, «Nusxa olish» bilan promptni qo'ying. 10 va 10b sahnalarda Diyor yo'q, namuna kerak emas. Rolik so'zsiz. Hook, oyat va bot yozuvlarini montajda o'zimiz qo'yamiz.</p>
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
