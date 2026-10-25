# «Robot bilan bir piyola choy»: timeline.SUB (o'zbekcha) → timeline_en.py / timeline_ru.py (o'sha vaqtlar, tarjima) va 3 ta .srt.
# Ishlatish: python3 video/robot/tarjima.py
import os, runpy
D = os.path.dirname(os.path.abspath(__file__))
tl = runpy.run_path(os.path.join(D, "timeline.py"))
EN = [
 "Money leaks out of your shop every day.", "And you don't even see it.",
 "What money? I only use you for pictures and videos.",
 "Pictures are fine. But that's not what I was made for.",
 "In 1956 scientists asked: can a machine do a person's thinking work?",
 "All day you watch the till, the phone, the customers.", "But nobody watches the cook's table.",
 "One lavash went out without sauce.", "The customer said nothing.", "But he never came back.",
 "Should I hire a supervisor? He needs a salary.",
 "One small camera. It only watches the table.", "Meat, vegetables, sauce.",
 "Stop.", "The sauce isn't in yet.",
 "Only for lavash?", "No.",
 "The most expensive work is done with the head, not the hands.", "Doctors, lawyers.",
 "How much does it cost to train one good doctor?",
 "First he has to be born.", "Then school.", "Then university.", "Then years of practice.",
 "And you see him for twenty minutes.", "And you pay for all those years.",
 "Is an AI doctor cheaper?",
 "I explain your test results in plain words.", "I tell you what to ask your doctor.", "Even at three in the morning.",
 "And lawyers?",
 "A draft contract.", "Explaining hard words.", "Finding a hidden fine in a rental contract.", "In a few minutes.",
 "So we don't need doctors and lawyers?",
 "We do.", "Someone has to check my answers.", "Especially when the case is complex.", "Or when a mistake is very costly.",
 "Cameras, test results, contracts...", "Won't you get into my phone, my money?",
 "I never ask for passwords.", "Run from any «AI» that asks for your password.", "That's not AI, that's a scammer.",
 "So should I fire the cook?",
 "No.", "I can't wrap a lavash. The cook is the hands, I'm the eyes.",
 "Do you have a shop too?",
]
RU = [
 "Из твоего магазина каждый день утекают деньги.", "А ты этого не видишь.",
 "Какие деньги? Я тебя использую только для картинок и видео.",
 "Картинки — это хорошо. Но меня придумали не для этого.",
 "В 1956 году учёные спросили: может ли машина выполнять умственную работу человека?",
 "Ты весь день смотришь на кассу, телефон, клиентов.", "А на стол повара никто не смотрит.",
 "Один лаваш ушёл без соуса.", "Клиент промолчал.", "Но больше не вернулся.",
 "Нанять контролёра? Ему нужна зарплата.",
 "Одна маленькая камера. Она смотрит только на стол.", "Мясо, овощи, соус.",
 "Стоп.", "Соус ещё не добавлен.",
 "Только для лаваша?", "Нет.",
 "Самая дорогая работа делается головой, а не руками.", "Врач, юрист.",
 "Сколько стоит подготовить одного хорошего врача?",
 "Сначала он должен родиться.", "Потом школа.", "Потом институт.", "Потом годы практики.",
 "А ты приходишь к нему на двадцать минут.", "И платишь за все эти годы.",
 "ИИ-врач дешевле?",
 "Я объясню твои анализы простыми словами.", "Подскажу, что спросить у врача.", "Даже в три часа ночи.",
 "А юрист?",
 "Черновик договора.", "Объяснение сложных слов.", "Найти скрытый штраф в договоре аренды.", "За несколько минут.",
 "Тогда врач и юрист не нужны?",
 "Нужны.", "Мои ответы должен кто-то проверять.", "Особенно если дело сложное.", "Или если ошибка очень дорогая.",
 "Камера, анализы, договоры...", "А ты не залезешь в мой телефон, в мои деньги?",
 "Я не прошу пароли.", "Беги от «ИИ», который просит твой пароль.", "Это не ИИ, это мошенник.",
 "Тогда уволить повара?",
 "Нет.", "Я не умею заворачивать лаваш. Повар — руки, я — глаза.",
 "У вас тоже есть магазин?",
]
TEXT = {
 "en": ["Ask our bot:", "@sahiychishopbot", "How can AI help your shop?"],
 "ru": ["Спросите бота:", "@sahiychishopbot", "Как ИИ поможет вашему магазину?"],
}
assert len(EN) == len(RU) == len(tl["SUB"]), (len(EN), len(RU), len(tl["SUB"]))

def ts(x):
    ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

out = os.path.join(D, "..", "final", "robot"); os.makedirs(out, exist_ok=True)
for lang, tr in (("uz", None), ("en", EN), ("ru", RU)):
    sub = tl["SUB"] if tr is None else [(s, e, w, t) for (s, e, w, _), t in zip(tl["SUB"], tr)]
    if tr is not None:
        text = [(a, b, t, sz, c, p) for (a, b, _, sz, c, p), t in zip(tl["TEXT"], TEXT[lang])]
        with open(os.path.join(D, f"timeline_{lang}.py"), "w") as f:
            f.write(f"# «Robot bilan bir piyola choy» {lang}: timeline.py SUB/TEXT vaqtlari, tarjima (tarjima.py yasaydi); --tl {lang}\n")
            f.write("SUB = [\n" + "".join(f" {x!r},\n" for x in sub) + "]\n")
            f.write("TEXT = [\n" + "".join(f" {x!r},\n" for x in text) + "]\n")
    with open(os.path.join(out, f"robot-{lang}.srt"), "w") as f:
        for i, (s, e, _, t) in enumerate(sub, 1):
            f.write(f"{i}\n{ts(s)} --> {ts(e)}\n{t}\n\n")
print("ok")
