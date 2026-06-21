##  `updateTag`[](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#updatetag)
`updateTag` is specifically designed for Server Actions to immediately expire cached data for read-your-own-writes scenarios. Unlike `revalidateTag`, it can only be used within Server Actions and immediately expires the cache entry.
app/lib/actions.ts
TypeScript
JavaScript TypeScript
```
import { updateTag } from 'next/cache'
import { redirect } from 'next/navigation'

export async function createPost(formData: FormData) {
  // Create post in database
  const post = await db.post.create({
    data: {
      title: formData.get('title'),
      content: formData.get('content'),
    },
  })

  // Immediately expire cache so the new post is visible
  updateTag('posts')
  updateTag(`post-${post.id}`)

  redirect(`/posts/${post.id}`)
}
```

The key differences between `revalidateTag` and `updateTag`:
  * **`updateTag`**: Only in Server Actions, immediately expires cache, for read-your-own-writes
  * **`revalidateTag`**: In Server Actions and Route Handlers, supports stale-while-revalidate with`profile="max"`


See the [`updateTag` API reference](https://nextjs.org/docs/app/api-reference/functions/updateTag) to learn more.
