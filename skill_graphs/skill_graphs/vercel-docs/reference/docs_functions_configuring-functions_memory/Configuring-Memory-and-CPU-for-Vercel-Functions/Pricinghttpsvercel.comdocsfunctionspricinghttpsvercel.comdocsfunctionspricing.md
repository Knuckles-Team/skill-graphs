##  [Pricing](https://vercel.com/docs/functions#pricing)[](https://vercel.com/docs/functions#pricing)
While memory / CPU size is not an explicitly billed metric, it is fundamental in how the billed metric of [Function Duration](https://vercel.com/docs/functions/usage-and-pricing#managing-function-duration) is calculated.
Legacy Billing Model: This describes the legacy Function duration billing model based on wall-clock time. For new projects, we recommend [Fluid Compute](https://vercel.com/docs/functions/usage-and-pricing) which bills separately for active CPU time and provisioned memory time for more cost-effective and transparent pricing.
You are charged based on the duration your Vercel functions have run. This is sometimes called "wall-clock time", which refers to the _actual time_ elapsed during a process, similar to how you would measure time passing on a wall clock. It includes all time spent from start to finish of the process, regardless of whether that time was actively used for processing or spent waiting for a streamed response. Function Duration is calculated in GB-Hours, which is the memory allocated for each Function in GB x the time in hours they were running.
For example, if a function [has](https://vercel.com/docs/functions/configuring-functions/memory) 1.7 GB (1769 MB) of memory and is executed 1 million times at a 1-second duration:
  * Total Seconds: 1M * (1s) = 1,000,000 Seconds
  * Total GB-Seconds: 1769/1024 GB * 1,000,000 Seconds = 1,727,539.06 GB-Seconds
  * Total GB-Hrs: 1,727,539.06 GB-Seconds / 3600 = 479.87 GB-Hrs
  * The total Vercel Function Execution is 479.87 GB-Hrs.


To see your current usage, open Usage in the sidebar on your team's [Dashboard](https://vercel.com/dashboard) and go to Functions > Duration. You can use the Ratio option to see the total amount of execution time across all projects within your team, including the completions, errors, and timeouts.
You can also view [Invocations](https://vercel.com/docs/functions/usage-and-pricing#managing-function-invocations) to see the number of times your Functions have been invoked. To learn more about the cost of Vercel Functions, see [Vercel Function Pricing](https://vercel.com/docs/pricing/serverless-functions).
* * *
[ Previous Fluid Compute ](https://vercel.com/docs/fluid-compute)[ Next Getting Started ](https://vercel.com/docs/functions/quickstart)
Was this helpful?
Send
Next.js (/app)
Choose a framework to optimize documentation to:
  * Next.js (/app)
  * Next.js (/pages)
  * Other frameworks


On this page
  * [Memory configuration considerations](https://vercel.com/docs/functions#memory-configuration-considerations)
  * [Setting your default function memory / CPU size](https://vercel.com/docs/functions#setting-your-default-function-memory-/-cpu-size)
  * [Memory / CPU type](https://vercel.com/docs/functions#memory-/-cpu-type)
  * [Viewing your function memory size](https://vercel.com/docs/functions#viewing-your-function-memory-size)
  * [Memory limits](https://vercel.com/docs/functions#memory-limits)
  * [Pricing](https://vercel.com/docs/functions#pricing)


Copy as MarkdownGive feedbackAsk AI about this page
