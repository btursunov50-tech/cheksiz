# «Telefoning eskirmagan»: timeline.SUB/TEXT (o'zbekcha) → timeline_en.py / timeline_ru.py (o'sha vaqtlar) va 3 ta .srt (video/final/eskirish/).
# Ishlatish: python3 video/eskirish/tarjima.py   (build_tl.py dan keyin)
import os, runpy
D = os.path.dirname(os.path.abspath(__file__))
tl = runpy.run_path(os.path.join(D, "timeline.py"))
EN = [
 "Your phone didn't get old.", "Maybe only its battery got tired.",
 "Master, my phone freezes, the charge doesn't last till evening.", "It's been two years, it's old.", "I'll buy a new one on installments!",
 "Diyor, who told you it freezes because it's old?",
 "Everybody knows that!",
 "Quiet, Diyor. Look.", "Geneva, December 1924.",
 "The world's biggest light bulb makers agreed:", "an ordinary bulb must not burn more than a thousand hours.",
 "Before that, bulbs burned up to 2,500 hours.", "A factory whose bulbs lasted longer paid a fine.",
 "On purpose?!",
 "2017.", "One of the most famous phone companies admitted a secret.",
 "What secret?",
 "It slowed down phones with worn-out batteries.", "So they wouldn't suddenly shut down.", "But it didn't tell the owners.",
 "People said \u201cmy phone is old\u201d and bought a new one.", "Often, just replacing the battery was enough.",
 "When it came out, the company agreed to pay people in the US up to half a billion dollars.", "In France it was fined 25 million euros.",
 "So my phone isn't old either,", "maybe just its battery is tired?",
 "Maybe.",
 "Forgive me, old friend... it wasn't your fault!",
 "Don't hug it, check its battery!",
 "Three checks before you buy a new one.", "What's the battery health?", "Is the storage full?", "How much does a new battery cost?",
 "They sell you not a phone, but the feeling that you got old.", "Always ask: who profits from this?",
 "Is your phone freezing? Send its model to our bot:", "@sahiychishopbot",
 "It shows you where to find the battery health", "and what to check before buying a new one.",
]
RU = [
 "Твой телефон не устарел.", "Может, просто устала батарея.",
 "Уста, телефон тормозит, заряда не хватает до вечера.", "Уже два года, устарел.", "Возьму новый в рассрочку!",
 "Диёр, кто сказал, что он тормозит, потому что устарел?",
 "Все же знают!",
 "Тихо, Диёр. Смотри.", "Женева, декабрь 1924 года.",
 "Крупнейшие производители лампочек в мире договорились:", "обычная лампочка не должна гореть больше тысячи часов.",
 "До этого лампочки горели до 2500 часов.", "Завод, чьи лампочки горели дольше, платил штраф.",
 "Нарочно?!",
 "2017 год.", "Одна из самых известных телефонных компаний признала секрет.",
 "Какой секрет?",
 "Она сама замедляла телефоны со старой батареей.", "Чтобы они внезапно не выключались.", "Но владельцам не сказала.",
 "Люди думали: «телефон устарел» — и покупали новый.", "А часто хватило бы просто заменить батарею.",
 "Когда это вскрылось, компания согласилась выплатить людям в США до полумиллиарда долларов.", "Во Франции её оштрафовали на 25 миллионов евро.",
 "Значит, мой телефон тоже не устарел,", "просто батарея, может, устала?",
 "Может быть.",
 "Прости, старый друг... ты не виноват!",
 "Не обнимай, проверь батарею!",
 "Три проверки перед покупкой нового.", "Сколько процентов здоровье батареи?", "Не забита ли память?", "Сколько стоит замена батареи?",
 "Тебе продают не телефон, а чувство, что ты устарел.", "Всегда спрашивай: кому это выгодно?",
 "Телефон тормозит? Напишите модель нашему боту:", "@sahiychishopbot",
 "Он покажет, где посмотреть здоровье батареи,", "и что проверить перед покупкой нового.",
]
TEXT = {
 "en": ["GENEVA · 1924", "BULB: NO MORE THAN 1,000 HOURS", "BEFORE: 2,500 HOURS", "LASTS LONGER — FINE", "2017",
        "OLD BATTERY → SLOW PHONE", "\u201cIT'S OLD!\u201d → NEW PHONE", "OFTEN A BATTERY WAS ENOUGH", "US: UP TO $500,000,000",
        "FRANCE: \u20ac25,000,000", "1. BATTERY HEALTH?", "2. STORAGE FULL?", "3. BATTERY PRICE?", "WHO PROFITS FROM THIS?",
        "@sahiychishopbot", "TEACHES YOU TO CHECK THE BATTERY"],
 "ru": ["ЖЕНЕВА · 1924", "ЛАМПОЧКА: НЕ БОЛЬШЕ 1000 ЧАСОВ", "РАНЬШЕ: 2500 ЧАСОВ", "ГОРИТ ДОЛЬШЕ — ШТРАФ", "2017",
        "СТАРАЯ БАТАРЕЯ → МЕДЛЕННЫЙ ТЕЛЕФОН", "«УСТАРЕЛ!» → НОВЫЙ ТЕЛЕФОН", "ЧАСТО ХВАТИЛО БЫ БАТАРЕИ", "США: ДО $500 000 000",
        "ФРАНЦИЯ: €25 000 000", "1. ЗДОРОВЬЕ БАТАРЕИ?", "2. ПАМЯТЬ ЗАБИТА?", "3. ЦЕНА ЗАМЕНЫ?", "КОМУ ЭТО ВЫГОДНО?",
        "@sahiychishopbot", "НАУЧИТ ПРОВЕРЯТЬ БАТАРЕЮ"],
}
assert len(EN) == len(RU) == len(tl["SUB"]), (len(EN), len(RU), len(tl["SUB"]))
assert all(len(v) == len(tl["TEXT"]) for v in TEXT.values())

def ts(x):
    ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

out = os.path.join(D, "..", "final", "eskirish"); os.makedirs(out, exist_ok=True)
for lang, tr in (("uz", None), ("en", EN), ("ru", RU)):
    sub = tl["SUB"] if tr is None else [(s, e, w, t) for (s, e, w, _), t in zip(tl["SUB"], tr)]
    if tr is not None:
        # uzun yozuvlar sig'ishi uchun o'lcham kichraytiriladi (1080 px kenglik)
        text = [(a, b, t, min(sz, int((1400 if lang == "ru" else 1900) / max(len(t), 1))), c, p) for (a, b, _, sz, c, p), t in zip(tl["TEXT"], TEXT[lang])]
        with open(os.path.join(D, f"timeline_{lang}.py"), "w") as f:
            f.write(f"# «Telefoning eskirmagan» {lang}: timeline.py SUB/TEXT vaqtlari, tarjima (tarjima.py yasaydi); yig.py --tl {lang}\n")
            f.write("SUB = [\n" + "".join(f" {x!r},\n" for x in sub) + "]\n")
            f.write("TEXT = [\n" + "".join(f" {x!r},\n" for x in text) + "]\n")
    with open(os.path.join(out, f"eskirish-{lang}.srt"), "w") as f:
        for i, (s, e, _, t) in enumerate(sub, 1):
            f.write(f"{i}\n{ts(s)} --> {ts(e)}\n{t}\n\n")
print("ok")
