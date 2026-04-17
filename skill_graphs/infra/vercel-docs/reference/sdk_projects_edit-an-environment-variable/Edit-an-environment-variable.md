# Edit an environment variable
PATCH`https://api.vercel.com/v9/projects/{idOrName}/env/{id}`
Edit a specific environment variable for a given project by passing the environment variable identifier and either passing the project `id` or `name` in the URL.
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

  const result = await vercel.projects.editProjectEnv({






9

    idOrName: "prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA",






10

    id: "XMbOEya1gUUO1ir4",






11

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






12

    slug: "my-team-url-slug",






13

    requestBody: {






14

      key: "GITHUB_APP_ID",






15

      target: [






16

        "preview",






17

      ],






18

      gitBranch: "feature-1",






19

      type: "plain",






20

      value: "bkWIjbnxcvo78",






21

      customEnvironmentIds: [






22

        "env_1234567890",






23

      ],






24

      comment: "database connection string for production",






25

    },






26

  });






27







28

  console.log(result);






29

}






30







31

run();




```

Response
```


1

{






2

  "type": "secret",






3

  "value": "string",






4

  "edgeConfigId": "example_id",






5

  "edgeConfigTokenId": "example_id",






6

  "createdAt": "123",






7

  "updatedAt": "123",






8

  "id": "icfg_1234567890",






9

  "createdBy": "string",






10

  "target": [],






11

  "key": "string",






12

  "gitBranch": "string",






13

  "updatedBy": "string",






14

  "sunsetSecretId": "example_id",






15

  "legacyValue": "string",






16

  "decrypted": "false",






17

  "configurationId": "example_id",






18

  "contentHint": {






19

    "type": "redis-url",






20

    "storeId": "example_id"






21

  },






22

  "internalContentHint": {






23

    "type": "flags-secret",






24

    "encryptedValue": "string"






25

  },






26

  "comment": "string",






27

  "customEnvironmentIds": []






28

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/projects/retrieve-the-environment-variables-of-a-project-by-id-or-name#authentication)[](https://vercel.com/docs/rest-api/sdk/projects/retrieve-the-environment-variables-of-a-project-by-id-or-name#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/projects/retrieve-the-environment-variables-of-a-project-by-id-or-name#path-parameters)[](https://vercel.com/docs/rest-api/sdk/projects/retrieve-the-environment-variables-of-a-project-by-id-or-name#path-parameters)
idOrNamestringRequired
The unique project identifier or the project name
idstringRequired
The unique environment variable identifier
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/projects/retrieve-the-environment-variables-of-a-project-by-id-or-name#query-parameters)[](https://vercel.com/docs/rest-api/sdk/projects/retrieve-the-environment-variables-of-a-project-by-id-or-name#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Body](https://vercel.com/docs/rest-api/sdk/projects/retrieve-the-environment-variables-of-a-project-by-id-or-name#body)[](https://vercel.com/docs/rest-api/sdk/projects/retrieve-the-environment-variables-of-a-project-by-id-or-name#body)
application/json
keystringOptional
The name of the environment variable
targetarrayOptional
The target environment of the environment variable
gitBranchstringOptional
If defined, the git branch of the environment variable (must have target=preview)
typestringOptional
The type of environment variable
+Show 5 enum values
valuestringOptional
The value of the environment variable
customEnvironmentIdsarrayOptional
The custom environments that the environment variable should be synced to
commentstringOptional
A comment to add context on what this env var is for
##  [Response](https://vercel.com/docs/rest-api/sdk/projects/retrieve-the-environment-variables-of-a-project-by-id-or-name#response)[](https://vercel.com/docs/rest-api/sdk/projects/retrieve-the-environment-variables-of-a-project-by-id-or-name#response)
200The environment variable was successfully edited
typestringRequired
+Show 5 enum values
valuestringRequired
edgeConfigIdstringOptional
edgeConfigTokenIdstringOptional
createdAtnumberOptional
updatedAtnumberOptional
idstringOptional
createdBystringOptional
targetobjectOptional2 variants
+Show 2 variants
keystringRequired
gitBranchstringOptional
updatedBystringOptional
sunsetSecretIdstringOptional
This is used to identify variables that have been migrated from type secret to sensitive.
legacyValuestringOptional
Legacy now-encryption ciphertext, present after migration swaps value/vsmValue
decryptedbooleanOptional
+Show 2 enum values
configurationIdstringOptional
contentHintobjectOptional15 variants
+Show 15 variants
internalContentHintobjectOptional
Similar to `contentHints`, but should not be exposed to the user.
+Show 2 properties
commentstringOptional
customEnvironmentIdsarrayOptional
##  [Errors](https://vercel.com/docs/rest-api/sdk/projects/retrieve-the-environment-variables-of-a-project-by-id-or-name#errors)[](https://vercel.com/docs/rest-api/sdk/projects/retrieve-the-environment-variables-of-a-project-by-id-or-name#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid. At least one environment variable failed validation
401The request is not authorized.
403You do not have permission to access this resource.
404Error
409The project is being transferred and removing an environment variable is not possible
429Error
500Error
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

  const result = await vercel.projects.editProjectEnv({






9

    idOrName: "prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA",






10

    id: "XMbOEya1gUUO1ir4",






11

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






12

    slug: "my-team-url-slug",






13

    requestBody: {






14

      key: "GITHUB_APP_ID",






15

      target: [






16

        "preview",






17

      ],






18

      gitBranch: "feature-1",






19

      type: "plain",






20

      value: "bkWIjbnxcvo78",






21

      customEnvironmentIds: [






22

        "env_1234567890",






23

      ],






24

      comment: "database connection string for production",






25

    },






26

  });






27







28

  console.log(result);






29

}






30







31

run();




```

Response
```


1

{






2

  "type": "secret",






3

  "value": "string",






4

  "edgeConfigId": "example_id",






5

  "edgeConfigTokenId": "example_id",






6

  "createdAt": "123",






7

  "updatedAt": "123",






8

  "id": "icfg_1234567890",






9

  "createdBy": "string",






10

  "target": [],






11

  "key": "string",






12

  "gitBranch": "string",






13

  "updatedBy": "string",






14

  "sunsetSecretId": "example_id",






15

  "legacyValue": "string",






16

  "decrypted": "false",






17

  "configurationId": "example_id",






18

  "contentHint": {






19

    "type": "redis-url",






20

    "storeId": "example_id"






21

  },






22

  "internalContentHint": {






23

    "type": "flags-secret",






24

    "encryptedValue": "string"






25

  },






26

  "comment": "string",






27

  "customEnvironmentIds": []






28

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
