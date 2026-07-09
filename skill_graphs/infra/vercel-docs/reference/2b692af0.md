# Retrieve project domains by project by id or name
GET`https://api.vercel.com/v9/projects/{idOrName}/domains`
Retrieve the domains associated with a given project by passing either the project `id` or `name` in the URL.
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

  const result = await vercel.projects.getProjectDomains({






9

    idOrName: "<value>",






10

    customEnvironmentId: "env_123abc4567",






11

    redirect: "example.com",






12

    limit: 20,






13

    since: 1609499532000,






14

    until: 1612264332000,






15

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






16

    slug: "my-team-url-slug",






17

  });






18







19

  console.log(result);






20

}






21







22

run();




```

Response
```


1

{






2

  "domains": [






3

    {






4

      "name": "Example Name",






5

      "apexName": "Example Name",






6

      "projectId": "example_id",






7

      "redirect": "string",






8

      "redirectStatusCode": "301",






9

      "gitBranch": "string",






10

      "customEnvironmentId": "example_id",






11

      "updatedAt": "123",






12

      "createdAt": "123",






13

      "verified": "false",






14

      "verification": [






15

        {






16

          "type": "string",






17

          "domain": "string",






18

          "value": "string",






19

          "reason": "Customer requested refund"






20

        }






21

      ]






22

    }






23

  ],






24

  "pagination": {






25

    "count": "123",






26

    "next": "123",






27

    "prev": "123"






28

  }






29

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/projects/retrieve-a-list-of-projects#authentication)[](https://vercel.com/docs/rest-api/sdk/projects/retrieve-a-list-of-projects#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/projects/retrieve-a-list-of-projects#path-parameters)[](https://vercel.com/docs/rest-api/sdk/projects/retrieve-a-list-of-projects#path-parameters)
idOrNameanyRequired
The unique project identifier or the project name
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/projects/retrieve-a-list-of-projects#query-parameters)[](https://vercel.com/docs/rest-api/sdk/projects/retrieve-a-list-of-projects#query-parameters)
productionanyOptional
Filters only production domains when set to `true`.
+Show 2 enum values
targetstringOptional
Filters on the target of the domain. Can be either "production", "preview"
+Show 2 enum values
customEnvironmentIdstringOptional
The unique custom environment identifier within the project
gitBranchstringOptional
Filters domains based on specific branch.
redirectsanyOptional
Excludes redirect project domains when "false". Includes redirect project domains when "true" (default).
+Show 2 enum values
redirectstringOptional
Filters domains based on their redirect target.
verifiedanyOptional
Filters domains based on their verification status.
+Show 2 enum values
limitnumberOptional
Maximum number of domains to list from a request (max 100).
sincenumberOptional
Get domains created after this JavaScript timestamp.
untilnumberOptional
Get domains created before this JavaScript timestamp.
orderanyOptional
Domains sort order by createdAt
+Show 2 enum values
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sdk/projects/retrieve-a-list-of-projects#response)[](https://vercel.com/docs/rest-api/sdk/projects/retrieve-a-list-of-projects#response)
200Successful response retrieving a list of domains
domainsarrayRequired
+Show 11 properties
paginationobjectRequired
+Show 3 properties
##  [Errors](https://vercel.com/docs/rest-api/sdk/projects/retrieve-a-list-of-projects#errors)[](https://vercel.com/docs/rest-api/sdk/projects/retrieve-a-list-of-projects#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
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

  const result = await vercel.projects.getProjectDomains({






9

    idOrName: "<value>",






10

    customEnvironmentId: "env_123abc4567",






11

    redirect: "example.com",






12

    limit: 20,






13

    since: 1609499532000,






14

    until: 1612264332000,






15

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






16

    slug: "my-team-url-slug",






17

  });






18







19

  console.log(result);






20

}






21







22

run();




```

Response
```


1

{






2

  "domains": [






3

    {






4

      "name": "Example Name",






5

      "apexName": "Example Name",






6

      "projectId": "example_id",






7

      "redirect": "string",






8

      "redirectStatusCode": "301",






9

      "gitBranch": "string",






10

      "customEnvironmentId": "example_id",






11

      "updatedAt": "123",






12

      "createdAt": "123",






13

      "verified": "false",






14

      "verification": [






15

        {






16

          "type": "string",






17

          "domain": "string",






18

          "value": "string",






19

          "reason": "Customer requested refund"






20

        }






21

      ]






22

    }






23

  ],






24

  "pagination": {






25

    "count": "123",






26

    "next": "123",






27

    "prev": "123"






28

  }






29

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
