##  [Global infrastructure](https://vercel.com/docs/regions#global-infrastructure)[](https://vercel.com/docs/regions#global-infrastructure)
Vercel's CDN is built on a sophisticated global infrastructure designed to optimize performance and reliability:
  * Points of Presence (PoPs): We operate over 126 PoPs distributed across the globe. These PoPs serve as the first point of contact for incoming requests, ensuring low-latency access for users worldwide.
  * Vercel Regions: Behind these PoPs, we maintain 20 compute-capable regions where your code can run close to your data.
  * Private Network: Traffic flows from PoPs to the nearest region through private, low-latency connections, ensuring fast and efficient data transfer.


This architecture balances the benefits of widespread geographical distribution with the efficiency of concentrated caching and compute resources.
###  [Caching strategy](https://vercel.com/docs/regions#caching-strategy)[](https://vercel.com/docs/regions#caching-strategy)
Our approach to caching is designed to maximize efficiency and performance:
  * By maintaining fewer, dense regions, we increase cache hit probability. This means that popular content is more likely to be available in each region's cache.
  * The extensive PoP network ensures that users can quickly access regional caches, minimizing latency.
  * This concentrated caching strategy results in higher cache hit ratios, reducing the need for requests to go back to the origin server and significantly improving response times.
