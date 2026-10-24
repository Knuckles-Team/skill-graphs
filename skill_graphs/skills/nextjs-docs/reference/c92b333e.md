## APIs[](https://nextjs.org/docs/app/guides/caching#apis)
The following table provides an overview of how different Next.js APIs affect caching:
API | Router Cache | Full Route Cache | Data Cache | React Cache
---|---|---|---|---
[`<Link prefetch>`](https://nextjs.org/docs/app/guides/caching#link) | Cache |  |  |
[`router.prefetch`](https://nextjs.org/docs/app/guides/caching#routerprefetch) | Cache |  |  |
[`router.refresh`](https://nextjs.org/docs/app/guides/caching#routerrefresh) | Revalidate |  |  |
[`fetch`](https://nextjs.org/docs/app/guides/caching#fetch) |  |  | Cache | Cache (GET and HEAD)
[`fetch` `options.cache`](https://nextjs.org/docs/app/guides/caching#fetch-optionscache) |  |  | Cache or Opt out |
[`fetch` `options.next.revalidate`](https://nextjs.org/docs/app/guides/caching#fetch-optionsnextrevalidate) |  | Revalidate | Revalidate |
[`fetch` `options.next.tags`](https://nextjs.org/docs/app/guides/caching#fetch-optionsnexttags-and-revalidatetag) |  | Cache | Cache |
[`revalidateTag`](https://nextjs.org/docs/app/guides/caching#fetch-optionsnexttags-and-revalidatetag) | Revalidate (Server Action) | Revalidate | Revalidate |
[`revalidatePath`](https://nextjs.org/docs/app/guides/caching#revalidatepath) | Revalidate (Server Action) | Revalidate | Revalidate |
[`const revalidate`](https://nextjs.org/docs/app/guides/caching#segment-config-options) |  | Revalidate or Opt out | Revalidate or Opt out |
[`const dynamic`](https://nextjs.org/docs/app/guides/caching#segment-config-options) |  | Cache or Opt out | Cache or Opt out |
[`cookies`](https://nextjs.org/docs/app/guides/caching#cookies) | Revalidate (Server Action) | Opt out |  |
[`headers`, `searchParams`](https://nextjs.org/docs/app/guides/caching#dynamic-apis) |  | Opt out |  |
[`generateStaticParams`](https://nextjs.org/docs/app/guides/caching#generatestaticparams) |  | Cache |  |
[`React.cache`](https://nextjs.org/docs/app/guides/caching#react-cache-function) |  |  |  | Cache
[`unstable_cache`](https://nextjs.org/docs/app/api-reference/functions/unstable_cache) |  |  | Cache |
###  `<Link>`[](https://nextjs.org/docs/app/guides/caching#link)
By default, the `<Link>` component automatically prefetches routes from the Full Route Cache and adds the React Server Component Payload to the Router Cache.
To disable prefetching, you can set the `prefetch` prop to `false`. But this will not skip the cache permanently, the route segment will still be cached client-side when the user visits the route.
Learn more about the [`<Link>` component](https://nextjs.org/docs/app/api-reference/components/link).
###  `router.prefetch`[](https://nextjs.org/docs/app/guides/caching#routerprefetch)
The `prefetch` option of the `useRouter` hook can be used to manually prefetch a route. This adds the React Server Component Payload to the Router Cache.
See the [`useRouter` hook](https://nextjs.org/docs/app/api-reference/functions/use-router) API reference.
###  `router.refresh`[](https://nextjs.org/docs/app/guides/caching#routerrefresh)
The `refresh` option of the `useRouter` hook can be used to manually refresh a route. This completely clears the Router Cache, and makes a new request to the server for the current route. `refresh` does not affect the Data or Full Route Cache.
The rendered result will be reconciled on the client while preserving React state and browser state.
See the [`useRouter` hook](https://nextjs.org/docs/app/api-reference/functions/use-router) API reference.
###  `fetch`[](https://nextjs.org/docs/app/guides/caching#fetch)
Data returned from `fetch` is _not_ automatically cached in the Data Cache.
By default, when no `cache` or `next.revalidate` options are provided:
  * [Dynamic rendering](https://nextjs.org/docs/app/guides/caching#dynamic-rendering): Fetch runs on every request and always returns fresh data.
  * [Static rendering](https://nextjs.org/docs/app/guides/caching#static-rendering): Fetched data is stored in the [Data Cache](https://nextjs.org/docs/app/guides/caching#data-cache), and the rendered output in the [Full Route Cache](https://nextjs.org/docs/app/guides/caching#full-route-cache). Next.js serves this cached result until the path is revalidated.


See the [`fetch` API Reference](https://nextjs.org/docs/app/api-reference/functions/fetch) for more options.
###  `fetch options.cache`[](https://nextjs.org/docs/app/guides/caching#fetch-optionscache)
You can opt individual `fetch` into caching by setting the `cache` option to `force-cache`:
```
// Opt into caching
fetch(`https://...`, { cache: 'force-cache' })
```

See the [`fetch` API Reference](https://nextjs.org/docs/app/api-reference/functions/fetch) for more options.
###  `fetch options.next.revalidate`[](https://nextjs.org/docs/app/guides/caching#fetch-optionsnextrevalidate)
You can use the `next.revalidate` option of `fetch` to set the revalidation period (in seconds) of an individual `fetch` request. This will revalidate the Data Cache, which in turn will revalidate the Full Route Cache. Fresh data will be fetched, and components will be re-rendered on the server.
```
// Revalidate at most after 1 hour
fetch(`https://...`, { next: { revalidate: 3600 } })
```

See the [`fetch` API reference](https://nextjs.org/docs/app/api-reference/functions/fetch) for more options.
###  `fetch options.next.tags` and `revalidateTag`[](https://nextjs.org/docs/app/guides/caching#fetch-optionsnexttags-and-revalidatetag)
Next.js has a cache tagging system for fine-grained data caching and revalidation.
  1. When using `fetch` or [`unstable_cache`](https://nextjs.org/docs/app/api-reference/functions/unstable_cache), you have the option to tag cache entries with one or more tags.
  2. Then, you can call `revalidateTag` to purge the cache entries associated with that tag.


For example, you can set a tag when fetching data:
```
// Cache data with a tag
fetch(`https://...`, { next: { tags: ['a', 'b', 'c'] } })
```

Then, call `revalidateTag` with a tag to purge the cache entry:
```
// Revalidate entries with a specific tag
revalidateTag('a')
```

There are two places you can use `revalidateTag`, depending on what you're trying to achieve:
  1. [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route) - to revalidate data in response of a third party event (e.g. webhook). This will not invalidate the Router Cache immediately as the Router Handler isn't tied to a specific route.
  2. [Server Actions](https://nextjs.org/docs/app/getting-started/updating-data) - to revalidate data after a user action (e.g. form submission). This will invalidate the Router Cache for the associated route.


###  `revalidatePath`[](https://nextjs.org/docs/app/guides/caching#revalidatepath)
`revalidatePath` allows you manually revalidate data **and** re-render the route segments below a specific path in a single operation. Calling the `revalidatePath` method revalidates the Data Cache, which in turn invalidates the Full Route Cache.
```
revalidatePath('/')
```

There are two places you can use `revalidatePath`, depending on what you're trying to achieve:
  1. [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route) - to revalidate data in response to a third party event (e.g. webhook).
  2. [Server Actions](https://nextjs.org/docs/app/getting-started/updating-data) - to revalidate data after a user interaction (e.g. form submission, clicking a button).


See the [`revalidatePath` API reference](https://nextjs.org/docs/app/api-reference/functions/revalidatePath) for more information.
> **`revalidatePath`**vs.**`router.refresh`**:
> Calling `router.refresh` will clear the Router cache, and re-render route segments on the server without invalidating the Data Cache or the Full Route Cache.
> The difference is that `revalidatePath` purges the Data Cache and Full Route Cache, whereas `router.refresh()` does not change the Data Cache and Full Route Cache, as it is a client-side API.
### Dynamic APIs[](https://nextjs.org/docs/app/guides/caching#dynamic-apis)
Dynamic APIs like `cookies` and `headers`, and the `searchParams` prop in Pages depend on runtime incoming request information. Using them will opt a route out of the Full Route Cache, in other words, the route will be dynamically rendered.
####  `cookies`[](https://nextjs.org/docs/app/guides/caching#cookies)
Using `cookies.set` or `cookies.delete` in a Server Action invalidates the Router Cache to prevent routes that use cookies from becoming stale (e.g. to reflect authentication changes).
See the [`cookies`](https://nextjs.org/docs/app/api-reference/functions/cookies) API reference.
### Segment Config Options[](https://nextjs.org/docs/app/guides/caching#segment-config-options)
The Route Segment Config options can be used to override the route segment defaults or when you're not able to use the `fetch` API (e.g. database client or 3rd party libraries).
The following Route Segment Config options will opt out of the Full Route Cache:
  * `const dynamic = 'force-dynamic'`


This config option will opt all fetches out of the Data Cache (i.e. `no-store`):
  * `const fetchCache = 'default-no-store'`


See the [`fetchCache`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#fetchcache) to see more advanced options.
See the [Route Segment Config](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config) documentation for more options.
###  `generateStaticParams`[](https://nextjs.org/docs/app/guides/caching#generatestaticparams)
For [dynamic segments](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes) (e.g. `app/blog/[slug]/page.js`), paths provided by `generateStaticParams` are cached in the Full Route Cache at build time. At request time, Next.js will also cache paths that weren't known at build time the first time they're visited.
To statically render all paths at build time, supply the full list of paths to `generateStaticParams`:
app/blog/[slug]/page.js
```
export async function generateStaticParams() {
  const posts = await fetch('https://.../posts').then((res) => res.json())

  return posts.map((post) => ({
    slug: post.slug,
  }))
}
```

To statically render a subset of paths at build time, and the rest the first time they're visited at runtime, return a partial list of paths:
app/blog/[slug]/page.js
```
export async function generateStaticParams() {
  const posts = await fetch('https://.../posts').then((res) => res.json())

  // Render the first 10 posts at build time
  return posts.slice(0, 10).map((post) => ({
    slug: post.slug,
  }))
}
```

To statically render all paths the first time they're visited, return an empty array (no paths will be rendered at build time) or utilize [`export const dynamic = 'force-static'`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamic):
app/blog/[slug]/page.js
```
export async function generateStaticParams() {
  return []
}
```

> **Good to know:** You must return an array from `generateStaticParams`, even if it's empty. Otherwise, the route will be dynamically rendered.
app/changelog/[slug]/page.js
```
export const dynamic = 'force-static'
```

To disable caching at request time, add the `export const dynamicParams = false` option in a route segment. When this config option is used, only paths provided by `generateStaticParams` will be served, and other routes will 404 or match (in the case of [catch-all routes](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#catch-all-segments)).
### React `cache` function[](https://nextjs.org/docs/app/guides/caching#react-cache-function)
The React `cache` function allows you to memoize the return value of a function, allowing you to call the same function multiple times while only executing it once.
`fetch` requests using the `GET` or `HEAD` methods are automatically memoized, so you do not need to wrap it in React `cache`. However, for other `fetch` methods, or when using data fetching libraries (such as some database, CMS, or GraphQL clients) that don't inherently memoize requests, you can use `cache` to manually memoize data requests.
utils/get-item.ts
TypeScript
JavaScript TypeScript
```
import { cache } from 'react'
import db from '@/lib/db'

export const getItem = cache(async (id: string) => {
  const item = await db.item.findUnique({ id })
  return item
})
```

[PreviousBackend for Frontend](https://nextjs.org/docs/app/guides/backend-for-frontend)[NextCI Build Caching](https://nextjs.org/docs/app/guides/ci-build-caching)
Was this helpful?
Send
* * *
* * *
#### Resources
[Docs](https://nextjs.org/docs)[Support Policy](https://nextjs.org/support-policy)[Learn](https://nextjs.org/learn)[Showcase](https://nextjs.org/showcase)[Blog](https://nextjs.org/blog)[Team](https://nextjs.org/team)[Next.js Conf](https://nextjs.org/conf)[Evals](https://nextjs.org/evals)
#### More
[Telemetry](https://nextjs.org/telemetry)[Governance](https://nextjs.org/governance)
#### About Vercel
#### Legal
Cookie Preferences
#### Subscribe to our newsletter
Stay updated on new releases and features, guides, and case studies.
Subscribe
© 2026 Vercel, Inc.
* * *
* * *
