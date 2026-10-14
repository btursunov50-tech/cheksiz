# voice pieces: (file, start, end, place_at)
V=[('ota',0.05,2.25,0.3),('diktor',2.9,4.85,2.8),
   ('ota',5.85,8.55,5.5),('diktor',5.4,9.7,8.6),
   ('ogil',0.15,2.5,13.5),('diktor',10.55,15.3,16.2),
   ('diktor',16.12,20.98,21.6),('diktor',21.62,25.3,27.6),('diktor',25.88,29.98,33.2),
   ('ogil',7.15,10.0,38.9),('ota',15.35,17.2,42.0),
   ('diktor',30.96,35.85,44.0),('diktor',36.64,42.3,49.3)]
CUTS=[5.2,13.2,21.2,27.2,32.7,38.7,46.7]; MAIN=55.3
# subtitles: (start,end,style,key)
S=[(0.3,2.6,'F','f1'),(2.8,4.9,'S','n1'),(5.5,8.2,'F','f2'),(8.6,12.9,'C','n2'),(13.5,15.9,'O','o1'),(16.2,21.0,'C','n3'),
   (21.6,24.2,'S','n4a'),(25.3,26.5,'S','n4b'),(27.6,31.3,'S','n5'),(33.2,35.1,'S','n6a'),(35.7,37.3,'S','n6b'),
   (38.9,41.8,'O','o2'),(42.0,43.9,'F','f3'),(44.0,46.6,'S','n7a'),(47.1,48.9,'S','n7b'),(49.3,51.8,'S','n8a'),(52.5,55.0,'S','n8b')]
T={'uz':{'f1':"«Ishlagan pulingni stolga qo'y!»",'n1':"Dadam buni nazarda tutmagan edi.",'f2':"«Biz seni yigirma yil boqdik!»",
 'n2':"Asl ma'nosi: men senga kerak bo'lmay qolishdan qo'rqaman.",'o1':"«Meni tug'ing deb so'ramaganman!»",
 'n3':"Asl ma'nosi: dada, bir marta bo'lsa ham men bilan faxrlaning.",'n4a':"U birinchi oyligidan dadasiga sovg'a olgan edi.",
 'n4b':"Berishga ulgurmadi.",'n5':"Dadasi esa yigirma yildan beri unga uy uchun pul yig'ardi.",'n6a':"Ikkalasi ham bir-birini yaxshi ko'rardi.",
 'n6b':"Faqat buni aytishni bilmasdi.",'o2':"«Sizni yaxshi ko'raman, dada.»",'f3':"«Men ham seni yaxshi ko'raman, o'g'lim.»",
 'n7a':"Ba'zan odamlar boshqa gapni aytadi,",'n7b':"qalbida esa boshqasini his qiladi.",'n8a':"Bugun yaqin insoningizga «yaxshi ko'raman» deng.",
 'n8b':"Ayta olmasangiz, shu videoni yuboring."},
 'ru':{'f1':"«Выкладывай зарплату на стол!»",'n1':"Папа имел в виду совсем другое.",'f2':"«Мы тебя двадцать лет кормили!»",
 'n2':"На самом деле: я боюсь, что стану тебе не нужен.",'o1':"«Я не просил меня рожать!»",'n3':"На самом деле: папа, хоть раз скажи, что гордишься мной.",
 'n4a':"Он купил отцу подарок с первой зарплаты.",'n4b':"Но не успел подарить.",'n5':"А отец двадцать лет копил ему на дом.",
 'n6a':"Они любили друг друга.",'n6b':"Просто не умели это сказать.",'o2':"«Я люблю тебя, папа.»",'f3':"«И я тебя люблю, сынок.»",
 'n7a':"Иногда люди говорят одно,",'n7b':"а в сердце чувствуют другое.",'n8a':"Скажите сегодня близкому «я тебя люблю».",'n8b':"Не можете сказать — отправьте ему это видео."},
 'en':{'f1':"“Put your salary on the table!”",'n1':"That's not what my father meant.",'f2':"“We fed you for twenty years!”",
 'n2':"What he meant: I'm afraid you won't need me anymore.",'o1':"“I never asked to be born!”",'n3':"What he meant: Dad, just once, tell me you're proud of me.",
 'n4a':"He bought his father a gift with his first salary.",'n4b':"He never got to give it.",'n5':"And his father had saved for twenty years to buy him a home.",
 'n6a':"They loved each other.",'n6b':"They just didn't know how to say it.",'o2':"“I love you, Dad.”",'f3':"“I love you too, son.”",
 'n7a':"Sometimes people say one thing,",'n7b':"but feel another in their heart.",'n8a':"Tell someone close “I love you” today.",'n8b':"If you can't, send them this video."}}
NOTE={'uz':("Dadaga. Birinchi oyligimdan","Uy uchun","Bugun «yaxshi ko'raman» deng"),
      'ru':("Папе. С первой зарплаты","На дом для сына","Скажите сегодня «я тебя люблю»"),
      'en':("For Dad. From my first salary","For my son's home","Say “I love you” today")}
AVQ={'uz':("Siz-chi?","Dadangizga oxirgi marta qachon «yaxshi ko'raman» degansiz?","Izohga yozing!"),
     'ru':("А вы?","Когда вы последний раз говорили папе «я тебя люблю»?","Напишите в комментариях!"),
     'en':("And you?","When did you last tell your dad “I\u00a0love\u00a0you”?","Tell me in the comments!")}
