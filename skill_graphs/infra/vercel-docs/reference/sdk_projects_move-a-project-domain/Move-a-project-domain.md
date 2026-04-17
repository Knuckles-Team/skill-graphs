# Move a project domain
POST`https://api.vercel.com/v1/projects/{idOrName}/domains/{domain}/move`
Move one project's domain to another project. Also allows the move of all redirects pointed to that domain in the same project.
Request
```


1

import { Vercel } from "@vercel/sdk";






2







3

const vercel = new Vercel({






4

  bearerToken: "<YOUR_BEARER_TOKEN_HERE>",






5

});






6







7

async function run() {






8

  const result = await vercel.projects.moveProjectDomain({






9

    idOrName: "<value>",






10

    domain: "www.example.com",






11

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






12

    slug: "my-team-url-slug",






13

    requestBody: {






14

      projectId: "prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA",






15

      gitBranch: null,






16

      redirect: "foobar.com",






17

      redirectStatusCode: 307,






18

    },






19

  });






20







21

  console.log(result);






22

}






23







24

run();




```

Response
```


1

{






2

  "name": "Example Name",






3

  "apexName": "Example Name",






4

  "projectId": "example_id",






5

  "redirect": "string",






6

  "redirectStatusCode": "301",






7

  "gitBranch": "string",






8

  "customEnvironmentId": "example_id",






9

  "updatedAt": "123",






10

  "createdAt": "123",






11

  "verified": "false",






12

  "verification": [






13

    {






14

      "type": "string",






15

      "domain": "string",






16

      "value": "string",






17

      "reason": "Customer requested refund"






18

    }






19

  ]






20

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/projects/retrieve-project-domains-by-project-by-id-or-name#authentication)[](https://vercel.com/docs/rest-api/sdk/projects/retrieve-project-domains-by-project-by-id-or-name#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/projects/retrieve-project-domains-by-project-by-id-or-name#path-parameters)[](https://vercel.com/docs/rest-api/sdk/projects/retrieve-project-domains-by-project-by-id-or-name#path-parameters)
idOrNamestringRequired
The unique project identifier or the project name
domainstringRequired
The project domain name
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/projects/retrieve-project-domains-by-project-by-id-or-name#query-parameters)[](https://vercel.com/docs/rest-api/sdk/projects/retrieve-project-domains-by-project-by-id-or-name#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Body](https://vercel.com/docs/rest-api/sdk/projects/retrieve-project-domains-by-project-by-id-or-name#body)[](https://vercel.com/docs/rest-api/sdk/projects/retrieve-project-domains-by-project-by-id-or-name#body)
application/json
projectIdstringRequired
gitBranchstringOptional
Git branch to link the project domain
redirectstringOptional
Target destination domain for redirect
redirectStatusCodeintegerOptional
Status code for domain redirect
+Show 5 enum values
##  [Response](https://vercel.com/docs/rest-api/sdk/projects/retrieve-project-domains-by-project-by-id-or-name#response)[](https://vercel.com/docs/rest-api/sdk/projects/retrieve-project-domains-by-project-by-id-or-name#response)
200The domain was updated successfully
namestringRequired
apexNamestringRequired
projectIdstringRequired
redirectstringOptional
redirectStatusCodenumberOptional
+Show 4 enum values
gitBranchstringOptional
customEnvironmentIdstringOptional
updatedAtnumberOptional
createdAtnumberOptional
verifiedbooleanRequired
`true` if the domain is verified for use with the project. If `false` it will not be used as an alias on this project until the challenge in `verification` is completed.
+Show 2 enum values
verificationarrayOptional
A list of verification challenges, one of which must be completed to verify the domain for use on the project. After the challenge is complete `POST /projects/:idOrName/domains/:domain/verify` to verify the domain. Possible challenges: - If `verification.type = TXT` the `verification.domain` will be checked for a TXT record matching `verification.value`.
+Show 4 properties
##  [Errors](https://vercel.com/docs/rest-api/sdk/projects/retrieve-project-domains-by-project-by-id-or-name#errors)[](https://vercel.com/docs/rest-api/sdk/projects/retrieve-project-domains-by-project-by-id-or-name#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid. The domain redirect is not valid
401The request is not authorized.
403You do not have permission to access this resource.
409The project is currently being transferred
Request
```


1

import { Vercel } from "@vercel/sdk";






2







3

