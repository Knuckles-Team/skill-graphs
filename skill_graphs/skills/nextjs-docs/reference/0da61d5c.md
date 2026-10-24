## Possible Ways to Fix It[](https://nextjs.org/docs/messages/no-async-client-component#possible-ways-to-fix-it)
  1. **Convert to a Server Component** : If possible, convert your Client Component to a Server Component. This allows you to use `async`/`await` directly in your component.
  2. **Remove the`async` keyword**: If you need to keep it as a Client Component, remove the `async` keyword and handle data fetching differently.
  3. **Use React Hooks for data fetching** : Utilize hooks like `useEffect` for client-side data fetching, or use third-party libraries.
  4. **Leverage the`use` API with a Context Provider**: Pass promises to child components using context, then resolve them with the `use` API.


### Recommended: Server-side data fetching[](https://nextjs.org/docs/messages/no-async-client-component#recommended-server-side-data-fetching)
We recommend fetching data on the server. For example:
app/page.tsx
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

### Using `use` with Context Provider[](https://nextjs.org/docs/messages/no-async-client-component#using-use-with-context-provider)
Another pattern to explore is using the React `use` API with a Context Provider. This allows you to pass Promises to child components and resolve them using the `use` API . Here's an example:
First, let's create a separate file for the context provider:
app/context.tsx
```
'use client'

import { createContext, useContext } from 'react'

export const BlogContext = createContext<Promise<any> | null>(null)

export function BlogProvider({
  children,
  blogPromise,
}: {
  children: React.ReactNode
  blogPromise: Promise<any>
}) {
  return (
    <BlogContext.Provider value={blogPromise}>{children}</BlogContext.Provider>
  )
}

export function useBlogContext() {
  const context = useContext(BlogContext)
  if (!context) {
    throw new Error('useBlogContext must be used within a BlogProvider')
  }
  return context
}
```

Now, let's create the Promise in a Server Component and stream it to the client:
app/page.tsx
```
import { BlogProvider } from './context'

export default function Page() {
  const blogPromise = fetch('https://api.vercel.app/blog').then((res) =>
    res.json()
  )

  return (
    <BlogProvider blogPromise={blogPromise}>
      <BlogPosts />
    </BlogProvider>
  )
}
```

Here is the blog posts component:
app/blog-posts.tsx
```
'use client'

import { use } from 'react'
import { useBlogContext } from './context'

export function BlogPosts() {
  const blogPromise = useBlogContext()
  const posts = use(blogPromise)

  return <div>{posts.length} blog posts</div>
}
```

This pattern allows you to start data fetching early and pass the Promise down to child components, which can then use the `use` API to access the data when it's ready.
### Client-side data fetching[](https://nextjs.org/docs/messages/no-async-client-component#client-side-data-fetching)
In scenarios where client fetching is needed, you can call `fetch` in `useEffect` (not recommended), or lean on popular React libraries in the community (such as
app/page.tsx
```
'use client'

import { useState, useEffect } from 'react'

export function Posts() {
  const [posts, setPosts] = useState(null)

  useEffect(() => {
    async function fetchPosts() {
      const res = await fetch('https://api.vercel.app/blog')
      const data = await res.json()
      setPosts(data)
    }
    fetchPosts()
  }, [])

  if (!posts) return <div>Loading...</div>

  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  )
}
```

Was this helpful?
Send
* * *
* * *
#### Resources
[Docs](https://nextjs.org/docs)[Support Policy](https://nextjs.org/support-policy)[Learn](https://nextjs.org/learn)[Showcase](https://nextjs.org/showcase)[Blog](https://nextjs.org/blog)[Team](https://nextjs.org/team)[Next.js Conf](https://nextjs.org/conf)[Evals](https://nextjs.org/evals)
#### More
[Telemetry](https://nextjs.org/telemetry)[Governance](https://nextjs.org/governance)
#### About Vercel
#### Legal
Cookie Preferences
#### Subscribe to our newsletter
Stay updated on new releases and features, guides, and case studies.
Subscribe
© 2026 Vercel, Inc.
* * *
* * *
