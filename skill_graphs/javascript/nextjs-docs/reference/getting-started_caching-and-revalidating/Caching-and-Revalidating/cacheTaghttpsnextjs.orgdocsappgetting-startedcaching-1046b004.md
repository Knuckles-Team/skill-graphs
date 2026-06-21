##  `cacheTag`[](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#cachetag)
[`cacheTag`](https://nextjs.org/docs/app/api-reference/functions/cacheTag) allows you to tag cached data in [Cache Components](https://nextjs.org/docs/app/getting-started/cache-components) so it can be revalidated on-demand. Previously, cache tagging was limited to `fetch` requests, and caching other work required the experimental `unstable_cache` API.
With Cache Components, you can use the [`use cache`](https://nextjs.org/docs/app/api-reference/directives/use-cache) directive to cache any computation, and `cacheTag` to tag it. This works with database queries, file system operations, and other server-side work.
app/lib/data.ts
TypeScript
JavaScript TypeScript
```
import { cacheTag } from 'next/cache'

export async function getProducts() {
  'use cache'
  cacheTag('products')

  const products = await db.query('SELECT * FROM products')
  return products
}
```

Once tagged, you can use [`revalidateTag`](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#revalidatetag) or [`updateTag`](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#updatetag) to invalidate the cache entry for products.
> **Good to know** : `cacheTag` is used with [Cache Components](https://nextjs.org/docs/app/getting-started/cache-components) and the [`use cache`](https://nextjs.org/docs/app/api-reference/directives/use-cache) directive. It expands the caching and revalidation story beyond `fetch`.
See the [`cacheTag` API reference](https://nextjs.org/docs/app/api-reference/functions/cacheTag) to learn more.
