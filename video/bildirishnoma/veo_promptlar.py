# «Telefon jiringlaydi» — Veo «Frames to video» promptlari (9:16, 6/8 s) → sahnalar.html (Artifact, nusxa tugmasi).
# Uslub: s01_namuna + Malika bozori (qahramonli sahnalar), tarix/tasvir sahnalari — rasmdagidek. Diyor neon (CLAUDE.md qoidasi), aniq o'zbekcha gap, kamera harakati boshida.
# Ishlatish: python3 video/bildirishnoma/veo_promptlar.py
import html, os
D = os.path.dirname(os.path.abspath(__file__))
U_V = "a calm deep warm male voice of about 30-35"
D_V = "a lighter young male voice of about 22"
NEON = "Diyor has a thin bright cyan-blue neon outline along his whole silhouette with a soft glow; it moves with him in every frame and never disappears. Nobody else has it. "
LOCK = ("Keep both characters exactly as in the image: Usta about 30, smooth young skin, short full black beard, black doppi with a white arch pattern, "
        "dark embroidered chapan with a red sash; Diyor about 20, round boyish face, messy jet-black hair. Same faces, five fingers on each hand. " + NEON +
        "One continuous shot, no cuts. Faces stay exactly as in the image from the first to the last frame. ")
LOCK_D = ("Keep Diyor exactly as in the image: about 20, round boyish face, messy jet-black hair, same clothes. Same face, five fingers on each hand. " + NEON + "One continuous shot, no cuts. ")
LOCK_U = ("Keep Usta exactly as in the image: about 30, smooth young skin, short full black beard, black doppi with a white arch pattern, dark embroidered chapan with a red sash. "
          "Same face, five fingers on each hand. One continuous shot, no cuts. His face stays exactly as in the image from the first to the last frame. ")
LOCK_0 = "Nobody appears; no faces anywhere. One continuous shot, no cuts. "
END = ("The blue lamps of the bazaar stay neon blue. Keep the semi-realistic hand-painted cartoon style of the image for the whole clip, never photorealistic. "
       "No readable text, no letters, no subtitles, no captions, no logos. The camera never stops moving.")
END_NC = ("Keep the exact look and style of the image for the whole clip. No readable text, no letters, no numbers, no subtitles, no logos, no brand marks. The camera never stops moving.")
END_OLD = ("This is a history scene: keep its look exactly as in the image (warm sepia and gold, soft film grain, natural light), do not turn it into a cartoon and do not add colours. "
           "No readable text appears; anything written stays blurred. No subtitles, no logos. The camera never stops moving.")

def say(lines):
    return " ".join(f'{w} says in Uzbek, in {v}: "{t}"' for w, v, t in lines)

