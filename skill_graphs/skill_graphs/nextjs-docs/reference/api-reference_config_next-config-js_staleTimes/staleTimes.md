# staleTimes
This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on
Last updated February 27, 2026
`staleTimes` is an experimental feature that enables caching of page segments in the [client-side router cache](https://nextjs.org/docs/app/guides/caching#client-side-router-cache).
You can enable this experimental feature and provide custom revalidation times by setting the experimental `staleTimes` flag:
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

The `static` and `dynamic` properties correspond with the time period (in seconds) based on different types of [link prefetching](https://nextjs.org/docs/app/api-reference/components/link#prefetch).
  * The `dynamic` property is used when the page is neither statically generated nor fully prefetched (e.g. with `prefetch={true}`).
    * Default: 0 seconds (not cached)
  * The `static` property is used for statically generated pages, or when the `prefetch` prop on `Link` is set to `true`, or when calling [`router.prefetch`](https://nextjs.org/docs/app/guides/caching#routerprefetch).
    * Default: 5 minutes


> **Good to know:**
>   * [Loading boundaries](https://nextjs.org/docs/app/api-reference/file-conventions/loading) are considered reusable for the `static` period defined in this configuration.
>   * This doesn't affect [partial rendering](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions), **meaning shared layouts won't automatically be refetched on every navigation, only the page segment that changes.**
>   * This doesn't change [back/forward caching](https://nextjs.org/docs/app/guides/caching#client-side-router-cache) behavior to prevent layout shift and to prevent losing the browser scroll position.
>

You can learn more about the Client Router Cache [here](https://nextjs.org/docs/app/guides/caching#client-side-router-cache).
### Version History[](https://nextjs.org/docs/app/api-reference/config/next-config-js/staleTimes#version-history)
Version | Changes
---|---
`v15.0.0` | The `dynamic` `staleTimes` default changed from 30s to 0s.
`v14.2.0` | Experimental `staleTimes` introduced.
[PreviousserverExternalPackages](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverExternalPackages)[NextstaticGeneration*](https://nextjs.org/docs/app/api-reference/config/next-config-js/staticGeneration)
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
