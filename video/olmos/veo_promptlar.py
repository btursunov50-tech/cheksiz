# «Olmos uzuk» — Veo «Frames to video» promptlari (9:16, 6/8 s) → sahnalar.html (Artifact, nusxa tugmasi).
# Uslub: img/s01_namuna (kunduzgi oltin yorug'lik, Toshkent ko'chasi, zargarlik oynasi). Yaqin ko'cha fonuslari ko'k neon (fonus_hammasi.sh).
# Har promptda kamera harakati, gapiruvchining aniq o'zbekcha gapi, Diyorning neon chizig'i (CLAUDE.md qoidasi), «chizilgan uslub, realistik emas».
# Ishlatish: python3 video/olmos/veo_promptlar.py
import html, os
D = os.path.dirname(os.path.abspath(__file__))
U_V = "a calm deep warm male voice of about 30-35"
D_V = "a lighter young male voice of about 22"
NEON = "Diyor has a thin bright cyan-blue neon outline along his whole silhouette with a soft glow; it moves with him in every frame and never disappears. Nobody else has it. "
LOCK = ("Keep both characters exactly as in the image: Usta about 30, smooth young skin, short full black beard, black doppi with a white arch pattern, "
        "dark embroidered chapan with a red sash; Diyor about 20, round boyish face, messy jet-black hair. Same faces, five fingers on each hand. " + NEON +
        "One continuous shot, no cuts. Faces stay exactly as in the image from the first to the last frame. ")
LOCK_D = ("Keep Diyor exactly as in the image: about 20, round boyish face, messy jet-black hair, same clothes. Same face, five fingers on each hand. " + NEON +
          "One continuous shot, no cuts. ")
LOCK_U = ("Keep Usta exactly as in the image: about 30, smooth young skin, short full black beard, black doppi with a white arch pattern, "
          "dark embroidered chapan with a red sash. Same face, five fingers on each hand. Only Usta is in this shot; no other people appear close. "
          "One continuous shot, no cuts. His face stays exactly as in the image from the first to the last frame. ")
LOCK_0 = "Faces of people stay in shadow or turned away; nobody looks at the camera. One continuous shot, no cuts. "
END = ("The street lamp glass that glows cool neon blue in the image stays neon blue. Keep the semi-realistic hand-painted cartoon style of the image for the whole clip, never photorealistic. "
       "No text, no subtitles, no captions, no logos. The camera never stops moving.")
END_OLD = ("This is a history scene: keep its realistic old-photograph look exactly as in the image (warm sepia and gold, soft film grain, natural light), do not turn it into a cartoon and do not add colours. "
           "No new text appears; anything written stays blurred and unreadable. No subtitles, no logos. The camera never stops moving.")

def say(lines):
    return " ".join(f'{w} says in Uzbek, in {v}: "{t}"' for w, v, t in lines)

