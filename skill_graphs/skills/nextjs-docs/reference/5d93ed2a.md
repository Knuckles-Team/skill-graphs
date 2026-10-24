##  `NextRequest` Geolocation[](https://nextjs.org/docs/app/guides/upgrading/version-15#nextrequest-geolocation)
The `geo` and `ip` properties on `NextRequest` have been removed as these values are provided by your hosting provider. A [codemod](https://nextjs.org/docs/app/guides/upgrading/codemods#150) is available to automate this migration.
If you are using Vercel, you can alternatively use the `geolocation` and `ipAddress` functions from
middleware.ts
```
import { geolocation } from '@vercel/functions'
import type { NextRequest } from 'next/server'

export function middleware(request: NextRequest) {
  const { city } = geolocation(request)

  // ...
}
```

middleware.ts
```
import { ipAddress } from '@vercel/functions'
import type { NextRequest } from 'next/server'

export function middleware(request: NextRequest) {
  const ip = ipAddress(request)

  // ...
}
```

[PreviousVersion 14](https://nextjs.org/docs/app/guides/upgrading/version-14)[NextVersion 16](https://nextjs.org/docs/app/guides/upgrading/version-16)
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
