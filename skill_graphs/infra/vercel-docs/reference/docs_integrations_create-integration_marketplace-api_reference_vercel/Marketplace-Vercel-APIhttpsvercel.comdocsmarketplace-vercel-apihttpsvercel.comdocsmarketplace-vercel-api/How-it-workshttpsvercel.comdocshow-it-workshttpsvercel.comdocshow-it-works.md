##  [How it works](https://vercel.com/docs#how-it-works)[](https://vercel.com/docs#how-it-works)
Your integration calls Vercel API endpoints to interact with Vercel's platform. You receive an access token when a user installs your integration, which you use to authenticate API requests.
Common operations include:
  * **Read project information** — Get project details, configuration, and deployment history
  * **Manage environment variables** — Create, update, or delete environment variables for projects
  * **Trigger deployments** — Programmatically deploy projects when external events occur
  * **Access team data** — Get team member information and permissions
  * **Update installations** — Send notifications or update installation status


Vercel also calls [Partner API endpoints](https://vercel.com/docs/integrations/create-integration/marketplace-api/reference/partner) on your server to manage the integration lifecycle. See [Native Integration Flows](https://vercel.com/docs/integrations/create-integration/marketplace-flows) to understand how these APIs work together.
