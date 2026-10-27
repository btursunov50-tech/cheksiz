# «70 foiz chegirma» — 12 sahna rasm promptlari sahifasi (ChatGPT, 9:16).
# Har promptga kerakli qahramonlarning alohida 9:16 namuna rasmi biriktiriladi (img/ref_usta.png, img/ref_diyor.png); sahifada prompt yonida turadi.
# Ishlatish: python3 video/chegirma/rasm_promptlar.py → video/chegirma/rasmlar.html (+ web/ref_*.webp)
# Rang (egasi, 2026-10-26): Kalamushqir'dan faqat ranglar, bitta kadrda 2–3 ta. Hayajonli joylarda plan + mimika yoziladi (2026-10-26).
# Yorliq, taymer, raqamlar rasmda bo'sh — «-70%», «300 000», «-43%» va h.k. montajda yoziladi.
import html

IMG = {   # egasi yuborgan sahna rasmlari: n → [("s01", "izoh"), ...]
 1: [("s01", "✅ tanlandi (C, bulutli, img/s01.png)")],
 2: [("s02", "✅ tasdiqlandi (B, img/s02.png)")],
 9: [("s09", "✅ tasdiqlandi (img/s09.png)")],
 10: [("s10", "✅ tasdiqlandi (img/s10.png)")],
 11: [("s11", "✅ tasdiqlandi (img/s11.png)")],
 12: [("s12", "✅ tasdiqlandi (img/s12.png)")],
 8: [("s08", "✅ tasdiqlandi (img/s08.png)")],
 7: [("s07", "✅ tasdiqlandi (img/s07.png)")],
 6: [("s06", "✅ tasdiqlandi (tahrirdan keyin, img/s06.png)")],
 5: [("s05", "✅ tasdiqlandi · Nike belgisi tozalandi (img/s05.png)")],
 4: [("s04", "✅ tasdiqlandi (img/s04.png)")],
 3: [("s03", "✅ tasdiqlandi (img/s03.png)")],
}
NOTE = {
 2: "A variantda Diyorning nuri pushti bo'lib qolgan edi (rad). B: moviy nur joyida, yuz namunadek, bir qo'li bannerni ko'rsatadi, ikkinchisida hamyon o'rniga telefon — 4-sahnadagi hamyon bilan kichik farq, sezilmaydi. Krossovkada juda xira belgi.",
 9: "Diyor yuzi namunadek, xotirjam ayyorona tabassum; moviy nur joyida. Do'kondan ko'chaga chiqyapti: bir qo'li hamyonni cho'ntakka qaytaradi, biri telefonda kalkulyator (ekranida raqam yo'q). Orqada bulutli ko'cha, yuzsiz odamlar. Ranglar: yalpiz yashil, bulutli ko'k. Javondagi krossovkalarda kichik Nike chiziqlari bor — orqa fonda, Veo'dan oldin ko'rib chiqiladi.",
 10: "Qiz (o'ylab topilgan): uzun qora o'rim soch, pushti-yalpiz atlas ko'ylak, oq sumka; yonidan ko'rinadi, yuzi qisman, Usta va Diyornikidan butunlay boshqa. Diyor yuzi namunadek, boshini qizga burib «sevib qolgan» qiyofada jilmayadi, qo'lida telefon, moviy nur joyida. Usta yuzi namunadek, ayyorona kulib, o'ng qo'lini Diyorning yelkasiga turtishga ko'targan, chap qo'li belbog'ida. Bulutli ko'cha, nam yo'lak, pushti va yashil vitrinalar.",
 12: "Usta o'ng qo'lida telefon (ekranda pushti yorliq surati va bo'sh pufakchalar), chap qo'li Diyorning yelkasida; Diyor bosh barmog'ini ko'taradi, ikkinchi qo'li cho'ntakda. Ikkala yuz namunadek. Moviy nur sochida, xudida xira. Tepada katta bulutli osmon — @sahiychishopbot uchun joy. Ekran tepasida mayda o'qilmaydigan yozuv — montajda bot suhbati ustiga qo'yiladi.",
 11: "Usta yaqin planda kameraga qaraydi, iliq tabassum; do'ppi, soqol namunadek. Ko'z atrofida yengil chiziqlar — boshqa sahnalardan biroz realistikroq/kattaroq ko'rinadi, lekin o'sha odam. Qo'llar kadrda yo'q. Bir tomonda sariq vitrina nuri, orqada bulutli ko'cha.",
 8: "Usta yuzi namunadek. O'ng qo'lda aniq 3 barmoq (bosh barmoq jimjiloqni ushlagan), chap qo'l pastda; ikkalasi yosh. Tepada 3 belgi: sariq lupa, ko'k o'lchov lentasi, pushti savol belgisi — yozuvsiz. Orqada eshikdan bulutli ko'cha, yuzsiz odamlar. Ranglar: sariq, ko'k, pushti. Lentada o'qilmaydigan mayda chiziqlar — normal.",
 7: "Usta yuzi namunadek; kaftini kameraga ochib «shoshilma» deydi — 5 barmoq, yosh qo'l. Oldinda kassada pushti neon taymer, ekrani bo'sh (montajda «faqat bugun 00:59:59»). Ranglar: pushti, binafsha. Chapdagi krossovkalar juda xira, belgi ko'rinmaydi.",
 6: "Diyor yuzi namunadek: hayron, bir qoshi ko'tarilgan, lablari qisilgan. Qo'llar: chap qo'lda 5 barmoq ochiq, o'ng qo'l ko'rsatkich barmog'i bilan sanaydi — to'g'ri. Binafsha neon oyna, sariq javonlar. Kamchilik: Diyorning nuri moviy emas, binafsharang tusga kirgan (atrofdagi binafsha nurdan) — 2-sahnadagi pushtichalik emas; Tahrirdan keyin (B) nur moviy, qolgan hamma narsa o'zgarmagan. Orqadagi krossovkalar juda xira, belgi ko'rinmaydi.",
 5: "Usta yuzi namunadek, ayyorona tabassum, kameraga qaraydi. Ikki qo'li pushti yorliqni qopqoqdek ko'tarib turibdi, ostidan sariq yorliq ochilgan (bo'sh — montajda «-43%»). Oq krossovkalarda aniq Nike belgisi (yon tomonida va tilida) bor edi — Claude tozaladi. Ranglar: pushti, sariq.",
 4: "Diyor yuzi namunadek: o'ylanib, biroz uyalib yuqoriga qaraydi, og'zi yarim ochiq; moviy nur joyida. Telefonni jinsi cho'ntagiga qaytaradi (2-sahnadagi telefon bilan mos), ikkinchi qo'li sumka tasmasida. Promptda yo'q bo'lsa ham orqada Usta turibdi: qo'llari qovushtirilgan, shubha bilan yon qaraydi, yuzi namunaga mos — 3-sahna bilan uzviy. Ranglar: yalpiz yashil, bulutli ko'k.",
 3: "Usta yuzi namunadek, qo'llari qovushtirilgan (ikkala qo'l), do'kon ichi: yalpiz yashil va sariq javonlar, oynadan bulutli ko'cha va yuzsiz odamlar. Diyor faqat orqasidan, moviy nur sochida. Ranglar: yashil, sariq.",
 1: "4 variant solishtirildi (A, B — quyoshli; C, D — bulutli). C tanlandi: yuz namunaga eng yaqin, orqadagi odamlar soyabon bilan, orqasidan, yuzsiz; yo'lak nam, osmon bulutli. Qo'llar yosh, ikkita. Krossovkadagi xira belgi montajdan oldin tozalanadi.",
}

