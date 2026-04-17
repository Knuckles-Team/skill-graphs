## Usage[](https://nextjs.org/docs/app/api-reference/functions/revalidateTag#usage)
`revalidateTag` can be called in Server Functions and Route Handlers.
`revalidateTag` cannot be called in Client Components or Proxy, as it only works in server environments.
### Revalidation Behavior[](https://nextjs.org/docs/app/api-reference/functions/revalidateTag#revalidation-behavior)
The revalidation behavior depends on whether you provide the second argument:
  * **With`profile="max"` (recommended)**: The tag entry is marked as stale, and the next time a resource with that tag is visited, it will use stale-while-revalidate semantics. This means the stale content is served while fresh content is fetched in the background.
  * **With a custom cache life profile** : For advanced usage, you can specify any cache life profile that your application has defined, allowing for custom revalidation behaviors tailored to your specific caching requirements.
  * **Without the second argument (deprecated)** : The tag entry is expired immediately, and the next request to that resource will be a blocking revalidate/cache miss. This behavior is now deprecated, and you should either use `profile="max"` or migrate to [`updateTag`](https://nextjs.org/docs/app/api-reference/functions/updateTag).


> **Good to know** : When using `profile="max"`, `revalidateTag` marks tagged data as stale, but fresh data is only fetched when pages using that tag are next visited. This means calling `revalidateTag` will not immediately trigger many revalidations at once. The invalidation only happens when any page using that tag is next visited.
