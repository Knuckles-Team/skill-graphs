## Examples[](https://nextjs.org/docs/app/api-reference/functions/revalidateTag#examples)
The following examples demonstrate how to use `revalidateTag` in different contexts. In both cases, we're using `profile="max"` to mark data as stale and use stale-while-revalidate semantics, which is the recommended approach for most use cases.
### Server Action[](https://nextjs.org/docs/app/api-reference/functions/revalidateTag#server-action)
app/actions.ts
TypeScript
JavaScript TypeScript
```
'use server'

import { revalidateTag } from 'next/cache'

export default async function submit() {
  await addPost()
  revalidateTag('posts', 'max')
}
```

### Route Handler[](https://nextjs.org/docs/app/api-reference/functions/revalidateTag#route-handler)
app/api/revalidate/route.ts
TypeScript
JavaScript TypeScript
```
import type { NextRequest } from 'next/server'
import { revalidateTag } from 'next/cache'

export async function GET(request: NextRequest) {
  const tag = request.nextUrl.searchParams.get('tag')

  if (tag) {
    revalidateTag(tag, 'max')
    return Response.json({ revalidated: true, now: Date.now() })
  }

  return Response.json({
    revalidated: false,
    now: Date.now(),
    message: 'Missing tag to revalidate',
  })
}
```

> **Good to know** : For webhooks or third-party services that need immediate expiration, you can pass `{ expire: 0 }` as the second argument: `revalidateTag(tag, { expire: 0 })`. This pattern is necessary when external systems call your Route Handlers and require data to expire immediately. For all other cases, it's recommended to use [`updateTag`](https://nextjs.org/docs/app/api-reference/functions/updateTag) in Server Actions for immediate updates instead.
[PreviousrevalidatePath](https://nextjs.org/docs/app/api-reference/functions/revalidatePath)[Nextunauthorized](https://nextjs.org/docs/app/api-reference/functions/unauthorized)
Was this helpful?
Send
