# «Sovg'a yutdingiz!» — kuchaytirilgan ssenariy (2026-10-24)

Asos: `ideas/diyor-usta.md`, 6-ssenariy. Format: tik 9:16, ~75 s, mini-drama. Qahramonlar: **Diyor** (yigit) va **Usta** (keksa, sokin, ko'p ko'rgan). Ikkalasi o'ylab topilgan.

O'zgarishlar (asl matnga nisbatan):
- Hook boshida: oxirgi soniyadan boshlanadi (Usta qo'lni ushlaydi), keyin «5 daqiqa oldin». EN hook ball **84.2** (asl birinchi qator 35.4).
- Zidlik tuzatildi: avval Telegram xabar keladi, keyin «bank xodimi» qo'ng'iroq qiladi.
- Asosiy burilish: kod sovg'aniki emas, **Telegram'ga kirish kodi** ekan. SMSda «bu kodni hech kimga bermang» deb yozilgan.
- «Agar bergan bo'lsa» sahnasi: akkaunt egallanadi, onasiga Diyor nomidan pul so'rab xabar boradi («Nusxa» bilan bog'lanadi).
- Oxirida aniq foyda: 3 belgi + bulutli parol (ikki bosqichli tekshiruv). Taymer 0:00 ga yetadi, hech narsa bo'lmaydi.
- Bot faqat yakuniy kartada. Raqamlar (2 mln, 5 daqiqa) misol, fakt emas.

## Sahnalar

| # | Vaqt | Nima ko'rinadi | Gap |
|---|---|---|---|
| 1 | 0–4 s | Diyorning barmog'i telefonda kodni aytmoqchi, Usta qo'lini ushlaydi | **Usta:** «To'xta! "Siz yutdingiz" degan notanishga SMS kodni hech qachon o'qib berma.» |
| 2 | 4–10 s | «5 daqiqa oldin». Telegram xabar: «Tabriklaymiz! Siz iPhone yutdingiz. 5 daqiqa ichida tasdiqlang», taymer 4:59 | **Diyor:** «Voy! iPhone yutibman! Faqat besh daqiqa vaqt bor ekan.» |
| 3 | 10–18 s | Qo'ng'iroq: «Bank xodimi». Diyor quloq soladi, SMS keladi | **Ovoz (telefonda):** «Sizga kod keldi. Shuni ayting, sovg'angizni rasmiylashtiramiz.» **Diyor:** «Hozir, hozir…» |
| 4 | 18–24 s | Usta (1-sahnaning davomi) | **Usta:** «Kodni aytishdan oldin, SMSni menga ovoz chiqarib o'qi.» |
| 5 | 24–31 s | SMS yaqin planda. So'zlar birma-bir yonadi. Sekinlashuv: barmoq «Yuborish» ustida to'xtaydi | **Diyor:** «Telegram kodi… "Bu kodni hech kimga bermang"…» (jimlik) |
| 6 | 31–38 s | Usta yonida o'tiradi | **Usta:** «Bu sovg'a kodi emas. Bu sening Telegram'ingning kaliti. Kalitni bersang, eshikni o'zing ochib berasan.» |
| 7 | 38–50 s | «Agar bergan bo'lsa…» (sovuq ko'k rang): Diyorning akkaunti boshqa telefonda ochiladi. Onasiga xabar: «Onajon, tezda 2 million tashlab yuboring, keyin tushuntiraman». Ona karta raqamini yozishni boshlaydi | **Usta (ortda):** «Ular sovg'a bermaydi. Sening nomingdan yaqinlaringdan pul so'rashadi.» |
| 8 | 50–60 s | Qaytamiz. Ekranda 3 belgi birma-bir chiqadi: ❌ tanlovda qatnashmagansan · ⏱ shoshiltirishyapti · 🔑 kod so'rashyapti | **Usta:** «Uchta belgi: tanlovda qatnashmagansan. Shoshiltirishyapti. Kod so'rashyapti. Uchalasi bo'lsa — bu tuzoq.» |
| 9 | 60–68 s | Diyor qo'ng'iroqni o'chiradi, sozlamalarda bulutli parolni yoqadi | **Usta:** «Go'shakni qo'y. Bankka o'zing rasmiy raqamdan qo'ng'iroq qil. Telegram'da bulutli parolni yoq: kodni bilib olishsa ham, kira olmaydi.» |
| 10 | 68–72 s | Taymer 0:00 ga yetadi. Hech narsa bo'lmaydi. Diyor jilmayadi | **Diyor:** «Besh daqiqa tugadi. Men esa hech narsa yo'qotmadim.» |
| 11 | 72–75 s | Usta kameraga qaraydi | **Usta:** «Haqiqiy sovg'a senga hech qachon kod so'ratmaydi.» |
| — | +3 s | Avatar, plashka: «Sizga ham shunaqa xabar kelganmi? Izohga yozing!» | — |
| — | +4 s | Yakuniy karta (OBUNA BO'LING, bot, sayt, @Boxo_xxxx) | — |

Sekinlashuv (qoida: 1–2 marta): 5-sahnada barmoq «Yuborish» ustida to'xtaganda; 10-sahnada taymer 0:00 ga tushganda «chirq» ovozi.

## Hook variantlari (EN tarjima balli, `hookscore.py`)
| Hook | Ball |
|---|---|
| «To'xta! "Siz yutdingiz" degan notanishga SMS kodni hech qachon o'qib berma.» (Stop. Never read this SMS code to a stranger who says you won.) | **84.2** ✅ |
| «SMS kodni ovoz chiqarib o'qima. Bu sovg'a emas.» | 54.6 |
| «Bitta kod. Besh daqiqa. Onam notanishga pul yuborishiga sal qoldi.» | 52.0 |
| Asl: «Siz sovg'a yutdingiz! SMS kodni ayting.» | 35.4 |

## Tekshirilgan faktlar
- Telegram kirish kodi xabarida «kodni hech kimga bermang» degan ogohlantirish bo'ladi; ekranda aniq so'zlar emas, umumiy ma'no ko'rsatiladi.
- Telegram'da bulutli parol bor: Sozlamalar → Maxfiylik va xavfsizlik → Ikki bosqichli tekshiruv. Yoqilgan bo'lsa, faqat SMS kod bilan akkauntga kirib bo'lmaydi.
- Banklar SMS kodni telefonda so'ramaydi: umumiy xavfsizlik qoidasi, raqam aytilmaydi.

Holat: 📝 ssenariy egasiga berildi. Ovoz bloki va rasm promptlari egasi so'raganda.
