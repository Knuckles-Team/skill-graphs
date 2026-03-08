##  `fetch`[](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#fetch)
By default, [`fetch`](https://nextjs.org/docs/app/api-reference/functions/fetch) requests are not cached. You can cache individual requests by setting the `cache` option to `'force-cache'`.
app/page.tsx
TypeScript
JavaScript TypeScript
```
export default async function Page() {
  const data = await fetch('https://...', { cache: 'force-cache' })
}
```

> **Good to know** : Although `fetch` requests are not cached by default, Next.js will [pre-render](https://nextjs.org/docs/app/guides/caching#static-rendering) routes that have `fetch` requests and cache the HTML. If you want to guarantee a route is [dynamic](https://nextjs.org/docs/app/guides/caching#dynamic-rendering), use the [`connection` API](https://nextjs.org/docs/app/api-reference/functions/connection).
To revalidate the data returned by a `fetch` request, you can use the `next.revalidate` option.
app/page.tsx
TypeScript
JavaScript TypeScript
```
export default async function Page() {
  const data = await fetch('https://...', { next: { revalidate: 3600 } })
}
```

This will revalidate the data after a specified amount of seconds.
You can also tag `fetch` requests to enable on-demand cache invalidation:
app/lib/data.ts
TypeScript
JavaScript TypeScript
```
export async function getUserById(id: string) {
  const data = await fetch(`https://...`, {
    next: {
      tags: ['user'],
    },
  })
}
```

See the [`fetch` API reference](https://nextjs.org/docs/app/api-reference/functions/fetch) to learn more.
