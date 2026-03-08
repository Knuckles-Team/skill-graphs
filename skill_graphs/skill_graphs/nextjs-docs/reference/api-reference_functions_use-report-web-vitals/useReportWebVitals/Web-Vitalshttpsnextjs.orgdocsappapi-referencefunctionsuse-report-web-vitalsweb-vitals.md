## Web Vitals[](https://nextjs.org/docs/app/api-reference/functions/use-report-web-vitals#web-vitals)
You can handle all the results of these metrics using the `name` property.
app/components/web-vitals.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { useReportWebVitals } from 'next/web-vitals'

type ReportWebVitalsCallback = Parameters<typeof useReportWebVitals>[0]

const handleWebVitals: ReportWebVitalsCallback = (metric) => {
  switch (metric.name) {
    case 'FCP': {
      // handle FCP results
    }
    case 'LCP': {
      // handle LCP results
    }
    // ...
  }
}

export function WebVitals() {
  useReportWebVitals(handleWebVitals)
}
```
