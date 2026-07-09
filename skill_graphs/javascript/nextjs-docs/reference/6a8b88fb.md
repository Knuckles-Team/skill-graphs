# page.js
Last updated February 27, 2026
The `page` file allows you to define UI that is **unique** to a route. You can create a page by default exporting a component from the file:
app/blog/[slug]/page.tsx
TypeScript
JavaScript TypeScript
```
export default function Page({
  params,
  searchParams,
}: {
  params: Promise<{ slug: string }>
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>
}) {
  return <h1>My Page</h1>
}
```
