## Examples[](https://nextjs.org/docs/app/api-reference/functions/updateTag#examples)
### Server Action with Read-Your-Own-Writes[](https://nextjs.org/docs/app/api-reference/functions/updateTag#server-action-with-read-your-own-writes)
app/actions.ts
TypeScript
JavaScript TypeScript
```
'use server'

import { updateTag } from 'next/cache'
import { redirect } from 'next/navigation'

export async function createPost(formData: FormData) {
  const title = formData.get('title')
  const content = formData.get('content')

  // Create the post in your database
  const post = await db.post.create({
    data: { title, content },
  })

  // Invalidate cache tags so the new post is immediately visible
  // 'posts' tag: affects any page that displays a list of posts
  updateTag('posts')
  // 'post-{id}' tag: affects the individual post detail page
  updateTag(`post-${post.id}`)

  // Redirect to the new post - user will see fresh data, not cached
  redirect(`/posts/${post.id}`)
}
```

### Error when used outside Server Actions[](https://nextjs.org/docs/app/api-reference/functions/updateTag#error-when-used-outside-server-actions)
app/api/posts/route.ts
TypeScript
JavaScript TypeScript
```
import { updateTag } from 'next/cache'

export async function POST() {
  // This will throw an error
  updateTag('posts')
  // Error: updateTag can only be called from within a Server Action

  // Use revalidateTag instead in Route Handlers
  revalidateTag('posts', 'max')
}
```
