##  [External rewrites](https://vercel.com/docs/routing/rewrites#external-rewrites)[](https://vercel.com/docs/routing/rewrites#external-rewrites)
External rewrites forward requests to APIs or websites outside your Vercel project, effectively allowing Vercel to function as a reverse proxy or standalone CDN. You can use this feature to:
  * Proxy API requests: Hide your actual API endpoint
  * Combine multiple services: Merge multiple backends under one domain
  * Create microfrontends: Combine multiple Vercel applications into a single website
  * Add caching: Cache external API responses on the CDN
  * Serve externally hosted content: Serve content that is not hosted on Vercel.


Example: Forward API requests to an external endpoint:
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "rewrites": [
    {
      "source": "/api/:path*",
      "destination": "https://api.example.com/:path*"
    }
  ]
}
```

A request to `/api/users` will be forwarded to `https://api.example.com/users` without changing the URL in the browser.
###  [Caching external rewrites](https://vercel.com/docs/routing/rewrites#caching-external-rewrites)[](https://vercel.com/docs/routing/rewrites#caching-external-rewrites)
External rewrites aren't cached by default. To enable caching, add the `x-vercel-enable-rewrite-caching` header to your `vercel.json`:
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "rewrites": [
    {
      "source": "/api/:path*",
      "destination": "https://api.example.com/:path*"
    }
  ],
  "headers": [
    {
      "source": "/api/:path*",
      "headers": [{ "key": "x-vercel-enable-rewrite-caching", "value": "1" }]
    }
  ]
}
```

This tells Vercel to respect caching headers on the upstream response. Once enabled, you can control the cache duration in two ways:
  1. From your API (preferred): When you control the backend, return [`CDN-Cache-Control`](https://vercel.com/docs/headers/cache-control-headers#cdn-cache-control-header) or [`Vercel-CDN-Cache-Control`](https://vercel.com/docs/headers/cache-control-headers#cdn-cache-control-header) headers in the API response:
`CDN-Cache-Control: max-age=60 `
This caches the response on the CDN for 60 seconds.
  2. From Vercel configuration: When you can't modify the backend, set caching headers in `vercel.json` alongside `x-vercel-enable-rewrite-caching`:
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "rewrites": [
    {
      "source": "/api/:path*",
      "destination": "https://api.example.com/:path*"
    }
  ],
  "headers": [
    {
      "source": "/api/:path*",
      "headers": [
        { "key": "x-vercel-enable-rewrite-caching", "value": "1" },
        {
          "key": "CDN-Cache-Control",
          "value": "max-age=60"
        }
      ]
    }
  ]
}
```

This caches the response on the CDN for 60 seconds.


For more information on caching headers, see the [Cache-Control headers documentation](https://vercel.com/docs/headers/cache-control-headers).
When caching external rewrites, it's best practice to also include a `Vercel-Cache-Tag` response header with a comma-separated list of tags so you can later [purge the CDN cache by tag](https://vercel.com/docs/cdn-cache/purge) at your convenience.
###  [Draining external rewrites](https://vercel.com/docs/routing/rewrites#draining-external-rewrites)[](https://vercel.com/docs/routing/rewrites#draining-external-rewrites)
You can export external rewrite data by draining logs from your application. External rewrite events appear in your runtime logs, allowing you to monitor proxy requests, track external API calls, and analyze traffic patterns to your backend services.
To get started, configure a [logs drain](https://vercel.com/docs/drains/using-drains).
###  [Observing external rewrites](https://vercel.com/docs/routing/rewrites#observing-external-rewrites)[](https://vercel.com/docs/routing/rewrites#observing-external-rewrites)
You can observe your external rewrite performance using Observability. The External Rewrites tab shows request counts, connection latency, and traffic patterns for your proxied requests, helping you monitor backend performance and validate that rewrites are working as expected.
Learn more in the [Observability Insights](https://vercel.com/docs/observability/insights#external-rewrites) documentation.
