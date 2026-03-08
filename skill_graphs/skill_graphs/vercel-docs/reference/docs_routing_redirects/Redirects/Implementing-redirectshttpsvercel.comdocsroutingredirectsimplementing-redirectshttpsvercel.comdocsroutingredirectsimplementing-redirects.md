##  [Implementing redirects](https://vercel.com/docs/routing/redirects#implementing-redirects)[](https://vercel.com/docs/routing/redirects#implementing-redirects)
Review the table below to understand which redirect method best fits your use case:
Redirect method | Use case | Definition location
---|---|---
[Configuration redirects](https://vercel.com/docs/redirects/configuration-redirects) | Support needed for wildcards, pattern matching, and geolocation-based rules. | Framework config or `vercel.json`
[Bulk redirects](https://vercel.com/docs/redirects/bulk-redirects) | For large-scale migrations or maintaining extensive redirect lists. It supports many thousands of simple redirects and is performant at scale. | CSV, JSON, or JSONL files
[Vercel Functions](https://vercel.com/docs/routing/redirects#vercel-functions) | For complex custom redirect logic. | Route files (code)
[Middleware](https://vercel.com/docs/routing/redirects#middleware) | Dynamic redirects that need to update without redeploying. | Middleware file and Edge Config
[Domain redirects](https://vercel.com/docs/routing/redirects#domain-redirects) | Domain-level redirects such as www to apex domain. | Dashboard (Domains section)
[Firewall redirects](https://vercel.com/docs/routing/redirects#firewall-redirects) | Emergency redirects that must execute before other redirects. | Firewall rules (dashboard)
###  [Vercel Functions](https://vercel.com/docs/routing/redirects#vercel-functions)[](https://vercel.com/docs/routing/redirects#vercel-functions)
Use Vercel Functions to implement any redirect logic you need. This may not be optimal depending on the use case.
Any route can redirect requests like so:
app/api/route.ts
Next.js (/app)
Next.js (/app) Next.js (/pages) SvelteKit Nuxt Other frameworks
TypeScript
TypeScript JavaScript Bash
```
import { redirect } from 'next/navigation';

export async function GET(request: Request) {
  redirect('https://nextjs.org/');
}
```

###  [Middleware](https://vercel.com/docs/routing/redirects#middleware)[](https://vercel.com/docs/routing/redirects#middleware)
For dynamic, critical redirects that need to run on every request, you can use [Middleware](https://vercel.com/docs/routing-middleware) and [Edge Config](https://vercel.com/docs/storage/edge-config).
Redirects can be stored in an Edge Config and instantly read from Middleware. This enables you to update redirect values without having to redeploy your website.
[Deploy a template](https://vercel.com/templates/next.js/maintenance-page) to get started.
###  [Domain Redirects](https://vercel.com/docs/routing/redirects#domain-redirects)[](https://vercel.com/docs/routing/redirects#domain-redirects)
You can redirect a `www` subdomain to an apex domain, or other domain redirects, through the [Domains](https://vercel.com/docs/projects/domains/deploying-and-redirecting#redirecting-domains) section of the dashboard.
###  [Firewall Redirects](https://vercel.com/docs/routing/redirects#firewall-redirects)[](https://vercel.com/docs/routing/redirects#firewall-redirects)
In emergency situations, you can also define redirects using [Firewall rules](https://vercel.com/docs/security/vercel-waf/examples#emergency-redirect) to redirect requests to a new page. Firewall redirects execute before CDN configuration redirects (e.g. `vercel.json` or `next.config.js`) are evaluated.
