## Examples[](https://nextjs.org/docs/app/api-reference/functions/refresh#examples)
app/actions.ts
TypeScript
JavaScript TypeScript
```
'use server'

import { refresh } from 'next/cache'

export async function createPost(formData: FormData) {
  const title = formData.get('title')
  const content = formData.get('content')

  // Create the post in your database
  const post = await db.post.create({
    data: { title, content },
  })

  refresh()
}
```

### Error when used outside Server Actions[](https://nextjs.org/docs/app/api-reference/functions/refresh#error-when-used-outside-server-actions)
app/api/posts/route.ts
TypeScript
JavaScript TypeScript
```
import { refresh } from 'next/cache'

export async function POST() {
  // This will throw an error
  refresh()
}
```

[Previousredirect](https://nextjs.org/docs/app/api-reference/functions/redirect)[NextrevalidatePath](https://nextjs.org/docs/app/api-reference/functions/revalidatePath)
Was this helpful?
Send
