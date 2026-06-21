##  [Using the Vercel REST API](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#using-the-vercel-rest-api)[](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#using-the-vercel-rest-api)
See the following API reference documentation for how to use Vercel REST API to create integrations:
  * [Creating a Project Environment Variable](https://vercel.com/docs/rest-api/reference/endpoints/projects/create-one-or-more-environment-variables)
  * [Forwarding Logs using Log Drains](https://vercel.com/docs/drains/reference/logs)
  * [Create an Access Token](https://vercel.com/docs/rest-api/vercel-api-integrations#create-an-access-token)
  * [Interacting with Teams](https://vercel.com/docs/rest-api/vercel-api-integrations#interacting-with-teams)
  * [Interacting with Configurations](https://vercel.com/docs/rest-api/vercel-api-integrations#interacting-with-configurations)
  * [Interacting with Vercel Projects](https://vercel.com/docs/rest-api/vercel-api-integrations#interacting-with-vercel-projects)


###  [Create an Access Token](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#create-an-access-token)[](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#create-an-access-token)
To use Vercel REST API, you need to authenticate with an [access token](https://vercel.com/docs/rest-api/reference/welcome#authentication) that contains the necessary [scope](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#scopes). You can then provide the API token through the [`Authorization` header](https://vercel.com/docs/rest-api#authentication).
####  [Exchange `code` for Access Token](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#exchange-code-for-access-token)[](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#exchange-code-for-access-token)
When you create an integration, you define a [redirect URL](https://vercel.com/docs/integrations/create-integration/submit-integration#redirect-url) that can have query parameters attached.
One of these parameters is the `code` parameter. This short-lived parameter is valid for 30 minutes and can be exchanged once for a long-lived access token using the following API endpoint:
terminal
```
{`POST https://api.vercel.com/v2/oauth/access_token`}
```

Pass the following values to the request body in the form of `application/x-www-form-urlencoded`.
Key | [Type](https://vercel.com/docs/rest-api/reference#types) | Required | Description
---|---|---|---
client_id | [ID](https://vercel.com/docs/rest-api/reference#types) | Yes | ID of your application.
client_secret | [String](https://vercel.com/docs/rest-api/reference#types) | Yes | Secret of your application.
code | [String](https://vercel.com/docs/rest-api/reference#types) | Yes | The code you received.
redirect_uri | [String](https://vercel.com/docs/rest-api/reference#types) | Yes | The Redirect URL you configured on the Integration Console.
####  [Example Request](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#example-request)[](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#example-request)
Show More
###  [Interacting with Teams](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#interacting-with-teams)[](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#interacting-with-teams)
The response of your `code` exchange request includes a `team_id` property. If `team_id` is not null, you know that this integration was installed on a team.
If your integration is installed on a team, append the `teamId` query parameter to each API request. See [Accessing Resources Owned by a Team](https://vercel.com/docs/rest-api#accessing-resources-owned-by-a-team) for more details.
###  [Interacting with Configurations](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#interacting-with-configurations)[](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#interacting-with-configurations)
Each installation of your integration is stored and tracked as a configuration.
Sometimes it makes sense to fetch the configuration in order to get more insights about the current scope or the projects your integration has access to.
To see which endpoints are available, see the [Configurations](https://vercel.com/docs/project-configuration) documentation for more details.
####  [Disabled Integration Configurations](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#disabled-integration-configurations)[](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#disabled-integration-configurations)
If an owner(s) of an integration leaves the team that's responsible for the integration, the integration will be flagged as disabled. The team will receive an email to take action (transfer ownership) within 30 days, otherwise the integration will be deleted.
When integration configurations are disabled:
  * Any API requests will fail with a `403` HTTP status code and a `code` of `integration_configuration_disabled`
  * We continue to send `project.created`, `project.removed` and `integration-configuration.removed` webhooks, as these will allow the integration configuration to operate correctly when re-activated. All other webhook delivery will be paused
  * Log drains will not receive any logs


###  [Interacting with Vercel Projects](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#interacting-with-vercel-projects)[](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#interacting-with-vercel-projects)
Deployments made with Vercel are grouped into Projects. This means that each deployment is assigned a name and is grouped into a project with other deployments using that same name.
Using the Vercel REST API, you can modify Projects that the Integration has access to. Here are some examples:
###  [Modifying Environment Variables on a Project](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#modifying-environment-variables-on-a-project)[](https://vercel.com/docs/integrations/create-integration/vercel-api-integrations#modifying-environment-variables-on-a-project)
When building a Vercel Integration, you may want to expose an API token or a configuration URL for deployments within a [Project](https://vercel.com/docs/projects/overview).
You can do so by [Creating a Project Environment Variable](https://vercel.com/docs/rest-api/reference/endpoints/projects/create-one-or-more-environment-variables) using the API.
Environment Variables created by an Integration will
[display the Integration's logo](https://vercel.com/docs/environment-variables#integration-environment-variables)
.
