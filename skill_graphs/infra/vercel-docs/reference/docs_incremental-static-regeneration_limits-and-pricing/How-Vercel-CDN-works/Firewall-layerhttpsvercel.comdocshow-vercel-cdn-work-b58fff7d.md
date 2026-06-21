##  [Firewall layer](https://vercel.com/docs/how-vercel-cdn-works#firewall-layer)[](https://vercel.com/docs/how-vercel-cdn-works#firewall-layer)
The [Vercel Firewall](https://vercel.com/docs/cdn-security) inspects every request before it reaches your application. It operates in three layers:
  * [Platform-wide firewall](https://vercel.com/docs/cdn-security#platform-wide-firewall): DDoS mitigation and protection against low-quality traffic, active for all customers at no cost.
  * [Web Application Firewall (WAF)](https://vercel.com/docs/vercel-firewall/vercel-waf): Custom rules to block or challenge requests based on IP, path, headers, geographic location, and more.
  * [Bot management](https://vercel.com/docs/bot-management): Detect and manage automated traffic with configurable policies.


Blocked requests never reach the routing or caching layers.
