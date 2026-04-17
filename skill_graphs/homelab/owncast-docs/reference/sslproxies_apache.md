### SSL & HTTP Proxies
  * [Caddy](https://owncast.online/docs/sslproxies/caddy/)
  * [HAProxy](https://owncast.online/docs/sslproxies/haproxy/)
  * [Lighttpd](https://owncast.online/docs/sslproxies/lighttpd/)
  * [NGINX](https://owncast.online/docs/sslproxies/nginx/)
  * [Apache](https://owncast.online/docs/sslproxies/apache/)


### [← Documentation](https://owncast.online/docs/ "Documentation")
### On this page
# Apache
If you’re already using Apache as a web server you can
Ensure required Apache modules are enabled using the `a2enmod` command.
```
$ sudo a2enmod proxy proxy_http ssl

```

```
<VirtualHost *:80>
        ServerName live.example.com
        ServerAdmin admin@example.com

        Redirect permanent / https://live.example.com

</VirtualHost>

# live-le-ssl.conf

<IfModule mod_ssl.c>
<VirtualHost *:443>
        ServerName live.example.com
        ServerAdmin admin@example.com

        ProxyRequests       Off
        ProxyPreserveHost   On
        AllowEncodedSlashes NoDecode

        ProxyPass        / http://localhost:8080/ upgrade=websocket
        ProxyPassReverse / http://localhost:8080/

        RequestHeader    set X-Forwarded-Proto "https"
        RequestHeader    set X-Forwarded-Port "443"

        SSLCertificateFile /path/to/fullchain.pem
        SSLCertificateKeyFile /path/to/privkey.pem
        Include /etc/letsencrypt/options-ssl-apache.conf

</VirtualHost>
</IfModule>
```

Recaptcha requires verification.
-
protected by **reCAPTCHA**
-
