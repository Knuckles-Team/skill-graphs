## Good to know[](https://nextjs.org/docs/app/api-reference/functions/headers#good-to-know)
  * `headers` is an **asynchronous** function that returns a promise. You must use `async/await` or React's
    * In version 14 and earlier, `headers` was a synchronous function. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.
  * Since `headers` is read-only, you cannot `set` or `delete` the outgoing request headers.
  * `headers` is a [Dynamic API](https://nextjs.org/docs/app/guides/caching#dynamic-rendering) whose returned values cannot be known ahead of time. Using it in will opt a route into **[dynamic rendering](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)**.
