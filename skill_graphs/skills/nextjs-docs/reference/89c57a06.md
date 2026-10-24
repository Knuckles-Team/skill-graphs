## Reference[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#reference)
### Cache profile properties[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#cache-profile-properties)
Cache profiles control caching behavior through three timing properties:
  * **[`stale`](https://nextjs.org/docs/app/api-reference/functions/cacheLife#stale)**: How long the client can use cached data without checking the server
  * **[`revalidate`](https://nextjs.org/docs/app/api-reference/functions/cacheLife#revalidate)**: After this time, the next request will trigger a background refresh
  * **[`expire`](https://nextjs.org/docs/app/api-reference/functions/cacheLife#expire)**: After this time with no requests, the next one waits for fresh content


####  `stale`[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#stale)
**Client-side:** How long the client can use cached data without checking the server.
During this time, the client-side router displays cached content immediately without any network request. After this period expires, the router must check with the server on the next navigation or request. This provides instant page loads from the client cache, but data may be outdated.
  * If omitted, defaults to the `default` profile's `stale` value (5 minutes, see [`staleTimes`](https://nextjs.org/docs/app/api-reference/config/next-config-js/staleTimes))


```
cacheLife({ stale: 300 }) // 5 minutes
```

####  `revalidate`[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#revalidate)
How often the server regenerates cached content in the background.
  * When a request arrives after this period, the server:
    1. Serves the cached version immediately (if available)
    2. Regenerates content in the background
    3. Updates the cache with fresh content
  * Similar to [Incremental Static Regeneration (ISR)](https://nextjs.org/docs/app/guides/incremental-static-regeneration)
  * If omitted, defaults to the `default` profile's `revalidate` value (15 minutes)


```
cacheLife({ revalidate: 900 }) // 15 minutes
```

####  `expire`[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#expire)
Maximum time before the server must regenerate cached content.
  * After this period with no traffic, the server regenerates content synchronously on the next request
  * When you set both `revalidate` and `expire`, `expire` must be longer than `revalidate`. Next.js validates this and raises an error for invalid configurations.
  * If omitted, defaults to the `default` profile's `expire` value (never expires)


```
cacheLife({ expire: 3600 }) // 1 hour
```

### Preset cache profiles[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#preset-cache-profiles)
If you don't specify a profile, Next.js uses the `default` profile. We recommend explicitly setting a profile to make caching behavior clear.
**Profile** | **Use Case** | `stale` | `revalidate` | `expire`
---|---|---|---|---
`default` | Standard content | 5 minutes | 15 minutes | never
`seconds` | Real-time data | 30 seconds | 1 second | 1 minute
`minutes` | Frequently updated content | 5 minutes | 1 minute | 1 hour
`hours` | Content updated multiple times per day | 5 minutes | 1 hour | 1 day
`days` | Content updated daily | 5 minutes | 1 day | 1 week
`weeks` | Content updated weekly | 5 minutes | 1 week | 30 days
`max` | Stable content that rarely changes | 5 minutes | 30 days | 1 year
### Custom cache profiles[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#custom-cache-profiles)
Define reusable cache profiles in your `next.config.ts` file:
next.config.ts
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  cacheComponents: true,
  cacheLife: {
    biweekly: {
      stale: 60 * 60 * 24 * 14, // 14 days
      revalidate: 60 * 60 * 24, // 1 day
      expire: 60 * 60 * 24 * 14, // 14 days
    },
  },
}

export default nextConfig
```

The example above caches for 14 days, checks for updates daily, and expires the cache after 14 days. You can then reference this profile throughout your application by its name:
> **Good to know** : Any omitted properties in a custom profile inherit from the `default` profile. This also applies to inline profile objects passed directly to `cacheLife()`.
app/page.tsx
```
'use cache'
import { cacheLife } from 'next/cache'

export default async function Page() {
  cacheLife('biweekly')
  return <div>Page</div>
}
```

### Overriding the default cache profiles[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#overriding-the-default-cache-profiles)
While the default cache profiles provide a useful way to think about how fresh or stale any given part of cacheable output can be, you may prefer different named profiles to better align with your applications caching strategies.
You can override the default named cache profiles by creating a new configuration with the same name as the defaults.
The example below shows how to override the default `"days"` cache profile:
next.config.ts
```
const nextConfig = {
  cacheComponents: true,
  cacheLife: {
    // Override the 'days' profile
    days: {
      stale: 3600, // 1 hour
      revalidate: 900, // 15 minutes
      expire: 86400, // 1 day
    },
  },
}

export default nextConfig
```

### Inline cache profiles[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#inline-cache-profiles)
For one-off cases, pass a profile object directly to `cacheLife`:
app/page.tsx
```
'use cache'
import { cacheLife } from 'next/cache'

export default async function Page() {
  cacheLife({
    stale: 3600,
    revalidate: 900,
    expire: 86400,
  })

  return <div>Page</div>
}
```

Inline profiles apply only to the specific function or component. For reusable configurations, define custom profiles in `next.config.ts`.
Using `cacheLife({})` with an empty object applies the `default` profile values.
### Client router cache behavior[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#client-router-cache-behavior)
The `stale` property controls the client-side router cache, not the `Cache-Control` header:
  * The server sends the stale time via the `x-nextjs-stale-time` response header
  * The client router uses this value to determine when to revalidate
  * **Minimum of 30 seconds is enforced** to ensure prefetched links remain usable


This 30-second minimum prevents prefetched data from expiring before users can click on links. It only applies to time-based expiration.
When you call revalidation functions from a Server Action ([`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag), [`revalidatePath`](https://nextjs.org/docs/app/api-reference/functions/revalidatePath), [`updateTag`](https://nextjs.org/docs/app/api-reference/functions/updateTag), or [`refresh`](https://nextjs.org/docs/app/api-reference/functions/refresh)), the entire client cache is immediately cleared, bypassing the stale time.
> **Good to know** : The `stale` property in `cacheLife` differs from [`staleTimes`](https://nextjs.org/docs/app/api-reference/config/next-config-js/staleTimes). While `staleTimes` is a global setting affecting all routes, `cacheLife` allows per-function or per-route configuration. Updating `staleTimes.static` also updates the `stale` value of the `default` cache profile.
