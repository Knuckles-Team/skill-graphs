# useReportWebVitals
Last updated February 27, 2026
The `useReportWebVitals` hook allows you to report
New functions passed to `useReportWebVitals` are called with the available metrics up to that point. To prevent reporting duplicated data, ensure that the callback function reference does not change (as shown in the code examples below).
pages/_app.js
```
import { useReportWebVitals } from 'next/web-vitals'

const logWebVitals = (metric) => {
  console.log(metric)
}

function MyApp({ Component, pageProps }) {
  useReportWebVitals(logWebVitals)

  return <Component {...pageProps} />
}
```
