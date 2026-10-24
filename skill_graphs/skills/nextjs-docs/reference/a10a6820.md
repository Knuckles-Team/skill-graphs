## Creating a nested route[](https://nextjs.org/docs/app/getting-started/layouts-and-pages#creating-a-nested-route)
A nested route is a route composed of multiple URL segments. For example, the `/blog/[slug]` route is composed of three segments:
  * `/` (Root Segment)
  * `blog` (Segment)
  * `[slug]` (Leaf Segment)


In Next.js:
  * **Folders** are used to define the route segments that map to URL segments.
  * **Files** (like `page` and `layout`) are used to create UI that is shown for a segment.


To create nested routes, you can nest folders inside each other. For example, to add a route for `/blog`, create a folder called `blog` in the `app` directory. Then, to make `/blog` publicly accessible, add a `page.tsx` file:
![File hierarchy showing blog folder and a page.js file](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fblog-nested-route.png&w=3840&q=75)![File hierarchy showing blog folder and a page.js file](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fblog-nested-route.png&w=3840&q=75)
app/blog/page.tsx
TypeScript
JavaScript TypeScript
```
// Dummy imports
import { getPosts } from '@/lib/posts'
import { Post } from '@/ui/post'

export default async function Page() {
  const posts = await getPosts()

  return (
    <ul>
      {posts.map((post) => (
        <Post key={post.id} post={post} />
      ))}
    </ul>
  )
}
```

You can continue nesting folders to create nested routes. For example, to create a route for a specific blog post, create a new `[slug]` folder inside `blog` and add a `page` file:
![File hierarchy showing blog folder with a nested slug folder and a page.js file](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fblog-post-nested-route.png&w=3840&q=75)![File hierarchy showing blog folder with a nested slug folder and a page.js file](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fblog-post-nested-route.png&w=3840&q=75)
app/blog/[slug]/page.tsx
TypeScript
JavaScript TypeScript
```
function generateStaticParams() {}

export default function Page() {
  return <h1>Hello, Blog Post Page!</h1>
}
```

Wrapping a folder name in square brackets (e.g. `[slug]`) creates a [dynamic route segment](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes) which is used to generate multiple pages from data. e.g. blog posts, product pages, etc.
