##  [Using Observability](https://vercel.com/docs/observability#using-observability)[](https://vercel.com/docs/observability#using-observability)
How you use Observability depends on the needs of your project, for example, perhaps builds are taking longer than expected, or your Vercel Functions seem to be increasing in cost. A brief overview of how you might use the tab would be:
  1. Decide what feature you want to investigate. For example, Vercel Functions.
  2. Use the date picker or the time range selector to choose the time period you want to investigate. Users on [Observability Plus](https://vercel.com/docs/observability/observability-plus) will have a longer retention period and more granular data.
  3. Let's investigate our graphs in more detail, for example, Error Rate. Click and drag to select a period of time and press the Zoom In button.

![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fobservability%2Ferror-rate-light.png&w=1080&q=75)![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fobservability%2Ferror-rate-dark.png&w=1080&q=75)
  1. Then, from the list of routes below, choose to reorder either based on the error rate or the duration to get an idea of which routes are causing the most issues.
  2. To learn more about specific routes, click on the route.
  3. The functions view will show you the performance of each route or function, including details about the function, latency, paths, and External APIs. Note that Latency and breakdown by path are only available for [Observability Plus](https://vercel.com/docs/observability/observability-plus) users.
  4. The function view also provides a direct link to the logs for that function, enabling you to pinpoint the cause of the issue.


###  [Available insights](https://vercel.com/docs/observability#available-insights)[](https://vercel.com/docs/observability#available-insights)
Observability provides different sections of features and traffic sources that help you monitor, analyze, and manage your applications either at the team or the project level. The following table shows their availability at each level:
Data source | Team Level | Project Level
---|---|---
[Vercel Functions](https://vercel.com/docs/observability/insights#vercel-functions) | ✓ | ✓
[External APIs](https://vercel.com/docs/observability/insights#external-apis) | ✓ | ✓
[Edge Requests](https://vercel.com/docs/observability/insights#edge-requests) | ✓ | ✓
[Middleware](https://vercel.com/docs/observability/insights#middleware) | ✓ | ✓
[Fast Data Transfer](https://vercel.com/docs/observability/insights#fast-data-transfer) | ✓ | ✓
[Image Optimization](https://vercel.com/docs/observability/insights#image-optimization) | ✓ | ✓
[ISR (Incremental Static Regeneration)](https://vercel.com/docs/observability/insights#isr-incremental-static-regeneration) | ✓ | ✓
[Blob](https://vercel.com/docs/observability/insights#blob) | ✓ |
[Build Diagnostics](https://vercel.com/docs/observability/insights#build-diagnostics) |  | ✓
[AI Gateway](https://vercel.com/docs/observability/insights#ai-gateway) | ✓ | ✓
[Queues](https://vercel.com/docs/observability/insights#queues) |  | ✓
[External Rewrites](https://vercel.com/docs/observability/insights#external-rewrites) | ✓ | ✓
[Microfrontends](https://vercel.com/docs/observability/insights#microfrontends) | ✓ | ✓
