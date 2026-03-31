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
  1. [Websockets](https://owncast.online/docs/sslproxies/nginx/#websockets)


# NGINX
NGINX is a popular web server used as a reverse proxy with free Let’s Encrypt certificates. Visit the
## Websockets[#](https://owncast.online/docs/sslproxies/nginx/#websockets)
People often look over the need to tell NGINX to proxy websockets correctly, leading to chat being disabled. Please read the quick
Essentially, you’ll need to edit `/etc/nginx/nginx.conf` to add the following map block to the http section
```
http {
...
map $http_upgrade $connection_upgrade {
    default upgrade;
    ''      close;
}
...
}
```

You’ll end up with a configuration that looks somewhat like the following when you’re done setting up NGINX. The below should be added to `/etc/nginx/sites-available/my.site.com.conf` and enabled with `ln /etc/nginx/sites-available/my.site.com.conf /etc/nginx/sites-enabled/my.site.com.conf` and tested with `sudo nginx -t`, then restarted `sudo service nginx restart`
```
server {
    server_name owncast.yourdomain.com;
    listen 443 ssl;
    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    location / {
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Host $host;
        proxy_set_header X-Forwarded-Server $host;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $connection_upgrade;
        proxy_set_header  Authorization $http_authorization;
        proxy_pass_header Authorization;
        proxy_pass http://127.0.0.1:8080;
    }
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
