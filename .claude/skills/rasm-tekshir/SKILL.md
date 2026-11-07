---
name: rasm-tekshir
description: Egasi yuborgan AI rasmlarni (ChatGPT, Gemini va boshqalar) javob berishdan OLDIN tekshiradi — har bir qahramon yuzini namuna (img/ref_*) va oldin tasdiqlangan sahnalar bilan yonma-yon solishtiradi, boshqa qahramonlar bilan bir xil yuz emasligini, soxta yozuv/suv belgisi/ortiqcha qo'l-buyumni, format (9:16), takror faylni tekshiradi, jadval beradi va tasdiqlanganini img/ ga saqlaydi. Egasi rasm yuborganda HAR GAL, so'ramasa ham ishlating.
---

# Rasm tekshirish

Egasining qoidalari (CLAUDE.md, 2026-10-17 va 2026-10-22): rasm haqida biror narsa deyishdan oldin yuzlarni kesib, namuna va boshqa qahramonlar bilan yonma-yon solishtir; qahramon o'zgarishi — asosiy xato; maqtashdan oldin tekshir.

## Qadamlar
1. Rasmlar chatdan `…/images/N.webp` bo'lib keladi (eng kattasi oxirgi raqamlar). Har biri qaysi sahnaga tegishli ekanini aniqlang (egasining gapi yoki rasm mazmuni).
2. Rasmga bir qarab, yuz sohasini nisbiy koordinata bilan belgilang va varaq yasang:
   ```
   python3 .claude/skills/rasm-tekshir/tekshir.py IMG1 IMG2 --ref video/<loyiha>/img/ref_<qahramon>.png \
     --ref video/<loyiha>/img/<eng yaxshi tasdiqlangan sahna>.png --box N=0.3,0.2,0.7,0.5 \
     --refbox ref_<qahramon>=0.42,0.08,0.75,0.3 --known video/<loyiha>/img --sheet <scratchpad>/tekshir.jpg
   ```
   Jadvaldagi «Takror» ustuni egasi eski faylni qayta yuborganini ko'rsatadi (ayting).
3. Varaqni **Read** bilan oching. Har rasm uchun:
   - yuz: yoshi (katta odamga aylanmadimi), shakli, soch (to'g'ri/jingalak), sepkil, ko'z; boshqa qahramonnikiga o'xshab qolmadimi;
   - kiyim, ranglar, maxsus belgilar (Diyor: to'q ko'k kapyushon, ryukzak, ingichka moviy neon chiziq);
   - mantiq: sahnaga mosmi (muzlatkichda issiq somsa bo'lmaydi), qo'llar soni, barmoqlar;
   - yozuv, suv belgisi, logotip, soxta harflar (kerak bo'lsa `crop` bilan yaqinlashtiring), bayroq;
   - format: 9:16 (yoki loyihada kelishilgani).
4. Javob: jadval (Sahna | Natija ✅/⚠️/❌ | Yuz | Boshqa | Xulosa). Nima xato va kim xato qildi (rasm vositasi) aniq ayting. Maqtov — faqat tekshiruvdan keyin.
5. Tasdiqlanganini saqlang: `python3 .claude/skills/rasm-tekshir/saqla.py IMG video/<loyiha> s07` (yuz faqat fonda bo'lsa va boshqacha chiqsa: `--blur x1,y1,x2,y2` — chuqurlik effekti, 3-sahna «Qora kvadrat» namunasi). Zaxira variantlarni `sNN_v2` deb saqlang.
6. Xato bo'lsa: promptni tuzating (yosh/dumaloq yuz, tasdiqlangan sahna rasmini qo'shimcha biriktirish, kamera ko'z darajasida, yuzga pastdan yorug'lik tushmasin) — `/promptlar` skill'i bilan sahifani yangilang va tuzatilgan promptni chatda kod blokida bering; biriktiriladigan rasmlarni chatda yuboring.
7. Loyiha README/SSENARIY ga «Tasdiqlangan rasmlar» qatorini yangilang, commit, PR, squash-merge.

## Saboqlar («Qora kvadrat», 2026-11-06)
- Gemini Diyorni boshqa uslubda chizadi — seriyada ChatGPT ishlating.
- Kuchli ifoda (ochko'zlik, qo'rquv) va pastdan qizil yorug'lik yuzni katta odamga aylantiradi: «NOT an adult man, round boyish face» + 1 va 4-sahna rasmlarini biriktirish yordam berdi.
- Promptda «yuz xira» desa ham AI tiniq chizishi mumkin — kodda xiralashtirish (saqla.py --blur) yetarli.
- Narx kabi yozuvlarni AI'ga yozdirmang: bo'sh joy qoldirib, PIL bilan perspektiva bo'yicha yozing (video/qora/img/s01_narx.png).
