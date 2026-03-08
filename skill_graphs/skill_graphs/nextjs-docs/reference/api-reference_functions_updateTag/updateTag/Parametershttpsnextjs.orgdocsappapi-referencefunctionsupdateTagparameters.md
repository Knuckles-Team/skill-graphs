## Parameters[](https://nextjs.org/docs/app/api-reference/functions/updateTag#parameters)
```
updateTag(tag: string): void;
```

  * `tag`: A string representing the cache tag associated with the data you want to update. Must not exceed 256 characters. This value is case-sensitive.


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
