## Rendering with search params[](https://nextjs.org/docs/app/getting-started/layouts-and-pages#rendering-with-search-params)
In a Server Component **page** , you can access search parameters using the [`searchParams`](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional) prop:
app/page.tsx
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

Using `searchParams` opts your page into [**dynamic rendering**](https://nextjs.org/docs/app/guides/caching#dynamic-rendering) because it requires an incoming request to read the search parameters from.
Client Components can read search params using the [`useSearchParams`](https://nextjs.org/docs/app/api-reference/functions/use-search-params) hook.
Learn more about `useSearchParams` in [statically rendered](https://nextjs.org/docs/app/api-reference/functions/use-search-params#static-rendering) and [dynamically rendered](https://nextjs.org/docs/app/api-reference/functions/use-search-params#dynamic-rendering) routes.
### What to use and when[](https://nextjs.org/docs/app/getting-started/layouts-and-pages#what-to-use-and-when)
  * Use the `searchParams` prop when you need search parameters to **load data for the page** (e.g. pagination, filtering from a database).
  * Use `useSearchParams` when search parameters are used **only on the client** (e.g. filtering a list already loaded via props).
  * As a small optimization, you can use `new URLSearchParams(window.location.search)` in **callbacks or event handlers** to read search params without triggering re-renders.
