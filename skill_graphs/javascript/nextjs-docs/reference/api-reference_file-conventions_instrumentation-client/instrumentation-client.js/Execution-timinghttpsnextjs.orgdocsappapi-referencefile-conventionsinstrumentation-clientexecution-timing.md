## Execution timing[](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation-client#execution-timing)
The `instrumentation-client.js` file executes at a specific point in the application lifecycle:
  1. **After** the HTML document is loaded
  2. **Before** React hydration begins
  3. **Before** user interactions are possible


This timing makes it ideal for setting up error tracking, analytics, and performance monitoring that needs to capture early application lifecycle events.
