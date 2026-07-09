##  [How it works](https://vercel.com/docs#how-it-works)[](https://vercel.com/docs#how-it-works)
When a user interacts with your integration, Vercel calls your Partner API endpoints on your integration server. You implement these endpoints to handle:
  * **Installation lifecycle** — Create, update, and delete installations when users add or remove your integration
  * **Resource management** — Provision and configure resources when users connect projects or add configuration
  * **Billing operations** — Handle invoice creation, usage reporting, and payment processing
  * **User authentication** — Validate and process user-initiated actions


Your integration also calls [Vercel API endpoints](https://vercel.com/docs/integrations/create-integration/marketplace-api/reference/vercel) to interact with Vercel resources like projects, deployments, and environment variables. See [Native Integration Flows](https://vercel.com/docs/integrations/create-integration/marketplace-flows) to understand how these APIs work together.
