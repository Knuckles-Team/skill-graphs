##  `revalidatePath`[](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#revalidatepath)
`revalidatePath` is used to revalidate a route and following an event. To use it, call it in a [Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route) or Server Action:
app/lib/actions.ts
TypeScript
JavaScript TypeScript
```
import { revalidatePath } from 'next/cache'

export async function updateUser(id: string) {
  // Mutate data
  revalidatePath('/profile')
```

See the [`revalidatePath` API reference](https://nextjs.org/docs/app/api-reference/functions/revalidatePath) to learn more.
