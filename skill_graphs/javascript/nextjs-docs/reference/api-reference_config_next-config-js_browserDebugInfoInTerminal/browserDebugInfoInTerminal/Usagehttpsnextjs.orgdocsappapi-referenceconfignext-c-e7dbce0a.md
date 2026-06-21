## Usage[](https://nextjs.org/docs/app/api-reference/config/next-config-js/browserDebugInfoInTerminal#usage)
Enable forwarding:
next.config.ts
TypeScript
JavaScript TypeScript
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    browserDebugInfoInTerminal: true,
  },
}

export default nextConfig
```

### Serialization limits[](https://nextjs.org/docs/app/api-reference/config/next-config-js/browserDebugInfoInTerminal#serialization-limits)
Deeply nested objects/arrays are truncated using **sensible defaults**. You can tweak these limits:
  * **depthLimit** : (optional) Limit stringification depth for nested objects/arrays. Default: 5
  * **edgeLimit** : (optional) Max number of properties or elements to include per object or array. Default: 100


next.config.ts
TypeScript
JavaScript TypeScript
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    browserDebugInfoInTerminal: {
      depthLimit: 5,
      edgeLimit: 100,
    },
  },
}

export default nextConfig
```

### Source location[](https://nextjs.org/docs/app/api-reference/config/next-config-js/browserDebugInfoInTerminal#source-location)
Source locations are included by default when this feature is enabled.
app/page.tsx
```
'use client'

export default function Home() {
  return (
    <button
      type="button"
      onClick={() => {
        console.log('Hello World')
      }}
    >
      Click me
    </button>
  )
}
```

Clicking the button prints this message to the terminal.
Terminal
```
[browser] Hello World (app/page.tsx:8:17)
```

To suppress them, set `showSourceLocation: false`.
  * **showSourceLocation** : Include source location info when available.


next.config.ts
TypeScript
JavaScript TypeScript
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    browserDebugInfoInTerminal: {
      showSourceLocation: false,
    },
  },
}

export default nextConfig
```

Version | Changes
---|---
`v15.4.0` | experimental `browserDebugInfoInTerminal` introduced
[PreviousbasePath](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath)[NextcacheComponents](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents)
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
