# «Sovg'a yutdingiz!» — 12 sahna rasm promptlari sahifasi (ChatGPT, 9:16).
# Har promptga qahramonlar varag'i (img/ref_qahramonlar.webp) biriktiriladi; sahifada uning rasmi prompt yonida turadi.
# Ishlatish: python3 video/sovga/rasm_promptlar.py → video/sovga/rasmlar.html (+ web/ref_qahramonlar.webp)
import html, os
# Egasi yuborgan sahna rasmlari: web/sNN<harf>.webp (a, b … variantlar) va izoh.
IMG = {
 1: [("s01", "✅ tasdiqlandi (940×1672)")],
 2: [("s02", "✅ tasdiqlandi (tahrirdan keyin)")],
 3: [("s03", "✅ tasdiqlandi (941×1672)")],
 4: [("s04", "✅ tasdiqlandi")],
 5: [("s05", "✅ tasdiqlandi (tahrirdan keyin)")],
 6: [("s06", "✅ tasdiqlandi")],
 7: [("s07", "✅ tasdiqlandi")],
 8: [("s08", "✅ tasdiqlandi")],
 9: [("s09", "✅ tasdiqlandi")],
 10: [("s10", "✅ tasdiqlandi")],
 11: [("s11", "✅ tasdiqlandi")],
 12: [("s12", "✅ tasdiqlandi")],
}
NOTE = {
 10: "Qum soat oldinda, orqada Diyor yuzini kaftlariga qo'yib quvonadi (2 qo'l). Tepada hali qum bor — videoda oxirgi qum tushib bitadi (Veo prompti).",
 9: "Diyor ekranni bosadi, Tulki qizil girdob bilan telefonga tortiladi, uy ustida moviy qulf-gumbaz; kalit stolda qoldi. Kichik farq: uy 6-sahnadagidan boshqacha (panjara, boshqa tom) — fonda, qoldi.",
 11: "Usta chiroqni ko'tarib kameraga qaraydi, yuzi namunadek, ikkinchi qo'li pastda.",
 12: "Usta o'ng qo'lida telefon, chap qo'li Diyorning yelkasida, chiroq devordagi ilgakda; Diyor bosh barmog'ini ko'taradi. Ekran tepasida mayda ma'nosiz yozuv bor — montajda ekran ustiga bot suhbatini (@sahiychishopbot) qo'yamiz. Tepada sarlavha uchun bo'sh joy bor.",
 8: "Uch hiyla tepadan pastga: ochiq bo'sh sovg'a qutisi, qum soat, Tulkining cho'zilgan panjasi (Tulkining o'zi ham ko'rinadi). Usta chiroqni ko'targan, yuzi namunadek. Belgilarni montajda yozamiz.",
 7: "Tepada Tulki kalitni buraydi (bir qo'lida sovg'a), derazalar qizil; pastda Ona qizil telefonga qarab, sumkasidan karta oladi. Ona namunadek (xavotirdan biroz kattaroq ko'rinadi). Kartada yozuv yo'q.",
 4: "Usta chiroqni ko'taradi, yuzi namunadek. Kichik farq: Diyor telefonni qo'lida ushlab turibdi (3 va 5-sahnada telefon stolda) — 3–4 soniyalik kadrda sezilmaydi, qoldi.",
 5: "Tahrirdan keyin Diyorning qo'llari yosh (ajin, tomir yo'q). Bir barmog'i telefon ustida to'xtagan, kaftida kalit.",
 6: "Diyor kalitni qulfga tutadi, Usta chiroqni ko'taradi. Derazalar moviy emas, iliq sariq chiqdi (ichida ona va oila soyalari) — 7 va 9-sahna promptlari shunga moslandi.",
 3: "Tulki telefondan chiqadi, bir qo'lida sovg'a, ikkinchisini cho'zgan; Diyor qo'lini cho'zadi. Telefon bitta, stolda. Namunaga mos.",
 2: "Tahrirdan keyin: telefon bitta (stolda), Diyor qo'llarini iyagi tagida qovushtirgan, qum faqat soat ichida.",
 1: "Chiroq stolda, Usta o'ng qo'li bilan ushlaydi, chap qo'li stolda; Diyorning ikkinchi qo'li cho'ntagida. Usta namunadan biroz kattaroq ko'rinadi, qoldi.",
}

