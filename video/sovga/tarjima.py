# «Sovg'a yutdingiz!»: timeline.SUB (o'zbekcha) → timeline_en.py / timeline_ru.py (o'sha vaqtlar, tarjima) va 3 ta .srt.
# Ishlatish: python3 video/sovga/tarjima.py
import os, runpy
D = os.path.dirname(os.path.abspath(__file__))
tl = runpy.run_path(os.path.join(D, "timeline.py"))
EN = [
 "Stop!", "Never read this SMS code to a stranger who says «You won».",
 "Wow! I won an iPhone!", "I only have five minutes.",
 "Hello, I'm calling from the bank.", "You've received a code.",
 "Just tell it to me and we'll process your gift.", "One moment, one moment...",
 "Before you say the code, read the SMS out loud to me.",
 "Telegram code...", "«Do not give this code to anyone»...",
 "This isn't a gift code.", "It's the key to your Telegram.",
 "Give away the key, and you open the door yourself.",
 "They don't give gifts.", "They ask your loved ones for money in your name.",
 "Three signs.", "You didn't enter any contest.", "They're rushing you.",
 "They're asking for a code.", "All three? It's a trap.",
 "Hang up.", "Call the bank yourself on its official number.",
 "Turn on Telegram's cloud password:", "even if they get the code, they can't log in.",
 "Five minutes are over.", "And I lost nothing.",
 "A real gift never asks you for a code.",
 "Got a suspicious message?", "Send a screenshot to our bot: @sahiychishopbot",
 "It tells you if it's a scam,", "and teaches you step by step to turn on the cloud password.",
]
RU = [
 "Стоп!", "Никогда не читай SMS-код незнакомцу, который говорит «Вы выиграли».",
 "Ого! Я выиграл iPhone!", "Всего пять минут осталось.",
 "Здравствуйте, вас беспокоят из банка.", "Вам пришёл код.",
 "Назовите его, и мы оформим ваш подарок.", "Сейчас, сейчас...",
 "Прежде чем назвать код, прочитай мне SMS вслух.",
 "Код Telegram...", "«Никому не сообщайте этот код»...",
 "Это не код подарка.", "Это ключ от твоего Telegram.",
 "Отдашь ключ — сам откроешь им дверь.",
 "Подарков они не дарят.", "От твоего имени они просят деньги у близких.",
 "Три признака.", "Ты не участвовал в конкурсе.", "Тебя торопят.",
 "У тебя просят код.", "Все три — это ловушка.",
 "Положи трубку.", "Сам позвони в банк по официальному номеру.",
 "Включи облачный пароль в Telegram:", "даже узнав код, они не войдут.",
 "Пять минут прошли.", "А я ничего не потерял.",
 "Настоящий подарок никогда не просит код.",
 "Пришло подозрительное сообщение?", "Отправьте скриншот нашему боту: @sahiychishopbot",
 "Он объяснит, мошенничество это или нет,", "и пошагово научит включить облачный пароль.",
]
TEXT = {
 "en": ["1. NO CONTEST", "2. RUSHING YOU", "3. ASKING FOR A CODE", "@sahiychishopbot"],
 "ru": ["1. НЕТ КОНКУРСА", "2. ТОРОПЯТ", "3. ПРОСЯТ КОД", "@sahiychishopbot"],
}
assert len(EN) == len(RU) == len(tl["SUB"])

def ts(x):
    ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

out = os.path.join(D, "..", "final", "sovga"); os.makedirs(out, exist_ok=True)
for lang, tr in (("uz", None), ("en", EN), ("ru", RU)):
    sub = tl["SUB"] if tr is None else [(s, e, w, t) for (s, e, w, _), t in zip(tl["SUB"], tr)]
    if tr is not None:
        text = [(a, b, t, sz, c, p) for (a, b, _, sz, c, p), t in zip(tl["TEXT"], TEXT[lang])]
        with open(os.path.join(D, f"timeline_{lang}.py"), "w") as f:
            f.write(f"# «Sovg'a yutdingiz!» {lang}: timeline.py SUB/TEXT vaqtlari, tarjima (tarjima.py yasaydi); --tl {lang}\n")
            f.write("SUB = [\n" + "".join(f" {x!r},\n" for x in sub) + "]\n")
            f.write("TEXT = [\n" + "".join(f" {x!r},\n" for x in text) + "]\n")
    with open(os.path.join(out, f"sovga-{lang}.srt"), "w") as f:
        for i, (s, e, _, t) in enumerate(sub, 1):
            f.write(f"{i}\n{ts(s)} --> {ts(e)}\n{t}\n\n")
print("ok")
