## Examples[](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#examples)
### With `generateStaticParams`[](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#with-generatestaticparams-1)
The [`generateStaticParams`](https://nextjs.org/docs/app/api-reference/functions/generate-static-params) function can be used to [statically generate](https://nextjs.org/docs/app/guides/caching#static-rendering) routes at build time instead of on-demand at request time.
app/blog/[slug]/page.tsx
TypeScript
JavaScript TypeScript
```
export async function generateStaticParams() {
  const posts = await fetch('https://.../posts').then((res) => res.json())

  return posts.map((post) => ({
    slug: post.slug,
  }))
}
```

When using `fetch` inside the `generateStaticParams` function, the requests are [automatically deduplicated](https://nextjs.org/docs/app/guides/caching#request-memoization). This avoids multiple network calls for the same data Layouts, Pages, and other `generateStaticParams` functions, speeding up build time.
### Dynamic GET Route Handlers with `generateStaticParams`[](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#dynamic-get-route-handlers-with-generatestaticparams)
`generateStaticParams` also works with dynamic [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route) to statically generate API responses at build time:
app/api/posts/[id]/route.ts
TypeScript
JavaScript TypeScript
```
export async function generateStaticParams() {
  const posts: { id: number }[] = await fetch(
    'https://api.vercel.app/blog'
  ).then((res) => res.json())

  return posts.map((post) => ({
    id: `${post.id}`,
  }))
}

export async function GET(
  request: Request,
  { params }: RouteContext<'/api/posts/[id]'>
) {
  const { id } = await params
  const res = await fetch(`https://api.vercel.app/blog/${id}`)

  if (!res.ok) {
    return Response.json({ error: 'Post not found' }, { status: 404 })
  }

  const post = await res.json()
  return Response.json(post)
}
```

In this example, route handlers for all blog post IDs returned by `generateStaticParams` will be statically generated at build time. Requests to other IDs will be handled dynamically at request time.