REFN = {"usta": "Usta", "diyor": "Diyor"}
NEED = {1: ["usta"], 2: ["diyor"], 3: ["usta", "diyor"], 4: ["diyor"], 5: ["usta"], 6: ["diyor"],
        7: ["usta"], 8: ["usta"], 9: ["diyor"], 10: ["usta", "diyor"], 11: ["usta"], 12: ["usta", "diyor"]}
def att(n):
    names = [REFN[k] for k in NEED[n]]
    lst = " and ".join(names)
    return (f"Attach the reference image{'s' if len(names) > 1 else ''} of {lst}. Keep every character exactly as in "
            f"{'their reference images' if len(names) > 1 else 'the reference image'}: the same face, age, hair, beard, clothes and props.")

# Rang palitrasi: har sahnada faqat 2–3 tasi.
COL = {"yellow": "warm golden yellow", "blue": "deep night blue", "red": "rich red", "cyan": "bright cyan-blue",
       "orange": "glowing orange", "teal": "emerald teal"}
COL.update({"sky": "cool cloudy grey-blue", "coral": "hot coral pink", "mint": "fresh mint green", "sun": "bright lemon-sun yellow", "violet": "soft violet"})
UZC = {"sky": "bulutli ko'k", "coral": "pushti-marjon", "mint": "yalpiz yashil", "sun": "limon sariq", "violet": "binafsha", "yellow": "sariq", "blue": "to'q ko'k", "red": "qizil", "cyan": "moviy", "orange": "to'q sariq", "teal": "zumrad"}
def sty(cols):
    c = ", ".join(COL[k] for k in cols[:-1]) + " and " + COL[cols[-1]]
    return (f"Style: the same hand-painted illustration style as the reference images (painterly ink and paint, visible brush texture, "
            f"cinematic soft daylight under a cloudy sky), a little darker and moodier, but still colourful and eye-catching: the coloured signs and shop lights glow against the grey day. Colour rule: the whole frame uses ONLY {len(cols)} main colours: {c}; "
            f"everything else is soft dark neutral shadow. Strong, saturated, glowing colour light, no rainbow, no other bright colours. "
            f"Vertical 9:16. No text, no letters, no numbers, no logos, no watermark, no subtitles.")

