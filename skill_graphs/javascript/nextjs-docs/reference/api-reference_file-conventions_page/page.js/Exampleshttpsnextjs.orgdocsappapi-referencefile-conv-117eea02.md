## Examples[](https://nextjs.org/docs/app/api-reference/file-conventions/page#examples)
### Displaying content based on `params`[](https://nextjs.org/docs/app/api-reference/file-conventions/page#displaying-content-based-on-params)
Using [dynamic route segments](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes), you can display or fetch specific content for the page based on the `params` prop.
app/blog/[slug]/page.tsx
TypeScript
JavaScript TypeScript
```
export default async function Page({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = await params
  return <h1>Blog Post: {slug}</h1>
}
```

### Handling filtering with `searchParams`[](https://nextjs.org/docs/app/api-reference/file-conventions/page#handling-filtering-with-searchparams)
You can use the `searchParams` prop to handle filtering, pagination, or sorting based on the query string of the URL.
app/shop/page.tsx
TypeScript
JavaScript TypeScript
```
export default async function Page({
  searchParams,
}: {
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>
}) {
  const { page = '1', sort = 'asc', query = '' } = await searchParams

  return (
    <div>
      <h1>Product Listing</h1>
      <p>Search query: {query}</p>
      <p>Current page: {page}</p>
      <p>Sort order: {sort}</p>
    </div>
  )
}
```

### Reading `searchParams` and `params` in Client Components[](https://nextjs.org/docs/app/api-reference/file-conventions/page#reading-searchparams-and-params-in-client-components)
To use `searchParams` and `params` in a Client Component (which cannot be `async`), you can use React's
app/page.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { use } from 'react'

export default function Page({
  params,
  searchParams,
}: {
  params: Promise<{ slug: string }>
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>
}) {
  const { slug } = use(params)
  const { query } = use(searchParams)
}
```
