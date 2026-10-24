# Regional Pricing
Last updated January 14, 2026
When using Managed Infrastructure resources on Vercel, some, but not all, are priced based on region. The following table shows the price range for resources priced by region. Your team will be charged based on the usage of your projects for each resource per region.
The Included column shows the amount of usage covered in your [billing cycle](https://vercel.com/docs/pricing/understanding-my-invoice#understanding-your-invoice). If you use more than this amount, the Additional column lists the rates for any extra usage as a range.
Active CPU and Provisioned Memory are billed at different rates depending on the region your [fluid compute](https://vercel.com/docs/fluid-compute) is deployed. The rates for each region can be found in the [fluid pricing](https://vercel.com/docs/functions/usage-and-pricing) documentation.
Resource | Included (Billing Cycle) | On-demand (Billing Cycle)
---|---|---
[Fast Data Transfer](https://vercel.com/docs/manage-cdn-usage#fast-data-transfer) | First 1 TB | 1 GB for $0.15 - $0.35
[Edge Requests](https://vercel.com/docs/manage-cdn-usage#edge-requests) | First 10,000,000 | 1,000,000 Requests for $2.00 - $3.20
Resource | On-demand (Billing Cycle)
---|---
[ISR Writes](https://vercel.com/docs/incremental-static-regeneration/limits-and-pricing#isr-writes-chart) | 1,000,000 Write Units for $4.00 - $6.40
[ISR Reads](https://vercel.com/docs/incremental-static-regeneration/limits-and-pricing#isr-reads-chart) | 1,000,000 Read Units for $0.40 - $0.64
[Fast Origin Transfer](https://vercel.com/docs/manage-cdn-usage#fast-origin-transfer) | 1 GB for $0.06 - $0.43
[Queue API Operations](https://vercel.com/docs/queues/pricing) | 1,000,000 Operations for $0.60 - $0.96
[Edge Request Additional CPU Duration](https://vercel.com/docs/manage-cdn-usage#edge-request-cpu-duration) | 1 Hour for $0.30 - $0.48
[Image Optimization Transformations](https://vercel.com/docs/image-optimization/limits-and-pricing#image-transformations) | $0.05 - $0.0812 per 1K
[Image Optimization Cache Reads](https://vercel.com/docs/image-optimization/limits-and-pricing#image-cache-reads) | $0.40 - $0.64 per 1M
[Image Optimization Cache Writes](https://vercel.com/docs/image-optimization/limits-and-pricing#image-cache-writes) | $4.00 - $6.40 per 1M
[Runtime Cache Writes](https://vercel.com/docs/functions/functions-api-reference/vercel-functions-package#getcache) | 1,000,000 Write Units for $4.00 - $6.40
[Runtime Cache Reads](https://vercel.com/docs/functions/functions-api-reference/vercel-functions-package#getcache) | 1,000,000 Read Units for $0.40 - $0.64
[WAF Rate Limiting](https://vercel.com/docs/security/vercel-waf/usage-and-pricing#rate-limiting-pricing) | 1,000,000 Allowed Requests for $0.50 - $0.80
[OWASP CRS per request number](https://vercel.com/docs/security/vercel-waf/usage-and-pricing#managed-ruleset-pricing) | 1,000,000 Inspected Requests for $0.80 - $1.28
[OWASP CRS per request size](https://vercel.com/docs/security/vercel-waf/usage-and-pricing#managed-ruleset-pricing) | 1 GB of inspected request payload for $0.20 - $0.32
[Blob Storage Size](https://vercel.com/docs/vercel-blob/usage-and-pricing#pricing) | 1 GB for $0.023 - $0.041
[Blob Simple Operations](https://vercel.com/docs/vercel-blob/usage-and-pricing#pricing) | 1,000,000 for $0.35 - $0.56
[Blob Advanced Operations](https://vercel.com/docs/vercel-blob/usage-and-pricing#pricing) | 1,000,000 for $4.50 - $7.00
[Blob Data Transfer](https://vercel.com/docs/vercel-blob/usage-and-pricing#pricing) | 1 GB for $0.05 - $0.117
[Private Data Transfer](https://vercel.com/docs/connectivity/static-ips) | 1 GB for $0.15 - $0.31
