# Renders the 8 morning-post videos (run inside video/tong/; needs Playwright + ffmpeg).
# Then copy out/*.mp4 to infinite/media/tong/. Change flowers/colors in anim.html (PAL, front/back lists).
set -e
export NODE_PATH=/opt/node22/lib/node_modules
OUT=${OUT:-out}; mkdir -p $OUT
r(){ rm -rf fr; node frames.js "$2" fr 25; ffmpeg -v error -y -framerate 25 -i fr/f%04d.jpg -c:v libx264 -preset slow -crf 22 -pix_fmt yuv420p -movflags +faststart -an $OUT/$1.mp4; echo done $1; }
r 2026-10-10 "mode=sat&day=Shanba,%2010-oktyabr&theme=aralash"
r dushanba "mode=day&day=Dushanba&wish=Yangi%20hafta%20muborak!&theme=atirgul"
r seshanba "mode=day&day=Seshanba&wish=Kuningiz%20barakali%20o'tsin!&theme=kungaboqar"
r chorshanba "mode=day&day=Chorshanba&wish=Ishlaringizga%20omad!&theme=lola"
r payshanba "mode=day&day=Payshanba&wish=Niyatlaringiz%20ijobat%20bo'lsin!&theme=lavanda"
r juma "mode=day&day=Juma&wish=Juma%20muborak!&theme=moychechak"
r shanba "mode=day&day=Shanba&wish=Kuningiz%20hamisha%20Alloh%20panohida%20o'tsin!&theme=aralash"
r yakshanba "mode=day&day=Yakshanba&wish=Oilangiz%20bilan%20xayrli%20dam%20oling!&theme=pion"
ls -la $OUT