# Egasi (2026-10-24): 16:9 varaqni Veo/GPT yaxshi tushunmaydi — har promptga faqat kerakli qahramonlarning alohida 9:16 rasmi.
REFN = {"usta": "Usta", "diyor": "Diyor", "tulki": "the fox", "ona": "Diyor's mother", "kalit": "the golden key"}
NEED = {1: ["usta", "diyor", "kalit"], 2: ["diyor"], 3: ["tulki", "diyor"], 4: ["usta", "diyor"], 5: ["diyor", "kalit"],
        6: ["usta", "diyor", "kalit"], 7: ["tulki", "ona", "kalit"], 8: ["usta", "tulki"], 9: ["diyor", "tulki"], 10: ["diyor"],
        11: ["usta"], 12: ["usta", "diyor"]}
def att(n):
    names = [REFN[k] for k in NEED[n]]
    lst = ", ".join(names[:-1]) + " and " + names[-1] if len(names) > 1 else names[0]
    return (f"Attach the reference image{'s' if len(names) > 1 else ''} of {lst}. Keep every character exactly as in "
            f"{'their reference images' if len(names) > 1 else 'the reference image'}: the same face, age, hair, clothes, colours and props.")
STY = ("Style: dark hand-drawn illustration exactly like the reference images, rough ink and charcoal lines, aged paper texture, "
       "deep black-brown shadows, almost no colour; the only bright colours are the cyan-blue glow around Diyor, the warm amber "
       "lantern light of Usta, the red eyes of the fox and the gold of the key. Moody fable atmosphere, like an old illustrated "
       "parable. Vertical 9:16. No text, no letters, no numbers, no logos, no watermark, no subtitles.")
U = ("USTA (the calm craftsman about 30 years old with a short jet-black beard, black-and-white Uzbek doppi, dark embroidered "
     "chapan robe with a red sash; his amber oil lantern is described in each scene; his hands are the young strong hands of a 30-year-old man, smooth skin, no wrinkles, no swollen veins, not old hands)")
D = ("DIYOR (the naive guy about 20 years old with messy black hair, big innocent eyes, dark blue hoodie, jeans and sneakers, "
     "outlined with a soft cyan-blue glow)")
F = ("THE FOX (the tall fox standing like a man in a dark three-piece suit with a red tie, big bushy tail, glowing red eyes)")
O = ("DIYOR'S MOTHER (the kind woman in the cream floral headscarf, knitted vest and floral dress)")
ROOM = "a dark old workshop room lit only by Usta's lantern and the phone screen"

