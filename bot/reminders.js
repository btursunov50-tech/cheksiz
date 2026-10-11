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
};
