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
  1. [Disclaimer](https://owncast.online/docs/scaling/#disclaimer)
  2. [Video](https://owncast.online/docs/scaling/#video)
    1. [Object Storage](https://owncast.online/docs/scaling/#object-storage)
    2. [Content Delivery Networks (CDNs)](https://owncast.online/docs/scaling/#content-delivery-networks-cdns)
  3. [Chat](https://owncast.online/docs/scaling/#chat)


# Scaling Owncast
## Disclaimer[#](https://owncast.online/docs/scaling/#disclaimer)
Owncast works great out of the box as a personal streaming service. The ease of install and all-in-one architecture allows for people to get up and running quickly. The downside of this is it requires a bit more thought around large deployments, as you can’t just run more copies of Owncast for scale.
If you are not familiar with the topics below, or you don’t feel comfortable with the following steps it’s unlikely you should be taking on the additional responsibility of a larger deployment of any service. **Basic system administration experience and understanding of the architecture is generally expected when trying to squeeze additional performance out of anything** , and this might not be for you. Don’t feel bad. **Owncast will still work great for you out of the box** , but you might want to acquire some professional help if you need something more than that.
## Video[#](https://owncast.online/docs/scaling/#video)
### Object Storage[#](https://owncast.online/docs/scaling/#object-storage)
The first step for scaling your video to a large number of concurrent viewers is to use the built-in support for [external storage services](https://owncast.online/docs/storage).
If the core problem is your server isn’t able to handle your number of viewers you can take advantage of 3rd party object storage providers so your viewers will download the video from there instead of your server. This means if you have 1 or 1000 viewers the video video traffic from your server will be exactly the same. Keep in mind each viewer will still be accessing your server directly for chat.
This allows you to generate the video on your Owncast server, but serve it from a provider who has unlimited bandwidth and capacity at a low cost.
With this setup you don’t need extra CPU or a more powerful server in order to support more viewers, as they don’t technically touch your server once the video begins.
[Read more about configuring external storage with Owncast](https://owncast.online/docs/storage).
### Content Delivery Networks (CDNs)[#](https://owncast.online/docs/scaling/#content-delivery-networks-cdns)
To support more people all around the world a CDN (content delivery network) is generally the next step. Putting a CDN in front of your video allows your video to be distributed by servers that are geographically closer to the viewer.
[Read more about using a CDN with Owncast](https://owncast.online/docs/cdns).
## Chat[#](https://owncast.online/docs/scaling/#chat)
When scaling chat you’re limited by what your single server will be able to handle as far as open connections. For most people the standard configuration is likely going to suffice, as it’s been tested to thousands of concurrent clients.
Owncast will automatically increase the amount of concurrent sockets that your operating system will allow. However, if you still get the `too many open files` error it’s because your `ulimit` value is lower than the number of open resources Owncast is trying to to use. You will want to have a more powerful server (cpu, ram) when raising the max limit and handle more chat connections.
You can increase concurrent connections by using the `ulimit` command or editing your system files. 
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