# (raqam, rasm, ovoz, kamera (uz), kamera (en), harakat, gaplar, qahramonlar: "ud" / "u" / "d" / "")
S = [
 ("1", "s01", "Usta: «Telefoning jiringlaganda sen telefonni emas, telefon seni boshqaradi.»", "Ustaga sekin yaqinlashish — sir aytayotgandek",
  "slow push-in from the medium shot toward Usta's face",
  "Usta looks into the lens with a knowing half-smile and speaks, his pointing hand moves slowly toward Diyor's phone, one eyebrow rises on «telefon seni boshqaradi». "
  "Diyor stays bent over the glowing phone, grinning, mouth closed; small round bubbles keep floating up from the screen; far away shoppers keep walking, the blue lamps sway gently.",
  [("Usta", U_V, "Telefoning jiringlaganda sen telefonni emas, telefon seni boshqaradi.")], "ud"),
 ("2", "s02", "Diyor: «Usta, bir daqiqa, xabar keldi!»", "qo'lda olingandek yengil chayqalib yaqinlashish — hayajon",
  "handheld, a light bouncy push-in toward Diyor's face",
  "Diyor talks fast and eagerly: his stretched hand wiggles its fingers toward the lens, then pulls back to the phone; wide eyes, big guilty grin, he nods quickly. "
  "The bubbles around the phone multiply and drift upward. Shoppers far away keep walking.",
  [("Diyor", D_V, "Usta, bir daqiqa, xabar keldi!")], "d"),
 ("3", "s03", "Usta: «Diyor, eshit. 2006-yil, Amerika.»", "kaft yonidan o'tib, chapdagi eski ofisga qarab suzish — o'tmishga «kirib boramiz»",
  "slow dolly forward and to the left, past Usta's raised palm, into the sepia office",
  "Usta speaks quietly, palm held up like «listen», then turns his head toward the sepia office on the left. The sepia office part keeps spreading across the picture from left to right: "
  "workers in the office type, seen from behind, a CRT monitor flickers, light dust drifts. The bazaar part stays in colour with swaying blue lamps.",
  [("Usta", U_V, "Diyor, eshit. Ikki ming oltinchi yil, Amerika.")], "u"),
 ("4", "s04", "Usta (kadr ortidan): «Bir muhandis cheksiz aylantirishni o'ylab topdi: sahifa tugamaydi, pastga tushaverasan.»", "monitorga sekin yaqinlashish — g'oya tug'ilyapti",
  "slow push-in from the desk toward the glowing monitor, ending on the screen",
  "The hands type steadily on the keyboard; on the CRT monitor the page of simple coloured blocks scrolls steadily downward and never ends; the desk lamp glows, steam curls from the coffee cup, "
  "the people far behind keep working, out of focus with no clear faces. Only hands and sleeves are in focus.",
  [], ""),
 ("5", "s05", "Usta: «Sahifa tugasa, to'xtaysan. Tugamasa, to'xtamaysan.»", "tunnel bo'ylab oldinga uchish — cheksizlik",
  "smooth forward flight down the centre of the endless phone-shaped tunnel at constant speed",
  "The picture cards keep flowing toward the viewer and past the camera, the cyan edges of the tunnel stream by, golden sparks twinkle; the far end of the tunnel stays endlessly far away.",
  [], ""),
 ("6", "s06", "Usta: «Keyinchalik u shu ixtirosidan afsuslanishini ochiq aytdi.»", "noutbukka juda sekin yaqinlashish — afsus",
  "very slow push-in toward the closed laptop on the desk",
  "Rain keeps running down the window, the city lights outside blur and shimmer, the desk lamp flickers softly, ice in the coffee cup slowly settles, the empty office chair turns a little as if someone had just stood up. Nobody is in the picture.",
  [], ""),
 ("7", "s07", "Diyor (kadr ortidan): «Ilovalar bizni ataylab ushlab turadimi?!»", "telefonga tez yaqinlashish va titrash — zarba",
  "fast snap push-in to the phone screen, then a small shake",
  "More and more glowing round notification bubbles burst out of the screen toward the viewer and past the camera, swirling and multiplying; the phone vibrates slightly; golden and cyan sparks fly.",
  [], ""),
 ("8", "s08", "Usta: «Bir tadqiqotga ko'ra, o'rtacha foydalanuvchi kuniga qirq oltitaga yaqin bildirishnoma oladi.»", "hisoblagich atrofida chapga sekin aylanish",
  "slow orbit to the left around the table, rising slightly, ending on the pile of bubbles",
  "The gauge needle swings steadily higher and trembles at the top; new bubbles keep dropping onto the pile, which grows taller and wobbles; golden sparks float up.",
  [], ""),
 ("9", "s09", "Usta: «Ilovalar sening e'tiboring bilan pul topadi: qancha uzoq qarasang, shuncha ko'p reklama ko'rsatiladi.»", "ko'zdan sekin orqaga chekinish — tangalar quyiladi",
  "slow pull-back from the eye to reveal the purse and hands below",
  "The coins pour in a steady stream from the eye into the purse, clinking and bouncing, the stream grows heavier and the purse fills up; the phone reflection in the iris pulses; blue lamps blur in the background.",
  [], ""),
 ("10", "s10", "Usta: «Uchta qoida. Keraksiz bildirishnomani o'chir. Kechasi tinch rejimni yoq. Ilovani ochishdan oldin so'ra: nega ochyapman?»", "tunnel bo'ylab uchta belgi tomon sekin yaqinlashish — har biri birma-bir yonadi",
  "slow push-in along the bazaar tunnel toward the three glowing icons, ending with them filling the frame",
  "The three round glowing icons (crossed-out bell, crescent moon, question mark) light up one after another from left to right: each pulses once with a bright flash and a ring of sparks, the others stay softer. "
  "Their reflections ripple on the wet floor, the blue lamps of the bazaar far behind sway, golden sparks float up.",
  [], ""),
 ("12", "s12", "Usta: «Ular senga ilovani emas, “o'tkazib yuboraman” degan qo'rquvni sotadi. Har gal so'ra: bundan kim foyda ko'radi?»", "Ustaning yuziga sekin yaqinlashish — jiddiy, ishonchli xulosa",
  "slow push-in on Usta's face, ending on a tight close-up",
  "Usta looks straight into the lens and speaks with calm conviction: his lips and jaw move naturally for the whole line, a slow knowing nod on «kim foyda ko'radi?», eyebrows slightly raised, a faint half-smile at the end. "
  "Shoppers far behind keep walking, the blue lamps sway gently, the headphones on the shelf at the left stay still.",
  [("Usta", U_V, "Ular senga ilovani emas, «o'tkazib yuboraman» degan qo'rquvni sotadi. Har gal so'ra: bundan kim foyda ko'radi?")], "u"),
 ("13", "s13", "Usta: «Qaysi bildirishnomani o'chirishni bilmasangiz, ilova nomini botimizga yozing: @sahiychishopbot. Bosqichma-bosqich o'rgatadi.»", "ikkalasiga sekin orqaga chekinib, telefonga e'tibor — iliq yakun",
  "slow pull-back from the phone to the medium shot of both, ending steady",
  "Usta speaks warmly into the lens: his lips and jaw move naturally for the whole line, he lifts the phone a little higher toward the viewer and nods; the crossed-out bell on the phone screen pulses softly. "
  "Diyor stands relaxed beside him with his thumb up, smiling, mouth closed, gives a small happy nod. Shoppers far behind keep walking, the blue lamps sway.",
  [("Usta", U_V, "Qaysi bildirishnomani o'chirishni bilmasangiz, ilova nomini botimizga yozing: @sahiychishopbot. Bosqichma-bosqich o'rgatadi.")], "ud"),
]
DUR = {"4": 8, "8": 8, "9": 8, "10": 8, "12": 8, "13": 8}
def vp(n, cam, act, lines, chars):
    dial = f" {say(lines)}" if lines else ""
    lock = LOCK if chars == "ud" else LOCK_D if chars == "d" else LOCK_U if chars == "u" else LOCK_0
    end = END_OLD if n == "4" else END if chars else END_NC
    return f"Vertical 9:16, {DUR.get(n, 6)} seconds. Start from the attached image. Camera: {cam}. {act}{dial} {lock}{end}"

