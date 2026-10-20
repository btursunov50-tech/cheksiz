---
name: kamera
description: Rasm→video promptlari uchun kamera harakati tanlash — har bir sahnaning hissiyotiga mos harakat (push-in, dolly, orbit, crane, handheld, rack focus, whip pan ...), ingliz tilidagi aniq iboralar va Hailuo/Kling/Veo/Dreamina'dagi bepul kamera boshqaruvi. Har bir video prompt yozishda ishlating.
---

# Kamera harakati (egasi, 2026-10-18: kamera harakati videoni kuchaytiradi, har promptda bo'lsin)

## Qoida
- Har bir rasm→video promptida **bitta asosiy kamera harakati** (boshida, aniq ibora bilan) + uning tezligi + qayerda tugashi. Bir klipda ikki xil harakatni aralashtirmang (AI chalkashadi).
- Harakat sahnaning hissiyotidan kelib chiqadi (jadval). Ketma-ket sahnalarda bir xil harakatni takrorlamang; tinch → keskin almashtiring.
- Harakat yuz/qahramonni kadrdan chiqarib yubormasin: "keep the face in frame for the whole clip".

## Hissiyot → harakat
| Hissiyot | Harakat | Ibora (promptga) |
|---|---|---|
| Sir, xavf, muhim gap | Sekin yaqinlashish | `slow push-in toward his face, ending in a close-up` |
| Hukm, kuch, ustunlik | Pastdan | `low-angle shot, camera slowly rises (crane up)` |
| Zaiflik, yolg'izlik | Yuqoridan, uzoqlashish | `high-angle shot, slow pull-back revealing the empty room` |
| Keskinlik, tortishuv | Ikki qahramon atrofida | `slow 90-degree orbit around the two men` |
| Shok, burilish | Keskin yaqinlashish | `fast snap zoom-in (crash zoom) on the phone screen` |
| Hayot, ko'cha, shoshilish | Qo'lda | `handheld camera, subtle natural shake, following him` |
| E'tibor bir narsadan boshqasiga | Fokus ko'chishi | `rack focus from the piyola in the foreground to his face` |
| Joyni ko'rsatish | Yon tomonga suzish | `smooth lateral dolly (truck) left along the table` |
| Mahsulot, detal | Makro, aylanish | `macro close-up, slow arc around the product` |
| Yakun, xulosa | Uzoqlashib ko'tarilish | `slow dolly out and crane up, ending wide` |
| Tez montaj zarbasi | Keskin burilish | `whip pan to the right` (keyingi kadrga ulanadi) |
| Gap tinch, harakat kerak emas | Deyarli qimirlamaydi | `locked-off static camera, only subtle breathing movement` |

## Vositalar (bepul)
- **Hailuo** (hailuoai.video): "Director" modeli matn ichidagi kamera buyruqlarini tushunadi: `[Push in]`, `[Pull out]`, `[Pan left]`, `[Pan right]`, `[Truck left]`, `[Tilt up]`, `[Pedestal up]`, `[Zoom in]`, `[Tracking shot]`, `[Shake]`, `[Static shot]`. Promptning boshiga yozing.
- **Kling** (klingai.com): "Camera movement / Camera control" tugmalari (Horizontal, Vertical, Zoom, Pan, Tilt, Roll, Master shots) — bepul tarifda ham bor; matndagi ibora + shu tugma.
- **Veo / Dreamina / Vidu**: tugma yo'q (yoki cheklangan) — faqat matndagi ibora; iborani promptning birinchi gapiga qo'ying.
- Egasiga har promptda qaysi tugmani bosishni ham yozing (Kling/Hailuo uchun).

## Claude'ning o'z yordamchisi (bepul, shu yerda ishlaydi): `harakat.py`
AI klip harakatsiz yoki zaif chiqsa, montajda kamera harakatini o'zim qo'shaman (faqat VIDEO klipga; harakatsiz rasmga emas):
```
python3 .claude/skills/kamera/harakat.py KIRISH.mp4 CHIQISH.mp4 --move pushin --ease
```
`pushin`, `pullout`, `panleft`, `panright`, `tiltup`, `tiltdown`, `shake` (qo'lda olingandek), `crash` (oxirida keskin yaqinlashish), `whipout` (oxirida "qamchi" o'tish), `rack` (xiradan aniqqa). `--amount` kuchini, `--ease` silliqligini boshqaradi. `/video-yig` dan oldin kerakli kliplarga qo'llang va `/klip-tekshir` varag'ida natijani ko'ring (yuz kadrdan chiqmasin).

## Sekinlashuv + zarba ovozi (egasi, 2026-10-20: «effekt chiroyli chiqadi»)
Biror narsa yerga tushadigan joyda (tilla tanga, uzuk, kalit, stakan, rasm, ko'z yoshi): tushayotganda kadr **juda sekinlashadi**, yerga tekkan lahzada **ovoz chiqadi** (tanga: jiring), keyin oddiy tezlik qaytadi. Muhim lahzani ajratib ko'rsatish kerak bo'lgan joyda ishlating, har sahnada emas (bir videoda 1–2 marta).
- **Promptga** (Veo/Kling/Hailuo), inglizcha: `speed ramp: the gold coin slips from his fingers and time slows into extreme slow motion as it falls, turning and catching the candlelight; it hits the stone floor with a crisp impact and a few tiny golden sparks, then normal speed resumes as it spins on the floor.` Kamera: `slow push-in following the coin down to floor level, ending on a low close-up of the floor`.
- **Montajda o'zim** (AI sekinlashtirmasa yoki ovoz bermasa): `python3 .claude/skills/kamera/ramp.py KIRISH.mp4 CHIQISH.mp4 --a <tushish boshi> --b <yerga tekkan payt> --slow 0.3 --sound tanga` (`zarba` = og'ir narsa, `yoq` = ovozsiz). a..b oralig'i minterpolate bilan silliq sekinlashadi, ovoz b nuqtaga tushadi. Natijani `/klip-tekshir` bilan ko'ring.
