## Usage[](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote#usage)
To use `'use cache: remote'`, enable the [`cacheComponents`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents) flag in your `next.config.ts` file:
next.config.ts
TypeScript
JavaScript TypeScript
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  cacheComponents: true,
}

export default nextConfig
```

Then add `'use cache: remote'` to the functions or components where you've determined remote caching is justified. The handler implementation is configured via [`cacheHandlers`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers), though hosting providers should typically provide this automatically. If you're self-hosting, see the `cacheHandlers` configuration reference to set up your cache storage.
### When to avoid remote caching[](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote#when-to-avoid-remote-caching)
  * If you already have a server-side cache key-value store wrapping your data layer, `use cache` may be sufficient to include data in the static shell without adding another caching layer
  * If operations are already fast (< 50ms) due to proximity or local access, the remote cache lookup might not improve performance
  * If cache keys have mostly unique values per request (search filters, price ranges, user-specific parameters), cache utilization will be near-zero
  * If data changes frequently (seconds to minutes), cache hits will quickly go stale, leading to frequent misses and waiting for upstream revalidation


### When remote caching makes sense[](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote#when-remote-caching-makes-sense)
Remote caching provides the most value when content is deferred to request time (outside the static shell). This typically happens when a component accesses request values like [`cookies()`](https://nextjs.org/docs/app/api-reference/functions/cookies), [`headers()`](https://nextjs.org/docs/app/api-reference/functions/headers), or [`searchParams`](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional), placing it inside a Suspense boundary. In this context:
  * Each request executes the component and looks up the cache
  * In serverless environments, each instance has its own ephemeral memory with low cache hit rates
  * Remote caching provides a shared cache across all instances, improving hit rates and reducing backend load


Compelling scenarios for `'use cache: remote'`:
  * **Rate-limited APIs** : Your upstream service has rate limits or request quotas that you risk hitting
  * **Protecting slow backends** : Your database or API becomes a bottleneck under high traffic
  * **Expensive operations** : Database queries or computations that are costly to run repeatedly
  * **Flaky or unreliable services** : External services that occasionally fail or have availability issues


In these cases, the cost and latency of remote caching is justified by avoiding worse outcomes (rate limit errors, backend overload, high compute bills, or degraded user experience).
For static shell content, `use cache` is usually sufficient. If your upstream source can't handle concurrent revalidation requests (like a rate-limited CMS), `use cache: remote` acts as a shared cache layer. This is the same pattern as putting a key-value store in front of a database, but declared in code.
### How `use cache: remote` differs from `use cache` and `use cache: private`[](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote#how-use-cache-remote-differs-from-use-cache-and-use-cache-private)
Next.js provides three caching directives, each designed for different use cases:
Feature | `use cache` | `'use cache: remote'` | `'use cache: private'`
---|---|---|---
**Server-side caching** | In-memory or cache handler | Remote cache handler | None
**Cache scope** | Shared across all users | Shared across all users | Per-client (browser)
**Can access cookies/headers directly** | No (must pass as arguments) | No (must pass as arguments) | Yes
**Server cache utilization** | May be low outside static shell | High (shared across instances) | N/A
**Additional costs** | None | Infrastructure (storage, network) | None
**Latency impact** | None | Cache handler lookup | None
### Caching with runtime data[](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote#caching-with-runtime-data)
Both `use cache` and `'use cache: remote'` can't access runtime values like cookies or search params directly. You can extract these values and pass them as arguments to cached functions. See [with runtime data](https://nextjs.org/docs/app/getting-started/cache-components#with-runtime-data) for this pattern.
> **Good to know** : `use cache` stores entries in-memory. In serverless environments, memory is not shared between instances and is typically destroyed after serving a request, leading to frequent cache misses for runtime caching.
### Cache key considerations[](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote#cache-key-considerations)
Be thoughtful about which values you include in cache keys. Each unique value creates a separate cache entry, reducing cache utilization. Consider this example with search filters:
app/products/[category]/page.tsx
```
import { Suspense } from 'react'

