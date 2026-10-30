# «Bepul yetkazish»: timeline.SUB/TEXT (o'zbekcha) → timeline_en.py / timeline_ru.py (o'sha vaqtlar) va 3 ta .srt (video/final/yetkazish/).
# Ishlatish: python3 video/yetkazish/tarjima.py   (build_tl.py dan keyin)
import os, runpy
D = os.path.dirname(os.path.abspath(__file__))
tl = runpy.run_path(os.path.join(D, "timeline.py"))
EN = [
 "Free delivery isn't free.", "You still pay for it.",
 "Master, I got shampoo, delivery is twenty thousand.", "If I add forty thousand more, it's free!",
 "Do you really need that forty-thousand thing?", "Not really...", "but it's free!",
 "Quiet, Diyor.", "Look.", "2002, America.",
 "The world's biggest online store cut free delivery from 99 dollars to 49, and two months later to 25.",
 "People added more to their carts to reach the limit.", "The store called it a \u201cpositive result\u201d.",
 "So they were counting on us?!",
 "Only in France they charged one franc, about twenty cents, for delivery.", "Sales there barely grew.",
 "The moment they made it zero, sales grew there too.",
 "Scientists tested it:", "most people chose the expensive chocolate.", "When the cheap one became \u201cfree\u201d, everyone switched to the free one.",
 "So the word \u201cfree\u201d fools the brain?", "It doesn't fool it.", "It rushes it.",
 "Do the math:", "you saved twenty thousand and spent forty.",
 "Three rules.", "Buy only what you need.", "Put things you'll buy soon anyway into one order.", "And ask:", "would I buy this if delivery weren't paid?",
 "They don't sell you delivery, they sell you the feeling of \u201cfree\u201d.", "Always ask:", "who profits from this?",
 "Send your cart and the delivery terms to our bot:", "@sahiychishopbot.", "It works out how much extra you pay for free delivery and what you can remove.",
]
RU = [
 "Бесплатная доставка — не бесплатная.", "Ты всё равно за неё платишь.",
 "Уста, взял шампунь, доставка двадцать тысяч.", "Добавлю ещё на сорок тысяч — будет бесплатно!",
 "А та вещь за сорок тысяч тебе нужна?", "Не особо...", "но ведь бесплатно!",
 "Тихо, Диёр.", "Смотри.", "2002 год, Америка.",
 "Крупнейший в мире интернет-магазин снизил порог бесплатной доставки с 99 долларов до 49, а через два месяца — до 25.",
 "Чтобы дотянуть до порога, люди добавляли в корзину ещё товары.", "Магазин назвал это «положительным результатом».",
 "Так они на нас рассчитывали?!",
 "Только во Франции за доставку брали один франк, около двадцати центов.", "Продажи там почти не выросли.",
 "Как только цену сделали нулём, продажи выросли и там.",
 "Учёные проверили:", "большинство выбирало дорогой шоколад.", "Как только дешёвый сделали «бесплатным», все перешли на бесплатный.",
 "Значит, слово «бесплатно» обманывает мозг?", "Не обманывает.", "Торопит.",
 "Посчитай:", "сэкономил двадцать тысяч, потратил сорок.",
 "Три правила.", "Бери только нужное.", "То, что всё равно купишь скоро, собери в один заказ.", "И спроси:", "купил бы я это, если бы доставка была платной?",
 "Тебе продают не доставку, а чувство «бесплатно».", "Всегда спрашивай:", "кому это выгодно?",
 "Напишите нашему боту, что в корзине и условия доставки:", "@sahiychishopbot.", "Он посчитает, сколько вы переплачиваете за бесплатную доставку и что можно убрать.",
]
TEXT = {
 "en": ["DELIVERY: 20,000", "+40,000 → FREE?", "2002 · USA", "$99 → $49 → $25", "MORE INTO THE CART", "FRANCE: 1 FRANC", "0 → SALES GREW",
        "\u201cFREE\u201d → EVERYONE TOOK IT", "SAVED: 20,000", "SPENT: 40,000", "1. ONLY WHAT YOU NEED", "2. ONE ORDER", "3. WOULD I BUY IT ANYWAY?",
        "WHO PROFITS FROM THIS?", "@sahiychishopbot", "COUNTS THE EXTRA COST"],
 "ru": ["ДОСТАВКА: 20 000", "+40 000 → БЕСПЛАТНО?", "2002 · США", "$99 → $49 → $25", "ЕЩЁ В КОРЗИНУ", "ФРАНЦИЯ: 1 ФРАНК", "0 → ПРОДАЖИ ВЫРОСЛИ",
        "«БЕСПЛАТНО» → ВСЕ ВЗЯЛИ", "СЭКОНОМИЛ: 20 000", "ПОТРАТИЛ: 40 000", "1. ТОЛЬКО НУЖНОЕ", "2. ОДИН ЗАКАЗ", "3. КУПИЛ БЫ И ТАК?",
        "КОМУ ЭТО ВЫГОДНО?", "@sahiychishopbot", "ПОСЧИТАЕТ ПЕРЕПЛАТУ"],
}
assert len(EN) == len(RU) == len(tl["SUB"]), (len(EN), len(RU), len(tl["SUB"]))
assert all(len(v) == len(tl["TEXT"]) for v in TEXT.values())

def ts(x):
    ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

out = os.path.join(D, "..", "final", "yetkazish"); os.makedirs(out, exist_ok=True)
for lang, tr in (("uz", None), ("en", EN), ("ru", RU)):
    sub = tl["SUB"] if tr is None else [(s, e, w, t) for (s, e, w, _), t in zip(tl["SUB"], tr)]
    if tr is not None:
        # uzun yozuvlar sig'ishi uchun o'lcham kichraytiriladi (1080 px kenglik)
        text = [(a, b, t, min(sz, int((1400 if lang == "ru" else 1900) / max(len(t), 1))), c, p) for (a, b, _, sz, c, p), t in zip(tl["TEXT"], TEXT[lang])]
        with open(os.path.join(D, f"timeline_{lang}.py"), "w") as f:
            f.write(f"# «Bepul yetkazish» {lang}: timeline.py SUB/TEXT vaqtlari, tarjima (tarjima.py yasaydi); yig.py --tl {lang}\n")
            f.write("SUB = [\n" + "".join(f" {x!r},\n" for x in sub) + "]\n")
            f.write("TEXT = [\n" + "".join(f" {x!r},\n" for x in text) + "]\n")
    with open(os.path.join(out, f"yetkazish-{lang}.srt"), "w") as f:
        for i, (s, e, _, t) in enumerate(sub, 1):
            f.write(f"{i}\n{ts(s)} --> {ts(e)}\n{t}\n\n")
print("ok")
