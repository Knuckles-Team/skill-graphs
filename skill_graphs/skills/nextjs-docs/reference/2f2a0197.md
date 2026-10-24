##  `unstable_cache`[](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#unstable_cache)
> **Good to know** : `unstable_cache` is an experimental API. We recommend opting into [Cache Components](https://nextjs.org/docs/app/getting-started/cache-components) and replacing `unstable_cache` with the [`use cache`](https://nextjs.org/docs/app/api-reference/directives/use-cache) directive. See the [Cache Components documentation](https://nextjs.org/docs/app/getting-started/cache-components) for more details.
`unstable_cache` allows you to cache the result of database queries and other async functions. To use it, wrap `unstable_cache` around the function. For example:
app/lib/data.ts
TypeScript
JavaScript TypeScript
```
import { db } from '@/lib/db'
export async function getUserById(id: string) {
  return db
    .select()
    .from(users)
    .where(eq(users.id, id))
    .then((res) => res[0])
}
```

app/page.tsx
TypeScript
JavaScript TypeScript
```
import { unstable_cache } from 'next/cache'
import { getUserById } from '@/app/lib/data'

export default async function Page({
  params,
}: {
  params: Promise<{ userId: string }>
}) {
  const { userId } = await params

  const getCachedUser = unstable_cache(
    async () => {
      return getUserById(userId)
    },
    [userId] // add the user ID to the cache key
  )
}
```

The function accepts a third optional object to define how the cache should be revalidated. It accepts:
  * `tags`: an array of tags used by Next.js to revalidate the cache.
  * `revalidate`: the number of seconds after cache should be revalidated.


app/page.tsx
TypeScript
JavaScript TypeScript
```
const getCachedUser = unstable_cache(
  async () => {
    return getUserById(userId)
  },
  [userId],
  {
    tags: ['user'],
    revalidate: 3600,
  }
)
```

See the [`unstable_cache` API reference](https://nextjs.org/docs/app/api-reference/functions/unstable_cache) to learn more.
