## Build Your Own[](https://nextjs.org/docs/pages/guides/analytics#build-your-own)
pages/_app.js
```
import { useReportWebVitals } from 'next/web-vitals'

function MyApp({ Component, pageProps }) {
  useReportWebVitals((metric) => {
    console.log(metric)
  })

  return <Component {...pageProps} />
}
```

View the [API Reference](https://nextjs.org/docs/pages/api-reference/functions/use-report-web-vitals) for more information.
