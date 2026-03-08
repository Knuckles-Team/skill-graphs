## Deduplicate requests and cache data[](https://nextjs.org/docs/app/getting-started/fetching-data#deduplicate-requests-and-cache-data)
One way to deduplicate `fetch` requests is with [request memoization](https://nextjs.org/docs/app/guides/caching#request-memoization). With this mechanism, `fetch` calls using `GET` or `HEAD` with the same URL and options in a single render pass are combined into one request. This happens automatically, and you can [opt out](https://nextjs.org/docs/app/guides/caching#opting-out) by passing an Abort signal to `fetch`.
Request memoization is scoped to the lifetime of a request.
You can also deduplicate `fetch` requests by using Next.js’ [Data Cache](https://nextjs.org/docs/app/guides/caching#data-cache), for example by setting `cache: 'force-cache'` in your `fetch` options.
Data Cache allows sharing data across the current render pass and incoming requests.
If you are _not_ using `fetch`, and instead using an ORM or database directly, you can wrap your data access with the
app/lib/data.ts
TypeScript
JavaScript TypeScript
```
import { cache } from 'react'
import { db, posts, eq } from '@/lib/db'

export const getPost = cache(async (id: string) => {
  const post = await db.query.posts.findFirst({
    where: eq(posts.id, parseInt(id)),
  })
})
```
