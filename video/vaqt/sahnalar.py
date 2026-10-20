# «VAQT» — Veo uchun video promptlari sahifasi (rasm + ovoz + prompt + men qo'shadigan effekt).
# Ishga tushirish: python3 video/vaqt/sahnalar.py  → video/vaqt/sahnalar.html (+ web/*.webp)
import html, os
from PIL import Image
KB = "Keep the old merchant exactly as in the image for the whole clip: same face, long white beard, white turban with the patterned cap, gold-embroidered dark robe and gold rings."
KA = "Keep the 7-year-old grandson exactly as in the image for the whole clip: same face, black embroidered doppi skullcap, brown embroidered vest and light shirt."
KQ = "Keep the daughter exactly as in the image for the whole clip: same face, light headscarf and ikat dress."
NOV = "No other person or figure appears anywhere in the frame, the doorway and the blue-lit side stay empty."
MUTE = "Nobody speaks, mouths stay closed."
def end(sec):
    return (f"Vertical 9:16, {sec} seconds, realistic cinematic motion that fills all {sec} seconds. Warm brown and amber candlelight look as in the image, "
            "deep soft shadows, gentle film grain. No text, no captions, no subtitles, no watermark, no new objects or people. No music, ambient sound only.")
S = [
 ("1", "Hook: qum soati", "0:00–0:04", "Diktor: «Vaqtni sotib olib bo'lmaydi. Lekin sen uni har kuni sotasan.»", None, None,
  "To'liq kodda, Veo kerak emas (tayyor: kod/hook.mp4)."),
 ("2", "Boy tanga sanaydi, Aziz eshikda", "0:04–0:12", "Aziz: «Bobo, osh tayyor.» Boy: «Keyin, bolam. Keyin.»", "s02_boy_aziz",
  ("Rack focus: the shot starts focused on the old merchant counting gold coins at the desk, then the focus slowly shifts to the grandson peeking from the doorway and stays there; the camera itself barely moves. "
   "The merchant keeps stacking coins and writing in his ledger and never looks up. The grandson smiles hopefully and says a short line with small natural lip movement; the merchant answers with a short line without raising his head and waves his hand once; the boy's smile fades, he lowers his eyes and slowly steps back behind the door. The candle flame flickers gently, the sunset in the window slowly darkens. "
   + KB + " " + KA, 8),
  "Rang (cine), ovoz qatorlari, tanga jiringlashi soat tik-tikiga mos."),
 ("3", "Sham o'chdi, tanga tushadi", "0:12–0:22", "Vaqt: «Qo'rqma. Olib ketgani kelmadim. Hisobingni ko'rsatgani keldim.»", "s03_tanga",
  ("Slow push-in that follows the falling coin down to floor level, ending on a low close-up of the stone floor. Speed ramp: the gold coin slips from the merchant's fingers and time slows into extreme slow motion as it falls, turning and catching the cold blue light; it hits the stone floor with a crisp impact and a few tiny golden sparks, then normal speed resumes and the coin spins on the floor. "
   "The merchant stays frozen, staring at the open doorway in shock; the thin smoke from the blown-out candle curls upward; the cold blue light from the doorway grows slowly brighter on the floor. " + NOV + " " + KB + " " + MUTE, 8),
  "Eshikda neon VAQT gavdasi (kod), sekinlashuv ramp.py bilan, tanga tekkanda «jiring», xonani qoraytirib ko'kroq qilaman."),
 ("4", "Boy sandiqni suradi", "0:22–0:30", "Boy: «O'tgan yillarimni qaytar, hamma oltinimni ol!»", "s04_sandiq",
  ("Smooth slow lateral dolly (truck) to the right, from the merchant's pleading face toward the empty blue-lit space on the right, keeping him in frame. "
   "The old merchant pushes the heavy open chest of gold coins forward with both hands, pleading, looking up and to the right as if at a very tall figure, and speaks a short desperate line with natural lip movement; a few coins slide on top of the pile. Dust floats in the cold blue light on the right. " + NOV + " " + KB, 8),
  "O'ng tomonda neon VAQT (kod)."),
 ("5", "Tangalar qumga aylanadi", "0:30–0:38", "Vaqt: «O'tgan vaqt sotilmaydi. Umr faqat Allohning qo'lida. Men faqat ko'rsataman.»", "s05_qum",
  ("Macro close-up, slow arc around the chest from left to right. One by one the gold coins crumble into fine golden sand, starting at the rim and spreading over the whole pile until the entire chest is a flowing mass of golden sand pouring over the edge onto the carpet like a waterfall; tiny grains glitter in the cold blue light. No hands, no people. ", 8),
  "Neon barmoq sandiqqa tegadigan uchqun (kod), qum shitirlashi."),
 ("6a", "1-xotira: qizcha qo'g'irchoq ko'rsatadi", "0:38–0:42", "(musiqa)", "x1_qogirchoq",
  ("Slow push-in toward the little girl's face. She holds the cloth doll up toward her father with a hopeful smile; he keeps counting gold coins and does not look at her; her smile slowly fades, she lowers the doll, hugs it to her chest and turns away. Keep the father and the little girl exactly as in the image for the whole clip. " + MUTE, 8),
  "Oltin xotira rangi, konturlar chiziladi, oxirida qumga aylanib to'kiladi (xotira.py)."),
 ("6b", "2-xotira: qizining to'yi, otaning o'rni bo'sh", "0:42–0:46", "(musiqa)", "x2_toy",
  ("Slow pull-back (dolly out) that reveals the empty ornate seat beside the bride. The bride keeps looking toward the gate, hopeful, then her smile slowly fades and she lowers her eyes; candle flames flicker, guests move softly in the blurred background. " + KQ + " " + MUTE, 8),
  "Oltin xotira rangi + qum (xotira.py)."),
 ("6c", "3-xotira: qizi chaqaloqni ko'rsatadi", "0:46–0:50", "(musiqa)", "x3_chaqaloq",
  ("Rack focus from the newborn baby in the daughter's arms to the father's hand waving her away. The daughter holds the sleeping baby out toward her father with a shy smile; he keeps writing in his ledger and waves his hand without looking up; she slowly draws the baby back to her chest. " + KQ + " " + KB + " " + MUTE, 8),
  "Oltin xotira rangi + qum (xotira.py)."),
 ("6d", "4-xotira: Azizning birinchi qadamlari", "0:50–0:54", "(musiqa)", "x4_qadam",
  ("Low-angle tracking shot at the toddler's height, moving slowly with him. The toddler takes three wobbly first steps toward his grandfather with arms stretched out and a big smile; the grandfather keeps writing and does not turn; the toddler loses balance and sits down softly on the carpet, and his mother quickly kneels and lifts him into her arms. Keep the grandfather, the mother and the toddler exactly as in the image for the whole clip. " + MUTE, 8),
  "Oltin xotira rangi + qum (xotira.py)."),
 ("6e", "5-xotira: rasm polga tushadi", "0:54–0:58", "(musiqa; oxirida Vaqt: «O'ttiz yil.»)", "x5_rasm",
  ("High angle, slow crane down that follows the drawing to the floor. Speed ramp: the grandson holds up his crayon drawing with a big smile, the grandfather keeps counting coins and does not look; the paper slips from the boy's fingers and drifts down in slow motion, swaying side to side, and lands softly on the floor; the boy's smile fades. " + KA + " " + KB + " " + MUTE, 8),
  "Oltin xotira rangi + qum, rasm tushganda sekinlashuv (ramp.py, ovoz: yumshoq)."),
 ("7", "Tavba, boy yig'laydi", "0:58–1:06", "Boy: «Bittasini qaytar...» Vaqt: «O'tganini hech kim qaytarolmaydi...»", "s07_tavba",
  ("Slow push-in toward his tearful face, ending in a close-up. The old merchant kneels and cries quietly, a tear runs down his cheek; golden sand slowly slips through his open fingers onto the carpet; he whispers a short line with small lip movement and looks up and to the right with deep regret; the cold blue light on his face pulses very softly. " + NOV + " " + KB, 8),
  "Vaqtning qum soati (yuqorisi qorong'i) o'ng tomonda, kodda."),
 ("8", "Sham qayta yonadi, tanga polda", "1:06–1:14", "Aziz: «Bobo, osh sovib qoldi.» Boy: «Hozir, bolam! Hozir!»", "s08_uygonish",
  ("Rack focus from the gold coin on the floor in the foreground to the old merchant in the background. The coin wobbles slightly and settles flat on the stone floor; the candle flame steadies and grows warm; the merchant closes his ledger, stands up, turns toward the door and calls out a short warm line with natural lip movement, with a soft new smile. " + KB, 8),
  "Tanga to'xtaganda yengil jiring."),
 ("9", "Hovli, osh, oila", "1:14–1:24", "(musiqa)", "s09_hovli",
  ("Slow dolly out and crane up, ending wide over the evening courtyard. The grandfather laughs softly and strokes his grandson's head, the boy laughs back; the daughter serves him a plate of osh with happy tears in her eyes; the lanterns glow warm, leaves move in a light breeze, steam rises from the osh. The blue shadow in the corner of the porch slowly fades into warm golden light. " + KB + " " + KA + " " + KQ + " " + MUTE, 8),
  "Ayvon soyasida neon VAQT oltinga aylanib so'nadi (kod)."),
 ("10", "Daftarning oxirgi sahifasi", "1:24–1:30", "Diktor: «O'tgan vaqt qaytmaydi. Shuning uchun — bugun va hozir.»", "s10_daftar",
  ("Locked-off static top-down camera, it does not move. The old merchant's hand dips the pen into the ink pot, lifts it and holds it still over the blank page for a few seconds, then slowly closes the ledger; the candle flame flickers. The page stays completely blank, no letters or lines are drawn. " + MUTE, 8),
  "Sahifaga «Foyda — bugun va hozir.» yozuvi qo'lda yozilgandek (kod), keyin qora ekran: VAQT."),
 ("13", "Epilog: bugungi kun", "1:30–1:40", "Aziz: «Bobo, bugungi AI maslahati!» Diktor: «Vaqtingizni bekorga ketkazmang...»", "s13_bugun",
  ("Handheld camera with subtle natural shake, slowly moving closer to the two of them. The grandson shows the smartphone to his grandfather and says a short excited line with natural lip movement, pointing at the screen; the grandfather leans in, reads, laughs warmly and nods; morning sunlight flickers through the leaves. The phone screen stays plain soft blue the whole time, with no text and no interface. "
   "Keep the grandfather exactly as in the image (black doppi, white beard, dark quilted chopon, light shirt) and the boy exactly as in the image (doppi, light shirt, jeans, sneakers) for the whole clip.", 8),
  "Oldin o'tish: eski kadr qumga aylanadi → «Bugun». Telefon ekranida «Kun maslahati», ko'k neon chiziq bo'lib ko'tariladi (kod); kanal va bot havolasi."),
]
os.makedirs("video/vaqt/web", exist_ok=True)
e = html.escape; cards = []
for n, name, t, voice, img, vid, mine in S:
    media = ""
    if img:
        im = Image.open(f"video/vaqt/img/{img}.jpg"); im.thumbnail((420, 746)); im.save(f"video/vaqt/web/{img}.webp", quality=80)
        media = f'<div class="media"><img src="web/{img}.webp" alt="{e(name)}"></div>'
    pr = ""
    if vid:
        txt, sec = vid
        pr = (f'<p class="lbl vid">🎬 Veo prompti — 9:16 (tik), {sec} s · shu rasmni yuklang</p>'
              f'<pre id="v{n}">{e(txt + " " + end(sec))}</pre>'
              f'<button type="button" class="copy" data-t="v{n}">Nusxa olish</button>')
    cards.append(f'''<article class="card" id="s{n}">
<header><span class="num">{n}</span><h2>{e(name)}</h2><span class="dur">{t}</span></header>
{media}<div class="txt"><p class="voice"><span class="lbl">Ovoz</span>{e(voice)}</p>
{pr}<p class="mine"><span class="lbl">Men qo'shaman</span>{e(mine)}</p></div>
</article>''')
head = open("video/robot/page_head.html").read()
head = head.replace("<title>Robot bilan choy sahnalari</title>", "<title>Vaqt sahnalari</title>")
head = head.replace("«Robot bilan bir piyola choy» sahnalari", "«VAQT» — Veo promptlari")
i = head.index('<p class="intro">'); j = head.index('</p>', i) + 4
head = head[:i] + ('<p class="intro">Har sahnada: rasm, ovoz qatori, Veo prompti va men montajda qo\'shadigan narsa. Veo\'ga faqat shu rasmni yuklang, formatni 9:16 qiling, «Nusxa olish» bilan promptni qo\'ying. '
                   'Vaqt (neon gavda) rasmlarda ataylab yo\'q: uni o\'zim kodda qo\'yaman, shuning uchun eshik va ko\'k tomon bo\'sh qolishi kerak. Ovozni o\'zimiz qo\'yamiz, Veo ovoziga e\'tibor bermang.</p>') + head[j:]
head = head.replace("</style>", ".mine{margin:0;color:var(--muted);font-size:14px}.vid{color:var(--sun)}</style>")
open("video/vaqt/sahnalar.html", "w").write(head + "\n".join(cards) + open("video/robot/page_tail.html").read())
print(len(S), "sahna")
