##  [Incremental Static Regeneration](https://vercel.com/docs/getting-started-with-vercel#incremental-static-regeneration)[](https://vercel.com/docs/getting-started-with-vercel#incremental-static-regeneration)
[Incremental Static Regeneration (ISR)](https://vercel.com/docs/incremental-static-regeneration) allows you to create or update content without redeploying your site. ISR has two main benefits for developers: better performance and faster build times.
To enable ISR in Astro, you need to use the `isr` to `true` in your configuration in `astro.config.mjs`:
ISR function requests do not include search params, similar to requests in static mode.
Using ISR with Astro on Vercel offers:
  * Better performance with our global [CDN](https://vercel.com/docs/cdn)
  * Zero-downtime rollouts to previously statically generated pages
  * Global content updates in 300ms
  * Generated pages are both cached and persisted to durable storage
