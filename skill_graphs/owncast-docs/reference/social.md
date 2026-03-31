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
  1. [What it supports](https://owncast.online/docs/social/#what-it-supports)
  2. [Why?](https://owncast.online/docs/social/#why)
  3. [How to enable](https://owncast.online/docs/social/#how-to-enable)
    1. [Requirements](https://owncast.online/docs/social/#requirements)
    2. [Configuration](https://owncast.online/docs/social/#configuration)
    3. [Private mode](https://owncast.online/docs/social/#private-mode)
  4. [How do people follow your Owncast server?](https://owncast.online/docs/social/#how-do-people-follow-your-owncast-server)
  5. [How it works](https://owncast.online/docs/social/#how-it-works)
  6. [Composing messages to your followers](https://owncast.online/docs/social/#composing-messages-to-your-followers)
  7. [Engagement](https://owncast.online/docs/social/#engagement)
  8. [Where to learn more about The Fediverse](https://owncast.online/docs/social/#where-to-learn-more-about-the-fediverse)
    1. [Discover services and sites that make up The Fediverse](https://owncast.online/docs/social/#discover-services-and-sites-that-make-up-the-fediverse)
    2. [Communities discussing The Fediverse](https://owncast.online/docs/social/#communities-discussing-the-fediverse)


# Social features
Owncast allows people to follow, engage with your server, and share your stream with others on what is known as the Fediverse, a decentralized network of services.
Social functionality was first supported in 
## What it supports[#](https://owncast.online/docs/social/#what-it-supports)
  1. People can follow your server.
  2. Your followers show up in the “Followers” tab on your stream’s page.
  3. You can send out posts to your followers via the admin.
  4. Your followers will automatically get notified when you go live.
  5. Your followers can share that you’ve gone live with their circle of followers.
  6. Actions such as following, liking or sharing get exposed within your stream’s chat.


## Why?[#](https://owncast.online/docs/social/#why)
It’s a good way for your audience to get notified when you go live, share it with their circle, and to be highlighted within your page and chat.
## How to enable[#](https://owncast.online/docs/social/#how-to-enable)
This functionality is disabled by default. To enable social features on your Owncast server visit the _Configuration - > Social_ page.
### Requirements[#](https://owncast.online/docs/social/#requirements)
  1. You must be hosting your Owncast server behind SSL, with a _https_ URL. Setup a [HTTP Proxy](https://owncast.online/docs/sslproxies/) if needed.
  2. Once you set your server name and your username that’s how people will see you. If you change either of those two settings you’ll show up as a different user and your existing followers may no longer be following you. It is not suggested you change these after you set them.


### Configuration[#](https://owncast.online/docs/social/#configuration)
Visit the _Configuration - > Social_ page to configure.
  1. You can set the username that you’re seen as.
  2. You can set the text that is sent out each time you go live.
  3. You can toggle “Private mode”.


### Private mode[#](https://owncast.online/docs/social/#private-mode)
Enabling _Private Mode_ will require those who wish to follow your server to be approved by you first. Approving followers can be done via the _Followers_ section in the admin.
Private Mode will also make it so any posts you send out are only visible to your followers, not others, as they cannot be shared.
## How do people follow your Owncast server?[#](https://owncast.online/docs/social/#how-do-people-follow-your-owncast-server)
Any person on the Fediverse using a service that is compatible with following Owncast, such as 
[Learn more about The Fediverse](https://owncast.online/docs/social/#learn-more).
## How it works[#](https://owncast.online/docs/social/#how-it-works)
The Fediverse is an ensemble of decentralized and interconnected servers that are used for social networking, microblogging and more. While each server is independently hosted, they communicate with each other.
Each Owncast instance operates as a completely standalone server with a single user that can take part in the Fediverse, exchanging posts and notifications with any participating user who is interested in them.
Any user on the Fediverse that is on a compatible server can follow any Owncast server that has this feature enabled.
## Composing messages to your followers[#](https://owncast.online/docs/social/#composing-messages-to-your-followers)
By clicking the _Compose_ button in the admin header you can create a post to send to your followers. This could be used to tell people when you plan on streaming, or to remind people that you’re still live.
## Engagement[#](https://owncast.online/docs/social/#engagement)
If somebody **follows** you, **likes** a post you send out, or **shares** any of your posts while a stream is live it will display that these actions took place within the chat feed. This can be disabled under the social settings.
![](https://owncast.online/docs/img/fediverse.svg)
#### The Fediverse
## Where to learn more about The Fediverse[#](https://owncast.online/docs/social/#where-to-learn-more-about-the-fediverse)
A decentralized network of different services built on standards is the future of social networking. Learn more about all the different services that make up The Fediverse and see how, much like Owncast can empower you to operate your own live streams, there are other opportunities to leave the centralized corporate social networking services in the past.
### Discover services and sites that make up The Fediverse[#](https://owncast.online/docs/social/#discover-services-and-sites-that-make-up-the-fediverse)
### Communities discussing The Fediverse[#](https://owncast.online/docs/social/#communities-discussing-the-fediverse)
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