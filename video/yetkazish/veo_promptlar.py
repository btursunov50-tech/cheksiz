# «Bepul yetkazish» — Veo «Frames to video» promptlari (9:16, 6 s) → sahnalar.html (Artifact, nusxa tugmasi).
# Egasi (2026-10-29): 6 soniyali, qisqa, puxta prompt; har kadrda aniq kamera harakati; mayda detallarga e'tibor.
# Kamera promptning boshida va oxirida; qo'shni sahnalarda harakat takrorlanmaydi. Gapiradigan qahramonning aniq o'zbekcha gapi promptda,
# tinglovchining og'zi yopiq. Ekrandagi narsalar (savat, chat) rasmdagidek qoladi. 5, 6, 8, 9, 10 — Usta ovozi kadr ortidan, keyin qo'yiladi.
# Ishlatish: python3 video/yetkazish/veo_promptlar.py
import html, os
D = os.path.dirname(os.path.abspath(__file__))
U_V = "a calm deep warm male voice of about 30-35"
D_V = "a lighter young male voice of about 22"
LOCK = ("Keep both characters exactly as in the image: Usta about 30, smooth young skin, short full black beard, black doppi with a white arch pattern, "
        "dark embroidered chapan with a red sash; Diyor about 20, round boyish face, messy jet-black hair, navy hoodie. Same faces, five fingers on each hand. ")
END = "Keep the hand-painted cartoon style of the image for the whole clip, never photorealistic. No text, no subtitles, no captions, no logos. The camera never stops moving."

def say(lines):
    return " ".join(f'{w} says in Uzbek, in {v}: "{t}"' for w, v, t in lines)

