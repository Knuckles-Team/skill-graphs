# Get a segment
GET`https://api.vercel.com/v1/projects/{projectIdOrName}/feature-flags/segments/{segmentIdOrSlug}`
Retrieve a feature flag segment by ID or slug.
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

  const result = await vercel.featureFlags.getFlagSegment({






9

    projectIdOrName: "<value>",






10

    segmentIdOrSlug: "<value>",






11

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






12

    slug: "my-team-url-slug",






13

  });






14







15

  console.log(result);






16

}






17







18

run();




```

Response
```


1

{






2

  "description": "string",






3

  "createdBy": "string",






4

  "usedByFlags": [],






5

  "usedBySegments": [],






6

  "id": "icfg_1234567890",






7

  "label": "string",






8

  "slug": "string",






9

  "createdAt": "123",






10

  "updatedAt": "123",






11

  "projectId": "example_id",






12

  "typeName": "segment",






13

  "data": {






14

    "rules": [






15

      {






16

        "id": "icfg_1234567890",






17

        "outcome": {






18

          "type": "all"






19

        },






20

        "conditions": [






21

          {






22

            "rhs": "string",






23

            "lhs": {






24

              "type": "segment"






25

            },






26

            "cmp": "eq"






27

          }






28

        ]






29

      }






30

    ],






31

    "include": "value",






32

    "exclude": "value"






33

  },






34

  "hint": "string",






35

  "metadata": {






36

    "creator": {






37

      "id": "icfg_1234567890",






38

      "name": "Example Name"






39

    }






40

  }






41

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/feature-flags/update-project-flag-settings#authentication)[](https://vercel.com/docs/rest-api/sdk/feature-flags/update-project-flag-settings#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/feature-flags/update-project-flag-settings#path-parameters)[](https://vercel.com/docs/rest-api/sdk/feature-flags/update-project-flag-settings#path-parameters)
projectIdOrNamestringRequired
The project id or name
segmentIdOrSlugstringRequired
The segment slug
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/feature-flags/update-project-flag-settings#query-parameters)[](https://vercel.com/docs/rest-api/sdk/feature-flags/update-project-flag-settings#query-parameters)
withMetadatabooleanOptional
Whether to include metadata
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sdk/feature-flags/update-project-flag-settings#response)[](https://vercel.com/docs/rest-api/sdk/feature-flags/update-project-flag-settings#response)
200Success
descriptionstringOptional
createdBystringOptional
usedByFlagsarrayOptional
usedBySegmentsarrayOptional
idstringRequired
labelstringRequired
slugstringRequired
createdAtnumberRequired
updatedAtnumberRequired
projectIdstringRequired
typeNamestringRequired
+Show 1 enum values
dataobjectRequired
+Show 3 properties
hintstringRequired
metadataobjectOptional
+Show 1 properties
##  [Errors](https://vercel.com/docs/rest-api/sdk/feature-flags/update-project-flag-settings#errors)[](https://vercel.com/docs/rest-api/sdk/feature-flags/update-project-flag-settings#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
402The account was soft-blocked for an unhandled reason. The account is missing a payment so payment method must be updated
403You do not have permission to access this resource.
404Error
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

  const result = await vercel.featureFlags.getFlagSegment({






9

    projectIdOrName: "<value>",






10

    segmentIdOrSlug: "<value>",






11

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






12

    slug: "my-team-url-slug",






13

  });






14







15

  console.log(result);






16

}






17







18

run();




```

Response
```


1

{






2

  "description": "string",






3

  "createdBy": "string",






4

  "usedByFlags": [],






5

  "usedBySegments": [],






6

  "id": "icfg_1234567890",






7

  "label": "string",






8

  "slug": "string",






9

  "createdAt": "123",






10

  "updatedAt": "123",






11

  "projectId": "example_id",






12

  "typeName": "segment",






13

  "data": {






14

    "rules": [






15

      {






16

        "id": "icfg_1234567890",






17

        "outcome": {






18

          "type": "all"






19

        },






20

        "conditions": [






21

          {






22

            "rhs": "string",






23

            "lhs": {






24

              "type": "segment"






25

            },






26

            "cmp": "eq"






27

          }






28

        ]






29

      }






30

    ],






31

    "include": "value",






32

    "exclude": "value"






33

  },






34

  "hint": "string",






35

  "metadata": {






36

    "creator": {






37

      "id": "icfg_1234567890",






38

      "name": "Example Name"






39

    }






40

  }






41

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
