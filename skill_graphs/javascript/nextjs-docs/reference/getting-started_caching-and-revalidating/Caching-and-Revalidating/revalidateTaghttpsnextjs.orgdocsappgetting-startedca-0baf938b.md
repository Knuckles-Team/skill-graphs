##  `revalidateTag`[](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#revalidatetag)
`revalidateTag` is used to revalidate cache entries based on a tag and following an event. The function now supports two behaviors:
  * **With`profile="max"`** : Uses stale-while-revalidate semantics, serving stale content while fetching fresh content in the background
  * **Without the second argument** : Legacy behavior that immediately expires the cache (deprecated)


After tagging your cached data, using [`fetch`](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#fetch) with `next.tags`, or the [`cacheTag`](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#cachetag) function, you may call `revalidateTag` in a [Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route) or Server Action:
app/lib/actions.ts
TypeScript
JavaScript TypeScript
```
import { revalidateTag } from 'next/cache'

export async function updateUser(id: string) {
  // Mutate data
  revalidateTag('user', 'max') // Recommended: Uses stale-while-revalidate
}
```

You can reuse the same tag in multiple functions to revalidate them all at once.
See the [`revalidateTag` API reference](https://nextjs.org/docs/app/api-reference/functions/revalidateTag) to learn more.
