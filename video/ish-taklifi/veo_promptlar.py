# «Oyiga 490 million» — Veo «Frames to video» promptlari (9:16, 8 s) → sahnalar.html (Artifact, nusxa tugmasi).
# Har prompt: boshlang'ich rasm biriktiriladi, joy o'zgarmaydi, yozuv/odam qo'shilmaydi. Ishlatish: python3 video/ish-taklifi/veo_promptlar.py
import html, os
D = os.path.dirname(os.path.abspath(__file__))
KEEP = ("Start from the attached image and keep its place, objects, colours and look exactly as in the image for the whole clip. Do not add any shop, street, sign, text, label or extra person. ")
NEG = "Negative: no text, no letters, no numbers, no subtitles, no captions, no logos, no brand marks, no watermarks, no signs."
REAL = "One continuous realistic shot, no cuts, natural motion, cinematic. All lamps and bulbs stay neon cyan-blue; no other neon outlines. The camera never stops moving. "
DIG = "One continuous shot, no cuts, rich detail. Light stays mainly warm gold on a dark background, cyan-blue only in the far background lamps. The camera never stops moving. "
# (raqam, rasm, ovoz, kamera uz, kamera en, harakat, uslub)
S = [
 ("1", "s1a", "1-qator (boshi): Oyiga to'rt yuz to'qson million so'm. Tajriba shart emas...", "avtobusga ergashib, keyin oldingi oynadan ichkariga kirish", "tracking shot alongside the bus, then a smooth push-in through the front windows into the bright interior",
  "The bus keeps driving steadily along the boulevard, trees sway, cars flow past with blurred light. The camera follows the bus, then glides forward and passes through the front window into the warm lit interior, ending among the passengers with the blue ceiling lamps glowing. Passengers move slightly, faces stay small and soft.", REAL),
 ("2", "s1b", "1-qatorning davomi: qiz telefonga qaraydi", "qizning yuziga sekin yaqinlashish, ko'k nur butun kadrni to'ldiradi", "slow push-in on her face while the blue screen glow grows until it fills the whole frame",
  "The young woman looks down at the phone she holds and smiles slightly, her eyes move over the screen, her thumb taps once, her hair shifts a little with the bus movement. The soft blue glow on her face slowly brightens. The camera pushes in toward her face and the blue light grows and washes over the frame until the whole frame is filled with glowing blue-white light.", REAL),
 ("3", "s1c", "2-qator (boshi): Post shunday deydi: Claude odamlarni masofaviy ishga taklif qilmoqda...", "ekran ichiga kirish, tanga tomon yaqinlashish", "smooth push-in toward the coin inside the screen",
  "The golden coin rotates slowly in the middle of the post, golden sparks swirl around it and rise, the soft blue lines of the layout drift upward as if the post is scrolling. The camera pushes in toward the coin until it nearly fills the frame.", DIG),
 ("4", "s02", "2-qator (oxiri): ...vazifa — sun'iy intellektni aylanib o'tish", "belgilarga sekin yaqinlashish", "slow push-in toward the three icons",
  "The three round icons (laptop, microchip, blank calendar) light up one after another from left to right with a soft golden flash and a ring of sparks, then hover and gently float up and down. Light moves across the glossy platform below them.", DIG),
 ("5", "s03", "3-qator: Men, Claude, o'zim tekshirdim. Bunday vakansiya topilmadi.", "lupaga yaqinlashish", "slow push-in on the magnifying glass",
  "The magnifying glass moves slowly across the paper; under the lens the printed lines break apart into golden dust and the paper dissolves until nothing is left, sparks float up. The glass reflects soft lights.", DIG),
 ("6", "s04", "4-qator: Lekin asosi haqiqiy: Anthropic'da xavfsizlik dasturi bor...", "qalqon atrofida chapga sekin aylanish", "slow orbit to the left around the shield",
  "The golden key floats toward the padlock and touches the keyhole with a burst of sparks; the padlock stays locked and the shield glows steadily. Reflections shift on the glossy floor. A slight slow-motion feel.", DIG),
 ("7", "s05", "5-qator: Bu oylik maosh emas. Bu topilgan har bir zaiflik uchun mukofot...", "taqvimga yuqoridan sekin yaqinlashish", "slow crane-down toward the calendar",
  "One more golden coin falls from above onto the single stack in slow motion and lands with a small flash and sparks; the rest of the calendar stays empty and dark. The coins glow warmly.", DIG),
 ("8", "s06", "6-qator: Va «tajribasiz» ham emas: yangi zaiflikni topish uchun chuqur bilim kerak...", "qulfga yaqinlashib, mitti kalitga o'tish", "slow push-in to the lock, ending with a rack focus to the tiny key on the floor",
  "The many gears inside the vault lock turn slowly and interlock, the central wheel rotates a little, golden light moves along the metal. The tiny key on the floor stays still and looks far too small. Dust sparks in the light.", DIG),
 ("9", "s07", "7-qator: Qizil bayroqlar: manba yo'q, havola yo'q, «shoshiling» muddati, klik tuzog'i.", "avtobus ichida orqadan sekin oldinga siljish", "slow forward dolly down the bus aisle behind the seats",
  "The glowing thin cyan lines between the screens pulse and travel from phone to phone like a spreading signal, the three small red flags wave gently and glow, passengers stay still looking at their phones, the bus sways slightly. Faces stay hidden from behind.", REAL),
 ("10", "s08", "8-qator: Firibgarlar aynan shunday e'lon bilan pasport, karta va tasdiq kodini so'raydi...", "ko'lmakka yaqinlashish", "slow push-in toward the pond with a slight downward tilt",
  "The coin on the hook swings gently and dips toward the water making rings; the passport booklet and the card drift closer to the coin like fish; the red glow under the water pulses slowly; a few drops fall from the coin.", DIG),
 ("11", "s09", "9-qator: Uchta qoida. Rasmiy sayt. Oldindan pul, karta, kod so'ramaydi. Shoshiltirsa, to'xtang.", "belgilar bo'ylab chapdan o'ngga sekin surilish", "slow truck right along the three icons",
  "The globe icon pulses once and its check mark glows, the wallet icon pulses once and its red slash flashes, the stopwatch hand holds still. They light up one after another from left to right with small golden sparks and a soft reflection on the floor.", DIG),
 ("12", "s10", "10-qator: Har gal so'rang: bundan kim foyda ko'radi?", "chuqurga tepadan yaqinlashish", "slow push-in down toward the pit",
  "Golden coins keep pouring in a steady stream from the pipe into the dark pit, bouncing and clinking, the pile at the bottom grows, the faint red glow pulses, sparks rise.", DIG),
 ("13", "s11", "11-qator: Shubhali post yoki vakansiya matnini botimizga yuboring: @sahiychishopbot...", "telefonga sekin yaqinlashish, ekran kadrni egallaydi", "slow push-in until the phone screen fills the frame",
  "The four golden corner marks close in slightly as if scanning, a soft golden line sweeps down over the blurred document, then the golden check mark pulses with sparks. The lower third of the frame stays calm and empty.", DIG),
]
e = html.escape
def vp(n, img, cam, act, style):
    start = KEEP if img else ""
    return f"Vertical 9:16, 8 seconds. {start}Camera: {cam}. {act} {style}{NEG}"
