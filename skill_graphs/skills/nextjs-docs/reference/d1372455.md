## Handling expected errors[](https://nextjs.org/docs/app/getting-started/error-handling#handling-expected-errors)
Expected errors are those that can occur during the normal operation of the application, such as those from [server-side form validation](https://nextjs.org/docs/app/guides/forms) or failed requests. These errors should be handled explicitly and returned to the client.
### Server Functions[](https://nextjs.org/docs/app/getting-started/error-handling#server-functions)
You can use the
For these errors, avoid using `try`/`catch` blocks and throw errors. Instead, model expected errors as return values.
app/actions.ts
TypeScript
JavaScript TypeScript
```
'use server'

export async function createPost(prevState: any, formData: FormData) {
  const title = formData.get('title')
  const content = formData.get('content')

  const res = await fetch('https://api.vercel.app/posts', {
    method: 'POST',
    body: { title, content },
  })
  const json = await res.json()

  if (!res.ok) {
    return { message: 'Failed to create post' }
  }
}
```

You can pass your action to the `useActionState` hook and use the returned `state` to display an error message.
app/ui/form.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { useActionState } from 'react'
import { createPost } from '@/app/actions'

const initialState = {
  message: '',
}

export function Form() {
  const [state, formAction, pending] = useActionState(createPost, initialState)

  return (
    <form action={formAction}>
      <label htmlFor="title">Title</label>
      <input type="text" id="title" name="title" required />
      <label htmlFor="content">Content</label>
      <textarea id="content" name="content" required />
      {state?.message && <p aria-live="polite">{state.message}</p>}
      <button disabled={pending}>Create Post</button>
    </form>
  )
}
```

### Server Components[](https://nextjs.org/docs/app/getting-started/error-handling#server-components)
When fetching data inside of a Server Component, you can use the response to conditionally render an error message or [`redirect`](https://nextjs.org/docs/app/api-reference/functions/redirect).
app/page.tsx
TypeScript
JavaScript TypeScript
```
export default async function Page() {
  const res = await fetch(`https://...`)
  const data = await res.json()

  if (!res.ok) {
    return 'There was an error.'
  }

  return '...'
}
```

### Not found[](https://nextjs.org/docs/app/getting-started/error-handling#not-found)
You can call the [`notFound`](https://nextjs.org/docs/app/api-reference/functions/not-found) function within a route segment and use the [`not-found.js`](https://nextjs.org/docs/app/api-reference/file-conventions/not-found) file to show a 404 UI.
app/blog/[slug]/page.tsx
TypeScript
JavaScript TypeScript
```
import { getPostBySlug } from '@/lib/posts'

export default async function Page({ params }: { params: { slug: string } }) {
  const { slug } = await params
  const post = getPostBySlug(slug)

  if (!post) {
    notFound()
  }

  return <div>{post.title}</div>
}
```

app/blog/[slug]/not-found.tsx
TypeScript
JavaScript TypeScript
```
export default function NotFound() {
  return <div>404 - Page Not Found</div>
}
```
