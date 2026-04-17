[![](https://owncast.online/images/logo.svg) Owncast](https://owncast.online/)
  * [Quickstart](https://owncast.online/quickstart/)
  * [Docs](https://owncast.online/docs/)
  * [Releases](https://owncast.online/releases)
  * [Troubleshoot](https://owncast.online/troubleshoot)
  * [Directory](https://directory.owncast.online)
  * [Shop](https://merch.owncast.online)


### chat
  * [Chat authentication](https://owncast.online/docs/chat/chat-authentication/)
  * [Chat moderation](https://owncast.online/docs/chat/moderation/)
  * [Custom emoji](https://owncast.online/docs/chat/emoji/)


### configure
  * [Configuration](https://owncast.online/docs/configuration/)
  * [Web Site + Chat](https://owncast.online/docs/website/)
  * [Video](https://owncast.online/docs/video/)
  * [Object Storage](https://owncast.online/docs/storage/)
  * [The Directory](https://owncast.online/docs/directory/)


### guides
  * [Installation](https://owncast.online/quickstart/installation/)
  * [SSL & HTTP Proxies](https://owncast.online/docs/sslproxies/)
  * [Content Delivery Networks (CDNs)](https://owncast.online/docs/cdns/)
  * [Embedding into your site](https://owncast.online/docs/embed/)
  * [Host public assets](https://owncast.online/docs/custom-assets/)
  * [Live stream notifications](https://owncast.online/docs/notifications/)
  * [Resources and requirements](https://owncast.online/docs/resources-requirements/)
  * [Run as a system service](https://owncast.online/docs/systemservice/)
  * [Social features](https://owncast.online/docs/social/)
  * [Stream Keys](https://owncast.online/docs/stream-keys/)
  * [Stream performance](https://owncast.online/docs/metrics/)
  * [Codecs & Hardware Acceleration](https://owncast.online/docs/codecs/)
  * [Scaling Owncast](https://owncast.online/docs/scaling/)
  * [Backups](https://owncast.online/docs/backups/)
  * [Adding custom Javascript](https://owncast.online/docs/custom-javascript/)
  * [Customizing appearance](https://owncast.online/docs/appearance/)
  * [Troubleshoot Common Problems](https://owncast.online/troubleshoot/)


### integrations
  * [Broadcasting Software](https://owncast.online/docs/broadcasting/)
  * [Build on top of Owncast](https://owncast.online/thirdparty/)
  * [API Documentation](https://owncast.online/docs/api/)


### On this page
  1. [Overview](https://owncast.online/docs/video/#overview)
  2. [Your stream can be played outside of your web site.](https://owncast.online/docs/video/#your-stream-can-be-played-outside-of-your-web-site)
  3. [How does an Owncast video stream work?](https://owncast.online/docs/video/#how-does-an-owncast-video-stream-work)
    1.       1. [Things to keep in mind.](https://owncast.online/docs/video/#things-to-keep-in-mind)
  4. [Things you can configure](https://owncast.online/docs/video/#things-you-can-configure)
    1. [Bitrate](https://owncast.online/docs/video/#bitrate)
    2. [Resolution](https://owncast.online/docs/video/#resolution)
    3. [Framerate](https://owncast.online/docs/video/#framerate)
    4. [CPU Usage](https://owncast.online/docs/video/#cpu-usage)
    5. [Latency Buffer](https://owncast.online/docs/video/#latency-buffer)
    6. [Player Lower Latency Mode](https://owncast.online/docs/video/#player-lower-latency-mode)
    7. [Video Passthrough](https://owncast.online/docs/video/#video-passthrough)
  5. [Audio](https://owncast.online/docs/video/#audio)
  6. [How you configure your broadcasting software matters.](https://owncast.online/docs/video/#how-you-configure-your-broadcasting-software-matters)
  7. [Hardware accelerated video encoding](https://owncast.online/docs/video/#hardware-accelerated-video-encoding)
  8. [Resource and requirement examples](https://owncast.online/docs/video/#resource-and-requirement-examples)


# Video
This document aims to outline what is being done to your content and the different knobs you can tweak to get the best output for your instance.
To see how your specific stream is performing, visit the [Stream Health](https://owncast.online/docs/metrics) page in the admin.
💡
Keep in mind it's hard to give specific settings that will give you the best quality and performance with Owncast because people have different servers and requirements.
## Overview[#](https://owncast.online/docs/video/#overview)
  1. Configure your broadcasting software to send a stream to Owncast that is reasonably close to what you expect to send to your viewers. [How you configure your broadcasting software matters](https://owncast.online/docs/video/#how-you-configure-your-broadcasting-software-matters). Don’t tell OBS to send to Owncast at 7000k at 60fps if you only expect to support bitrates of 4000k and 2000k at 30fps.
  2. Start with a single [output configuration](https://owncast.online/docs/video/#things-you-can-configure) with average settings. Test it. See how your hardware handles it. If you want to, and are able to, then add another and test that. Repeat until you arrive at the configuration you want to offer your viewers and that your hardware can handle.
  3. If your hardware can’t handle your current configuration then reduce the number of output variants to only a single one, [reduce the quality of video you’re sending to Owncast](https://owncast.online/docs/video/#how-you-configure-your-broadcasting-software-matters), reduce your [framerate](https://owncast.online/docs/video/#framerate), and reduce the [CPU usage](https://owncast.online/docs/video/#cpu-usage)


## Your stream can be played outside of your web site.[#](https://owncast.online/docs/video/#your-stream-can-be-played-outside-of-your-web-site)
Because Owncast uses the HLS standard, almost any video player can play your stream. You can also build your own app that plays it. Commonly used video player such as Quicktime, VLC, and mpv can play your stream simply by using its base URL as `https://owncast.mydomain.com`. Alternatively, you can also access your stream directly on your server by putting the path of `/hls/stream.m3u8` into your player. For example: `https://owncast.mydomain.com/hls/stream.m3u8`.
## How does an Owncast video stream work?[#](https://owncast.online/docs/video/#how-does-an-owncast-video-stream-work)
Owncast takes your source stream and converts it to short, individual video segments. A list of these segments is supplied to your viewer’s player and will read and play all the segments in order. This is using a specification called
This video from Jon Dahl is gives a very good overview of internet video, starting with _“what happens when you press play in your web browser?”_ and touching on every piece of the stack, backend and frontend. It translates very well to how Owncast works and is suggested if you want to learn more.
In this case Owncast works as the Media encoder, Stream segmenter, and distribution web server. However [Owncast supports video being distributed via 3rd party storage as well](https://owncast.online/docs/storage), so in that case the video segments would be distributed from there, instead.
![](https://docs-assets.developer.apple.com/published/88e87744a3/de18e941-81de-482f-843d-834a4dd3aa71.png)
#### Things to keep in mind.[#](https://owncast.online/docs/video/#things-to-keep-in-mind)
  1. The more work you need done to convert the video from one size, quality or format to another the more it will slow everything else down.
  2. The slower things go the slower the stream is provided to the user.
  3. If stream is provided to the user too slowly they’ll start seeing buffering and errors.


Here’s what knobs can be tweaked when trying to determine the quality or qualities you want to provide your user while balancing the amount of server resources you’re consuming.
## Things you can configure[#](https://owncast.online/docs/video/#things-you-can-configure)
### Bitrate[#](https://owncast.online/docs/video/#bitrate)
The bitrate is the amount of data you send when you stream. A higher bitrate takes up more available internet bandwidth and create larger sized segments of video, making it take longer for viewers to download. Increasing your bitrate can improve your video quality, but only up to a certain point.
### Resolution[#](https://owncast.online/docs/video/#resolution)
Resolution refers to the size of a video on a screen. Like bitrates you can provide multiple different sizes for different cases, but asking to resize a video amounts in additional work that needs to be performed.
It’s recommended if you have to change the size to only change the width **or** the height, and it’ll keep the correct aspect ratio for you. If you change both the width and the height you may be changing the aspect ratio of the video you may end up with a squished picture if you don’t set it correctly.
### Framerate[#](https://owncast.online/docs/video/#framerate)
Framerate is the number of frames per second in the video. Owncast defaults to 24fps, but other common framerates are 30 or 60. Increasing the framerate will use more CPU on your server, and more bandwidth for your users as more frames of video have to be processed and made available to your viewers any given second.
### CPU Usage[#](https://owncast.online/docs/video/#cpu-usage)
The more CPU you use the better the output image will be, or the smaller of a file the output will be for the same quality. However, you will need to balance the amount of CPU you have available with the amount you can use to process video.
If your hardware is being maxed out then your video may not be processed and delivered fast enough to keep up with the real-time requirements of live video.
Each stream output quality adds significant CPU usage and slows down the overall generation of video segments. It’s generally advised to start with one output, and then add additional, one at a time, to see how it impacts your CPU usage.
If your CPU is being over-utilized, here are some steps you can try taking to resolve this.
  1. You may have too many video outputs defined in your settings. Try limiting yourself to a single output, and go from there.
  2. Change your settings to use [less cpu](https://owncast.online/docs/encoding/#cpu-usage).
  3. Experiment with reducing the bitrate and framerate of your video.
  4. If you’ve gone down to a single output, changed to using less cpu, and experimented with different qualities in your broadcasting software, it’s possible the server you’re running Owncast is just not powerful enough for the task and you might need to try a different environment to run this on.
  5. For your highest quality, match your Owncast server output bitrate exactly to what your broadcasting software is sending to minimize the amount of work your server has to do.
  6. If you find you cannot accomplish encoding of any sort due to your server hardware, you may want to experiment with enabling [video passthrough](https://owncast.online/docs/video/#video-passthrough), where your video is not re-encoded. However, this may not be a solution in all environments and there are often side effects. [Read more](https://owncast.online/docs/video/#video-passthrough).


In general, the easiest way to save CPU is to decrease the input size, decrease the output size, or both.
One easy optimization for CPU usage is to make sure your inbound video matches your highest output quality.
The highest bitrate, resolution and framerate quality you have configured in Owncast to offer your viewers should match what you’re sending Owncast in your broadcasting software to reduce the amount of extra CPU work it needs to do. Start with your highest quality matching your broadcasting software and then go from there. Lower qualities, of course, should be offered for people with slower network connections or are geographically distant.
### Latency Buffer[#](https://owncast.online/docs/video/#latency-buffer)
You have some control over the live latency between the broadcaster and the viewer. While it’s completely understandable to want to have as little latency as possible you may need to increase the latency buffer if you’re experiencing issues. In general the lower the latency the less buffer is available for any possible slow transfers, network blips or errors.
💡
If you require real-time, video conferencing style latency you may want to look for a different solution that doesn't use HLS video, as this scaling and distribution model will never get to sub-second levels.
### Player Lower Latency Mode[#](https://owncast.online/docs/video/#player-lower-latency-mode)
For some browsers, a “Lower latency” option is available in the web player. This should be seen as an experimental feature that will improve over time. If you turn it on and experience a negative playback experience with increased buffering you will probably want to turn it off.
Experimental player lower latency mode was first supported in
### Video Passthrough[#](https://owncast.online/docs/video/#video-passthrough)
💡
Turning on video passthrough may make your stream unplayable or unreliable, and is not recommended. Read about Video Passthrough before turning it on and learn about the risks involved.
**Note: This is generally not recommended and can often cause playback issues for your viewers.**
This is an advanced setting that most people should not use.
Owncast has an optional setting to turn off re-encoding of your inbound stream, potentially saving substantial hardware utilization and supporting a higher quality stream with less resources. **However** , because your video will not be re-encoded it’s possible that certain video from certain sources may end up **not being playable at all**. This is the risk of enabling this.
To enable, visit the advanced settings for a specific stream output. You can turn on “Video Passthrough”.
  1. Turn it on if you require it.
  2. Test it.
  3. If your video won’t play, **then turn it off**.
  4. Only one output should be set as “passthrough”.


Because enabling Passthrough tells Owncast to not encode your video at all, your stream is at the mercy of what your broadcasting software is sending, and that is often not highly compatible with live streaming. For example your live latency may be substantially higher than expected because the stream is not able to be broken up into the specifically sized chunks, as expected. This can also cause issues when switching between different video qualities. For example, switching between a passthrough quality and an properly encoded quality. Worst case your stream may not be playable at all with passthrough enabled.
**Drawback** : Passthrough bypasses the Owncast video encoding pipeline, leading to video that is not processed for live streaming. This can lead to unexpected results **including longer than expected latency** , skips or “blips” in video playback. Or worst case, the video is not playable at all. **This setting is not encouraged.**
## Audio[#](https://owncast.online/docs/video/#audio)
What you’re sending from your broadcasting software is generally reasonable and additional conversion isn’t required, even for low-bandwidth viewers. Owncast will not change the audio stream and instead just pass it along to the end users to save additional work being performed.
## How you configure your broadcasting software matters.[#](https://owncast.online/docs/video/#how-you-configure-your-broadcasting-software-matters)
You will want to configure your broadcasting software to match the highest quality you can offer your viewers. **That means if your Owncast server can only handle 720p@2500k you should not configure your broadcasting software to send 1080p@6000k**. The more conversion work you ask Owncast to do the more resources it will use on your server, making it even harder to offer the best qualities to your viewers.
If you find yourself trying to squeeze better performance out of Owncast then try setting your broadcasting software to a lower quality as well as lowering the quality in your Owncast instance.
Read more about [configuring your broadcasting software](https://owncast.online/docs/broadcasting/).
## Hardware accelerated video encoding[#](https://owncast.online/docs/video/#hardware-accelerated-video-encoding)
If you are running on physical hardware you may be able to increase the performance of your Owncast instance by using your hardware along with a compatible codec, taking the heavy load off of your CPU. There is no guarantee all hardware configurations, drivers or operating systems will work and it may take some effort on your part to install all of the additional software required to get it working. Read more about what is supported, and how, at our [hardware accelerated encoding with additional codecs](https://owncast.online/docs/codecs) document.
## Resource and requirement examples[#](https://owncast.online/docs/video/#resource-and-requirement-examples)
Visit the [resources and requirements](https://owncast.online/docs/resources-requirements/) page to see some examples of what you can expect from your server hardware and network connection and how it may affect your viewers.
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
