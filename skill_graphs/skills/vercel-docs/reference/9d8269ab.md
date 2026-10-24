##  [Managing your static IPs](https://vercel.com/docs/security#managing-your-static-ips)[](https://vercel.com/docs/security#managing-your-static-ips)
###  [Routing build traffic](https://vercel.com/docs/security#routing-build-traffic)[](https://vercel.com/docs/security#routing-build-traffic)
If your application calls data sources at build time, you can route its build traffic through your static IPs to keep your data sources secure.
To enable this, go to your [project's connectivity settings](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fconnectivity&title=Go+to+Connectivity+Settings):
  1. Go to your project's Settings
  2. Navigate to Connectivity
  3. Toggle Use Static IPs for builds under Static IPs


This setting is disabled by default. When enabled, both your project's build and deployed function traffic will route through static IPs and count as [Private Data Transfer](https://vercel.com/docs/security#pricing).
###  [Routing Middleware support](https://vercel.com/docs/security#routing-middleware-support)[](https://vercel.com/docs/security#routing-middleware-support)
Static IPs (region-specific) don't apply to [middleware](https://vercel.com/docs/routing-middleware) (which are deployed at the [edge](https://vercel.com/docs/glossary#edge)).
###  [Checking usage](https://vercel.com/docs/security#checking-usage)[](https://vercel.com/docs/security#checking-usage)
  1. Go to your Team and click the Usage tab
  2. Scroll down to the Content, Caching & Optimization section. Static IPs data transfer is metered by Private Data Transfer
  3. Click Private Data Transfer for more detail about direction, regions, and projects


###  [Static IPs with deployment environments](https://vercel.com/docs/security#static-ips-with-deployment-environments)[](https://vercel.com/docs/security#static-ips-with-deployment-environments)
When you configure static IPs in a project, they apply to all the [environments](https://vercel.com/docs/deployments/environments) set up in this project.
###  [Regional considerations](https://vercel.com/docs/security#regional-considerations)[](https://vercel.com/docs/security#regional-considerations)
  * Choose regions close to your backend services to reduce latency
  * Each configured region has its own static IP pair
