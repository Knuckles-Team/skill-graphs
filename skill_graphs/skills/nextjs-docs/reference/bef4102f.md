##  `not-found.js`[](https://nextjs.org/docs/app/api-reference/file-conventions/not-found#not-foundjs)
The **not-found** file is used to render UI when the [`notFound`](https://nextjs.org/docs/app/api-reference/functions/not-found) function is thrown within a route segment. Along with serving a custom UI, Next.js will return a `200` HTTP status code for streamed responses, and `404` for non-streamed responses (see [Status Codes](https://nextjs.org/docs/app/api-reference/file-conventions/loading#status-codes) for details about SEO).
app/not-found.tsx
TypeScript
JavaScript TypeScript
```
import Link from 'next/link'

export default function NotFound() {
  return (
    <div>
      <h2>Not Found</h2>
      <p>Could not find requested resource</p>
      <Link href="/">Return Home</Link>
    </div>
  )
}
```
