# «G'azabda sukut» — Veo video promptlari (9:16, 8 s) → sahnalar.html (o'sha Artifact) + video_promptlar.txt.
# Qoidalar (/promptlar): kamera harakati bilan boshlanadi (qo'shnilarda takrorlanmaydi), rasmdagi harakat davom etadi va qaytmaydi,
# bitta aniq harakat, Diyorning neon chizig'i, Diyor gapirmaydi, yuzlar o'zgarmaydi, oxirida Negative qatori.
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", ".claude", "skills", "promptlar")); from sahifa import page, VEO_NEG, neon
KEEP = ("Keep every person exactly as in the image for the whole clip: Diyor's round boyish young face, messy black hair, dark navy hoodie, jeans and sneakers"
        "{x}; faces must not change into other people; same setting and colours.")
SIL = "Silent video: no audio at all, no voices, no sound effects, no music."  # egasi 2026-11-08: audiosiz, og'izlar qimirlasin
TALK = {  # Diyor gapiradigan sahnalar: lablari tabiiy qimirlaydi (ovozsiz)
 "3": "While smiling Diyor says a few calm words to the colleague, his lips and jaw moving naturally as if talking.",
 "5": "While nodding with his hand on his chest Diyor says a few polite words to the men, his lips and jaw moving naturally as if talking.",
 "7": "While shaking hands both of them say a few warm words to each other, their lips and jaws moving naturally as if talking.",
 "8": "While hugging her and then sitting, Diyor talks softly to his mother and she answers, both their lips moving naturally as if talking.",
}
QUIET = "Diyor keeps his mouth closed in this scene: his calm silence is the point."
S = [
 ("1", "s01", "Juda sekin push-in: yuz va barmoqqa yaqinlashadi",
  "Barmoq «Yuborish» tomon tushadi va tegmasdan, millimetr qolganda to'xtaydi. Montajda: shu payt kadr qotadi, kulrang, «To'xtang!»",
  "Very slow push-in toward Diyor's thumb and face. Diyor's thumb slowly moves down toward the blank glowing phone screen and stops just a millimetre above it, never touching it; his angry frown slowly softens into hesitation, his eyes blink once. The red glow of the screen pulses softly on his face. The phone screen stays plain and blank for the whole clip.", ""),
 ("2", "s02", "Statik (kamera qimirlamaydi)",
  "Odam qo'lini siltab baqiradi; Diyor ko'zini yumib, chuqur nafas oladi, yelkasi tushadi, xotirjam qoladi",
  "Static camera, zero camera movement. The angry man waves his raised hand and shouts at Diyor, his lips and jaw moving clearly and naturally as if shouting; Diyor, still holding the overhead rail, slowly closes his eyes and takes one deep calm breath, his chest rising and his shoulders dropping, his face staying calm and relaxed. The bus sways gently, the city lights pass behind the windows, the blurred passengers sit still.", ", and the angry man's face, grey-black beard, black flat cap and brown leather jacket exactly as in the image"),
 ("3", "s03", "Sekin push-in Diyorning yuziga",
  "Hamkasbi bosh chayqab kinoya qiladi; Diyor sekin, samimiy jilmayadi va ishiga qaytadi",
  "Slow push-in toward Diyor's face. The colleague shakes his head with a mocking smirk, arms still crossed; Diyor looks at him and slowly breaks into a warm, sincere smile, nods once, then calmly turns back to his laptop and keeps typing. The laptop screen stays plain and blank.", ", and the colleague's face exactly as in the image"),
 ("4", "s04", "Statik yaqin kadr",
  "Yozishni to'xtatadi, telefonni ekrani bilan pastga ag'darib skameykaga qo'yadi, chuqur nafas olib daraxtlarga qaraydi",
  "Static close shot, zero camera movement. Diyor stops typing, his thumbs freeze; he looks at the phone for a second, then turns it face down and places it on the bench beside him. He leans back, exhales slowly and looks up at the red autumn leaves; a few leaves fall slowly. The phone stays face down and he does not pick it up again.", ""),
 ("5", "s05", "Sekin pull-back: butun choyxona ko'rinadi",
  "Ikki kishi qizishib bahslashishda davom etadi; Diyor hurmat bilan bosh egadi, piyolasi bilan so'rining narigi chetiga — o'ngga suriladi va bog'ga qarab xotirjam choy ichadi",
  "Slow pull-back revealing the whole teahouse terrace. The two men keep arguing heatedly, waving their hands, their lips and jaws moving clearly and naturally as if shouting; Diyor, his right hand on his chest, gives them a small respectful nod with a kind smile, then, holding his piyola, slides along the carpet to the far right edge of the topchan away from them, turns to face the garden and calmly sips his tea. He moves only to the right and never comes back. Everyone stays in their socks; the shoes stay on the ground below the topchan.", ", and the two men's faces exactly as in the image"),
 ("6", "s06", "Statik past burchak",
  "Rahbar qog'ozni stolga urib baqiradi; Diyor bir marta xotirjam bosh irg'aydi, qo'llari oldida qovushgan",
  "Static low-angle shot, zero camera movement. The boss slams the sheet of paper on the desk with his fist and shouts, leaning forward, his lips and jaw moving clearly and naturally as if shouting; Diyor stays standing straight with his hands calmly together in front of him, listens and gives one slow calm nod, his face steady and respectful. The laptop screen stays plain and blank; the paper has no readable text.", ", and the boss's face exactly as in the image"),
 ("7", "s07", "Sekin yon tomonga suzish (truck chapga), ko'z darajasida",
  "Diyor qo'lini uzatib turadi; odam boshini ko'taradi, ikkilanadi, keyin qo'lini qisadi, ikkalasi jilmayadi",
  "Slow truck to the left at eye level, ending on both of them. Diyor keeps his right hand held out with a kind smile; the man slowly lifts his head, looks at Diyor's hand, hesitates for a moment, then takes it and they shake hands firmly; the man's embarrassed face softens into a small grateful smile. Rain glistens on the pavement, autumn leaves drift down, the bus in the background stays blurred.", ", and the man's face, grey-black beard, black flat cap and brown leather jacket exactly as in the image"),
 ("8", "s08", "Sekin pull-back: iliq xona ko'rinadi",
  "Telefon tokchada qoladi; Diyor onasining oldiga kelib, uni bag'riga bosib quchoqlaydi, keyin yoniga o'tirib, piyoladagi choyni ichadi (piyolalar rasmda allaqachon to'la)",
  "Slow pull-back revealing the warm room. Diyor leaves his phone face down on the shelf, walks to his mother, bends down and hugs her warmly, holding her close to his chest for a moment; she closes her eyes with a happy smile and pats his back. Then he sits down at the table beside her, picks up one of the piyola cups that are already full of tea and takes a sip, smiling at her. Nobody pours tea; the cups are already full, the teapot stays on the table. The phone stays on the shelf and nobody touches it again.", ", and the mother's face and headscarf exactly as in the image"),
]
def prompt(n, img, cam, what, p, x):
    talk = TALK.get(n, QUIET)
    return f"Vertical 9:16 video, 8 seconds, from the attached image. {p} {talk} {neon()} {KEEP.format(x=x)} {SIL}\n{VEO_NEG}"
cards = [dict(num=n, title=f"{n}-sahna — video, 9:16 (tik), 8 s", shot=f"web/{img}.webp", shotcap=f"img/{img}.png — Veo'ga shuni yuklang",
              whatlbl="Nima bo'ladi", what=what, cam=cam, prompt=prompt(n, img, cam, what, p, x)) for n, img, cam, what, p, x in S]
page("G'azabda sukut sahnalari", "«G'azabda sukut» <em>video sahnalari</em>",
     "8 ta sahna, hammasi 9:16 (tik), 8 soniya. Veo'da har biri uchun chapdagi rasmni yuklang va «Nusxa olish» bilan promptni qo'ying. Hikoyachi ovozi, oyatlar, telefon yozuvlari, bot va avatar montajda qo'shiladi. Rasm promptlari: rasm_sahifa.html.",
     cards, os.path.join(D, "sahnalar.html"))
open(os.path.join(D, "video_promptlar.txt"), "w").write("\n\n".join(f"### {x[0]}\n" + prompt(*x) for x in S))
print(len(S), "video prompt")
