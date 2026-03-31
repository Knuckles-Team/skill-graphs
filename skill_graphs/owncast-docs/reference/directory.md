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
  1. [If your server is not showing up in the directory](https://owncast.online/docs/directory/#if-your-server-is-not-showing-up-in-the-directory)


# The Directory
To help people discover streams by people using Owncast we have an optional Owncast directory you can add yourself to.
  1. Visit the **“General”** settings in the admin.
  2. Set the public URL to your Owncast instance that you want people to be linked to.
  3. Set the **“About”** with a brief description of your stream.
  4. Set the **tags** associated with the content you stream.
  5. Mark if your content is _Not Safe For Work_ (nsfw).


💡
This directory is operated as a complimentary service by the Owncast project to share people's streams. There is no obligation to list any specific server or topic. Any server can be removed at any time for any reason.
## If your server is not showing up in the directory[#](https://owncast.online/docs/directory/#if-your-server-is-not-showing-up-in-the-directory)
  1. It’s opt-in, so make sure you follow the [configuration directions](https://owncast.online/docs/directory) to enable the directory for your server.
  2. It will take approximately 5min for your server to show up the first time you stream after enabling this feature.
  3. You may want to run your server with `owncast --enableVerboseLogging` to see what errors show up.
  4. If you used to be listed, but no longer show up you may need to reset your registration to the server in the admin’s Server Settings.
  5. If you recently changed the URL of your server reset your registration in your Server Settings.
  6. If there’s some issue that’s causing you not to be listed 

Owncast directory was first supported in 
Recaptcha requires verification. 
- 
protected by **reCAPTCHA**
-