##  [Caching](https://vercel.com/docs/getting-started-with-vercel#caching)[](https://vercel.com/docs/getting-started-with-vercel#caching)
Vercel automatically caches static files at the edge after the first request, and stores them for up to 31 days on Vercel's CDN. Dynamic content can also be cached, and both dynamic and static caching behavior can be configured with [Cache-Control headers](https://vercel.com/docs/headers#cache-control-header).
The following Astro component will show a new time every 10 seconds. It does so by setting a 10 second max age on the contents of the page, then serving stale content while new content is being rendered on the server when that age is exceeded.
[Learn more about Cache Control options](https://vercel.com/docs/headers#cache-control-header).
src/pages/ssr-with-swr-caching.astro
```
---
Astro.response.headers.set('Cache-Control', 's-maxage=10, stale-while-revalidate');
const time = new Date().toLocaleTimeString();
---

<h1>{time}</h1>
```

###  [CDN Cache-Control headers](https://vercel.com/docs/getting-started-with-vercel#cdn-cache-control-headers)[](https://vercel.com/docs/getting-started-with-vercel#cdn-cache-control-headers)
You can also control how the cache behaves on any CDNs you may be using outside of Vercel's CDN with CDN Cache-Control Headers.
The following example tells downstream CDNs to cache the content for 60 seconds, and Vercel's CDN to cache it for 3600 seconds:
src/pages/ssr-with-swr-caching.astro
```
---
Astro.response.headers.set('Vercel-CDN-Cache-Control', 'max-age=3600',);
Astro.response.headers.set('CDN-Cache-Control', 'max-age=60',);
const time = new Date().toLocaleTimeString();
---

<h1>{time}</h1>
```

[Learn more about CDN Cache-Control headers](https://vercel.com/docs/headers/cache-control-headers#cdn-cache-control-header).
Caching on Vercel:
  * Automatically optimizes and caches assets for the best performance
  * Requires no additional services to procure or set up
  * Supports zero-downtime rollouts
