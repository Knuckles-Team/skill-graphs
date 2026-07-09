## Caching and ISR[](https://nextjs.org/docs/pages/guides/self-hosting#caching-and-isr)
Next.js can cache responses, generated static pages, build outputs, and other static assets like images, fonts, and scripts.
Caching and revalidating pages (with [Incremental Static Regeneration](https://nextjs.org/docs/app/guides/incremental-static-regeneration)) use the **same shared cache**. By default, this cache is stored to the filesystem (on disk) on your Next.js server. **This works automatically when self-hosting** using both the Pages and App Router.
You can configure the Next.js cache location if you want to persist cached pages and data to durable storage, or share the cache across multiple containers or instances of your Next.js application.
### Automatic Caching[](https://nextjs.org/docs/pages/guides/self-hosting#automatic-caching)
  * Next.js sets the `Cache-Control` header of `public, max-age=31536000, immutable` to truly immutable assets. It cannot be overridden. These immutable files contain a SHA-hash in the file name, so they can be safely cached indefinitely. For example, [Static Image Imports](https://nextjs.org/docs/app/getting-started/images#local-images). You can [configure the TTL](https://nextjs.org/docs/app/api-reference/components/image#minimumcachettl) for images.
  * Incremental Static Regeneration (ISR) sets the `Cache-Control` header of `s-maxage: <revalidate in getStaticProps>, stale-while-revalidate`. This revalidation time is defined in your [`getStaticProps` function](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props) in seconds. If you set `revalidate: false`, it will default to a one-year cache duration.
  * Dynamically rendered pages set a `Cache-Control` header of `private, no-cache, no-store, max-age=0, must-revalidate` to prevent user-specific data from being cached. This applies to both the App Router and Pages Router. This also includes [Draft Mode](https://nextjs.org/docs/app/guides/draft-mode).


### Static Assets[](https://nextjs.org/docs/pages/guides/self-hosting#static-assets)
If you want to host static assets on a different domain or CDN, you can use the `assetPrefix` [configuration](https://nextjs.org/docs/app/api-reference/config/next-config-js/assetPrefix) in `next.config.js`. Next.js will use this asset prefix when retrieving JavaScript or CSS files. Separating your assets to a different domain does come with the downside of extra time spent on DNS and TLS resolution.
[Learn more about `assetPrefix`](https://nextjs.org/docs/app/api-reference/config/next-config-js/assetPrefix).
### Configuring Caching[](https://nextjs.org/docs/pages/guides/self-hosting#configuring-caching)
By default, generated cache assets will be stored in memory (defaults to 50mb) and on disk. If you are hosting Next.js using a container orchestration platform like Kubernetes, each pod will have a copy of the cache. To prevent stale data from being shown since the cache is not shared between pods by default, you can configure the Next.js cache to provide a cache handler and disable in-memory caching.
To configure the ISR/Data Cache location when self-hosting, you can configure a custom handler in your `next.config.js` file:
next.config.js
```
module.exports = {
  cacheHandler: require.resolve('./cache-handler.js'),
  cacheMaxMemorySize: 0, // disable default in-memory caching
}
```

Then, create `cache-handler.js` in the root of your project, for example:
cache-handler.js
```
const cache = new Map()

module.exports = class CacheHandler {
  constructor(options) {
    this.options = options
  }

  async get(key) {
    // This could be stored anywhere, like durable storage
    return cache.get(key)
  }

  async set(key, data, ctx) {
    // This could be stored anywhere, like durable storage
    cache.set(key, {
      value: data,
      lastModified: Date.now(),
      tags: ctx.tags,
    })
  }

  async revalidateTag(tags) {
    // tags is either a string or an array of strings
    tags = [tags].flat()
    // Iterate over all entries in the cache
    for (let [key, value] of cache) {
      // If the value's tags include the specified tag, delete this entry
      if (value.tags.some((tag) => tags.includes(tag))) {
        cache.delete(key)
      }
    }
  }

  // If you want to have temporary in memory cache for a single request that is reset
  // before the next request you can leverage this method
  resetRequestCache() {}
}
```

Using a custom cache handler will allow you to ensure consistency across all pods hosting your Next.js application. For instance, you can save the cached values anywhere, like
> **Good to know:**
>   * `revalidatePath` is a convenience layer on top of cache tags. Calling `revalidatePath` will call the `revalidateTag` function with a special default tag for the provided page.
>
