# «Oyiga 490 million» — rasm promptlari (ChatGPT/rasm yaratish, 9:16, odamsiz) → rasmlar.html (Artifact, nusxa tugmasi). Ssenariy: ideas/ish-taklifi.md
# Ishlatish: python3 video/ish-taklifi/rasm_promptlar.py
import html, os
D = os.path.dirname(os.path.abspath(__file__))
STYLE = ("Semi-realistic hand-painted cartoon illustration, rich detail, warm golden glow with cyan-blue neon accents. Only 2-3 main colours in the frame: golden yellow, cyan blue and one accent colour (red where it says danger). "
         "The background is only softly blurred bokeh lights and plain surfaces, never a readable street, shop, sign or building front. "
         "Nobody appears: no people, no faces, no hands, no human silhouettes. No text, no letters, no numbers, no words in any language, no logos, no brand marks, no watermarks.")
STYLE_R = ("Photorealistic cinematic photograph, natural light, shot on a 35mm lens, shallow depth of field, rich warm golden-hour tones with cyan-blue accents, high detail, no cartoon look. "
           "All people are fictional (no real person, no celebrity). No text, no letters, no numbers, no words in any language, no route numbers, no signs, no shop signs, no logos, no brand marks, no watermarks. Phones and screens show only abstract glowing shapes, never readable writing.")
