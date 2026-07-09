# use cache: private
This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on
Last updated February 27, 2026
The `'use cache: private'` directive allows functions to access runtime request APIs like `cookies()`, `headers()`, and `searchParams` within a cached scope. However, results are **never stored on the server** , they're cached only in the browser's memory and do not persist across page reloads.
Reach for `'use cache: private'` when:
  * You want to cache a function that already accesses runtime data, and refactoring to [move the runtime access outside and pass values as arguments](https://nextjs.org/docs/app/getting-started/cache-components#with-runtime-data) is not practical.
  * Compliance requirements prevent storing certain data on the server, even temporarily


Because this directive accesses runtime data, the function executes on every server render and is excluded from running during [static shell](https://nextjs.org/docs/app/getting-started/cache-components#how-rendering-works-with-cache-components) generation.
It is **not** possible to configure custom cache handlers for `'use cache: private'`.
For a comparison of the different cache directives, see [How `use cache: remote` differs from `use cache` and `use cache: private`](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote#how-use-cache-remote-differs-from-use-cache-and-use-cache-private).
> **Good to know** : This directive is marked as `experimental` because it depends on runtime prefetching, which is not yet stable. Runtime prefetching is an upcoming feature that will let the router prefetch past the [static shell](https://nextjs.org/docs/app/getting-started/cache-components#how-rendering-works-with-cache-components) into **any** cached scope, not just private caches.
