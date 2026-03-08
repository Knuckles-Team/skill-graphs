##  [When to use runtime cache](https://vercel.com/docs/regions#when-to-use-runtime-cache)[](https://vercel.com/docs/regions#when-to-use-runtime-cache)
Runtime cache is best when your functions fetch the same data multiple times or perform expensive computations that can be reused, such as in the following scenarios:
  * API calls that return the same data across multiple requests
  * Database queries that don't change frequently
  * Expensive computations you want to reuse
  * Data fetching in server components or API routes


Runtime cache is not a good fit for:
  * User-specific data that differs for each request
  * Data that must be fresh on every request
  * Complete HTTP responses (use [CDN cache](https://vercel.com/docs/cdn-cache) instead)
