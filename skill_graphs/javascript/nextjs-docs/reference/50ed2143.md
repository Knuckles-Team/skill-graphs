## Client Instrumentation[](https://nextjs.org/docs/pages/guides/analytics#client-instrumentation)
For more advanced analytics and monitoring needs, Next.js provides a `instrumentation-client.js|ts` file that runs before your application's frontend code starts executing. This is ideal for setting up global analytics, error tracking, or performance monitoring tools.
To use it, create an `instrumentation-client.js` or `instrumentation-client.ts` file in your application's root directory:
instrumentation-client.js
```
// Initialize analytics before the app starts
console.log('Analytics initialized')

// Set up global error tracking
window.addEventListener('error', (event) => {
  // Send to your error tracking service
  reportError(event.error)
})
```
