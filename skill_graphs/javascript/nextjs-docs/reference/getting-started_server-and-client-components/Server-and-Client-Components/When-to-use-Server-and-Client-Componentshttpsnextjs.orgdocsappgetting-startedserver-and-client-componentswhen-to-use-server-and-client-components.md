## When to use Server and Client Components?[](https://nextjs.org/docs/app/getting-started/server-and-client-components#when-to-use-server-and-client-components)
The client and server environments have different capabilities. Server and Client components allow you to run logic in each environment depending on your use case.
Use **Client Components** when you need:
  * `onClick`, `onChange`.
  * `useEffect`.
  * Browser-only APIs. E.g. `localStorage`, `window`, `Navigator.geolocation`, etc.


Use **Server Components** when you need:
  * Fetch data from databases or APIs close to the source.
  * Use API keys, tokens, and other secrets without exposing them to the client.
  * Reduce the amount of JavaScript sent to the browser.
  * Improve the


For example, the `<Page>` component is a Server Component that fetches data about a post, and passes it as props to the `<LikeButton>` which handles client-side interactivity.
app/[id]/page.tsx
TypeScript
JavaScript TypeScript
```
import LikeButton from '@/app/ui/like-button'
import { getPost } from '@/lib/data'

export default async function Page({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  const post = await getPost(id)

  return (
    <div>
      <main>
        <h1>{post.title}</h1>
        {/* ... */}
        <LikeButton likes={post.likes} />
      </main>
    </div>
  )
}
```

app/ui/like-button.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { useState } from 'react'

export default function LikeButton({ likes }: { likes: number }) {
  // ...
}
```
