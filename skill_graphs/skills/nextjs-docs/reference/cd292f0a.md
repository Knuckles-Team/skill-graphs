## Examples[](https://nextjs.org/docs/app/api-reference/functions/use-pathname#examples)
### Do something in response to a route change[](https://nextjs.org/docs/app/api-reference/functions/use-pathname#do-something-in-response-to-a-route-change)
app/example-client-component.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { useEffect } from 'react'
import { usePathname, useSearchParams } from 'next/navigation'

function ExampleClientComponent() {
  const pathname = usePathname()
  const searchParams = useSearchParams()
  useEffect(() => {
    // Do something here...
  }, [pathname, searchParams])
}
```

### Avoid hydration mismatch with rewrites[](https://nextjs.org/docs/app/api-reference/functions/use-pathname#avoid-hydration-mismatch-with-rewrites)
When a page is pre-rendered, the HTML is generated for the source pathname. If the page is then reached through a rewrite using `next.config` or `Proxy`, the browser URL may differ, and `usePathname()` will read the rewritten pathname on the client.
To avoid hydration mismatches, design the UI so that only a small, isolated part depends on the client pathname. Render a stable fallback on the server and update that part after mount.
app/example-client-component.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { useEffect, useState } from 'react'
import { usePathname } from 'next/navigation'

export default function PathnameBadge() {
  const pathname = usePathname()
  const [clientPathname, setClientPathname] = useState('')

  useEffect(() => {
    setClientPathname(pathname)
  }, [pathname])

  return (
    <p>
      Current pathname: <span>{clientPathname}</span>
    </p>
  )
}
```

Version | Changes
---|---
`v13.0.0` |  `usePathname` introduced.
[PrevioususeParams](https://nextjs.org/docs/app/api-reference/functions/use-params)[NextuseReportWebVitals](https://nextjs.org/docs/app/api-reference/functions/use-report-web-vitals)
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
