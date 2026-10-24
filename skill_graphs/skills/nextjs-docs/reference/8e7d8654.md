## Relationship with `revalidateTag` and `updateTag`[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#relationship-with-revalidatetag-and-updatetag)
`revalidatePath`, [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag) and [`updateTag`](https://nextjs.org/docs/app/api-reference/functions/updateTag) serve different purposes:
  * **`revalidatePath`**: Invalidates a specific page or layout path
  * **`revalidateTag`**: Marks data with specific tags as**stale**. Applies across all pages that use those tags
  * **`updateTag`**: Expires data with specific tags. Applies across all pages that use those tags


When you call `revalidatePath`, only the specified path gets fresh data on the next visit. Other pages that use the same data tags will continue to serve cached data until those specific tags are also revalidated:
```
// Page A: /blog
const posts = await fetch('https://api.vercel.app/blog', {
  next: { tags: ['posts'] },
})

// Page B: /dashboard
const recentPosts = await fetch('https://api.vercel.app/blog?limit=5', {
  next: { tags: ['posts'] },
})
```

After calling `revalidatePath('/blog')`:
  * **Page A (/blog)** : Shows fresh data (page re-rendered)
  * **Page B (/dashboard)** : Still shows stale data (cache tag 'posts' not invalidated)


Learn about the difference between [`revalidateTag` and `updateTag`](https://nextjs.org/docs/app/api-reference/functions/updateTag#differences-from-revalidatetag).
### Building revalidation utilities[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#building-revalidation-utilities)
`revalidatePath` and `updateTag` are complementary primitives that are often used together in utility functions to ensure comprehensive data consistency across your application:
```
'use server'

import { revalidatePath, updateTag } from 'next/cache'

export async function updatePost() {
  await updatePostInDatabase()

  revalidatePath('/blog') // Refresh the blog page
  updateTag('posts') // Refresh all pages using 'posts' tag
}
```

This pattern ensures that both the specific page and any other pages using the same data remain consistent.