# (raqam, rasm, ovoz, kamera (uz), kamera (en), harakat, gaplar, qahramonlar bormi)
S = [
 ("1", "s01", "Usta: «Bepul yetkazish bepul emas. Uning pulini baribir to'laysan.»", "sekin yaqinlashish Usta yuziga",
  "slow push-in from the medium shot to a close-up of Usta's face",
  "Usta looks into the lens with a knowing half-smile and speaks; one eyebrow rises on «bepul emas», a slow small nod at the end. "
  "Behind him, out of focus, Diyor keeps scrolling with his thumb and grinning at the phone, mouth closed. The string lights sway gently.",
  [("Usta", U_V, "Bepul yetkazish bepul emas. Uning pulini baribir to'laysan.")], True),
 ("2", "s02", "Diyor: «Usta, shampun oldim, yetkazish yigirma ming ekan. Yana qirq minglik narsa qo'shsam, bepul bo'larkan!»", "qo'lda, telefondan yuzga suzish",
  "handheld, a light bouncy drift from the phone screen to Diyor's excited face",
  "Diyor talks fast and excited, pushes the phone toward the lens and taps the bottom card twice with his index finger, bouncing a little; "
  "eyes wide, big grin. The phone screen stays exactly as in the image: a shampoo bottle card, a box card, an empty blue button.",
  [("Diyor", D_V, "Usta, shampun oldim, yetkazish yigirma ming ekan. Yana qirq minglik narsa qo'shsam, bepul bo'larkan!")], True),
 ("3", "s03", "Usta: «O'sha qirq minglik narsa senga kerakmi?» — Diyor: «Unchalik emas… lekin bepul-ku!»", "Diyor yelkasi ustidan Usta tomon sekin yaqinlashish",
  "slow push-in toward Usta over Diyor's blurred shoulder; Diyor's shoulder stays at the left edge and never covers Usta",
  "Usta finishes pouring, puts the teapot down on the table, holds the small piyola, raises one eyebrow with an amused smile and asks. "
  "Then Diyor in the blurred foreground shrugs and tilts his head as he answers (his face stays turned away); Usta listens, mouth closed, and takes a sip from the small piyola cup, never from the teapot. "
  "The same courtyard with red cushions, string lights and grapevine stays behind him.",
  [("Usta", U_V, "O'sha qirq minglik narsa senga kerakmi?"), ("Diyor", D_V, "Unchalik emas... lekin bepul-ku!")], True),
 ("4", "s04", "Usta: «Jim, Diyor. Qara. 2002-yil, Amerika.»", "kaftga qarab sekin yaqinlashish, keyin ofis tomonga yengil burilish",
  "slow push-in toward Usta's raised palm, then a gentle pan to the left toward the painted office",
  "Usta speaks quietly, palm held up like «quiet, watch», then turns his head toward the office on the left. "
  "The background stays as in the image: the painted early-2000s office on the left and the courtyard on the right; office workers in the office keep typing, seen from behind. The lantern flame flickers.",
  [("Usta", U_V, "Jim, Diyor. Qara. Ikki ming ikkinchi yil, Amerika.")], True),
 ("5", "s05", "Usta (kadr ortidan): «Dunyodagi eng katta onlayn do'kon bepul yetkazishni 99 dollardan 49 dollarga, ikki oydan keyin 25 dollarga tushirdi.»", "yuqoridan pastga, doskaga qarab kran",
  "slow crane down and forward over the desks toward the whiteboard",
  "Office workers type on old keyboards, the bars on the monitors grow taller one by one, boxes move along the conveyor behind the glass, a worker in the warehouse walks right with a box. Desk lamps glow. Nobody looks at the camera, no faces.",
  [], False),
 ("6", "s06", "Usta (kadr ortidan): «Odamlar chegaraga yetish uchun savatga yana narsa qo'shdi. Do'kon buni ijobiy natija deb e'lon qildi.»", "konveyer bo'ylab o'ngga yonma-yon kuzatish",
  "slow sideways tracking shot to the right along the conveyor",
  "The boxes roll slowly to the right on the conveyor. The hands keep dropping things in: the candle, the socks, the mug, the chocolate; the boxes overflow. Workers in the back keep walking. Only hands and sleeves, no faces.",
  [], False),
 ("7", "s07", "Diyor: «Bizni sanashgan ekan-da?!»", "tez yaqinlashish ko'zlarga",
  "fast snap push-in to an extreme close-up of Diyor's eyes, then a tiny shake",
  "Diyor lowers his hand from his mouth and shouts in shock, eyes huge, eyebrows high, staring at the phone; its blue light flickers on his chin. The string lights behind him blur.",
  [("Diyor", D_V, "Bizni sanashgan ekan-da?!")], True),
 ("8", "s08", "Usta (kadr ortidan): «Faqat Fransiyada yetkazish uchun bir frank, ya'ni yigirma sent olishgan. U yerda sotuv deyarli o'smagan.»", "xaritaga tepadan sekin aylanib yaqinlashish",
  "top-down slow push-in with a slight clockwise rotation toward France",
  "The green arrows over the other countries pulse and grow a little taller. Over France the grey arrow stays flat and the coin stays still. The lamp flame flickers. The map does not change shape.",
  [], False),
 ("9", "s09", "Usta (kadr ortidan): «Narxni nolga tushirishgan zahoti, u yerda ham sotuv o'sib ketdi.»", "Fransiyadan orqaga va yuqoriga ko'tarilish",
  "slow pull-back and crane up from France to show the whole map",
  "The big green arrow over France shoots higher with a burst of green sparks and glows brighter than all others; the small arrows pulse. The lamp flame flickers. The map does not change shape.",
  [], False),
 ("10", "s10", "Usta (kadr ortidan): «Olimlar sinab ko'rgan: qimmat shokoladni ko'pchilik tanlagan. Arzonini bepul qilishgan zahoti — hamma bepuliga o'tgan.»", "stol balandligida konfetga qarab yaqinlashish",
  "low push-in at table height toward the small red candy",
  "All the hands reach eagerly toward the small red candy; the nearest hand grabs it first, the others hurry closer. Nobody touches the truffle on the gold dish. The lantern flame flickers. Only hands and sleeves, no faces.",
  [], False),
 ("11", "s11", "Diyor: «Demak, ‘bepul’ so'zi miyani aldaydi?» — Usta: «Aldamaydi. Shoshiltiradi.»", "ikkalasi atrofida o'ngga sekin yoy",
  "slow arc to the right around both men",
  "Diyor lifts his eyes from the phone to Usta and asks, puzzled, finger on his chin. Usta taps his temple twice and answers calmly with a small smile; Diyor listens, mouth closed, and slowly nods.",
  [("Diyor", D_V, "Demak, bepul so'zi miyani aldaydi?"), ("Usta", U_V, "Aldamaydi. Shoshiltiradi.")], True),
 ("12", "s12", "Usta: «Hisobla: yigirma ming tejading, qirq ming sarflading.»", "telefondan Diyor yuziga fokus o'tishi + yengil yaqinlashish",
  "rack focus from the phone screen to Diyor's face with a gentle push-in",
  "Usta, seen from behind, speaks and taps the blue button twice with his finger; his jaw moves under the beard. Diyor's dreamy smile slowly fades: eyebrows rise, eyes widen, his cheeks blush and he slowly lowers his hands, embarrassed, mouth closed. "
  "The phone screen stays exactly as in the image: the shampoo card, the box card, the blue button.",
  [("Usta", U_V, "Hisobla: yigirma ming tejading, qirq ming sarflading.")], True),
 ("13", "s13", "Usta: «Uchta qoida. Faqat kerakli narsani ol. Yaqinda baribir oladigan narsalarni bitta buyurtmaga yig'. Va so'ra: yetkazish pullik bo'lmaganida ham shuni olarmidim?»", "pastdan yuqoriga belgilar tomon ko'tarilish",
  "low-angle slow crane up toward the three glowing symbols",
  "Usta keeps exactly three fingers raised and speaks with confidence; the symbols light up one by one as he talks: the cart, then the calendar, then the question mark, each with a small pulse of sparks. The lantern flame flickers.",
  [("Usta", U_V, "Uchta qoida. Faqat kerakli narsani ol. Yaqinda baribir oladigan narsalarni bitta buyurtmaga yig'.")], True),
 ("14", "s14", "Usta: «Ular senga yetkazishni emas, ‘tekin’ degan tuyg'uni sotadi. Har gal so'ra: bundan kim foyda ko'radi?»", "juda sekin yaqinlashish ko'zlarga",
  "very slow push-in to an extreme close-up of Usta's eyes",
  "Usta looks straight into the lens and speaks slowly and warmly; on the question his eyebrows lift, his head tilts a little and he gives a small knowing smile. The string lights twinkle in the blurred background.",
  [("Usta", U_V, "Ular senga yetkazishni emas, tekin degan tuyg'uni sotadi. Har gal so'ra: bundan kim foyda ko'radi?")], True),
 ("15", "s15", "Usta: «Savatingizdagi narsalarni va yetkazish shartini botimizga yozing: @sahiychishopbot. Bepul yetkazish uchun ortiqcha qancha to'layotganingizni hisoblab, nimani olib tashlash mumkinligini aytadi.»", "orqaga va yuqoriga ko'tarilish, osmon ochiladi",
  "slow pull-back and crane up, revealing more of the night sky and the moon",
  "Usta holds the phone toward the viewer and speaks with a friendly smile; Diyor nods twice and keeps his thumb up, smiling, mouth closed. The phone screen stays exactly as in the image: the chat bubbles and the cart icon. The lanterns glow, the stars twinkle.",
  [("Usta", U_V, "Savatingizdagi narsalarni va yetkazish shartini botimizga yozing: sahiychi shop bot.")], True),
]

