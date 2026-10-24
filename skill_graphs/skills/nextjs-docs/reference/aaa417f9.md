## Behavior[](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#behavior)
  * Since the `params` prop is a promise. You must use `async`/`await` or React's use function to access the values.
    * In version 14 and earlier, `params` was a synchronous prop. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.


### With Cache Components[](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#with-cache-components)
When using [Cache Components](https://nextjs.org/docs/app/getting-started/cache-components) with dynamic route segments, how you handle params depends on whether you use [`generateStaticParams`](https://nextjs.org/docs/app/api-reference/functions/generate-static-params).
Without `generateStaticParams`, param values are unknown during prerendering, making params runtime data. You must wrap param access in `<Suspense>` boundaries to provide fallback UI.
With `generateStaticParams`, you provide sample param values that can be used at build time. The build process validates that dynamic content and other runtime APIs are correctly handled, then generates static HTML files for the samples. Pages rendered with runtime params are saved to disk after a successful first request.
The sections below demonstrate both patterns.
#### Without `generateStaticParams`[](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#without-generatestaticparams)
All params are runtime data. Param access must be wrapped by Suspense fallback UI. Next.js generates a static shell at build time, and content loads on each request.
> **Good to know** : You can also use [`loading.tsx`](https://nextjs.org/docs/app/api-reference/file-conventions/loading) for page-level fallback UI.
app/blog/[slug]/page.tsx
```
import { Suspense } from 'react'

export default function Page({ params }: PageProps<'/blog/[slug]'>) {
  return (
    <div>
      <h1>Blog Post</h1>
      <Suspense fallback={<div>Loading...</div>}>
        {params.then(({ slug }) => (
          <Content slug={slug} />
        ))}
      </Suspense>
    </div>
  )
}

async function Content({ slug }: { slug: string }) {
  const res = await fetch(`https://api.vercel.app/blog/${slug}`)
  const post = await res.json()

  return (
    <article>
      <h2>{post.title}</h2>
      <p>{post.content}</p>
    </article>
  )
}
```

#### With `generateStaticParams`[](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#with-generatestaticparams)
Provide params ahead of time to prerender pages at build time. You can prerender all routes or a subset depending on your needs.
During the build process, the route is executed with each sample param to collect the HTML result. If dynamic content or runtime data are accessed incorrectly, the build will fail.
app/blog/[slug]/page.tsx
```
import { Suspense } from 'react'

export async function generateStaticParams() {
  return [{ slug: '1' }, { slug: '2' }, { slug: '3' }]
}

export default async function Page({ params }: PageProps<'/blog/[slug]'>) {
  const { slug } = await params

  return (
    <div>
      <h1>Blog Post</h1>
      <Content slug={slug} />
    </div>
  )
}

async function Content({ slug }: { slug: string }) {
  const post = await getPost(slug)
  return (
    <article>
      <h2>{post.title}</h2>
      <p>{post.content}</p>
    </article>
  )
}

async function getPost(slug: string) {
  'use cache'
  const res = await fetch(`https://api.vercel.app/blog/${slug}`)
  return res.json()
}
```

Build-time validation only covers code paths that execute with the sample params. If your route has conditional logic that accesses runtime APIs for certain param values not in your samples, those branches won't be validated at build time:
app/blog/[slug]/page.tsx
```
import { cookies } from 'next/headers'

export async function generateStaticParams() {
  return [{ slug: 'public-post' }, { slug: 'hello-world' }]
}

export default async function Page({ params }: PageProps<'/blog/[slug]'>) {
  const { slug } = await params

  if (slug.startsWith('private-')) {
    // This branch is never executed at build time
    // Runtime requests for 'private-*' slugs will error
    return <PrivatePost slug={slug} />
  }

  return <PublicPost slug={slug} />
}

async function PrivatePost({ slug }: { slug: string }) {
  const token = (await cookies()).get('token')
  // ... fetch and render private post using token for auth
}
```

For runtime params not returned by `generateStaticParams`, validation occurs during the first request. In the example above, requests for slugs starting with `private-` will fail because `PrivatePost` accesses `cookies()` without a Suspense boundary. Other runtime params that don't hit the conditional branch will render successfully and be saved to disk for subsequent requests.
To fix this, wrap `PrivatePost` with Suspense:
app/blog/[slug]/page.tsx
```
import { Suspense } from 'react'
import { cookies } from 'next/headers'

export async function generateStaticParams() {
  return [{ slug: 'public-post' }, { slug: 'hello-world' }]
}

export default async function Page({ params }: PageProps<'/blog/[slug]'>) {
  const { slug } = await params

  if (slug.startsWith('private-')) {
    return (
      <Suspense fallback={<div>Loading...</div>}>
        <PrivatePost slug={slug} />
      </Suspense>
    )
  }

  return <PublicPost slug={slug} />
}

async function PrivatePost({ slug }: { slug: string }) {
  const token = (await cookies()).get('token')
  // ... fetch and render private post using token for auth
}
```
