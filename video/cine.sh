#!/usr/bin/env bash
# Soft cinematic look for a 1080x1920 base video (apply before subtitles, so they stay sharp):
# slow zoom that restarts at each scene cut, soft teal/orange grade, light vignette and grain,
# thin black bars at the top and bottom.
# Usage: video/cine.sh in.mp4 out.mp4 "4.8 6.6 12.4"   (scene cut times in seconds; may be empty)
set -euo pipefail
IN=$1; OUT=$2; read -r -a CUTS <<< "${3:-}"
starts=(0 "${CUTS[@]}")
# Seconds since the current scene started.
expr="t-${starts[-1]}"
for ((i=${#starts[@]}-2; i>=0; i--)); do expr="if(lt(t,${starts[i+1]}),t-${starts[i]},$expr)"; done
Z="(1.02+0.012*($expr))"
ffmpeg -v error -y -i "$IN" -vf "\
scale=w='trunc(1080*$Z/2)*2':h='trunc(1920*$Z/2)*2':eval=frame:flags=bicubic,crop=1080:1920,\
eq=contrast=1.06:saturation=1.06:gamma=0.98,\
colorbalance=rs=-0.035:bs=0.04:rh=0.04:gh=0.01:bh=-0.035,\
vignette=angle=PI/5.5,noise=alls=4:allf=t,\
drawbox=x=0:y=0:w=1080:h=96:color=black:t=fill,drawbox=x=0:y=1824:w=1080:h=96:color=black:t=fill,\
setsar=1,format=yuv420p" -c:v libx264 -preset medium -crf 20 -r 30 -an "$OUT"
