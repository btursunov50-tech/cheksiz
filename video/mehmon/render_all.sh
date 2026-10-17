#!/usr/bin/env bash
# Rebuild all three language versions from seg*.mp4 (segs.txt), cuts.txt, sub_*.ass, avq_*.png, mixI.wav
set -e
cd "$(dirname "$0")"
ENC="-c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p -r 30 -an"
AY=/tmp/claude-0/-home-user-cheksiz/2a2cb10c-3170-5137-84c1-a19971a38055/scratchpad/aytilmagan
ffmpeg -v error -y -f concat -safe 0 -i segs.txt -c copy raw.mp4
/home/user/cheksiz/video/cine.sh raw.mp4 cine.mp4 "$(cat cuts.txt)"
/home/user/cheksiz/video/sfx.sh voice_d.wav vsfx.wav "$(cat cuts.txt)"
mkdir -p send
for L in uz en ru; do
  ffmpeg -v error -y -i cine.mp4 -vf "ass=sub_$L.ass,format=yuv420p" -t 126.86 $ENC main_$L.mp4
  ffmpeg -v error -y -i /home/user/cheksiz/video/avatar.mp4 -i avq_$L.png -filter_complex "[0:v]trim=0:3,setpts=PTS-STARTPTS,scale=1080:1920:flags=lanczos,fps=30,setsar=1[a];[a][1:v]overlay=0:1200:enable='gte(t,0.3)'[v]" -map "[v]" $ENC av_$L.mp4
  printf "file 'main_$L.mp4'\nfile 'av_$L.mp4'\nfile '$AY/end_$L.mp4'\n" > lf_$L.txt
  ffmpeg -v error -y -f concat -safe 0 -i lf_$L.txt -c copy allv_$L.mp4
done
echo built
