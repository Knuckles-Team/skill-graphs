## Disable source maps[](https://nextjs.org/docs/app/guides/memory-usage#disable-source-maps)
Generating source maps consumes extra memory during the build process.
You can disable source map generation by adding `productionBrowserSourceMaps: false` and `experimental.serverSourceMaps: false` to your Next.js configuration.
When using the `cacheComponents` feature, Next.js will use source maps by default during the prerender phase of `next build`. If you consistently encounter memory issues during that phase (after "Generating static pages"), you can try disabling source maps in that phase by adding `enablePrerenderSourceMaps: false` to your Next.js configuration.
> **Good to know** : Some plugins may turn on source maps and may require custom configuration to disable.
