##  [Redirect status codes](https://vercel.com/docs/routing/redirects#redirect-status-codes)[](https://vercel.com/docs/routing/redirects#redirect-status-codes)
  * 307 Temporary Redirect: Not cached by client, the method and body never changed. This type of redirect does not affect SEO and search engines will treat them as normal redirects.
  * 302 Found: Not cached by client, the method may or may not be changed to `GET`.
  * 308 Permanent Redirect: Cached by client, the method and body never changed. This type of redirect does not affect SEO and search engines will treat them as normal redirects.
  * 301 Moved Permanently: Cached by client, the method may or may not be changed to `GET`.
