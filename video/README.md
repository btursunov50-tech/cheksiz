# Video (Shorts / Reels) yasash

Birinchi marta MrBeast Toshkent videosi (2026-10-07) uchun ishlatilgan. Vertikal 1080×1920, 30 fps.

## Fayllar
| Fayl | Nima |
|---|---|
| `template.html` | Sahnalar, matnlar, subtitrlar va animatsiya. `data-s`/`data-e` = sahna boshi/oxiri (soniya), `data-d` = sahna ichidagi kechikish |
| `render.js` | HTML'ni kadrlarga aylantiradi (Playwright + Chromium) |
| `mark.png` | Oltin ∞ logotip (shaffof fon), `infinite/media/infinity.jpg` dan kesilgan |
| `card.png` | **Repoda yo'q.** Skrinshot sahnasi uchun o'z rasmingiz (shaxsiy ma'lumotni xiralashtiring) |

## Qadamlar
1. Matnni yozing → egasi AI ovozda o'qitadi (bu muhitda o'zbekcha TTS yo'q) va `.wav` yuboradi.
2. **Har bir gap qaysi soniyada boshlanishini aniqlang.** Claude ovozni eshita olmaydi. Eng yaxshisi: har bir gapni alohida fayl qilish. Bo'lmasa: jimliklar (RMS < -42 dB) va bo'g'inlar sonini solishtirish (250–1200 Hz energiya cho'qqilari ≈ bo'g'inlar).
3. `template.html` dagi vaqtlarni ovozga moslang, oldin bir nechta kadrni ko'rib chiqing:
   `NODE_PATH=/opt/node22/lib/node_modules node render.js template.html prev 36 30 3,15,30`
4. To'liq kadrlar: `node render.js template.html frames 35.8`
5. Ovoz + musiqa (musiqa ovoz ostida pasayadi):
   ```
   ffmpeg -i voice.wav -ss 0.8 -i music.mp3 -filter_complex "[0:a]aresample=44100,loudnorm=I=-14:TP=-1.5,apad,asplit=2[v][sc];[1:a]aresample=44100,volume=0.5,afade=t=in:d=0.4,afade=t=out:st=34.3:d=1.5[m];[m][sc]sidechaincompress=threshold=0.03:ratio=4:attack=15:release=350[md];[v][md]amix=inputs=2:duration=shortest:normalize=0,alimiter=limit=0.9[a]" -map "[a]" -t 35.8 -c:a aac -b:a 160k -ac 2 mix.m4a
   ffmpeg -framerate 30 -i frames/f%05d.jpg -i mix.m4a -c:v libx264 -crf 20 -pix_fmt yuv420p -c:a copy -movflags +faststart out.mp4
   ```

## Platformalar
| Platforma | Video | Subtitr |
|---|---|---|
| YouTube | Subtitrsiz (`.sub{display:none}`) | Alohida `.srt`: uz, ru, en (Studio → Субтитры → С временными кодами) |
| Instagram, Facebook | Ruscha subtitr videoga yozilgan | — |
| LinkedIn | Inglizcha subtitr videoga yozilgan | Post matni: "AI bilan qanday yasadim" |

## Har bir video oxirida
Qizil **OBUNA BO'LING** tugmasi va uning tagida **oltin rangda** Telegram bot (`@sahiychishopbot`) va sayt (`cheksiz-one.vercel.app/infinite`).

**Tartib (har bir video):** asosiy qism → **avatar 3 soniya** (`avatar.mp4`, egasining avatari) → **obuna kartochkasi 4 soniya**.
- Avatar ustida pastda (y=1250) savol plashkasi: "Siz-chi? / <videoga mos savol> / Izohga yozing!" (ru/en versiyalarda tarjima).
  ```
  ffmpeg -i avatar.mp4 -i avq.png -filter_complex "[0:v]trim=0:3,setpts=PTS-STARTPTS,scale=1080:1920,fps=30,setsar=1[a];[a][1:v]overlay=0:1250:enable='gte(t,0.3)'[v]" ...
  ```
- Kartochka (vertikal, uz/ru/en): `end_uz.html`, `end_ru.html`, `end_en.html` (`mark.png` shu papkada bo'lishi kerak).
  `NODE_PATH=/opt/node22/lib/node_modules node render_end.js end_uz.html fe_uz 4 30` → 120 kadr.
- Musiqa avatar va kartochka davomida ham chaladi, oxirgi ~3 soniyada so'nadi.
