## Examples[](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#examples)
### Static Rendering[](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#static-rendering)
#### All paths at build time[](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#all-paths-at-build-time)
To statically render all paths at build time, supply the full list of paths to `generateStaticParams`:
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

#### Subset of paths at build time[](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#subset-of-paths-at-build-time)
To statically render a subset of paths at build time, and the rest the first time they're visited at runtime, return a partial list of paths:
app/blog/[slug]/page.tsx
TypeScript
JavaScript TypeScript
```
export async function generateStaticParams() {
  const posts = await fetch('https://.../posts').then((res) => res.json())

  // Render the first 10 posts at build time
  return posts.slice(0, 10).map((post) => ({
    slug: post.slug,
  }))
}
```

Then, by using the [`dynamicParams`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamicparams) segment config option, you can control what happens when a dynamic segment is visited that was not generated with `generateStaticParams`.
app/blog/[slug]/page.tsx
TypeScript
JavaScript TypeScript
```
// All posts besides the top 10 will be a 404
export const dynamicParams = false

export async function generateStaticParams() {
  const posts = await fetch('https://.../posts').then((res) => res.json())
  const topPosts = posts.slice(0, 10)

  return topPosts.map((post) => ({
    slug: post.slug,
  }))
}
```

#### All paths at runtime[](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#all-paths-at-runtime)
To statically render all paths the first time they're visited, return an empty array (no paths will be rendered at build time) or utilize [`export const dynamic = 'force-static'`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamic):
app/blog/[slug]/page.js
```
export async function generateStaticParams() {
  return []
}
```

> **Good to know:**
>   * You must always return an array from `generateStaticParams`, even if it's empty. Otherwise, the route will be dynamically rendered.
>

app/changelog/[slug]/page.js
```
export const dynamic = 'force-static'
```

