[![](https://owncast.online/images/logo.svg) Owncast](https://owncast.online/)
  * [Quickstart](https://owncast.online/quickstart/)
  * [Docs](https://owncast.online/docs/)
  * [Releases](https://owncast.online/releases)
  * [Troubleshoot](https://owncast.online/troubleshoot)
  * [Directory](https://directory.owncast.online)
  * [Shop](https://merch.owncast.online)


### Broadcasting Software
  * [OBS/Streamlabs OBS](https://owncast.online/docs/broadcasting/obs/)
  * [Restream.io](https://owncast.online/docs/broadcasting/restream/)
  * [Zoom](https://owncast.online/docs/broadcasting/zoom/)
  * [Ffmpeg](https://owncast.online/docs/broadcasting/ffmpeg/)
  * [Compatible Hardware](https://owncast.online/docs/broadcasting/hardware/)
  * [Jitsi](https://owncast.online/docs/broadcasting/jitsi/)


### [← Documentation](https://owncast.online/docs/ "Documentation")
### On this page
  1. [Compatibility](https://owncast.online/docs/broadcasting/#compatibility)
  2. [Pointing your software to Owncast](https://owncast.online/docs/broadcasting/#pointing-your-software-to-owncast)
  3. [How you configure your broadcasting software matters](https://owncast.online/docs/broadcasting/#how-you-configure-your-broadcasting-software-matters)
  4. [Broadcasting Settings](https://owncast.online/docs/broadcasting/#broadcasting-settings)
    1. [Video resolution and quality](https://owncast.online/docs/broadcasting/#video-resolution-and-quality)
    2. [Resolution and Frame rate](https://owncast.online/docs/broadcasting/#resolution-and-frame-rate)
    3. [Bitrate](https://owncast.online/docs/broadcasting/#bitrate)
    4. [Keyframe Interval](https://owncast.online/docs/broadcasting/#keyframe-interval)
    5. [Audio settings](https://owncast.online/docs/broadcasting/#audio-settings)
    6. [Audio bitrate and quality](https://owncast.online/docs/broadcasting/#audio-bitrate-and-quality)
  5. [Dropping frames](https://owncast.online/docs/broadcasting/#dropping-frames)
  6. [Errors or disconnections](https://owncast.online/docs/broadcasting/#errors-or-disconnections)


# Broadcasting Software
## Compatibility
In general Owncast is compatible with any software that uses `RTMP` to broadcast to a remote server. `RTMP` is what all the major live streaming services use, so if you’re currently using one of those it’s likely that you can point your existing software at your Owncast instance instead.
However, we haven’t tested with everything. So if you’re using something specific
## Pointing your software to Owncast
Most broadcasting software will have a way to specify a “custom” location as a RTMP endpoint. In this case you would specify `rtmp://yourserver/live` as the RTMP destination, specifying your streaming key where it asks for it. The default stream key is `abc123` but you should change this immediately after setting up Owncast.
If your software doesn’t have a place to specify a streaming key you can simply append it to your RTMP location, for example: `rtmp://yourserver/live/abc123`.
## How you configure your broadcasting software matters
You will want to configure your broadcasting software to match the highest quality you can offer your viewers. **That means if your Owncast server can only handle 720p@2500k you should not configure your broadcasting software to send 1080p@6000k**. The more conversion work you ask Owncast to do the more resources it will use on your server, making it even harder to offer the best qualities to your viewers.
Every server, environment, network speed and processing capacity is different. Just because you _want_ to offer a certain quality doesn’t mean your server can support it.
If you find yourself trying to squeeze better performance out of Owncast then try setting your broadcasting software to a lower quality as well as lowering the quality in your Owncast instance.
## Broadcasting Settings
The following are some suggested settings for a high quality stream you can set in your broadcasting software. But you should keep in mind the highest quality you’ll be offering your viewers, as stated above. Continue to read more about the values.
### Video resolution and quality
Resolution | Framerate | Bitrate
---|---|---
1920x1080 | 60fps | 5000k
1920x1080 | 30fps | 4500k
1280x720 | 60fps | 4000k
1280x720 | 30fps | 3000k
### Resolution and Frame rate
Resolution refers to the size of a video on a screen, and frame rate refers to how many frames per second are displayed. Full HD resolution is typically 1080p, 60 frames per second (fps). Streaming at a higher resolution like 1080p requires a higher bitrate, and a higher frame rate takes more encoding power. If you have the bandwidth and encoding power both on your broadcasting computer and your Owncast server to stream at 1080p, 60 fps, great! If not, try one of the other settings above to optimize your video quality and stability.
### Bitrate
The bitrate is the amount of data you send to your Owncast server when you stream. A higher bitrate takes up more of your available internet bandwidth. Increasing your bitrate can improve your video quality, but only up to a certain point.
### Keyframe Interval
It is suggested you set your broadcasting software keyframe setting at _2_ and **not** at `auto`.
### Audio settings
Set your broadcasting software to send Owncast `AAC` audio.
### Audio bitrate and quality
When streaming also make sure to match your audio quality to what you’re streaming. If you’re a music focused stream then maybe go higher. If you’re just talking, then maybe you can afford to go lower.
Owncast will not re-encode audio, so it will go out exactly how it’s sent.
Quality | Bitrate
---|---
Low | 96kbps
Medium | 128kpbs
High | 192kbps
Higher | 256kbps
Highest | 320kbps
## Dropping frames
Read more about troubleshooting [Dropped frames](https://owncast.online/troubleshoot/dropped-frames) being reported in your broadcasting software.
## Errors or disconnections
Make sure your broadcasting computer is broadcasting live video reliably. If your own computer or network connection is having a hard time getting video to the internet then viewers will be stuck in a buffering state. Reduce the bitrate, resolution and/or framerate in your broadcasting software on broadcasting device if needed.
Take note of any dropped frames and investigate what’s causing those drops. Is it your local CPU or GPU? Is it your local network? Or is it the Owncast server dropping them due to hardware usage?
If, for example, your
[OBS/Streamlabs OBS →](https://owncast.online/docs/broadcasting/obs/)
OBS is a popular piece of free software for live streaming.
[Restream.io →](https://owncast.online/docs/broadcasting/restream/)
Restream is a commercial service to stream to multiple locations at once.
[Zoom →](https://owncast.online/docs/broadcasting/zoom/)
Zoom is a video conferencing provider.
[Ffmpeg →](https://owncast.online/docs/broadcasting/ffmpeg/)
ffmpeg is a leading command line tool for processing video.
[Compatible Hardware →](https://owncast.online/docs/broadcasting/hardware/)
Various pieces of hardware have been tested with Owncast.
[Jitsi →](https://owncast.online/docs/broadcasting/jitsi/)
Jitsi is an open source video conferencing provider.
  * [About](https://owncast.online/about)
  * [FAQ](https://owncast.online/faq)
  * [Videos](https://videos.owncast.online)
  * [Directory](https://directory.owncast.online)
  * [Merch Store](https://merch.owncast.online)
  * [Newsletter](https://owncast.online/newsletter)
  * [Roadmap](https://owncast.online/roadmap)
  * [Code of Conduct](https://owncast.online/contribute)
  * [Trademark](https://owncast.online/trademark)


  * [Contact](https://owncast.online/contact)
  * [Fediverse](https://social.owncast.online/@owncast)

![](https://owncast.online/images/logo.svg)
Recaptcha requires verification.
-
protected by **reCAPTCHA**
-
