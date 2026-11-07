---
name: promptlar
description: Video loyihasi uchun rasm (ChatGPT) va video (Veo/Kling) promptlarini egasining barcha qoidalari bilan yozadi va bitta Artifact sahifaga (rasm, nima bo'ladi, kamera, prompt, «Nusxa olish») chiqaradi. Egasi rasm/video prompt so'raganda, rasmlar tasdiqlanib video bosqichiga o'tilganda yoki prompt tuzatilganda ishlating.
---

# Promptlar

Namuna loyiha: `video/qora/` (`rasm_promptlar.py`, `video_promptlar.py`). Sahifa quruvchi: `.claude/skills/promptlar/sahifa.py` (`page()`, `VEO_NEG`, `neon()`).

## Har bir promptdagi majburiy qoidalar (CLAUDE.md)
1. **Format** sarlavhada va ichida: «**4-sahna — 9:16 (tik), 8 s**» va `Vertical 9:16 image/video`.
2. **To'liq blok**: umumiy uslub matni har promptning ichida takrorlanadi; «buni boshiga qo'shing» demang.
3. **Ranglar**: kadrda 2–3 asosiy rang, nomlari bilan (Kalamushqirdan faqat ranglar).
4. **Qahramon**: to'liq tavsif (yosh, yuz shakli, soch, kiyim); Diyor bo'lsa neon chiziq batafsil (`neon()`); «Keep the character exactly as in the reference image»; qo'llar soni.
5. **Namuna**: «Attach the reference image…» deyilsa, o'sha rasm sahifada prompt yonida turadi va chatda ham yuboriladi (qaysi promptga ekani yozilib). Yuz o'zgarsa — eng yaxshi tasdiqlangan sahna rasmini ham biriktiring.
6. **Plan**: hissiy joyda close-up / push-in va yuz ifodasi batafsil (ko'z, qosh, og'iz); kuchli ifodada «not an adult, round young face», kamera ko'z darajasida.
7. **Matn yo'q**: «No text, no letters, no numbers, no logos, no watermark». Kerakli yozuv (narx, BANK) — rasmda bo'sh joy, keyin kodda yoziladi; qisqa so'z bo'lsa harfma-harf (B-A-N-K).
8. **Veo qo'shimcha**: kamera harakati bilan boshlanadi (qo'shni sahnalarda takrorlanmaydi; statik = nol harakat); rasmdagi harakatni davom ettiradi (yo'nalish qaytmaydi); qahramonlar aniq harakat qiladi; gapiruvchi personaj `X says in Uzbek: "..."` (so'zsiz rolikda: «silent film, does not speak»); muhim tushishda sekinlashuv (speed ramp); joy nomlari (bazaar, bank vault) yozuv chaqirishi mumkin — kerak bo'lmasa sirtlarni tasvirlang; alohida oxirgi qator `VEO_NEG`.
9. **Mantiq**: sahna haqiqatga mos (muzlatkichdan issiq somsa chiqmaydi, varaq g'oyib bo'lmaydi, og'izdan tutun yo'q).

## Ish tartibi
1. Loyihada `rasm_promptlar.py` / `video_promptlar.py` yozing (ro'yxat `S`, `prompt()` funksiyasi) — `sahifa.page()` bilan HTML, `.txt` bilan matn.
2. Sahifani bitta Artifact sifatida chop eting (birinchi marta `Artifact quickstart` → publish, `files` bilan `web/*.webp`); keyin har o'zgarishda **o'sha fayl yo'li** bilan qayta publish (URL o'zgarmaydi). Rasmlar tasdiqlangach sahifa video bosqichiga o'tadi: faqat tasdiqlangan rasm, nima bo'ladi, kamera, Veo prompt.
3. Chatda: image promptlar — har biri alohida kod blokida (to'liq); Veo promptlar — faqat sahifada (chatda havola va qaysi sahnalar qo'shilgani), lekin tuzatilgan bitta prompt chatda ham berilishi mumkin.
4. Commit, PR, squash-merge.
