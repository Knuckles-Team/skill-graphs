## Revalidation[](https://nextjs.org/docs/app/api-reference/directives/use-cache#revalidation)
By default, `use cache` uses the `default` profile with these settings:
  * **stale** : 5 minutes (client-side)
  * **revalidate** : 15 minutes (server-side)
  * **expire** : Never expires by time


lib/data.ts
```
async function getData() {
  'use cache'
  // Implicitly uses default profile
  return fetch('/api/data')
}
```

### Customizing cache lifetime[](https://nextjs.org/docs/app/api-reference/directives/use-cache#customizing-cache-lifetime)
Use the [`cacheLife`](https://nextjs.org/docs/app/api-reference/functions/cacheLife) function to customize cache duration:
lib/data.ts
```
import { cacheLife } from 'next/cache'

async function getData() {
  'use cache'
  cacheLife('hours') // Use built-in 'hours' profile
  return fetch('/api/data')
}
```

### On-demand revalidation[](https://nextjs.org/docs/app/api-reference/directives/use-cache#on-demand-revalidation)
Use [`cacheTag`](https://nextjs.org/docs/app/api-reference/functions/cacheTag), [`updateTag`](https://nextjs.org/docs/app/api-reference/functions/updateTag), or [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag) for on-demand cache invalidation:
lib/data.ts
```
import { cacheTag } from 'next/cache'

async function getProducts() {
  'use cache'
  cacheTag('products')
  return fetch('/api/products')
}
```

app/actions.ts
```
'use server'

import { updateTag } from 'next/cache'

export async function updateProduct() {
  await db.products.update(...)
  updateTag('products') // Invalidates all 'products' caches
}
```

Both `cacheLife` and `cacheTag` integrate across client and server caching layers, meaning you configure your caching semantics in one place and they apply everywhere.
