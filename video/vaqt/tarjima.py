# timeline.SUB (o'zbekcha, vaqtlar ovozdan) → timeline_en.py / timeline_ru.py (o'sha vaqtlar, tarjima matn) va 3 ta .srt
import sys, os
sys.path.insert(0, "video/vaqt"); import timeline as tl
EN = ["You can't buy time.", "But you sell it every day.", "Grandpa, the plov is ready.", "Later, my boy.", "Later.",
      "Don't be afraid.", "I didn't come to take anything.", "I came to show you your account.",
      "Give me back my past years, take all my gold!", "Time that has passed can't be sold.", "Life is in Allah's hands alone.",
      "I only show.", "Thirty years.", "Give back just one...", "No one can bring back the past.",
      "Only Allah knows how much is left.", "But today and now are still yours.", "Grandpa, the plov is getting cold.",
      "Right now, my boy!", "Right now!", "Time that's gone never returns.", "That's why: today and now.",
      "Grandpa, today's AI tip!", "Don't waste your time.", "Learn one new thing every day.",
      "A free AI tip on our channel every morning,", "and send your questions to our bot."]
RU = ["Время нельзя купить.", "Но ты продаёшь его каждый день.", "Дедушка, плов готов.", "Потом, сынок.", "Потом.",
      "Не бойся.", "Я пришёл не забирать.", "Я пришёл показать твой счёт.",
      "Верни мои прошлые годы, забери всё золото!", "Прошедшее время не продаётся.", "Жизнь только в руках Аллаха.",
      "Я лишь показываю.", "Тридцать лет.", "Верни хотя бы одно...", "Прошлое никто не вернёт.",
      "Сколько осталось, знает только Аллах.", "Но сегодня и сейчас ещё твои.", "Дедушка, плов остывает.",
      "Сейчас, сынок!", "Сейчас!", "Ушедшее время не вернуть.", "Поэтому — сегодня и сейчас.",
      "Дедушка, сегодняшний совет по ИИ!", "Не тратьте время зря.", "Каждый день узнавайте что-то новое.",
      "Каждое утро на нашем канале бесплатный совет по ИИ,", "а вопросы пишите нашему боту."]
assert len(EN) == len(RU) == len(tl.SUB)
T0, T1 = tl.TEXT[0][:2], tl.TEXT[1][:2]
TX = {"en": [("Profit —\\Ntoday and now.", 64), ("TODAY", 120)], "ru": [("Прибыль —\\Nсегодня и сейчас.", 60), ("СЕГОДНЯ", 110)]}
def tc(x): return f"{int(x//3600):02}:{int(x%3600//60):02}:{int(x%60):02},{int(round(x%1*1000)):03}"
for lang, tr in (("uz", None), ("en", EN), ("ru", RU)):
    subs = [(s, e, w, tr[i] if tr else x) for i, (s, e, w, x) in enumerate(tl.SUB)]
    if tr:
        clip = [c + f"_{lang}" if c in ("h01", "t11", "k14") else c for c in tl.CLIP]
        (a, b), (c, d) = T0, T1
        txt = [(a, b, TX[lang][0][0], TX[lang][0][1], "FFC34D", (560, 820)), (c, d, TX[lang][1][0], TX[lang][1][1], "FFC34D", (540, 330))]
        with open(f"video/vaqt/timeline_{lang}.py", "w") as f:
            f.write(f"# «VAQT» {lang}: vaqtlar timeline.py dan (tarjima.py yasaydi), --tl {lang}\n")
            f.write("SUB = [\n" + "".join(f" {s!r},\n" for s in subs) + "]\n")
            f.write(f"TEXT = {txt!r}\nCLIP = {clip!r}\n")
    os.makedirs("video/final/vaqt", exist_ok=True)
    with open(f"video/final/vaqt/vaqt-{lang}.srt", "w") as f:
        for i, (s, e, w, x) in enumerate(subs, 1):
            f.write(f"{i}\n{tc(s)} --> {tc(e)}\n{x}\n\n")
print("ok")
