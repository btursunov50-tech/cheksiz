# Voice: owner's WAV, 55.5 s, silencedetect -40 dB.
SEG=[(0,4.23),(5.27,7.43),(8.35,9.50),(10.47,11.93),(12.32,13.33),(14.20,15.39),(15.76,20.32),(21.21,23.89),(24.80,27.72),(28.71,31.27),(32.36,37.87),(38.95,44.00),(45.07,45.61),(46.03,47.15),(48.11,50.63),(51.54,53.58),(53.97,55.52)]
UZ=["Meta bu AI uchun|*2 milliard dollar* taklif qilgan.","Siz uni *bepul*|sinab ko'rishingiz mumkin.","Bu *Manus*.","U oddiy chatbot emas,","*AI agent*.","Siz vazifa berasiz,","u o'zi brauzer ochadi,|ma'lumot qidiradi|va ishni *oxiriga* yetkazadi:","hisobot, taqdimot,|hatto *sayt*.","O'tgan yil dekabrda|Meta uni *sotib olmoqchi* bo'ldi.","Lekin aprelda Xitoy|bu bitimni *to'xtatdi*.","Manus mustaqil qoldi|va shu oktabrda|*yarim milliard dollardan* ortiq|sarmoya oldi.","Bepul tarifda|har kuni *kredit* beriladi,|lekin murakkab vazifa|ularni tez tugatadi.","*Maslahat*:","kichik vazifadan boshlang.","Masalan, raqobatchilaringiz|*ro'yxatini* tuzdiring.","Kelajakda AI bilan|gaplashmaymiz,","unga *ish topshiramiz*."]
GR=[(0,0),(1,1),(2,4),(5,7),(8,8),(9,9),(10,10),(11,11),(12,14),(15,16)]
RU=["Meta предлагала за этот ИИ *2 миллиарда долларов*.","А вы можете попробовать его *бесплатно*.","Это *Manus*. Не обычный чат-бот, а *ИИ-агент*.","Вы даёте задачу, он сам открывает браузер, ищет данные и доводит работу до конца: отчёт, презентация, даже *сайт*.","В декабре прошлого года Meta хотела его *купить*.","Но в апреле Китай *остановил* сделку.","Manus остался независимым и в октябре привлёк *более полумиллиарда долларов*.","На бесплатном тарифе каждый день дают *кредиты*, но сложная задача быстро их тратит.","*Совет*: начните с маленькой задачи. Например, составьте список конкурентов.","В будущем мы не будем болтать с ИИ, мы будем *давать ему работу*."]
EN=["Meta offered *2 billion dollars* for this AI.","And you can try it *for free*.","This is *Manus*. Not a regular chatbot, an *AI agent*.","You give it a task, it opens a browser, finds the information and finishes the job: a report, slides, even a *website*.","Last December, Meta tried to *buy* it.","But in April, China *blocked* the deal.","Manus stayed independent and this October raised *over half a billion dollars*.","The free plan gives you *credits* every day, but a complex task burns through them fast.","*Tip*: start with a small task. For example, have it list your competitors.","In the future we won't chat with AI. We'll *give it work*."]
AVQ={'uz':["Siz-chi?","Manus'ga qanday vazifa berardingiz?","Izohga yozing!"],'ru':["А вы?","Какую задачу вы бы дали Manus?","Напишите в комментариях!"],'en':["What about you?","What task would you give Manus?","Tell us in the comments!"]}
CUTS=[7.9,14.0,24.3,32.0,38.6,44.7,51.2]
MAIN=56.3
# On-screen labels per language
LB={
 'uz':dict(g1a="xabarlarga ko'ra",g1b="BEPUL sinab ko'ring",agent=["chatbot","AI AGENT"],task="Vazifa beraman → Manus o'zi bajaradi",out="Hisobot • Taqdimot • Sayt",
           d1=("2025 · DEKABR","Meta Manus'ni sotib olishga kelishdi"),d2=("2026 · APREL","Xitoy bitimni to'xtatdi"),
           o1="2026 · OKTABR",o2="sarmoya",o3="Manus endi mustaqil",o4="baho ~$4 mlrd (xabarlarga ko'ra)",
           cred="Bepul tarif: har kuni kredit",cred2="Bitta vazifa ham kredit sarflaydi",tip="Maslahat: kichik vazifadan boshlang",end=["AI bilan gaplashmaymiz","unga ISH TOPSHIRAMIZ"]),
 'ru':dict(g1a="по сообщениям СМИ",g1b="Попробуйте БЕСПЛАТНО",agent=["чат-бот","ИИ-АГЕНТ"],task="Даю задачу → Manus делает сам",out="Отчёт • Презентация • Сайт",
           d1=("2025 · ДЕКАБРЬ","Meta договорилась купить Manus"),d2=("2026 · АПРЕЛЬ","Китай остановил сделку"),
           o1="2026 · ОКТЯБРЬ",o2="инвестиций",o3="Manus теперь независим",o4="оценка ~$4 млрд (по сообщениям)",
           cred="Бесплатный тариф: кредиты каждый день",cred2="Даже одна задача тратит кредиты",tip="Совет: начните с маленькой задачи",end=["Не болтать с ИИ","а ДАВАТЬ ЕМУ РАБОТУ"]),
 'en':dict(g1a="as reported",g1b="Try it FREE",agent=["chatbot","AI AGENT"],task="I give a task → Manus does it",out="Reports • Slides • Websites",
           d1=("DECEMBER 2025","Meta agreed to buy Manus"),d2=("APRIL 2026","China blocked the deal"),
           o1="OCTOBER 2026",o2="raised",o3="Manus is independent now",o4="valued at ~$4B (as reported)",
           cred="Free plan: daily credits",cred2="Even one task uses credits",tip="Tip: start with a small task",end=["Don't just chat with AI","GIVE IT WORK"]),
}
