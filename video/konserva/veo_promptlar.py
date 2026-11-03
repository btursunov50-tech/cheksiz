# «Konserva» — Veo matndan-video promptlari (rasm kerak emas, odam va yuz yo'q) → sahnalar.html (Artifact, nusxa tugmasi).
# Ishlatish: python3 video/konserva/veo_promptlar.py
import html, os
D = os.path.dirname(os.path.abspath(__file__))
STYLE = ("Semi-realistic hand-painted cartoon illustration style, rich and detailed, warm golden-hour glow of a Tashkent bazaar with cyan-blue neon lamps. "
         "Only 2-3 main colours in the frame: golden yellow, cyan blue and one accent (red for danger). Nobody appears: no people, no faces, no hands, no human figures, no silhouettes of people. "
         "One continuous shot, no cuts. The camera never stops moving.")
NEG = "Negative: no people, no faces, no hands, no human silhouettes, no text, no letters, no numbers, no Arabic or any other script, no signs, no shop signs, no storefronts, no subtitles, no captions, no logos, no brand marks, no watermarks."
# (raqam, ovoz, kamera uz, kamera en, sahna)
S = [
 ("1", "Bankadagi bir sana «xavfsiz» deydi, boshqasi «mazali». Ular bir xil emas.",
  "bankaga sekin yaqinlashib, o'ngga biroz aylanish",
  "slow push-in from a medium shot to a close-up with a gentle 15-degree orbit to the right",
  "A single shiny tin can stands in the centre of a dark wet counter. On its paper label two small round glowing stamps float: a cyan-blue glowing shield on the left and a golden glowing star on the right, no writing on them. They pulse one after the other, tiny blue and golden sparks rise, the blurred bazaar lamps glow behind."),
 ("2", "Tasavvur qiling: do'konga kirdingiz, bir banka konserva oldingiz. Sanani ko'rdingiz va xotirjam bo'ldingiz.",
  "javon bo'ylab oldinga silliq siljish, bitta bankada to'xtash",
  "smooth forward dolly along a store aisle at shelf height, settling on one tin",
  "Long shelves full of identical tin cans line both sides of a store aisle. Hanging blue neon lamps sway slightly, dust motes drift in the golden light. One tin in the middle of the shelf catches a warm spotlight and the camera slowly settles on it."),
 ("3", "Lekin bu sana aslida nimani bildiradi?",
  "bankaning qopqog'iga tez, lekin silliq yaqinlashish",
  "fast but smooth push-in to an extreme close-up of a tin can's lid",
  "An extreme close-up of the round metal lid of a tin can. A glowing cyan-blue clock dial with only tick marks and no numerals appears above it and its hand turns slowly, then stops as the golden light flickers. A sense of mystery and a question, dark background with soft golden bokeh."),
 ("4", "Birinchidan, yozuvlarning farqini bilib oling. Tayyorlangan sana — mahsulot qachon ishlab chiqarilganini ko'rsatadi. Yaroqlilik muddati — shu sanagacha mahsulot xavfsiz. «Eng yaxshi sifatgacha» — bu sifat sanasi.",
  "bankaning atrofida chapga sekin aylanish",
  "slow orbit to the left around the tin can",
  "A tin can on the wet counter with its paper label peeled open like a page. Three glowing round icons rise one after another from the label, each lighting up for about two seconds: a golden gear, a cyan-blue shield, a golden star. The icons have no writing. Reflections ripple on the wet counter."),
 ("4b", "(4-sahnaning davomi: «Yaroqlilik muddati — shu sanagacha mahsulot xavfsiz. «Eng yaxshi sifatgacha» — bu sifat sanasi.»)",
  "ikki belgiga sekin yaqinlashish va to'xtash",
  "slow push-in toward two large glowing symbols, then hold",
  "Two large glowing round symbols hang side by side above a wet counter in a dark bazaar: a steady cyan-blue shield on the left and a golden star on the right. The shield stays calm and solid, the star flickers softly like a candle, and a thin line of light connects them and splits in two. Their reflections ripple on the counter, tiny blue and golden sparks rise. The symbols carry no writing."),
 ("5", "Muddati o'tgan mahsulotni yemang.",
  "tez yaqinlashib, qotib turish",
  "snap push-in, then hold",
  "A dull, old, slightly dented tin can in the centre of the frame. A big glowing red circle with a diagonal slash across it (the universal forbidden sign, no writing) pulses over it, red light flashes on the walls. Hard dramatic contrast, dark background."),
 ("6", "Ikkinchidan, quruq mahsulotga ham ishonavermang. Guruch, makaron va un to'g'ri saqlansa uzoq turadi, lekin namlik va hasharotlar ularni muddatidan oldin buzishi mumkin.",
  "yog'och javon bo'ylab o'ngga sekin surilish",
  "slow pan right across a wooden kitchen shelf",
  "A wooden kitchen shelf with glass jars of rice, pasta and a paper bag of flour. Water droplets condense and run down the jar glass, the flour bag has damp dark stains, and small cartoon beetles crawl out of a crack of the bag. The camera ends on the beetles. Golden light with blue shadows."),
 ("7", "Uchinchidan, bankaga qarang. Shishgan, oqayotgan, qattiq zanglagan yoki choklari shikastlangan bo'lsa, yemang.",
  "pastdan, banka qatori bo'ylab sirpanib, shishgan bankaga yaqinlashish",
  "low-angle tracking move along a row of tins, ending in a slow push-in on the swollen one",
  "A row of identical clean tin cans on a shelf. The can in the middle has a swollen, domed lid, rust streaks along its seam and a drop of dark liquid slowly leaking down its side. A red glow pulses around it while the other cans stay normal."),
 ("8", "Eng xavflisi botulizm: og'ir zaharlanishga olib keladigan kasallik. Xavfli konserva ba'zan tashqaridan bilinmaydi. Shuning uchun shubhali konservani tatib ko'rib tekshirmang.",
  "bankaga yaqinlashib, devor ichiga «kirib», yana chiqish",
  "slow push-in that passes through the can wall like a cutaway, then a slow pull-out",
  "A plain silver tin can with NO label and no writing of any kind stands alone on a dark wooden table; the background is only soft blurred warm golden lights, no street, no shop, no signs, no people. The can looks perfectly normal from outside. The camera passes through its wall like a cutaway: inside it is dark and a faint sickly green glow shows tiny stylised spores floating and multiplying. The camera then pulls back out and the can looks completely normal again. Red accent, dark moody lighting."),
 ("9", "To'rtinchidan, sut mahsulotlari. Hidi yoki ko'rinishi o'zgargan bo'lsa, ichmang. Hid normal bo'lsa ham, bu to'liq xavfsizlikni kafolatlamaydi.",
  "tepadan sekin pastga tushish",
  "slow crane-down from above toward the glass bottle",
  "A glass bottle of milk on a counter in the cold glow of a store fridge. At first the milk looks normal, then a slight yellow tint and small curdled swirls form inside while an amber warning light slowly pulses. Calm, serious mood."),
 ("9b", "(9-sahnaning davomi: «Hid normal bo'lsa ham, bu to'liq xavfsizlikni kafolatlamaydi.»)",
  "ikki stakan orasidan sekin yaqinlashish",
  "slow push-in between two glasses, ending on a close-up of the right one",
  "Two identical glasses of milk stand side by side on a plain cyan-tiled counter in cold fridge light; the background is only soft blurred golden and blue bokeh lights, no shop, no signs, no people, no silhouettes. They look exactly the same. As the camera comes closer, inside the right glass tiny glowing red particles become visible, drifting in the milk. An amber warning light pulses softly. Calm, serious mood."),
 ("10", "Do'konda esa uchta ish qiling. Sanani tekshiring. Qadoq butunligiga ishonch hosil qiling. Saqlash shartlariga amal qiling.",
  "javon bo'ylab sekin orqaga chekinish",
  "gentle dolly back along the aisle",
  "In a store aisle three glowing icons float at eye level and light up one after another with a ring of golden sparks: a rectangular label with only tick marks and no numerals, a perfectly round intact tin can outline, a snowflake. All three icons are cyan-blue with golden edges and carry no writing."),
 ("11", "Arzon ekan deb shubhali mahsulotni sotib olmang. Pulni tejash mumkin, lekin sog'liqni xavf ostiga qo'yishga arzimaydi.",
  "tarozining ustiga sekin yaqinlashish",
  "slow push-in on a balance scale",
  "A brass balance scale on a counter. The left pan holds a small pile of golden coins, the right pan holds a glowing red heart. The heart side sinks heavily, the coins rise and some slide off and fall with golden sparks. Warm light, blue neon in the blurred background."),
 ("12", "Mahsulot yorlig'ining suratini botimizga yuboring: @sahiychishopbot. Yozuvlar nimani bildirishini tushuntirib, tekshirishni bosqichma-bosqich o'rgatadi.",
  "telefonga sekin yaqinlashib, ekran butun kadrni egallaydi",
  "slow push-in toward a smartphone until its screen fills the frame",
  "A smartphone stands upright on a store shelf with its screen facing the camera. On the screen a glowing cyan-blue frame scans a photo of a tin can, a thin scanning line sweeps down, and then a glowing golden check mark symbol appears. No writing on the screen. The lower third of the frame stays calm and empty."),
 ("13", "Videoni yaqinlaringizga ham yuboring: balki kimnidir jiddiy xatodan asrab qolar.",
  "telefondan ko'tarilib, orqaga chekinib shaharga qarash",
  "smooth crane up and pull-back from the phone to a wide view of the city",
  "From the phone glowing cyan-blue paper-plane shapes fly out and arc toward the distant windows of a Tashkent neighbourhood at golden hour. One by one warm golden lights switch on in the windows. The TV tower stands in the evening sky. The mood is warm and hopeful."),
]
DUR = 8
def vp(cam, scene):
    return f"Vertical 9:16, {DUR} seconds. Camera: {cam}. {scene} {STYLE} {NEG}"
