#!/bin/bash
# «Olmos»: kadrga yaqin (katta) ko'cha fonuslarining faqat shishasi ko'k neon (egasi, 2026-10-30: «hamma lampochkalarni emas, kadrda yaqin turganini»).
# --glass cx,cy,hw,hh = fonus shishasi ellipsi (941x1672, o'lchangan). Asl rasmlar img/asl/ da.
cd "$(dirname "$0")"; mkdir -p img/asl
run(){ n=$1; shift; [ -f img/asl/$n.png ] || cp img/$n.png img/asl/$n.png; python3 fonus.py img/asl/$n.png img/$n.png --show "${SHOW:-/dev/null}_$n.jpg" "$@"; }
run s02 --glass 72,270,28,34 --glass 80,468,16,20
run s03 --glass 68,272,30,36
run s04 --glass 75,283,30,34 --glass 88,468,16,20
run s07 --glass 70,272,28,32 --glass 70,472,16,20
run s09 --glass 347,210,26,30
run s10 --glass 110,272,15,18
run s11 --glass 90,490,18,22 --glass 155,482,20,24
run s12 --glass 147,530,18,22
run s13 --glass 125,345,15,22 --glass 167,305,15,20
