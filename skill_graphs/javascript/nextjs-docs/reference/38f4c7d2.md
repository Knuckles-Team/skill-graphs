## Convention[](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#convention)
A Dynamic Segment can be created by wrapping a folder's name in square brackets: `[folderName]`. For example, a blog could include the following route `app/blog/[slug]/page.js` where `[slug]` is the Dynamic Segment for blog posts.
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
  return <div>My Post: {slug}</div>
}
```

Dynamic Segments are passed as the `params` prop to [`layout`](https://nextjs.org/docs/app/api-reference/file-conventions/layout), [`page`](https://nextjs.org/docs/app/api-reference/file-conventions/page), [`route`](https://nextjs.org/docs/app/api-reference/file-conventions/route), and [`generateMetadata`](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#generatemetadata-function) functions.
Route | Example URL | `params`
---|---|---
`app/blog/[slug]/page.js` | `/blog/a` | `{ slug: 'a' }`
`app/blog/[slug]/page.js` | `/blog/b` | `{ slug: 'b' }`
`app/blog/[slug]/page.js` | `/blog/c` | `{ slug: 'c' }`
### In Client Components[](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#in-client-components)
In a Client Component **page** , dynamic segments from props can be accessed using the
app/blog/[slug]/page.tsx
TypeScript
JavaScript TypeScript
```
'use client'
import { use } from 'react'

export default function BlogPostPage({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = use(params)

  return (
    <div>
      <p>{slug}</p>
    </div>
  )
}
```

Alternatively Client Components can use the [`useParams`](https://nextjs.org/docs/app/api-reference/functions/use-params) hook to access the `params` anywhere in the Client Component tree.
### Catch-all Segments[](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#catch-all-segments)
Dynamic Segments can be extended to **catch-all** subsequent segments by adding an ellipsis inside the brackets `[...folderName]`.
For example, `app/shop/[...slug]/page.js` will match `/shop/clothes`, but also `/shop/clothes/tops`, `/shop/clothes/tops/t-shirts`, and so on.
Route | Example URL | `params`
---|---|---
`app/shop/[...slug]/page.js` | `/shop/a` | `{ slug: ['a'] }`
`app/shop/[...slug]/page.js` | `/shop/a/b` | `{ slug: ['a', 'b'] }`
`app/shop/[...slug]/page.js` | `/shop/a/b/c` | `{ slug: ['a', 'b', 'c'] }`
### Optional Catch-all Segments[](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#optional-catch-all-segments)
Catch-all Segments can be made **optional** by including the parameter in double square brackets: `[[...folderName]]`.
For example, `app/shop/[[...slug]]/page.js` will **also** match `/shop`, in addition to `/shop/clothes`, `/shop/clothes/tops`, `/shop/clothes/tops/t-shirts`.
The difference between **catch-all** and **optional catch-all** segments is that with optional, the route without the parameter is also matched (`/shop` in the example above).
Route | Example URL | `params`
---|---|---
`app/shop/[[...slug]]/page.js` | `/shop` | `{ slug: undefined }`
`app/shop/[[...slug]]/page.js` | `/shop/a` | `{ slug: ['a'] }`
`app/shop/[[...slug]]/page.js` | `/shop/a/b` | `{ slug: ['a', 'b'] }`
`app/shop/[[...slug]]/page.js` | `/shop/a/b/c` | `{ slug: ['a', 'b', 'c'] }`
### TypeScript[](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#typescript)
When using TypeScript, you can add types for `params` depending on your configured route segment — use [`PageProps<'/route'>`](https://nextjs.org/docs/app/api-reference/file-conventions/page#page-props-helper), [`LayoutProps<'/route'>`](https://nextjs.org/docs/app/api-reference/file-conventions/layout#layout-props-helper), or [`RouteContext<'/route'>`](https://nextjs.org/docs/app/api-reference/file-conventions/route#route-context-helper) to type `params` in `page`, `layout`, and `route` respectively.
Route `params` values are typed as `string`, `string[]`, or `undefined` (for optional catch-all segments), because their values aren't known until runtime. Users can enter any URL into the address bar, and these broad types help ensure that your application code handles all these possible cases.
Route |  `params` Type Definition
---|---
`app/blog/[slug]/page.js` | `{ slug: string }`
`app/shop/[...slug]/page.js` | `{ slug: string[] }`
`app/shop/[[...slug]]/page.js` | `{ slug?: string[] }`
`app/[categoryId]/[itemId]/page.js` | `{ categoryId: string, itemId: string }`
If you're working on a route where `params` can only have a fixed number of valid values, such as a `[locale]` param with a known set of language codes, you can use runtime validation to handle any invalid params a user may enter, and let the rest of your application work with the narrower type from your known set.
/app/[locale]/page.tsx
```
import { notFound } from 'next/navigation'
import type { Locale } from '@i18n/types'
import { isValidLocale } from '@i18n/utils'

function assertValidLocale(value: string): asserts value is Locale {
  if (!isValidLocale(value)) notFound()
}

export default async function Page(props: PageProps<'/[locale]'>) {
  const { locale } = await props.params // locale is typed as string
  assertValidLocale(locale)
  // locale is now typed as Locale
}
```