U = ("USTA (the calm man about 30 years old with a short jet-black beard, black-and-white Uzbek doppi skullcap, dark embroidered "
     "chapan robe with a red sash; his hands are the young strong hands of a 30-year-old man, smooth skin, no wrinkles, no swollen veins)")
D = ("DIYOR (the naive guy about 20 years old with messy black hair, big innocent eyes, dark blue hoodie, jeans and sneakers, "
     "outlined with a soft cyan-blue glow)")
HANDS = ("Every person has exactly two arms and two hands, every hand clearly belongs to its own arm and shoulder, no hand does two things at once.")
# v3 (egasi): «juda yorug', ozgina qorong'iroq, bulutli bo'lsin».
# v2 (egasi, 2026-10-27): «oldingi videoga o'xshab qoldi» — kunduz, odamlar yuradigan ko'cha, do'konning tashqarisi va ichi, boshqa ranglar.
STREET = ("a busy modern shopping street in Tashkent on a cloudy late afternoon, overcast sky with heavy grey clouds, soft diffused light, the whole scene a little darker and moodier, wet-looking pavement: wide sidewalk, trees, a few passers-by walking past in the background "
          "(small, softly out of focus, seen from the side or back, no clear faces), shop fronts with big glass doors")
SHOP_IN = ("inside a bright modern clothes and sneaker shop: white walls, light wooden shelves with sneakers, racks of jackets and hoodies, "
           "a glass entrance door with the cloudy street and passers-by visible through it, a few shoppers far in the background, softly out of focus, no clear faces")
SIGN = "a huge blank hot coral pink sale banner with nothing written on it (we add «-70%» later)"
OLD = "a small blank white card with a thin coral line crossed through it (the old price, written later)"
NEW = "a big blank lemon-yellow price card (the new price, written later)"
PEOPLE = "Background passers-by are small, blurred and faceless; only Usta and Diyor are in focus."