#### With Cache Components[](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#with-cache-components)
When using [Cache Components](https://nextjs.org/docs/app/getting-started/cache-components) with dynamic routes, `generateStaticParams` must return **at least one param**. Empty arrays cause a [build error](https://nextjs.org/docs/messages/empty-generate-static-params). This allows Cache Components to validate your route doesn't incorrectly access `cookies()`, `headers()`, or `searchParams` at runtime.
> **Good to know** : If you don't know the actual param values at build time, you can return a placeholder param (e.g., `[{ slug: '__placeholder__' }]`) for validation, then handle it in your page with `notFound()`. However, this prevents build time validation from working effectively and may cause runtime errors.
See the [dynamic routes section](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#with-cache-components) for detailed walkthroughs.
### With Route Handlers[](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#with-route-handlers)
You can use `generateStaticParams` with [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route) to statically generate API responses at build time:
app/api/posts/[id]/route.ts
TypeScript
JavaScript TypeScript
```
export async function generateStaticParams() {
  return [{ id: '1' }, { id: '2' }, { id: '3' }]
}

export async function GET(
  request: Request,
  { params }: RouteContext<'/api/posts/[id]'>
) {
  const { id } = await params
  // This will be statically generated for IDs 1, 2, and 3
  return Response.json({ id, title: `Post ${id}` })
}
```

### Route Handlers with Cache Components[](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#route-handlers-with-cache-components)
When using [Cache Components](https://nextjs.org/docs/app/getting-started/cache-components), combine with `use cache` for optimal caching:
app/api/posts/[id]/route.ts
```
export async function generateStaticParams() {
  return [{ id: '1' }, { id: '2' }, { id: '3' }]
}

async function getPost(id: Promise<string>) {
  'use cache'
  const resolvedId = await id
  const response = await fetch(`https://api.example.com/posts/${resolvedId}`)
  return response.json()
}

export async function GET(
  request: Request,
  { params }: RouteContext<'/api/posts/[id]'>
) {
  const post = await getPost(params.then((p) => p.id))
  return Response.json(post)
}
```

See the [Route Handlers documentation](https://nextjs.org/docs/app/api-reference/file-conventions/route#static-generation-with-generatestaticparams) for more details.
### Disable rendering for unspecified paths[](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#disable-rendering-for-unspecified-paths)
To prevent unspecified paths from being statically rendered at runtime, add the `export const dynamicParams = false` option in a route segment. When this config option is used, only paths provided by `generateStaticParams` will be served, and unspecified routes will 404 or match (in the case of [catch-all routes](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#catch-all-segments)).
### Multiple Dynamic Segments in a Route[](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#multiple-dynamic-segments-in-a-route)
You can generate params for dynamic segments above the current layout or page, but **not below**. For example, given the `app/products/[category]/[product]` route:
  * `app/products/[category]/[product]/page.js` can generate params for **both** `[category]` and `[product]`.
  * `app/products/[category]/layout.js` can **only** generate params for `[category]`.


There are two approaches to generating params for a route with multiple dynamic segments:
#### Generate params from the bottom up[](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#generate-params-from-the-bottom-up)
Generate multiple dynamic segments from the child route segment.
app/products/[category]/[product]/page.tsx
TypeScript
JavaScript TypeScript
```
// Generate segments for both [category] and [product]
export async function generateStaticParams() {
  const products = await fetch('https://.../products').then((res) => res.json())

  return products.map((product) => ({
    category: product.category.slug,
    product: product.id,
  }))
}

export default function Page({
  params,
}: {
  params: Promise<{ category: string; product: string }>
}) {
  // ...
}
```

#### Generate params from the top down[](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#generate-params-from-the-top-down)
Generate the parent segments first and use the result to generate the child segments.
app/products/[category]/layout.tsx
TypeScript
JavaScript TypeScript
```
// Generate segments for [category]
export async function generateStaticParams() {
  const products = await fetch('https://.../products').then((res) => res.json())

  return products.map((product) => ({
    category: product.category.slug,
  }))
}

export default function Layout({
  params,
}: {
  params: Promise<{ category: string }>
}) {
  // ...
}
```

A child route segment's `generateStaticParams` function is executed once for each segment a parent `generateStaticParams` generates.
The child `generateStaticParams` function can use the `params` returned from the parent `generateStaticParams` function to dynamically generate its own segments.
app/products/[category]/[product]/page.tsx
TypeScript
JavaScript TypeScript
```
// Generate segments for [product] using the `params` passed from
// the parent segment's `generateStaticParams` function
export async function generateStaticParams({
  params: { category },
}: {
  params: { category: string }
}) {
  const products = await fetch(
    `https://.../products?category=${category}`
  ).then((res) => res.json())

  return products.map((product) => ({
    product: product.id,
  }))
}

export default function Page({
  params,
}: {
  params: Promise<{ category: string; product: string }>
}) {
  // ...
}
```

Notice that the params argument can be accessed synchronously and includes only parent segment params.
For type completion, you can make use of the TypeScript `Awaited` helper in combination with either [`Page Props helper`](https://nextjs.org/docs/app/api-reference/file-conventions/page#page-props-helper) or [`Layout Props helper`](https://nextjs.org/docs/app/api-reference/file-conventions/layout#layout-props-helper):
app/products/[category]/[product]/page.tsx
TypeScript
JavaScript TypeScript
```
export async function generateStaticParams({
  params: { category },
}: {
  params: Awaited<LayoutProps<'/products/[category]'>['params']>
}) {
  const products = await fetch(
    `https://.../products?category=${category}`
  ).then((res) => res.json())

  return products.map((product) => ({
    product: product.id,
  }))
}
```

> **Good to know** : `fetch` requests are automatically [memoized](https://nextjs.org/docs/app/guides/caching#request-memoization) for the same data across all `generate`-prefixed functions, Layouts, Pages, and Server Components. React [`cache` can be used](https://nextjs.org/docs/app/guides/caching#react-cache-function) if `fetch` is unavailable.
