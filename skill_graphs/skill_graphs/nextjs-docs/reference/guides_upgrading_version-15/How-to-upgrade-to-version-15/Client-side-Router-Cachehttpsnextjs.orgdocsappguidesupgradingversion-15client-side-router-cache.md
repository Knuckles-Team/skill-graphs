## Client-side Router Cache[](https://nextjs.org/docs/app/guides/upgrading/version-15#client-side-router-cache)
When navigating between pages via `<Link>` or `useRouter`, [page](https://nextjs.org/docs/app/api-reference/file-conventions/page) segments are no longer reused from the client-side router cache. However, they are still reused during browser backward and forward navigation and for shared layouts.
To opt page segments into caching, you can use the [`staleTimes`](https://nextjs.org/docs/app/api-reference/config/next-config-js/staleTimes) config option:
next.config.js
```
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    staleTimes: {
      dynamic: 30,
      static: 180,
    },
  },
}

module.exports = nextConfig
```

[Layouts](https://nextjs.org/docs/app/api-reference/file-conventions/layout) and [loading states](https://nextjs.org/docs/app/api-reference/file-conventions/loading) are still cached and reused on navigation.
