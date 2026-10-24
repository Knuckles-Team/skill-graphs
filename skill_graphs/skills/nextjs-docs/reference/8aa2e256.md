# cacheComponents
Last updated February 27, 2026
The `cacheComponents` flag is a feature in Next.js that causes data fetching operations in the App Router to be excluded from pre-renders unless they are explicitly cached. This can be useful for optimizing the performance of dynamic data fetching in Server Components.
It is useful if your application requires fresh data fetching during runtime rather than serving from a pre-rendered cache.
It is expected to be used in conjunction with [`use cache`](https://nextjs.org/docs/app/api-reference/directives/use-cache) so that your data fetching happens at runtime by default unless you define specific parts of your application to be cached with `use cache` at the page, function, or component level.
