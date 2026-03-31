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
  1. [Base knowledge](https://owncast.online/docs/resources-requirements/#base-knowledge)
    1. [Viewer count does not impact CPU use](https://owncast.online/docs/resources-requirements/#viewer-count-does-not-impact-cpu-use)
  2. [Example Scenario](https://owncast.online/docs/resources-requirements/#example-scenario)
    1. [Offer a high and low quality option](https://owncast.online/docs/resources-requirements/#offer-a-high-and-low-quality-option)
    2. [Offer a single high quality option using the least amount of CPU](https://owncast.online/docs/resources-requirements/#offer-a-single-high-quality-option-using-the-least-amount-of-cpu)
    3. [Use a S3 compatible storage provider for bandwidth](https://owncast.online/docs/resources-requirements/#use-a-s3-compatible-storage-provider-for-bandwidth)
  3. [Summarized FAQ](https://owncast.online/docs/resources-requirements/#summarized-faq)
    1. [How much bandwidth will Owncast use?](https://owncast.online/docs/resources-requirements/#how-much-bandwidth-will-owncast-use)
    2. [How much CPU will Owncast use?](https://owncast.online/docs/resources-requirements/#how-much-cpu-will-owncast-use)
    3. [Does CPU usage increase with more viewers?](https://owncast.online/docs/resources-requirements/#does-cpu-usage-increase-with-more-viewers)
    4. [How much CPU is used for each output quality?](https://owncast.online/docs/resources-requirements/#how-much-cpu-is-used-for-each-output-quality)
    5. [How does frame rate affect CPU usage?](https://owncast.online/docs/resources-requirements/#how-does-frame-rate-affect-cpu-usage)
    6. [How much disk space will Owncast use?](https://owncast.online/docs/resources-requirements/#how-much-disk-space-will-owncast-use)
    7. [Can I just offer one quality, the highest possible, to lower the CPU requirements? I only want people to see the best quality video, anyway.](https://owncast.online/docs/resources-requirements/#can-i-just-offer-one-quality-the-highest-possible-to-lower-the-cpu-requirements-i-only-want-people-to-see-the-best-quality-video-anyway)
  4. [Learn more](https://owncast.online/docs/resources-requirements/#learn-more)


# Resources and requirements
It’s impossible to give a single answer about what the requirements are for you to run Owncast, or what it will cost. It’s your server, and it’s completely up to you how you choose to configure it, and in what environments you choose to run it. Every environment has different performance, prices and features.
## Base knowledge[#](https://owncast.online/docs/resources-requirements/#base-knowledge)
It’s very helpful for you to understand the basics included in video streaming.
  * CPU: Used to transcode the video to multiple qualities so viewers can watch it on different speed networks.
  * Network bandwidth: Used to distribute the video to your viewers.


### Viewer count does not impact CPU use[#](https://owncast.online/docs/resources-requirements/#viewer-count-does-not-impact-cpu-use)
Knowing this, you see that **CPU usage is the same regardless of how many viewers you have**. 0 or 100, the CPU is still performing the work. Think of it like creating a zip file. If you have a 100MB file, and you zip it, and it becomes 70MB, you can send that 70MB file to as many people as you want without zipping that file again for each person. But you still need to send the file to each person seperately, requiring network bandwidth for each time you send it. However, if you want to send some people a 70MB version and others a 50MB version, you’ll need to create two seperate files. That 50MB version will take longer and use more CPU to create, because of the additional work it takes to compress the file more. This is the same with video. The more work required to encode your video, the more CPU that’s required. Generally, the more you need to reduce the size and bitrate of your video, the more CPU that will be used. But offering low bitrate/lower quality versions of your stream is important to enable more viewers to watch it from across the world, on any kind of network.
Now that you understand the basics, let’s use an example to illustrate how your configuration can impact your server’s resources, and most importantly, your viewers’ experience. It’s a little simplistic and the actual numbers can vary in real life, but it could help answer the question of “approximately how much bandwidth and CPU will Owncast use?”
## Example Scenario[#](https://owncast.online/docs/resources-requirements/#example-scenario)
You’ve configured your broadcasting source (such as OBS) to stream to your Owncast instance at **5000kbps**. You have **25 viewers**. **5** of them are on slow or mobile networks, **17** of them have fast, stable internet, and **3** of them have fast internet most of the time but the speed fluctuates. All 25 viewers watched an entire stream that lasts two hours. You have a hosting provider that gives you 4TB of bandwidth per month.
### Offer a high and low quality option[#](https://owncast.online/docs/resources-requirements/#offer-a-high-and-low-quality-option)
You decide to offer both a high and low quality option, and you set the high quality option to 5000kbps and the low quality option to 1500kbps.
**How much bandwidth is used on your server for this stream?**
Bitrate | Duration | Viewers | Total  
---|---|---|---  
0.000625 Gigabytes per second (5000kbps) | 7200 seconds | 19 | 85 Gigabytes  
0.0001875 Gigabytes per second (1500kbps) | 7200 seconds | 6 | 8.1 Gigabytes  
|  |  |  **Total** : 93.1 Gigabytes  
**How much CPU?**
Quality | CPU Usage  
---|---  
5000kbps | Some (It matches the input)  
1500kbps | More (CPU needs to be used to compress the video)  
**How is the viewer experience?**
Quality | Viewers | Experience  
---|---|---  
5000kbps | 20 | Good  
1500kbps | 5 | Good  
**Result** : You’ve provided both a high and low quality option for your viewers so those with a slow network have an option, and those with a fast network that might periodically slow down can dip down into the low quality when needed. Additionally, in this case you saved almost 20G of bandwidth traffic due to offering a lower quality. You’re using more CPU for a much better experience. You would be able to stream 43 times in a month before you hit your bandwidth limit.
### Offer a single high quality option using the least amount of CPU[#](https://owncast.online/docs/resources-requirements/#offer-a-single-high-quality-option-using-the-least-amount-of-cpu)
You’ve decided you want to use as little CPU on your Owncast server as possible so you enable “Video Passthrough” mode as the only output available. This means the exact video you’re sending from your local broadcasting software is what is sent to your viewers.
**How much bandwidth is used on your server for this stream?**
Bitrate | Duration | Viewers | Total  
---|---|---|---  
0.000625 Gigabytes per second (5000kbps) | 7200 seconds | 25 | 112.5 Gigabytes  
**How much CPU?**
Quality | CPU Usage  
---|---  
5000kbps | Little  
**How is the viewer experience?**
Quality | Viewers | Experience  
---|---|---  
5000kbps | 17 | Good  
5000kbps | 3 | Bad  
5000kbps | 5 | Unwatchable  
**Result** : You’re not using much CPU, but only **65%** of your viewers are having a good experience. The other **35%** are having a bad experience with frequent buffering, and **20%** of them cannot watch your stream at all. You would be able to stream 35 times in a month before you hit your bandwidth limit.
### Use a S3 compatible storage provider for bandwidth[#](https://owncast.online/docs/resources-requirements/#use-a-s3-compatible-storage-provider-for-bandwidth)
If you have concerns about your hosting plan, bandwidth allocation or viewership growth you can use a S3 storage provider instead of your server for bandwidth responsibilities. In this example you again decide to offer both a high and low quality option, and you set the high quality option to 5000kbps and the low quality option to 1500kbps. The CPU used is the same as the above example for the high+low quality option. Learn more about [S3 compatible storage](https://owncast.online/docs/storage).
**How much bandwidth is used on your server for this stream?**
Bitrate | Duration | Total  
---|---|---  
0.000625 Gigabytes per second (5000kbps) | 7200 seconds | 4.5 Gigabytes  
0.0001875 Gigabytes per second (1500kbps) | 7200 seconds | 1.35 Gigabytes  
|  |  **Total** : 5.85 Gigabytes  
**How much outbound bandwidth is used on your S3 provider for this stream?**
Bitrate | Duration | Viewers | Total  
---|---|---|---  
0.000625 Gigabytes per second (5000kbps) | 7200 seconds | 19 | 85 Gigabytes  
0.0001875 Gigabytes per second (1500kbps) | 7200 seconds | 6 | 8.1 Gigabytes  
|  |  |  **Total** : 93.1 Gigabytes  
**Result** : You’ve provided both a high and low quality option for your viewers so those with a slow network have an option, and those with a fast network that might periodically slow down can dip down into the low quality when needed. However, these video qualities are not being served from your Owncast server, but instead an external S3 compatible storage provider. This allows for increasing your viewership and adding additional video qualities without concern of you exhausting your server’s bandwidth allocation. You would be able to stream 24/7 without worry using this configuration, however you’d be using the same amount of your server bandwidth if you had zero viewers or 100 viewers. Your CPU usage would be the same as if you were serving the video directly from your server.
## Summarized FAQ[#](https://owncast.online/docs/resources-requirements/#summarized-faq)
### How much bandwidth will Owncast use?[#](https://owncast.online/docs/resources-requirements/#how-much-bandwidth-will-owncast-use)
It depends on your configuration and how many viewers you have. If you offer more video quality options you will often reduce your network transfer requirements. Look into object storage (S3) to reduce your server’s network requirements.
### How much CPU will Owncast use?[#](https://owncast.online/docs/resources-requirements/#how-much-cpu-will-owncast-use)
It depends on how many different quality output options you are offering your viewers and what those qualities are.
### Does CPU usage increase with more viewers?[#](https://owncast.online/docs/resources-requirements/#does-cpu-usage-increase-with-more-viewers)
Not in a meaningful way. There are limits when you’re talking tens of thousands of chat participants, however.
### How much CPU is used for each output quality?[#](https://owncast.online/docs/resources-requirements/#how-much-cpu-is-used-for-each-output-quality)
It depends on your configuration, but generally if you said one CPU core for each quality you’re offering, that’s a good rule of thumb. But it’s not a hard rule and can be less.
### How does frame rate affect CPU usage?[#](https://owncast.online/docs/resources-requirements/#how-does-frame-rate-affect-cpu-usage)
The fewer frames, the less CPU that is used. If you want to reduce the CPU being used on one of your video qualities you can reduce the frame rate. If you want to reduce the CPU being used for all of Owncast you can reduce the frame rate of your inbound source content in your broadcasting software, such as OBS.
### How much disk space will Owncast use?[#](https://owncast.online/docs/resources-requirements/#how-much-disk-space-will-owncast-use)
Almost none, as the live stream is cleaned up in real-time as you stream.
### Can I just offer one quality, the highest possible, to lower the CPU requirements? I only want people to see the best quality video, anyway.[#](https://owncast.online/docs/resources-requirements/#can-i-just-offer-one-quality-the-highest-possible-to-lower-the-cpu-requirements-i-only-want-people-to-see-the-best-quality-video-anyway)
It’s not about you, your bandwidth, or your CPU. It’s about your viewers. Not everyone can watch the highest quality. If they can’t watch your stream because you didn’t have them in mind then it’s not worth streaming in the first place.
## Learn more[#](https://owncast.online/docs/resources-requirements/#learn-more)
Visit the detailed [video documentation](https://owncast.online/docs/video) to learn more about how Owncast handles video.
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