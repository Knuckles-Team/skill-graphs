##  [Using data cache](https://vercel.com/docs/routing#using-data-cache)[](https://vercel.com/docs/routing#using-data-cache)
When you deploy a Next.js project that uses
###  [Time-based revalidation](https://vercel.com/docs/routing#time-based-revalidation)[](https://vercel.com/docs/routing#time-based-revalidation)
app/page.tsx
TypeScript
TypeScript JavaScript Bash
```
export default async function Page() {
  const res = await fetch('https://api.vercel.app/blog', {
    next: {
      revalidate: 3600, // 1 hour
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

###  [Tag-based revalidation](https://vercel.com/docs/routing#tag-based-revalidation)[](https://vercel.com/docs/routing#tag-based-revalidation)
app/page.tsx
TypeScript
TypeScript JavaScript Bash
```
export default async function Page() {
  const res = await fetch('https://api.vercel.app/blog', {
    next: {
      tags: ['blog'], // Invalidate with revalidateTag('blog') on-demand
    },
  });
  const data = await res.json();

  return '...';
}
```

app/actions.ts
TypeScript
TypeScript JavaScript Bash
```
'use server';

import { revalidateTag } from 'next/cache';

export default async function action() {
  revalidateTag('blog');
}
```

###  [Revalidation behavior](https://vercel.com/docs/routing#revalidation-behavior)[](https://vercel.com/docs/routing#revalidation-behavior)
Vercel persists cached data across deployments, unless you explicitly invalidate it using framework APIs like `res.revalidate`, `revalidateTag`, and `revalidatePath`, or by [manually purging the cache](https://vercel.com/docs/routing#manually-purging-data-cache). Cache is not updated at build time. When invalidated, Vercel updates the data at run time, triggered by the next request to the invalidated path.
When the system triggers a revalidation, Vercel marks the corresponding path or cache tag as stale in every region. The next request to that path or tag, regardless of the region, initiates revalidation and updates the cache globally. Vercel purges and updates the regional cache in all regions within 300ms.
