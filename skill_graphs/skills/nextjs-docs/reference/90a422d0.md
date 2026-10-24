## Async `id` parameter for `sitemap` (Breaking change)[](https://nextjs.org/docs/app/guides/upgrading/version-16#async-id-parameter-for-sitemap-breaking-change)
Previously, the `id` values returned from [`generateSitemaps`](https://nextjs.org/docs/app/api-reference/functions/generate-sitemaps) were passed directly to the `sitemap` generating function.
app/product/sitemap.js
```
export async function generateSitemaps() {
  return [{ id: 0 }, { id: 1 }, { id: 2 }, { id: 3 }]
}

// Next.js 15 - synchronous id access
export default async function sitemap({ id }) {
  const start = id * 50000 // id is a number
  // ...
}
```

Starting with **Next.js 16** , the `sitemap` generating function now receives `id` as a promise.
app/product/sitemap.js
```
export async function generateSitemaps() {
  return [{ id: 0 }, { id: 1 }, { id: 2 }, { id: 3 }]
}

// Next.js 16 - asynchronous id access
export default async function sitemap({ id }) {
  const resolvedId = await id // id is now Promise<string>
  const start = Number(resolvedId) * 50000
  // ...
}
```
