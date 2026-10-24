## Usage[](https://nextjs.org/docs/app/api-reference/functions/updateTag#usage)
`updateTag` can **only** be called from within [Server Actions](https://nextjs.org/docs/app/getting-started/updating-data). It cannot be used in Route Handlers, Client Components, or any other context.
If you need to invalidate cache tags in Route Handlers or other contexts, use [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag) instead.
> **Good to know** : `updateTag` immediately expires the cached data for the specified tag. The next request will wait to fetch fresh data rather than serving stale content from the cache, ensuring users see their changes immediately.
