# Kuzgi O'zbekiston: 7 ta ertalabki video (gullar o'rniga obida rasmi). Rasmlar: kuz/<nom>.jpg (1:1, KUZ.md dagi promptlar).
# Ishlatish: video/tong ichida  bash all_kuz.sh  → out_kuz/*.mp4 → infinite/media/tong/ ga ko'chiriladi (bot kodi o'zgarmaydi).
set -e
export NODE_PATH=/opt/node22/lib/node_modules
OUT=${OUT:-out_kuz}; mkdir -p $OUT
r(){ [ -f "kuz/$2.jpg" ] || { echo "YO'Q: kuz/$2.jpg"; return; }; F=fr_$1; rm -rf $F; node frames.js "mode=day&kuz=1&theme=kuz1&day=$3&wish=$4&place=$5&bg=kuz/$2.jpg&rain=${6:-0}" $F 25
  ffmpeg -v error -y -framerate 25 -i $F/f%04d.jpg -c:v libx264 -preset slow -crf 22 -pix_fmt yuv420p -movflags +faststart -an $OUT/$1.mp4; rm -rf $F; echo done $1; }
r dushanba   registon  "Dushanba"   "Yangi%20hafta%20muborak!"                       "Samarqand,%20Registon" &
r seshanba   poikalon  "Seshanba"   "Kuningiz%20barakali%20o'tsin!"                  "Buxoro,%20Poi%20Kalon" 1 &
r chorshanba xiva      "Chorshanba" "Ishlaringizga%20omad!"                          "Xiva,%20Ichan%20Qal'a" &
r payshanba  hazratiimom "Payshanba" "Niyatlaringiz%20ijobat%20bo'lsin!"             "Toshkent,%20Hazrati%20Imom" 1 &
r juma       shahrisabz "Juma%20muborak!" ""                                          "Shahrisabz,%20Oqsaroy" &
r shanba     teleminora "Shanba"    "Kuningiz%20hamisha%20Alloh%20panohida%20o'tsin!" "Toshkent%20teleminorasi" 1 &
r yakshanba  qoqon     "Yakshanba"  "Oilangiz%20bilan%20xayrli%20dam%20oling!"       "Qo'qon,%20Xudoyorxon%20o'rdasi" &
wait; ls -la $OUT
