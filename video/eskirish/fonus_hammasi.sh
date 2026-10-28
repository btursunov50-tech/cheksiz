#!/bin/bash
# Ko'cha fonuslarini navbatma-navbat (bittasi ko'k, bittasi o'z rangida) faqat ichini ko'k neon qiladi (egasi, 2026-10-28). Asl rasmlar img/asl/ ga ko'chiriladi.
# Koordinatalar 941x1672 o'lchamdagi rasm bo'yicha (lamp = fonus boshi: cx,cy,r; roi = uzoqdagi mayda fonuslar qatori).
cd "$(dirname "$0")"; mkdir -p img/asl
run(){ n=$1; shift; [ -f img/asl/$n.png ] || cp img/$n.png img/asl/$n.png; python3 fonus.py img/asl/$n.png img/$n.png --show "${SHOW:-/dev/null}_$n.jpg" "$@"; }
run s01 --lamp 845,515,38
run s02 --lamp 770,398,42 --roi 780,740,941,900
run s03 --lamp 903,144,48
run s04 --lamp 155,402,48 --lamp 68,539,26 --lamp 713,524,26 --lamp 759,493,22 --lamp 642,600,20 --roi 0,620,130,780
run s06b --lamp 868,622,45 --lamp 724,820,32
run s07 --lamp 80,516,48 --lamp 21,577,24 --lamp 653,645,32 --lamp 777,729,26 --roi 600,700,941,870 --roi 0,450,200,900
run s11 --lamp 88,304,58 --lamp 61,539,24 --lamp 915,524,36 --roi 700,650,941,800 --roi 0,520,140,760
run s12 --lamp 48,296,58 --lamp 100,562,26 --lamp 152,660,24 --lamp 915,665,30 --lamp 812,729,24 --lamp 737,736,22 --roi 600,680,941,800 --roi 0,520,190,760
run s13 --lamp 58,592,52 --lamp 27,787,22 --lamp 78,845,20 --lamp 78,885,20 --lamp 120,962,20 --lamp 146,985,18 --roi 640,900,941,1060
run s14 --lamp 46,577,52 --lamp 83,744,30 --lamp 114,842,24 --lamp 862,934,32 --lamp 767,949,26 --lamp 653,956,24 --roi 450,960,941,1050 --roi 0,700,200,1000
run s15 --lamp 46,425,48 --lamp 130,569,36 --lamp 190,660,26 --lamp 838,683,30 --roi 790,680,941,790 --roi 0,600,200,800
