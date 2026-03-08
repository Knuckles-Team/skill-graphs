## Cache Interactions[](https://nextjs.org/docs/app/guides/caching#cache-interactions)
When configuring the different caching mechanisms, it's important to understand how they interact with each other:
### Data Cache and Full Route Cache[](https://nextjs.org/docs/app/guides/caching#data-cache-and-full-route-cache)
  * Revalidating or opting out of the Data Cache **will** invalidate the Full Route Cache, as the render output depends on data.
  * Invalidating or opting out of the Full Route Cache **does not** affect the Data Cache. You can dynamically render a route that has both cached and uncached data. This is useful when most of your page uses cached data, but you have a few components that rely on data that needs to be fetched at request time. You can dynamically render without worrying about the performance impact of re-fetching all the data.


### Data Cache and Client-side Router cache[](https://nextjs.org/docs/app/guides/caching#data-cache-and-client-side-router-cache)
  * To immediately invalidate the Data Cache and Router cache, you can use [`revalidatePath`](https://nextjs.org/docs/app/guides/caching#revalidatepath) or [`revalidateTag`](https://nextjs.org/docs/app/guides/caching#fetch-optionsnexttags-and-revalidatetag) in a [Server Action](https://nextjs.org/docs/app/getting-started/updating-data).
  * Revalidating the Data Cache in a [Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route) **will not** immediately invalidate the Router Cache as the Route Handler isn't tied to a specific route. This means Router Cache will continue to serve the previous payload until a hard refresh, or the automatic invalidation period has elapsed.
