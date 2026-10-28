# «Telefoning eskirmagan» — Veo «Frames to video» promptlari (9:16, 8 s) → sahnalar.html (Artifact, nusxa tugmasi).
# Egasi (2026-10-28, «veo nima uchun kamera harakatlarini qilmayapti?»): kamera gapi promptning boshida va oxirida, qisqa;
# «hamma narsa joyida qolsin» degan gap yo'q (Veo kamerani qotirib qo'yardi) — faqat qahramonlar o'zgarmasin; prompt qisqa.
# Gapiradigan qahramonning aniq o'zbekcha gapi promptda (egasi qoidasi). Qahramonsiz sahnalarda ovoz keyin qo'yiladi.
# Ishlatish: python3 video/eskirish/veo_promptlar.py
import html, os
D = os.path.dirname(os.path.abspath(__file__))
USTA_V = "a calm deep warm male voice of about 30-35"
DIYOR_V = "a lighter young male voice of about 22"
LOCK = ("Keep every character exactly as in the image for the whole clip: Usta about 30 with a fuller face, short full black beard, black doppi with white arch pattern, "
        "dark embroidered chapan with a red sash; Diyor about 20 with a round boyish face, messy straight jet-black hair, navy hoodie, thin cyan-blue glow outline. "
        "Same faces, same age, five fingers on each hand. The street lamps glow cool neon blue, exactly as in the image, and stay blue. ")
END = "No text, no subtitles, no logos, no watermark. The camera keeps moving as described for the whole 8 seconds and is never static."

def say(lines):
    return " ".join(f'{w} says in Uzbek, in {v}: "{t}"' for w, v, t in lines)

