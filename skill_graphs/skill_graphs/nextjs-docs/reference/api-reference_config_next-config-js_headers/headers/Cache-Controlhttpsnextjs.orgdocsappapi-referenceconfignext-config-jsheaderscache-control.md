## Cache-Control[](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#cache-control)
Next.js sets the `Cache-Control` header of `public, max-age=31536000, immutable` for truly immutable assets. It cannot be overridden. These immutable files contain a SHA-hash in the file name, so they can be safely cached indefinitely. For example, [Static Image Imports](https://nextjs.org/docs/app/getting-started/images#local-images). You cannot set `Cache-Control` headers in `next.config.js` for these assets.
However, you can set `Cache-Control` headers for other responses or data.
Learn more about [caching](https://nextjs.org/docs/app/guides/caching) with the App Router.
