# «Ko'rish bor. Pul yo'q.» — holat

Sahifa (rasm + video promptlari): https://claude.ai/artifact/7j5B4eDvcszZYR2qJM8yMQ (`rasm_prompts.py` -> `rasmlar.html`).
Ovoz: `voice/`, vaqtlar `timeline.py`. Rasmlar: `img/01..11` (hammasi tayyor).

## Kliplar (`clips/`, /klip-tekshir bilan tekshirilgan)
| Klip | Vosita | Uzunlik | Holat |
|---|---|---|---|
| s01 telefon nuri | Veo | 6 s | ✅ push-in, tabassum kengayadi; yuz namunadek |
| s02 2-yigit chiqadi | Veo | 6 s | ✅ kameraga yurib keladi; yuz, palto, etik namunadek |
| s03 telefonni tushiradi | Veo | 6 s | ✅ ~1.45 s da crash zoom (BOOM shu yerga), keyin yaqin plan; ~3 s da lab biroz ochiladi (dovdirash) |
| s04 «Shovqin» | Veo | 6 s | ✅ statik, lampochka tebranadi, havoda mayda chang; sahna ~7.2 s -> 1.2x sekinlashadi |
| s05a trend (yonga) | Veo | 8 s | ✅ ekranlarda ilova tugmalari ko'rinadi (o'qiladigan yozuv yo'q), ekranlar orasida bitta lampochka |
| s05b trend (ichkariga) | Veo | 8 s | ✅ birinchi kadr rasmdan boshlanmaydi (Veo rasmni boshlang'ich kadr qilmagan), lekin s05a oxiriga mos ko'k-qora uslub |
| s05w ofitsiant (5b) | Veo | 6 s | ✅ qiz o'tadi, ikkala yigit unga qaraydi; oxirida orqaga o'girilmaydi (qiz ketgan tomonga qarab qoladi) — keyingi 6a kesimi buni yopadi; qizning yuzi, do'ppi, ko'ylak namunadek |
| s06a suhbat | Veo | 6 s | ✅ 2-yigit gapiradi (lab harakati ruxsat), 1-yigit iyagini ushlab tinglaydi; derazadagi osmon oxiriga borib biroz yorishadi — cine.sh bilan qoraytiriladi |
| s06b piyola | Veo | 6 s | ✅ fokus choynakdan yuzga ko'chadi (~1.2 s xira, keyin aniq); bug' iyakkacha, yuzni to'smaydi; piyolani qo'ymaydi, ushlab turadi |
| s07 non | Veo | 6 s | ✅ non atrofida aylanadi, naqsh o'zgarmaydi; 2 s dan keyin tepada qalin bug' (nonni to'smaydi) |
| s08 tikuvchi | Veo | 4 s | ✅ chokni tortib ko'rsatadi, qo'llar to'g'ri; klip 4 s, sahna ~6 s -> 1.5x sekinlashadi (minterpolate) |
| s09 gulchi | Veo | 6 s | ✅ guldasta uzatiladi, oxirida xaridor qo'lida; qo'llar soni to'g'ri |
| s10 bitta surat | Veo | 8 s | ✅ kameraga jilmayadi, keyin telefonga o'girilib suratga oladi; ekranda faqat non va kamera tugmasi, yozuv yo'q; sahna ~9 s -> 1.13x |
| s11 yakun | ? (756×1344) | 6 s | ✅ uzoqlashib ko'tariladi, keng kadrda tugaydi; yuzlar va kiyim namunadek, krossovkada belgi yo'q; START 1.4 |
Hamma kliplar tayyor. Yig'ish: `python3 video/korish/ovoz.py` (ovoz.flac + SUB vaqtlari), keyin `/video-yig --voice ovoz.flac` (timeline.py: SUB, CUT, CLIP, START, BOOM, TEXT).

## Musiqa (2026-10-18)
- Curious Unease (Suno) — egasiga yoqmadi: bass yo'q.
- Egasi YouTube Audio Library'dan 2 ta trek berdi (`music/`). Tanlandi: **Whitefish Salad «LATASH»** (bass 73%, ~92 BPM), trekning 5.5 s dan: bass tushishi (13.5 s) videoning 8.0 s dagi BOOM ga tushadi, 31–35 s (ofitsiant) tinchroq joy, 67.3 s da to'xtaydi.
- Zaxira: Yo Picasso «Verified Picasso» (bass 77%, ~99 BPM).
- Yig'ish: `--voice ovoz.flac --music "video/korish/music/Whitefish_Salad_-_LATASH.mp3:5.5"`.
- Egasi Suno'da 2 ta trek qildi (bepul tarif: «Music: made with Suno», monetizatsiyasiz): **Nocturnal Tension** (bass 81%, birinchi zarba 8.5 s) va Nocturnal Pressure (bass 80%, zarba 6.5 s). 4-versiyada Tension 0.5 s dan: zarba 8.0 s dagi BOOM ga tushadi. `--music "video/korish/music/Nocturnal_Tension.mp3:0.5"`.
- 5-versiya (egasi ma'qulladi): Nocturnal Tension oxirigacha davom etadi, avatar va yakuniy karta ustida 5 s da sekin so'nadi (`MUSIC_FADE = 5`). Tayyor uz video: `video/final/korish/korish_uz.mp4`.
