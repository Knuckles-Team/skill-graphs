# unstable_cache
Last updated February 27, 2026
> **Note:** This API has been replaced by [`use cache`](https://nextjs.org/docs/app/api-reference/directives/use-cache) in Next.js 16. We recommend opting into [Cache Components](https://nextjs.org/docs/app/getting-started/cache-components) and replacing `unstable_cache` with the `use cache` directive.
`unstable_cache` allows you to cache the results of expensive operations, like database queries, and reuse them across multiple requests.
```
import { getUser } from './data';
import { unstable_cache } from 'next/cache';

const getCachedUser = unstable_cache(
  async (id) => getUser(id),
  ['my-app-user']
);

export default async function Component({ userID }) {
  const user = await getCachedUser(userID);
  ...
}
```

> **Good to know** :
>   * Accessing dynamic data sources such as `headers` or `cookies` inside a cache scope is not supported. If you need this data inside a cached function use `headers` outside of the cached function and pass the required dynamic data in as an argument.
>   * This API uses Next.js' built-in [Data Cache](https://nextjs.org/docs/app/guides/caching#data-cache) to persist the result across requests and deployments.
>
