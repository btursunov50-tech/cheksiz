---
name: tong-mavsum
description: Telegram kanaldagi har kungi 05:00 «Xayrli tong» postining 7 ta hafta kuni videosini yangi mavsum yoki mavzuga o'tkazadi (rasmlar → animatsiya, barglar/yomg'ir/gullar, ovoz, yozuvlar), tekshiradi, saytga qo'yadi va Telegram keshini yangilaydi. Egasi ertalabki post rasmlari, mavsum (qish, bahor), tilak yoki ovozni o'zgartirishni so'raganda ishlating.
---

# Ertalabki post mavsumi

Kod: `bot/tong.js` (kunlar, tilaklar, caption HTML: salom va «kun, sana» qalin; `MEDIA_VER`), `api/tong.js` (`sendVideo`, ovoz uchun), videolar `infinite/media/tong/<kun>.mp4`.
Shablon: `video/tong/anim.html` (gullar: `all.sh`; rasm fon: `bg=`, `kuz=1` zarang barglari, jigarrang ham, `rain=1`, `place=`), `frames.js` (`DUR` muhit o'zgaruvchisi), kuz to'plami: `video/tong/all_kuz.sh`, `video/tong/KUZ.md`, ovoz `video/tong/audio/nashid.m4a`.

## Qadamlar
1. Mavzu va joylarni kelishing (7 kun; tarixi yomon joy/shaxs bo'lmasin — masalan Xudoyorxon o'rdasi o'rniga Qo'qon Jome masjidi). Egasiga ChatGPT uchun 7 ta to'liq 1:1 prompt bering (joy, mavsum, ranglar, tepa chorak bo'sh osmon, pastki beshdan bir bo'sh yo'lak, «no text»).
2. Rasmlar kelganda `/rasm-tekshir` (haqiqiy obidaga o'xshashi, soxta yozuv, o'lcham; enli bo'lsa 1:1 qayta so'rang yoki o'rtaga qo'yib, tepani osmon rangi bilan to'ldiring). Kichik (414 px) bo'lsa LANCZOS + UnsharpMask bilan 1080 ga.
3. `video/tong/<mavsum>/<nom>.jpg` ga saqlang, `all_<mavsum>.sh` yozing (`all_kuz.sh` namunasi: kun, tilak, joy, yomg'ir ustuni). Uzun tilak avtomatik 2 qatorga o'tadi; tilak bo'sh bo'lsa joy bilan bir qatorda.
4. Render: `OUT=<scratchpad>/out bash all_<mavsum>.sh`; har videoni tekshiring: davomiylik, `freezedetect`/`blackdetect`, 2–3 kadrga Read bilan qarang (yozuv chetdan chiqmasin, haykal/yuz ustiga tushmasin). Egasiga namunalarni yuboring.
5. `infinite/media/tong/` ga ko'chiring va **`bot/tong.js` dagi `MEDIA_VER` ni o'zgartiring** (Telegram faylni URL bo'yicha keshlaydi; aks holda eski video chiqishi mumkin).
6. Ovoz: azon ishlatilmaydi (bomdoddan oldin chalg'itadi); nashid yoki tabiat ovozi, past (−24 LUFS), boshlanish misra boshida, oxiri nafas joyida (energiya bo'yicha 50 ms aniqlikda toping, egasidan eshitib tasdiqlashni so'rang).
7. Commit, PR, squash-merge; Vercel'da production deploy «READY» ekanini tekshiring (`mcp__Vercel__list_deployments`, team `team_gKsvvjTQJ0vX4ZGtl5l6rrZH`, project `cheksiz`). Postni o'zim ko'ra olmayman — egasidan ertangi postni ko'rishni so'rang (https://t.me/infinite_ai_and_me). Ish jurnali bepul tarifda faqat 1 soat saqlanadi.
