---
name: video-yig
description: Loyiha kliplarini (video/<loyiha>/clips) ovoz vaqtiga moslab bitta tik 9:16 video qiladi — klip sekinlashtirish (minterpolate), sinematik rang (cine.sh), sahna kesimlarida whoosh (sfx.sh), ovoz + musiqa (sidechain), o'zbekcha subtitr, STOP yozuvi, avatar (3 s, savol plashkasi) va yakuniy karta, oxirida qora/qotgan kadr/ovozsiz joy tekshiruvi va 30 MB dan kichik nusxa. "Videoni yig'", "ko'rib chiqish versiyasi", "/video-yig'" deganda ishlating.
---

# Video yig'ish

## Loyiha papkasida bo'lishi kerak
- `timeline.py`: `SUB` — (boshi, oxiri, "R"/"O" yoki boshqa, matn) ovoz qatorlari; `CUT` — sahna kesimlari (0 dan oxirgacha); `CLIP` — klip nomlari; `START` — {sahna: klipning boshlanish soniyasi}; ixtiyoriy `STOP` — (boshi, oxiri) qizil STOP yozuvi. Namuna: `video/robot/timeline.py`.
- `clips/<CLIP>.mp4` — `/klip-tekshir` dan o'tgan toza kliplar.
- ovoz fayli (standart `dialog.flac`). Vaqtlarni pauzalardan toping (`silencedetect`), egasidan 2–3 joyni tasdiqlating — Claude ovozni eshitmaydi.

## Ishga tushirish
```
python3 .claude/skills/video-yig/yig.py --dir video/robot --work <scratchpad>/robot_build \
  --avq "Siz-chi?|AIga nimani ishonasiz?|Izohga yozing!" --send
```
- `--n 13` — faqat birinchi 13 sahna (oraliq ko'rib chiqish).
- `--music fayl.mp3:197` — musiqa (trekdagi boshlanish soniyasi). Egasi qoidasi: musiqa butun video va matn tayyor bo'lgandan keyin tanlanadi, bir nechta trekni yamoq qilmang.
- `--no-norm` — ovoz balandligini o'zgartirmaydi (loudnorm o'rniga limiter); musiqani oldindan kerakli dB ga tushiring va `--music-vol 1` bering.
- `--reuse` — faqat ovoz/subtitr/musiqa o'zgarsa, tayyor `cine.mp4` qayta ishlatiladi (tez).
- Bitta sahna klipi 1.8 martadan ko'p sekinlashsa skript ogohlantiradi: egasidan yangi klip so'rang, harakatsiz rasm qo'ymang.

## Yuborishdan oldin
1. Jadvaldagi qotgan/qora kadr, ovozsiz joyni tekshiring (yakuniy kartaning 0.3 s fade-in i — normal).
2. `sheet.jpg` ni **Read** bilan ko'ring: subtitr o'qiladimi, sahna to'g'ri gapga tushganmi, STOP joyidami.
3. Egasiga `send_uz.mp4` ni yuboring, nimalar bor, nimani tekshirishi kerakligini jadval bilan ayting.
4. en/ru versiyalar uchun `SUB` tarjimasi alohida `timeline_en.py`/`_ru` qilib beriladi (keyingi qadam).
