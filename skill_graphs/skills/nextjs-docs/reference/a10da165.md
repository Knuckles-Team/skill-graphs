## Multiple Dynamic Segments[](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#multiple-dynamic-segments)
app/products/[category]/[product]/page.tsx
TypeScript
JavaScript TypeScript
```
export function generateStaticParams() {
  return [
    { category: 'a', product: '1' },
    { category: 'b', product: '2' },
    { category: 'c', product: '3' },
  ]
}

// Three versions of this page will be statically generated
// using the `params` returned by `generateStaticParams`
// - /products/a/1
// - /products/b/2
// - /products/c/3
export default async function Page({
  params,
}: {
  params: Promise<{ category: string; product: string }>
}) {
  const { category, product } = await params
  // ...
}
```
