##  [Differences from deployment-level routes](https://vercel.com/docs/routing/project-routing-rules#differences-from-deployment-level-routes)[](https://vercel.com/docs/routing/project-routing-rules#differences-from-deployment-level-routes)
Project-level routing rules support the same core actions as `vercel.json` routes: rewrites, redirects, status codes, and header modifications. The main difference is that project-level rules run at the CDN without access to your deployment's code, so [Routing Middleware](https://vercel.com/docs/functions/routing-middleware) isn't available. If your routing logic requires custom code (for example, authentication checks or A/B test assignments), use Routing Middleware in your deployment instead.
A few other `vercel.json` fields are also deployment-only: `locale` for i18n routing, and the internal fields `handle`, `check`, `continue`, and `mitigate`.
* * *
[ Previous Rewrites ](https://vercel.com/docs/routing/rewrites)[ Next Security ](https://vercel.com/docs/cdn-security)
Was this helpful?
Send
On this page
  * [Create a routing rule](https://vercel.com/docs/routing/project-routing-rules#create-a-routing-rule)
  * [Match conditions](https://vercel.com/docs/routing/project-routing-rules#match-conditions)
  * [Path matching](https://vercel.com/docs/routing/project-routing-rules#path-matching)
  * [Additional conditions](https://vercel.com/docs/routing/project-routing-rules#additional-conditions)
  * [Available actions](https://vercel.com/docs/routing/project-routing-rules#available-actions)
  * [Primary actions](https://vercel.com/docs/routing/project-routing-rules#primary-actions)
  * [Modify actions](https://vercel.com/docs/routing/project-routing-rules#modify-actions)
  * [Stage, test, and publish](https://vercel.com/docs/routing/project-routing-rules#stage-test-and-publish)
  * [Rule ordering](https://vercel.com/docs/routing/project-routing-rules#rule-ordering)
  * [Manage rules with the API](https://vercel.com/docs/routing/project-routing-rules#manage-rules-with-the-api)
  * [Differences from deployment-level routes](https://vercel.com/docs/routing/project-routing-rules#differences-from-deployment-level-routes)


Copy as MarkdownGive feedbackAsk AI about this page