S = [
 (1, "0–6 s", "Usta: Bu 70 foizlik chegirma 70 foiz emas. To'lashdan oldin hisoblang.", ["coral", "sky", "sun"],
  f"Wide shot, slightly low angle, OUTSIDE the shop. {STREET}. Over the shop entrance hangs {SIGN}; next to the door, on a stand, {OLD} and {NEW} above a pair of white sneakers. "
  f"{U} stands on the sidewalk next to the entrance, turned to the camera with a calm, knowing half-smile, the index finger of his right hand pointing up at the coral banner, his left hand relaxed. "
  f"Cloudy grey-blue sky, soft dim daylight, no direct sun. {PEOPLE} {HANDS}"),
 (2, "6–12 s", "Diyor: Usta, qarang! Uch yuz ming edi, bir yuz yetmish ming bo'libdi! Hozir olmasam, yutqazaman!", ["coral", "sun"],
  f"Close-up, eye level, OUTSIDE on the cloudy sidewalk. {D} rushes toward the shop door, overjoyed: eyes wide and shining, eyebrows high, a huge open grin; one hand points at the coral sale banner, "
  f"the other pulls a wallet out of his hoodie pocket. Coral banner light and the warm lemon glow of the shop window on his face; the street with blurred passers-by behind him. {PEOPLE} {HANDS}"),
 (3, "12–17 s", "Usta: Bu narsani chegirmani ko'rishdan oldin ham qidirayotgan edingmi?", ["mint", "sun"],
  f"Over-the-shoulder shot INSIDE the shop, just past the entrance: from behind {D} (we see only his messy hair, shoulder and cyan glow, no face) toward {U}, who stands calm with folded arms "
  f"between racks of hoodies, one eyebrow slightly raised, asking quietly. {SHOP_IN}. Fresh mint green shelves and lemon-yellow light. {PEOPLE} {HANDS}"),
 (4, "17–21 s", "Diyor: Yo'q… Chegirmani ko'rib qoldim.", ["mint", "sky"],
  f"Close-up INSIDE the shop. {D} frozen next to a wall of sneakers, the wallet half out of his pocket, his smile gone, mouth slightly open, eyes looking up and to the side as he thinks, "
  f"a little embarrassed. Mint green shelves, cool grey-blue daylight from the street door behind him. {PEOPLE} {HANDS}"),
 (5, "21–29 s", "Usta: Hisoblaylik. Uch yuz mingdan bir yuz o'ttiz ming tushgan. Bu yetmish emas, qirq uch foiz.", ["coral", "sun"],
  f"Medium close-up INSIDE the shop at the sneaker stand. {U} lifts a big blank coral pink sale tag up with both hands like a lid; underneath it on the stand a smaller blank lemon-yellow card is revealed, glowing "
  f"(we write «-43%» on it later). Usta looks at the camera over the tag with a calm, slightly amused face. {SHOP_IN}. {PEOPLE} {HANDS}"),
 (6, "29–32 s", "Diyor: Unda nega yetmish deb yozishgan?", ["violet", "sun"],
  f"Medium shot INSIDE the shop near a full-length mirror. {D} counts on his fingers, confused: one eyebrow up, head tilted, lips pressed; soft violet light from a neon strip on the shop wall, "
  f"lemon-yellow card glowing behind him. {PEOPLE} {HANDS}"),
 (7, "32–38 s", "Usta: Katta raqam ko'zni, taymer qo'lni shoshiltiradi. Kerakli narsa shoshilishni talab qilmaydi.", ["coral", "violet"],
  f"Close-up INSIDE the shop: a glowing coral pink digital countdown timer on the cash desk, its display blank with no digits (we write «faqat bugun 00:59:59» later); "
  f"behind it, slightly out of focus, {U} raises a calm open palm, saying «slow down». Coral and soft violet light only. {PEOPLE} {HANDS}"),
 (8, "38–48 s", "Usta: Uchta tekshiruv: boshqa do'kondagi narxi qancha? O'lchami, sifati, kafolati bir xilmi? Va shu mahsulot senga kecha ham kerakmidi?", ["sky", "sun", "coral"],
  f"Medium shot INSIDE the shop by the glass door; the cloudy street with blurred passers-by is visible behind him. {U} faces the camera and holds up three fingers of his right hand; his left hand at his side. "
  f"Above his hand float three glowing symbols in a row with no writing: a lemon-yellow magnifying glass, a sky blue measuring tape, a coral question mark. {PEOPLE} {HANDS}"),
 (9, "48–53 s", "Diyor: Demak, avval hisoblayman, keyin olaman.", ["mint", "sky"],
  f"Medium shot, Diyor walking OUT of the shop through the glass door onto the cloudy street. {D} puts his wallet back into his hoodie pocket with one hand and smiles a relaxed, clever smile, a small confident nod; "
  f"his other hand holds his phone showing a plain calculator screen with no digits. Mint green shop sign light and a cloudy grey-blue sky; passers-by blurred on the street. {PEOPLE} {HANDS}"),
 (10, "53–66 s", "Diyor qizga qarab qoladi. Usta: Hoy-hoy, Diyor! Sen do'konda chegirma qidiryapsanmi yoki ko'chada kelin? — Diyor: Yo'q, usta... men... hisoblayapman! — Usta: Ko'zing narxda bo'lsin, ukam. Avval hisob, keyin kelin!", ["coral", "mint", "sky"],
  f"Medium-wide shot OUTSIDE on the cloudy sidewalk in front of the shop. In the foreground on the right a fictional young Uzbek woman about 22 years old walks past to the right, seen from the side and three-quarter back, "
  f"her face only partly visible: very long glossy black hair in one long braid down her back, an elegant modest long-sleeved Uzbek atlas (ikat) dress with a coral and mint pattern, a small handbag; she looks ahead and does not notice anyone. "
  f"In the middle {D} has stopped dead with his phone in one hand, his head turned after her, staring with a dreamy, love-struck face: eyebrows raised, eyes soft and wide, mouth slightly open, a goofy smile; his other hand hangs loose. "
  f"Right behind him {U} leans in with an amused, mock-strict face, one eyebrow high, a knowing smile, his right hand raised about to tap Diyor on the shoulder, his left hand on his own sash. "
  f"Cloudy grey-blue sky, wet pavement, the coral shop banner glowing. Other passers-by are small, blurred and faceless. {HANDS}"),
 (11, "66–71 s", "Usta: Xaridni foiz emas, ehtiyoj hal qilsin.", ["sun", "sky"],
  f"Close-up portrait OUTSIDE on the street, eye level. {U} looks straight into the camera with a warm, wise smile; warm lemon light from a shop window on one side of his face, cool cloudy grey-blue daylight on the other, "
  f"the busy street softly blurred. His hands are not in the frame. {PEOPLE}"),
 (12, "71–81 s", "Usta: Chegirma yorlig'ini suratga olib botimizga yuboring: @sahiychishopbot. Haqiqiy foizni hisoblab, nimani tekshirishni aytib beradi.", ["sky", "sun", "mint"],
  f"Medium shot OUTSIDE on the sidewalk in front of the shop. {U} holds a smartphone toward the camera with his right hand; the screen glows mint green with a chat: a photo of a blank coral sale tag and a few empty message bubbles, "
  f"no readable text. His left hand rests on the shoulder of {D}, who stands beside him and gives a thumbs up with one hand. Cloudy grey-blue sky, soft dim daylight, blurred passers-by. "
  f"Leave empty cloudy sky in the top third of the frame for a title. {PEOPLE} {HANDS}"),
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
.sw-sky{{background:#5ab8f0}} .sw-coral{{background:#ff5e7e;color:var(--fg)}} .sw-mint{{background:#4fd6a0}} .sw-sun{{background:#ffe14d}} .sw-violet{{background:#9b7bff;color:var(--fg)}}
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
