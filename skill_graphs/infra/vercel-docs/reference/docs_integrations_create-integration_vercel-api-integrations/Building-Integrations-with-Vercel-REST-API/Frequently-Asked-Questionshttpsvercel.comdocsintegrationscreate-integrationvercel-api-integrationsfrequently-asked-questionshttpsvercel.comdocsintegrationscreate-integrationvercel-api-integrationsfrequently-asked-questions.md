##  [Frequently Asked Questions](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#frequently-asked-questions)[](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#frequently-asked-questions)
###  [Are integration configuration IDs reused after deletion?](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#are-integration-configuration-ids-reused-after-deletion)[](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#are-integration-configuration-ids-reused-after-deletion)
No, integration configuration IDs (`icfg_*`) are not reused after an integration is deleted or uninstalled. Each installation of an integration receives a unique configuration ID that is permanently retired when the integration is removed. If you reinstall the same integration later, a new unique configuration ID will be generated.
* * *
[ Previous Upgrade an Integration ](https://vercel.com/docs/integrations/create-integration/upgrade-integration)[ Next Secrets Rotation ](https://vercel.com/docs/integrations/create-integration/secrets-rotation)
Was this helpful?
Send
On this page
  * [Using the Vercel REST API](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#using-the-vercel-rest-api)
  * [Create an Access Token](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#create-an-access-token)
  * [Exchange code for Access Token](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#exchange-code-for-access-token)
  * [Example Request](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#example-request)
  * [Example Response](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#example-response)
  * [Interacting with Teams](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#interacting-with-teams)
  * [Interacting with Configurations](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#interacting-with-configurations)
  * [Disabled Integration Configurations](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#disabled-integration-configurations)
  * [Interacting with Vercel Projects](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#interacting-with-vercel-projects)
  * [Modifying Environment Variables on a Project](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#modifying-environment-variables-on-a-project)
  * [Scopes](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#scopes)
  * [Integration Configuration](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#using-the-vercel-api/scopes/integration-configuration)
  * [Deployments](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#using-the-vercel-api/scopes/deployments)
  * [Deployment Checks](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#using-the-vercel-api/scopes/deployment-checks)
  * [Edge Config](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#using-the-vercel-api/scopes/edge-config)
  * [Projects](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#using-the-vercel-api/scopes/projects)
  * [Project Environmental Variables](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#using-the-vercel-api/scopes/project-environmental-variables)
  * [Global Project Environmental Variables](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#using-the-vercel-api/scopes/global-project-environmental-variables)
  * [Teams](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#using-the-vercel-api/scopes/teams)
  * [User](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#using-the-vercel-api/scopes/user)
  * [Log Drains](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#using-the-vercel-api/scopes/log-drains)
  * [Drains](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#using-the-vercel-api/scopes/drains)
  * [Domain](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#using-the-vercel-api/scopes/domain)
  * [Billing](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#using-the-vercel-api/scopes/billing)
  * [Updating Scopes](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#updating-scopes)
  * [Confirmed Scope Changes](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#confirmed-scope-changes)
  * [Common Errors](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#common-errors)
  * [CORS issues](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#cors-issues)
  * [403 Forbidden responses](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#403-forbidden-responses)
  * [Frequently Asked Questions](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#frequently-asked-questions)
  * [Are integration configuration IDs reused after deletion?](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#are-integration-configuration-ids-reused-after-deletion)


Copy as MarkdownGive feedbackAsk AI about this page