# (raqam, rasm, ovoz qatori(lari) ko'rinishi, kamera (uz), kamera (en), harakat, gaplar [(kim, ovoz, matn)], qahramonlar bormi)
S = [
 ("1", "s01", "Usta: «Telefoning eskirmagan. Balki faqat batareyasi charchagandir.»", "sekin yaqinlashish (ikkalasiga)",
  "slow steady push-in from the medium shot to a medium close-up of both men, ending with Usta's face in the upper third",
  "USTA SPEAKS to the viewer with a calm knowing half-smile, his open palm gently moves toward Diyor's phone as he talks, one eyebrow rises on the word about the battery. "
  "Diyor keeps frowning at his frozen phone, taps the dark screen twice with his thumb and shakes his head, mouth closed. Leaves drift down, passers-by far away keep walking.",
  [("Usta", USTA_V, "Telefoning eskirmagan. Balki faqat batareyasi charchagandir.")], True),
 ("2", "s02", "Diyor: «Usta, telefonim qotyapti, quvvati kechgacha yetmaydi. Ikki yil bo'ldi, eskirdi. Nasiyaga yangisini olaman!»", "qo'lda olingandek chayqalish + yaqinlashish",
  "handheld camera with a light nervous shake, slowly pushing in to a close-up of Diyor's angry face",
  "DIYOR SPEAKS fast and annoyed: he shakes the phone in his raised hand, his other hand waves in frustration, eyebrows drawn together, cheeks puffed; "
  "on the last words he nods firmly as if he has decided. Yellow leaves fall behind him, a passer-by far away keeps walking.",
  [("Diyor", DIYOR_V, "Usta, telefonim qotyapti, quvvati kechgacha yetmaydi. Ikki yil bo'ldi, eskirdi. Nasiyaga yangisini olaman!")], True),
 ("3", "s03", "Usta: «Diyor, kim aytdi telefon eskirgani uchun qotayotganini?» — Diyor: «Hamma biladi-ku!»", "Usta atrofida o'ngga sekin yoy",
  "slow 20-degree arc to the right around Usta, over Diyor's blurred shoulder, ending on a medium close-up of Usta",
  "USTA SPEAKS, arms folded, head tilted, one eyebrow raised high with an amused smile, a sharp simple question. Then Diyor in the blurred foreground answers quickly, "
  "his head nods and his shoulder shrugs (his face stays turned away); Usta listens with his mouth closed and a small smile.",
  [("Usta", USTA_V, "Diyor, kim aytdi telefon eskirgani uchun qotayotganini?"), ("Diyor", DIYOR_V, "Hamma biladi-ku!")], True),
 ("4", "s04", "Usta: «Jim, Diyor. Qara. Jeneva, 1924-yil, dekabr.»", "Usta yonidan o'tib, eski shaharga qarab oldinga suzish",
  "slow dolly forward and slightly to the right, past Usta's raised hand, toward the old sepia city, ending on the old street with the trams",
  "USTA SPEAKS quietly and mysteriously, his open palm held up like «be quiet and watch», then he turns his head toward the old city. "
  "In the sepia part the old trams roll slowly to the right, men in long coats and hats keep walking away, gas lamps flicker, light snow falls. The border between the golden street and the sepia city slowly spreads to the left.",
  [("Usta", USTA_V, "Jim, Diyor. Qara. Jeneva, ming to'qqiz yuz yigirma to'rtinchi yil, dekabr.")], True),
 ("5", "s05", "Usta (ovoz, kadrda yo'q): «Dunyodagi eng katta lampochka zavodlari kelishib oldi: oddiy lampochka ming soatdan ortiq yonmasin.»", "yuqoridan pastga sekin tushish (kran)",
  "slow crane down from the high angle toward the table, ending at table height among the glowing blue bulbs",
  "The two men in the middle finish their handshake and slowly let go; the man at the head of the table pushes the paper forward and taps it with one finger; "
  "the others nod slowly. The blue neon bulbs on the table flicker softly. Faces stay in the shadow of the hats, no recognizable faces. Nobody speaks on screen, mouths closed; "
  "the voice-over is added later. Keep the sepia 1920s look and the blue neon bulbs.", [], False),
 ("6", "s06", "Usta (ovoz): «Undan oldin ikki ming besh yuz soatgacha yonardi. Uzoqroq yonadiganini chiqargan zavod jarima to'lardi.»", "lampochkalar qatori bo'ylab o'ngdan chapga suzish",
  "slow lateral truck from right to left along the rows of glowing bulbs, ending on the one dark bulb in the middle",
  "The technician in the white coat keeps writing on the clipboard; the blue neon clock hands tick forward; one more bulb at the far end flickers and goes dark. "
  "Nobody speaks on screen; the voice-over is added later. Keep the sepia look, the blue neon clock and the blue ceiling lamps.", [], False),
 ("6b", "s06b", "Diyor: «Ataylab-a?!»", "keskin yaqinlashish (yuzga)",
  "fast snap zoom-in (crash zoom) on Diyor's shocked face, ending in an extreme close-up of his eyes and open mouth",
  "DIYOR SPEAKS one short shocked word, his eyes grow even wider, eyebrows jump up, his hand freezes at his chin, then he blinks twice in disbelief.",
  [("Diyor", DIYOR_V, "Ataylab-a?!")], True),
 ("7", "s07", "Usta: «2017-yil. Eng mashhur telefon kompaniyalaridan biri bir sirni tan oldi.» — Diyor: «Qanaqa sir?»", "ikkalasi atrofida chapga sekin aylanish",
  "slow 30-degree orbit to the left around the two men, the TV tower moving behind them, ending on a medium close-up of both faces",
  "USTA SPEAKS slowly and mysteriously, turning the phone in his hand and looking at it; then DIYOR SPEAKS quickly, leaning closer with wide curious eyes and raised eyebrows. "
  "While one talks, the other keeps his mouth closed. The TV tower lights twinkle, passers-by on the embankment keep walking.",
  [("Usta", USTA_V, "Ikki ming o'n yettinchi yil. Eng mashhur telefon kompaniyalaridan biri bir sirni tan oldi."), ("Diyor", DIYOR_V, "Qanaqa sir?")], True),
 ("8", "s08", "Usta (ovoz): «Batareyasi eskirgan telefonlarni o'zi sekinlashtirib qo'ygan. To'satdan o'chib qolmasin deb. Lekin egasiga aytmagan.»", "makro, telefon atrofida sekin yoy",
  "macro shot, slow arc around the floating phone from left to right with a gentle push-in toward the snail",
  "The snail crawls very slowly forward to the right across the screen, its eye stalks swaying, leaving a glowing red trail; the red battery level blinks weakly twice. "
  "Nothing speaks; the voice-over is added later. No text on the screen.", [], False),
 ("9", "s09", "Usta (ovoz): «Odamlar ‘telefonim eskirdi’ deb, yangisini sotib olgan. Ko'pincha esa faqat batareyani almashtirish yetardi.»", "yuqoridan pastga sekin egilish (savatga)",
  "slow tilt down from the shop counter to the basket of old phones in the foreground, ending on a close-up of the old phones",
  "At the counter the customer hands over his old phone and takes a white box; the two people with white boxes keep walking away toward the glass doors and out; "
  "a hand drops one more perfectly fine old phone into the basket. Faces stay unseen. Nobody speaks; the voice-over is added later. No logos on boxes or phones.", [], False),
 ("10", "s10", "Usta (ovoz): «Bu ochilgach, kompaniya Amerikada odamlarga yarim milliard dollargacha to'lashga rozi bo'ldi. Fransiyada yigirma besh million yevro jarima oldi.»", "pastdan sekin yaqinlashish + sekinlashuv",
  "low-angle slow push-in toward the gavel and the phone",
  "Speed ramp: the gavel lifts and strikes the block again in extreme slow motion, golden dust and sparks burst up, then normal speed resumes; "
  "the stacks of banknotes tremble slightly from the hit and the cracked phone's red battery icon blinks. Nobody on screen; the voice-over is added later. "
  "No readable text on the money.", [], False),
 ("11", "s11", "Diyor: «Demak, mening telefonim ham eskirmagan, shunchaki batareyasi charchagan bo'lishi mumkin?» — Usta: «Bo'lishi mumkin.»", "Diyor yuziga sekin yaqinlashish",
  "slow push-in to a close-up of Diyor's face, Usta staying visible behind his shoulder",
  "DIYOR SPEAKS slowly, his excitement turning into hope: he looks at the phone, then up at Usta with soft wide eyes and a growing smile. "
  "Then USTA SPEAKS two short words with a warm nod and a smile. While one talks, the other keeps his mouth closed. The TV tower lights twinkle behind them.",
  [("Diyor", DIYOR_V, "Demak, mening telefonim ham eskirmagan, shunchaki batareyasi charchagan bo'lishi mumkin?"), ("Usta", USTA_V, "Bo'lishi mumkin.")], True),
 ("12", "s12", "Diyor: «Kechir, eski do'stim... sen aybsiz ekansan!» — Usta: «Quchoqlama, batareyasini tekshir!»", "qo'lda, yengil chayqalish, ozgina uzoqlashish",
  "handheld camera with a playful light bounce, slowly pulling back to show both men from the waist up",
  "Comedy: DIYOR SPEAKS with his eyes closed, hugging the phone to his chest and rocking it like a baby, a guilty loving smile. "
  "Then USTA SPEAKS laughing, his eyes crinkled, wagging his pointing finger at the phone in a friendly scolding way. While one talks, the other keeps his mouth closed.",
  [("Diyor", DIYOR_V, "Kechir, eski do'stim... sen aybsiz ekansan!"), ("Usta", USTA_V, "Quchoqlama, batareyasini tekshir!")], True),
 ("13", "s13", "Usta: «Yangisini olishdan oldin uchta tekshiruv. Batareya holati necha foiz? Xotira to'lib qolmaganmi? Batareya almashtirish qancha turadi?»", "pastdan tepaga sekin ko'tarilish",
  "low-angle shot, the camera slowly cranes up from his chest to his raised hand and the three symbols",
  "USTA SPEAKS clearly, keeping exactly three fingers up; the battery, the chip and the wrench symbols pulse brightly one after another from left to right, "
  "and with each one he gives a small firm nod; at the end he looks straight into the camera with a caring smile. The symbols have no letters or numbers.",
  [("Usta", USTA_V, "Yangisini olishdan oldin uchta tekshiruv. Batareya holati necha foiz? Xotira to'lib qolmaganmi? Batareya almashtirish qancha turadi?")], True),
 ("14", "s14", "Usta: «Ular senga telefon emas, ‘eskirding’ degan tuyg'uni sotadi. Har gal so'ra: bundan kim foyda ko'radi?»", "yuzga juda sekin yaqinlashish",
  "very slow push-in to a close-up of Usta's face (never closer than the whole face)",
  "USTA SPEAKS warmly and wisely straight into the camera: a calm smile, soft eyes, a slight head tilt on the question, one slow nod at the end. "
  "The TV tower lights and the lamps along the canal twinkle behind him.",
  [("Usta", USTA_V, "Ular senga telefon emas, eskirding degan tuyg'uni sotadi. Har gal so'ra: bundan kim foyda ko'radi?")], True),
 ("15", "s15", "Usta: «Telefoningiz qotyaptimi? Botimizga modelini yozing: @sahiychishopbot. …»", "uzoqlashib, tepaga ko'tarilish (osmon kattalashadi)",
  "slow dolly out and crane up, ending in a medium wide shot with the evening sky and the TV tower filling the top third",
  "USTA SPEAKS in a friendly inviting way to the viewer, pushing the glowing phone a little toward the camera; the empty chat bubbles on the screen pulse softly. "
  "Diyor keeps his mouth closed, smiles, nods twice and pumps his thumb up. Passers-by on the embankment keep walking.",
  [("Usta", USTA_V, "Telefoningiz qotyaptimi? Botimizga modelini yozing: sahiychi shop bot. Batareya holatini qayerdan ko'rishni va yangisini olishdan oldin nimani tekshirishni bosqichma-bosqich o'rgatadi.")], True),
]

