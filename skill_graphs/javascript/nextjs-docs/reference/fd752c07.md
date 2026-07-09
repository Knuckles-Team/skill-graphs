## Good to know[](https://nextjs.org/docs/app/api-reference/functions/cookies#good-to-know)
  * `cookies` is an **asynchronous** function that returns a promise. You must use `async/await` or React's
    * In version 14 and earlier, `cookies` was a synchronous function. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.
  * `cookies` is a [Dynamic API](https://nextjs.org/docs/app/guides/caching#dynamic-rendering) whose returned values cannot be known ahead of time. Using it in a layout or page will opt a route into [dynamic rendering](https://nextjs.org/docs/app/guides/caching#dynamic-rendering).
  * The `.delete` method can only be called:
    * In a [Server Function](https://nextjs.org/docs/app/getting-started/updating-data) or [Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route).
    * If it belongs to the same domain from which `.set` is called. For wildcard domains, the specific subdomain must be an exact match. Additionally, the code must be executed on the same protocol (HTTP or HTTPS) as the cookie you want to delete.
  * HTTP does not allow setting cookies after streaming starts, so you must use `.set` in a [Server Function](https://nextjs.org/docs/app/getting-started/updating-data) or [Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route).