# Egasi (2026-10-29, «gap uzun joyga 8 soniya qil»): gapi ~6 s dan uzun sahnalar 8 s.
DUR = {"2": 8, "5": 8, "6": 8, "8": 8, "10": 8, "13": 8, "14": 8, "15": 8}
def vp(n, cam, act, lines, chars):
    dial = f" {say(lines)}" if lines else ""
    return (f"Vertical 9:16, {DUR.get(n, 6)} seconds. Start from the attached image. Camera: {cam}. {act}{dial} "
            f"{LOCK if chars else ''}{END}")

DONE = {"1": "Veo (yozuv tozalandi)", "2": "Veo (tugma tozalandi)", "5": "Veo", "6": "Veo", "7": "Veo"}
e = html.escape
cards = []
for n, img, voice, camuz, cam, act, lines, chars in S:
    if n in DONE: continue
    p = vp(n, cam, act, lines, chars)
    cards.append(f"""<article class="card"><header><span class="num">{n}</span><h2>{n}-sahna — 9:16 (tik), {DUR.get(n, 6)} s</h2></header>
<div class="row"><figure class="sc"><img src="web/{img}.webp" alt="{n}-sahna rasmi"><figcaption>Veo'ga: {img}.png</figcaption></figure>
<div class="txt"><span class="lbl">Ovoz</span><p class="voice">{e(voice)}</p>
<span class="lbl">Kamera: {e(camuz)}</span>
<pre id="v{n}">{e(p)}</pre><button class="copy" data-t="v{n}">Nusxa olish</button></div></div></article>""")

