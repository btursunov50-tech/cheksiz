# «Ta'm sehrlari»: videodagi 5 ta + 20 ta isbotli kombinatsiya → maza.html (Artifact). python3 ideas/maza/gen.py
import html, os, json
D = os.path.dirname(os.path.abspath(__file__)); e = html.escape
CAT = [  # (kalit, nom, tavsif)
 ("ilm", "Ilmiy tadqiqot bilan isbotlangan", "Laboratoriya tajribalarida takrorlangan, mexanizmi aniq"),
 ("kimyo", "Kimyoviy asosi bor", "Ikkalasida bir xil hid moddasi bor, shuning uchun o'xshash ta'm beradi"),
 ("tekstura", "Oziq-ovqat fani (tuzilish)", "Ta'm emas, tuzilishi o'zgaradi: krem, muzqaymoq, «go'sht»"),
 ("klassik", "Oshpazlik klassikasi", "Ko'p oshxonalarda tan olingan, lekin ta'm «almashmaydi», kuchayadi"),
 ("kuchsiz", "Kuchsiz da'vo", "Faqat qisman o'xshaydi"),
]
# (raqam, videoda?, formula, natija, izoh, kategoriya)
R = [
 (1, True, "🥔 chips + 🍅 cherry pomidor", "🍕 pitsa", "Pomidor va qovurilgan kartoshka ta'mi pitsaga yaqin, lekin pishloq va oregano yo'qligi uchun to'liq emas", "kuchsiz"),
 (2, True, "🍌 banan + 🥒 bodring", "🍈 qovun", "Bodring va qovun bir oiladan: ikkalasida «bodring aldegidi» (2,6-nonadienal) bor, banan shirinlik beradi", "kimyo"),
 (3, True, "🍅 pomidor + 🍚 shakar", "🍓 qulupnay", "Pomidorda qulupnayning asosiy hid moddasi furaneol bor; shakar qo'shilsa o'xshashlik seziladi", "kimyo"),
 (4, True, "🥒 bodring + 🍚 shakar", "🍈 qovun (deyiladi)", "Yana o'sha 2,6-nonadienal: qovun ta'mli moddalarda asosiy komponent", "kimyo"),
 (5, True, "🍋 limon + 🪵 dolchin + 🍯 asal", "🥤 kola", "Kola ta'mi sitrus moylari, dolchin, vanil va shakardan iborat; bu uchtasi asosini beradi", "kimyo"),
 (6, False, "🫐 mo'jiza mevasi + 🍋 limon", "🍋‍🟩 shirin limonad", "Mo'jiza mevasidagi miraculin oqsili nordonni 30–60 daqiqa shirin qilib ko'rsatadi", "ilm"),
 (7, False, "🌿 artishok, keyin 💧 suv", "🍬 shirin suv", "Artishokdagi moddalar til retseptorini vaqtincha to'sadi, suv ichilganda shirin tuyuladi", "ilm"),
 (8, False, "☕ qahva + 🧂 bir chimdim tuz", "☕ kamroq achchiq qahva", "Natriy achchiqlikni bosadi (Breslin va Beauchamp, 1995–1997)", "ilm"),
 (9, False, "🍊 greypfrut + 🧂 tuz", "🍊 shirinroq, kamroq achchiq", "Natriy achchiqni bosgani uchun shirinlik ko'proq seziladi", "ilm"),
 (10, False, "🍉 tarvuz + 🧂 ozgina tuz", "🍉 yanada shirin tarvuz", "Tuz qarama-qarshiligi va achchiqni bosish shirinlikni kuchaytiradi", "ilm"),
 (11, False, "🍫 qora shokolad + 🧂 dengiz tuzi", "🍫 yumshoqroq, shirinroq", "O'sha mexanizm: tuz kakaoning achchiqligini kamaytiradi", "ilm"),
 (12, False, "🍶 qatiq + 🌼 vanil", "🍬 shakarsiz «shirin» qatiq", "Vanil hidi miyada shirinlik bilan bog'langan, shakarsiz ham shirinroq tuyuladi", "ilm"),
 (13, False, "🌱 gimnema choyi + 🍚 shakar", "😶 ta'msiz shakar", "Gimnema kislotalari shirinlik retseptorini bir muddat to'sadi", "ilm"),
 (14, False, "🪥 tish pastasi + 🍊 apelsin sharbati", "🤢 achchiq sharbat (ogohlantirish)", "Pastadagi SLS shirinlik sezgisini pasaytirib, achchiqni kuchaytiradi", "ilm"),
 (15, False, "🥝 kivi yoki 🍍 ananas + 🥛 sut", "😖 achchiq sut (ogohlantirish)", "Fermentlar (aktinidin, bromelain) sut oqsilini achchiq bo'laklarga parchalaydi", "ilm"),
 (16, False, "🤍 oq shokolad + 🐟 ikra", "✨ kutilmagan juftlik", "Heston Blumenthal tajribasi: ikkalasida umumiy aminlar bor, «foodpairing» g'oyasi shundan boshlangan", "kimyo"),
 (17, False, "🍌 muzlatilgan banan → blender", "🍨 muzqaymoq", "Pektin va kam suv kremsimon tuzilish beradi, sut kerak emas", "tekstura"),
 (18, False, "🫘 no'xat suvi (akvafaba) → ko'pirtirish", "🥚 oqsil kremi (merenga)", "No'xat oqsillari va saponinlar tuxum oqidek ko'pik hosil qiladi", "tekstura"),
 (19, False, "🥑 avokado + 🍫 kakao + 🍯 asal", "🍮 shokoladli mus", "Avokado yog'i krem tuzilishini beradi, ta'mi kakaodan", "tekstura"),
 (20, False, "🌳 yosh jekfrut + 🍖 ziravor", "🥩 «go'sht» tolasi", "Pishmagan jekfrut tolasi pishgan go'shtdek ajraladi", "tekstura"),
 (21, False, "🥦 gulkaram → maydalash", "🍚 «guruch»", "Mayda bo'laklar guruchdek ko'rinadi, uglevod kam", "tekstura"),
 (22, False, "🍓 qulupnay + 🍷 balzamik sirka", "🍓 yorqinroq qulupnay", "Nordon sirka shirinlikni kontrast bilan kuchaytiradi", "klassik"),
 (23, False, "🍓 qulupnay + ⚫ qora murch", "🍓 o'tkirroq, xushbo'yroq", "Murch issiqligi meva hidini ochadi", "klassik"),
 (24, False, "🍫 shokolad + 🌶 achchiq qalampir", "🔥 «Aztek shokoladi»", "Qadimiy Markaziy Amerika ichimligi; kapsaitsin shirinlikka issiqlik qo'shadi", "klassik"),
 (25, False, "🍏 olma + 🪵 dolchin", "🥧 olma pirogi ta'mi", "Pirog ta'mining asosi aynan shu juftlik", "klassik"),
]
cnt = {k: sum(1 for r in R if r[5] == k) for k, _, _ in CAT}
mx = max(cnt.values())
bars = "".join(
  f'<div class="bar-row" tabindex="0" data-tip="{e(n)}: {cnt[k]} ta ({e(d)})"><span class="bar-lbl">{e(n)}</span>'
  f'<span class="bar-track"><span class="bar c-{k}" style="width:{cnt[k]/mx*100:.1f}%"></span></span><span class="bar-val">{cnt[k]}</span></div>'
  for k, n, d in CAT)
