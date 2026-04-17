## Web Vitals[](https://nextjs.org/docs/app/guides/analytics#web-vitals)
You can handle all the results of these metrics using the `name` property.
app/_components/web-vitals.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { useReportWebVitals } from 'next/web-vitals'

export function WebVitals() {
  useReportWebVitals((metric) => {
    switch (metric.name) {
      case 'FCP': {
        // handle FCP results
      }
      case 'LCP': {
        // handle LCP results
      }
      // ...
    }
  })
}
```
