##  [Using runtime cache](https://vercel.com/docs/regions#using-runtime-cache)[](https://vercel.com/docs/regions#using-runtime-cache)
You can cache your Vercel function with any framework by using the functions of the helper method [`getCache`](https://vercel.com/docs/functions/functions-api-reference/vercel-functions-package#getcache).
###  [Runtime cache with any framework](https://vercel.com/docs/regions#runtime-cache-with-any-framework)[](https://vercel.com/docs/regions#runtime-cache-with-any-framework)
This example caches data fetched from the API so that it expires after 1 hour and adds a tag to the cache entry so you can invalidate it later from code:
api/your-function.ts
```

import { getCache } from '@vercel/functions';

export default {
  async fetch(request) {
    const cache = getCache();

    // Get a value from cache
    const value = await cache.get('somekey');

    if (value) {
      return new Response(JSON.stringify(value));
    }

    const res = await fetch('https://api.vercel.app/blog');
    const originValue = await res.json();

    // Set a value in cache with TTL and tags
    await cache.set('somekey', originValue, {
      ttl: 3600, // 1 hour in seconds
      tags: ['example-tag'],
    });

    return new Response(JSON.stringify(originValue));
  },
};
```

###  [Runtime cache with Next.js](https://vercel.com/docs/regions#runtime-cache-with-next.js)[](https://vercel.com/docs/regions#runtime-cache-with-next.js)
With Next.js, you can use runtime cache or data cache in the following ways:
Next.js version | Runtime cache | Data cache
---|---|---
Next.js 16 and above |  [`use cache: remote`](https://vercel.com/docs/regions#using-use-cache:-remote) or [fetch with `getCache`](https://vercel.com/docs/functions/functions-api-reference/vercel-functions-package#getcache) | [fetch with `force-cache`](https://vercel.com/docs/regions#using-fetch-with-force-cache)
Next.js 15 | [fetch with `getCache`](https://vercel.com/docs/functions/functions-api-reference/vercel-functions-package#getcache) |  [fetch](https://vercel.com/docs/runtime-cache/data-cache) or [`unstable_cache`](https://vercel.com/docs/regions#using-unstable_cache)
Next.js 14 and below | [fetch with `getCache`](https://vercel.com/docs/functions/functions-api-reference/vercel-functions-package#getcache) | [fetch](https://vercel.com/docs/runtime-cache/data-cache)
###  [Next.js 16 and above](https://vercel.com/docs/regions#next.js-16-and-above)[](https://vercel.com/docs/regions#next.js-16-and-above)
With Next.js 16, you have two options for runtime caching:
  * `use cache: remote`: A directive that caches entire functions or components with Runtime cache. Requires enabling `cacheComponents` in your config.
  * `fetch` with `force-cache`: Caches individual fetch requests without additional configuration with [Data cache](https://vercel.com/docs/runtime-cache/data-cache).


####  [Using use cache: remote](https://vercel.com/docs/regions#using-use-cache:-remote)[](https://vercel.com/docs/regions#using-use-cache:-remote)
Use the `use cache: remote` directive at the file, component, or function level to cache the output of a function or component.
`use cache` is in-memory by default. This means that it is ephemeral, and disappears when the instance that served the request is shut down. `use cache: remote` is a declarative way telling the system to store the cached output in a remote cache such Vercel runtime cache.
First, enable the `cacheComponents` flag in your `next.config.ts` file:
next.config.ts
```
import type { NextConfig } from 'next';

const nextConfig: NextConfig = {
  cacheComponents: true,
};

export default nextConfig;
```

Then, use the `use cache: remote` directive in your code. This example caches data so that it expires after 1 hour and adds a tag to the cache entry so you can invalidate it later from code:
app/page.tsx
```
import { cacheLife, cacheTag } from 'next/cache';

export default async function Page() {
  const data = await getData();

  return (
    <main>
      <h1>Data</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </main>
  );
}

async function getData() {
  'use cache: remote'
  cacheTag('example-tag')
  cacheLife({ expire: 3600 }) // 1 hour

  const response = await fetch('https://api.example.com/data');
  return response.json();
}
```

You can also use runtime cache in API routes:
app/api/products/route.ts
```
import { cacheLife } from 'next/cache';

export async function GET() {
  const data = await getProducts();
  return Response.json(data);
}

async function getProducts() {
  'use cache: remote'
  cacheLife({ expire: 3600 }) // 1 hour

  const response = await fetch('https://api.example.com/products');
  return response.json();
}
```

####  [Using fetch with force-cache](https://vercel.com/docs/regions#using-fetch-with-force-cache)[](https://vercel.com/docs/regions#using-fetch-with-force-cache)
If you don't enable `cacheComponents`, you can use `fetch` with `cache: 'force-cache'` to cache individual fetch requests:
app/page.tsx
```
export default async function Page() {
  const res = await fetch('https://api.example.com/blog', {
    cache: 'force-cache',
    next: {
      revalidate: 3600, // revalidate in background every hour
      tags: ['blog'],
    },
  });
  const data = await res.json();

  return (
    <main>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </main>
  );
}
```

###  [Next.js 15](https://vercel.com/docs/regions#next.js-15)[](https://vercel.com/docs/regions#next.js-15)
In Next.js 15, use the `fetch()` API with `cache: 'force-cache'` or `unstable_cache` for runtime caching with [Data cache](https://vercel.com/docs/runtime-cache/data-cache).
####  [Using fetch with cache options](https://vercel.com/docs/regions#using-fetch-with-cache-options)[](https://vercel.com/docs/regions#using-fetch-with-cache-options)
Use `cache: 'force-cache'` to persist data in the cache:
app/page.tsx
```
export default async function Page() {
  const res = await fetch('https://api.example.com/blog', {
    cache: 'force-cache',
  });
  const data = await res.json();

  return (
    <main>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </main>
  );
}
```

For time-based revalidation, combine `cache: 'force-cache'` with the `next.revalidate` option:
app/page.tsx
```
export default async function Page() {
  const res = await fetch('https://api.example.com/blog', {
    cache: 'force-cache',
    next: {
      revalidate: 3600, // revalidate in background every hour
    },
  });
  const data = await res.json();

  return (
    <main>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </main>
  );
}
```

For tag-based revalidation, combine `cache: 'force-cache'` with the `next.tags` option:
app/page.tsx
```
export default async function Page() {
  const res = await fetch('https://api.example.com/blog', {
    cache: 'force-cache',
    next: {
      tags: ['blog'],
    },
  });
  const data = await res.json();

  return (
    <main>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </main>
  );
}
```

Then invalidate the cache using `revalidateTag`:
app/actions.ts
```
'use server';

import { revalidateTag } from 'next/cache';

export async function invalidateBlog() {
  revalidateTag('blog');
}
```

####  [Using unstable_cache](https://vercel.com/docs/regions#using-unstable_cache)[](https://vercel.com/docs/regions#using-unstable_cache)
For non-fetch data sources, use `unstable_cache`:
app/page.tsx
```
import { unstable_cache } from 'next/cache';

const getCachedData = unstable_cache(
  async () => {
    // Fetch from database, API, or other source
    const data = await db.query('SELECT * FROM posts');
    return data;
  },
  ['posts'], // Cache key
  {
    revalidate: 3600, // 1 hour
    tags: ['posts'],
  }
);

export default async function Page() {
  const data = await getCachedData();

  return (
    <main>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </main>
  );
}
```

###  [Next.js 14 and below](https://vercel.com/docs/regions#next.js-14-and-below)[](https://vercel.com/docs/regions#next.js-14-and-below)
If you're using Next.js 14 or below, see [Data Cache](https://vercel.com/docs/runtime-cache/data-cache) for the legacy caching approach or use the framework-agnostic [`getCache`](https://vercel.com/docs/functions/functions-api-reference/vercel-functions-package#getcache) function.
###  [Revalidation](https://vercel.com/docs/regions#revalidation)[](https://vercel.com/docs/regions#revalidation)
You can control how long data stays cached using the following revalidation options:
####  [Time-based revalidation](https://vercel.com/docs/regions#time-based-revalidation)[](https://vercel.com/docs/regions#time-based-revalidation)
This example revalidates the cache every hour:
The Next.js examples are for Next.js 15 and above. For Next.js 14 and below, see [Data Cache](https://vercel.com/docs/runtime-cache/data-cache).
app/api/products/route.ts
TypeScript JavaScript
Next.js (/app) Next.js (/pages) Other frameworks
```
import type { NextApiRequest, NextApiResponse } from 'next';
import { cacheLife, cacheTag } from 'next/cache';

export default async function handler(
  request: NextApiRequest,
  response: NextApiResponse,
) {
  const data = await getProducts();
  return response.status(200).json(data);
}

async function getProducts() {
  'use cache: remote'
  cacheTag('products')
  cacheLife({ expire: 3600 }) // 1 hour

  const response = await fetch('https://api.example.com/products');
  return response.json();
}
```

```
import { cacheLife, cacheTag } from 'next/cache';

export default async function handler(request, response) {
  const data = await getProducts();
  return response.status(200).json(data);
}

async function getProducts() {
  'use cache: remote'
  cacheTag('products')
  cacheLife({ expire: 3600 }) // 1 hour

  const response = await fetch('https://api.example.com/products');
  return response.json();
}
```

```
import { cacheLife } from 'next/cache';

export async function GET() {
  const data = await getProducts();
  return Response.json(data);
}

async function getProducts() {
  'use cache: remote'
  cacheLife({ expire: 3600 }) // 1 hour

  const response = await fetch('https://api.example.com/products');
  return response.json();
}
```

```
import { cacheLife } from 'next/cache';

export async function GET() {
  const data = await getProducts();
  return Response.json(data);
}

async function getProducts() {
  'use cache: remote'
  cacheLife({ expire: 3600 }) // 1 hour

  const response = await fetch('https://api.example.com/products');
  return response.json();
}
```

```
import { getCache } from '@vercel/functions';

export default {
  async fetch(request: Request) {
    const cache = getCache();

    // Try to get from cache
    const cachedData = await cache.get('products');

    if (cachedData) {
      return Response.json(cachedData);
    }

    // Fetch from origin
    const response = await fetch('https://api.example.com/products');
    const data = await response.json();

    // Store in cache with TTL
    await cache.set('products', data, {
      ttl: 3600, // 1 hour in seconds
    });

    return Response.json(data);
  },
};
```

```
import { getCache } from '@vercel/functions';

export default {
  async fetch(request) {
    const cache = getCache();

    // Try to get from cache
    const cachedData = await cache.get('products');

    if (cachedData) {
      return Response.json(cachedData);
    }

    // Fetch from origin
    const response = await fetch('https://api.example.com/products');
    const data = await response.json();

    // Store in cache with TTL
    await cache.set('products', data, {
      ttl: 3600, // 1 hour in seconds
    });

    return Response.json(data);
  },
};
```

####  [Tag-based revalidation](https://vercel.com/docs/regions#tag-based-revalidation)[](https://vercel.com/docs/regions#tag-based-revalidation)
This example associates the `products` tag with the data:
app/api/products/route.ts
TypeScript JavaScript
Next.js (/app) Next.js (/pages) Other frameworks
```
import type { NextApiRequest, NextApiResponse } from 'next';
import { cacheLife, cacheTag } from 'next/cache';

export default async function handler(
  request: NextApiRequest,
  response: NextApiResponse,
) {
  const data = await getProducts();
  return response.status(200).json(data);
}

async function getProducts() {
  'use cache: remote'
  cacheTag('products')
  cacheLife({ expire: 3600 }) // 1 hour

  const response = await fetch('https://api.example.com/products');
  return response.json();
}
```

```
import { cacheLife, cacheTag } from 'next/cache';

export default async function handler(request, response) {
  const data = await getProducts();
  return response.status(200).json(data);
}

async function getProducts() {
  'use cache: remote'
  cacheTag('products')
  cacheLife({ expire: 3600 }) // 1 hour

  const response = await fetch('https://api.example.com/products');
  return response.json();
}
```

```
import { cacheLife, cacheTag } from 'next/cache';

export async function GET() {
  const data = await getProducts();
  return Response.json(data);
}

async function getProducts() {
  'use cache: remote'
  cacheTag('products')
  cacheLife({ expire: 3600 }) // 1 hour

  const response = await fetch('https://api.example.com/products');
  return response.json();
}
```

```
import { cacheLife, cacheTag } from 'next/cache';

export async function GET() {
  const data = await getProducts();
  return Response.json(data);
}

async function getProducts() {
  'use cache: remote'
  cacheTag('products')
  cacheLife({ expire: 3600 }) // 1 hour

  const response = await fetch('https://api.example.com/products');
  return response.json();
}
```

```
import { getCache } from '@vercel/functions';

export default {
  async fetch(request: Request) {
    const cache = getCache();

    // Try to get from cache
    const cachedData = await cache.get('products');

    if (cachedData) {
      return Response.json(cachedData);
    }

    // Fetch from origin
    const response = await fetch('https://api.example.com/products');
    const data = await response.json();

    // Store in cache with TTL and tags
    await cache.set('products', data, {
      ttl: 3600, // 1 hour in seconds
      tags: ['products'],
    });

    return Response.json(data);
  },
};
```

```
import { getCache } from '@vercel/functions';

export default {
  async fetch(request) {
    const cache = getCache();

    // Try to get from cache
    const cachedData = await cache.get('products');

    if (cachedData) {
      return Response.json(cachedData);
    }

    // Fetch from origin
    const response = await fetch('https://api.example.com/products');
    const data = await response.json();

    // Store in cache with TTL and tags
    await cache.set('products', data, {
      ttl: 3600, // 1 hour in seconds
      tags: ['products'],
    });

    return Response.json(data);
  },
};
```

You can then revalidate the cache for any data associated with the `products` tag by using the `revalidateTag` function. For example, use a server action:
app/actions.ts
```
import { revalidateTag } from 'next/cache';

export async function invalidateProductsCache() {
  revalidateTag('products');
}
```

####  [Path-based revalidation](https://vercel.com/docs/regions#path-based-revalidation)[](https://vercel.com/docs/regions#path-based-revalidation)
This example revalidates the cache for the `/products` path using a server action:
app/actions.ts
```
import { revalidatePath } from 'next/cache';

export async function POST() {
  revalidatePath('/products');
}
```
