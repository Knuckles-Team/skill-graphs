## API Reference[](https://nextjs.org/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath#api-reference)
The cache handler can implement the following methods: `get`, `set`, `revalidateTag`, and `resetRequestCache`.
###  `get()`[](https://nextjs.org/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath#get)
Parameter | Type | Description
---|---|---
`key` | `string` | The key to the cached value.
Returns the cached value or `null` if not found.
###  `set()`[](https://nextjs.org/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath#set)
Parameter | Type | Description
---|---|---
`key` | `string` | The key to store the data under.
`data` | Data or `null` | The data to be cached.
`ctx` | `{ tags: [] }` | The cache tags provided.
Returns `Promise<void>`.
###  `revalidateTag()`[](https://nextjs.org/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath#revalidatetag)
Parameter | Type | Description
---|---|---
`tag` |  `string` or `string[]` | The cache tags to revalidate.
Returns `Promise<void>`. Learn more about [revalidating data](https://nextjs.org/docs/app/guides/incremental-static-regeneration) or the [`revalidateTag()`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag) function.
###  `resetRequestCache()`[](https://nextjs.org/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath#resetrequestcache)
This method resets the temporary in-memory cache for a single request before the next request.
Returns `void`.
**Good to know:**
  * `revalidatePath` is a convenience layer on top of cache tags. Calling `revalidatePath` will call your `revalidateTag` function, which you can then choose if you want to tag cache keys based on the path.
