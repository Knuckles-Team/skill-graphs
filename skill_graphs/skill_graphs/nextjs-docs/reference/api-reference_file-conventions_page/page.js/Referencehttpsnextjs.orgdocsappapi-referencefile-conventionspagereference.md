## Reference[](https://nextjs.org/docs/app/api-reference/file-conventions/page#reference)
### Props[](https://nextjs.org/docs/app/api-reference/file-conventions/page#props)
####  `params` (optional)[](https://nextjs.org/docs/app/api-reference/file-conventions/page#params-optional)
A promise that resolves to an object containing the [dynamic route parameters](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes) from the root segment down to that page.
app/shop/[slug]/page.tsx
TypeScript
JavaScript TypeScript
```
export default async function Page({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = await params
}
```

Example Route | URL | `params`
---|---|---
`app/shop/[slug]/page.js` | `/shop/1` | `Promise<{ slug: '1' }>`
`app/shop/[category]/[item]/page.js` | `/shop/1/2` | `Promise<{ category: '1', item: '2' }>`
`app/shop/[...slug]/page.js` | `/shop/1/2` | `Promise<{ slug: ['1', '2'] }>`
  * Since the `params` prop is a promise, you must use `async/await` or React's
    * In version 14 and earlier, `params` was a synchronous prop. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.


####  `searchParams` (optional)[](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional)
A promise that resolves to an object containing the
app/shop/page.tsx
TypeScript
JavaScript TypeScript
```
export default async function Page({
  searchParams,
}: {
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>
}) {
  const filters = (await searchParams).filters
}
```

Client Component **pages** can also access `searchParams` using React’s
app/shop/page.tsx
TypeScript
JavaScript TypeScript
```
'use client'
import { use } from 'react'

export default function Page({
  searchParams,
}: {
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>
}) {
  const filters = use(searchParams).filters
}
```

Example URL | `searchParams`
---|---
`/shop?a=1` | `Promise<{ a: '1' }>`
`/shop?a=1&b=2` | `Promise<{ a: '1', b: '2' }>`
`/shop?a=1&a=2` | `Promise<{ a: ['1', '2'] }>`
  * Since the `searchParams` prop is a promise. You must use `async/await` or React's
    * In version 14 and earlier, `searchParams` was a synchronous prop. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.
  * `searchParams` is a **[Dynamic API](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)** whose values cannot be known ahead of time. Using it will opt the page into **[dynamic rendering](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)** at request time.
  * `searchParams` is a plain JavaScript object, not a `URLSearchParams` instance.


### Page Props Helper[](https://nextjs.org/docs/app/api-reference/file-conventions/page#page-props-helper)
You can type pages with `PageProps` to get strongly typed `params` and `searchParams` from the route literal. `PageProps` is a globally available helper.
app/blog/[slug]/page.tsx
```
export default async function Page(props: PageProps<'/blog/[slug]'>) {
  const { slug } = await props.params
  const query = await props.searchParams
  return <h1>Blog Post: {slug}</h1>
}
```

> **Good to know**
>   * Using a literal route (e.g. `'/blog/[slug]'`) enables autocomplete and strict keys for `params`.
>   * Static routes resolve `params` to `{}`.
>   * Types are generated during `next dev`, `next build`, or with `next typegen`.
>   * After type generation, the `PageProps` helper is globally available. It doesn't need to be imported.
>