catname = {k: n for k, n, _ in CAT}
cards = "".join(
  f'<article class="card"><header><span class="num">{n}</span>{"<span class=vid>videoda</span>" if v else ""}'
  f'<span class="tag"><i class="dot c-{c}"></i>{e(catname[c])}</span></header>'
  f'<p class="f">{e(a)}</p><p class="res">= {e(b)}</p><p class="why">{e(w)}</p></article>' for n, v, a, b, w, c in R)
page = f"""<title>Ta'm sehrlari</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,800&family=Manrope:wght@400;600;700&display=swap">
<style>
/* Layout: headline, one bar chart of counts per evidence level, then a 2-column grid of 25 numbered combination cards. */
:root{{--bg:#fbfaf7;--card:#ffffff;--line:#e6e2d9;--fg:#1f1d1a;--muted:#6b665d;--track:#f0ede6;
--c-ilm:#2a78d6;--c-kimyo:#eb6834;--c-tekstura:#1baf7a;--c-klassik:#eda100;--c-kuchsiz:#e87ba4;
--display:"Fraunces",Georgia,serif;--body:"Manrope",system-ui,sans-serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#1a1a19;--card:#232321;--line:#363531;--fg:#f0efec;--muted:#c3c2b7;--track:#2c2b28;
--c-ilm:#3987e5;--c-kimyo:#d95926;--c-tekstura:#199e70;--c-klassik:#c98500;--c-kuchsiz:#d55181;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#1a1a19;--card:#232321;--line:#363531;--fg:#f0efec;--muted:#c3c2b7;--track:#2c2b28;
--c-ilm:#3987e5;--c-kimyo:#d95926;--c-tekstura:#199e70;--c-klassik:#c98500;--c-kuchsiz:#d55181;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font-family:var(--body);font-size:15px;line-height:1.5;margin:0}}
.wrap{{max-width:900px;margin:0 auto;padding-block:28px 56px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:grid;gap:24px}}
h1{{font-family:var(--display);font-weight:800;font-size:clamp(32px,7vw,52px);line-height:1.05;margin:0;text-wrap:balance}}
.lead{{margin:0;color:var(--muted);max-width:62ch}}
.panel{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:18px;display:grid;gap:12px}}
.panel h2{{font-family:var(--display);font-size:22px;margin:0}}
.bar-row{{display:grid;grid-template-columns:minmax(0,15em) minmax(0,1fr) 2.2em;gap:10px;align-items:center;padding:4px 0;outline:none}}
.bar-row:focus-visible{{outline:2px solid var(--fg);outline-offset:2px;border-radius:4px}}
.bar-lbl{{font-size:14px;min-width:0}} .bar-val{{font-weight:700;font-variant-numeric:tabular-nums;text-align:right}}
.bar-track{{height:22px;background:var(--track);border-radius:0 4px 4px 0;display:block}}
.bar{{display:block;height:100%;border-radius:0 4px 4px 0}}
@media (max-width:560px){{.bar-row{{grid-template-columns:minmax(0,1fr) 2em}} .bar-lbl{{grid-column:1/-1}} .bar-track{{grid-column:1}}}}
.c-ilm{{background:var(--c-ilm)}} .c-kimyo{{background:var(--c-kimyo)}} .c-tekstura{{background:var(--c-tekstura)}} .c-klassik{{background:var(--c-klassik)}} .c-kuchsiz{{background:var(--c-kuchsiz)}}
.total{{margin:0;color:var(--muted);font-size:14px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,260px),1fr));gap:12px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px;display:grid;gap:6px;align-content:start}}
.card header{{display:flex;gap:8px;align-items:center;flex-wrap:wrap}}
.num{{font-family:var(--display);font-weight:800;font-size:20px;font-variant-numeric:tabular-nums;min-width:1.6em}}
.vid{{font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;border:1px solid var(--fg);border-radius:99px;padding:1px 8px}}
.tag{{font-size:12px;color:var(--muted);display:inline-flex;gap:6px;align-items:center}}
.dot{{width:10px;height:10px;border-radius:50%;display:inline-block}}
.f{{margin:0;font-weight:700;font-size:16px}} .res{{margin:0;font-weight:700;font-size:16px}} .why{{margin:0;color:var(--muted);font-size:13.5px}}
#tip{{position:fixed;pointer-events:none;background:var(--fg);color:var(--bg);font-size:13px;padding:6px 10px;border-radius:6px;max-width:260px}}
.src{{font-size:13px;color:var(--muted);margin:0}} .src a{{color:inherit}}
</style>
<div class="wrap">
<h1>Ta'm sehrlari: 25 ta juftlik</h1>
<p class="lead">Videodagi 5 ta «ikki mahsulot = boshqa ta'm» va yana 20 ta isbotli variant. Har biri qanchalik isbotlangani bo'yicha rang bilan belgilangan.</p>
<section class="panel" aria-label="Isbot darajasi bo'yicha soni">
<h2>Isbot darajasi bo'yicha</h2>
{bars}
<p class="total">Jami: {len(R)} ta (videoda {sum(1 for r in R if r[1])}, yangi {sum(1 for r in R if not r[1])}). Ustuni ustiga olib boring: izoh chiqadi.</p>
</section>
<div class="grid">{cards}</div>
<p class="src">Manbalar: Breslin & Beauchamp, «Salt enhances flavour by suppressing bitterness», Nature 1997; furaneol (pomidor, qulupnay) va 2,6-nonadienal (bodring, qovun) — oziq-ovqat kimyosi ma'lumotlari. Ta'm har odamda biroz farq qiladi. 14 va 15 — sinab ko'rmang, ogohlantirish.</p>
</div>
<div id="tip" hidden></div>
<script>
const tip=document.getElementById('tip');
document.querySelectorAll('.bar-row').forEach(r=>{{
 const show=(x,y)=>{{tip.textContent=r.dataset.tip;tip.hidden=false;tip.style.left=Math.min(x+12,innerWidth-280)+'px';tip.style.top=(y+12)+'px'}};
 r.addEventListener('mousemove',ev=>show(ev.clientX,ev.clientY));
 r.addEventListener('mouseleave',()=>tip.hidden=true);
 r.addEventListener('focus',()=>{{const b=r.getBoundingClientRect();show(b.left,b.bottom)}});
 r.addEventListener('blur',()=>tip.hidden=true);
}});
</script>
"""
open(os.path.join(D, "maza.html"), "w").write(page)
print(cnt, len(R))
