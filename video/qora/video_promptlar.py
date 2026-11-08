# «Qora kvadrat» — Veo video promptlari (9:16, 8 s, so'zsiz). Tasdiqlangan rasmlar img/sNN.png dan → rasmlar.html (o'sha Artifact sahifa).
# Qoidalar: har prompt kamera harakati bilan boshlanadi, rasmda boshlangan harakatni davom ettiradi, Diyorning neon chizig'i batafsil,
# qahramon gapirmaydi (so'zsiz rolik), oxirida alohida Negative qatori. Ishlatish: python3 video/qora/video_promptlar.py
import html, os, re
D = os.path.dirname(os.path.abspath(__file__))
KEEP = "Keep everything exactly as in the image for the whole clip: Diyor's round boyish young face, messy black hair, dark navy hoodie, jeans, sneakers and backpack, the setting and the colours."
NEON = ("Diyor's thin bright cyan-blue neon line runs exactly along his whole outer silhouette (hair, face, hoodie, arms, legs) with a soft blue glow; "
        "it moves with him in every frame and never disappears; nothing else in the frame has this outline.")
SIL = "This is a silent film: Diyor does not speak, no dialogue, his mouth only shows the expression."
NEG = "Negative: no text, no letters, no numbers, no subtitles, no captions, no logos, no brand names, no watermarks, no extra people, no extra hands"
# (raqam, rasm, kamera (uz), nima bo'ladi (uz), Veo prompt, neg o'zgarishi)
S = [
 ("1", "s01_narx", "Sekin push-in: yondan monitorga yaqinlashib, kartina va narx yozuviga to'xtaydi",
  "Diyor ekranga engashadi, ko'zlari kattalashadi, sichqonchani bosadi. Narx ko'rinadi",
  "Slow push-in from beside Diyor toward the monitor, ending on the painting and the white price label under it. Diyor leans closer to the screen, his eyes widen more, his eyebrows rise, a fascinated smile grows; he clicks the mouse once and his chin hand drops to the desk. The screen glow flickers softly on his face, the red mousepad glows. Keep the white price label and the text on it exactly unchanged and sharp.", "price"),
 ("2", "s02", "Sekin orbit: Diyor atrofida chapdan o'ngga chorak aylana",
  "Varaqni biroz buradi, boshini egadi, kvadrat suvdek to'lqinlanadi, qizil nur yuzida yonib-o'chadi",
  "Slow quarter orbit around Diyor from left to right, ending a little in front of him. He slowly turns the printed sheet in his hands and tilts his head, studying it with curious amazement; the black square on the paper ripples like dark water and the red glow deep inside pulses, lighting his face from below in slow waves. The printer's red light blinks on the desk.", ""),
 ("3", "s03", "Statik makro kadr (kamera qimirlamaydi), sekinlashtirilgan",
  "Barmoq bo'g'imigacha sekin botib kiradi, qizil halqalar tarqaladi. Orqadagi yuz xira qoladi",
  "Static locked macro shot, no camera movement, slow motion. Diyor's index finger slowly sinks deeper into the black square up to the knuckle and simply disappears inside, red rings ripple outward across the black surface like rings on water, tiny red sparks rise. In the background his face stays strongly blurred; his shoulders flinch back slightly in surprise.", ""),
 ("4", "s04", "Kamera stol ostiga tushadi (tilt down) va qaytib Diyorga ko'tariladi",
  "Qo'li tirsagigacha ichkarida, stol ostida hech narsa yo'q. Qo'lini qimirlatib, boshini orqaga tashlab kuladi",
  "The camera tilts down under the desk to show the empty space where no hand comes out, then tilts back up to Diyor. He wiggles his arm inside the black square up to the elbow, red light pulsing around the edge where his arm enters the paper; he throws his head back and laughs with delight, his free fist shaking in the air with joy.", ""),
 ("5", "s05", "Sekin pull-back: oshxona to'liq ko'rinadi",
  "Qo'lini kvadratdan to'liq chiqaradi, muzqaymoqni tishlab, kameraga ko'z qisadi",
  "Slow pull-back revealing the whole dark kitchen. Diyor pulls his arm fully out of the black square on the closed fridge door, the red glow fades back into the square; he licks the frosty ice cream cone (a little cold mist only around the ice cream, no smoke and no vapour from his mouth) and winks at the camera with a cheeky grin, shoulders bouncing. The printed sheet with the black square stays taped on the fridge door, unchanged and fully visible, for the whole clip.", ""),
 ("6", "s06", "Sekin truck o'ngga: devor bo'ylab bankomat tomon suriladi",
  "Pul dastasini cho'ntagiga tiqib, yana qo'l suqadi, orqaga xavotir bilan qaraydi. Barglar tushadi",
  "Slow truck right along the wet wall toward the cash machine. Diyor stuffs the stack of banknotes into his hoodie pocket, reaches into the black square again and pulls out another stack, glancing nervously over his shoulder twice; red maple leaves drift down, rain reflections shimmer on the pavement, the street lamp flickers.", ""),
 ("7", "s07", "Statik o'rta kadr (kamera qimirlamaydi, yaqinlashmaydi)",
  "Pulni mahkamroq quchoqlaydi, ayyorona tabassum biroz kengayadi, ko'zlari u yoq-bu yoqqa qaraydi. Yuz o'zgarmaydi",
  "Static medium shot, zero camera movement, the framing stays exactly as in the image. Diyor hugs the pile of banknotes a little tighter, his sly closed-mouth smile widens only slightly, his eyes glance left and right twice; red leaves fall slowly behind him. His face stays exactly the same round boyish young face as in the image for the whole clip: same size, same proportions, no exaggerated grin, no bulging eyes, no wrinkles, no red light on the face. Subtle movement only.", ""),
 ("7b", "s07b", "Kran yuqoriga: ho'l yo'lakdan BANK yozuviga ko'tariladi, keyin Diyor o'ngdagi tor yo'lakka kirib ketadi",
  "BANK yozuviga qarab turib, yo'lakni ko'rsatadi va o'sha tomonga yurib, kadrdan chiqib ketadi",
  "Low crane up from the wet pavement to the glowing gold BANK letters, keeping the letters B-A-N-K exactly as in the image and unchanged. Diyor looks up at the letters with an excited grin, points at the dark narrow alley on the right, then walks quickly to the right into the alley, his hood bobbing, and leaves the frame on the right; red leaves swirl on the wet stones behind him.", "bank"),
 ("8", "s08", "Statik past kadr (kamera qimirlamaydi)",
  "Oyoqlari kvadratga sudralib kiradi, kedalar g'oyib bo'ladi, qizil nur chaqnaydi",
  "Static low-angle shot at ground level, zero camera movement. Diyor's legs wriggle and slide forward into the black square on the wall, the sneakers kick once and disappear inside, the red glow around the square flares brightly and then calms; red leaves blow across the wet ground.", ""),
 ("9", "s09", "Yuqoridan sekin orbit, pul tushishi sekinlashtirilgan (speed ramp)",
  "Quvonchdan aylanadi, banknotalar havoda sekin uchadi, oltin yaltiraydi",
  "Slow overhead orbit around Diyor. He spins around with joy, arms full of money and gold bars, eyes closed, laughing; banknotes fly up around him and then float down in slow motion (speed ramp: normal speed, then slow while the notes fall, then normal again); gold bars glint, his cyan outline reflects on the gold.", ""),
 ("10", "s10", "Qo'lda olingan yaqin kadr (handheld), shamol",
  "Skotch ko'chadi, varaq shamolda pirpiraydi va chapga uchib ketadi",
  "Handheld close-up with a light shake from the wind. The tape peels off further, the paper flaps harder in the gusts, then the last corner tears loose and the sheet flies away to the left out of the frame among swirling red leaves; the bare concrete wall stays behind, the cold blue street light flickers.", "nodiyor"),
 ("10b", "s10b", "Yuqoridan sekin push-in, sekinlashtirilgan",
  "Varaq ko'lmakda, qora rang qizil burama bo'lib eriydi, kvadrat yo'qoladi",
  "Slow push-in from directly above, slow motion. The soaked paper lies in the puddle; the black square dissolves into the water in slow black and red swirls of ink until the square is gone, raindrops make rings on the surface, red leaves drift on the water, the street lamp reflection trembles.", "nodiyor"),
 ("11", "s11", "Sekin pull-back: yuzdan qorong'ilikka uzoqlashadi",
  "Devorni mushti bilan uradi, pullar sekin tushadi, faqat neon chizig'i yonadi",
  "Slow pull-back from Diyor's face into the darkness of the vault. He pounds the smooth steel wall with both fists, then presses his palms against it again, tears on his cheeks, breath fogging in the cold; banknotes slip out of his pockets and fall slowly to the floor; the only light is his own cyan neon outline and the small red emergency lamp far behind. His face stays round, boyish and young.", ""),
]
def prompt(n, img, cam, what, p, mode):
    neg = NEG
    if mode == "price": neg = NEG.replace("no text, no letters, no numbers,", "no new text, no extra letters or numbers besides the existing price label,")
    if mode == "bank": neg = NEG.replace("no text, no letters, no numbers,", "no other text besides the gold BANK letters, no numbers,")
    body = p if mode == "nodiyor" else f"{p} {NEON} {SIL}"
    keep = "Keep everything exactly as in the image for the whole clip: the setting, the objects and the colours." if mode == "nodiyor" else KEEP
    return f"Vertical 9:16 video, 8 seconds, from the attached image. {body} {keep} Colours: deep night darkness, electric cyan-blue neon and glowing red. No music.\n{neg}"