page = f"""<title>Bepul yetkazish sahnalari</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Manrope:wght@400;600&family=JetBrains+Mono:wght@400&display=swap">
<style>
/* Layout: one column of scene cards; golden-hour palette (single dark theme, deliberately). */
:root{{--bg:#0f1116;--card:#181b23;--line:#2c3140;--fg:#eef0f5;--muted:#a7b0c4;--gold:#f2b544;--mint:#5fd3a6;
--display:"Cormorant Garamond",Georgia,serif;--body:"Manrope",system-ui,sans-serif;--mono:"JetBrains Mono",ui-monospace,monospace;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font-family:var(--body);font-size:15px;line-height:1.55;margin:0}}
.wrap{{max-width:780px;margin:0 auto;padding:28px 16px 60px;display:grid;gap:22px}}
h1{{font-family:var(--display);font-weight:700;font-size:clamp(30px,6vw,44px);margin:0;line-height:1.1}} h1 em{{font-style:normal;color:var(--gold)}}
.intro{{color:var(--muted);margin:0;max-width:64ch}}
.card{{display:grid;gap:14px;background:var(--card);border:1px solid var(--line);border-radius:8px;padding:16px}}
header{{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}} .num{{font-family:var(--mono);color:var(--gold);font-size:14px}}
h2{{font-family:var(--display);font-weight:700;font-size:26px;margin:0}}
.row{{display:grid;grid-template-columns:190px minmax(0,1fr);gap:16px;align-items:start}}
@media (max-width:560px){{.row{{grid-template-columns:minmax(0,1fr)}} .sc{{max-width:240px}}}}
.sc{{margin:0;display:grid;gap:6px}} .sc img{{width:100%;border-radius:4px;display:block;border:1px solid var(--line)}}
.sc figcaption{{font-size:12px;color:var(--muted);font-family:var(--mono)}}
.txt{{min-width:0;display:flex;flex-direction:column;gap:8px}} .lbl{{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}}
.voice{{margin:0;font-style:italic}}
pre{{margin:0;white-space:pre-wrap;word-break:break-word;font-family:var(--mono);font-size:12.5px;line-height:1.6;background:var(--bg);border:1px solid var(--line);border-radius:6px;padding:12px;user-select:all}}
.copy{{align-self:flex-start;font:600 15px var(--body);color:#111;background:var(--gold);border:0;border-radius:8px;padding:10px 18px;cursor:pointer}}
.copy.done{{background:var(--mint)}} .copy:focus-visible{{outline:2px solid var(--fg);outline-offset:2px}}
</style>
<div class="wrap">
<h1>«Bepul yetkazish» <em>sahnalari</em></h1>
<p class="intro"><b>Tayyor:</b> 1, 2, 5, 6, 7. <b>3 va 4 — yangi prompt</b> (birinchi kliplarda uslub haqiqiy suratga o'tib ketgan edi). Qolgan sahnalar tartib bilan. Har biri uchun: Veo'da «Frames to video» ni oching, chapdagi rasmni yuklang, <b>9:16</b> va sarlavhadagi uzunlikni (<b>6 s</b> yoki <b>8 s</b>) qo'ying, «Nusxa olish» bilan promptni qo'ying. Gapiradigan sahnada qahramonning o'zbekcha gapi promptda. Gapi uzun sahnalar (2, 5, 6, 8, 10, 13, 14, 15) — 8 s. 13 va 15-sahnada gap 8 s dan ham uzun: promptda asosiy qismi, qolganini montajda sig'diraman. 5, 6, 8, 9, 10-sahnalarda hech kim gapirmaydi — Usta ovozi keyin qo'yiladi.</p>
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
open(os.path.join(D, "sahnalar.html"), "w").write(page)
print(len(S), "sahna; eng uzun prompt:", max(len(vp(n, c, a, l, ch).split()) for n, _, _, _, c, a, l, ch in S), "so'z")
