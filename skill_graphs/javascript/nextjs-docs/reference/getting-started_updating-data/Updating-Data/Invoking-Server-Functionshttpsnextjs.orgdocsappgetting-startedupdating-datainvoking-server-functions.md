## Invoking Server Functions[](https://nextjs.org/docs/app/getting-started/updating-data#invoking-server-functions)
There are two main ways you can invoke a Server Function:
  1. [Forms](https://nextjs.org/docs/app/getting-started/updating-data#forms) in Server and Client Components
  2. [Event Handlers](https://nextjs.org/docs/app/getting-started/updating-data#event-handlers) and [useEffect](https://nextjs.org/docs/app/getting-started/updating-data#useeffect) in Client Components


> **Good to know:** Server Functions are designed for server-side mutations. The client currently dispatches and awaits them one at a time. This is an implementation detail and may change. If you need parallel data fetching, use [data fetching](https://nextjs.org/docs/app/getting-started/fetching-data#server-components) in Server Components, or perform parallel work inside a single Server Function or [Route Handler](https://nextjs.org/docs/app/guides/backend-for-frontend#manipulating-data).
### Forms[](https://nextjs.org/docs/app/getting-started/updating-data#forms)
React extends the HTML `action` prop.
When invoked in a form, the function automatically receives the
app/ui/form.tsx
TypeScript
JavaScript TypeScript
```
import { createPost } from '@/app/actions'

export function Form() {
  return (
    <form action={createPost}>
      <input type="text" name="title" />
      <input type="text" name="content" />
      <button type="submit">Create</button>
    </form>
  )
}
```

app/actions.ts
TypeScript
JavaScript TypeScript
```
'use server'

export async function createPost(formData: FormData) {
  const title = formData.get('title')
  const content = formData.get('content')

  // Update data
  // Revalidate cache
}
```

### Event Handlers[](https://nextjs.org/docs/app/getting-started/updating-data#event-handlers)
You can invoke a Server Function in a Client Component by using event handlers such as `onClick`.
app/like-button.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { incrementLike } from './actions'
import { useState } from 'react'

export default function LikeButton({ initialLikes }: { initialLikes: number }) {
  const [likes, setLikes] = useState(initialLikes)

  return (
    <>
      <p>Total Likes: {likes}</p>
      <button
        onClick={async () => {
          const updatedLikes = await incrementLike()
          setLikes(updatedLikes)
        }}
      >
        Like
      </button>
    </>
  )
}
```
