## Parameters[](https://nextjs.org/docs/app/api-reference/functions/revalidateTag#parameters)
```
revalidateTag(tag: string, profile: string | { expire?: number }): void;
```

  * `tag`: A string representing the cache tag associated with the data you want to revalidate. Must not exceed 256 characters. This value is case-sensitive.
  * `profile`: A string that specifies the revalidation behavior. The recommended value is `"max"` which provides stale-while-revalidate semantics, or any of the other default or custom profiles defined in [`cacheLife`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheLife). Alternatively, you can pass an object with an `expire` property for custom expiration behavior.


Tags must first be assigned to cached data. You can do this in two ways:
  * Using the [`next.tags`](https://nextjs.org/docs/app/guides/caching#fetch-optionsnexttags-and-revalidatetag) option with `fetch` for caching external API requests:


```
fetch(url, { next: { tags: ['posts'] } })
```

  * Using [`cacheTag`](https://nextjs.org/docs/app/api-reference/functions/cacheTag) inside cached functions or components with the `'use cache'` directive:


```
import { cacheTag } from 'next/cache'

async function getData() {
  'use cache'
  cacheTag('posts')
  // ...
}
```

> **Good to know** : The single-argument form `revalidateTag(tag)` is deprecated. It currently works if TypeScript errors are suppressed, but this behavior may be removed in a future version. Update to the two-argument signature.
