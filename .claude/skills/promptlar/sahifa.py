#!/usr/bin/env python3
"""Rasm / Veo prompt sahifasi (Artifact) — har sahna: rasm yoki namunalar, nima bo'ladi, kamera, prompt, «Nusxa olish».

from sahifa import page, VEO_NEG, neon
page("Loyiha sahnalari", "«Loyiha» <em>sahnalari</em>", "Kirish matni...", cards, "video/<loyiha>/sahnalar.html")
card = dict(num="3", title="3-sahna — video, 9:16 (tik), 8 s", shot="web/s03.webp" yoki None,
            refs=[("web/ref_diyor.webp", "ref_diyor.png")], what="...", cam="...", prompt="...")
Rasmlar sahifa yonidagi web/ papkasida bo'lishi va Artifact publish'da `files` bilan yuborilishi kerak.
"""
import html
e = html.escape
VEO_NEG = "Negative: no text, no letters, no numbers, no subtitles, no captions, no logos, no brand names, no watermarks, no extra people, no extra hands, no ring above any head"
def neon(name="Diyor"):
    return (f"{name}'s thin bright cyan-blue neon line runs exactly along his whole outer silhouette (hair, face, hoodie, arms, legs) with a soft blue glow; "
            "it moves with him in every frame and never disappears; nothing else in the frame has this outline.")
CSS = """:root{--bg:#0b0f1a;--card:#131a2a;--line:#26304a;--fg:#eef2fb;--muted:#9fb0cf;--acc:#2fd3ff;--red:#ff3b4f;--gold:#f2b544;
--display:"Cormorant Garamond",Georgia,serif;--body:"Manrope",system-ui,sans-serif;--mono:"JetBrains Mono",ui-monospace,monospace;color-scheme:dark}
body{background:var(--bg);color:var(--fg);font-family:var(--body);font-size:15px;line-height:1.55;margin:0}
.wrap{max-width:820px;margin:0 auto;padding-block:28px 60px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:grid;gap:22px}
h1{font-family:var(--display);font-weight:700;font-size:clamp(30px,6vw,44px);margin:0;line-height:1.1;text-wrap:balance} h1 em{font-style:normal;color:var(--red)}
.intro{color:var(--muted);margin:0;max-width:66ch}
.card{display:grid;gap:14px;background:var(--card);border:1px solid var(--line);border-radius:8px;padding:16px}
header{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap} .num{font-family:var(--mono);color:var(--acc);font-size:14px}
h2{font-family:var(--display);font-weight:700;font-size:26px;margin:0}
.row{display:grid;grid-template-columns:170px minmax(0,1fr);gap:16px;align-items:start}
@media (max-width:560px){.row{grid-template-columns:minmax(0,1fr)} .side{grid-template-columns:repeat(2,minmax(0,140px))}}
.side{display:grid;gap:8px;align-content:start} .fig{margin:0;display:grid;gap:4px} .fig img{width:100%;max-width:100%;border-radius:4px;display:block;border:1px solid var(--line)}
.fig figcaption,.rh{font-size:12px;color:var(--muted);font-family:var(--mono);margin:0}
.txt{min-width:0;display:flex;flex-direction:column;gap:6px} .lbl{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.what,.cam{margin:0 0 6px} .cam{color:var(--acc)}
pre{margin:0;white-space:pre-wrap;word-break:break-word;font-family:var(--mono);font-size:12.5px;line-height:1.6;background:var(--bg);border:1px solid var(--line);border-radius:6px;padding:12px;user-select:all}
.copy{align-self:flex-start;font:600 15px var(--body);color:#111;background:var(--acc);border:0;border-radius:8px;padding:10px 18px;cursor:pointer;margin-top:4px}
.copy.done{background:var(--gold)} .copy:focus-visible{outline:2px solid var(--fg);outline-offset:2px}"""
JS = """document.querySelectorAll('.copy').forEach(b=>b.addEventListener('click',()=>{
 const pre=document.getElementById(b.dataset.t);const t=pre.textContent;
 const ok=()=>{b.textContent='Nusxa olindi';b.classList.add('done');setTimeout(()=>{b.textContent='Nusxa olish';b.classList.remove('done')},1800)};
 const sel=()=>{const r=document.createRange();r.selectNodeContents(pre);const s=getSelection();s.removeAllRanges();s.addRange(r);b.textContent='Belgilandi, nusxa oling'};
 try{navigator.clipboard.writeText(t).then(ok,sel)}catch(e){sel()}
}));"""
def page(title, h1, intro, cards, out):
    cs = []
    for c in cards:
        side = ""
        if c.get("shot"): side += f'<figure class="fig"><img src="{c["shot"]}" alt="{e(c["num"])}-sahna"><figcaption>{e(c.get("shotcap", "Veo/ChatGPT ga shuni yuklang"))}</figcaption></figure>'
        if c.get("refs"):
            side += '<p class="rh">Biriktiring:</p>' + "".join(f'<figure class="fig"><img src="{src}" alt="{e(cap)}"><figcaption>{e(cap)}</figcaption></figure>' for src, cap in c["refs"])
        if not side: side = '<p class="rh">Namuna kerak emas</p>'
        pid = "p" + "".join(ch for ch in c["num"] if ch.isalnum())
        extra = (f'<span class="lbl">Kamera</span><p class="cam">{e(c["cam"])}</p>' if c.get("cam") else "")
        cs.append(f'<article class="card"><header><span class="num">{e(c["num"])}</span><h2>{e(c["title"])}</h2></header>'
                  f'<div class="row"><div class="side">{side}</div><div class="txt"><span class="lbl">{e(c.get("whatlbl", "Nima bo'ladi"))}</span>'
                  f'<p class="what">{e(c.get("what", ""))}</p>{extra}<pre id="{pid}">{e(c["prompt"])}</pre>'
                  f'<button class="copy" data-t="{pid}">Nusxa olish</button></div></div></article>')
    html_ = (f'<title>{e(title)}</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n'
             '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Manrope:wght@400;600&family=JetBrains+Mono:wght@400&display=swap">\n'
             f'<style>\n/* Layout: one column of scene cards, image left, prompt right (single dark theme, deliberately). */\n{CSS}\n</style>\n'
             f'<div class="wrap">\n<h1>{h1}</h1>\n<p class="intro">{e(intro)}</p>\n{"".join(cs)}\n</div>\n<script>\n{JS}\n</script>\n')
    open(out, "w").write(html_)
    return out
