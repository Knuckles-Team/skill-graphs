##  [Core Web Vitals explained](https://vercel.com/docs/logs#core-web-vitals-explained)[](https://vercel.com/docs/logs#core-web-vitals-explained)
The Core Web Vitals, as defined by Google and the
Speed Insights now uses Lighthouse 10 scoring criteria instead of Lighthouse 6 criteria as explained in [Updated Scoring Criteria](https://vercel.com/docs/speed-insights/migrating-from-legacy#updated-scoring-criteria)
Metric | Description | Target Value
---|---|---
[Largest Contentful Paint (LCP)](https://vercel.com/docs/logs#largest-contentful-paint-lcp) | Measures the time from page start to when the largest content element is fully visible. | 2.5 seconds or less
[Cumulative Layout Shift (CLS)](https://vercel.com/docs/logs#cumulative-layout-shift-cls) | Quantifies the fraction of layout shift experienced by the user over the lifespan of the page. | 0.1 or less
[Interaction to Next Paint (INP)](https://vercel.com/docs/logs#interaction-to-next-paint-inp) | Measures the time from user interaction to when the browser renders the next frame. | 200 milliseconds or less
[First Contentful Paint (FCP)](https://vercel.com/docs/logs#first-contentful-paint-fcp) | Measures the time from page start to the rendering of the first piece of DOM content. | 1.8 seconds or less
[First Input Delay (FID)](https://vercel.com/docs/logs#first-input-delay-fid) | Measures the time from a user's first interaction to the time the browser is able to respond. | 100 milliseconds or less
[Total Blocking Time (TBT)](https://vercel.com/docs/logs#total-blocking-time-tbt) | Measures the total amount of time between FCP and TTI where the main thread was blocked long enough to prevent input responsiveness. | Under 800 milliseconds
[Time to First Byte (TTFB)](https://vercel.com/docs/logs#time-to-first-byte-ttfb) | Measures the time from the request of a resource to when the first byte of a response begins to arrive. | Under 800 milliseconds
###  [Largest Contentful Paint (LCP)](https://vercel.com/docs/logs#largest-contentful-paint-lcp)[](https://vercel.com/docs/logs#largest-contentful-paint-lcp)
A good LCP time is considered to be 2.5 seconds or less.
###  [Cumulative Layout Shift (CLS)](https://vercel.com/docs/logs#cumulative-layout-shift-cls)[](https://vercel.com/docs/logs#cumulative-layout-shift-cls)
The score is calculated from the product of two measures:
  * The impact fraction - the area of the viewport impacted by the shift
  * The distance fraction - the distance the elements have moved relative to the viewport between frames


A good CLS score is considered to be 0.1 or less.
###  [Interaction to Next Paint (INP)](https://vercel.com/docs/logs#interaction-to-next-paint-inp)[](https://vercel.com/docs/logs#interaction-to-next-paint-inp)
This metric is used to gauge the responsiveness of a page to user interactions. The quicker the page responds to user input, the better the INP.
Lower INP times are better, with an INP time of 200 milliseconds or less being considered good.
###  [First Contentful Paint (FCP)](https://vercel.com/docs/logs#first-contentful-paint-fcp)[](https://vercel.com/docs/logs#first-contentful-paint-fcp)
Lower FCP times are better, with an FCP time of 1.8 seconds or less being considered good.
