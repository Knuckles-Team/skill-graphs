## Web Vitals[](https://nextjs.org/docs/pages/api-reference/functions/use-report-web-vitals#web-vitals)
You can handle all the results of these metrics using the `name` property.
pages/_app.js
```
import { useReportWebVitals } from 'next/web-vitals'

const handleWebVitals = (metric) => {
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

function MyApp({ Component, pageProps }) {
  useReportWebVitals(handleWebVitals)

  return <Component {...pageProps} />
}
```