const vercel = new Vercel({






4

  bearerToken: "<YOUR_BEARER_TOKEN_HERE>",






5

});






6







7

async function run() {






8

  const result = await vercel.projects.moveProjectDomain({






9

    idOrName: "<value>",






10

    domain: "www.example.com",






11

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






12

    slug: "my-team-url-slug",






13

    requestBody: {






14

      projectId: "prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA",






15

      gitBranch: null,






16

      redirect: "foobar.com",






17

      redirectStatusCode: 307,






18

    },






19

  });






20







21

  console.log(result);






22

}






23







24

run();




```

Response
```


1

{






2

  "name": "Example Name",






3

  "apexName": "Example Name",






4

  "projectId": "example_id",






5

  "redirect": "string",






6

  "redirectStatusCode": "301",






7

  "gitBranch": "string",






8

  "customEnvironmentId": "example_id",






9

  "updatedAt": "123",






10

  "createdAt": "123",






11

  "verified": "false",






12

  "verification": [






13

    {






14

      "type": "string",






15

      "domain": "string",






16

      "value": "string",






17

      "reason": "Customer requested refund"






18

    }






19

  ]






20

}




```

Copy as MarkdownGive feedbackAsk AI about this page
## Get Started
  * [Templates](https://vercel.com/templates)
  * [Supported frameworks](https://vercel.com/docs/frameworks)
  * [Marketplace](https://vercel.com/marketplace)
  * [Domains](https://vercel.com/domains)


## Build
  * [Next.js on Vercel](https://vercel.com/frameworks/nextjs)
  * [Turborepo](https://vercel.com/solutions/turborepo)


## Scale
  * [Content delivery network](https://vercel.com/cdn)
  * [Fluid compute](https://vercel.com/fluid)
  * [CI/CD](https://vercel.com/products/previews)
  * [Observability](https://vercel.com/products/observability)
  * [AI GatewayNew](https://vercel.com/ai-gateway)
  * [Vercel AgentNew](https://vercel.com/agent)


## Secure
  * [Platform security](https://vercel.com/security)
  * [Web Application Firewall](https://vercel.com/security/web-application-firewall)
  * [Bot management](https://vercel.com/security/bot-management)
  * [BotID](https://vercel.com/botid)
  * [SandboxNew](https://vercel.com/sandbox)


## Resources
  * [Pricing](https://vercel.com/pricing)
  * [Customers](https://vercel.com/customers)
  * [Enterprise](https://vercel.com/enterprise)
  * [Articles](https://vercel.com/i)
  * [Startups](https://vercel.com/startups)
  * [Solution partners](https://vercel.com/partners/solution-partners)


## Learn
  * [Docs](https://vercel.com/docs)
  * [Blog](https://vercel.com/blog)
  * [Changelog](https://vercel.com/changelog)
  * [Knowledge Base](https://vercel.com/kb)
  * [Academy](https://vercel.com/academy)
  * [Community](https://community.vercel.com)


## Frameworks
  * [Next.js](https://vercel.com/frameworks/nextjs)
  * [Nuxt](https://vercel.com/docs/frameworks/full-stack/nuxt)
  * [Svelte](https://vercel.com/docs/frameworks/full-stack/sveltekit)
  * [Nitro](https://vercel.com/docs/frameworks/backend/nitro)
  * [Turbo](https://vercel.com/solutions/turborepo)


## SDKs
## Use Cases
  * [Composable commerce](https://vercel.com/solutions/composable-commerce)
  * [Multi-tenant platforms](https://vercel.com/solutions/multi-tenant-saas)
  * [Web apps](https://vercel.com/solutions/web-apps)
  * [Marketing sites](https://vercel.com/solutions/marketing-sites)
  * [Platform engineers](https://vercel.com/solutions/platform-engineering)
  * [Design engineers](https://vercel.com/solutions/design-engineering)


## Company
  * [About](https://vercel.com/about)
  * [Careers](https://vercel.com/careers)
  * [Help](https://vercel.com/help)
  * [Press](https://vercel.com/press)
  * [Legal](https://vercel.com/legal)
  * [Privacy Policy](https://vercel.com/legal/privacy-policy)


## Community
  * [Open source program](https://vercel.com/open-source-program)
  * [Events](https://vercel.com/events)
  * [Shipped on Vercel](https://vercel.com/shipped)


[](https://vercel.com/home)

Select a display theme: systemlightdark
