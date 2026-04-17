##  [Visualize](https://vercel.com/docs/logs#visualize)[](https://vercel.com/docs/logs#visualize)
The `Visualize` clause selects what query data is displayed. You can select one of the following fields at a time, [aggregating](https://vercel.com/docs/logs#aggregations) each field in one of several ways:
Field Name | Description | Aggregations
---|---|---
Edge Requests | The number of [Edge Requests](https://vercel.com/docs/manage-cdn-usage#edge-requests) | Count, Count per Second, Percentages
Duration | The time spent serving a request, as measured by Vercel's CDN | Sum, Sum per Second, Min/Max, Percentages, Percentiles
Incoming Fast Data Transfer | The amount of [Fast Data Transfer](https://vercel.com/docs/manage-cdn-usage#fast-data-transfer) used by the request. | Sum, Sum per Second, Min/Max, Percentages, Percentiles
Outgoing Fast Data Transfer | The amount of [Fast Data Transfer](https://vercel.com/docs/manage-cdn-usage#fast-data-transfer) used by the response. | Sum, Sum per Second, Min/Max, Percentages, Percentiles
Function Duration | The amount of [Vercel Function duration](https://vercel.com/docs/fluid-compute#pricing-and-usage), as measured in GB-hours. | Sum, Sum per Second, Min/Max, Percentages, Percentiles
Function Invocations | The number of [Vercel Function invocations](https://vercel.com/docs/functions/usage-and-pricing#managing-function-invocations) | Count, Count per Second, Percentages
Function Duration | The amount of [Vercel Function duration](https://vercel.com/docs/functions/usage-and-pricing#managing-function-duration), as measured in GB-hours. | Sum, Sum per Second, Min/Max, Percentages, Percentiles
Function CPU Time | The amount of CPU time a Vercel Function has spent responding to requests, as measured in milliseconds. | Sum, Sum per Second, Min/Max, Percentages, Percentiles
Incoming Fast Origin Transfer | The amount of [Fast Origin Transfer](https://vercel.com/docs/manage-cdn-usage#fast-origin-transfer) used by the request. | Sum, Sum per Second, Min/Max, Percentages, Percentiles
Outgoing Fast Origin Transfer | The amount of [Fast Origin Transfer](https://vercel.com/docs/manage-cdn-usage#fast-origin-transfer) used by the response. | Sum, Sum per Second, Min/Max, Percentages, Percentiles
Provisioned Memory | The amount of memory provisioned to a Vercel Function. | Sum, Sum per Second, Min/Max, Percentages, Percentiles
Peak Memory | The maximum amount of memory used by Vercel Function at any point in time. | Sum, Sum per Second, Min/Max, Percentages, Percentiles
Requests Blocked | All requests blocked by either the system or user. | Count, Count per Second, Percentages
Incoming Legacy Bandwidth | Legacy Bandwidth sent from the client to Vercel | Sum, Sum per Second, Min/Max, Percentages, Percentiles
Outgoing Legacy Bandwidth | Legacy Bandwidth sent from Vercel to the client | Sum, Sum per Second, Min/Max, Percentages, Percentiles
Total Legacy Bandwidth | Sum of Incoming and Outgoing Legacy Bandwidth | Sum, Sum per Second, Min/Max, Percentages, Percentiles
###  [Aggregations](https://vercel.com/docs/logs#aggregations)[](https://vercel.com/docs/logs#aggregations)
The visualize field can be aggregated in the following ways:
Aggregation | Description
---|---
Count | The number of requests that occurred
Count per Second | The average rate of requests that occurred
Sum | The sum of the field value across all requests
Sum per Second | The sum of the field value as a rate per second
Minimum | The smallest observed field value
Maximum | The largest observed field value
Percentiles (75th, 90th, 95th, 99th) | Percentiles for the field values. For example, 90% of requests will have a duration that is less than the 90th percentile of duration.
Percentages | Each group is reported as a percentage of the ungrouped whole. For example, if a query for request groups by hosts, one host may have 10% of the total request count. Anything excluded by the `where` clause is not counted towards the ungrouped whole.
Aggregations are calculated within each point on the chart (hourly, daily, etc depending on the selected granularity) and also across the entire query window