def card(n, img, voice, camuz, cam, act, style):
    fig = f'<figure class="sc"><img src="web/{img}.webp" alt="{n}-kadr rasmi"><figcaption>Veo\'ga birinchi kadr: {img}.png</figcaption></figure>' if img else ''
    body = f"""<div class="txt"><span class="lbl">Ovoz</span><p class="voice">{e(voice)}</p><span class="lbl">Kamera: {e(camuz)}</span>
<pre id="v{n}">{e(vp(n, img, cam, act, style))}</pre><button class="copy" data-t="v{n}">Nusxa olish</button></div>"""
    return f"""<article class="card"><header><span class="num">{n}</span><h2>{n}-klip — 9:16 (tik), 8 s</h2></header><div class="row">{fig}{body}</div></article>"""
cards = "".join(card(n, img, v, cu, ce, a, st) for n, img, v, cu, ce, a, st in S)
css = open('/tmp/css_block.txt').read()
css = css.replace("</style>", ".row{display:grid;grid-template-columns:190px minmax(0,1fr);gap:16px;align-items:start}\n@media (max-width:560px){.row{grid-template-columns:minmax(0,1fr)} .sc{max-width:240px}}\n.sc{margin:0;display:grid;gap:6px} .sc img{width:100%;border-radius:4px;display:block;border:1px solid var(--line)} .sc figcaption{font-size:12px;color:var(--muted);font-family:var(--mono)}\n.txt{min-width:0;display:flex;flex-direction:column;gap:8px}\n</style>")
page = f"""<title>490 million sahnalari</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Manrope:wght@400;600&family=JetBrains+Mono:wght@400&display=swap">
{css}
<div class="wrap">
<h1>«Oyiga 490 million» <em>sahnalari</em></h1>
<p class="intro">13 ta klip uchun Veo promptlari. Hammasida: Veo'da «Frames to video» tanlang, rasmni <b>birinchi kadr</b> qilib yuklang, <b>9:16</b> va <b>8 soniya</b> qo'ying, «Nusxa olish» bilan promptni qo'ying. Rasm biriktirilgani uchun Veo boshqa joy chizmaydi va yozuv qo'shmaydi. 1-klipda avtobus, 2-klipda qiz telefonda, 3-klip telefon ichi. Montajda bu uchtasidan 4–5 soniyadan olinadi, shuning uchun 1-qator ovozga mos tushadi. Odam yuzi faqat 2-klipda (qiz), qolganlarida yo'q yoki orqadan.</p>
{cards}
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
print(len(S), "klip; eng uzun prompt:", max(len(vp(n, i, ce, a, st).split()) for n, i, _, _, ce, a, st in S), "so'z")
