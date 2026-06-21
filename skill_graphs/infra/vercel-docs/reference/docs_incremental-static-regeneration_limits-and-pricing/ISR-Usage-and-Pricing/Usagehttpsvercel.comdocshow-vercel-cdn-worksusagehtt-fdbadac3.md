##  [Usage](https://vercel.com/docs/how-vercel-cdn-works#usage)[](https://vercel.com/docs/how-vercel-cdn-works#usage)
The table below shows the metrics for the [ISR](https://vercel.com/docs/pricing/incremental-static-regeneration) section of the [Usage dashboard](https://vercel.com/docs/pricing/manage-and-optimize-usage#viewing-usage).
To view information on managing each resource, select the resource link in the Metric column. To jump straight to guidance on optimization, select the corresponding resource link in the Optimize column. The cost for each metric is based on the request location. See the [pricing section](https://vercel.com/docs/incremental-static-regeneration/limits-and-pricing#pricing) and choose the region from the dropdown for specific information.
Manage and Optimize pricing Metric | Description | Priced | Optimize
---|---|---|---
[Reads](https://vercel.com/docs/incremental-static-regeneration/limits-and-pricing#isr-reads-chart) | The total amount of Read Units used to access ISR data | [Yes](https://vercel.com/docs/pricing/regional-pricing) | [Learn More](https://vercel.com/docs/incremental-static-regeneration/limits-and-pricing#optimizing-isr-reads-and-writes)
[Writes](https://vercel.com/docs/incremental-static-regeneration/limits-and-pricing#isr-writes-chart) | The total amount of Write Units used to store new ISR data | [Yes](https://vercel.com/docs/pricing/regional-pricing) | [Learn More](https://vercel.com/docs/incremental-static-regeneration/limits-and-pricing#optimizing-isr-reads-and-writes)
###  [Storage](https://vercel.com/docs/how-vercel-cdn-works#storage)[](https://vercel.com/docs/how-vercel-cdn-works#storage)
There is no limit on storage for ISR. All the data you write remains cached for the duration you specify. Only you or your team can invalidate this cache, unless it goes unaccessed for 31 days.
###  [Written data](https://vercel.com/docs/how-vercel-cdn-works#written-data)[](https://vercel.com/docs/how-vercel-cdn-works#written-data)
The total amount of Write Units used to durably store new ISR data, measured in 8 KB units.
###  [Read data](https://vercel.com/docs/how-vercel-cdn-works#read-data)[](https://vercel.com/docs/how-vercel-cdn-works#read-data)
The total amount of Read Units used to access ISR data, measured in 8 KB units.
ISR reads and writes are measured in 8 KB units:
  * Read unit: One read unit equals 8 KB of data read from the ISR cache
  * Write unit: One write unit equals 8 KB of data written to the ISR cache
