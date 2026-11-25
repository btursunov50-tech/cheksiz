---
name: taqrizchi
description: «Qattiq taqrizchi» sikli — ssenariy, ovoz bloki, post matnlari yoki promptni egasiga berishdan OLDIN o'zi tekshiradi, kamchiliklarni ro'yxat qiladi, tuzatadi va qayta baholaydi; faqat baho oshgan versiya qabul qilinadi (ko'pi bilan 3 aylana). POSTS.md uchun `post_tekshir.py` avtomatik baho beradi. Har yangi ssenariy, POSTS.md yoki prompt sahifasi tayyor bo'lganda so'ramasdan ishlating.
---

# Qattiq taqrizchi

G'oya Google'ning ochiq kodli **Paper Orchestra** tizimidan olingan (github.com/google-research/paper-orchestra, Apache-2.0; egasi 2026-11-25 yubordi, `ideas/IDEAS.md` 33). Kod ko'chirilmagan, faqat usul:

1. **Yozuvchi** qoralama yozadi.
2. **Taqrizchi** qattiq baholaydi: kuchli joylar, zaif joylar, savollar, 10 ballik baho.
3. Yozuvchi faqat zaif joylarni tuzatadi, kuchli joylarga tegmaydi.
4. Qayta baho. **Baho oshmasa, eski versiya qoladi** (yomonlashgan tuzatish qabul qilinmaydi).
5. Ko'pi bilan 3 aylana, keyin egasiga beriladi.
6. **Haqiqat manbai**: raqam va faktlar faqat tekshirilgan ro'yxatdan (POSTS.md dagi «Faktlar:» qatori, ssenariy manbalari) olinadi. Taqrizchi yangi fakt so'rasa va u ro'yxatda bo'lmasa, to'qilmaydi: o'sha talab tashlab ketiladi yoki egasidan so'raladi.

## 1. Post matnlari (avtomatik)
```bash
python3 .claude/skills/taqrizchi/post_tekshir.py video/<loyiha>/POSTS.md
```
Tekshiradi: har platforma bo'limi bor; AI satri (uz/ru/en); @sahiychishopbot va bosiladigan `t.me/sahiychishopbot` (Instagram, YouTube); izoh so'rovi (savol); Telegram'da sayt havolasi; Suno bo'lsa «Music: made with Suno»; YouTube'da `<` `>` yo'q; sarlavha ≤100 belgi, `#shorts`, hook bahosi ≥50 (`ig-reel/hookscore.py`). **10/10 bo'lmaguncha egasiga bermang.**

## 2. Ssenariy va ovoz bloki (qo'lda, shu ro'yxat bo'yicha)
| # | Tekshiruv | Qoida (CLAUDE.md) |
|---|---|---|
| 1 | Hook (1-satr) inglizchasi ≥50 | hookscore |
| 2 | Bot chaqiruvi shu mavzu uchun, `bot/knowledge.js` da bor | 2026-10-24 |
| 3 | Oxirgi raqamli satr — avatar savoli («Siz-chi? … Izohga yozing!») | 2026-10-27 |
| 4 | Bitta hikoyachi (Diyor/Usta faqat so'ralsa) | 2026-11-02 |
| 5 | Har fakt manbali, raqamlar to'qilmagan | Hooks qoidasi |
| 6 | Ovoz bloki: bitta nusxa blok, sozlamalar + raqamli satrlar, BIP formati | 2026-10-28 |
| 7 | Oyat bo'lsa: sura va oyat raqami, ma'no tarjimasi | «G'azabda sukut» |

## 3. Rasm/Veo promptlari (qo'lda)
| # | Tekshiruv |
|---|---|
| 1 | Format belgisi (9:16 …) sarlavhada va prompt ichida |
| 2 | Kamera harakati boshida; hissiy joyda yaqin plan + yuz ifodasi |
| 3 | Gapiruvchi o'zbekcha satri `says in Uzbek: "..."` |
| 4 | `Negative:` qatori; «halo», «danger», joy so'zlari (bazaar) yo'q |
| 5 | Boshlang'ich kadr = harakat boshi; yo'nalish aniq, teskarisi taqiqlangan |
| 6 | Rasmdagi buyumlar holati (to'la piyola, ochiq eshik) bilan mos harakat |
| 7 | Namuna rasm kerak bo'lsa, u prompt yonida |

## Natija formati (egasiga ko'rsatmang, o'zingiz uchun)
```
Baho: 7/10
Kuchli: ...
Zaif: 1) ... 2) ...
Tuzatildi: ...
Yangi baho: 9/10 (qabul)
```
Egasiga faqat yakuniy, tekshirilgan matn beriladi.
