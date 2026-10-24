##  `fetch` requests[](https://nextjs.org/docs/app/guides/upgrading/version-15#fetch-requests)
[`fetch` requests](https://nextjs.org/docs/app/api-reference/functions/fetch) are no longer cached by default.
To opt specific `fetch` requests into caching, you can pass the `cache: 'force-cache'` option.
app/layout.js
```
export default async function RootLayout() {
  const a = await fetch('https://...') // Not Cached
  const b = await fetch('https://...', { cache: 'force-cache' }) // Cached

  // ...
}
```

To opt all `fetch` requests in a layout or page into caching, you can use the `export const fetchCache = 'default-cache'` [segment config option](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config). If individual `fetch` requests specify a `cache` option, that will be used instead.
app/layout.js
```
// Since this is the root layout, all fetch requests in the app
// that don't set their own cache option will be cached.
export const fetchCache = 'default-cache'

export default async function RootLayout() {
  const a = await fetch('https://...') // Cached
  const b = await fetch('https://...', { cache: 'no-store' }) // Not cached

  // ...
}
```
