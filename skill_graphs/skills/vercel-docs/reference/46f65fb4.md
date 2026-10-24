##  [`cache-control`](https://vercel.com/docs/headers/response-headers#cache-control)[](https://vercel.com/docs/headers/response-headers#cache-control)
Used to specify directives for caching mechanisms in both the [CDN cache](https://vercel.com/docs/caching/cdn-cache) and the browser cache. See the [Cache-Control headers](https://vercel.com/docs/headers#cache-control-header) section for more detail.
If you use this header to instruct the CDN to cache data, such as with the [`s-maxage`](https://vercel.com/docs/headers/cache-control-headers#s-maxage) directive, Vercel returns the following `cache-control` header to the client:
-`cache-control: public, max-age=0, must-revalidate`