FMT = "Vertical 9:16 image (1080x1920)."
# (raqam, ovoz, kadr (uz), sahna)
S = [
 ("1a", "Oyiga to'rt yuz to'qson million so'm. Tajriba shart emas. Ariza topshirasizmi?", "tashqaridan avtobus, o'rtacha plan (REALISTIK, 1-kadr boshlanishi)", "R",
  "Medium-wide shot at golden hour on a wide poplar-lined boulevard in Tashkent: a modern city bus drives along the street seen from a low front-three-quarter angle, its large windows glowing warmly and passengers visible as soft shapes behind the glass. The bus body is plain white with a plain blue stripe and no route number and no writing. Mid-century apartment blocks and the Tashkent TV tower far away in the haze, cars motion-blurred, no shop signs. Warm sunset light. Neon: a thin bright cyan-blue neon light line traces the edges of the bus body, the roof line, the window frames and the wheel arches like a glowing outline, the street lamps along the boulevard glow with cyan-blue neon rings, and thin cyan neon lines run along the kerb and road markings, all reflected on the glass and the road. Neon lines only, no neon signs and no writing."),
 ("1b", "(1-kadrning davomi: avtobus ichida qiz telefonga qaraydi)", "avtobus ichi, qizning yuzi va telefon, yaqin plan (REALISTIK, 2-kadr boshlanishi)", "R",
  "Close-up inside a city bus in Tashkent. A beautiful young Uzbek woman of about 22 with long dark hair, soft natural makeup and a light elegant outfit sits by the window looking down at her smartphone. Her face is lit by the cyan-blue glow of the screen and by warm golden sunset light through the window. Other passengers are only soft out-of-focus shapes in the background, the street blurred outside. The phone screen shows only an abstract glowing layout, no readable writing, no logo on the phone. Natural, calm, slightly curious expression. Neon: a thin bright cyan-blue neon LED strip runs along the bus window frame and the ceiling edge, the handrail glows with a thin cyan neon line, the phone has a glowing cyan neon edge and a soft cyan neon rim light outlines her hair and shoulder."),
 ("1c", "(2-kadrning oxiri: kamera telefon ichiga kiradi)", "telefon ekrani butun kadrda, yaqin plan (RAQAMLI uslub)", "S",
  "Extreme close-up. A smartphone screen fills the whole frame and glows like a portal: an abstract social post layout of soft blurred lines and a big glowing golden coin shape in the middle, cyan-blue neon edges, golden sparks rising out of the screen. Dark glossy glass reflections at the borders of the frame."),
 ("2", "Post shunday deydi: Claude odamlarni masofaviy ishga taklif qilmoqda, ariza 22-noyabrgacha, vazifa — sun'iy intellektni aylanib o'tish.", "uchta belgi, o'rtacha plan", "S",
  "Medium shot. Three glowing round icons float side by side above a dark glossy surface: a laptop outline, a microchip with circuit lines, and a blank calendar page with a grid of empty squares and no numerals. Cyan-blue neon outlines with golden inner glow, small sparks between them."),
 ("3", "Men, Claude, o'zim tekshirdim. Bunday vakansiya topilmadi.", "lupa va yo'qolayotgan qog'oz, yaqin plan", "S",
  "Close-up. A large magnifying glass with a brass rim hovers over a sheet of paper made of blurred empty lines. Under the lens the paper dissolves into golden dust and sparks and nothing is left of it. Cyan-blue light reflects in the glass, dark warm background with soft bokeh."),
 ("4", "Lekin asosi haqiqiy: Anthropic'da xavfsizlik dasturi bor. Tadqiqotchilar Claude'ning himoyasidagi zaif joyni topib, kompaniyaga yashirin xabar beradi va mukofot oladi.", "qalqon, qulf va kalit, past burchak", "S",
  "Low-angle medium shot. A big glowing cyan-blue shield with a golden padlock in its centre stands on a dark glossy surface. A small golden key hovers near the lock with sparks. The shield is solid and strong, reflections on the surface, soft golden bokeh behind."),
 ("5", "Bu oylik maosh emas. Bu topilgan har bir zaiflik uchun mukofot, eng ko'pi taxminan o'ttiz besh ming dollar.", "taqvim va bitta tangalar uyumi, yuqoridan", "S",
  "High-angle medium shot. An empty calendar page with a grid of blank squares, no numerals, lies on a dark glossy surface. A single stack of golden coins stands on just one square while other squares stay empty. A few golden sparks rise. Cyan-blue edge glow on the calendar."),
 ("6", "Va «tajribasiz» ham emas: yangi zaiflikni topish uchun chuqur bilim kerak. Postning o'zi ham muhandislar va olimlarni afzal ko'radi.", "ulkan murakkab qulf, keng plan", "S",
  "Wide shot. A huge intricate mechanical vault lock made of many interlocking gears, rings and cogs glows in cyan-blue and gold. In front of it lies one tiny plain key that is far too small. Dark plain background with soft golden bokeh, a sense of scale and difficulty."),
 ("7", "Qizil bayroqlar: manba yo'q, havola yo'q, «shoshiling» muddati, va «kimga yuborishni bilasiz» degan klik tuzog'i.", "avtobus ichida telefonlar zanjiri, orqadan o'rtacha plan (REALISTIK)", "R",
  "Medium shot inside a city bus in Tashkent filmed from behind the seats. Several passengers hold their smartphones and every screen glows cyan-blue; only the backs of heads and shoulders are visible, no faces. Thin glowing cyan lines connect the lit screens one to another like a spreading network, and above the seat backs three small red flags float and glow. Warm golden light through the windows, soft focus, calm cinematic mood. Neon: thin bright cyan-blue neon LED strips run along the ceiling and the handrails of the bus, and the whole bus interior is outlined by glowing cyan neon lines. No neon signs and no writing."),
 ("8", "Firibgarlar aynan shunday e'lon bilan pasport, karta va tasdiq kodini so'raydi, yoki oldindan pul oladi.", "ekran qorong'u ko'lmakdek, ilgakli tanga, yaqin plan (RAQAMLI uslub, «phishing = baliq tutish»)", "S",
  "Macro close-up. A smartphone lies flat on a dark surface and its glowing screen has turned into a dark pond. A shiny golden coin hangs on a fishing hook from a thin line just above the water surface with small ripples. A blank passport-style booklet with a plain globe emblem and a blank bank card shape with no numbers rise toward the coin like fish. A faint red glow under the water. Cyan-blue and golden light, dark moody background."),
 ("9", "Uchta qoida. Vakansiyani faqat kompaniyaning rasmiy saytidan tekshiring. Ish beruvchi oldindan pul, karta yoki kod so'ramaydi. Shoshiltirsa, to'xtang.", "uchta belgi, o'rtacha plan", "S",
  "Medium shot. Three glowing round icons float side by side: a globe with a golden check mark, a wallet with a red slanted slash across it, and a stopwatch with its hand paused. Cyan-blue outlines, golden inner glow, red only on the slash. No numerals on the stopwatch, only tick marks."),
 ("10", "Har gal so'rang: bundan kim foyda ko'radi?", "tangalar chuqurga oqib tushadi, yuqoridan pastga", "S",
  "High-angle shot looking down. A stream of golden coins pours from a glowing pipe into a dark circular pit in the middle of a plain dark floor. A faint red glow rises from the pit. Cyan-blue soft rim light on the pipe, golden sparks."),
 ("11", "Shubhali post yoki vakansiya matnini botimizga yuboring. Qizil bayroqlarni topib, qanday tekshirishni bosqichma-bosqich o'rgatadi.", "telefon, o'rtacha plan, pastki uchdan bir qism bo'sh", "S",
  "Medium shot. A smartphone stands upright on a dark glossy shelf with its screen facing the camera. On the screen a glowing cyan-blue scanning frame sits around a blurred empty document and a golden check mark symbol glows beside it, no writing. The lower third of the image stays calm and empty. Soft golden bokeh behind."),
]
e = html.escape
def p(sc, st): return f"{FMT} {sc} {STYLE_R if st == 'R' else STYLE}"
cards = "".join(f"""<article class="card"><header><span class="num">{n}</span><h2>{n}-sahna — 9:16 (tik), rasm</h2></header>
<span class="lbl">Ovoz</span><p class="voice">{e(v)}</p><span class="lbl">Kadr: {e(k)}</span>
<pre id="p{n}">{e(p(sc, st))}</pre><button class="copy" data-t="p{n}">Nusxa olish</button></article>""" for n, v, k, st, sc in S)
css = open('/tmp/css_block.txt').read().replace("<style>", "<style>\n/* Layout: one column of prompt cards; single dark look with gold accents, same family as the other scene pages. */")
page = f"""<title>490 million rasmlari</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Manrope:wght@400;600&family=JetBrains+Mono:wght@400&display=swap">
{css}
<div class="wrap">
<h1>«Oyiga 490 million» <em>rasmlari</em></h1>
<p class="intro">Rasm promptlari (ChatGPT yoki boshqa rasm yaratuvchi, <b>9:16</b>). <b>REALISTIK</b> sahnalar (1a, 1b, 7): Toshkent avtobusi va fotorealistik qiz. <b>RAQAMLI</b> sahnalar (1c, 8 va qolganlari): telefon ichidagi dunyo, yorqin neon uslubi. Bu aralashma ataylab: tashqi dunyo realistik, telefon ichi raqamli. Qiz va yo'lovchilar to'qima (haqiqiy odam emas). Hamma sahnada yozuv va raqam yo'q: «490», qoidalar va bot nomi montajda kod bilan qo'yiladi. Orqa fon faqat xira yorug'lik: bu rasmlarni keyin Veo'ga birinchi kadr qilib beramiz, shunda Veo boshqa joy chizmaydi. Har prompt to'liq, uslub matni har birida takrorlangan. Rasmlar kelgach yuz, yozuv va ortiqcha narsa bormi tekshiraman.</p>
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
open(os.path.join(D, "rasmlar.html"), "w").write(page)
print(len(S), "sahna; eng uzun prompt:", max(len(p(sc, st).split()) for _, _, _, st, sc in S), "so'z")
