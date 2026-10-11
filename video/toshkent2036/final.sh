#!/usr/bin/env bash
# final.sh LANG [music.mp3 start_sec]  -> out_LANG.mp4 (main 47.4 s + avatar 3 s + end card 4 s)
set -e
L=$1; M=${2:-}; MS=${3:-0}
CUTS=$(cat cuts.txt); TOT=54.4
ENC="-c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p -r 30 -an"
ffmpeg -v error -y -t 47.4 -i seg/cine.mp4 -vf "ass=sub_$L.ass,format=yuv420p" $ENC seg/main_$L.mp4
printf "file 'main_$L.mp4'\nfile '../av_$L.mp4'\nfile '../end_$L.mp4'\n" > seg/l_$L.txt
ffmpeg -v error -y -f concat -safe 0 -i seg/l_$L.txt -c copy seg/v_$L.mp4
# voice (loudnorm) padded to full length
ffmpeg -v error -y -i src/voice.wav -af "aresample=48000,loudnorm=I=-14:TP=-1.5,apad" -t $TOT -ac 2 seg/voice.wav
if [ -n "$M" ]; then
  ffmpeg -v error -y -i seg/voice.wav -ss $MS -i "$M" -filter_complex "[0:a]asplit=2[v][sc];[1:a]aresample=48000,volume=0.55,afade=t=in:d=0.6,afade=t=out:st=$(echo "$TOT-3" | bc):d=3[m];[m][sc]sidechaincompress=threshold=0.03:ratio=4:attack=15:release=350[md];[v][md]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95" -t $TOT seg/mix0.wav
else cp seg/voice.wav seg/mix0.wav; fi
/home/user/cheksiz/video/sfx.sh seg/mix0.wav seg/mix.wav "$CUTS"
ffmpeg -v error -y -i seg/v_$L.mp4 -i seg/mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 160k -t $TOT -movflags +faststart out_$L.mp4
echo done $L
