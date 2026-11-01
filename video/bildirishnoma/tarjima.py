# «Telefon jiringlaydi»: timeline.SUB/TEXT (o'zbekcha) → timeline_en.py / timeline_ru.py (o'sha vaqtlar) va 3 ta .srt (video/final/yetkazish/).
# Ishlatish: python3 video/yetkazish/tarjima.py   (build_tl.py dan keyin)
import os, runpy
D = os.path.dirname(os.path.abspath(__file__))
tl = runpy.run_path(os.path.join(D, "timeline.py"))
EN = [
 "When your phone rings, you don't control the phone. The phone controls you.",
 "Master, one minute, a message came!",
 "Diyor, listen.", "2006, America.",
 "An engineer invented infinite scrolling:", "the page never ends, you just keep scrolling down.",
 "When a page ends, you stop.", "When it doesn't, you don't.",
 "Later he openly said he regretted his invention.",
 "Do apps keep us hooked on purpose?!",
 "According to one study, the average user gets close to forty-six notifications a day.",
 "Apps make money from your attention:", "the longer you look, the more ads they show.",
 "Three rules.", "Turn off useless notifications.", "Turn on silent mode at night.", "Before opening an app, ask:", "why am I opening it?",
 "Phone silent, me calm!",
 "They don't sell you the app, they sell you the fear of \u201cmissing out\u201d.",
 "Every time, ask:", "who profits from this?",
 "If you don't know which notification to turn off, write the app's name to our bot:", "@sahiychishopbot.", "It teaches you step by step.",
]
RU = [
 "Когда звонит телефон, это не ты управляешь телефоном, а телефон управляет тобой.",
 "Уста, минуточку, пришло сообщение!",
 "Диёр, слушай.", "2006 год, Америка.",
 "Один инженер придумал бесконечную прокрутку:", "страница не кончается, ты всё листаешь вниз.",
 "Кончилась страница — ты остановился.", "Не кончилась — не остановишься.",
 "Позже он открыто сказал, что жалеет о своём изобретении.",
 "Приложения нас нарочно удерживают?!",
 "По одному исследованию, средний пользователь получает почти сорок шесть уведомлений в день.",
 "Приложения зарабатывают на твоём внимании:", "чем дольше смотришь, тем больше рекламы показывают.",
 "Три правила.", "Отключи ненужные уведомления.", "Включи ночью тихий режим.", "Перед тем как открыть приложение, спроси:", "зачем я его открываю?",
 "Телефон молчит, я спокоен!",
 "Тебе продают не приложение, а страх «пропустить».",
 "Каждый раз спрашивай:", "кому это выгодно?",
 "Если не знаешь, какое уведомление отключить, напиши название приложения нашему боту:", "@sahiychishopbot.", "Он научит шаг за шагом.",
]
TEXT = {
 "en": ["2006 \u00b7 USA", "INFINITE SCROLL", "~46 NOTIFICATIONS A DAY", "ATTENTION = MONEY", "1. TURN OFF USELESS ONES", "2. SILENT MODE AT NIGHT", "3. WHY AM I OPENING IT?", "WHO PROFITS FROM THIS?", "@sahiychishopbot"],
 "ru": ["2006 \u00b7 США", "БЕСКОНЕЧНАЯ ЛЕНТА", "~46 УВЕДОМЛЕНИЙ В ДЕНЬ", "ВНИМАНИЕ = ДЕНЬГИ", "1. ОТКЛЮЧИ НЕНУЖНОЕ", "2. НОЧЬЮ ТИХИЙ РЕЖИМ", "3. ЗАЧЕМ Я ОТКРЫВАЮ?", "КОМУ ЭТО ВЫГОДНО?", "@sahiychishopbot"],
}
assert len(EN) == len(RU) == len(tl["SUB"]), (len(EN), len(RU), len(tl["SUB"]))
assert all(len(v) == len(tl["TEXT"]) for v in TEXT.values())

def ts(x):
    ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

out = os.path.join(D, "..", "final", "bildirishnoma"); os.makedirs(out, exist_ok=True)
for lang, tr in (("uz", None), ("en", EN), ("ru", RU)):
    sub = tl["SUB"] if tr is None else [(s, e, w, t) for (s, e, w, _), t in zip(tl["SUB"], tr)]
    if tr is not None:
        # uzun yozuvlar sig'ishi uchun o'lcham kichraytiriladi (1080 px kenglik)
        text = [(a, b, t, min(sz, int((1400 if lang == "ru" else 1900) / max(len(t), 1))), c, p) for (a, b, _, sz, c, p), t in zip(tl["TEXT"], TEXT[lang])]
        with open(os.path.join(D, f"timeline_{lang}.py"), "w") as f:
            f.write(f"# «Telefon jiringlaydi» {lang}: timeline.py SUB/TEXT vaqtlari, tarjima (tarjima.py yasaydi); yig.py --tl {lang}\n")
            f.write("SUB = [\n" + "".join(f" {x!r},\n" for x in sub) + "]\n")
            f.write("TEXT = [\n" + "".join(f" {x!r},\n" for x in text) + "]\n")
    with open(os.path.join(out, f"bildirishnoma-{lang}.srt"), "w") as f:
        for i, (s, e, _, t) in enumerate(sub, 1):
            f.write(f"{i}\n{ts(s)} --> {ts(e)}\n{t}\n\n")
print("ok")
