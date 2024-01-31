#!/bin/bash

while true; do
    # Overlay için rastgele video URL'si al
    overlay_data=$(python3 get_overlay_data.py)  
    # FFmpeg ile video akışını başlat
    ffmpeg -i "$overlay_data" -vf "drawtext=text='Overlay Text':fontsize=24:fontcolor=white:x=10:y=10" \
        -c:v libx264 -preset veryfast -maxrate 3000k -bufsize 6000k -pix_fmt yuv420p -g 50 \
        -c:a aac -b:a 160k -ac 2 -ar 44100 -f flv "rtmp://localhost:1935/live/stream_key"
done