S = [
 (1, "0–5 s", "Usta: To'xta! «Siz yutdingiz» degan notanishga SMS kodni hech qachon o'qib berma.",
  f"Close-up of hands in {ROOM}. {U} has put his lit amber lantern down on the wooden table beside the phone, so it stands on the table "
  f"and neither of his hands holds it. With his right hand he firmly grabs the thin wrist of {D}; his left hand rests on the table. "
  f"Usta has exactly two arms and two hands, Diyor has exactly two arms and two hands, every hand clearly belongs to its own arm and "
  f"shoulder, no hand does two things at once. Diyor's fingers hold a small glowing "
  f"golden key, about to drop it onto a smartphone lying on the wooden table; from the dark phone screen two glowing red fox eyes "
  f"stare up, waiting. Amber lantern light from the side, cyan glow on Diyor's sleeve."),
 (2, "6–11 s", "Diyor: Voy! iPhone yutibman! Faqat besh daqiqa vaqt bor ekan.",
  f"Medium shot of {D} in {ROOM}, overjoyed, mouth open, hugging the smartphone with both hands. Above the phone floats a glowing "
  f"ghostly image of a wrapped gift box with a red ribbon, like a hologram. High above his head hangs a large old brass sand hourglass, "
  f"the sand running fast."),
 (3, "12–21 s", "Telefon: Assalomu alaykum, bankdan bezovta qilyapman… Shuni ayting… — Diyor: Hozir, hozir…",
  f"The smartphone lies on the wooden table in {ROOM}. Out of its glowing screen, as if through a small window, {F} leans out "
  f"halfway with a sweet fake smile, holding the wrapped gift box with the red ribbon in one paw and stretching the other paw forward, "
  f"palm up, asking. {D} bends toward the phone eagerly, his face lit by the screen."),
 (4, "22–26 s", "Usta: Kodni aytishdan oldin, SMSni menga ovoz chiqarib o'qi.",
  f"{U} stands tall and raises his amber oil lantern high; its warm light pushes the darkness of {ROOM} back. His face is calm and firm. "
  f"In the foreground, slightly out of focus, {D} freezes with the phone in his hands and looks up at him."),
 (5, "27–33 s", "Diyor: Telegram kodi… «Bu kodni hech kimga bermang»…",
  f"Extreme close-up of the open palm of {D}. Lines of glowing light, like unreadable letters, rise from the phone screen into his palm "
  f"and melt together into a small glowing golden key. His other finger hovers just above the phone, stopped in the air. "
  f"Cyan glow around his hand, darkness all around."),
 (6, "34–42 s", "Usta: Bu sovg'a kodi emas. Bu sening Telegram'ingning kaliti…",
  f"Wide shot at night: {U} and {D} stand in front of a small old house with a wooden door and windows glowing soft cyan-blue; "
  f"in the windows the warm silhouettes of a mother and a family. Usta lifts his lantern toward the keyhole of the door. The golden key "
  f"in Diyor's hand and the keyhole shine with the same gold light, they fit together."),
 (7, "43–49 s", "Usta: Ular sovg'a bermaydi. Sening nomingdan yaqinlaringdan pul so'rashadi.",
  f"Vertical split composition, cold and dark. Upper half: {F} turns the golden key in the door of the small house; red light spills "
  f"out of the door and the warm amber windows turn red. Lower half: inside a dim kitchen, {O} sits at the table looking worried at "
  f"her smartphone glowing red, one hand reaching into her purse for a bank card."),
 (8, "50–61 s", "Usta: Uchta belgi. Tanlovda qatnashmagansan. Shoshiltirishyapti. Kod so'rashyapti…",
  f"Three objects float in a row in the darkness, each glowing red like a warning: an opened gift box that is completely empty inside, "
  f"an old sand hourglass, and the fox's stretched paw with the palm up. At the left edge {U} holds up his lantern, its amber light "
  f"revealing the three tricks."),
 (9, "62–71 s", "Usta: Go'shakni qo'y… Telegram'da bulutli parolni yoq…",
  f"{D} presses the phone screen off with a determined face. The fox on the screen shrinks and is sucked back into the black glass, "
  f"his red eyes fading. In the background the small house with warm amber windows and family silhouettes: a big soft glowing cyan-blue cloud shaped like a "
  f"padlock settles over its roof and closes around it."),
 (10, "72–77 s", "Diyor: Besh daqiqa tugadi. Men esa hech narsa yo'qotmadim.",
  f"Close-up of the old brass sand hourglass: the very last grain of sand falls through the neck, caught in mid-air. Behind it, "
  f"slightly out of focus, {D} smiles with relief, his cyan-blue glow brighter than before."),
 (11, "77–83 s", "Usta: Haqiqiy sovg'a senga hech qachon kod so'ratmaydi.",
  f"Portrait of {U} looking straight into the camera, the amber lantern raised near his face, a calm wise slight smile. Dark "
  f"background of {ROOM}, warm light on his face and the embroidery of his chapan."),
 (12, "84–95 s", "Usta: Shubhali xabar keldimi? Skrinshotini botimizga yuboring: @sahiychishopbot…",
  f"{U} holds a smartphone out toward the camera with his right hand, his amber lantern hangs on a hook on the wall behind him, his left hand rests on Diyor's shoulder, the screen showing a simple chat with a few glowing message bubbles and no readable "
  f"text. Next to him {D} smiles and nods, cyan glow around him. Lantern light, dark workshop behind them. Leave empty dark space in "
  f"the top third of the frame for a title added later."),
]

# Veo (rasm → video) promptlari: boshlang'ich kadr = tasdiqlangan sahna rasmi. Har birida bitta kamera harakati, qo'shni sahnalarda takrorlanmaydi.
KEEP = ("Keep every character exactly as in the image for the whole clip: the same face, age, hair, clothes, colours and props, "
        "the same number of arms and hands. Keep the background and the dark hand-drawn illustration style exactly as in the image. "
        "No new people, no extra objects, no text, no letters, no captions, no subtitles, no watermark. No dialogue and no lip-sync: "
        "mouths stay closed or move only slightly; only quiet ambient sound.")