# (raqam, rasm, ovoz, kamera (uz), kamera (en), harakat, gaplar, qahramonlar: "ud" / "u" / "d" / "")
S = [
 ("1", "s01", "Usta: «Olmos noyob emas. Senga shunday deb aytishgan.»", "sekin yaqinlashish Usta yuziga — sir aytayotgandek, tomoshabin unga yaqinlashadi",
  "slow push-in from the medium shot toward Usta's face",
  "Usta looks into the lens with a sly knowing smile and speaks, his pointing hand moves slowly toward the ring in the window; one eyebrow rises on «noyob emas». "
  "Behind him Diyor keeps both palms on the glass and stares at the big ring with a dreamy open-mouthed smile, mouth not speaking. Passers-by far away keep walking, sparkles twinkle on the rings.",
  [("Usta", U_V, "Olmos noyob emas. Senga shunday deb aytishgan.")], "ud"),
 ("2", "s02", "Diyor: «Usta, to'yga olmos uzuk olaman! …»", "qo'lda olingandek yengil chayqalib yaqinlashish — Diyorning hayajoni seziladi",
  "handheld, a light bouncy push-in toward Diyor",
  "Diyor talks fast and proudly: he pushes the phone toward the lens, pats his chest twice with his other hand, chin up, eyes shining, big grin. "
  "The phone screen stays exactly as in the image: the blue check, the bar and the blue button. Golden leaves drift down, passers-by keep walking.",
  [("Diyor", D_V, "Usta, to'yga olmos uzuk olaman! Sevgilimga olmos uzukni berib,")], "d"),
 ("2b", "s02b", "Diyor (orzusi): «…sevgim qanchalik kuchli ekanini isbotlayman! Lekin pulim yetmaydi, kredit olaman!»", "pastdan Diyor atrofida sekin aylanib ko'tarilish — dabdabali tush hissi",
  "slow low-angle arc to the right around the kneeling Diyor, rising a little, dreamy soft glow",
  "A dream: Diyor kneels and lifts the open ring box higher, the huge diamond flashes like a star; he speaks with a proud happy face. "
  "The bride in the white veil keeps her hand at her face, touched; her face stays hidden by the veil. Golden sparkles float in the air, chandeliers glitter, guests far away clap.",
  [("Diyor", D_V, "sevgim qanchalik kuchli ekanini isbotlayman! Lekin pulim yetmaydi, kredit olaman!")], "d"),
 ("3", "s03", "Usta: «Diyor, kim aytdi sevgi olmosda deb?» — Diyor: «Hamma biladi-ku! Kinoda ham, reklamada ham.»", "Diyor yelkasi ustidan Ustaga sekin yaqinlashish — suhbatga kirib boramiz",
  "slow push-in toward Usta over Diyor's blurred shoulder; Diyor's shoulder stays at the left edge",
  "Usta, arms folded, raises one eyebrow with an amused smile and asks; then Diyor in the blurred foreground shrugs and waves one hand as he answers (his face stays turned away); "
  "Usta listens with his mouth closed and tilts his head. Sparkles twinkle on the rings in the window.",
  [("Usta", U_V, "Diyor, kim aytdi sevgi olmosda deb?"), ("Diyor", D_V, "Hamma biladi-ku! Kinoda ham, reklamada ham.")], "ud"),
 ("4", "s04", "Usta: «Diyor, eshit. 1938-yil, Amerika.»", "kaft yonidan o'tib, eski shaharga qarab suzish — o'tmishga «kirib boramiz»",
  "slow dolly forward and to the right, past Usta's raised palm, toward the old sepia city",
  "Usta speaks quietly, palm held up like «listen», then turns his head toward the old city. In the sepia part the old cars roll slowly to the right, "
  "men in long coats and hats keep walking away, the sepia dust drifts and the border with the golden street slowly spreads to the left.",
  [("Usta", U_V, "Diyor, eshit. Ming to'qqiz yuz o'ttiz sakkizinchi yil, Amerika.")], "u"),
 ("5", "s05", "Usta (kadr ortidan): «Dunyodagi eng katta olmos kompaniyasi reklama agentligini yollaydi…»", "stol ustidan olmosga qarab yuqoridan tushish — hammaning ko'zi olmosda",
  "slow crane down and forward over the table toward the glowing diamond",
  "The man at the easel points from the heart sketch to the ring sketch with his pencil; the men at the table lean in and nod slowly; the diamond on the velvet cushion pulses with light, "
  "dust floats in the sunbeams from the window. Old sepia film look.",
  [], ""),
 ("6", "s06", "Usta (kadr ortidan): «1947-yil. Bitta shior yoziladi: ‘Olmos — abadiy’…»", "mashinkaga juda sekin yaqinlashish — tarixiy lahza, shior tug'ilyapti",
  "very slow push-in toward the typewriter paper",
  "The hands type steadily on the old typewriter, the keys strike, the carriage slides to the left and rings at the end of the line; the desk lamp flickers softly, "
  "the diamond in the open ring box sparkles. Only hands and sleeves, no face. The paper line stays blurred and unreadable.",
  [], ""),
 ("6b", "s06", "Usta (kadr ortidan, davomi): «…Keyin bu asrning eng mashhur reklama shiori deb tan olindi.»", "uzuk qutisiga qarab sekin yon tomonga siljish — shior uzukka bog'lanadi",
  "slow sideways slide to the right from the typewriter to the open ring box, ending on the sparkling ring",
  "The typing hands stop; one hand pulls the finished sheet out of the typewriter and lays it on the desk next to the ring box (the text on it stays blurred and unreadable); "
  "the diamond in the red velvet box catches the lamp light and sparkles brighter, steam rises from the coffee cup. Only hands and sleeves, no face.",
  [], ""),
 ("7", "s07", "Diyor: «Yo'q, mumkin emas! Shiormi?!»", "yuzga tez «sakrab» yaqinlashish va titrash — hayrat zarbasi",
  "fast snap push-in to Diyor's face, then a tiny shake",
  "Diyor shouts in shock, eyes huge, eyebrows high, both hands pressing his cheeks; his hair bounces, the cyan outline flickers brighter for a moment. The rings in the window sparkle.",
  [("Diyor", D_V, "Yo'q, mumkin emas! Shiormi?!")], "d"),
 ("8", "s08", "Usta (kadr ortidan): «Televizorda, gazetada, kinoda — har joyda: uzuk olmosli bo'lsin, deyishdi…»", "eski narsalar ustidan chapdan o'ngga suzish — reklama hamma joyda edi",
  "slow sideways glide from left to right over the vintage objects, staying at the same distance as the image (no zoom in)",
  "The old TV screen flickers with the ring on the woman's hand, the film strip slides slowly, the cinema lamp in the corner glows, the diamonds on the poster, the newspaper and in the red box sparkle one after another. "
  "IMPORTANT: there are no letters anywhere: the newspapers show only big ring photos and soft grey blurred stripes instead of text, the poster has no title, no signs or labels appear; the camera never moves close enough to read anything.",
  [], ""),
 ("8b", "s08", "Usta (kadr ortidan, davomi): «…Keyinroq reklama aytdi: uzukka ikki oylik maoshingni sarfla.»", "qizil qutidagi uzukka sekin yaqinlashish — «ikki oylik maosh» shu toshda",
  "slow push-in from the whole table to the red velvet ring box, ending on the sparkling diamond",
  "The film strip stops, the old TV flickers and dims, the cinema lamp glows warmer; the diamond in the red box sparkles brighter and brighter as the camera comes closer. "
  "IMPORTANT: there are no letters anywhere: the newspapers show only ring photos and soft grey blurred stripes instead of text, no signs or labels appear.",
  [], ""),
 ("9", "s09", "Usta: «Sen sevgi sotib olmayapsan. Kredit sotib olyapsan.»", "fokus telefondan Diyor yuziga o'tadi — raqamdan hissiyotga",
  "rack focus from the phone chart to Diyor's face with a gentle push-in",
  "Usta, seen from behind, taps the growing bars on the screen twice and speaks; his jaw moves under the beard. Diyor's shock deepens: mouth opens wider, he swallows, mouth closed while listening. "
  "The chart on the screen stays exactly as in the image, no numbers.",
  [("Usta", U_V, "Sen sevgi sotib olmayapsan. Kredit sotib olyapsan.")], "ud"),
 ("10", "s10", "Diyor: «Demak, sevgilim olmosni emas, meni xohlaydi?»", "ikkalasiga sekin yaqinlashish — iliq, samimiy lahza",
  "slow gentle push-in toward both men",
  "Diyor, still scratching the back of his head, looks up at Usta and asks with a shy hopeful smile; Usta listens with his mouth closed, smiles warmly and pats Diyor's shoulder twice.",
  [("Diyor", D_V, "Demak, sevgilim olmosni emas, meni xohlaydi?")], "ud"),
 ("10b", "s10b", "Usta (kadr ortidan): «Inshaalloh.» — haqiqiy to'y", "dasturxon ustidan kelin-kuyovga sekin yaqinlashish — haqiqiy baxt",
  "slow push-in over the festive table toward the couple",
  "Diyor gently slips the simple thin ring on the bride's finger and smiles shyly and happily; the bride smiles softly under her veil, her face mostly hidden; "
  "relatives behind clap, a man plays the doira drum, string lights glow, steam rises from the plov. Nobody speaks.",
  [], "d"),
 ("11", "s11", "Usta: «Uchta savol. Bu uzukni kreditsiz ola olasanmi? To'ydan keyin necha oy to'laysan? Sevgiling bilan birga gaplashdingmi?»", "pastdan belgilarga qarab ko'tarilish — Usta ustoz sifatida ulug'lanadi",
  "low-angle slow crane up toward the three glowing symbols",
  "Usta keeps exactly three fingers raised and speaks with confidence; the symbols light up one by one as he talks: the ring, then the calculator, then the handshake, each with a small burst of sparkles.",
  [("Usta", U_V, "Uchta savol. Bu uzukni kreditsiz ola olasanmi? To'ydan keyin necha oy to'laysan?")], "u"),
 ("12", "s12", "Usta: «Ular senga tosh emas, ‘sevgi shu narxda’ degan tuyg'uni sotadi. Har gal so'ra: bundan kim foyda ko'radi?»", "juda sekin, ozgina yaqinlashish — asosiy fikr, yuz o'zgarmasin",
  "one continuous shot: a very slow, very small push-in, the framing stays a close-up as in the image",
  "Usta looks into the lens and speaks slowly and warmly with small natural head movements; on the question his eyebrows lift a little and he gives a small knowing smile. "
  "The sun flares softly behind him, passers-by far away keep walking.",
  [("Usta", U_V, "Ular senga tosh emas, sevgi shu narxda degan tuyg'uni sotadi. Har gal so'ra: bundan kim foyda ko'radi?")], "u"),
 ("13", "s13", "Usta: «To'y xarajatlaringiz ro'yxatini botimizga yozing: @sahiychishopbot…»", "sekin orqaga chekinish — xayrlashuv, bot va ikkalasi kadrda",
  "slow gentle pull-back, both men stay in the frame",
  "Usta holds the phone toward the viewer and speaks with a friendly smile; Diyor nods twice and keeps his thumb up, smiling, mouth closed. "
  "The phone screen stays exactly as in the image: the chat bubbles and the ring picture. Golden leaves drift, passers-by keep walking.",
  [("Usta", U_V, "To'y xarajatlaringiz ro'yxatini botimizga yozing: sahiychi shop bot.")], "ud"),
]
DUR = {"6b": 8, "8b": 8, "2b": 8, "3": 8, "5": 8, "6": 8, "8": 8, "11": 8, "12": 8, "13": 8}
def vp(n, cam, act, lines, chars):
    dial = f" {say(lines)}" if lines else ""
    lock = LOCK if chars == "ud" else LOCK_D if chars == "d" else LOCK_U if chars == "u" else LOCK_0
    end = END_OLD if n in OLD else END
    if n == "4": end = "The sepia old-city part keeps its old-photograph look; Usta and the golden street keep the cartoon style. " + end
    return f"Vertical 9:16, {DUR.get(n, 6)} seconds. Start from the attached image. Camera: {cam}. {act}{dial} {lock}{end}"
