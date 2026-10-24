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
Get a single check
# Get a single check
GET`https://api.vercel.com/v1/deployments/{deploymentId}/checks/{checkId}`
Return a detailed response for a single check.
This endpoint is deprecated
Request
```


1

package main






2







3

import(






4

	"os"






5

	"github.com/vercel/vercel"






6

	"context"






7

	"log"






8

)






9







10

func main() {






11

    s := vercel.New(






12

        vercel.WithSecurity(os.Getenv("VERCEL_BEARER_TOKEN")),






13

    )






14







15

    ctx := context.Background()






16

    res, err := s.Checks.GetCheck(ctx, "dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6", "check_2qn7PZrx89yxY34vEZPD31Y9XVj6", nil, nil)






17

    if err != nil {






18

        log.Fatal(err)






19

    }






20

    if res.Object != nil {






21

        // handle response






22

    }






23

}




```

Response
```


1

{






2

  "id": "icfg_1234567890",






3

  "name": "Example Name",






4

  "createdAt": "123",






5

  "updatedAt": "123",






6

  "deploymentId": "example_id",






7

  "status": "running",






8

  "conclusion": "canceled",






9

  "externalId": "example_id",






10

  "output": {






11

    "metrics": {






12

      "FCP": {






13

        "value": "123",






14

        "previousValue": "123",






15

        "source": "web-vitals"






16

      },






17

      "LCP": {






18

        "value": "123",






19

        "previousValue": "123",






20

        "source": "web-vitals"






21

      },






22

      "CLS": {






23

        "value": "123",






24

        "previousValue": "123",






25

        "source": "web-vitals"






26

      },






27

      "TBT": {






28

        "value": "123",






29

        "previousValue": "123",






30

        "source": "web-vitals"






31

      },






32

      "virtualExperienceScore": {






33

        "value": "123",






34

        "previousValue": "123",






35

        "source": "web-vitals"






36

      }






37

    }






38

  },






39

  "completedAt": "123",






40

  "path": "string",






41

  "blocking": "false",






42

  "detailsUrl": "https://example.com",






43

  "integrationId": "example_id",






44

  "startedAt": "123",






45

  "rerequestable": "false"






46

}




```

##  [Authentication](https://vercel.com/docs#authentication)[](https://vercel.com/docs#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs#path-parameters)[](https://vercel.com/docs#path-parameters)
deploymentIdstringRequired
The deployment to get the check for.
checkIdstringRequired
The check to fetch
##  [Query parameters](https://vercel.com/docs#query-parameters)[](https://vercel.com/docs#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs#response)[](https://vercel.com/docs#response)
200Success
idstringRequired
namestringRequired
createdAtnumberRequired
updatedAtnumberRequired
deploymentIdstringRequired
statusstringRequired
+Show 3 enum values
conclusionstringOptional
+Show 6 enum values
externalIdstringOptional
outputobjectOptional
+Show 1 properties
completedAtnumberOptional
pathstringOptional
blockingbooleanRequired
+Show 2 enum values
detailsUrlstringOptional
integrationIdstringRequired
startedAtnumberOptional
rerequestablebooleanOptional
+Show 2 enum values
##  [Errors](https://vercel.com/docs#errors)[](https://vercel.com/docs#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource. The provided token is not from an OAuth2 Client that created the Check
404Check was not found The deployment was not found
