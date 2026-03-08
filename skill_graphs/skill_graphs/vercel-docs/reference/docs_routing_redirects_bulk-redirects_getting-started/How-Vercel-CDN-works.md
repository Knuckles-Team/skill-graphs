# How Vercel CDN works
Last updated March 8, 2026
Every request to a Vercel deployment flows through a globally distributed CDN before it reaches your application code. The CDN handles routing, caching, security, and compression automatically, so your app is fast by default.
When a visitor requests a page, the CDN processes it through a series of layers. Each layer can resolve the request on its own or pass it to the next.
Close to user
Client
PoP
Vercel Region
[CDN Cache](https://vercel.com/docs/caching/cdn-cache)Global across all Vercel regions for fast delivery
Function Region
[ISR Cache](https://vercel.com/docs/incremental-static-regeneration)Can be revalidated on-demand or based on time
Vercel Function
[Runtime Cache](https://vercel.com/docs/caching/runtime-cache)For data used in Vercel Functions
Backend
