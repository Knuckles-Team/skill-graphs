## Examples[](https://nextjs.org/docs/app/api-reference/file-conventions/not-found#examples)
### Data Fetching[](https://nextjs.org/docs/app/api-reference/file-conventions/not-found#data-fetching)
By default, `not-found` is a Server Component. You can mark it as `async` to fetch and display data:
app/not-found.tsx
TypeScript
JavaScript TypeScript
```
import Link from 'next/link'
import { headers } from 'next/headers'

export default async function NotFound() {
  const headersList = await headers()
  const domain = headersList.get('host')
  const data = await getSiteData(domain)
  return (
    <div>
      <h2>Not Found: {data.name}</h2>
      <p>Could not find requested resource</p>
      <p>
        View <Link href="/blog">all posts</Link>
      </p>
    </div>
  )
}
```

If you need to use Client Component hooks like `usePathname` to display content based on the path, you must fetch data on the client-side instead.
### Metadata[](https://nextjs.org/docs/app/api-reference/file-conventions/not-found#metadata)
For `global-not-found.js`, you can export a `metadata` object or a [`generateMetadata`](https://nextjs.org/docs/app/api-reference/functions/generate-metadata) function to customize the `<title>`, `<meta>`, and other head tags for your 404 page:
> **Good to know** : Next.js automatically injects `<meta name="robots" content="noindex" />` for pages that return a 404 status code, including `global-not-found.js` pages.
app/global-not-found.tsx
TypeScript
JavaScript TypeScript
```
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Not Found',
  description: 'The page you are looking for does not exist.',
}

export default function GlobalNotFound() {
  return (
    <html lang="en">
      <body>
        <div>
          <h1>Not Found</h1>
          <p>The page you are looking for does not exist.</p>
        </div>
      </body>
    </html>
  )
}
```
