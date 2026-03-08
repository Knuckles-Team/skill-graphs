Menu
# Vercel Documentation
Last updated January 30, 2026
Vercel is the AI Cloud, a unified platform for building, deploying, and scaling AI-powered applications. Ship web apps, agentic workloads, and everything in between.
##  [Get started with Vercel](https://vercel.com/docs#get-started-with-vercel)[](https://vercel.com/docs#get-started-with-vercel)
Build any type of application on Vercel: static sites with your favorite [framework](https://vercel.com/docs/frameworks), [multi-tenant](https://vercel.com/docs/multi-tenant) SaaS products, [microfrontends](https://vercel.com/docs/microfrontends), or [AI-powered agents](https://vercel.com/kb/guide/how-to-build-ai-agents-with-vercel-and-the-ai-sdk).
The [Vercel Marketplace](https://vercel.com/docs/integrations) provides integrations for AI providers, databases, CMSs, analytics, and storage.
Connect your [Git repository](https://vercel.com/docs/git) to deploy on every push, with [automatic preview environments](https://vercel.com/docs/deployments/environments#preview-environment-pre-production) for testing changes before production.
See the [getting started guide](https://vercel.com/docs/getting-started-with-vercel) for more information, or the [incremental migration guide](https://vercel.com/docs/incremental-migration) to migrate an existing application.
##  [Quick references](https://vercel.com/docs#quick-references)[](https://vercel.com/docs#quick-references)
[Configuring vercel.json](https://vercel.com/docs/project-configuration)[Working with Domains](https://vercel.com/docs/domains/working-with-domains)[Storage for your Vercel project](https://vercel.com/docs/storage)[Vercel MCP](https://vercel.com/docs/agent-resources/vercel-mcp)[Caching on Vercel](https://vercel.com/docs/cdn-cache)
##  [Build your applications](https://vercel.com/docs#build-your-applications)[](https://vercel.com/docs#build-your-applications)
Use one or more of the following tools to build your application depending on your needs:
  * [Next.js](https://vercel.com/docs/frameworks/nextjs): Build full-stack applications with Next.js, or any of our [supported frameworks](https://vercel.com/docs/frameworks/more-frameworks)
  * [Functions](https://vercel.com/docs/functions): API routes with [Fluid compute](https://vercel.com/docs/fluid-compute), [active CPU, and provisioned memory](https://vercel.com/docs/functions/usage-and-pricing), perfect for AI workloads
  * [Routing Middleware](https://vercel.com/docs/routing-middleware): Customize your application's behavior with code that runs before a request is processed
  * [Incremental Static Regeneration](https://vercel.com/docs/incremental-static-regeneration): Automatically regenerate your pages on a schedule or when a request is made
  * [Image Optimization](https://vercel.com/docs/image-optimization): Optimize your images for the web
  * [Manage environments](https://vercel.com/docs/deployments/environments): Local, preview, production, and custom environments
  * [Feature flags](https://vercel.com/docs/feature-flags): Control the visibility of features in your application


##  [Use Vercel's AI infrastructure](https://vercel.com/docs#use-vercel's-ai-infrastructure)[](https://vercel.com/docs#use-vercel's-ai-infrastructure)
Add intelligence to your applications with Vercel's AI-first infrastructure:
  * [AI SDK](https://vercel.com/docs/ai-sdk): Integrate language models with streaming and tool calling
  * [AI Gateway](https://vercel.com/docs/ai-gateway): Route to any AI provider with automatic failover
  * [Agents](https://vercel.com/kb/guide/how-to-build-ai-agents-with-vercel-and-the-ai-sdk): Build autonomous workflows and conversational interfaces
  * [MCP Servers](https://vercel.com/docs/mcp): Create tools for AI agents to interact with your systems
  * [Agent Resources](https://vercel.com/docs/agent-resources): Access documentation for AI tools, MCP servers, agent skills, and more
  * [Sandbox](https://vercel.com/docs/vercel-sandbox): Secure execution environments for untrusted code
  * [Claim deployments](https://vercel.com/docs/deployments/claim-deployments): Allow AI agents to deploy a project and let a human take over


##  [Collaborate with your team](https://vercel.com/docs#collaborate-with-your-team)[](https://vercel.com/docs#collaborate-with-your-team)
Collaborate with your team using the following tools:
  * [Toolbar](https://vercel.com/docs/vercel-toolbar): An in-browser toolbar that lets you leave feedback, manage feature flags, preview drafts, edit content live, inspect [performance](https://vercel.com/docs/vercel-toolbar/interaction-timing-tool)/[layout](https://vercel.com/docs/vercel-toolbar/layout-shift-tool)/[accessibility](https://vercel.com/docs/vercel-toolbar/accessibility-audit-tool), and navigate/share deployment pages
  * [Comments](https://vercel.com/docs/comments): Let teams and invited collaborators comment on your preview deployments and production environments
  * [Draft mode](https://vercel.com/docs/draft-mode): View your unpublished headless CMS content on your site


##  [Secure your applications](https://vercel.com/docs#secure-your-applications)[](https://vercel.com/docs#secure-your-applications)
Secure your applications with the following tools:
  * [Deployment Protection](https://vercel.com/docs/deployment-protection): Protect your applications from unauthorized access
  * [RBAC](https://vercel.com/docs/rbac): Role-based access control for your applications
  * [Configurable WAF](https://vercel.com/docs/vercel-firewall/vercel-waf): Customizable rules to protect against attacks, scrapers, and unwanted traffic
  * [Bot Management](https://vercel.com/docs/bot-management): Protect your applications from bots and automated traffic
  * [BotID](https://vercel.com/docs/botid): An invisible CAPTCHA that protects against sophisticated bots without showing visible challenges or requiring manual intervention
  * [AI bot filtering](https://vercel.com/docs/bot-management#ai-bots-managed-ruleset): Control traffic from AI bots
  * [Platform DDoS Mitigation](https://vercel.com/docs/security/ddos-mitigation): Protect your applications from DDoS attacks


##  [Deploy and scale](https://vercel.com/docs#deploy-and-scale)[](https://vercel.com/docs#deploy-and-scale)
Vercel handles infrastructure automatically based on your framework and code, and provides the following tools to help you deploy and scale your applications:
  * [Vercel Delivery Network](https://vercel.com/docs/cdn): Fast, globally distributed execution
  * [Rolling Releases](https://vercel.com/docs/rolling-releases): Roll out new deployments in increments
  * [Rollback deployments](https://vercel.com/docs/instant-rollback): Roll back to a previous deployment, for swift recovery from production incidents, like breaking changes or bugs
  * [Observability suite](https://vercel.com/docs/observability): Monitor performance and debug your AI workflows and apps


* * *
[ Next Getting Started ](https://vercel.com/docs/getting-started-with-vercel)
Was this helpful?
Send
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
SSO Token Exchange
# SSO Token Exchange
POST`https://api.vercel.com/v1/integrations/sso/token`
During the authorization process, Vercel sends the user to the provider [redirectLoginUrl](https://vercel.com/docs/integrations/create-integration/submit-integration#redirect-login-url), that includes the OAuth authorization `code` parameter. The provider then calls the SSO Token Exchange endpoint with the sent code and receives the OIDC token. They log the user in based on this token and redirects the user back to the Vercel account using deep-link parameters included the redirectLoginUrl. Providers should not persist the returned `id_token` in a database since the token will expire. See [**Authentication with SSO**](https://vercel.com/docs/integrations/create-integration/marketplace-api#authentication-with-sso) for more details.
exchange-sso-tokenexchange-sso-token
Request
```


1

import { Vercel } from "@vercel/sdk";






2







3

const vercel = new Vercel();






4







5

async function run() {






6

  const result = await vercel.authentication.exchangeSsoToken({






7

    code: "<value>",






8

    clientId: "<id>",






9

    clientSecret: "<value>",






10

    grantType: "authorization_code",






11

  });






12







13

  console.log(result);






14

}






15







16

run();




```

Response
```


1

{






2

  "id_token": "example_id",






3

  "token_type": "string",






4

  "expires_in": "123",






5

  "access_token": "string",






6

  "refresh_token": "string"






7

}




```

##  [Body](https://vercel.com/docs#body)[](https://vercel.com/docs#body)
application/json
Option 1Option 2
codestringRequired
The sensitive code received from Vercel
statestringOptional
The state received from the initialization request
client_idstringRequired
The integration client id
client_secretstringRequired
The integration client secret
redirect_uristringOptional
The integration redirect URI
grant_typestringRequired
The grant type, when using x-www-form-urlencoded content type
+Show 1 enum values
##  [Response](https://vercel.com/docs#response)[](https://vercel.com/docs#response)
200Success
id_tokenstringRequired
token_typestringRequired
expires_innumberOptional
access_tokenstringRequired
refresh_tokenstringOptional
##  [Errors](https://vercel.com/docs#errors)[](https://vercel.com/docs#errors)
400One of the provided values in the request body is invalid.
403Error
500Error
