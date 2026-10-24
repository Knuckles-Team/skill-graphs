## Example[](https://nextjs.org/docs/app/api-reference/functions/unstable_cache#example)
app/page.tsx
TypeScript
JavaScript TypeScript
```
import { unstable_cache } from 'next/cache'

export default async function Page({
  params,
}: {
  params: Promise<{ userId: string }>
}) {
  const { userId } = await params
  const getCachedUser = unstable_cache(
    async () => {
      return { id: userId }
    },
    [userId], // add the user ID to the cache key
    {
      tags: ['users'],
      revalidate: 60,
    }
  )

  //...
}
```
