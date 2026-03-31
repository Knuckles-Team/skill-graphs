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
  1. [Browser notifications](https://owncast.online/docs/notifications/#browser-notifications)
    1. [Enabling browser notifications on iOS](https://owncast.online/docs/notifications/#enabling-browser-notifications-on-ios)
    2. [Browser extension](https://owncast.online/docs/notifications/#browser-extension)
  2. [Fediverse](https://owncast.online/docs/notifications/#fediverse)
  3. [Discord](https://owncast.online/docs/notifications/#discord)
  4. [Twitter (deprecated)](https://owncast.online/docs/notifications/#twitter-deprecated)


# Live stream notifications
Some streams benefit from announcing to their audience when they go live.
This is not an endorsement of any particular service, but it may help some streamers integrate into their existing communities.
If you’d like to expand on this and send automated notifications to other destinations, create a custom [webhook](https://owncast.online/thirdparty/webhooks/).
External notification was first supported in 
## Browser notifications[#](https://owncast.online/docs/notifications/#browser-notifications)
Using browser push notifications your viewers can choose to be notified each time you go live.
Not all browser support this feature, and browser that do may handle it differently. Brave Browser, for example, require you to choose the duration the notifications are valid. They will likely want to select “Forever” to keep the notification active.
### Enabling browser notifications on iOS[#](https://owncast.online/docs/notifications/#enabling-browser-notifications-on-ios)
You can request to be notified when a stream goes live on iOS by following these steps:
  1. Open Safari and navigate to your Owncast instance.
  2. Tap the share icon at the bottom of your browser.
  3. Tap “Add to Home Screen”.
  4. Tap the new Owncast icon on your home screen.
  5. Press the “Notify” button.
  6. Tap “Allow” when prompted.


### Browser extension[#](https://owncast.online/docs/notifications/#browser-extension)
Another suggested way to receive browser notifications from any number of streams is by using the 
## Fediverse[#](https://owncast.online/docs/notifications/#fediverse)
The Fediverse social features have built in support to notify your followers when you go live. [Visit the documentation](https://owncast.online/docs/social/) for more information.
## Discord[#](https://owncast.online/docs/notifications/#discord)
You can notify a Discord channel when your stream goes live. Visit the 
  * Visit Edit Channel / Integrations on your Discord channel.
  * Create a webhook.
  * Provide URL in the Owncast configuration.


## Twitter (deprecated)[#](https://owncast.online/docs/notifications/#twitter-deprecated)
Since 
Recaptcha requires verification. 
- 
protected by **reCAPTCHA**
-