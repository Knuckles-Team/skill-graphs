# How to implement Incremental Static Regeneration (ISR)
Last updated February 27, 2026
Examples
Incremental Static Regeneration (ISR) enables you to:
  * Update static content without rebuilding the entire site
  * Reduce server load by serving prerendered, static pages for most requests
  * Ensure proper `cache-control` headers are automatically added to pages
  * Handle large amounts of content pages without long `next build` times


Here's a minimal example:
pages/blog/[id].tsx
TypeScript
JavaScript TypeScript
```
import type { GetStaticPaths, GetStaticProps } from 'next'

interface Post {
  id: string
  title: string
  content: string
}

interface Props {
  post: Post
}

export const getStaticPaths: GetStaticPaths = async () => {
  const posts = await fetch('https://api.vercel.app/blog').then((res) =>
    res.json()
  )
  const paths = posts.map((post: Post) => ({
    params: { id: String(post.id) },
  }))

  return { paths, fallback: 'blocking' }
}

export const getStaticProps: GetStaticProps<Props> = async ({
  params,
}: {
  params: { id: string }
}) => {
  const post = await fetch(`https://api.vercel.app/blog/${params.id}`).then(
    (res) => res.json()
  )

  return {
    props: { post },
    // Next.js will invalidate the cache when a
    // request comes in, at most once every 60 seconds.
    revalidate: 60,
  }
}

export default function Page({ post }: Props) {
  return (
    <main>
      <h1>{post.title}</h1>
      <p>{post.content}</p>
    </main>
  )
}
```

Here's how this example works:
  1. During `next build`, all known blog posts are generated
  2. All requests made to these pages (e.g. `/blog/1`) are cached and instantaneous
  3. After 60 seconds has passed, the next request will still return the cached (now stale) page
  4. The cache is invalidated and a new version of the page begins generating in the background
  5. Once generated successfully, the next request will return the updated page and cache it for subsequent requests
  6. If `/blog/26` is requested, and it exists, the page will be generated on-demand. This behavior can be changed by using a different [fallback](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#fallback-false) value. However, if the post does not exist, then 404 is returned.
