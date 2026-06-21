## Fetching data[](https://nextjs.org/docs/app/getting-started/fetching-data#fetching-data)
### Server Components[](https://nextjs.org/docs/app/getting-started/fetching-data#server-components)
You can fetch data in Server Components using any asynchronous I/O, such as:
  1. The [`fetch` API](https://nextjs.org/docs/app/getting-started/fetching-data#with-the-fetch-api)
  2. An [ORM or database](https://nextjs.org/docs/app/getting-started/fetching-data#with-an-orm-or-database)
  3. Reading from the filesystem using Node.js APIs like `fs`


#### With the `fetch` API[](https://nextjs.org/docs/app/getting-started/fetching-data#with-the-fetch-api)
To fetch data with the `fetch` API, turn your component into an asynchronous function, and await the `fetch` call. For example:
app/blog/page.tsx
TypeScript
JavaScript TypeScript
```
export default async function Page() {
  const data = await fetch('https://api.vercel.app/blog')
  const posts = await data.json()
  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  )
}
```

> **Good to know:**
>   * `fetch` responses are not cached by default. However, Next.js will [pre-render](https://nextjs.org/docs/app/guides/caching#static-rendering) the route and the output will be cached for improved performance. If you'd like to opt into [dynamic rendering](https://nextjs.org/docs/app/guides/caching#dynamic-rendering), use the `{ cache: 'no-store' }` option. See the [`fetch` API Reference](https://nextjs.org/docs/app/api-reference/functions/fetch).
>   * During development, you can log `fetch` calls for better visibility and debugging. See the [`logging` API reference](https://nextjs.org/docs/app/api-reference/config/next-config-js/logging).
>

#### With an ORM or database[](https://nextjs.org/docs/app/getting-started/fetching-data#with-an-orm-or-database)
Since Server Components are rendered on the server, you can safely make database queries using an ORM or database client. Turn your component into an asynchronous function, and await the call:
app/blog/page.tsx
TypeScript
JavaScript TypeScript
```
import { db, posts } from '@/lib/db'

export default async function Page() {
  const allPosts = await db.select().from(posts)
  return (
    <ul>
      {allPosts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  )
}
```

### Client Components[](https://nextjs.org/docs/app/getting-started/fetching-data#client-components)
There are two ways to fetch data in Client Components, using:
  1. React's
  2. A community library like


#### Streaming data with the `use` API[](https://nextjs.org/docs/app/getting-started/fetching-data#streaming-data-with-the-use-api)
You can use React's [stream](https://nextjs.org/docs/app/getting-started/fetching-data#streaming) data from the server to client. Start by fetching data in your Server component, and pass the promise to your Client Component as prop:
app/blog/page.tsx
TypeScript
JavaScript TypeScript
```
import Posts from '@/app/ui/posts'
import { Suspense } from 'react'

export default function Page() {
  // Don't await the data fetching function
  const posts = getPosts()

  return (
    <Suspense fallback={<div>Loading...</div>}>
      <Posts posts={posts} />
    </Suspense>
  )
}
```

Then, in your Client Component, use the `use` API to read the promise:
app/ui/posts.tsx
TypeScript
JavaScript TypeScript
```
'use client'
import { use } from 'react'

export default function Posts({
  posts,
}: {
  posts: Promise<{ id: string; title: string }[]>
}) {
  const allPosts = use(posts)

  return (
    <ul>
      {allPosts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  )
}
```

In the example above, the `<Posts>` component is wrapped in a [streaming](https://nextjs.org/docs/app/getting-started/fetching-data#streaming).
#### Community libraries[](https://nextjs.org/docs/app/getting-started/fetching-data#community-libraries)
You can use a community library like
app/blog/page.tsx
TypeScript
JavaScript TypeScript
```
'use client'
import useSWR from 'swr'

const fetcher = (url) => fetch(url).then((r) => r.json())

export default function BlogPage() {
  const { data, error, isLoading } = useSWR(
    'https://api.vercel.app/blog',
    fetcher
  )

  if (isLoading) return <div>Loading...</div>
  if (error) return <div>Error: {error.message}</div>

  return (
    <ul>
      {data.map((post: { id: string; title: string }) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  )
}
```
