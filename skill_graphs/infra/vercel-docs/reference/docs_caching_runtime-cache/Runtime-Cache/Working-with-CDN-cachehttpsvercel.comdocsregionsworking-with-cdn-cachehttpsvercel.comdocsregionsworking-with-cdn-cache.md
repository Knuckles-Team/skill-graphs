##  [Working with CDN cache](https://vercel.com/docs/regions#working-with-cdn-cache)[](https://vercel.com/docs/regions#working-with-cdn-cache)
Runtime cache can work alongside CDN caching in two ways:
  1. With [Vercel ISR](https://vercel.com/docs/incremental-static-regeneration): Vercel handles CDN caching for your pages and routes, while runtime cache stores the data fetches within your functions
  2. With manual CDN caching (shown below): You set `Cache-Control` headers to cache HTTP responses at the CDN, while runtime cache stores data fetches within your functions


This section covers the manual approach. If you're using [Vercel ISR](https://vercel.com/docs/incremental-static-regeneration), runtime cache operates independently as described in [limits and usage](https://vercel.com/docs/regions#limits-and-usage).
When you've set up runtime cache with a serverless function and manual CDN caching, the following happens:
  1. Your function runs and checks the runtime cache in the region where it is executed for data
  2. If that region's runtime cache has the data, it returns the data immediately
  3. If not, your function fetches the data from origin and stores it in that region's runtime cache
  4. Your function generates a response using the data
  5. If you configured [CDN cache](https://vercel.com/docs/cdn-cache) via `Cache-Control` headers, it will cache the complete response in [Vercel regions](https://vercel.com/docs/regions)


This example uses runtime cache to fetch and cache product data, and CDN cache to cache the complete API response:
app/api/products/route.ts
```
import { cacheLife } from 'next/cache';

export async function GET() {
  const products = await getProducts();

  return new Response(JSON.stringify(products), {
    status: 200,
    headers: {
      'Content-Type': 'application/json',
      'Cache-Control': 'public, s-maxage=60', // CDN caches for 60 seconds
    },
  });
}

async function getProducts() {
  'use cache: remote' // Runtime cache
  cacheLife({ expire: 3600 }) // 1 hour

  const response = await fetch('https://api.example.com/products');
  return response.json();
}
```

In this example:
  * Runtime cache stores product data in the region for 1 hour (3600 seconds)
  * CDN cache stores the complete HTTP response in the regional cache for 60 seconds
  * If the CDN cache expires, the function runs but can still use runtime-cached data
  * If both caches expire, the function fetches fresh data from the origin
