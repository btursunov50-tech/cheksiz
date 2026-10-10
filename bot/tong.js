// Daily "Xayrli tong" post for the Telegram channel (sent by api/tong.js at 05:00 Tashkent).
// Videos live in infinite/media/tong/: one per weekday (motto at the bottom) plus
// optional dated specials (YYYY-MM-DD.mp4) listed in SPECIAL. Edit tips and wishes here.

const MEDIA_URL = "https://cheksiz-one.vercel.app/infinite/media/tong/";
const CHANNEL = "@infinite_ai_and_me";

// Index = JS getUTCDay() of the Tashkent date (0 = Sunday).
const DAYS = [
  { file: "yakshanba", name: "yakshanba", wish: "Oilangiz bilan xayrli dam oling!" },
  { file: "dushanba", name: "dushanba", wish: "Yangi hafta muborak!" },
  { file: "seshanba", name: "seshanba", wish: "Kuningiz barakali o'tsin!" },
  { file: "chorshanba", name: "chorshanba", wish: "Ishlaringizga omad!" },
  { file: "payshanba", name: "payshanba", wish: "Niyatlaringiz ijobat bo'lsin!" },
  { file: "juma", name: "juma", wish: "Juma muborak!" },
  { file: "shanba", name: "shanba", wish: "Kuningiz hamisha Alloh panohida o'tsin!" },
];

const MONTHS = ["yanvar", "fevral", "mart", "aprel", "may", "iyun", "iyul", "avgust", "sentyabr", "oktyabr", "noyabr", "dekabr"];

// Dated videos that replace the weekday one (first post: motto in the center).
const SPECIAL = ["2026-10-10"];

const TIPS = [
  "ChatGPT yoki Claude'dan biror narsa so'raganda \"menga 5 yoshli bolaga tushuntirgandek tushuntir\" deb yozing. Eng qiyin mavzu ham oson bo'ladi.",
  "AI'ga savol berishdan oldin o'zingiz kim ekaningizni yozing: \"Men Toshkentda kafe egasiman...\". Javob sizga moslashadi.",
  "AI javobi yoqmasa, yangidan boshlamang: \"qisqaroq qil\", \"oddiyroq yoz\" yoki \"3 ta variant ber\" deb davom ettiring.",
  "Mijozga xabar yozishdan oldin AI'dan \"shu matnni xushmuomala va qisqa qilib ber\" deb so'rang.",
  "Telefoningizdagi rasmni AI'ga yuborib \"bu yerda nima yozilgan?\" deb so'rang. Hujjat, chek va menyularni o'qiydi.",
  "AI xato qilishi mumkin. Raqamlar, narxlar va sanalarni har doim o'zingiz tekshiring.",
  "Ijtimoiy tarmoq uchun post kerakmi? AI'ga mahsulotingizni tasvirlab \"Instagram uchun 3 xil matn yoz\" deng.",
  "Shaxsiy ma'lumotlar (parol, karta raqami, pasport) ni hech qachon AI chatga yozmang.",
  "Ovozli xabar bilan ham AI'ga savol berish mumkin. Yozishga vaqt bo'lmasa, gapiring.",
  "Biznesingiz Google Xaritada bormi? Mijozlarning ko'pchiligi joyni avval xaritadan qidiradi.",
  "AI'dan reja so'rang: \"Bu hafta do'konimga ko'proq mijoz jalb qilish uchun 5 ta oddiy qadam ber\".",
  "Chet tilida xat kerakmi? O'zbekcha yozing va AI'dan \"ruschaga/inglizchaga tarjima qil, rasmiy uslubda\" deb so'rang.",
  "QR katalog mijozga mahsulotlaringizni telefonida darhol ko'rsatadi: menyu, narx, rasm, hammasi bir joyda.",
  "AI'ga misol bering: \"mana shu postdek uslubda yangisini yoz\". Misol bilan natija ancha yaxshi chiqadi.",
  "Uzun matnni AI'ga tashlab \"eng muhim 3 ta fikrni ayt\" deng. Vaqtingiz tejaladi.",
  "Telegram bot mijozlarga kechasi ham javob beradi. Siz uxlasangiz ham savollar javobsiz qolmaydi.",
  "Yangi g'oya kerakmi? AI'dan \"10 ta g'oya ber, eng g'alatisini ham qo'sh\" deb so'rang.",
  "AI bilan ishlashda aniq bo'ling: \"yaxshi matn\" emas, \"50 so'zli, quvnoq, yoshlar uchun matn\" deng.",
  "Mahsulot rasmini yorug' joyda, oddiy fonda oling. AI fonni keyin chiroyli qilib beradi.",
  "Mijoz shikoyat qildimi? AI'dan \"xotirjam va hurmat bilan javob yoz\" deb yordam so'rang.",
  "Har kuni 10 daqiqa AI bilan biror yangi narsa sinab ko'ring. Bir oyda katta farqni sezasiz.",
  "AI'dan jadval so'rash mumkin: \"haftalik xarajatlarimni jadval qilib ber\" deng va raqamlarni yozing.",
  "Video reklama uchun avval qisqa ssenariy yozing: muammo, yechim, chaqiriq. AI bunga yordam beradi.",
  "Logotip oddiy bo'lsa yaxshi esda qoladi: 1–2 rang, bitta belgi, aniq nom.",
  "AI'dan o'zingizni tekshirtiring: \"shu matnda xato bormi? imlosini to'g'irla\".",
  "Bir xil savolni har kuni bermang: yaxshi chiqqan so'rovingizni saqlab qo'ying va qayta ishlating.",
  "Mijozlar ko'p so'raydigan 10 ta savolni yozib chiqing. Bot va sayt uchun eng kerakli ma'lumot shu.",
  "AI'ga rol bering: \"Sen tajribali sotuvchisan, mana mahsulotim, qanday sotay?\"",
  "Farzandlaringizga ham AI'dan to'g'ri foydalanishni o'rgating: savol berish, javobni tekshirish.",
  "Eng yaxshi AI ham sizning tajribangiz o'rnini bosmaydi. U yordamchi, qaror esa sizda.",
];

