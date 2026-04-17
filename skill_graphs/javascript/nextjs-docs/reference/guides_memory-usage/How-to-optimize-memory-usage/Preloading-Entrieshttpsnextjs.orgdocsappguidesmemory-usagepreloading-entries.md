## Preloading Entries[](https://nextjs.org/docs/app/guides/memory-usage#preloading-entries)
When the Next.js server starts, it preloads each page's JavaScript modules into memory, rather than at request time.
This optimization allows for faster response times, in exchange for a larger initial memory footprint.
To disable this optimization, set the `experimental.preloadEntriesOnStart` flag to `false`.
next.config.ts
TypeScript
JavaScript TypeScript
```
import type { NextConfig } from 'next'

const config: NextConfig = {
  experimental: {
    preloadEntriesOnStart: false,
  },
}

export default config
```

Next.js doesn't unload these JavaScript modules, meaning that even with this optimization disabled, the memory footprint of your Next.js server will eventually be the same if all pages are eventually requested.
[PreviousMDX](https://nextjs.org/docs/app/guides/mdx)[NextMigrating](https://nextjs.org/docs/app/guides/migrating)
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
