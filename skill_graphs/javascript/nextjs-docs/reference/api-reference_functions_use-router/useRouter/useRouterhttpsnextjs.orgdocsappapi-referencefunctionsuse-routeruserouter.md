##  `useRouter()`[](https://nextjs.org/docs/app/api-reference/functions/use-router#userouter)
  * `router.push(href: string, { scroll: boolean })`: Perform a client-side navigation to the provided route. Adds a new entry into the
  * `router.replace(href: string, { scroll: boolean })`: Perform a client-side navigation to the provided route without adding a new entry into the browser’s history stack.
  * `router.refresh()`: Refresh the current route. Making a new request to the server, re-fetching data requests, and re-rendering Server Components. The client will merge the updated React Server Component payload without losing unaffected client-side React (e.g. `useState`) or browser state (e.g. scroll position).
  * `router.prefetch(href: string, options?: { onInvalidate?: () => void })`: [Prefetch](https://nextjs.org/docs/app/getting-started/linking-and-navigating#prefetching) the provided route for faster client-side transitions. The optional `onInvalidate` callback is called when the [prefetched data becomes stale](https://nextjs.org/docs/app/guides/prefetching#extending-or-ejecting-link).
  * `router.back()`: Navigate back to the previous route in the browser’s history stack.
  * `router.forward()`: Navigate forwards to the next page in the browser’s history stack.


> **Good to know** :
>   * You must not send untrusted or unsanitized URLs to `router.push` or `router.replace`, as this can open your site to cross-site scripting (XSS) vulnerabilities. For example, `javascript:` URLs sent to `router.push` or `router.replace` will be executed in the context of your page.
>   * The `<Link>` component automatically prefetch routes as they become visible in the viewport.
>   * `refresh()` could re-produce the same result if fetch requests are cached. Other Dynamic APIs like `cookies` and `headers` could also change the response.
>   * The `onInvalidate` callback is called at most once per prefetch request. It signals when you may want to trigger a new prefetch for updated route data.
>

### Migrating from `next/router`[](https://nextjs.org/docs/app/api-reference/functions/use-router#migrating-from-nextrouter)
  * The `useRouter` hook should be imported from `next/navigation` and not `next/router` when using the App Router
  * The `pathname` string has been removed and is replaced by [`usePathname()`](https://nextjs.org/docs/app/api-reference/functions/use-pathname)
  * The `query` object has been removed and is replaced by [`useSearchParams()`](https://nextjs.org/docs/app/api-reference/functions/use-search-params)
  * `router.events` has been replaced. [See below.](https://nextjs.org/docs/app/api-reference/functions/use-router#router-events)


[View the full migration guide](https://nextjs.org/docs/app/guides/migrating/app-router-migration).
