## API Reference[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers#api-reference)
A cache handler must implement the
###  `get()`[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers#get)
Retrieve a cache entry for the given cache key.
```
get(cacheKey: string, softTags: string[]): Promise<CacheEntry | undefined>
```

Parameter | Type | Description
---|---|---
`cacheKey` | `string` | The unique key for the cache entry.
`softTags` | `string[]` | Tags to check for staleness (used in some cache strategies).
Returns a `CacheEntry` object if found, or `undefined` if not found or expired.
Your `get` method should retrieve the cache entry from storage, check if it has expired based on the `revalidate` time, and return `undefined` for missing or expired entries.
```
const cacheHandler = {
  async get(cacheKey, softTags) {
    const entry = cache.get(cacheKey)
    if (!entry) return undefined

    // Check if expired
    const now = Date.now()
    if (now > entry.timestamp + entry.revalidate * 1000) {
      return undefined
    }

    return entry
  },
}
```

###  `set()`[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers#set)
Store a cache entry for the given cache key.
```
set(cacheKey: string, pendingEntry: Promise<CacheEntry>): Promise<void>
```

Parameter | Type | Description
---|---|---
`cacheKey` | `string` | The unique key to store the entry under.
`pendingEntry` | `Promise<CacheEntry>` | A promise that resolves to the cache entry.
The entry may still be pending when this is called (i.e., its value stream may still be written to). Your handler should await the promise before processing the entry.
Returns `Promise<void>`.
Your `set` method must await the `pendingEntry` promise before storing it, since the cache entry may still be generating when this method is called. Once resolved, store the entry in your cache system.
```
const cacheHandler = {
  async set(cacheKey, pendingEntry) {
    // Wait for the entry to be ready
    const entry = await pendingEntry

    // Store in your cache system
    cache.set(cacheKey, entry)
  },
}
```

###  `refreshTags()`[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers#refreshtags)
Called periodically before starting a new request to sync with external tag services.
```
refreshTags(): Promise<void>
```

This is useful if you're coordinating cache invalidation across multiple instances or services. For in-memory caches, this can be a no-op.
Returns `Promise<void>`.
For in-memory caches, this can be a no-op. For distributed caches, use this to sync tag state from an external service or database before processing requests.
```
const cacheHandler = {
  async refreshTags() {
    // For in-memory cache, no action needed
    // For distributed cache, sync tag state from external service
  },
}
```

###  `getExpiration()`[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers#getexpiration)
Get the maximum revalidation timestamp for a set of tags.
```
getExpiration(tags: string[]): Promise<number>
```

Parameter | Type | Description
---|---|---
`tags` | `string[]` | Array of tags to check expiration for.
Returns:
  * `0` if none of the tags were ever revalidated
  * A timestamp (in milliseconds) representing the most recent revalidation
  * `Infinity` to indicate soft tags should be checked in the `get` method instead


If you're not tracking tag revalidation timestamps, return `0`. Otherwise, find the most recent revalidation timestamp across all the provided tags. Return `Infinity` if you prefer to handle soft tag checking in the `get` method.
```
const cacheHandler = {
  async getExpiration(tags) {
    // Return 0 if not tracking tag revalidation
    return 0

    // Or return the most recent revalidation timestamp
    // return Math.max(...tags.map(tag => tagTimestamps.get(tag) || 0));
  },
}
```

###  `updateTags()`[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers#updatetags)
Called when tags are revalidated or expired.
```
updateTags(tags: string[], durations?: { expire?: number }): Promise<void>
```

Parameter | Type | Description
---|---|---
`tags` | `string[]` | Array of tags to update.
`durations` | `{ expire?: number }` | Optional expiration duration in seconds.
Your handler should update its internal state to mark these tags as invalidated.
Returns `Promise<void>`.
When tags are revalidated, your handler should invalidate all cache entries that have any of those tags. Iterate through your cache and remove entries whose tags match the provided list.
```
const cacheHandler = {
  async updateTags(tags, durations) {
    // Invalidate all cache entries with matching tags
    for (const [key, entry] of cache.entries()) {
      if (entry.tags.some((tag) => tags.includes(tag))) {
        cache.delete(key)
      }
    }
  },
}
```
