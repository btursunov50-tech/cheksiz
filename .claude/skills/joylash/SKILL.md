---
name: joylash
description: Tayyor videoni ijtimoiy tarmoqlarga joylash uchun egasiga to'liq qo'llanma va barcha post matnlarini (Telegram uz, YouTube sarlavha + tavsif, Instagram/Facebook ru, LinkedIn en) uning tasdiqlangan formatida tayyorlaydi, fayllarni yuboradi va PUBLISHED.md ni yangilaydi. Video tayyor bo'lganda yoki egasi «joylash», «post matni», «qanday joylayman» deganda ishlating.
---

# Joylash qo'llanmasi

Namuna: `video/oyiga/POSTS.md`, tartib va matn oxiri: `video/PUBLISHED.md` («Joylash tartibi», «Matn oxiri»).

## Fayllar (har video uchun, `video/final/<loyiha>/`)
| Fayl | Qayerga | Subtitr |
|---|---|---|
| `1-telegram-<nom>-uz.mp4` | Telegram kanal https://t.me/infinite_ai_and_me | o'zbekcha kuydirilgan |
| `2-youtube-linkedin-<nom>-en.mp4` | YouTube + LinkedIn | inglizcha kuydirilgan; YouTube'ga uz/ru `.srt` |
| `3-instagram-facebook-<nom>-ru.mp4` | Instagram (Facebook'ga Instagram'dan ulashiladi) | ruscha kuydirilgan |
| `<nom>-uz.srt`, `<nom>-ru.srt`, `<nom>-en.srt` | YouTube subtitrlari | — |
Har fayl < 30 MB (chatga yuborish chegarasi). Yuborishda caption faqat «platforma + fayl nomi».

## Javob tuzilishi (egasi tasdiqlagan «Nusxa» formati)
Bitta xabarda, platformalar ketma-ketligi bilan; har birida sarlavha + havola, fayl nomi, qisqa qadamlar, so'ng **har bir matn alohida kod blokida**:
1. **Telegram** — https://t.me/infinite_ai_and_me — uz matn.
2. **YouTube** — https://studio.youtube.com — sarlavha (alohida blok; hook `python3 .claude/skills/ig-reel/hookscore.py` bilan baholanadi), tavsif (alohida blok). Qadamlar: til = o'zbek, joy = Toshkent, «не для детей», subtitrlar `.srt` (uz, ru, en), **«Altered or synthetic content» = Yes**. Sarlavha/tavsifda `<` `>` YO'Q (menyu yo'li → bilan).
3. **Instagram** — https://www.instagram.com — ru matn; kesishda «Оригинал»; joy Ташкент; **«AI info / Метка ИИ»** yoqiladi.
4. **Facebook** — faqat: «Instagram'da 'Facebook'ga ham ulashish'ni yoqing» (alohida yuklamaymiz).
5. **LinkedIn** — https://www.linkedin.com/feed/ — en matn, «AI bilan qanday yasadim» uslubi, egasining yoshi/shaxsiy ma'lumoti yo'q.
Oldingi xabarlarga havola qilmang — barcha matn shu xabarda.

## Har matnda
- Video mavzusiga mos bot chaqirig'i (@sahiychishopbot nima qila olishi — faqat `bot/knowledge.js` da bor narsa).
- Boshqa joyga ishora bo'lsa, haqiqiy havola (youtu.be/…).
- Musiqa: Suno bepul bo'lsa «🎵 Music: made with Suno» (monetizatsiya yo'q); egasining o'z treki bo'lsa nomi.
- Oxirida AI qatori: uz «Video sun'iy intellekt yordamida yaratilgan. Qahramonlar o'ylab topilgan, haqiqiy shaxslarga o'xshashlik tasodifiy.» / ru «Видео создано с помощью искусственного интеллекта. Персонажи вымышлены, любое сходство с реальными людьми случайно.» / en «Made with AI. The characters are fictional; any resemblance to real people is coincidental.»
- «для развлечения», «no copyright intended» kabi gaplarni yozmang (himoya qilmaydi). Begona kadr bo'lsa, xavfni oldindan ayting.
- Matnni `/ig-human` qoidalari bilan tozalang (em-dash, «AI so'zlari»).

## Keyin
`video/<loyiha>/POSTS.md` ga matnlar; egasi havolalarni yuborgach `video/PUBLISHED.md` ga qator va `video/final/<loyiha>/` ni o'chirish; commit, PR, squash-merge.
