# Project-Level Routing Rules
Last updated March 8, 2026
Project-level routing rules let you add redirects, rewrites, response headers, and other routing logic from the dashboard, API, or CLI, without deploying new code. Changes take effect immediately after publishing.
These rules are separate from deployment-level routes defined in `vercel.json` or your framework configuration. They run at the CDN level on every request, after [bulk redirects](https://vercel.com/docs/routing/redirects/bulk-redirects) and before your deployment's own routes. See the [routing order](https://vercel.com/docs/routing#routing-order) for the full sequence.
