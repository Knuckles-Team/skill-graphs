##  [How runtime cache works](https://vercel.com/docs/regions#how-runtime-cache-works)[](https://vercel.com/docs/regions#how-runtime-cache-works)
Runtime cache stores data in a non-durable cache close to where your function executes. Each [region](https://vercel.com/docs/regions) where your function runs has its own cache, allowing reads and writes to happen in the same region for low latency. It has the following characteristics:
  * Regional: Each region has its own cache
  * Isolated: Runtime cache is isolated per Vercel project and deployment environment (`preview` and `production`)
  * Persistent across deployments: Cached data persists across deployments and can be invalidated through time-based expiration or by calling `expireTag`
  * Ephemeral: Each project has a storage limit. When your project reaches this limit, Vercel evicts (removes) the entries that haven't been accessed recently to free up space for new entries
  * Automatic: When runtime cache is enabled, Vercel handles caching for you
  * Framework-agnostic: Works with all frameworks


The cache sits between your function and your data source, reducing the need to repeatedly fetch the same data. See [limits and usage](https://vercel.com/docs/regions#limits-and-usage) for information on item size, tags per item, and maximum tag length.
