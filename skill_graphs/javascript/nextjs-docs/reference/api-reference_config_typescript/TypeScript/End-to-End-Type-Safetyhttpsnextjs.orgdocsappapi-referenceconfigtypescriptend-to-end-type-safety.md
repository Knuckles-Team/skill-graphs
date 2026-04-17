## End-to-End Type Safety[](https://nextjs.org/docs/app/api-reference/config/typescript#end-to-end-type-safety)
The Next.js App Router has **enhanced type safety**. This includes:
  1. **No serialization of data between fetching function and page** : You can `fetch` directly in components, layouts, and pages on the server. This data _does not_ need to be serialized (converted to a string) to be passed to the client side for consumption in React. Instead, since `app` uses Server Components by default, we can use values like `Date`, `Map`, `Set`, and more without any extra steps. Previously, you needed to manually type the boundary between server and client with Next.js-specific types.
  2. **Streamlined data flow between components** : With the removal of `_app` in favor of root layouts, it is now easier to visualize the data flow between components and pages. Previously, data flowing between individual `pages` and `_app` were difficult to type and could introduce confusing bugs. With [colocated data fetching](https://nextjs.org/docs/app/getting-started/fetching-data) in the App Router, this is no longer an issue.


[Data Fetching in Next.js](https://nextjs.org/docs/app/getting-started/fetching-data) now provides as close to end-to-end type safety as possible without being prescriptive about your database or content provider selection.
We're able to type the response data as you would expect with normal TypeScript. For example:
app/page.tsx
TypeScript
JavaScript TypeScript
```
async function getData() {
  const res = await fetch('https://api.example.com/...')
  // The return value is *not* serialized
  // You can return Date, Map, Set, etc.
  return res.json()
}

export default async function Page() {
  const name = await getData()

  return '...'
}
```

For _complete_ end-to-end type safety, this also requires your database or content provider to support TypeScript. This could be through using an
