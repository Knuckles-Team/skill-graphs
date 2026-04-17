# Remove an environment variable
DEL`https://api.vercel.com/v9/projects/{idOrName}/env/{id}`
Delete a specific environment variable for a given project by passing the environment variable identifier and either passing the project `id` or `name` in the URL.
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

  const result = await vercel.projects.removeProjectEnv({






9

    idOrName: "prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA",






10

    id: "XMbOEya1gUUO1ir4",






11

    customEnvironmentId: "env_123abc4567",






12

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






13

    slug: "my-team-url-slug",






14

  });






15







16

  console.log(result);






17

}






18







19

run();




```

Response
```


1

[






2

  {






3

    "type": "secret",






4

    "value": "string",






5

    "edgeConfigId": "example_id",






6

    "edgeConfigTokenId": "example_id",






7

    "createdAt": "123",






8

    "updatedAt": "123",






9

    "id": "icfg_1234567890",






10

    "createdBy": "string",






11

    "target": [],






12

    "key": "string",






13

    "gitBranch": "string",






14

    "updatedBy": "string",






15

    "sunsetSecretId": "example_id",






16

    "legacyValue": "string",






17

    "decrypted": "false",






18

    "configurationId": "example_id",






19

    "contentHint": {






20

      "type": "redis-url",






21

      "storeId": "example_id"






22

    },






23

    "internalContentHint": {






24

      "type": "flags-secret",






25

      "encryptedValue": "string"






26

    },






27

    "comment": "string",






28

    "customEnvironmentIds": []






29

  }






30

]




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/projects/create-one-or-more-environment-variables#authentication)[](https://vercel.com/docs/rest-api/sdk/projects/create-one-or-more-environment-variables#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/projects/create-one-or-more-environment-variables#path-parameters)[](https://vercel.com/docs/rest-api/sdk/projects/create-one-or-more-environment-variables#path-parameters)
idOrNamestringRequired
The unique project identifier or the project name
idstringRequired
The unique environment variable identifier
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/projects/create-one-or-more-environment-variables#query-parameters)[](https://vercel.com/docs/rest-api/sdk/projects/create-one-or-more-environment-variables#query-parameters)
customEnvironmentIdstringOptional
The unique custom environment identifier within the project
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sdk/projects/create-one-or-more-environment-variables#response)[](https://vercel.com/docs/rest-api/sdk/projects/create-one-or-more-environment-variables#response)
200The environment variable was successfully removed
##  [Errors](https://vercel.com/docs/rest-api/sdk/projects/create-one-or-more-environment-variables#errors)[](https://vercel.com/docs/rest-api/sdk/projects/create-one-or-more-environment-variables#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
409The project is being transferred and removing an environment variable is not possible
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

  const result = await vercel.projects.removeProjectEnv({






9

    idOrName: "prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA",






10

    id: "XMbOEya1gUUO1ir4",






11

    customEnvironmentId: "env_123abc4567",






12

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






13

    slug: "my-team-url-slug",






14

  });






15







16

  console.log(result);






17

}






18







19

run();




```

Response
```


1

[






2

  {






3

    "type": "secret",






4

    "value": "string",






5

    "edgeConfigId": "example_id",






6

    "edgeConfigTokenId": "example_id",






7

    "createdAt": "123",






8

    "updatedAt": "123",






9

    "id": "icfg_1234567890",






10

    "createdBy": "string",






11

    "target": [],






12

    "key": "string",






13

    "gitBranch": "string",






14

    "updatedBy": "string",






15

    "sunsetSecretId": "example_id",






16

    "legacyValue": "string",






17

    "decrypted": "false",






18

    "configurationId": "example_id",






19

    "contentHint": {






20

      "type": "redis-url",






21

      "storeId": "example_id"






22

    },






23

    "internalContentHint": {






24

      "type": "flags-secret",






25

      "encryptedValue": "string"






26

    },






27

    "comment": "string",






28

    "customEnvironmentIds": []






29

  }






30

]




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
