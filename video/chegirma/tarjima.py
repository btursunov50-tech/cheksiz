# «70 foiz chegirma»: timeline.SUB/TEXT (o'zbekcha) → timeline_en.py / timeline_ru.py (o'sha vaqtlar) va 3 ta .srt (video/final/chegirma/).
# Kliplardagi yozuvlar (-70%, 300 000, 170 000, -43%, taymer) raqam — tarjima kerak emas.
# Ishlatish: python3 video/chegirma/tarjima.py   (build_tl.py dan keyin)
import os, runpy
D = os.path.dirname(os.path.abspath(__file__))
tl = runpy.run_path(os.path.join(D, "timeline.py"))
EN = [
 "This 70% discount", "is not 70%.", "Do the math before you pay.",
 "Master, look! It was three hundred thousand,", "now it's one hundred seventy thousand!", "If I don't buy it now, I lose!",
 "Were you looking for this", "before you saw the discount?",
 "No...", "I just saw the discount.",
 "Let's do the math.", "From three hundred thousand, one hundred thirty thousand is off.", "That's not seventy,", "it's forty-three percent.",
 "Then why did they write seventy?",
 "A big number rushes your eyes,", "a timer rushes your hands.", "What you really need never needs a rush.",
 "Three checks.", "What's the price in another shop?", "Same size, quality and warranty?", "And did you need it yesterday too?",
 "So I count first,", "then I buy.",
 "Hey-hey, Diyor!", "Are you hunting for discounts in the shop", "or for a bride on the street?",
 "No, master... I'm... I'm counting!",
 "Keep your eyes on the price, bro.", "Math first, bride later!",
 "Let the need decide,", "not the percent.",
 "Take a photo of the price tag", "and send it to our bot:", "@sahiychishopbot",
 "It works out the real percent", "and tells you what to check.",
]
RU = [
 "Эта скидка 70%", "— вовсе не 70%.", "Посчитайте, прежде чем платить.",
 "Уста, смотрите! Было триста тысяч,", "стало сто семьдесят тысяч!", "Не куплю сейчас — проиграю!",
 "Ты искал эту вещь", "ещё до того, как увидел скидку?",
 "Нет...", "Просто увидел скидку.",
 "Давай посчитаем.", "С трёхсот тысяч скинули сто тридцать тысяч.", "Это не семьдесят,", "а сорок три процента.",
 "Тогда почему написали семьдесят?",
 "Большая цифра торопит глаза,", "таймер — руки.", "Нужная вещь не требует спешки.",
 "Три проверки.", "Сколько стоит в другом магазине?", "Размер, качество, гарантия — те же?", "И нужна ли тебе эта вещь была ещё вчера?",
 "Значит, сначала посчитаю,", "потом куплю.",
 "Эй-эй, Диёр!", "Ты в магазине скидки ищешь", "или на улице невесту?",
 "Нет, уста... я... я считаю!",
 "Смотри на цену, братишка.", "Сначала расчёт, потом невеста!",
 "Пусть покупку решает нужда,", "а не процент.",
 "Сфотографируйте ценник со скидкой", "и отправьте нашему боту:", "@sahiychishopbot",
 "Он посчитает настоящий процент", "и подскажет, что проверить.",
]
TEXT = {
 "en": ["300,000 → 170,000", "300,000 − 170,000 = 130,000", "130,000 ÷ 300,000 = 43%", "IF 70%: IT WOULD BE 90,000", "TODAY ONLY?",
        "1. OTHER SHOP'S PRICE?", "2. SIZE · QUALITY · WARRANTY", "3. NEEDED IT YESTERDAY?", "MATH FIRST, THEN BUY",
        "MATH FIRST, BRIDE LATER!", "NEED, NOT PERCENT", "@sahiychishopbot", "FINDS THE REAL PERCENT"],
 "ru": ["300 000 → 170 000", "300 000 − 170 000 = 130 000", "130 000 ÷ 300 000 = 43%", "ЕСЛИ БЫ 70%: БЫЛО БЫ 90 000", "ТОЛЬКО СЕГОДНЯ?",
        "1. ЦЕНА В ДРУГОМ МАГАЗИНЕ?", "2. РАЗМЕР · КАЧЕСТВО · ГАРАНТИЯ", "3. НУЖНО БЫЛО ВЧЕРА?", "СНАЧАЛА РАСЧЁТ, ПОТОМ ПОКУПКА",
        "СНАЧАЛА РАСЧЁТ, ПОТОМ НЕВЕСТА!", "НУЖДА, А НЕ ПРОЦЕНТ", "@sahiychishopbot", "НАЙДЁТ НАСТОЯЩИЙ ПРОЦЕНТ"],
}
assert len(EN) == len(RU) == len(tl["SUB"]), (len(EN), len(RU), len(tl["SUB"]))
assert all(len(v) == len(tl["TEXT"]) for v in TEXT.values())

def ts(x):
    ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

out = os.path.join(D, "..", "final", "chegirma"); os.makedirs(out, exist_ok=True)
for lang, tr in (("uz", None), ("en", EN), ("ru", RU)):
    sub = tl["SUB"] if tr is None else [(s, e, w, t) for (s, e, w, _), t in zip(tl["SUB"], tr)]
    if tr is not None:
        # uzun yozuvlar sig'ishi uchun o'lcham kichraytiriladi (1080 px kenglik)
        text = [(a, b, t, min(sz, int((1400 if lang == "ru" else 1900) / max(len(t), 1))), c, p) for (a, b, _, sz, c, p), t in zip(tl["TEXT"], TEXT[lang])]
        with open(os.path.join(D, f"timeline_{lang}.py"), "w") as f:
            f.write(f"# «70 foiz chegirma» {lang}: timeline.py SUB/TEXT vaqtlari, tarjima (tarjima.py yasaydi); yig.py --tl {lang}\n")
            f.write("SUB = [\n" + "".join(f" {x!r},\n" for x in sub) + "]\n")
            f.write("TEXT = [\n" + "".join(f" {x!r},\n" for x in text) + "]\n")
    with open(os.path.join(out, f"chegirma-{lang}.srt"), "w") as f:
        for i, (s, e, _, t) in enumerate(sub, 1):
            f.write(f"{i}\n{ts(s)} --> {ts(e)}\n{t}\n\n")
print("ok")
