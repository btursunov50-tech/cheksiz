# «Oyiga 490 million»: timeline.SUB/TEXT (o'zbekcha) → timeline_en.py / timeline_ru.py va 3 ta .srt (video/final/oyiga-490/).
import os, runpy
D = os.path.dirname(os.path.abspath(__file__))
tl = runpy.run_path(os.path.join(D, "timeline.py"))
EN = [
 "490 million soums a month.", "No experience needed.", "Would you apply?",
 "The post says:", "Claude is inviting people to remote work, applications until November 22, the task is to get around artificial intelligence.",
 "I, Claude, checked it myself.", "No such vacancy was found.",
 "But the basis is real:", "Anthropic has a safety program.", "Researchers find a weak spot in Claude's protection, quietly report it to the company and get a reward.",
 "It is not a salary.", "It is a reward for each flaw found, at most about thirty-five thousand dollars.",
 "And it is not \\u201cno experience\\u201d either:", "finding a new flaw takes deep knowledge.", "The post itself prefers engineers and scientists.",
 "Red flags:", "no source, no link, a \\u201churry up\\u201d deadline, and a \\u201cyou know who to send it to\\u201d click trap.",
 "Scammers use exactly such an ad to ask for a passport, a card and a verification code, or to take money in advance.",
 "Three rules.", "Check a vacancy only on the company's official site.", "An employer never asks for money, a card or a code in advance.", "If someone rushes you, stop.",
 "Every time, ask:", "who profits from this?",
 "Send a suspicious post or job text to our bot:", "@sahiychishopbot.", "It finds the red flags and teaches you step by step how to check.",
]
RU = [
 "490 миллионов сумов в месяц.", "Опыт не нужен.", "Подадите заявку?",
 "В посте сказано:", "Claude приглашает людей на удалённую работу, заявки до 22 ноября, задача — обойти искусственный интеллект.",
 "Я, Claude, сам проверил.", "Такой вакансии не нашлось.",
 "Но основа настоящая:", "у Anthropic есть программа безопасности.", "Исследователи находят слабое место в защите Claude, тайно сообщают компании и получают награду.",
 "Это не зарплата.", "Это награда за каждую найденную уязвимость, максимум около тридцати пяти тысяч долларов.",
 "И «без опыта» тоже неправда:", "чтобы найти новую уязвимость, нужны глубокие знания.", "В самом посте тоже предпочитают инженеров и учёных.",
 "Красные флаги:", "нет источника, нет ссылки, срок «спешите» и кликбейт «вы знаете, кому отправить».",
 "Мошенники именно таким объявлением просят паспорт, карту и код подтверждения или берут деньги вперёд.",
 "Три правила.", "Проверяйте вакансию только на официальном сайте компании.", "Работодатель не просит деньги, карту или код заранее.", "Если торопят, остановитесь.",
 "Каждый раз спрашивайте:", "кому это выгодно?",
 "Отправьте подозрительный пост или текст вакансии нашему боту:", "@sahiychishopbot.", "Он найдёт красные флаги и шаг за шагом научит проверять.",
]
TEXT = {
 "en": ["490 MILLION A MONTH?", "NO SUCH VACANCY", "BUG BOUNTY = REWARD FOR FLAWS", "NOT A SALARY", "NOT \\u201cNO EXPERIENCE\\u201d", "RED FLAGS", "1. OFFICIAL SITE", "2. NO MONEY, CARD, CODE", "3. RUSHED? STOP", "WHO PROFITS FROM THIS?", "@sahiychishopbot"],
 "ru": ["490 МИЛЛИОНОВ В МЕСЯЦ?", "ТАКОЙ ВАКАНСИИ НЕТ", "BUG BOUNTY = НАГРАДА ЗА УЯЗВИМОСТЬ", "НЕ ЗАРПЛАТА", "И ОПЫТ НУЖЕН", "КРАСНЫЕ ФЛАГИ", "1. ОФИЦИАЛЬНЫЙ САЙТ", "2. НИ ДЕНЕГ, НИ КАРТЫ, НИ КОДА", "3. ТОРОПЯТ? СТОП", "КОМУ ЭТО ВЫГОДНО?", "@sahiychishopbot"],
}
# tartib: TEXT ro'yxati build_tl.py dagi tartib bo'yicha
order = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert len(EN) == len(RU) == len(tl["SUB"]), (len(EN), len(RU), len(tl["SUB"]))
assert all(len(v) == len(tl["TEXT"]) for v in TEXT.values()), (len(tl["TEXT"]),)
def ts(x):
    ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"
out = os.path.join(D, "..", "final", "oyiga-490"); os.makedirs(out, exist_ok=True)
for lang, tr in (("uz", None), ("en", EN), ("ru", RU)):
    sub = tl["SUB"] if tr is None else [(s, e, w, t) for (s, e, w, _), t in zip(tl["SUB"], tr)]
    if tr is not None:
        text = [(a, b, t, min(sz, int((1400 if lang == "ru" else 1900) / max(len(t), 1))), c, p) for (a, b, _, sz, c, p), t in zip(tl["TEXT"], TEXT[lang])]
        with open(os.path.join(D, f"timeline_{lang}.py"), "w") as f:
            f.write(f"# «Oyiga 490 million» {lang}: tarjima.py yasaydi; yig.py --tl {lang}\n")
            f.write("SUB = [\n" + "".join(f" {x!r},\n" for x in sub) + "]\n")
            f.write("TEXT = [\n" + "".join(f" {x!r},\n" for x in text) + "]\n")
    with open(os.path.join(out, f"oyiga-490-{lang}.srt"), "w") as f:
        for i, (s, e, _, t) in enumerate(sub, 1):
            f.write(f"{i}\n{ts(s)} --> {ts(e)}\n{t}\n\n")
print("ok")
