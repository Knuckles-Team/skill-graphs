# redirect
Last updated February 27, 2026
The `redirect` function allows you to redirect the user to another URL. `redirect` can be used while rendering in [Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components), [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route), and [Server Functions](https://nextjs.org/docs/app/getting-started/updating-data).
When used in a [streaming context](https://nextjs.org/docs/app/getting-started/linking-and-navigating#streaming), this will insert a meta tag to emit the redirect on the client side. When used in a server action, it will serve a 303 HTTP redirect response to the caller. Otherwise, it will serve a 307 HTTP redirect response to the caller.
If a resource doesn't exist, you can use the [`notFound` function](https://nextjs.org/docs/app/api-reference/functions/not-found) instead.
