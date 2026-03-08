# generateStaticParams
Last updated February 27, 2026
The `generateStaticParams` function can be used in combination with [dynamic route segments](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes) to [**statically generate**](https://nextjs.org/docs/app/guides/caching#static-rendering) routes at build time instead of on-demand at request time.
`generateStaticParams` can be used with:
  * [Pages](https://nextjs.org/docs/app/api-reference/file-conventions/page) (`page.tsx`/`page.js`)
  * [Layouts](https://nextjs.org/docs/app/api-reference/file-conventions/layout) (`layout.tsx`/`layout.js`)
  * [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route) (`route.ts`/`route.js`)


app/blog/[slug]/page.tsx
TypeScript
JavaScript TypeScript
```
// Return a list of `params` to populate the [slug] dynamic segment
export async function generateStaticParams() {
  const posts = await fetch('https://.../posts').then((res) => res.json())

  return posts.map((post) => ({
    slug: post.slug,
  }))
}

// Multiple versions of this page will be statically generated
// using the `params` returned by `generateStaticParams`
export default async function Page({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = await params
  // ...
}
```

> **Good to know** :
>   * You can use the [`dynamicParams`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamicparams) segment config option to control what happens when a dynamic segment is visited that was not generated with `generateStaticParams`.
>   * You must return [an empty array from `generateStaticParams`](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#all-paths-at-build-time) or utilize [`export const dynamic = 'force-static'`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamic) in order to revalidate (ISR) [paths at runtime](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#all-paths-at-runtime).
>   * During `next dev`, `generateStaticParams` will be called when you navigate to a route.
>   * During `next build`, `generateStaticParams` runs before the corresponding Layouts or Pages are generated.
>   * During revalidation (ISR), `generateStaticParams` will not be called again.
>   * `generateStaticParams` replaces the [`getStaticPaths`](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths) function in the Pages Router.
>
