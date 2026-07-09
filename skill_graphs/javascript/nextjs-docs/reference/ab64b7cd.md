# serverComponentsHmrCache
This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on
Last updated February 27, 2026
The experimental `serverComponentsHmrCache` option allows you to cache `fetch` responses in Server Components across Hot Module Replacement (HMR) refreshes in local development. This results in faster responses and reduced costs for billed API calls.
By default, the HMR cache applies to all `fetch` requests, including those with the `cache: 'no-store'` option. This means uncached requests will not show fresh data between HMR refreshes. However, the cache will be cleared on navigation or full-page reloads.
You can disable the HMR cache by setting `serverComponentsHmrCache` to `false` in your `next.config.js` file:
next.config.ts
TypeScript
JavaScript TypeScript
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    serverComponentsHmrCache: false, // defaults to true
  },
}

export default nextConfig
```

> **Good to know:** For better observability, we recommend using the [`logging.fetches`](https://nextjs.org/docs/app/api-reference/config/next-config-js/logging) option which logs fetch cache hits and misses in the console during development.
[PreviousserverActions](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverActions)[NextserverExternalPackages](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverExternalPackages)
Was this helpful?
Send
* * *
* * *
#### Resources
[Docs](https://nextjs.org/docs)[Support Policy](https://nextjs.org/support-policy)[Learn](https://nextjs.org/learn)[Showcase](https://nextjs.org/showcase)[Blog](https://nextjs.org/blog)[Team](https://nextjs.org/team)[Next.js Conf](https://nextjs.org/conf)[Evals](https://nextjs.org/evals)
#### More
[Telemetry](https://nextjs.org/telemetry)[Governance](https://nextjs.org/governance)
#### About Vercel
#### Legal
Cookie Preferences
#### Subscribe to our newsletter
Stay updated on new releases and features, guides, and case studies.
Subscribe
© 2026 Vercel, Inc.
* * *
* * *
