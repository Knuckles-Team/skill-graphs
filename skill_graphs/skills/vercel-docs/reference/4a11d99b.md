##  [When to use data cache](https://vercel.com/docs/routing#when-to-use-data-cache)[](https://vercel.com/docs/routing#when-to-use-data-cache)
Data cache is best when your Next.js App Router pages fetch data that can be reused across requests:
  * API calls that return the same data across multiple requests
  * Database queries that don't change frequently
  * Data fetching in server components or route handlers
  * Pages with a mix of static and dynamic data


Data cache is not a good fit for:
  * User-specific data that differs for each request
  * Data that must be fresh on every request
  * Complete HTTP responses (use [CDN Cache](https://vercel.com/docs/cdn-cache) instead)
  * Next.js 15 and above (use [Runtime Cache](https://vercel.com/docs/runtime-cache) instead)
