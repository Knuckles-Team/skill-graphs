## Generated metadata[](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#generated-metadata)
You can use [`generateMetadata`](https://nextjs.org/docs/app/api-reference/functions/generate-metadata) function to `fetch` metadata that depends on data. For example, to fetch the title and description for a specific blog post:
app/blog/[slug]/page.tsx
TypeScript
JavaScript TypeScript
```
import type { Metadata, ResolvingMetadata } from 'next'

type Props = {
  params: Promise<{ slug: string }>
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>
}

export async function generateMetadata(
  { params, searchParams }: Props,
  parent: ResolvingMetadata
): Promise<Metadata> {
  const slug = (await params).slug

  // fetch post information
  const post = await fetch(`https://api.vercel.app/blog/${slug}`).then((res) =>
    res.json()
  )

  return {
    title: post.title,
    description: post.description,
  }
}

export default function Page({ params, searchParams }: Props) {}
```

### Streaming metadata[](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#streaming-metadata)
For dynamically rendered pages, Next.js streams metadata separately, injecting it into the HTML once `generateMetadata` resolves, without blocking UI rendering.
Streaming metadata improves perceived performance by allowing visual content to stream first.
Streaming metadata is **disabled for bots and crawlers** that expect metadata to be in the `<head>` tag (e.g. `Twitterbot`, `Slackbot`, `Bingbot`). These are detected by using the User Agent header from the incoming request.
You can customize or **disable** streaming metadata completely, with the [`htmlLimitedBots`](https://nextjs.org/docs/app/api-reference/config/next-config-js/htmlLimitedBots#disabling) option in your Next.js config file.
Statically rendered pages don’t use streaming since metadata is resolved at build time.
Learn more about [streaming metadata](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#streaming-metadata).
### Memoizing data requests[](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#memoizing-data-requests)
There may be cases where you need to fetch the **same** data for metadata and the page itself. To avoid duplicate requests, you can use React's
app/lib/data.ts
TypeScript
JavaScript TypeScript
```
import { cache } from 'react'
import { db } from '@/app/lib/db'

// getPost will be used twice, but execute only once
export const getPost = cache(async (slug: string) => {
  const res = await db.query.posts.findFirst({ where: eq(posts.slug, slug) })
  return res
})
```

app/blog/[slug]/page.tsx
TypeScript
JavaScript TypeScript
```
import { getPost } from '@/app/lib/data'

export async function generateMetadata({
  params,
}: {
  params: { slug: string }
}) {
  const post = await getPost(params.slug)
  return {
    title: post.title,
    description: post.description,
  }
}

export default async function Page({ params }: { params: { slug: string } }) {
  const post = await getPost(params.slug)
  return <div>{post.title}</div>
}
```