export default async function ProductsPage({
  params,
  searchParams,
}: {
  params: Promise<{ category: string }>
  searchParams: Promise<{ minPrice?: string }>
}) {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <ProductList params={params} searchParams={searchParams} />
    </Suspense>
  )
}

async function ProductList({
  params,
  searchParams,
}: {
  params: Promise<{ category: string }>
  searchParams: Promise<{ minPrice?: string }>
}) {
  const { category } = await params

  const { minPrice } = await searchParams

  // Cache only on category (few unique values)
  // Don't include price filter (many unique values)
  const products = await getProductsByCategory(category)

  // Filter price in memory instead of creating cache entries
  // for every price value
  const filtered = minPrice
    ? products.filter((p) => p.price >= parseFloat(minPrice))
    : products

  return <div>{/* render filtered products */}</div>
}

async function getProductsByCategory(category: string) {
  'use cache: remote'
  // Only category is part of the cache key
  // Much better utilization than caching every price filter value
  return db.products.findByCategory(category)
}
```

In this example, the remote handler stores more data per cache entry (all products in a category) to achieve better cache hit rates. This is worth it when the cost of cache misses (hitting your backend) outweighs the storage cost of larger entries.
The same principle applies to user-specific data. Rather than caching per-user data directly, use user preferences to determine what shared data to cache.
For example, if users have a language preference in their session, extract that preference and use it to cache shared content:
  * Instead of remote caching `getUserProfile(sessionID)`, which creates one entry per user
  * Remote cache `getCMSContent(language)` to create one entry per language


app/components/welcome-message.tsx
```
import { cookies } from 'next/headers'
import { cacheLife } from 'next/cache'

export async function WelcomeMessage() {
  // Extract the language preference (not unique per user)
  const language = (await cookies()).get('language')?.value || 'en'

  // Cache based on language (few unique values: en, es, fr, de, etc.)
  // All users who prefer 'en' share the same cache entry
  const content = await getCMSContent(language)

  return <div>{content.welcomeMessage}</div>
}

async function getCMSContent(language: string) {
  'use cache: remote'
  cacheLife({ expire: 3600 })
  // Creates ~10-50 cache entries (one per language)
  // instead of thousands (one per user)
  return cms.getHomeContent(language)
}
```

This way all users who prefer the same language share a cache entry, improving cache utilization and reducing load on your CMS.
The pattern is the same in both examples: find the dimension with fewer unique values (category vs. price, language vs. user ID), cache on that dimension, and filter or select the rest in memory.
If the service used by `getUserProfile` cannot scale with your frontend load, you may still be able to use the `use cache` directive with a short `cacheLife` for in-memory caching. However, for most user data, you likely want to fetch directly from the source (which might already be wrapped in a key/value store as mentioned in the guidelines above).
Only use [`'use cache: private'`](https://nextjs.org/docs/app/api-reference/directives/use-cache-private) if you have compliance requirements or can't refactor to pass runtime data as arguments.
### Nesting rules[](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote#nesting-rules)
Remote caches have specific nesting rules:
  * Remote caches **can** be nested inside other remote caches (`'use cache: remote'`)
  * Remote caches **can** be nested inside regular caches (`'use cache'`)
  * Remote caches **cannot** be nested inside private caches (`'use cache: private'`)
  * Private caches **cannot** be nested inside remote caches


```
// VALID: Remote inside remote
async function outerRemote() {
  'use cache: remote'
  const result = await innerRemote()
  return result
}

async function innerRemote() {
  'use cache: remote'
  return getData()
}

// VALID: Remote inside regular cache
async function outerCache() {
  'use cache'
  // The inner remote cache will work when deferred to request time
  const result = await innerRemote()
  return result
}

async function innerRemote() {
  'use cache: remote'
  return getData()
}

// INVALID: Remote inside private
async function outerPrivate() {
  'use cache: private'
  const result = await innerRemote() // Error!
  return result
}

async function innerRemote() {
  'use cache: remote'
  return getData()
}

// INVALID: Private inside remote
async function outerRemote() {
  'use cache: remote'
  const result = await innerPrivate() // Error!
  return result
}

async function innerPrivate() {
  'use cache: private'
  return getData()
}
```
