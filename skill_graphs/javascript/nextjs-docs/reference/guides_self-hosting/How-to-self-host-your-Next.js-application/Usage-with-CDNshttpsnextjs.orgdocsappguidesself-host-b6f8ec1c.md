## Usage with CDNs[](https://nextjs.org/docs/app/guides/self-hosting#usage-with-cdns)
When using a CDN in front of your Next.js application, the page will include `Cache-Control: private` response header when dynamic APIs are accessed. This ensures that the resulting HTML page is marked as non-cacheable. If the page is fully prerendered to static, it will include `Cache-Control: public` to allow the page to be cached on the CDN.
If you don't need a mix of both static and dynamic components, you can make your entire route static and cache the output HTML on a CDN. This Automatic Static Optimization is the default behavior when running `next build` if dynamic APIs are not used.
As Partial Prerendering moves to stable, we will provide support through the Deployment Adapters API.
