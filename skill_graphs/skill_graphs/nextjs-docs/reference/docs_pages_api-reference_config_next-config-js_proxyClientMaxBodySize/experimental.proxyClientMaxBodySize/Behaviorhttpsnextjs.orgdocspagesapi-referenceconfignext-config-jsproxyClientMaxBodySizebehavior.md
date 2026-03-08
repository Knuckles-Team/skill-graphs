## Behavior[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/proxyClientMaxBodySize#behavior)
When a request body exceeds the configured limit:
  1. Next.js will buffer only the first N bytes (up to the limit)
  2. A warning will be logged to the console indicating the route that exceeded the limit
  3. The request will continue processing normally, but only the partial body will be available
  4. The request will **not** fail or return an error to the client


If your application needs to process the full request body, you should either:
  * Increase the `proxyClientMaxBodySize` limit
  * Handle the partial body gracefully in your application logic
