#!/usr/bin/env python3
"""Qattiq taqrizchi: video/<loyiha>/POSTS.md dagi post matnlarini kanal qoidalari
bo'yicha tekshiradi va 10 ballik baho beradi.

G'oya google-research/paper-orchestra (Apache-2.0) dagi «taqrizchi -> tuzatish ->
qayta baho, faqat ball oshsa qabul» siklidan olingan; kod o'zimizniki.

Ishlatish: python3 .claude/skills/taqrizchi/post_tekshir.py video/tugma/POSTS.md [--json]
"""
import json, re, subprocess, sys, os

AI = {
    "uz": "Video sun'iy intellekt yordamida yaratilgan.",
    "ru": "Видео создано с помощью искусственного интеллекта.",
    "en": "Made with AI.",
}
BOT = "@sahiychishopbot"
BOT_LINK = "t.me/sahiychishopbot"
SITE = "cheksiz-one.vercel.app/infinite"
HOOK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ig-reel", "hookscore.py")


def blocks(md):
    """(sarlavha, ichidagi matn) juftlari: har ``` blok oldingi ## sarlavha va oraliq matn bilan."""
    out, head, ctx = [], "", ""
    lines = md.split("\n"); i = 0
    while i < len(lines):
        l = lines[i]
        if l.startswith("## "):
            head, ctx = l[3:].strip(), ""
        elif l.startswith("```"):
            j = i + 1; body = []
            while j < len(lines) and not lines[j].startswith("```"):
                body.append(lines[j]); j += 1
            out.append((head, ctx.strip(), "\n".join(body)))
            ctx = ""; i = j
        else:
            ctx += l + "\n"
        i += 1
    return out


def kind(head, ctx):
    w = head.lower().split(" ")[0] if head else ""
    c = ctx.lower()
    if w.startswith("telegram"): return "telegram"
    if w.startswith("linkedin"): return "linkedin"
    if w.startswith("instagram") or w.startswith("facebook"): return "instagram"
    if w.startswith("youtube"):
        if "title" in c or "sarlavha" in c or "title" in head.lower() or "sarlavha" in head.lower(): return "yt_title"
        return "yt_desc"
    return None


def hookscore(text):
    try:
        r = subprocess.run([sys.executable, HOOK, "--hook", text, "--json"], capture_output=True, text=True, timeout=30)
        d = json.loads(r.stdout)
        if isinstance(d, list): d = d[0]
        return float(d.get("score", d.get("overall", 0)))
    except Exception:
        return None


def check(path):
    md = open(path, encoding="utf-8").read()
    header = md.split("## ")[0]
    suno = "suno" in header.lower()
    res = []  # (platforma, qoida, ok, izoh)
    def add(p, rule, ok, note=""): res.append((p, rule, bool(ok), note))
    seen = set()
    for head, ctx, b in blocks(md):
        k = kind(head, ctx)
        if not k: continue
        seen.add(k)
        if k == "yt_title":
            t = b.strip().splitlines()[0] if b.strip() else ""
            add(k, "100 belgidan qisqa", len(t) <= 100, f"{len(t)} belgi")
            add(k, "#shorts bor", "#shorts" in t.lower())
            add(k, "< > belgilari yo'q", "<" not in t and ">" not in t)
            hs = hookscore(re.sub(r"#\w+", "", t).strip())
            if hs is not None:
                add(k, "hook bahosi 50 dan yuqori", hs >= 50, f"{hs:.1f}")
            continue
        lang = {"telegram": "uz", "instagram": "ru", "yt_desc": "en", "linkedin": "en"}[k]
        add(k, "AI satri oxirida", AI[lang] in b)
        add(k, "< > belgilari yo'q" if k == "yt_desc" else "matn bo'sh emas",
            ("<" not in b and ">" not in b) if k == "yt_desc" else len(b.strip()) > 50)
        if k in ("telegram", "instagram", "yt_desc"):
            add(k, "bot chaqiruvi bor", BOT in b or BOT_LINK in b)
            add(k, "izoh so'rovi (savol) bor", "?" in b)
        if k in ("instagram", "yt_desc"):
            add(k, "bot havolasi bosiladigan (t.me/...)", BOT_LINK in b)
        if suno and k != "linkedin":
            add(k, "«Music: made with Suno»", "Music: made with Suno" in b)
        if "«на YouTube»" in b or "on YouTube" in b and "youtu" not in b:
            add(k, "«YouTube'da» deyilsa havola bor", False)
        if k == "telegram":
            add(k, "sayt havolasi bor", SITE in b)
    for need in ("telegram", "yt_title", "yt_desc", "instagram", "linkedin"):
        if need not in seen:
            add(need, "bo'lim topildi", False, "POSTS.md da yo'q")
    ok = sum(r[2] for r in res); n = len(res) or 1
    return res, round(10 * ok / n, 1)


def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    res, score = check(sys.argv[1])
    if "--json" in sys.argv:
        print(json.dumps({"score": score, "checks": [dict(platform=p, rule=r, ok=o, note=n) for p, r, o, n in res]}, ensure_ascii=False, indent=1)); return
    print(f"\nTAQRIZCHI: {sys.argv[1]}\n" + "=" * 60)
    for p, r, o, n in res:
        print(f"  {'✅' if o else '❌'} {p:<10} {r}{'  (' + n + ')' if n else ''}")
    print("-" * 60 + f"\n  BAHO: {score}/10   ({'tayyor' if score == 10 else 'tuzatish kerak'})\n")

if __name__ == "__main__":
    main()