e = html.escape
cards = "".join(f"""<article class="card"><header><span class="num">{n}</span><h2>{n}-sahna — 9:16 (tik), {DUR} s</h2></header>
<span class="lbl">Ovoz</span><p class="voice">{e(v)}</p><span class="lbl">Kamera: {e(cu)}</span>
<pre id="v{n}">{e(vp(ce, sc))}</pre><button class="copy" data-t="v{n}">Nusxa olish</button></article>""" for n, v, cu, ce, sc in S)
page = f"""<title>Konserva sahnalari</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Manrope:wght@400;600&family=JetBrains+Mono:wght@400&display=swap">
<style>
/* Layout: one column of prompt cards; deliberately one dark look with gold accents, same family as the other scene pages. */
:root{{--bg:#0f1116;--card:#181b23;--line:#2c3140;--fg:#eef0f5;--muted:#a7b0c4;--gold:#f2b544;--mint:#5fd3a6;
--display:"Cormorant Garamond",Georgia,serif;--body:"Manrope",system-ui,sans-serif;--mono:"JetBrains Mono",ui-monospace,monospace;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font-family:var(--body);font-size:15px;line-height:1.55;margin:0;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
.wrap{{max-width:780px;margin:0 auto;padding-block:28px 60px;display:grid;gap:22px}}
h1{{font-family:var(--display);font-weight:700;font-size:clamp(30px,6vw,44px);margin:0;line-height:1.1;text-wrap:balance}} h1 em{{font-style:normal;color:var(--gold)}}
.intro{{color:var(--muted);margin:0;max-width:64ch}}
.card{{display:grid;gap:10px;background:var(--card);border:1px solid var(--line);border-radius:8px;padding:16px;min-width:0}}
header{{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}} .num{{font-family:var(--mono);color:var(--gold);font-size:14px}}
h2{{font-family:var(--display);font-weight:700;font-size:26px;margin:0}}
.lbl{{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}}
.voice{{margin:0;font-style:italic}}
pre{{margin:0;white-space:pre-wrap;word-break:break-word;font-family:var(--mono);font-size:12.5px;line-height:1.6;background:var(--bg);border:1px solid var(--line);border-radius:6px;padding:12px;user-select:all}}
.copy{{justify-self:start;font:600 15px var(--body);color:#111;background:var(--gold);border:0;border-radius:8px;padding:10px 18px;cursor:pointer}} .copy.done{{background:var(--mint)}} .copy:focus-visible{{outline:2px solid var(--fg);outline-offset:2px}}
</style>
<div class="wrap">
<h1>«Konserva» <em>sahnalari</em></h1>
<p class="intro">Rasm kerak emas: Veo'da «Text to video» tanlang, <b>9:16</b> va <b>8 soniya</b> qo'ying, «Nusxa olish» bilan promptni qo'ying. Hamma sahnada odam, yuz va qo'l yo'q, yozuv va raqam yo'q (belgilar faqat rasm). Har prompt to'liq, uslub matni har birida takrorlangan. Ovoz Manus'dan keldi, ba'zi qatorlar uzun chiqdi: 4 va 9-sahna ikkitadan klip (4+4b va 9+9b, jami 16 s). 6, 8 va 12-sahna bitta klip, montajda 1,3–1,6 marta sekinlashtiriladi. Klip kelgach tekshiraman.</p>
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
print(len(S), "sahna; eng uzun prompt:", max(len(vp(ce, sc).split()) for _, _, _, ce, sc in S), "so'z")
