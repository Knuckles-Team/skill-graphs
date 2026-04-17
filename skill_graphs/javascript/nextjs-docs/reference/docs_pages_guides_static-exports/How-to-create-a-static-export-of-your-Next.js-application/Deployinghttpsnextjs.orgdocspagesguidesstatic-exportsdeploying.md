## Deploying[](https://nextjs.org/docs/pages/guides/static-exports#deploying)
With a static export, Next.js can be deployed and hosted on any web server that can serve HTML/CSS/JS static assets.
When running `next build`, Next.js generates the static export into the `out` folder. For example, let's say you have the following routes:
  * `/`
  * `/blog/[id]`


After running `next build`, Next.js will generate the following files:
  * `/out/index.html`
  * `/out/404.html`
  * `/out/blog/post-1.html`
  * `/out/blog/post-2.html`


If you are using a static host like Nginx, you can configure rewrites from incoming requests to the correct files:
nginx.conf
```
server {
  listen 80;
  server_name acme.com;

  root /var/www/out;

  location / {
      try_files $uri $uri.html $uri/ =404;
  }

  # This is necessary when `trailingSlash: false`.
  # You can omit this when `trailingSlash: true`.
  location /blog/ {
      rewrite ^/blog/(.*)$ /blog/$1.html break;
  }

  error_page 404 /404.html;
  location = /404.html {
      internal;
  }
}
```
