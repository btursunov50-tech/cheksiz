#!/bin/bash
# Ko'cha fonuslari: katta fonuslarning faqat shishasi ko'k neon (egasi, 2026-10-28), zich uzoq qatorlarda navbatma-navbat (--roi).
# --glass cx,cy,hw,hh = fonus shishasi ellipsi, 941x1672 rasmda aniq o'lchangan (2026-10-28: avvalgi taxminiy joylar shishadan siljib ketgan edi).
cd "$(dirname "$0")"; mkdir -p img/asl
run(){ n=$1; shift; [ -f img/asl/$n.png ] || cp img/$n.png img/asl/$n.png; python3 fonus.py img/asl/$n.png img/$n.png --show "${SHOW:-/dev/null}_$n.jpg" "$@"; }
run s01 --glass 848,520,10,11
run s02 --glass 768,409,19,21 --roi 780,740,941,900
run s03 --glass 905,193,25,30
run s04 --glass 155,406,17,24 --glass 68,544,11,13 --glass 713,550,12,15 --glass 642,606,8,10 --roi 0,620,130,780
run s06b --glass 868,630,29,25 --glass 724,814,22,20
run s07 --glass 80,525,24,28 --glass 24,596,15,15 --glass 653,660,16,20 --glass 778,728,11,13 --roi 600,700,941,870 --roi 0,450,200,900
run s11 --glass 85,325,29,42 --glass 63,550,13,15 --glass 915,540,18,25 --roi 700,650,941,800 --roi 0,520,140,760
run s12 --glass 48,322,29,45 --glass 102,555,14,14 --glass 154,664,11,11 --glass 914,682,12,16 --glass 812,729,11,11 --glass 739,732,9,9 --roi 600,680,941,800 --roi 0,520,190,760
run s13 --glass 57,620,28,35 --glass 26,789,14,16 --glass 72,849,8,9 --glass 82,883,10,10 --glass 122,960,10,10 --glass 148,989,9,9 --roi 640,900,941,1060
run s14 --glass 47,610,26,36 --glass 83,777,19,21 --glass 110,855,15,16 --glass 862,946,17,20 --glass 765,954,14,17 --glass 653,965,13,15 --roi 450,960,941,1050 --roi 0,700,200,1000
run s15 --glass 44,447,26,39 --glass 130,585,16,25 --glass 190,667,11,14 --glass 841,691,14,19 --roi 790,680,941,790 --roi 0,600,200,800
