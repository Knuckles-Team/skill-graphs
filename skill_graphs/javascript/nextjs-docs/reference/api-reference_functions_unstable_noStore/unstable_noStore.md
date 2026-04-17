# unstable_noStore
This is a legacy API and no longer recommended. It's still supported for backward compatibility.
Last updated February 27, 2026
**In version 15, we recommend using[`connection`](https://nextjs.org/docs/app/api-reference/functions/connection) instead of `unstable_noStore`.**
`unstable_noStore` can be used to declaratively opt out of static rendering and indicate a particular component should not be cached.
```
import { unstable_noStore as noStore } from 'next/cache';

export default async function ServerComponent() {
  noStore();
  const result = await db.query(...);
  ...
}
```

> **Good to know** :
>   * `unstable_noStore` is equivalent to `cache: 'no-store'` on a `fetch`
>   * `unstable_noStore` is preferred over `export const dynamic = 'force-dynamic'` as it is more granular and can be used on a per-component basis
>

  * Using `unstable_noStore` inside [`unstable_cache`](https://nextjs.org/docs/app/api-reference/functions/unstable_cache) will not opt out of static generation. Instead, it will defer to the cache configuration to determine whether to cache the result or not.
