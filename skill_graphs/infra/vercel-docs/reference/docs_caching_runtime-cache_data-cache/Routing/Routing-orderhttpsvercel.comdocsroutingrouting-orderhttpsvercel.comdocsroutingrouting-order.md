##  [Routing order](https://vercel.com/docs/routing#routing-order)[](https://vercel.com/docs/routing#routing-order)
Requests flow through multiple routing layers in a fixed order. Each layer can modify, redirect, or terminate the request before it reaches the next step.
### Routing Order
Requests flow through these features in order. Each feature can modify or block the request before it reaches the next step.
[Firewall](https://vercel.com/docs/security/vercel-firewall)
Blocks malicious traffic and enforces security rules
[Microfrontends](https://vercel.com/docs/microfrontends)
Routes between multiple applications on the same domain
[Skew Protection](https://vercel.com/docs/deployments/skew-protection)
Ensures client and server versions match
[Rolling Releases](https://vercel.com/docs/rolling-releases)
Gradually routes traffic to new deployments
[Bulk Redirects](https://vercel.com/docs/routing/redirects/bulk-redirects)
Applies bulk redirects configured at the project level
[Project Routes](https://vercel.com/docs/routing/project-routing-rules)
Applies routing rules configured from the dashboard or API
[Deployment Routes](https://vercel.com/docs/project-configuration)
Applies all routes defined in your deployment configuration
Headers + Redirects
From vercel.json or next.config.js
Middleware
Runs custom logic on each request
File System Routes
Pages and API routes from your codebase
Rewrites
URL path transformations
Project Routes are [project-level routing rules](https://vercel.com/docs/routing/project-routing-rules) you configure from the dashboard or API. They run after bulk redirects and before your deployment's own routes. This means you can add, change, or remove rules without deploying new code.
