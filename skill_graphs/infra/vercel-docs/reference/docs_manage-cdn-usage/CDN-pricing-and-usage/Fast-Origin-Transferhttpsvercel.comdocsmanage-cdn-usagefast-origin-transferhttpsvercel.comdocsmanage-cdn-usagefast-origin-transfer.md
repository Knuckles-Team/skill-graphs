##  [Fast Origin Transfer](https://vercel.com/docs/manage-cdn-usage#fast-origin-transfer)[](https://vercel.com/docs/manage-cdn-usage#fast-origin-transfer)
Fast Origin Transfer is incurred when using any of Vercel's compute products. These include Vercel Functions, Middleware, and the Data Cache (used through ISR).
Select a Region
Cape Town, South Africa (cpt1) Cleveland, USA (cle1) Dubai, UAE (dxb1) Dublin, Ireland (dub1) Frankfurt, Germany (fra1) Hong Kong (hkg1) London, UK (lhr1) Montréal, Canada (yul1) Mumbai, India (bom1) Osaka, Japan (kix1) Paris, France (cdg1) Portland, USA (pdx1) San Francisco, USA (sfo1) São Paulo, Brazil (gru1) Seoul, South Korea (icn1) Singapore (sin1) Stockholm, Sweden (arn1) Sydney, Australia (syd1) Tokyo, Japan (hnd1) Washington, D.C., USA (iad1)
Managed Infrastructure pricing Resource | Hobby Included | On-demand Rates
---|---|---
Resource | Hobby Included | On-demand Rates
[Fast Origin Transfer](https://vercel.com/docs/pricing/regional-pricing) | First 10 GB | $0.06 per 1 GB
###  [Calculating Fast Origin Transfer](https://vercel.com/docs/manage-cdn-usage#calculating-fast-origin-transfer)[](https://vercel.com/docs/manage-cdn-usage#calculating-fast-origin-transfer)
Usage is incurred on both the input and output data transfer when using compute on Vercel. For example:
  * Incoming: The number of bytes sent as part of the
    * For common `GET` requests, the incoming bytes are normally inconsequential (less than 1KB for a normal request).
    * For `POST` requests, like a file upload API, the incoming bytes would include the entire uploaded file.
  * Outgoing: The number of bytes sent as the


###  [Optimizing Fast Origin Transfer](https://vercel.com/docs/manage-cdn-usage#optimizing-fast-origin-transfer)[](https://vercel.com/docs/manage-cdn-usage#optimizing-fast-origin-transfer)
####  [Functions](https://vercel.com/docs/manage-cdn-usage#functions)[](https://vercel.com/docs/manage-cdn-usage#functions)
When using Incremental Static Regeneration (ISR) on Vercel, a Vercel Function is used to generate the static page. This optimization section applies for both server-rendered function usage, as well as usage for ISR. ISR usage on Vercel is billed under the Vercel Data Cache.
If using Vercel Functions, you can optimize Fast Origin Transfer by reducing the size of the response. Ensure your Function is only responding with relevant data (no extraneous API fields).
You can also add [caching headers](https://vercel.com/docs/cdn-cache) to the function response. By caching the response, future requests serve from the CDN cache, rather than invoking the function again. This reduces Fast Origin Transfer usage and improves performance.
Ensure your Function supports `If-Modified-Since` or `Etag` to prevent duplicate data transmission (
####  [Middleware](https://vercel.com/docs/manage-cdn-usage#middleware)[](https://vercel.com/docs/manage-cdn-usage#middleware)
If using Middleware, it is possible to accrue Fast Origin Transfer twice for a single Function request. To prevent this, you want to only run Middleware when necessary. For example, Next.js allows you to set a
####  [Investigating usage](https://vercel.com/docs/manage-cdn-usage#investigating-usage)[](https://vercel.com/docs/manage-cdn-usage#investigating-usage)
  * Look at the Fast Origin Transfer section of the Usage page:
    * Observe incoming vs outgoing usage. Reference the list above for optimization tips.
    * Observe the breakdown by project.
    * Observe the breakdown by region (Fast Origin Transfer is [priced regionally](https://vercel.com/docs/manage-cdn-usage#fast-origin-transfer))
  * If optimizing Outgoing Fast Origin Transfer:
    * Observe the breakdown by project to identify which projects contribute most
    * Filter by invocations to see which specific compute is being accessed most
