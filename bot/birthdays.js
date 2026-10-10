// "Bugun tug'ilgan mashhurlar" for the morning post (bot/tong.js), keyed "MM-DD".
// Order: Uzbek first, then world names; living people before the deceased.
// Only add a name after checking the birth date in at least two sources:
// a wrong birthday in a public post is worse than a missing one. Keep "who" short
// (Telegram media captions are limited to 1024 characters).
// years: "1942" for living people, "1937–2023" for the deceased.

module.exports = {
  "10-11": [
    { flag: "🇮🇳", name: "Amitabh Bachchan", years: "1942", who: "hind kinosining afsonaviy aktyori, 200 dan ortiq filmda suratga tushgan" },
    { flag: "🇬🇧", name: "Bobby Charlton", years: "1937–2023", who: "Angliya futbol afsonasi, 1966-yilgi jahon chempioni" },
    { flag: "🇺🇸", name: "Eleanor Roosevelt", years: "1884–1962", who: "AQSh birinchi xonimi, Inson huquqlari umumjahon deklaratsiyasi mualliflaridan" },
  ],
};
