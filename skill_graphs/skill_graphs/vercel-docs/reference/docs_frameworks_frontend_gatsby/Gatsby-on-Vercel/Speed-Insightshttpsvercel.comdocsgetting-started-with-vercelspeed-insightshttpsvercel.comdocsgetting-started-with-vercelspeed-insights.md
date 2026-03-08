##  [Speed Insights](https://vercel.com/docs/getting-started-with-vercel#speed-insights)[](https://vercel.com/docs/getting-started-with-vercel#speed-insights)
[Core Web Vitals](https://vercel.com/docs/speed-insights) are supported for Gatsby v4+ projects with no initial configuration necessary.
When you deploy a Gatsby v4+ site on Vercel, we automatically install the `@vercel/gatsby-plugin-vercel-analytics` package and add it to the `plugins` array in your `gatsby-config.js` file.
We do not recommend installing the Gatsby analytics plugin yourself.
To access your Core Web Vitals data, you must enable Vercel analytics in your project's dashboard. [See our quickstart guide to do so now](https://vercel.com/docs/analytics/quickstart).
To summarize, using Speed Insights with Gatsby on Vercel:
  * Enables you to track traffic performance metrics, such as [First Contentful Paint](https://vercel.com/docs/speed-insights/metrics#first-contentful-paint-fcp), or [First Input Delay](https://vercel.com/docs/speed-insights/metrics#first-input-delay-fid)
  * Enables you to view performance analytics by page name and URL for more granular analysis
  * Shows you [a score for your app's performance](https://vercel.com/docs/speed-insights/metrics#how-the-scores-are-determined) on each recorded metric, which you can use to track improvements or regressions


[Learn more about Speed Insights](https://vercel.com/docs/speed-insights)
