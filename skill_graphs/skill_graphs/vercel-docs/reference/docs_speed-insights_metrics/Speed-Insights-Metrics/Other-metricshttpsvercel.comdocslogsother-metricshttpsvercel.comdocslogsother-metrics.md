##  [Other metrics](https://vercel.com/docs/logs#other-metrics)[](https://vercel.com/docs/logs#other-metrics)
###  [Time to First Byte (TTFB)](https://vercel.com/docs/logs#time-to-first-byte-ttfb)[](https://vercel.com/docs/logs#time-to-first-byte-ttfb)
Time to First Byte (TTFB) measures the time between the request for a resource and when the first byte of a response begins to arrive.
Lower TTFB times are better, with a good TTFB time being considered as under 800 milliseconds.
###  [First Input Delay (FID)](https://vercel.com/docs/logs#first-input-delay-fid)[](https://vercel.com/docs/logs#first-input-delay-fid)
A good FID score is 100 milliseconds or less.
As
###  [Total Blocking Time (TBT)](https://vercel.com/docs/logs#total-blocking-time-tbt)[](https://vercel.com/docs/logs#total-blocking-time-tbt)
Total Blocking Time (TBT) quantifies how non-interactive a page is. It measures the total time between the First Contentful Paint (FCP) and Time to Interactive (TTI) where the main thread was blocked for long enough to prevent user input. Long tasks (over 50 ms) block the main thread, preventing the user from interacting with the page. The sum of the time portions exceeding 50 ms constitutes the TBT.
Lower TBT times are better, with a good TBT time being considered as under 800 milliseconds.
For more in-depth information related to performance metrics, visit the PageSpeed Insights
