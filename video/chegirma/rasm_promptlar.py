# «70 foiz chegirma» — 11 sahna rasm promptlari sahifasi (ChatGPT, 9:16).
# Har promptga kerakli qahramonlarning alohida 9:16 namuna rasmi biriktiriladi (img/ref_usta.png, img/ref_diyor.png); sahifada prompt yonida turadi.
# Ishlatish: python3 video/chegirma/rasm_promptlar.py → video/chegirma/rasmlar.html (+ web/ref_*.webp)
# Rang (egasi, 2026-10-26): Kalamushqir'dan faqat ranglar, bitta kadrda 2–3 ta. Hayajonli joylarda plan + mimika yoziladi (2026-10-26).
# Yorliq, taymer, raqamlar rasmda bo'sh — «-70%», «300 000», «-43%» va h.k. montajda yoziladi.
import html

IMG = {}   # egasi yuborgan sahna rasmlari: n → [("s01", "izoh"), ...]
NOTE = {}

REFN = {"usta": "Usta", "diyor": "Diyor"}
NEED = {1: ["usta"], 2: ["diyor"], 3: ["usta", "diyor"], 4: ["diyor"], 5: ["usta"], 6: ["diyor"],
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
SHOP = "a small clothes and shoe shop on an evening street in Tashkent, a big glass shop window with jackets and sneakers on shelves"
SIGN = "a huge blank red sale sign with nothing written on it (we add «-70%» later)"
OLD = "a small blank white card with a thin red line crossed through it (the old price, written later)"
NEW = "a big blank golden yellow price card (the new price, written later)"

S = [
 (1, "0–6 s", "Usta: Bu 70 foizlik chegirma 70 foiz emas. To'lashdan oldin hisoblang.", ["red", "yellow", "blue"],
  f"Medium shot, slightly low angle. {SHOP}. In the window hangs {SIGN}, glowing red; under it {OLD} and next to it {NEW}, the same blank black sneakers on a stand below. "
  f"{U} stands in front of the window, turned to the camera with a calm, knowing half-smile, the index finger of his right hand resting on the red sign, his left hand relaxed at his side. "
  f"Deep night blue street, wet pavement reflecting the red and gold light. {HANDS}"),
 (2, "6–12 s", "Diyor: Usta, qarang! Uch yuz ming edi, bir yuz yetmish ming bo'libdi! Hozir olmasam, yutqazaman!", ["red", "cyan"],
  f"Close-up, eye level. {D} in front of the glowing red sale window, overjoyed and in a hurry: eyes wide and shining, eyebrows high, a huge open grin, one hand pointing at the window, "
  f"the other hand already pulling a wallet out of his hoodie pocket. Red sale light on his face; his own cyan-blue outline glow. {HANDS}"),
 (3, "12–16 s", "Usta: Bu narsani chegirmani ko'rishdan oldin ham qidirayotgan edingmi?", ["yellow", "blue"],
  f"Over-the-shoulder shot from behind {D} (we see only his messy hair, shoulder and cyan glow, no face) toward {U}, who stands calm with folded arms, one eyebrow slightly raised, "
  f"asking quietly. Warm golden window light on Usta's face, deep night blue around. Only these two people. {HANDS}"),
 (4, "16–20 s", "Diyor: Yo'q… Chegirmani ko'rib qoldim.", ["blue", "cyan"],
  f"Close-up of {D} frozen with the wallet half out of his pocket, his smile gone, mouth slightly open, eyes looking up and to the side as he thinks, "
  f"a little embarrassed. Deep night blue background, his cyan-blue glow dimmer. {HANDS}"),
 (5, "20–28 s", "Usta: Hisoblaylik. Uch yuz mingdan bir yuz o'ttiz ming tushgan. Bu yetmish emas, qirq uch foiz.", ["red", "yellow"],
  f"Medium close-up. {U} lifts the huge blank red sale sign up with both hands like a lid; underneath it, on the window, a smaller blank golden yellow card is revealed, glowing "
  f"(we write «-43%» on it later). Usta looks at the camera over the sign with a calm, slightly amused face. Red and gold light only, dark background. {HANDS}"),
 (6, "28–32 s", "Diyor: Unda nega yetmish deb yozishgan?", ["blue", "yellow"],
  f"Medium shot. {D} counts on his fingers, confused: one eyebrow up, head tilted, lips pressed; behind him the shop window with the small golden card glowing. "
  f"Deep night blue around. {HANDS}"),
 (7, "32–38 s", "Usta: Katta raqam ko'zni, taymer qo'lni shoshiltiradi. Kerakli narsa shoshilishni talab qilmaydi.", ["red", "blue"],
  f"Close-up of a glowing red digital countdown timer stuck on the shop window glass, its display blank with no digits (we write «faqat bugun 00:59:59» later); "
  f"reflected in the glass behind it, {U} raises a calm open palm, saying «slow down». Red timer light and deep night blue only. {HANDS}"),
 (8, "38–48 s", "Usta: Uchta tekshiruv: boshqa do'kondagi narxi qancha? O'lchami, sifati, kafolati bir xilmi? Va shu mahsulot senga kecha ham kerakmidi?", ["yellow", "blue", "red"],
  f"Medium shot. {U} faces the camera and holds up three fingers of his right hand; his left hand at his side. Above his hand float three glowing symbols in a row with no writing: "
  f"a golden magnifying glass, a blue measuring tape, a red question mark. Deep night blue background. {HANDS}"),
 (9, "48–52 s", "Diyor: Demak, avval hisoblayman, keyin olaman.", ["cyan", "yellow"],
  f"Medium shot. {D} puts his wallet back into his hoodie pocket with one hand and smiles a relaxed, clever smile, giving a small confident nod; his other hand holds his phone showing a "
  f"plain calculator screen with no digits. Warm golden window light; his cyan-blue glow bright and steady. {HANDS}"),
 (10, "52–56 s", "Usta: Xaridni foiz emas, ehtiyoj hal qilsin.", ["orange", "blue"],
  f"Close-up portrait, eye level. {U} looks straight into the camera with a warm, wise smile. Warm orange street-lamp light on one side of his face, deep night blue on the other. "
  f"His hands are not in the frame."),
 (11, "56–66 s", "Usta: Chegirma yorlig'ini suratga olib botimizga yuboring: @sahiychishopbot. Haqiqiy foizni hisoblab, nimani tekshirishni aytib beradi.", ["blue", "yellow", "teal"],
  f"Medium shot. {U} holds a smartphone toward the camera with his right hand; the screen glows emerald teal with a chat: a photo of a blank red sale tag and a few empty message bubbles, "
  f"no readable text. His left hand rests on the shoulder of {D}, who stands beside him and gives a thumbs up with one hand. Warm golden shop light behind them, deep blue shadows. "
  f"Leave empty dark space in the top third of the frame for a title. {HANDS}"),
]

e = html.escape
cards = []
for n, t, voice, cols, scene in S:
    p = f"{att(n)} Scene {n}, vertical 9:16. {scene} {sty(cols)}"
    refs = "".join(f'<figure class="ref"><img src="web/ref_{k}.webp" alt="{REFN[k]} namunasi"><figcaption>ref_{k}.png</figcaption></figure>' for k in NEED[n])
    sw = "".join(f'<span class="sw sw-{k}">{UZC[k]}</span>' for k in cols)
    imgs = "".join(f'<figure class="sc"><img src="web/{f}.webp" alt="{n}-sahna, {e(c)}"><figcaption>{e(c)}</figcaption></figure>' for f, c in IMG.get(n, []))
    got = (f'<div class="scenes">{imgs}</div>' + (f'<p class="note">{e(NOTE[n])}</p>' if n in NOTE else "")) if imgs else ""
    cards.append(f"""<article class="card"><header><span class="num">{n:02d}</span><h2>{n}-sahna — 9:16 (tik)</h2><span class="dur">{t}</span><span class="sws">{sw}</span></header>{got}
<div class="row"><div class="refs"><p class="rh">Shu rasmni biriktiring:</p>{refs}</div>
<div class="txt"><span class="lbl">Ovoz</span><p class="voice">{e(voice)}</p>
<span class="lbl">Rasm prompti (ChatGPT, 9:16)</span>
<pre id="p{n}">{e(p)}</pre><button class="copy" data-t="p{n}">Nusxa olish</button></div></div></article>""")

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
<h1>«70 foiz chegirma» <em>sahnalari</em></h1>
<p class="intro">11 ta sahna. Har biri uchun: ChatGPT'da yangi chat oching, chapdagi namuna rasmni biriktiring, «Nusxa olish» bilan promptni qo'ying va o'lchamni 9:16 qiling. Har kadrda faqat 2–3 ta rang bor, ular sarlavha yonida ko'rsatilgan. Narx va raqamlarni montajda o'zimiz yozamiz, shuning uchun rasmda yorliqlar bo'sh bo'ladi. Veo promptlari rasmlar tasdiqlangach shu sahifaga qo'shiladi.</p>
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