V = {
 1: ("fast snap zoom-in (crash zoom) from the two faces down to the golden key above the phone, ending in a close-up of the key and the red eyes",
     "Usta's hand tightens on Diyor's wrist and stops it; Diyor's fingers tremble and the golden key swings slightly above the phone; the red fox eyes on the screen narrow and glow brighter; the lantern flame flickers."),
 2: ("slow tilt up from the glowing gift box above the phone to Diyor's joyful face and then to the hourglass above him, ending on Diyor and the hourglass",
     "the glowing gift box slowly turns in the air and sparkles; Diyor bounces on his toes with joy, hands clasped under his chin; the sand in the hourglass runs fast inside the glass; dust glitters in the lantern light."),
 3: ("slow push-in toward the fox leaning out of the phone screen, ending in a medium close-up of the fox and Diyor's reaching hand",
     "the fox slides further out of the glowing screen with a sweet fake smile, offering the gift box and stretching his open paw toward Diyor; Diyor's hand slowly reaches toward the paw; red light pulses from the screen."),
 4: ("low-angle shot, the camera slowly cranes up with the lantern as Usta raises it, ending on Usta's calm face lit by the lantern",
     "Usta slowly raises the lantern higher and its warm light spreads and pushes the shadows back across the workshop; Diyor freezes and looks up at him; the cyan glow around Diyor flickers softly."),
 5: ("macro close-up, slow rack focus from Diyor's finger above the phone to the golden key in his palm",
     "speed ramp: glowing light lines rise from the phone into his palm and melt into the golden key; as his finger moves toward the screen, time slows into extreme slow motion and the finger stops just above the glass, trembling; then normal speed resumes as the key glows brighter."),
 6: ("smooth lateral dolly (truck) right along the house wall, from Diyor and Usta to the glowing keyhole, ending on the key in front of the keyhole",
     "Usta holds the lantern near the door; Diyor slowly brings the golden key toward the keyhole; a thin line of gold light connects the key and the keyhole; inside the warm windows the family silhouettes move gently."),
 7: ("high-angle shot, slow pull-back that reveals both halves of the frame, ending wide on the fox at the door above and the mother below",
     "the fox turns the golden key and the door opens with a red glow; the warm windows slowly turn red one by one; below, the worried mother stares at her red glowing phone and slowly pulls a bank card out of her purse."),
 8: ("slow tilt down from the empty gift box to the hourglass and then to the fox's open paw, ending on the paw and the fox's red eyes",
     "the three tricks glow red one after another as the camera passes them: the empty gift box opens wider, the sand runs in the hourglass, the fox's paw beckons; Usta's lantern light moves over them from the left."),
 9: ("slow dolly out and crane up from Diyor's finger on the phone to the house behind him, ending wide on the glowing blue padlock dome over the house",
     "Diyor presses the screen and it goes dark; the fox is sucked back into the black glass in a red swirl and disappears; the soft cyan-blue padlock dome slowly closes over the roof of the house and its glow settles."),
 10: ("locked-off static camera on the hourglass, then a slow rack focus to Diyor's face at the end",
     "speed ramp: the last sand runs out of the top bulb; the very last grain falls in extreme slow motion through the neck and lands on the pile with a tiny golden sparkle and a soft click; normal speed resumes; the focus moves to Diyor, who laughs with relief, his cyan glow growing brighter."),
 11: ("slow push-in toward Usta's face, ending in a close-up of his eyes and the lantern",
     "Usta looks straight into the camera with a calm wise smile, holding the lantern near his face; the flame flickers softly and warm light moves over the embroidery of his chapan."),
 12: ("slow dolly out, ending in a medium shot of both of them with dark empty space above for a title",
     "Usta holds the phone toward the camera and the chat bubbles on the screen glow softly; his other hand stays on Diyor's shoulder; Diyor smiles and gives a thumbs up; the hanging lantern sways slightly."),
}
def vp(n):
    cam, act = V[n]
    return (f"Vertical 9:16, 8 seconds. Start from the attached image of scene {n}. Camera: {cam}. Action: {act} {KEEP}")

e = html.escape
UZ = {"usta": "Usta", "diyor": "Diyor", "tulki": "Tulki", "ona": "Ona", "kalit": "Oltin kalit"}
cards = []
for n, t, voice, scene in S:
    p = f"{att(n)} Scene {n}, vertical 9:16. {scene} {STY}"
    imgs = "".join(f'<figure class="sc"><img src="web/{f}.webp" alt="{n}-sahna, {e(c)}"><figcaption>{e(c)}</figcaption></figure>' for f, c in IMG.get(n, []))
    got = (f'<div class="scenes">{imgs}</div>' + (f'<p class="note">{e(NOTE[n])}</p>' if n in NOTE else "")) if imgs else ""
    cards.append(f"""<article class="card"><header><span class="num">{n:02d}</span><h2>{n}-sahna — 9:16 (tik)</h2><span class="dur">{t}</span></header>{got}
<div class="txt"><span class="lbl">Ovoz</span><p class="voice">{e(voice)}</p>
<span class="lbl">Veo prompti (9:16, 8 s) — Veo'ga yuqoridagi rasmni yuklang</span>
<pre id="v{n}">{e(vp(n))}</pre><button class="copy" data-t="v{n}">Nusxa olish</button></div></article>""")

