## Examples[](https://nextjs.org/docs/app/getting-started/updating-data#examples)
### Showing a pending state[](https://nextjs.org/docs/app/getting-started/updating-data#showing-a-pending-state)
While executing a Server Function, you can show a loading indicator with React's `pending` boolean:
app/ui/button.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { useActionState, startTransition } from 'react'
import { createPost } from '@/app/actions'
import { LoadingSpinner } from '@/app/ui/loading-spinner'

export function Button() {
  const [state, action, pending] = useActionState(createPost, false)

  return (
    <button onClick={() => startTransition(action)}>
      {pending ? <LoadingSpinner /> : 'Create Post'}
    </button>
  )
}
```

### Refreshing[](https://nextjs.org/docs/app/getting-started/updating-data#refreshing)
After a mutation, you may want to refresh the current page to show the latest data. You can do this by calling [`refresh`](https://nextjs.org/docs/app/api-reference/functions/refresh) from `next/cache` in a Server Action:
app/lib/actions.ts
TypeScript
JavaScript TypeScript
```
'use server'

import { refresh } from 'next/cache'

export async function updatePost(formData: FormData) {
  // Update data
  // ...

  refresh()
}
```

This refreshes the client router, ensuring the UI reflects the latest state. The `refresh()` function does not revalidate tagged data. To revalidate tagged data, use [`updateTag`](https://nextjs.org/docs/app/api-reference/functions/updateTag) or [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag) instead.
### Revalidating[](https://nextjs.org/docs/app/getting-started/updating-data#revalidating)
After performing an update, you can revalidate the Next.js cache and show the updated data by calling [`revalidatePath`](https://nextjs.org/docs/app/api-reference/functions/revalidatePath) or [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag) within the Server Function:
app/lib/actions.ts
TypeScript
JavaScript TypeScript
```
import { revalidatePath } from 'next/cache'

export async function createPost(formData: FormData) {
  'use server'
  // Update data
  // ...

  revalidatePath('/posts')
}
```

### Redirecting[](https://nextjs.org/docs/app/getting-started/updating-data#redirecting)
You may want to redirect the user to a different page after performing an update. You can do this by calling [`redirect`](https://nextjs.org/docs/app/api-reference/functions/redirect) within the Server Function.
app/lib/actions.ts
TypeScript
JavaScript TypeScript
```
'use server'

import { revalidatePath } from 'next/cache'
import { redirect } from 'next/navigation'

export async function createPost(formData: FormData) {
  // Update data
  // ...

  revalidatePath('/posts')
  redirect('/posts')
}
```

Calling `redirect` [throws](https://nextjs.org/docs/app/api-reference/functions/redirect#behavior) a framework handled control-flow exception. Any code after it won't execute. If you need fresh data, call [`revalidatePath`](https://nextjs.org/docs/app/api-reference/functions/revalidatePath) or [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag) beforehand.
### Cookies[](https://nextjs.org/docs/app/getting-started/updating-data#cookies)
You can `get`, `set`, and `delete` cookies inside a Server Action using the [`cookies`](https://nextjs.org/docs/app/api-reference/functions/cookies) API.
When you [set or delete](https://nextjs.org/docs/app/api-reference/functions/cookies#understanding-cookie-behavior-in-server-functions) a cookie in a Server Action, Next.js re-renders the current page and its layouts on the server so the **UI reflects the new cookie value**.
> **Good to know** : The server update applies to the current React tree, re-rendering, mounting, or unmounting components, as needed. Client state is preserved for re-rendered components, and effects re-run if their dependencies changed.
app/actions.ts
TypeScript
JavaScript TypeScript
```
'use server'

import { cookies } from 'next/headers'

export async function exampleAction() {
  const cookieStore = await cookies()

  // Get cookie
  cookieStore.get('name')?.value

  // Set cookie
  cookieStore.set('name', 'Delba')

  // Delete cookie
  cookieStore.delete('name')
}
```

### useEffect[](https://nextjs.org/docs/app/getting-started/updating-data#useeffect)
You can use the React `onKeyDown` for app shortcuts, an intersection observer hook for infinite scrolling, or when the component mounts to update a view count:
app/view-count.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { incrementViews } from './actions'
import { useState, useEffect, useTransition } from 'react'

export default function ViewCount({ initialViews }: { initialViews: number }) {
  const [views, setViews] = useState(initialViews)
  const [isPending, startTransition] = useTransition()

  useEffect(() => {
    startTransition(async () => {
      const updatedViews = await incrementViews()
      setViews(updatedViews)
    })
  }, [])

  // You can use `isPending` to give users feedback
  return <p>Total Views: {views}</p>
}
```
