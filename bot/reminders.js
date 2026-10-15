// Owner-only reminders sent by the bot (api/remind.js; crons at 09:00, 20:00 and 21:00 Tashkent).
// Key: Tashkent date "YYYY-MM-DD"; value: list of messages. A plain string is sent at 09:00,
// { at: 20, text } at 20:00 (only 9, 20 and 21 have crons). Old dates can be deleted.

module.exports = {
  "2026-10-11": [
    "📌 Eslatma: bugun 5-video («100 o'zbekistonlikdan 7 tasi AI ishlatadi») ni joylang!\n\n" +
      "1) Telegram kanal: 1-telegram-7foiz-uz.mp4\n" +
      "2) YouTube: 2-youtube-linkedin-7foiz-en.mp4 + uz/ru .srt\n" +
      "3) Instagram va Facebook: 3-instagram-facebook-7foiz-ru.mp4\n" +
      "4) LinkedIn: 2-youtube-linkedin-7foiz-en.mp4\n\n" +
      "Matnlarni Claude'dan so'rang, havolalarni unga yuboring ✅",
    {
      at: 20,
      text:
        "🎵 Eslatma: klipni joylash vaqti! «Yuragingni qaytib bermayman»\n\n" +
        "1) YouTube (to'liq): 1-youtube-toliq-16x9-en.mp4 + klip-uz.srt, klip-ru.srt, monetizatsiya o'chiq\n" +
        "2) YouTube Shorts: 2-shorts-telegram-uz.mp4, «Связанное видео» = to'liq klip\n" +
        "3) Instagram va Facebook: 3-instagram-facebook-ru.mp4\n" +
        "4) LinkedIn: 4-linkedin-en.mp4\n\n" +
        "Har bir postda: «Music: made with Suno». Matnlar Claude'dagi xabarda ✅",
    },
    {
      at: 21,
      text:
        "⏰ Klip joylandimi? Hozir (21:00–22:00) odamlar eng faol vaqt.\n\n" +
        "Joylagan bo'lsangiz, havolalarni Claude'ga yuboring: u PUBLISHED.md ga yozib qo'yadi ✅",
    },
  ],
  "2026-10-12": [
    "📌 Eslatma: bugun «Toshkent 2036» videosini joylang!\n\n" +
      "1) Telegram kanal: 1-telegram-toshkent2036-uz.mp4\n" +
      "2) YouTube Shorts: 2-youtube-linkedin-toshkent2036-en.mp4 + toshkent2036-uz.srt, toshkent2036-ru.srt\n" +
      "3) Instagram va Facebook: 3-instagram-facebook-toshkent2036-ru.mp4\n" +
      "4) LinkedIn: 2-youtube-linkedin-toshkent2036-en.mp4\n\n" +
      "Har bir postda: «Music: Duty Calls – Rod Kim». Matnlar Claude'dagi xabarda ✅\n" +
      "Keyingi video: «Dadamga AI o'rgatdim» — Claude'ga «5-g'oyani boshlaymiz» deb yozing.",
    {
      at: 20,
      text:
        "🎵 Eslatma: bugun kechqurun «Yuragingni qaytib bermayman» klipini joylang!\n\n" +
        "1) YouTube (to'liq): 1-youtube-toliq-16x9-en.mp4 + klip-uz.srt, klip-ru.srt, monetizatsiya o'chiq\n" +
        "2) YouTube Shorts: 2-shorts-telegram-uz.mp4\n" +
        "3) Instagram va Facebook: 3-instagram-facebook-ru.mp4\n" +
        "4) LinkedIn: 4-linkedin-en.mp4\n\n" +
        "Har bir postda: «Music: made with Suno». Matnlar Claude'dagi xabarda ✅",
    },
    {
      at: 21,
      text: "⏰ Klip joylandimi? Havolalarni Claude'ga yuboring ✅",
    },
  ],
  "2026-10-13": [
    "📌 Eslatma: bugun «Kalamushqir» videosini joylang!\n\n" +
      "1) Telegram kanal: 1-telegram-kalamushqir-uz.mp4\n" +
      "2) YouTube Shorts: 2-youtube-linkedin-kalamushqir-en.mp4 + kalamushqir-uz.srt, kalamushqir-ru.srt\n" +
      "3) Instagram va Facebook: 3-instagram-facebook-kalamushqir-ru.mp4\n" +
      "4) LinkedIn: 2-youtube-linkedin-kalamushqir-en.mp4\n\n" +
      "Har bir postda: «Music: The Road To Mordor, Frodo's Quest – Ezra Lipp». Matnlarni Claude'dan so'rang (\"Kalamushqir matnlari\"), havolalarni unga yuboring ✅",
  ],
  "2026-10-14": [
    "📌 Eslatma: bugun «Dadamga AI o'rgatdim» videosini joylang!\n\n" +
      "1) Telegram kanal: 1-telegram-dadam-uz.mp4\n" +
      "2) YouTube Shorts: 2-youtube-linkedin-dadam-en.mp4 + dadam-uz.srt, dadam-ru.srt\n" +
      "3) Instagram va Facebook: 3-instagram-facebook-dadam-ru.mp4\n" +
      "4) LinkedIn: 2-youtube-linkedin-dadam-en.mp4\n\n" +
      "Har bir postda: «Music: Dutar's Whisper». Matnlarni Claude'dan so'rang (\"Dadam matnlari\"), havolalarni unga yuboring ✅",
  ],
  "2026-10-15": [
    "📌 Eslatma: bugun «Manus» videosini joylang!\n\n" +
      "1) Telegram kanal: 1-telegram-manus-uz.mp4\n" +
      "2) YouTube Shorts: 2-youtube-linkedin-manus-en.mp4 + manus-uz.srt, manus-ru.srt\n" +
      "3) Instagram va Facebook: 3-instagram-facebook-manus-ru.mp4\n" +
      "4) LinkedIn: 2-youtube-linkedin-manus-en.mp4\n\n" +
      "Har bir postda: «Music: Duty Calls – Rod Kim» va https://manus.im havolasi. Matnlarni Claude'dan so'rang (\"Manus matnlari\"), havolalarni unga yuboring ✅",
  ],
  "2026-10-16": [
    "📌 Eslatma: bugun «Nusxa» videosini joylang!\n\n" +
      "1) Telegram kanal: 1-telegram-nusxa-uz.mp4\n" +
      "2) YouTube Shorts: 2-youtube-linkedin-nusxa-en.mp4 + nusxa-uz.srt, nusxa-ru.srt\n" +
      "3) Instagram va Facebook: 3-instagram-facebook-nusxa-ru.mp4\n" +
      "4) LinkedIn: 2-youtube-linkedin-nusxa-en.mp4\n\n" +
      "Musiqa: YouTube/LinkedIn – «The Road To Mordor – Ezra Lipp, Piano Dreams – Michael Yanis»; Telegram/Instagram/Facebook – «Piano Dreams – Michael Yanis, Vodiy Yulduzlari – Tohir Mahkamov». Matnlarni Claude'dan so'rang (\"Nusxa matnlari\"), havolalarni unga yuboring ✅",
    {
      at: 20,
      text:
        "🌯 Eslatma: «Lavash AI» sinovi!\n\n" +
        "Uyda kamerada (yoki telefonda) lavash tayyorlanishini tepadan 10–15 daqiqa video oling: stol ustida, yorug' joyda, bir nechta lavash.\n" +
        "Lavash menyusini (retsept va ingredientlar ro'yxati) ham yozing.\n\n" +
        "Ikkalasini Claude'ga yuboring: u AI ingredientlarni ajrata oladimi, tekshiradi ✅",
    },
    {
      at: 12,
      text:
        "🤖 Eslatma: «Robot bilan bir piyola choy» videosi!\n\n" +
        "ChatGPT'da 22 ta rasm promptidan avval 1-rasmni (robot) qiling va Claude'ga yuboring. Yoqsa, qolganlarini shu suhbatda davom ettiring.\n" +
        "Promptlar: Claude'dan \"Robot promptlari\" deb so'rang ✅",
    },
  ],
  "2026-10-17": [
    "📌 Eslatma: bugun «Aytilmagan gaplar» videosini joylang!\n\n" +
      "1) Telegram kanal: 1-telegram-aytilmagan-uz.mp4\n" +
      "2) YouTube Shorts: 2-youtube-linkedin-aytilmagan-en.mp4 + aytilmagan-uz.srt, aytilmagan-ru.srt\n" +
      "3) Instagram va Facebook: 3-instagram-facebook-aytilmagan-ru.mp4\n" +
      "4) LinkedIn: 2-youtube-linkedin-aytilmagan-en.mp4\n\n" +
      "Musiqa: Reviver – The Grey Room / Density & Time, Cutscene Crush – Blue Deer Studio. Matnlarni Claude'dan so'rang (\"Aytilmagan matnlari\"), havolalarni unga yuboring ✅",
  ],
};