e = html.escape
cards = []
for n, img, cam, what, p, mode in S:
    pr = prompt(n, img, cam, what, p, mode)
    cards.append(f"""<article class="card"><header><span class="num">{n}</span><h2>{n}-sahna — video, 9:16 (tik), 8 s</h2></header>
<div class="row"><figure class="shot"><img src="web/{img}.webp" alt="{n}-sahna rasmi"><figcaption>img/{img}.png — Veo'ga shuni yuklang</figcaption></figure>
<div class="txt"><span class="lbl">Nima bo'ladi</span><p class="what">{e(what)}</p><span class="lbl">Kamera</span><p class="cam">{e(cam)}</p>
<pre id="p{n}">{e(pr)}</pre><button class="copy" data-t="p{n}">Nusxa olish</button></div></div></article>""")
page = f"""<title>Qora kvadrat sahnalari</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Manrope:wght@400;600&family=JetBrains+Mono:wght@400&display=swap">
<style>
/* Layout: one column of scene cards, image left, prompt right; night palette (single dark theme, deliberately: the film is dark neon). */
:root{{--bg:#0b0f1a;--card:#131a2a;--line:#26304a;--fg:#eef2fb;--muted:#9fb0cf;--cyan:#2fd3ff;--red:#ff3b4f;--gold:#f2b544;
--display:"Cormorant Garamond",Georgia,serif;--body:"Manrope",system-ui,sans-serif;--mono:"JetBrains Mono",ui-monospace,monospace;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font-family:var(--body);font-size:15px;line-height:1.55;margin:0}}
.wrap{{max-width:820px;margin:0 auto;padding-block:28px 60px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:grid;gap:22px}}
h1{{font-family:var(--display);font-weight:700;font-size:clamp(30px,6vw,44px);margin:0;line-height:1.1;text-wrap:balance}} h1 em{{font-style:normal;color:var(--red)}}
.intro{{color:var(--muted);margin:0;max-width:66ch}}
.card{{display:grid;gap:14px;background:var(--card);border:1px solid var(--line);border-radius:8px;padding:16px}}
header{{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}} .num{{font-family:var(--mono);color:var(--cyan);font-size:14px}}
h2{{font-family:var(--display);font-weight:700;font-size:26px;margin:0}}
.row{{display:grid;grid-template-columns:170px minmax(0,1fr);gap:16px;align-items:start}}
@media (max-width:560px){{.row{{grid-template-columns:minmax(0,1fr)}} .shot{{max-width:200px}}}}
.shot{{margin:0;display:grid;gap:4px}} .shot img{{width:100%;max-width:100%;border-radius:4px;display:block;border:1px solid var(--line)}}
.shot figcaption{{font-size:12px;color:var(--muted);font-family:var(--mono)}}
.txt{{min-width:0;display:flex;flex-direction:column;gap:6px}} .lbl{{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}}
.what,.cam{{margin:0 0 6px}} .cam{{color:var(--cyan)}}
pre{{margin:0;white-space:pre-wrap;word-break:break-word;font-family:var(--mono);font-size:12.5px;line-height:1.6;background:var(--bg);border:1px solid var(--line);border-radius:6px;padding:12px;user-select:all}}
.copy{{align-self:flex-start;font:600 15px var(--body);color:#111;background:var(--cyan);border:0;border-radius:8px;padding:10px 18px;cursor:pointer;margin-top:4px}}
.copy.done{{background:var(--gold)}} .copy:focus-visible{{outline:2px solid var(--fg);outline-offset:2px}}
</style>
<div class="wrap">
<h1>«Qora kvadrat» <em>video sahnalari</em></h1>
<p class="intro">13 ta sahna, hammasi 9:16 (tik), 8 soniya, so'zsiz. Har biri uchun Veo'da chapdagi rasmni yuklang va «Nusxa olish» bilan promptni qo'ying. 12-sahna (oyat, qizil olovli harflar), 13 (bot) va 14 (avatar) montajda qo'shiladi. Rasm promptlari repo'da: video/qora/rasm_promptlar.txt</p>
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
open(os.path.join(D, "video_promptlar.txt"), "w").write("\n\n".join(f"### {n}\n" + prompt(*x) for x in S for n in [x[0]]))
print(len(S), "video prompt")
