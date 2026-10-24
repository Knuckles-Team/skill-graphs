##  [Rewrites to external origins](https://vercel.com/docs/routing#rewrites-to-external-origins)[](https://vercel.com/docs/routing#rewrites-to-external-origins)
External rewrites forward requests to a different backend or API outside your Vercel project. The visitor's browser still shows your domain, while the CDN proxies the request to the external origin.
Use external rewrites when you need to:
  * Proxy API requests to an external backend under your domain
  * Migrate to Vercel incrementally by routing some paths to your existing infrastructure
  * Serve content from a headless CMS or third-party service at your own URL


```
{
  "rewrites": [
    { "source": "/api/:path*", "destination": "https://api.example.com/:path*" }
  ]
}
```

Vercel can also [cache responses from external origins](https://vercel.com/docs/caching/cdn-cache) to reduce load on your backend.
