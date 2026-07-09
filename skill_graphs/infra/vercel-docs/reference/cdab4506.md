##  [Understanding data points](https://vercel.com/docs/logs#understanding-data-points)[](https://vercel.com/docs/logs#understanding-data-points)
In the context of Vercel's Speed Insights, a data point is a single unit of information that represents a measurement of a specific Web Vital metric during a user's visit to your website.
Data points are collected on hard navigations, which in the case of Next.js apps, are only the first-page view in a session. During a user's visit, data points are gathered during the initial page load, user interaction, and upon leaving the page.
As of now, up to 6 data points can be potentially tracked per visit:
  * On page load: Time to First Byte ([TTFB](https://vercel.com/docs/logs#time-to-first-byte-ttfb)) and First Contentful Paint ([FCP](https://vercel.com/docs/logs#first-contentful-paint-fcp))
  * On interaction: First Input Delay ([FID](https://vercel.com/docs/logs#first-input-delay-fid)) and Largest Contentful Paint ([LCP](https://vercel.com/docs/logs#largest-contentful-paint-lcp))
  * On leave: Interaction to Next Paint ([INP](https://vercel.com/docs/logs#interaction-to-next-paint-inp)), Cumulative Layout Shift ([CLS](https://vercel.com/docs/logs#cumulative-layout-shift-cls)), and, if not already sent, Largest Contentful Paint ([LCP](https://vercel.com/docs/logs#largest-contentful-paint-lcp)).


The collection of metrics may vary depending on how users interact with or exit the page. On average, you can expect to collect between 3 and 6 metrics per visit.
These data points provide insights into various performance aspects of your website, such as the time it takes to display the first content ([FCP](https://vercel.com/docs/logs#first-contentful-paint-fcp)) and the delay between user input and response ([FID](https://vercel.com/docs/logs#first-input-delay-fid)). By analyzing these data points, you can gain valuable information to optimize and enhance the performance of your website.
###  [How the percentages are calculated?](https://vercel.com/docs/logs#how-the-percentages-are-calculated)[](https://vercel.com/docs/logs#how-the-percentages-are-calculated)
By default, the user experience percentile is set to P75, which offers a balanced overview of the majority of user experiences. You can view the data for the other percentiles by selecting them in the time-based line graph.
The chosen percentile corresponds to the proportion of users who experience a load time faster than a specific value. Here's how each percentile is defined:
  * P75: Represents the experience of the fastest 75% of your users, excluding the slowest 25%.
  * P90: Represents the experience of the fastest 90% of your users, excluding the slowest 10%.
  * P95: Represents the experience of the fastest 95% of your users, excluding the slowest 5%.
  * P99: Represents the experience of the fastest 99% of your users, excluding the slowest 1%.


For instance, a P75 score of 1 second for [First Contentful Paint (FCP)](https://vercel.com/docs/logs#first-contentful-paint-fcp) means that 75% of your users experience an FCP faster than 1 second. Similarly, a P99 score of 8 seconds means 99% of your users experience an FCP faster than 8 seconds.
