##  [Observability](https://vercel.com/docs/getting-started-with-vercel#observability)[](https://vercel.com/docs/getting-started-with-vercel#observability)
With [Vercel Observability](https://vercel.com/docs/observability), you can view detailed performance insights broken down by route and monitor function execution performance. This can help you identify bottlenecks and optimization opportunities.
Nitro (>=2.12) generates routing hints for [functions observability insights](https://vercel.com/docs/observability/insights#vercel-functions), providing a detailed view of performance broken down by route.
To enable this feature, ensure you are using a compatibility date of `2025-07-15` or later.
Framework integrations can use the `ssrRoutes` configuration to declare SSR routes. For more information, see
