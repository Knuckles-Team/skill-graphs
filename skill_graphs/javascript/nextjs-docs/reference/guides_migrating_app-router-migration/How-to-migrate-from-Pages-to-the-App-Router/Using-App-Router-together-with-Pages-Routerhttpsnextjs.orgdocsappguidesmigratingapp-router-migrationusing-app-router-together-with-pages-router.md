## Using App Router together with Pages Router[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#using-app-router-together-with-pages-router)
When navigating between routes served by the different Next.js routers, there will be a hard navigation. Automatic link prefetching with `next/link` will not prefetch across routers.
Instead, you can
