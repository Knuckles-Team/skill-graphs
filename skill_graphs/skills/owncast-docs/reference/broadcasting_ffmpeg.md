### Broadcasting Software
  * [OBS/Streamlabs OBS](https://owncast.online/docs/broadcasting/obs/)
  * [Restream.io](https://owncast.online/docs/broadcasting/restream/)
  * [Zoom](https://owncast.online/docs/broadcasting/zoom/)
  * [Ffmpeg](https://owncast.online/docs/broadcasting/ffmpeg/)
  * [Compatible Hardware](https://owncast.online/docs/broadcasting/hardware/)
  * [Jitsi](https://owncast.online/docs/broadcasting/jitsi/)


### [← Documentation](https://owncast.online/docs/ "Documentation")
# ffmpeg
Streaming with ffmpeg is quite easy. You can stream any connected webcam or HDMI grabber that appears in `/dev/video*` and incoming alsa audio devices. In this example, the `/dev/video2` video device and the `hw:1,0` alsa audio device are used:
```
ffmpeg -f alsa -ac 2 -i hw:1,0 -thread_queue_size 64 \
  -f v4l2 -framerate 60 -video_size 1280x720 -input_format yuyv422 -i /dev/video2 \
  -c:v libx264 -preset veryfast -b:v 1984k -maxrate 1984k -bufsize 3968k \
  -vf "format=yuv420p" -g 60 -c:a aac -b:a 128k -ar 44100 \
  -f flv rtmp://<ip-of-your-server>/live/<your-streaming-key>
```

Recaptcha requires verification.
-
protected by **reCAPTCHA**
-