// Tashkent is UTC+5 all year.
function tashkentDate(now = new Date()) {
  const d = new Date(now.getTime() + 5 * 3600 * 1000);
  const iso = d.toISOString().slice(0, 10);
  return { iso, weekday: d.getUTCDay(), day: d.getUTCDate(), month: d.getUTCMonth() };
}

const BIRTHDAYS = require("./birthdays");
const CAPTION_LIMIT = 1024; // Telegram media caption limit

function buildPost(now = new Date()) {
  const t = tashkentDate(now);
  const day = DAYS[t.weekday];
  // Tip 1 on the first post day (2026-10-10), then one new tip per day in order.
  const n = Math.round((Date.parse(t.iso) - Date.parse("2026-10-10")) / 86400000);
  const tip = TIPS[((n % TIPS.length) + TIPS.length) % TIPS.length];
  const file = SPECIAL.includes(t.iso) ? t.iso : day.file;
  const born = BIRTHDAYS[t.iso.slice(5)] || [];
  const make = (people) =>
    [
      "🌸 Assalomu alaykum, Alloh suygan bandalar!",
      "",
      "🤲 Hasbunallohu va ni'mal vakil",
      "Bizga Allohning O'zi yetarlidir...",
      "",
      "☀️ Xayrli tong, aziz obunachilar!",
      `📅 Bugun ${day.name}, ${t.day}-${MONTHS[t.month]}. ${day.wish}`,
      "",
      ...(people.length
        ? ["🎂 Bugun tug'ilgan mashhurlar:", ...people.map((p) => `• ${p.flag} ${p.name} (${p.years}) — ${p.who}`), ""]
        : []),
      `💡 Kun maslahati: ${tip}`,
      "",
      "🤖 Bot: @sahiychishopbot",
      "♾️ Infinite AI & Me",
    ].join("\n");
  // Drop names from the end until the caption fits.
  let people = born;
  let caption = make(people);
  while (caption.length > CAPTION_LIMIT && people.length) caption = make((people = people.slice(0, -1)));
  return { date: t.iso, video: `${MEDIA_URL}${file}.mp4`, caption };
}

// Redis set of private chats that get the post too (joined with /start, left with /tong_off).
const SUBS_KEY = "iam:tong:subs";

// One-time clip post (owner opens /api/tong?key=<WEBHOOK_SECRET>&clip=1). Suno free plan: credit, no monetization.
const CLIP = {
  id: "yuragingni-qaytib-bermayman",
  video: "https://cheksiz-one.vercel.app/infinite/media/klip/yuragingni-qaytib-bermayman.mp4",
  caption: [
    "🎵 «Yuragingni qaytib bermayman»",
    "",
    "Infinite AI & Me'dan sizga sovg'a: sun'iy intellekt yordamida yaratilgan qo'shiq va klip. Yoqsa, do'stlaringizga ulashing! ❤️",
    "",
    "🎧 Music: made with Suno",
    "🤖 Bot: @sahiychishopbot",
    "♾️ Infinite AI & Me",
  ].join("\n"),
};

module.exports = { buildPost, CHANNEL, SUBS_KEY, CLIP, TIPS, DAYS };
