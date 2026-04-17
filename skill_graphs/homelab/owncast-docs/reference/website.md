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
  1. [Overview](https://owncast.online/docs/website/#overview)
    1. [Name and description](https://owncast.online/docs/website/#name-and-description)
    2. [Tags](https://owncast.online/docs/website/#tags)
    3. [External social links](https://owncast.online/docs/website/#external-social-links)
    4. [Web page content](https://owncast.online/docs/website/#web-page-content)
  2. [Chat](https://owncast.online/docs/website/#chat)
    1. [Text Formatting](https://owncast.online/docs/website/#text-formatting)
    2. [Custom Emoji](https://owncast.online/docs/website/#custom-emoji)
  3. [Player](https://owncast.online/docs/website/#player)
  4. [Custom Styles via CSS](https://owncast.online/docs/website/#custom-styles-via-css)
    1. [Some examples of things you can try.](https://owncast.online/docs/website/#some-examples-of-things-you-can-try)


# Web Site + Chat
## Overview[#](https://owncast.online/docs/website/#overview)
Owncast includes a web interface for your video with built-in chat that is available once you start the server. It shows online/offline states, viewer counts, stream duration, your instance’s description, images, links and more. You can just start using it without making any changes, but you’ll likely want to update the content displayed on your page by visiting your server admin page.
Additionally, the web interface was specifically built to be customizable by anybody comfortable tweaking colors and styles. No development environment is needed, just open the admin and start tweaking.
If you want to embed Owncast in your existing website, checkout our [documentation on embedding Owncast](https://owncast.online/docs/embed/).
Below are some items you’ll likely want to customize to update the content that displays on your page.
Changing settings in the admin panel was first supported in
### Name and description[#](https://owncast.online/docs/website/#name-and-description)
By setting your name, description and logo you can quickly update the contents of the website to reflect your stream.
![Owncast general settings](https://owncast.online/docs/img/admin-general-settings.png)
Owncast general settings
### Tags[#](https://owncast.online/docs/website/#tags)
By setting tags you’re showing potential viewers what categories of content you typically stream.
![Add tags](https://owncast.online/docs/img/admin-settings-tags-social.png)
Add tags
### External social links[#](https://owncast.online/docs/website/#external-social-links)
You can add links to your profiles on other sites by adding them in the admin.
![Add social links](https://owncast.online/docs/img/admin-settings-social-handle.png)
Add social links
### Web page content[#](https://owncast.online/docs/website/#web-page-content)
The body of your page content can be customized in your admin. Use standard
## Chat[#](https://owncast.online/docs/website/#chat)
### Text Formatting[#](https://owncast.online/docs/website/#text-formatting)
The web chat supports some basic formatting using
Italic: `*your text*`
Bold: `**your text**`
Strikethrough: `~~your text~~`
Code blocks: ``your text``
### Custom Emoji[#](https://owncast.online/docs/website/#custom-emoji)
Place your own custom emoji images into `/webroot/img/emoji/` and the next time you refresh the web site you’ll see your images in the emoji picker, available for use in chat.
Emoji was first supported in
## Player[#](https://owncast.online/docs/website/#player)
The web video player has a handful of keyboard shortcuts you can use.
Action | Shortcut
---|---
Play/Pause | _Spacebar_
Volume up | _0_
Volume down | _9_
Mute | _m_
Toggle full screen | _f_
Toggle chat | _c_
Player shortcuts was first supported in
## Custom Styles via CSS[#](https://owncast.online/docs/website/#custom-styles-via-css)
Under the General Settings in the admin you can write your own CSS that will get applied to the web page. There is no validation or sanity checks, so anything you write will get inserted into a `<style>` tag on your page. So if you make a CSS mistake, you may mess something up on your page.
### Some examples of things you can try.[#](https://owncast.online/docs/website/#some-examples-of-things-you-can-try)
  1. Customize your font.
  2. Change text sizes and colors.
  3. Set a new background color.
  4. Completely hide specific things you don’t want or care about.

Custom styles was first supported in
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
