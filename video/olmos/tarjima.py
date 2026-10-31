# «Olmos uzuk»: timeline.SUB/TEXT (o'zbekcha) → timeline_en.py / timeline_ru.py (o'sha vaqtlar) va 3 ta .srt (video/final/olmos/).
# Ishlatish: python3 video/olmos/tarjima.py   (build_tl.py dan keyin)
import os, runpy
D = os.path.dirname(os.path.abspath(__file__))
tl = runpy.run_path(os.path.join(D, "timeline.py"))
EN = [
 "Diamonds are not rare.", "You were told they are.",
 "Master, I'll buy a diamond ring for the wedding!", "I'll give my love a diamond ring and prove how strong my love is!", "But I don't have the money, so I'll take a loan!",
 "Diyor, who said love is in a diamond?", "Everybody knows it!", "In movies, in ads.",
 "Diyor, listen.", "1938, America.",
 "The world's biggest diamond company hires an advertising agency.", "The task:", "make people think a diamond is the sign of love.",
 "1947.", "One slogan is written:", "\u201cA diamond is forever\u201d.", "Later it was named the most famous ad slogan of the century.",
 "No way!", "A slogan?!",
 "On TV, in newspapers, in movies \u2014 everywhere:", "a ring must have a diamond, they said.", "Later the ads said:", "spend two months' salary on the ring.",
 "You're not buying love.", "You're buying a loan.",
 "So my love wants me, not the diamond?", "God willing.",
 "Three questions.", "Can you buy this ring without a loan?", "How many months will you pay after the wedding?", "Did you talk it over with your love?",
 "They don't sell you a stone, they sell you the feeling that \u201clove costs this much\u201d.", "Always ask:", "who profits from this?",
 "Send the list of your wedding costs to our bot:", "@sahiychishopbot.", "It works out the total and the extra you pay on the loan, and where you can save.",
]
RU = [
 "Бриллиант — не редкость.", "Тебе так сказали.",
 "Уста, куплю на свадьбу кольцо с бриллиантом!", "Подарю любимой кольцо с бриллиантом и докажу, как сильна моя любовь!", "Но денег не хватает, возьму кредит!",
 "Диёр, кто сказал, что любовь — в бриллианте?", "Все же знают!", "И в кино, и в рекламе.",
 "Диёр, послушай.", "1938 год, Америка.",
 "Крупнейшая в мире алмазная компания нанимает рекламное агентство.", "Задача:", "чтобы люди считали бриллиант знаком любви.",
 "1947 год.", "Пишется один слоган:", "«Бриллиант — навсегда».", "Позже его признали самым известным рекламным слоганом века.",
 "Не может быть!", "Слоган?!",
 "По телевизору, в газетах, в кино — везде:", "кольцо должно быть с бриллиантом, говорили они.", "Позже реклама сказала:", "потрать на кольцо две зарплаты.",
 "Ты покупаешь не любовь.", "Ты покупаешь кредит.",
 "Значит, любимая хочет меня, а не бриллиант?", "Иншаллах.",
 "Три вопроса.", "Можешь купить это кольцо без кредита?", "Сколько месяцев будешь платить после свадьбы?", "Вы обсудили это вместе с любимой?",
 "Тебе продают не камень, а чувство «любовь стоит столько».", "Всегда спрашивай:", "кому это выгодно?",
 "Напишите нашему боту список свадебных расходов:", "@sahiychishopbot.", "Он посчитает итог и переплату по кредиту и подскажет, где сэкономить.",
]
TEXT = {
 "en": ["1938 · USA", "1947", "\u201cA DIAMOND IS FOREVER\u201d", "RING = 2 MONTHS' SALARY?", "1. WITHOUT A LOAN?", "2. HOW MANY MONTHS?", "3. TALKED IT OVER?",
        "WHO PROFITS FROM THIS?", "@sahiychishopbot", "COUNTS YOUR WEDDING COSTS"],
 "ru": ["1938 · США", "1947", "«БРИЛЛИАНТ — НАВСЕГДА»", "КОЛЬЦО = 2 ЗАРПЛАТЫ?", "1. БЕЗ КРЕДИТА?", "2. СКОЛЬКО МЕСЯЦЕВ?", "3. ОБСУДИЛИ ВМЕСТЕ?",
        "КОМУ ЭТО ВЫГОДНО?", "@sahiychishopbot", "ПОСЧИТАЕТ РАСХОДЫ НА СВАДЬБУ"],
}
assert len(EN) == len(RU) == len(tl["SUB"]), (len(EN), len(RU), len(tl["SUB"]))
assert all(len(v) == len(tl["TEXT"]) for v in TEXT.values())

def ts(x):
    ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

out = os.path.join(D, "..", "final", "olmos"); os.makedirs(out, exist_ok=True)
for lang, tr in (("uz", None), ("en", EN), ("ru", RU)):
    sub = tl["SUB"] if tr is None else [(s, e, w, t) for (s, e, w, _), t in zip(tl["SUB"], tr)]
    if tr is not None:
        # uzun yozuvlar sig'ishi uchun o'lcham kichraytiriladi (1080 px kenglik)
        text = [(a, b, t, min(sz, int((1400 if lang == "ru" else 1900) / max(len(t), 1))), c, p) for (a, b, _, sz, c, p), t in zip(tl["TEXT"], TEXT[lang])]
        with open(os.path.join(D, f"timeline_{lang}.py"), "w") as f:
            f.write(f"# «Olmos uzuk» {lang}: timeline.py SUB/TEXT vaqtlari, tarjima (tarjima.py yasaydi); yig.py --tl {lang}\n")
            f.write("SUB = [\n" + "".join(f" {x!r},\n" for x in sub) + "]\n")
            f.write("TEXT = [\n" + "".join(f" {x!r},\n" for x in text) + "]\n")
    with open(os.path.join(out, f"olmos-{lang}.srt"), "w") as f:
        for i, (s, e, _, t) in enumerate(sub, 1):
            f.write(f"{i}\n{ts(s)} --> {ts(e)}\n{t}\n\n")
print("ok")
