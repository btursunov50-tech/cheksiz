# «Konserva»: timeline.SUB/TEXT (o'zbekcha) → timeline_en.py / timeline_ru.py (o'sha vaqtlar) va 3 ta .srt (video/final/yetkazish/).
# Ishlatish: python3 video/yetkazish/tarjima.py   (build_tl.py dan keyin)
import os, runpy
D = os.path.dirname(os.path.abspath(__file__))
tl = runpy.run_path(os.path.join(D, "timeline.py"))
EN = [
 "One date on the can says \u201csafe\u201d, another says \u201ctasty\u201d.", "They are not the same.",
 "Imagine:", "you walk into a store and pick up a can of food.", "You see the date and relax.",
 "But what does this date actually mean?",
 "First, learn the difference between the labels.", "Production date shows when the product was made.", "Expiry date: the product is safe until this date.", "\u201cBest before\u201d is a quality date.",
 "Do not eat an expired product.",
 "Second, don't blindly trust dry goods.", "Rice, pasta and flour last long if stored properly, but moisture and insects can spoil them early.",
 "Third, look at the can.", "If it is swollen, leaking, badly rusted or its seams are damaged, do not eat it.",
 "The most dangerous thing is botulism:", "a disease that can cause severe poisoning.", "A dangerous can sometimes looks fine from outside.", "So never taste a suspicious can to check it.",
 "Fourth, dairy products.", "If the smell or look has changed, do not drink it.", "Even if the smell is normal, it doesn't fully guarantee safety.",
 "In the store, do three things.", "Check the date.", "Make sure the package is intact.", "Follow the storage conditions.",
 "Don't buy a suspicious product just because it's cheap.", "You can save money, but it's not worth risking your health.",
 "Send a photo of the product label to our bot:", "@sahiychishopbot.", "It explains what the label means and teaches you how to check, step by step.",
 "Send this video to your loved ones too:", "it may save someone from a serious mistake.",
]
RU = [
 "Одна дата на банке говорит «безопасно», другая — «вкусно».", "Это не одно и то же.",
 "Представьте:", "вы зашли в магазин и взяли банку консервов.", "Увидели дату и успокоились.",
 "Но что эта дата на самом деле означает?",
 "Во-первых, поймите разницу между надписями.", "Дата изготовления показывает, когда продукт сделан.", "Срок годности — до этой даты продукт безопасен.", "«Лучше употребить до» — это дата качества.",
 "Не ешьте продукт с истёкшим сроком.",
 "Во-вторых, не доверяйте слепо сухим продуктам.", "Рис, макароны и мука долго хранятся при правильном хранении, но влага и насекомые могут испортить их раньше срока.",
 "В-третьих, посмотрите на банку.", "Если она вздулась, течёт, сильно заржавела или повреждены швы — не ешьте.",
 "Самое опасное — ботулизм:", "болезнь, которая может вызвать тяжёлое отравление.", "Опасная консерва иногда выглядит нормально.", "Поэтому никогда не пробуйте подозрительные консервы на вкус.",
 "В-четвёртых, молочные продукты.", "Если запах или вид изменились, не пейте.", "Даже если запах нормальный, это не гарантирует полную безопасность.",
 "В магазине сделайте три вещи.", "Проверьте дату.", "Убедитесь, что упаковка целая.", "Соблюдайте условия хранения.",
 "Не покупайте сомнительный продукт только потому, что он дешёвый.", "Деньги можно сэкономить, но здоровьем рисковать не стоит.",
 "Отправьте фото этикетки продукта нашему боту:", "@sahiychishopbot.", "Он объяснит, что значат надписи, и шаг за шагом научит проверять.",
 "Отправьте это видео и близким:", "возможно, оно убережёт кого-то от серьёзной ошибки.",
]
TEXT = {
 "en": ["TWO DATES, TWO MEANINGS", "PRODUCTION DATE", "EXPIRY DATE = SAFE", "\u201cBEST BEFORE\u201d = QUALITY", "DON'T EAT EXPIRED FOOD", "SWOLLEN \u00b7 LEAKING \u00b7 RUSTED", "BOTULISM: NEVER TASTE", "1. CHECK THE DATE", "2. IS THE PACKAGE INTACT?", "3. STORAGE CONDITIONS", "@sahiychishopbot", "SEND A PHOTO OF THE LABEL"],
 "ru": ["ДВЕ ДАТЫ, ДВА СМЫСЛА", "ДАТА ИЗГОТОВЛЕНИЯ", "СРОК ГОДНОСТИ = БЕЗОПАСНО", "«ЛУЧШЕ ДО» = КАЧЕСТВО", "НЕ ЕШЬТЕ ПРОСРОЧЕННОЕ", "ВЗДУТАЯ · ТЕЧЁТ · РЖАВАЯ", "БОТУЛИЗМ: НЕ ПРОБУЙТЕ", "1. ПРОВЕРЬТЕ ДАТУ", "2. УПАКОВКА ЦЕЛАЯ?", "3. УСЛОВИЯ ХРАНЕНИЯ", "@sahiychishopbot", "ОТПРАВЬТЕ ФОТО ЭТИКЕТКИ"],
}
assert len(EN) == len(RU) == len(tl["SUB"]), (len(EN), len(RU), len(tl["SUB"]))
assert all(len(v) == len(tl["TEXT"]) for v in TEXT.values())

def ts(x):
    ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

out = os.path.join(D, "..", "final", "konserva"); os.makedirs(out, exist_ok=True)
for lang, tr in (("uz", None), ("en", EN), ("ru", RU)):
    sub = tl["SUB"] if tr is None else [(s, e, w, t) for (s, e, w, _), t in zip(tl["SUB"], tr)]
    if tr is not None:
        # uzun yozuvlar sig'ishi uchun o'lcham kichraytiriladi (1080 px kenglik)
        text = [(a, b, t, min(sz, int((1400 if lang == "ru" else 1900) / max(len(t), 1))), c, p) for (a, b, _, sz, c, p), t in zip(tl["TEXT"], TEXT[lang])]
        with open(os.path.join(D, f"timeline_{lang}.py"), "w") as f:
            f.write(f"# «Konserva» {lang}: timeline.py SUB/TEXT vaqtlari, tarjima (tarjima.py yasaydi); yig.py --tl {lang}\n")
            f.write("SUB = [\n" + "".join(f" {x!r},\n" for x in sub) + "]\n")
            f.write("TEXT = [\n" + "".join(f" {x!r},\n" for x in text) + "]\n")
    with open(os.path.join(out, f"konserva-{lang}.srt"), "w") as f:
        for i, (s, e, _, t) in enumerate(sub, 1):
            f.write(f"{i}\n{ts(s)} --> {ts(e)}\n{t}\n\n")
print("ok")
