## Returns[](https://nextjs.org/docs/app/api-reference/functions/unstable_cache#returns)
`unstable_cache` returns a function that when invoked, returns a Promise that resolves to the cached data. If the data is not in the cache, the provided function will be invoked, and its result will be cached and returned.