TOOL = {}
DONE = {}
e = html.escape
cards = []
for n, img, voice, camuz, cam, act, lines, chars in S:
    if n in DONE: continue
    p = vp(n, cam, act, lines, chars)
    cards.append(f"""<article class="card"><header><span class="num">{n}</span><h2>{n}-sahna — 9:16 (tik), {DUR.get(n, 6)} s</h2>{f'<span class="tool">{TOOL[n]}</span>' if n in TOOL else ''}</header>
<div class="row"><figure class="sc"><img src="web/{img}.webp" alt="{n}-sahna rasmi"><figcaption>Veo'ga: {img}.png</figcaption></figure>
<div class="txt"><span class="lbl">Ovoz</span><p class="voice">{e(voice)}</p>
<span class="lbl">Kamera: {e(camuz)}</span>
<pre id="v{n}">{e(p)}</pre><button class="copy" data-t="v{n}">Nusxa olish</button></div></div></article>""")

page = f"""<title>Telefon jiringlaydi sahnalari</title>
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
.tool{{font-size:13px;font-weight:600;color:#111;background:var(--gold);border-radius:99px;padding:2px 10px}} .copy.done{{background:var(--mint)}} .copy:focus-visible{{outline:2px solid var(--fg);outline-offset:2px}}
</style>
<div class="wrap">
<h1>«Telefon jiringlaydi» <em>sahnalari</em></h1>
<p class="intro">Hozircha rasmi tayyor sahnalar: 1–10, 12, 13 (11-sahna rasmi kelgach qo'shiladi). 7 va 8-sahnada yangi rasmlar. Har biri uchun: Veo'da «Frames to video», rasmni <b>birinchi kadr</b> qilib yuklang, <b>9:16</b> va sarlavhadagi uzunlikni qo'ying, «Nusxa olish» bilan promptni qo'ying. 2-sahnaga yangi rasmni (5 barmoqli, olmasiz telefon) yuklang. 4, 5, 6, 7, 8, 9-sahnalarda odam yo'q va gap yo'q — Usta/Diyor ovozi montajda qo'yiladi.</p>
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
