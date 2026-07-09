## Examples[](https://nextjs.org/docs/app/guides/incremental-static-regeneration#examples)
### Time-based revalidation[](https://nextjs.org/docs/app/guides/incremental-static-regeneration#time-based-revalidation)
This fetches and displays a list of blog posts on /blog. After an hour has passed, the next visitor will still receive the cached (stale) version of the page immediately for a fast response. Simultaneously, Next.js triggers regeneration of a fresh version in the background. Once the new version is successfully generated, it replaces the cached version, and subsequent visitors will receive the updated content.
app/blog/page.tsx
TypeScript
JavaScript TypeScript
```
interface Post {
  id: string
  title: string
  content: string
}

export const revalidate = 3600 // invalidate every hour

export default async function Page() {
  const data = await fetch('https://api.vercel.app/blog')
  const posts: Post[] = await data.json()
  return (
    <main>
      <h1>Blog Posts</h1>
      <ul>
        {posts.map((post) => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul>
    </main>
  )
}
```

We recommend setting a high revalidation time. For instance, 1 hour instead of 1 second. If you need more precision, consider using on-demand revalidation. If you need real-time data, consider switching to [dynamic rendering](https://nextjs.org/docs/app/guides/caching#dynamic-rendering).
### On-demand revalidation with `revalidatePath`[](https://nextjs.org/docs/app/guides/incremental-static-regeneration#on-demand-revalidation-with-revalidatepath)
For a more precise method of revalidation, invalidate cached pages on-demand with the `revalidatePath` function.
For example, this Server Action would get called after adding a new post. Regardless of how you retrieve your data in your Server Component, either using `fetch` or connecting to a database, this will invalidate the cache for the entire route. The next request to that route will trigger regeneration and serve fresh data, which will then be cached for subsequent requests.
> **Note:** `revalidatePath` invalidates the cache entries but regeneration happens on the next request. If you want to eagerly regenerate the cache entry immediately instead of waiting for the next request, you can use the Pages router [`res.revalidate`](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#on-demand-validation-with-resrevalidate) method. We're working on adding new methods to provide eager regeneration capabilities for the App Router.
app/actions.ts
TypeScript
JavaScript TypeScript
```
'use server'

import { revalidatePath } from 'next/cache'

export async function createPost() {
  // Invalidate the cache for the /posts route
  revalidatePath('/posts')
}
```

### On-demand revalidation with `revalidateTag`[](https://nextjs.org/docs/app/guides/incremental-static-regeneration#on-demand-revalidation-with-revalidatetag)
For most use cases, prefer revalidating entire paths. If you need more granular control, you can use the `revalidateTag` function. For example, you can tag individual `fetch` calls:
app/blog/page.tsx
TypeScript
JavaScript TypeScript
```
export default async function Page() {
  const data = await fetch('https://api.vercel.app/blog', {
    next: { tags: ['posts'] },
  })
  const posts = await data.json()
  // ...
}
```

If you are using an ORM or connecting to a database, you can use `unstable_cache`:
app/blog/page.tsx
TypeScript
JavaScript TypeScript
```
import { unstable_cache } from 'next/cache'
import { db, posts } from '@/lib/db'

const getCachedPosts = unstable_cache(
  async () => {
    return await db.select().from(posts)
  },
  ['posts'],
  { revalidate: 3600, tags: ['posts'] }
)

export default async function Page() {
  const posts = getCachedPosts()
  // ...
}
```

You can then use `revalidateTag` in a [Server Actions](https://nextjs.org/docs/app/getting-started/updating-data) or [Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route):
app/actions.ts
TypeScript
JavaScript TypeScript
```
'use server'

import { revalidateTag } from 'next/cache'

export async function createPost() {
  // Invalidate all data tagged with 'posts'
  revalidateTag('posts')
}
```

### Handling uncaught exceptions[](https://nextjs.org/docs/app/guides/incremental-static-regeneration#handling-uncaught-exceptions)
If an error is thrown while attempting to revalidate data, the last successfully generated data will continue to be served from the cache. On the next subsequent request, Next.js will retry revalidating the data. [Learn more about error handling](https://nextjs.org/docs/app/getting-started/error-handling).
### Customizing the cache location[](https://nextjs.org/docs/app/guides/incremental-static-regeneration#customizing-the-cache-location)
You can configure the Next.js cache location if you want to persist cached pages and data to durable storage, or share the cache across multiple containers or instances of your Next.js application. [Learn more](https://nextjs.org/docs/app/guides/self-hosting#caching-and-isr).
