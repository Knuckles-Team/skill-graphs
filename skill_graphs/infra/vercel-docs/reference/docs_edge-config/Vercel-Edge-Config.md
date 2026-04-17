# Vercel Edge Config
Last updated January 24, 2026
Edge Config is available on [all plans](https://vercel.com/docs/plans)
An [Edge Config](https://vercel.com/edge-config) is a global data store that [enables experimentation with feature flags, A/B testing, critical redirects, and IP blocking](https://vercel.com/docs/edge-config#use-cases). It enables you to read data in the region closest to the user without querying an external database or hitting upstream servers.
With Vercel's optimizations, you can read Edge Config data at negligible latency. The vast majority of your reads will complete within 15ms [at P99](https://vercel.com/docs/speed-insights/metrics#how-the-percentages-are-calculated), or often less than 1ms.
You can use an Edge Config in [Middleware](https://vercel.com/docs/routing-middleware) and [Vercel Functions](https://vercel.com/docs/functions).
Vercel's Edge Config read optimizations are only available on the Edge and Node.js runtimes. Optimizations can be enabled for other runtimes, [such as Ruby, Go, and Python](https://vercel.com/docs/functions/runtimes) upon request. See [our Edge Config limits docs](https://vercel.com/docs/edge-config/edge-config-limits) to learn more.
