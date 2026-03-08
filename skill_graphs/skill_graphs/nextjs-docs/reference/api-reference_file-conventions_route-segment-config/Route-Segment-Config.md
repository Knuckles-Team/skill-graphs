# Route Segment Config
Last updated February 27, 2026
> **Good to know** :
>   * The options outlined on this page are disabled if the [`cacheComponents`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents) flag is on, and will eventually be deprecated in the future.
>   * Route Segment options only take effect in Server Component Pages, Layouts, or Route Handlers.
>   * `generateStaticParams` cannot be used inside a `'use client'` file.
>

The Route Segment options allows you to configure the behavior of a [Page](https://nextjs.org/docs/app/api-reference/file-conventions/layout), [Layout](https://nextjs.org/docs/app/api-reference/file-conventions/layout), or [Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route) by directly exporting the following variables:
Option | Type | Default
---|---|---
[`dynamic`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamic) | `'auto' | 'force-dynamic' | 'error' | 'force-static'` | `'auto'`
[`dynamicParams`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamicparams) | `boolean` | `true`
[`revalidate`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#revalidate) | `false | 0 | number` | `false`
[`fetchCache`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#fetchcache) | `'auto' | 'default-cache' | 'only-cache' | 'force-cache' | 'force-no-store' | 'default-no-store' | 'only-no-store'` | `'auto'`
[`runtime`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#runtime) | `'nodejs' | 'edge'` | `'nodejs'`
[`preferredRegion`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#preferredregion) | `'auto' | 'global' | 'home' | string | string[]` | `'auto'`
[`maxDuration`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#maxduration) | `number` | Set by deployment platform
