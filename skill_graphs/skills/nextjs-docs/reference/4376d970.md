## Using `use cache`[](https://nextjs.org/docs/app/getting-started/cache-components#using-use-cache)
The [`use cache`](https://nextjs.org/docs/app/api-reference/directives/use-cache) directive caches the return value of async functions and components. You can apply it at the function, component, or file level.
Arguments and any closed-over values from parent scopes automatically become part of the [cache key](https://nextjs.org/docs/app/api-reference/directives/use-cache#cache-keys), which means different inputs produce separate cache entries. This enables personalized or parameterized cached content.
When [dynamic content](https://nextjs.org/docs/app/getting-started/cache-components#dynamic-content) doesn't need to be fetched fresh from the source on every request, caching it lets you include the content in the static shell during prerendering, or reuse the result at runtime across multiple requests.
Cached content can be revalidated in two ways: automatically based on the cache lifetime, or on-demand using tags with [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag) or [`updateTag`](https://nextjs.org/docs/app/api-reference/functions/updateTag).
> **Good to know** : See [serialization requirements and constraints](https://nextjs.org/docs/app/api-reference/directives/use-cache#constraints) for details on what can be cached and how arguments work.
### During prerendering[](https://nextjs.org/docs/app/getting-started/cache-components#during-prerendering)
While [dynamic content](https://nextjs.org/docs/app/getting-started/cache-components#dynamic-content) is fetched from external sources, it's often unlikely to change between accesses. Product catalog data updates with inventory changes, blog post content rarely changes after publishing, and analytics reports for past dates remain static.
If this data doesn't depend on [runtime data](https://nextjs.org/docs/app/getting-started/cache-components#runtime-data), you can use the `use cache` directive to include it in the static HTML shell. Use [`cacheLife`](https://nextjs.org/docs/app/api-reference/functions/cacheLife) to define how long to use the cached data.
When revalidation occurs, the static shell is updated with fresh content. See [Tagging and revalidating](https://nextjs.org/docs/app/getting-started/cache-components#tagging-and-revalidating) for details on on-demand revalidation.
app/page.tsx
```
import { cacheLife } from 'next/cache'

export default async function Page() {
  'use cache'
  cacheLife('hours')

  const users = await db.query('SELECT * FROM users')

  return (
    <ul>
      {users.map((user) => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  )
}
```

The `cacheLife` function accepts a cache profile name (like `'hours'`, `'days'`, or `'weeks'`) or a custom configuration object to control cache behavior:
app/page.tsx
```
import { cacheLife } from 'next/cache'

export default async function Page() {
  'use cache'
  cacheLife({
    stale: 3600, // 1 hour until considered stale
    revalidate: 7200, // 2 hours until revalidated
    expire: 86400, // 1 day until expired
  })

  const users = await db.query('SELECT * FROM users')

  return (
    <ul>
      {users.map((user) => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  )
}
```

See the [`cacheLife` API reference](https://nextjs.org/docs/app/api-reference/functions/cacheLife) for available profiles and custom configuration options.
### With runtime data[](https://nextjs.org/docs/app/getting-started/cache-components#with-runtime-data)
Runtime data and [`use cache`](https://nextjs.org/docs/app/api-reference/directives/use-cache) cannot be used in the same scope. However, you can extract values from runtime APIs and pass them as arguments to cached functions.
app/profile/page.tsx
```
import { cookies } from 'next/headers'
import { Suspense } from 'react'

export default function Page() {
  // Page itself creates the dynamic boundary
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <ProfileContent />
    </Suspense>
  )
}

// Component (not cached) reads runtime data
async function ProfileContent() {
  const session = (await cookies()).get('session')?.value

  return <CachedContent sessionId={session} />
}

// Cached component/function receives data as props
async function CachedContent({ sessionId }: { sessionId: string }) {
  'use cache'
  // sessionId becomes part of cache key
  const data = await fetchUserData(sessionId)
  return <div>{data}</div>
}
```

At request time, `CachedContent` executes if no matching cache entry is found, and stores the result for future requests.
### With non-deterministic operations[](https://nextjs.org/docs/app/getting-started/cache-components#with-non-deterministic-operations)
Within a `use cache` scope, non-deterministic operations execute during prerendering. This is useful when you want the same rendered output served to all users:
```
export default async function Page() {
  'use cache'

  // Execute once, then cached for all requests
  const random = Math.random()
  const random2 = Math.random()
  const now = Date.now()
  const date = new Date()
  const uuid = crypto.randomUUID()
  const bytes = crypto.getRandomValues(new Uint8Array(16))

  return (
    <div>
      <p>
        {random} and {random2}
      </p>
      <p>{now}</p>
      <p>{date.getTime()}</p>
      <p>{uuid}</p>
      <p>{bytes}</p>
    </div>
  )
}
```

All requests will be served a route containing the same random numbers, timestamp, and UUID until the cache is revalidated.
### Tagging and revalidating[](https://nextjs.org/docs/app/getting-started/cache-components#tagging-and-revalidating)
Tag cached data with [`cacheTag`](https://nextjs.org/docs/app/api-reference/functions/cacheTag) and revalidate it after mutations using [`updateTag`](https://nextjs.org/docs/app/api-reference/functions/updateTag) in Server Actions for immediate updates, or [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag) when delays in updates are acceptable.
#### With `updateTag`[](https://nextjs.org/docs/app/getting-started/cache-components#with-updatetag)
Use `updateTag` when you need to expire and immediately refresh cached data within the same request:
app/actions.ts
```
import { cacheTag, updateTag } from 'next/cache'

export async function getCart() {
  'use cache'
  cacheTag('cart')
  // fetch data
}

export async function updateCart(itemId: string) {
  'use server'
  // write data using the itemId
  // update the user cart
  updateTag('cart')
}
```

#### With `revalidateTag`[](https://nextjs.org/docs/app/getting-started/cache-components#with-revalidatetag)
Use `revalidateTag` when you want to invalidate only properly tagged cached entries with stale-while-revalidate behavior. This is ideal for static content that can tolerate eventual consistency.
app/actions.ts
```
import { cacheTag, revalidateTag } from 'next/cache'

export async function getPosts() {
  'use cache'
  cacheTag('posts')
  // fetch data
}

export async function createPost(post: FormData) {
  'use server'
  // write data using the FormData
  revalidateTag('posts', 'max')
}
```

For more detailed explanation and usage examples, see the [`use cache` API reference](https://nextjs.org/docs/app/api-reference/directives/use-cache).
### What should I cache?[](https://nextjs.org/docs/app/getting-started/cache-components#what-should-i-cache)
What you cache should be a function of what you want your UI loading states to be. If data doesn't depend on runtime data and you're okay with a cached value being served for multiple requests over a period of time, use `use cache` with `cacheLife` to describe that behavior.
For content management systems with update mechanisms, consider using tags with longer cache durations and rely on `revalidateTag` to mark static initial UI as ready for revalidation. This pattern allows you to serve fast, cached responses while still updating content when it actually changes, rather than expiring the cache preemptively.
