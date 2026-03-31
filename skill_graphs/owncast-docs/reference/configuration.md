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
  1. [Web site details](https://owncast.online/docs/configuration/#web-site-details)
  2. [Video output](https://owncast.online/docs/configuration/#video-output)
  3. [Custom Ports](https://owncast.online/docs/configuration/#custom-ports)
  4. [External storage providers](https://owncast.online/docs/configuration/#external-storage-providers)


# Configuration
Configuration is done through the Owncast administration page located on your server under `/admin`.
**Admin Authentication:**
  * **Username:** `admin`
  * **Password:** your admin password (not your stream key)


The default admin password is `abc123`.
**Note:** Your stream key is only used by your streaming software to publish video; it is not your admin password.
**It’s highly encouraged to change both your stream key and your admin passwords immediately after installation by visiting`/admin/config/server/`**
Some common items many people would want to update after installing Owncast are:
  * Your site name, logo, description and external links that are displayed on the [web site](https://owncast.online/docs/website).
  * The **stream key** to gain access to broadcasting to your stream and your admin.
  * Enable your stream to show up in the [Owncast Directory](https://owncast.online/docs/directory).


## Web site details[#](https://owncast.online/docs/configuration/#web-site-details)
Your site name, logo, description, and page content can be set in the admin. You can also add links to your social profiles and web sites that exist elsewhere. [See details about the web site and chat interface](https://owncast.online/docs/website). Changing page settings in the admin panel was first supported in 
![Owncast general settings](https://owncast.online/docs/img/admin-general-settings.png)
Owncast general settings
## Video output[#](https://owncast.online/docs/configuration/#video-output)
Depending on your hardware you may be able to configure your server to support multiple output variants for multiple different viewing conditions. [Learn how to configure your video and see how it directly effects your CPU usage](https://owncast.online/docs/encoding).
![Owncast video settings](https://owncast.online/docs/img/admin-config-video-variant.png)
Owncast video settings
Changing video settings in the admin panel was first supported in 
## Custom Ports[#](https://owncast.online/docs/configuration/#custom-ports)
Per default, Owncast will run a `http` web server on port `8080` and a RTMP server on port `1935`. You can change the ports in the the admin. You must restart Owncast for these changes to take effect.
You can also set the port for the web server on the command line via the `-webserverport` flag.
![Owncast server settings](https://owncast.online/docs/img/admin-server-settings.png)
Owncast server settings
Custom ports was first supported in Port settings in the admin panel was first supported in 
## External storage providers[#](https://owncast.online/docs/configuration/#external-storage-providers)
Instead of serving video directly from your personal server you can use a S3 compatible storage provider to offload the bandwidth and storage requirements elsewhere. [See how to configure the storage provider of your choice](https://owncast.online/docs/storage).
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