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
  1. [SSL](https://owncast.online/docs/sslproxies/lighttpd/#ssl)
  2. [Reverse Proxy](https://owncast.online/docs/sslproxies/lighttpd/#reverse-proxy)


# lighttpd
## SSL[#](https://owncast.online/docs/sslproxies/lighttpd/#ssl)
An implementation of
```
$SERVER["socket"] == "[::]:443" {
ssl.engine = "enable"
ssl.cipher-list = "HIGH"
$HTTP["host"] == "owncast.yourdomain.com" {
ssl.pemfile = "/etc/letsencrypt/live/yourdomain.com/fullchain.pem"
ssl.privkey = "/etc/letsencrypt/live/yourdomain.com/privkey.pem"
ssl.dh-file = "/etc/letsencrypt/ssl-dhparams.pem"
}
}
```

## Reverse Proxy[#](https://owncast.online/docs/sslproxies/lighttpd/#reverse-proxy)
Proxying of incoming websocket connections is integrated with the module.
An example configuration for lighttpd might appear as follows:
```
$HTTP["host"] == "owncast.yourdomain.com" {
proxy.forwarded = ( "host" => 1,
"proto" => 1,
"for" => 1,
"remote_user" => 1 )

    # Required for websocket (chat) forwarding:
    proxy.header = ( "upgrade" => "enable" )

}
```

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