page = f"""<title>Sovg'a yutdingiz sahnalari</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Manrope:wght@400;600&family=JetBrains+Mono:wght@400&display=swap">
<style>
/* Layout: one column of scene cards; ink-and-lantern night look (single dark theme, deliberately). */
:root{{--bg:#0f0c0a;--card:#1a1410;--line:#3a2a1e;--fg:#efe4d4;--muted:#b9a185;--amber:#f2a33a;--cyan:#5fd0ff;--red:#e2493a;
--display:"Cormorant Garamond",Georgia,serif;--body:"Manrope",system-ui,sans-serif;--mono:"JetBrains Mono",ui-monospace,monospace;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font-family:var(--body);font-size:15px;line-height:1.55}}
.wrap{{max-width:760px;margin:0 auto;padding-block:28px 60px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:grid;gap:22px}}
h1{{font-family:var(--display);font-weight:700;font-size:clamp(30px,6vw,44px);margin:0;line-height:1.1;text-wrap:balance}}
h1 em{{font-style:normal;color:var(--amber)}}
.intro{{color:var(--muted);margin:0;max-width:62ch}}
.legend{{display:flex;flex-wrap:wrap;gap:8px 16px;font-size:13px;color:var(--muted)}}
.legend b{{font-weight:600}} .c{{color:var(--cyan)}} .a{{color:var(--amber)}} .r{{color:var(--red)}}
.card{{display:grid;gap:14px;background:var(--card);border:1px solid var(--line);border-radius:8px;padding:16px}}
header{{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}}
.num{{font-family:var(--mono);color:var(--amber);font-size:14px}}
h2{{font-family:var(--display);font-weight:700;font-size:26px;margin:0}}
.dur{{font-size:12px;letter-spacing:.06em;text-transform:uppercase;border:1px solid var(--line);border-radius:99px;padding:2px 10px;color:var(--muted)}}
.row{{display:grid;grid-template-columns:180px minmax(0,1fr);gap:16px;align-items:start}}
@media (max-width:560px){{.row{{grid-template-columns:minmax(0,1fr)}}}}
.refs{{display:grid;grid-template-columns:repeat(auto-fill,minmax(80px,1fr));gap:8px;align-content:start}} .rh{{grid-column:1/-1;margin:0;font-size:12px;color:var(--muted)}}
.ref{{margin:0;display:grid;gap:4px}} .ref img{{width:100%;border-radius:4px;display:block;border:1px solid var(--line)}}
.ref figcaption{{font-size:12px;color:var(--muted)}}
.scenes{{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px}}
.sc{{margin:0;display:grid;gap:6px}} .sc img{{width:100%;border-radius:4px;display:block;border:1px solid var(--line)}}
.sc figcaption{{font-size:12px;color:var(--muted)}} .note{{margin:0;font-size:13px;color:var(--amber)}}
.txt{{min-width:0;display:flex;flex-direction:column;gap:8px}}
.lbl{{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}}
.voice{{margin:0;font-style:italic}}
pre{{margin:0;white-space:pre-wrap;word-break:break-word;font-family:var(--mono);font-size:12.5px;line-height:1.6;background:var(--bg);border:1px solid var(--line);border-radius:6px;padding:12px;user-select:all}}
.copy{{align-self:flex-start;font:600 15px var(--body);color:var(--bg);background:var(--amber);border:0;border-radius:8px;padding:10px 18px;cursor:pointer}}
.copy.done{{background:var(--cyan)}} .copy:focus-visible{{outline:2px solid var(--fg);outline-offset:2px}}
</style>
<div class="wrap">
<h1>«Sovg'a yutdingiz!» <em>sahnalari</em></h1>
<p class="intro">12 ta sahna rasmi tayyor. Endi har sahna uchun bitta ish: Veo'da shu kartadagi rasmni yuklang, o'lchamni 9:16 qiling va «Nusxa olish» bilan Veo promptini qo'ying (8 s). Rasm promptlari (ChatGPT) endi kerak emas, sahifadan olib tashlandi; ular repoda (rasm_promptlar.py) saqlanadi. Yozuvlarni (bot nomi, belgilar) montajda o'zimiz qo'shamiz.</p>
<p class="legend"><span><b class="c">Moviy</b> — Diyor</span><span><b class="a">Sariq chiroq</b> — Usta</span><span><b class="r">Qizil ko'z</b> — Tulki (firibgar)</span><span><b class="a">Oltin kalit</b> — SMS kod</span></p>
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
open("video/sovga/rasmlar.html", "w").write(page)
print(len(S), "sahna")
