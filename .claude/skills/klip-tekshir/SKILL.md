---
name: klip-tekshir
description: Egasi yuborgan AI video klipini (Veo, Vidu, Dreamina, Hailuo, Kling) tekshiradi va tozalaydi — suv belgisini kesadi, qora/qotgan kadrni topadi, manba rasm va namunalar (img/ref_*) bilan yonma-yon varaq chiqaradi, natijani jadval qilib beradi. Egasi video klip yuborganda yoki "/klip-tekshir" deganda ishlating.
---

# Klip tekshirish

Egasining qoidasi (CLAUDE.md, 2026-10-17): har bir klipni boshi, o'rtasi, oxiri bo'yicha manba rasm va `img/ref_*` bilan solishtir; qahramon o'zgarsa — bu asosiy xato; qaysi vosita (rasm yoki video) xato qilganini ayt.

## Qadamlar
1. Klipni scratchpad'ga nusxalang, sahna raqamini aniqlang (fayl nomidagi prompt yoki egasining gapi bo'yicha).
2. Ishga tushiring:
   ```
   python3 .claude/skills/klip-tekshir/tekshir.py KLIP.mp4 --name sNN --out video/<loyiha>/clips \
     --src video/<loyiha>/img/NN_*.jpg --ref video/<loyiha>/img/ref_robot.jpg --ref video/<loyiha>/img/ref_odam.jpg \
     --sheet <scratchpad>/sNN_sheet.jpg
   ```
   Vosita o'lcham bo'yicha aniqlanadi va belgisi avtomatik kesiladi (Vidu 540×958, Dreamina 704×1248, Hailuo 768×1344; Veo 720×1280 — belgisiz). Noma'lum o'lchamda `--crop w:h:x:y` bering.
3. Varaqni **Read** bilan oching va ko'z bilan tekshiring:
   - har bir qahramon namunaga mosmi (yuz, soch, soqol, kiyim; robot: og'iz yo'q, ko'z yoylari, ∞, do'ppi, quloq halqalari);
   - klip oxirigacha o'zgarmayaptimi (robot burilib ko'zi buzilishi, yuz o'zgarishi);
   - ortiqcha yozuv, o'qiladigan harf, begona narsa, qo'shimcha odam;
   - shubhali joyni `ffmpeg -ss T ... crop=` bilan yaqinlashtirib qarang.
4. Xato faqat klipning bir qismida bo'lsa — yaxshi qismini oling (`timeline.py` dagi `START`) va egasiga ayting.
5. Egasiga jadval: nima to'g'ri, nima xato, kim xato qildi, nima tuzatildi, sahna uzunligi va klip qanchaga sekinlashadi. Keyin `README.md` ga qayd, commit, PR, squash-merge.
