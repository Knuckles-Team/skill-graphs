##  [How Data cache works](https://vercel.com/docs/routing#how-data-cache-works)[](https://vercel.com/docs/routing#how-data-cache-works)
Data cache stores data in a regional cache close to where your function executes. It has the following characteristics:
  * Regional: Every region in which your function runs has an independent cache, so data used in server-side rendering or route handlers is cached close to where the function executes
  * Isolated: Data cache is isolated per Vercel project and [deployment environment](https://vercel.com/docs/deployments/environments) (`production` or `preview`)
  * Persistent across deployments: Cached data persists across deployments unless you explicitly invalidate it
  * Time-based revalidation: All cached data can define a revalidation interval, after which the data is marked as stale, triggering a re-fetch from origin
  * On-demand revalidation: Any data can be triggered for revalidation on-demand, regardless of the revalidation interval. The revalidation propagates to all regions within 300ms
  * Tag-based revalidation: Next.js allows associating tags with data, which can be used to revalidate all data with the same tag at once with
  * Ephemeral: Each project has a storage limit. When your project reaches this limit, Vercel evicts (removes) the entries that haven't been accessed recently to free up space for new entries
