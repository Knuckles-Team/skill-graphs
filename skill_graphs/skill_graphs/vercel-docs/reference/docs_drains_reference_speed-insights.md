Speed Insights
Speed Insights
# Speed Insights Overview
Last updated February 9, 2026
Speed Insights is available on [all plans](https://vercel.com/docs/plans)
Vercel Speed Insights provides you with a detailed view of your website's performance [metrics](https://vercel.com/docs/speed-insights/metrics), based on [Core Web Vitals](https://vercel.com/docs/speed-insights/metrics#core-web-vitals-explained), enabling you to make data-driven decisions for optimizing your site. For granular visitor data, use [Web Analytics](https://vercel.com/docs/analytics).
The Speed Insights dashboard offers in-depth information about scores and individual metrics without the need for code modifications or leaving the Vercel dashboard.
To get started, follow the quickstart to [enable Speed Insights](https://vercel.com/docs/speed-insights/quickstart) and learn more about the [dashboard view](https://vercel.com/docs/speed-insights#dashboard-view) and [metrics](https://vercel.com/docs/speed-insights/metrics).
When you enable Speed Insights, Vercel tracks data on all deployed environments, including [preview](https://vercel.com/docs/deployments/environments#preview-environment-pre-production) and [production](https://vercel.com/docs/deployments/environments#production-environment) deployments.
##  [Dashboard view](https://vercel.com/docs/speed-insights#dashboard-view)[](https://vercel.com/docs/speed-insights#dashboard-view)
![A snapshot of the Speed Insights tab from the project view.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fspeed-insights%2Fv2%2Fres-chart-light.png&w=3840&q=75)![A snapshot of the Speed Insights tab from the project view.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fspeed-insights%2Fv2%2Fres-chart-dark.png&w=3840&q=75)A snapshot of the Speed Insights tab from the project view.
Once you [enable Speed Insights](https://vercel.com/docs/speed-insights/quickstart), you can access the dashboard by selecting your project in the Vercel [dashboard](https://vercel.com/dashboard), and clicking [Speed Insights](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fspeed-insights&title=Go+to+Speed+Insights) in the sidebar.
The Speed Insights dashboard displays data that you can sort and inspect based on a variety of parameters:
  * Device type: Toggle between mobile and desktop.
  * Environment: Filter by preview, production, or all environments.
  * Time range: Select the timeframe dropdown in the top-right of the page to choose a predefined timeframe. Alternatively, select the Calendar icon to specify a custom timeframe. The [available durations vary](https://vercel.com/docs/speed-insights/limits-and-pricing#reporting-window-for-data-points), depending on the account type.
  * [Performance metric](https://vercel.com/docs/speed-insights/metrics): Switch between parameters that include Real Experience Score (RES), First Contentful Paint (FCP) and Largest Contentful Paint (LCP), and use the views to view more information.
  * Performance metric views: When you select a performance metric, the dashboard displays three views:
    * Time-based line graph that, by default, shows the P75 [percentile of data](https://vercel.com/docs/speed-insights/metrics#how-the-percentages-are-calculated) for the selected metric [data points](https://vercel.com/docs/speed-insights/metrics#understanding-data-points) and time range. You can include P90, P95 and P99 in this view.
    * Kanban board that shows which routes, paths, or HTML elements need improvement (URLs that make up less than 0.5% of visits are not shown by default).
    * Geographical map showing the experience metric by country: ![Geographic map of the P75 score where the color intensity indicates the relative amount of data points per country](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fspeed-insights%2Fv2%2Fcountry-map-light.png&w=3840&q=75)![Geographic map of the P75 score where the color intensity indicates the relative amount of data points per country](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fspeed-insights%2Fv2%2Fcountry-map-dark.png&w=3840&q=75)Geographic map of the P75 score where the color intensity indicates the relative amount of data points per country


The data in the Kanban and map views is selectable so that you can filter by country, route, path and HTML element. The red, orange and green colors in the map view indicate the P75 score.
  * [Quickstart](https://vercel.com/docs/speed-insights/quickstart)
  * [Usage and pricing](https://vercel.com/docs/speed-insights/limits-and-pricing#pricing)
  * [Managing usage & costs](https://vercel.com/docs/speed-insights/managing-usage)
  * [Data points](https://vercel.com/docs/speed-insights/metrics#understanding-data-points)
  * [Metrics](https://vercel.com/docs/speed-insights/metrics)


##  [More resources](https://vercel.com/docs/speed-insights#more-resources)[](https://vercel.com/docs/speed-insights#more-resources)
* * *
[ Previous Notebooks ](https://vercel.com/docs/notebooks)[ Next Getting Started ](https://vercel.com/docs/speed-insights/quickstart)
Was this helpful?
Send
Speed Insights
# Speed Insights Drains Reference
Last updated September 24, 2025
Speed Insights Drains send performance metrics and web vitals from your applications to external endpoints for storage and analysis. To enable Speed Insights Drains, [create a drain](https://vercel.com/docs/drains/using-drains) and choose the Speed Insights data type.
Vercel sends Speed Insights data to endpoint URLs over HTTPS when your application collects performance metrics.
##  [Speed Insights Schema](https://vercel.com/docs/speed-insights#speed-insights-schema)[](https://vercel.com/docs/speed-insights#speed-insights-schema)
The following table describes the possible fields that are sent via Speed Insights Drains:
Name | Type | Description | Example
---|---|---|---
`schema` | string | Schema version identifier | `vercel.speed_insights.v1`
`timestamp` | string | ISO timestamp when the metric was collected | `2023-09-14T15:30:00.000Z`
`projectId` | string | Identifier for the Vercel project | `Qmc52npNy86S8VV4Mt8a8dP1LEkRNbgosW3pBCQytkcgf2`
`ownerId` | string | Identifier for the project owner | `team_nLlpyC6REAqxydlFKbrMDlud`
`deviceId` | number | Unique device identifier | 12345
`metricType` | string | Type of performance metric |  `CLS`, `LCP`, `FID`, `FCP`, `TTFB`, `INP`
`value` | number | Metric value | 0.1
`origin` | string | Origin URL where the metric was collected | `https://example.com`
`path` | string | URL path where the metric was collected | `/dashboard`
`route` | string | Route pattern for the page | `/dashboard/[id]`
`country` | string | Country code of the user | `US`
`region` | string | Region code of the user | `CA`
`city` | string | City of the user | `San Francisco`
`osName` | string | Operating system name | `macOS`
`osVersion` | string | Operating system version | `13.4`
`clientName` | string | Client browser name | `Chrome`
`clientType` | string | Type of client | `browser`
`clientVersion` | string | Client browser version | `114.0.5735.90`
`deviceType` | string | Type of device | `desktop`
`deviceBrand` | string | Device brand | `Apple`
`connectionSpeed` | string | Network connection speed | `4g`
`browserEngine` | string | Browser engine name | `Blink`
`browserEngineVersion` | string | Browser engine version | `114.0.5735.90`
`scriptVersion` | string | Speed Insights script version | `1.0.0`
`sdkVersion` | string | SDK version used to collect metrics | `2.1.0`
`sdkName` | string | SDK name used to collect metrics | `@vercel/speed-insights`
`vercelEnvironment` | string | Vercel environment | `production`
`vercelUrl` | string | Vercel deployment URL | `*.vercel.app`
`deploymentId` | string | Identifier for the Vercel deployment | `dpl_2YZzo1cJAjijSf1hwDFK5ayu2Pid`
`attribution` | string | Attribution information for the metric | `attribution-data`
##  [Format](https://vercel.com/docs/speed-insights#format)[](https://vercel.com/docs/speed-insights#format)
Vercel supports the following formats for Speed Insights Drains. You can configure the format when [configuring the Drain destination](https://vercel.com/docs/drains/using-drains#configure-destination):
###  [JSON](https://vercel.com/docs/speed-insights#json)[](https://vercel.com/docs/speed-insights#json)
Vercel sends Speed Insights data as JSON arrays containing metric objects:
```
[
  { "schema": "vercel.speed_insights.v1", "timestamp": "2023-09-14T15:30:00.000Z", "projectId": "Qmc52npNy86S8VV4Mt8a8dP1LEkRNbgosW3pBCQytkcgf2", "ownerId": "team_nLlpyC6REAqxydlFKbrMDlud", "deviceId": 12345, "metricType": "CLS", "value": 0.1, "origin": "https://example.com", "path": "/dashboard" },
  { "schema": "vercel.speed_insights.v1", "timestamp": "2023-09-14T15:30:05.000Z", "projectId": "Qmc52npNy86S8VV4Mt8a8dP1LEkRNbgosW3pBCQytkcgf2", "ownerId": "team_nLlpyC6REAqxydlFKbrMDlud", "deviceId": 67890, "metricType": "LCP", "value": 2.5, "origin": "https://example.com", "path": "/home" }
]
```

###  [NDJSON](https://vercel.com/docs/speed-insights#ndjson)[](https://vercel.com/docs/speed-insights#ndjson)
Vercel sends Speed Insights data as newline-delimited JSON objects:
```
{"schema": "vercel.speed_insights.v1","timestamp": "2023-09-14T15:30:00.000Z","projectId": "Qmc52npNy86S8VV4Mt8a8dP1LEkRNbgosW3pBCQytkcgf2","ownerId": "team_nLlpyC6REAqxydlFKbrMDlud","deviceId": 12345,"metricType": "CLS","value": 0.1,"origin": "https://example.com","path": "/dashboard"}
{"schema": "vercel.speed_insights.v1","timestamp": "2023-09-14T15:30:05.000Z","projectId": "Qmc52npNy86S8VV4Mt8a8dP1LEkRNbgosW3pBCQytkcgf2","ownerId": "team_nLlpyC6REAqxydlFKbrMDlud","deviceId": 67890,"metricType": "LCP","value": 2.5,"origin": "https://example.com","path": "/home"}
```

##  [Sampling Rate](https://vercel.com/docs/speed-insights#sampling-rate)[](https://vercel.com/docs/speed-insights#sampling-rate)
When you configure a Speed Insights Drain in the Vercel UI, you can set the sampling rate to control the volume of data sent. This helps manage costs when you have high traffic volumes.
##  [More resources](https://vercel.com/docs/speed-insights#more-resources)[](https://vercel.com/docs/speed-insights#more-resources)
For more information on Speed Insights Drains and how to use them, check out the following resources:
  * [Drains overview](https://vercel.com/docs/drains)
  * [Configure Drains](https://vercel.com/docs/drains/using-drains)


* * *
[ Previous Notebooks ](https://vercel.com/docs/notebooks)[ Next Getting Started ](https://vercel.com/docs/speed-insights/quickstart)
Was this helpful?
Send
