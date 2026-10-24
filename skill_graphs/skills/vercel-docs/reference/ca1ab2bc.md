##  [Vercel features support](https://vercel.com/docs/functions/runtimes#vercel-features-support)[](https://vercel.com/docs/functions/runtimes#vercel-features-support)
The following features are supported by Vercel Functions:
###  [Secure Compute](https://vercel.com/docs/functions/runtimes#secure-compute)[](https://vercel.com/docs/functions/runtimes#secure-compute)
Vercel's [Secure Compute](https://vercel.com/docs/secure-compute) feature offers enhanced security for your Vercel Functions, including dedicated IP addresses and VPN options. This can be particularly important for functions that handle sensitive data.
###  [Streaming](https://vercel.com/docs/functions/runtimes#streaming)[](https://vercel.com/docs/functions/runtimes#streaming)
Streaming refers to the ability to send or receive data in a continuous flow.
The Node.js runtime supports streaming by default. Streaming is also supported when using the [Python runtime](https://vercel.com/docs/functions/streaming-functions#streaming-python-functions).
Vercel Functions have a [maximum duration](https://vercel.com/docs/functions/configuring-functions/duration), meaning that it isn't possible to stream indefinitely.
Node.js and Edge runtime streaming functions support the [`waitUntil` method](https://vercel.com/docs/functions/functions-api-reference/vercel-functions-package#waituntil), which allows for an asynchronous task to be performed during the lifecycle of the request. This means that while your function will likely run for the same amount of time, your end-users can have a better, more interactive experience.
###  [Cron jobs](https://vercel.com/docs/functions/runtimes#cron-jobs)[](https://vercel.com/docs/functions/runtimes#cron-jobs)
[Cron jobs](https://vercel.com/docs/cron-jobs) are time-based scheduling tools used to automate repetitive tasks. When a cron job is triggered through the [cron expression](https://vercel.com/docs/cron-jobs#cron-expressions), it calls a Vercel Function.
###  [Vercel Storage](https://vercel.com/docs/functions/runtimes#vercel-storage)[](https://vercel.com/docs/functions/runtimes#vercel-storage)
From your function, you can communicate with a choice of [data stores](https://vercel.com/docs/storage). To ensure low-latency responses, it's crucial to have compute close to your databases. Always deploy your databases in regions closest to your functions to avoid long network roundtrips. For more information, see our [best practices](https://vercel.com/docs/storage#locate-your-data-close-to-your-functions) documentation.
###  [Edge Config](https://vercel.com/docs/functions/runtimes#edge-config)[](https://vercel.com/docs/functions/runtimes#edge-config)
An [Edge Config](https://vercel.com/docs/edge-config) is a global data store that enables experimentation with feature flags, A/B testing, critical redirects, and IP blocking. It enables you to read data at the edge without querying an external database or hitting upstream servers.
###  [Tracing](https://vercel.com/docs/functions/runtimes#tracing)[](https://vercel.com/docs/functions/runtimes#tracing)
Vercel supports [Tracing](https://vercel.com/docs/tracing) that allows you to send OpenTelemetry traces from your Vercel Functions to any application performance monitoring (APM) vendors.
* * *
[ Previous Streaming ](https://vercel.com/docs/functions/streaming-functions)[ Next Node.js ](https://vercel.com/docs/functions/runtimes/node-js)
Was this helpful?
Send
On this page
  * [Official runtimes](https://vercel.com/docs/functions/runtimes#official-runtimes)
  * [Community runtimes](https://vercel.com/docs/functions/runtimes#community-runtimes)
  * [Features](https://vercel.com/docs/functions/runtimes#features)
  * [Location](https://vercel.com/docs/functions/runtimes#location)
  * [Failover mode](https://vercel.com/docs/functions/runtimes#failover-mode)
  * [Isolation boundary](https://vercel.com/docs/functions/runtimes#isolation-boundary)
  * [File system support](https://vercel.com/docs/functions/runtimes#file-system-support)
  * [Archiving](https://vercel.com/docs/functions/runtimes#archiving)
  * [Functions created per deployment](https://vercel.com/docs/functions/runtimes#functions-created-per-deployment)
  * [Caching data](https://vercel.com/docs/functions/runtimes#caching-data)
  * [Environment variables](https://vercel.com/docs/functions/runtimes#environment-variables)
  * [Vercel features support](https://vercel.com/docs/functions/runtimes#vercel-features-support)
  * [Secure Compute](https://vercel.com/docs/functions/runtimes#secure-compute)
  * [Streaming](https://vercel.com/docs/functions/runtimes#streaming)
  * [Cron jobs](https://vercel.com/docs/functions/runtimes#cron-jobs)
  * [Vercel Storage](https://vercel.com/docs/functions/runtimes#vercel-storage)
  * [Edge Config](https://vercel.com/docs/functions/runtimes#edge-config)
  * [Tracing](https://vercel.com/docs/functions/runtimes#tracing)


Copy as MarkdownGive feedbackAsk AI about this page
[Functions](https://vercel.com/docs/functions)
Runtimes
