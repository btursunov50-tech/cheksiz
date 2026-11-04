# «Oyiga 490 million» — rasm promptlari (ChatGPT/rasm yaratish, 9:16, odamsiz) → rasmlar.html (Artifact, nusxa tugmasi). Ssenariy: ideas/ish-taklifi.md
# Ishlatish: python3 video/ish-taklifi/rasm_promptlar.py
import html, os
D = os.path.dirname(os.path.abspath(__file__))
STYLE = ("Semi-realistic hand-painted cartoon illustration, rich detail, warm golden glow with cyan-blue neon accents. Only 2-3 main colours in the frame: golden yellow, cyan blue and one accent colour (red where it says danger). "
         "The background is only softly blurred bokeh lights and plain surfaces, never a readable street, shop, sign or building front. "
         "Nobody appears: no people, no faces, no hands, no human silhouettes. No text, no letters, no numbers, no words in any language, no logos, no brand marks, no watermarks.")
FMT = "Vertical 9:16 image (1080x1920)."
# (raqam, ovoz, kadr (uz), sahna)
S = [
 ("1", "Oyiga to'rt yuz to'qson million so'm. Tajriba shart emas. Ariza topshirasizmi?", "o'rtacha plan, pastdan biroz yuqoriga",
  "Medium shot, slightly low angle. A smartphone stands upright on a dark glossy surface, its screen glowing with an abstract social post layout made only of soft blurred lines and a big glowing golden coin shape in the middle. Around the phone a tall stack of shiny golden coins and golden sparks. Cyan-blue neon rim light on the phone edges."),
 ("2", "Post shunday deydi: Claude odamlarni masofaviy ishga taklif qilmoqda, ariza 22-noyabrgacha, vazifa — sun'iy intellektni aylanib o'tish.", "uchta belgi, o'rtacha plan",
  "Medium shot. Three glowing round icons float side by side above a dark glossy surface: a laptop outline, a microchip with circuit lines, and a blank calendar page with a grid of empty squares and no numerals. Cyan-blue neon outlines with golden inner glow, small sparks between them."),
 ("3", "Men, Claude, o'zim tekshirdim. Bunday vakansiya topilmadi.", "lupa va yo'qolayotgan qog'oz, yaqin plan",
  "Close-up. A large magnifying glass with a brass rim hovers over a sheet of paper made of blurred empty lines. Under the lens the paper dissolves into golden dust and sparks and nothing is left of it. Cyan-blue light reflects in the glass, dark warm background with soft bokeh."),
 ("4", "Lekin asosi haqiqiy: Anthropic'da xavfsizlik uchun «bug bounty» dasturi bor. Tadqiqotchilar himoyani aylanib o'tish yo'lini topadi.", "qalqon, qulf va kalit, past burchak",
  "Low-angle medium shot. A big glowing cyan-blue shield with a golden padlock in its centre stands on a dark glossy surface. A small golden key hovers near the lock with sparks. The shield is solid and strong, reflections on the surface, soft golden bokeh behind."),
 ("5", "Bu oylik maosh emas. Bu topilgan har bir zaiflik uchun mukofot, eng ko'pi taxminan o'ttiz besh ming dollar.", "taqvim va bitta tangalar uyumi, yuqoridan",
  "High-angle medium shot. An empty calendar page with a grid of blank squares, no numerals, lies on a dark glossy surface. A single stack of golden coins stands on just one square while other squares stay empty. A few golden sparks rise. Cyan-blue edge glow on the calendar."),
 ("6", "Va «tajribasiz» ham emas: yangi zaiflikni topish uchun chuqur bilim kerak. Postning o'zi ham muhandislar va olimlarni afzal ko'radi.", "ulkan murakkab qulf, keng plan",
  "Wide shot. A huge intricate mechanical vault lock made of many interlocking gears, rings and cogs glows in cyan-blue and gold. In front of it lies one tiny plain key that is far too small. Dark plain background with soft golden bokeh, a sense of scale and difficulty."),
 ("7", "Qizil bayroqlar: manba yo'q, havola yo'q, «shoshiling» muddati, va «kimga yuborishni bilasiz» degan klik tuzog'i.", "uchta qizil bayroq qatorda, o'rtacha plan",
  "Medium shot. Three tall red flags on thin poles stand in a row on a dark plain surface, each flag glowing a little and waving in a slow wind. Behind them only soft blurred golden and cyan bokeh lights. Red is the single accent colour. No symbols on the flags."),
 ("8", "Firibgarlar aynan shunday e'lon bilan pasport, karta va tasdiq kodini so'raydi, yoki oldindan pul oladi.", "ilgakli tanga, tuzoq, o'rtacha plan",
  "Medium shot, slight dutch tilt. A shiny golden coin hangs on a fishing hook from a thin line above a dark open trap box. Inside the box lie a blank passport-style booklet with a plain globe emblem and a blank bank card shape with no numbers. A faint red glow comes from the trap. Dark moody background."),
 ("9", "Uchta qoida. Vakansiyani faqat kompaniyaning rasmiy saytidan tekshiring. Ish beruvchi oldindan pul, karta yoki kod so'ramaydi. Shoshiltirsa, to'xtang.", "uchta belgi, o'rtacha plan",
  "Medium shot. Three glowing round icons float side by side: a globe with a golden check mark, a wallet with a red slanted slash across it, and a stopwatch with its hand paused. Cyan-blue outlines, golden inner glow, red only on the slash. No numerals on the stopwatch, only tick marks."),
 ("10", "Har gal so'rang: bundan kim foyda ko'radi?", "tangalar chuqurga oqib tushadi, yuqoridan pastga",
  "High-angle shot looking down. A stream of golden coins pours from a glowing pipe into a dark circular pit in the middle of a plain dark floor. A faint red glow rises from the pit. Cyan-blue soft rim light on the pipe, golden sparks."),
 ("11", "Shubhali post yoki vakansiya matnini botimizga yuboring. Qizil bayroqlarni topib, qanday tekshirishni bosqichma-bosqich o'rgatadi.", "telefon, o'rtacha plan, pastki uchdan bir qism bo'sh",
  "Medium shot. A smartphone stands upright on a dark glossy shelf with its screen facing the camera. On the screen a glowing cyan-blue scanning frame sits around a blurred empty document and a golden check mark symbol glows beside it, no writing. The lower third of the image stays calm and empty. Soft golden bokeh behind."),
]
e = html.escape
def p(sc): return f"{FMT} {sc} {STYLE}"
cards = "".join(f"""<article class="card"><header><span class="num">{n}</span><h2>{n}-sahna — 9:16 (tik), rasm</h2></header>
<span class="lbl">Ovoz</span><p class="voice">{e(v)}</p><span class="lbl">Kadr: {e(k)}</span>
<pre id="p{n}">{e(p(sc))}</pre><button class="copy" data-t="p{n}">Nusxa olish</button></article>""" for n, v, k, sc in S)
css = open('/tmp/css_block.txt').read().replace("<style>", "<style>\n/* Layout: one column of prompt cards; single dark look with gold accents, same family as the other scene pages. */")
page = f"""<title>490 million rasmlari</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Manrope:wght@400;600&family=JetBrains+Mono:wght@400&display=swap">
{css}
<div class="wrap">
<h1>«Oyiga 490 million» <em>rasmlari</em></h1>
<p class="intro">11 ta sahna uchun rasm promptlari (ChatGPT yoki boshqa rasm yaratuvchi, <b>9:16</b>). Hammasida odam, yuz va qo'l yo'q, yozuv va raqam yo'q: «490», qoidalar va bot nomi montajda kod bilan qo'yiladi. Orqa fon faqat xira yorug'lik: bu rasmlarni keyin Veo'ga birinchi kadr qilib beramiz, shunda Veo boshqa joy chizmaydi. Har prompt to'liq, uslub matni har birida takrorlangan. Rasmlar kelgach yuz, yozuv va ortiqcha narsa bormi tekshiraman.</p>
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
print(len(S), "sahna; eng uzun prompt:", max(len(p(sc).split()) for _, _, _, sc in S), "so'z")
