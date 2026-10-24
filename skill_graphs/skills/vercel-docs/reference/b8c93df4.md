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