OLD = {"5", "6", "6b", "8", "8b"}

TOOL = {}
DONE = {"1": "Veo", "2": "Veo", "2b": "Veo", "3": "Veo", "4": "Veo (0–6.5 s)", "5": "Veo", "6": "Veo", "6b": "Veo", "7": "Veo"}
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

page = f"""<title>Olmos uzuk sahnalari</title>
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
<h1>«Olmos uzuk» <em>sahnalari</em></h1>
<p class="intro">15 ta sahna, tartib bilan. Har biri uchun: Veo'da «Frames to video» ni oching, rasmni <b>birinchi kadr</b> joyiga yuklang, <b>9:16</b> va sarlavhadagi uzunlikni (6 yoki 8 s) qo'ying, «Nusxa olish» bilan promptni qo'ying. Rasmlardagi yaqin fonuslar ko'k neonga bo'yalgan — yangi rasmni yuklang. 6 va 8-sahnalar ikkiga bo'lingan (6+6b, 8+8b — bitta rasmdan ikki xil kamera), Usta gapi to'liq sig'adi. 11-sahna tuzatildi. Diyor bor har promptda neon chizig'i, tarix sahnalarida (5, 6, 8) «eski surat, realistik ko'rinish o'zgarmasin» deb yozilgan. 5, 6, 8, 10b-sahnalarda hech kim gapirmaydi — Usta ovozi keyin qo'yiladi.</p>
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