def vp(cam, act, lines, chars):
    dial = f" Dialogue: {say(lines)}" if lines else ""
    return (f"Vertical 9:16, 8 seconds. Start from the attached image. Camera: {cam}. Action: {act}{dial} "
            f"{LOCK if chars else ''}{END}")

# Tayyor kliplar (2026-10-28): sahifada faqat qolganlari ko'rsatiladi, navbat bilan.
DONE = {"1": "Veo", "3": "Seedance", "4": "Seedance", "5": "Veo", "6": "Veo (0–4.5 s)", "8": "Veo (batareya tuzatilgan)"}
e = html.escape
cards = []
for n, img, voice, camuz, cam, act, lines, chars in S:
    if n in DONE: continue
    p = vp(cam, act, lines, chars)
    cards.append(f"""<article class="card"><header><span class="num">{n}</span><h2>{n}-sahna — 9:16 (tik), 8 s</h2></header>
<div class="row"><figure class="sc"><img src="web/{img}.webp" alt="{n}-sahna rasmi"><figcaption>Veo'ga: {img}.png</figcaption></figure>
<div class="txt"><span class="lbl">Ovoz</span><p class="voice">{e(voice)}</p>
<span class="lbl">Kamera: {e(camuz)}</span>
<pre id="v{n}">{e(p)}</pre><button class="copy" data-t="v{n}">Nusxa olish</button></div></div></article>""")

page = f"""<title>Telefoning eskirmagan sahnalari</title>
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
<h1>«Telefoning eskirmagan» <em>sahnalari</em></h1>
<p class="intro"><b>Tayyor kliplar:</b> {', '.join(f'{k} ({v})' for k, v in DONE.items())}. Quyida faqat <b>qolgan {len(S) - len(DONE)} ta sahna</b>, tartib bilan — yuqoridan boshlang. 16 ta rasm tayyor. Har sahna uchun: Veo'da «Frames to video» ni oching, chapdagi rasmni yuklang, 9:16 va 8 s qiling, «Nusxa olish» bilan promptni qo'ying. Kamera gapi promptning boshida va oxirida; qahramon gapirsa — gapi o'zbekcha promptda. 5, 6, 8, 9, 10-sahnalarda hech kim gapirmaydi: Usta ovozi keyin qo'yiladi.</p>
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
print(len(S), "sahna; eng uzun prompt:", max(len(vp(c, a, l, ch).split()) for _, _, _, _, c, a, l, ch in S), "so'z")
