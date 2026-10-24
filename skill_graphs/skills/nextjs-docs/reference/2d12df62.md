## Web Vitals[](https://nextjs.org/docs/pages/guides/analytics#web-vitals)
You can handle all the results of these metrics using the `name` property.
pages/_app.js
```
import { useReportWebVitals } from 'next/web-vitals'

function MyApp({ Component, pageProps }) {
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

  return <Component {...pageProps} />
}
```
