# permanentRedirect
Last updated February 27, 2026
The `permanentRedirect` function allows you to redirect the user to another URL. `permanentRedirect` can be used in Server Components, Client Components, [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route), and [Server Functions](https://nextjs.org/docs/app/getting-started/updating-data).
When used in a streaming context, this will insert a meta tag to emit the redirect on the client side. When used in a server action, it will serve a 303 HTTP redirect response to the caller. Otherwise, it will serve a 308 (Permanent) HTTP redirect response to the caller.
If a resource doesn't exist, you can use the [`notFound` function](https://nextjs.org/docs/app/api-reference/functions/not-found) instead.
> **Good to know** : If you prefer to return a 307 (Temporary) HTTP redirect instead of 308 (Permanent), you can use the [`redirect` function](https://nextjs.org/docs/app/api-reference/functions/redirect) instead.
