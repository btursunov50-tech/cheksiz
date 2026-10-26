# «Oyiga atigi…»: timeline.SUB (o'zbekcha) → timeline_en.py / timeline_ru.py (o'sha vaqtlar, tarjima) va 3 ta .srt.
# Ishlatish: python3 video/oyiga/tarjima.py
import os, runpy
D = os.path.dirname(os.path.abspath(__file__))
tl = runpy.run_path(os.path.join(D, "timeline.py"))
EN = [
 "Only one hundred thousand a month.", "But nobody told you the total.",
 "Master, it's only one hundred thousand a month!", "I can easily afford it.",
 "For how many months?", "How much will you pay in total?",
 "One hundred thousand...", "twelve months...", "one million two hundred thousand.",
 "Now add the down payment,", "and the service fee?",
 "The seller only told me the monthly payment.", "I didn't ask the cash price.",
 "A price cut into small pieces hides a big total.", "Put the two side by side.",
 "Ask three questions.", "What's the cash price?", "How much will I pay in total?",
 "What happens if I'm late?",
 "I'm not in a hurry.", "I'll do the math first.",
 "After «only ... a month» one question is left:", "how much in total, in the end?",
 "Send a photo of the price tag or the contract to our bot:", "@sahiychishopbot",
 "It works out how much you'll pay in total,", "and tells you which questions to ask the seller.",
]
RU = [
 "Всего сто тысяч в месяц.", "Но никто не сказал, сколько всего.",
 "Уста, всего сто тысяч в месяц!", "Спокойно возьму.",
 "На сколько месяцев?", "Сколько заплатишь всего?",
 "Сто тысяч...", "двенадцать месяцев...", "миллион двести тысяч.",
 "А если добавить первый взнос,", "и плату за услуги?",
 "Продавец назвал только платёж в месяц.", "А цену за наличные я не спросил.",
 "Цена, разбитая на кусочки, прячет большую сумму.", "Положи их рядом.",
 "Задай три вопроса.", "Сколько стоит за наличные?", "Сколько я заплачу всего?",
 "Что будет, если опоздаю?",
 "Не тороплюсь.", "Сначала посчитаю.",
 "После «всего ... в месяц» остаётся один вопрос:", "сколько всего в итоге?",
 "Отправьте нашему боту фото ценника или договора:", "@sahiychishopbot",
 "Он посчитает, сколько вы заплатите всего,", "и подскажет, что спросить у продавца.",
]
TEXT = {
 "en": ["ONLY 100,000 A MONTH", "12 MONTHS", "100,000 × 12 = 1,200,000", "+ DOWN PAYMENT", "+ SERVICE FEE",
        "1. CASH PRICE?", "2. TOTAL?", "3. IF I'M LATE?", "HOW MUCH IN TOTAL?", "@sahiychishopbot"],
 "ru": ["ВСЕГО 100 000 В МЕСЯЦ", "12 МЕСЯЦЕВ", "100 000 × 12 = 1 200 000", "+ ПЕРВЫЙ ВЗНОС", "+ ПЛАТА ЗА УСЛУГИ",
        "1. ЦЕНА ЗА НАЛИЧНЫЕ?", "2. СКОЛЬКО ВСЕГО?", "3. А ЕСЛИ ОПОЗДАЮ?", "СКОЛЬКО ВСЕГО В ИТОГЕ?", "@sahiychishopbot"],
}
assert len(EN) == len(RU) == len(tl["SUB"]), (len(EN), len(RU), len(tl["SUB"]))
assert all(len(v) == len(tl["TEXT"]) for v in TEXT.values())

def ts(x):
    ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

out = os.path.join(D, "..", "final", "oyiga"); os.makedirs(out, exist_ok=True)
for lang, tr in (("uz", None), ("en", EN), ("ru", RU)):
    sub = tl["SUB"] if tr is None else [(s, e, w, t) for (s, e, w, _), t in zip(tl["SUB"], tr)]
    if tr is not None:
        text = [(a, b, t, sz, c, p) for (a, b, _, sz, c, p), t in zip(tl["TEXT"], TEXT[lang])]
        with open(os.path.join(D, f"timeline_{lang}.py"), "w") as f:
            f.write(f"# «Oyiga atigi…» {lang}: timeline.py SUB/TEXT vaqtlari, tarjima (tarjima.py yasaydi); --tl {lang}\n")
            f.write("SUB = [\n" + "".join(f" {x!r},\n" for x in sub) + "]\n")
            f.write("TEXT = [\n" + "".join(f" {x!r},\n" for x in text) + "]\n")
    with open(os.path.join(out, f"oyiga-{lang}.srt"), "w") as f:
        for i, (s, e, _, t) in enumerate(sub, 1):
            f.write(f"{i}\n{ts(s)} --> {ts(e)}\n{t}\n\n")
print("ok")
