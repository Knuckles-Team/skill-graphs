[![](https://owncast.online/images/logo.svg) Owncast](https://owncast.online/)
  * [Quickstart](https://owncast.online/quickstart/)
  * [Docs](https://owncast.online/docs/)
  * [Releases](https://owncast.online/releases)
  * [Troubleshoot](https://owncast.online/troubleshoot)
  * [Directory](https://directory.owncast.online)
  * [Shop](https://merch.owncast.online)


### SSL & HTTP Proxies
  * [Caddy](https://owncast.online/docs/sslproxies/caddy/)
  * [HAProxy](https://owncast.online/docs/sslproxies/haproxy/)
  * [Lighttpd](https://owncast.online/docs/sslproxies/lighttpd/)
  * [NGINX](https://owncast.online/docs/sslproxies/nginx/)
  * [Apache](https://owncast.online/docs/sslproxies/apache/)


### [← Documentation](https://owncast.online/docs/ "Documentation")
### On this page
  1. [Why you want to support SSL](https://owncast.online/docs/sslproxies/#why-you-want-to-support-ssl)
  2. [When you might not need it](https://owncast.online/docs/sslproxies/#when-you-might-not-need-it)
  3. [Popular options](https://owncast.online/docs/sslproxies/#popular-options)
  4. [Inherit display name from reverse proxy](https://owncast.online/docs/sslproxies/#inherit-display-name-from-reverse-proxy)
  5. [Suggested](https://owncast.online/docs/sslproxies/#suggested)


# SSL & HTTP Proxies
While not required, most people will want to support SSL on a public Owncast server. If you already have a 
💡
People often overlook the need to proxy their websockets, so if you're having issues with chat make sure you configured your proxy to pass those through.
## Why you want to support SSL
  1. If you want to embed your Owncast video or chat into a page that is using SSL your Owncast server will also need to be secured.
  2. Browsers will label your site as 
  3. It looks more professional and your site will come off more trustworthy.
  4. Securing web traffic on the public internet is the right thing to do.


## When you might not need it
  1. If you’re just testing and experimenting with Owncast.
  2. You’re running the service internally and you don’t have any plans for a public audience.


## Popular options
You can use any method you like to add SSL support but there are some popular options we’ve seen work well with people. If you have any specific questions or would like to make suggestions on configurations or other setups [let us know](https://owncast.online/contact).
## Inherit display name from reverse proxy
Owncast usually assigns a random display name when new users are joining the chat. Upstream reverse proxies can influence this behavior by setting a `X-Forwarded-User` HTTP header. This header will be used instead of a random name to derive a user’s display name. A user will still be able to change it’s own display name to any desired value.
Inherit display name from reverse proxy was first supported in 
## Suggested
If you have no requirement to use other options else it is suggested you install [Caddy](https://owncast.online/docs/sslproxies/caddy/) as it can be installed quickly and easily.
[Caddy →](https://owncast.online/docs/sslproxies/caddy/)
Caddy is possibly the fastest way to setup a SSL proxy.
[HAProxy →](https://owncast.online/docs/sslproxies/haproxy/)
HAproxy is a well known performant reverse proxy.
[Lighttpd →](https://owncast.online/docs/sslproxies/lighttpd/)
lighttpd is a lightweight option for SSL proxying.
[NGINX →](https://owncast.online/docs/sslproxies/nginx/)
NGINX is a very popular solution for SSL proxying.
[Apache →](https://owncast.online/docs/sslproxies/apache/)
If you're already using Apache you can use it as a proxy.
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