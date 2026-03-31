### SSL & HTTP Proxies
  * [Caddy](https://owncast.online/docs/sslproxies/caddy/)
  * [HAProxy](https://owncast.online/docs/sslproxies/haproxy/)
  * [Lighttpd](https://owncast.online/docs/sslproxies/lighttpd/)
  * [NGINX](https://owncast.online/docs/sslproxies/nginx/)
  * [Apache](https://owncast.online/docs/sslproxies/apache/)


### [← Documentation](https://owncast.online/docs/ "Documentation")
### On this page
  1. [1. Make sure you don’t have other web servers running.](https://owncast.online/docs/sslproxies/caddy/#1-make-sure-you-dont-have-other-web-servers-running)
  2. [2. Install Caddy](https://owncast.online/docs/sslproxies/caddy/#2-install-caddy)
  3. [3. Run Caddy as a reverse proxy](https://owncast.online/docs/sslproxies/caddy/#3-run-caddy-as-a-reverse-proxy)
  4. [4. Run Owncast normally](https://owncast.online/docs/sslproxies/caddy/#4-run-owncast-normally)
  5. [5. Access Owncast through the proxy](https://owncast.online/docs/sslproxies/caddy/#5-access-owncast-through-the-proxy)


# Caddy
While we will try to walk you through some installation steps **it is highly suggested you follow Caddy’s**. Caddy is a well documented quality piece of software that you should get familiar with if you need to run a SSL reverse proxy.
## 1. Make sure you don’t have other web servers running.[#](https://owncast.online/docs/sslproxies/caddy/#1-make-sure-you-dont-have-other-web-servers-running)
If you are running other pieces of web server software such as Apache or NGINX using port 80 or 443 then you won’t be able to continue with this Caddy install. Either remove the other pieces of software or read up on how to make them live in harmony.
## 2. Install Caddy[#](https://owncast.online/docs/sslproxies/caddy/#2-install-caddy)
Depending on your system there may be different options on installing. Using APT is suggested if it’s supported on your machine.
Using APT (recommended)
Installing this package automatically starts and runs Caddy for you as a systemd service so it will automatically run Caddy each time you start your machine.
```
sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list
sudo apt update
sudo apt install caddy
```

Download manually
  1. Find the version for your platform and operating system.
  2. Unarchive the file: `tar -xvzf caddy_2.3.0_linux_amd64.tar.gz`
  3. You’re likely to want to setup Caddy as a system service to auatomatically start in the background. 


## 3. Run Caddy as a reverse proxy[#](https://owncast.online/docs/sslproxies/caddy/#3-run-caddy-as-a-reverse-proxy)
Single command line
It offers automatic configuration of HTTPS with a single command.
```
caddy reverse-proxy --from owncast.mydomain.com --to 127.0.0.1:8080
```

Replace `owncast.mydomain.com` with the public hostname of your Owncast server like `watch.owncast.online` for example.
Caddyfile
The 
Add to your Caddyfile:
```
owncast.mydomain.com {
encode gzip
reverse_proxy 127.0.0.1:8080
tls webmaster@mydomain.com
}
```

Replace `owncast.mydomain.com` with the public hostname of your Owncast server like `watch.owncast.online` for example.
* * *
If you specify `owncast.mydomain.com` without a protocol or a port, it will attempt to use the default `http` and `https` ports (80 and 443). Since these are `sudo` or as `root`.
## 4. Run Owncast normally[#](https://owncast.online/docs/sslproxies/caddy/#4-run-owncast-normally)
Continue to run Owncast on port 8080.
## 5. Access Owncast through the proxy[#](https://owncast.online/docs/sslproxies/caddy/#5-access-owncast-through-the-proxy)
* * *
You should now be able to access your Owncast server by visiting 
Replace `owncast.mydomain.com` with the public hostname of your Owncast server like `watch.owncast.online` for example.
Recaptcha requires verification. 
- 
protected by **reCAPTCHA**
-