## Removals[](https://nextjs.org/docs/app/guides/upgrading/version-16#removals)
These features were previously deprecated and are now removed:
### AMP Support[](https://nextjs.org/docs/app/guides/upgrading/version-16#amp-support)
AMP adoption has declined significantly, and maintaining this feature adds complexity to the framework. All AMP APIs and configurations have been removed:
  * `amp` configuration from your Next config file
  * `next/amp` hook imports and usage (`useAmp`)


```
// Removed
import { useAmp } from 'next/amp'

// Removed
export const config = { amp: true }
```

  * `export const config = { amp: true }` from pages


next.config.js
```
const nextConfig = {
  // Removed
  amp: {
    canonicalBase: 'https://example.com',
  },
}

export default nextConfig
```

Evaluate if AMP is still necessary for your use case. Most performance benefits can now be achieved through Next.js's built-in optimizations and modern web standards.
###  `next lint` Command[](https://nextjs.org/docs/app/guides/upgrading/version-16#next-lint-command)
The `next lint` command has been removed. Use Biome or ESLint directly. `next build` no longer runs linting.
A codemod is available to automate migration:
pnpmnpmyarnbun
Terminal
```
pnpm dlx @next/codemod@canary next-lint-to-eslint-cli .
```

The `eslint` option in the Next.js config file is also removed.
next.config.mjs
```
/** @type {import('next').NextConfig} */
const nextConfig = {
  // No longer supported
  // eslint: {},
}

export default nextConfig
```

### Runtime Configuration[](https://nextjs.org/docs/app/guides/upgrading/version-16#runtime-configuration)
`serverRuntimeConfig` and `publicRuntimeConfig` have been removed. Use environment variables instead.
**Before (Next.js 15):**
next.config.js
```
module.exports = {
  serverRuntimeConfig: {
    dbUrl: process.env.DATABASE_URL,
  },
  publicRuntimeConfig: {
    apiUrl: '/api',
  },
}
```

pages/index.tsx
```
import getConfig from 'next/config'

export default function Page() {
  const { publicRuntimeConfig } = getConfig()
  return <p>API URL: {publicRuntimeConfig.apiUrl}</p>
}
```

**After (Next.js 16):**
For server-only values, access environment variables directly in Server Components:
app/page.tsx
```
async function fetchData() {
  const dbUrl = process.env.DATABASE_URL
  // Use for server-side operations only
  return await db.query(dbUrl, 'SELECT * FROM users')
}

export default async function Page() {
  const data = await fetchData()
  return <div>{/* render data */}</div>
}
```

> **Good to know** : Use the [taint API](https://nextjs.org/docs/app/api-reference/config/next-config-js/taint) to prevent accidentally passing sensitive server values to Client Components.
For client-accessible values, use the `NEXT_PUBLIC_` prefix:
.env.local
```
NEXT_PUBLIC_API_URL="/api"
```

app/components/client-component.tsx
```
'use client'

export default function ClientComponent() {
  const apiUrl = process.env.NEXT_PUBLIC_API_URL
  return <p>API URL: {apiUrl}</p>
}
```

To ensure environment variables are read at runtime (not bundled at build time), use the [`connection()`](https://nextjs.org/docs/app/api-reference/functions/connection) function before reading from `process.env`:
app/page.tsx
```
import { connection } from 'next/server'

export default async function Page() {
  await connection()
  const config = process.env.RUNTIME_CONFIG
  return <p>{config}</p>
}
```

Learn more about [environment variables](https://nextjs.org/docs/app/guides/environment-variables).
###  `devIndicators` Options[](https://nextjs.org/docs/app/guides/upgrading/version-16#devindicators-options)
The following options have been removed from [`devIndicators`](https://nextjs.org/docs/app/api-reference/config/next-config-js/devIndicators):
  * `appIsrStatus`
  * `buildActivity`
  * `buildActivityPosition`


The indicator itself remains available.
###  `experimental.dynamicIO`[](https://nextjs.org/docs/app/guides/upgrading/version-16#experimentaldynamicio)
The `experimental.dynamicIO` flag has been renamed to `cacheComponents`:
Update your Next config file, by removing the `dynamicIO` flag.
next.config.js
```
// Next.js 15 - experimental.dynamicIO is now removed
module.exports = {
  experimental: {
    dynamicIO: true,
  },
}
```

Add the [`cacheComponents`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents) flag set to true.
next.config.js
```
// Next.js 16 - use cacheComponents instead
module.exports = {
  cacheComponents: true,
}
```

###  `unstable_rootParams`[](https://nextjs.org/docs/app/guides/upgrading/version-16#unstable_rootparams)
The `unstable_rootParams` function has been removed. We are working on an alternative API that we will ship in an upcoming minor release.
[PreviousVersion 15](https://nextjs.org/docs/app/guides/upgrading/version-15)[NextVideos](https://nextjs.org/docs/app/guides/videos)
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
