#!/usr/bin/env bash
# Adds a soft "whoosh" that rises into each scene cut and a low "boom" on the cut.
# Usage: video/sfx.sh in.wav out.wav "4.8 6.6 12.4"   (same cut times as cine.sh)
set -euo pipefail
IN=$1; OUT=$2; read -r -a CUTS <<< "${3:-}"
args=(-i "$IN"); fc=""; mix="[0:a]"; n=1
for c in "${CUTS[@]}"; do
  w=$(awk "BEGIN{printf \"%d\", ($c-0.45)*1000}"); b=$(awk "BEGIN{printf \"%d\", $c*1000}")
  args+=(-f lavfi -t 0.7 -i "anoisesrc=c=pink:a=0.9,highpass=f=400,lowpass=f=5000,afade=t=in:d=0.45:curve=exp,afade=t=out:st=0.45:d=0.25")
  args+=(-f lavfi -t 0.9 -i "sine=f=48,afade=t=out:st=0.05:d=0.85,volume=2.2")
  fc+="[$n:a]adelay=$w|$w,volume=0.3[w$n];[$((n+1)):a]adelay=$b|$b,volume=0.7[b$n];"
  mix+="[w$n][b$n]"; n=$((n+2))
done
ffmpeg -v error -y "${args[@]}" -filter_complex "${fc}${mix}amix=inputs=$n:normalize=0,alimiter=limit=0.95[a]" -map "[a]" "$OUT"
