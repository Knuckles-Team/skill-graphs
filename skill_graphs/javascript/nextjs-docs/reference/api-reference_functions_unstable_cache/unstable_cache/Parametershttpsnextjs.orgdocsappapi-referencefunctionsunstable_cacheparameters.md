## Parameters[](https://nextjs.org/docs/app/api-reference/functions/unstable_cache#parameters)
```
const data = unstable_cache(fetchData, keyParts, options)()
```

  * `fetchData`: This is an asynchronous function that fetches the data you want to cache. It must be a function that returns a `Promise`.
  * `keyParts`: This is an extra array of keys that further adds identification to the cache. By default, `unstable_cache` already uses the arguments and the stringified version of your function as the cache key. It is optional in most cases; the only time you need to use it is when you use external variables without passing them as parameters. However, it is important to add closures used within the function if you do not pass them as parameters.
  * `options`: This is an object that controls how the cache behaves. It can contain the following properties:
    * `tags`: An array of tags that can be used to control cache invalidation. Next.js will not use this to uniquely identify the function.
    * `revalidate`: The number of seconds after which the cache should be revalidated. Omit or pass `false` to cache indefinitely or until matching `revalidateTag()` or `revalidatePath()` methods are called.
