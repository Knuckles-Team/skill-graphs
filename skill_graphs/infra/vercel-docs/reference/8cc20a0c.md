##  [Incremental Static Regeneration (ISR)](https://vercel.com/docs/getting-started-with-vercel#incremental-static-regeneration-isr)[](https://vercel.com/docs/getting-started-with-vercel#incremental-static-regeneration-isr)
[Incremental Static Regeneration (ISR)](https://vercel.com/docs/incremental-static-regeneration) allows you to create or update content _without_ redeploying your site. ISR has two main benefits for developers: better performance and faster build times.
To enable ISR in a Nuxt route, add a `routeRules` option to your `nuxt.config.ts`, as shown in the example below:
nuxt.config.ts
TypeScript
TypeScript JavaScript Bash
```
export default defineNuxtConfig({
  routeRules: {
    // all routes (by default) will be revalidated every 60 seconds, in the background
    '/**': { isr: 60 },
    // this page will be generated on demand and then cached permanently
    '/static': { isr: true },
    // this page is statically generated at build time and cached permanently
    '/prerendered': { prerender: true },
    // this page will be always fresh
    '/dynamic': { isr: false },
  },
});
```

You should use the `isr` option rather than `swr` to enable ISR in a route. The `isr` option enables Nuxt to use Vercel's Cache.
using ISR with Nuxt on Vercel offers:
  * Better performance with our global [CDN](https://vercel.com/docs/cdn)
  * Zero-downtime rollouts to previously statically generated pages
  * Global content updates in 300ms
  * Generated pages are both cached and persisted to durable storage
