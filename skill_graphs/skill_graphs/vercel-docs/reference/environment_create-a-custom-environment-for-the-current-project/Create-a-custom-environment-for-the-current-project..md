# Create a custom environment for the current project.
POST`https://api.vercel.com/v9/projects/{idOrName}/custom-environments`
Creates a custom environment for the current project. Cannot be named 'Production' or 'Preview'.
TypeScriptNext.jscURL
https://api.vercel.com/v9/projects/{idOrName}/custom-environments
```


1

const response = await fetch('https://api.vercel.com/v9/projects/idOrName/custom-environments?teamId=string&slug=string', {






2

  method: 'POST',






3

  headers: {






4

    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',






5

    'Content-Type': 'application/json',






6

  },






7

  body: JSON.stringify({






8

    "slug": "string",






9

    "description": "string",






10

    "branchMatcher": {






11

      "type": "equals",






12

      "pattern": "string"






13

    },






14

    "copyEnvVarsFrom": "string"






15

  }),






16

});






17







18

const data = await response.json();






19

console.log(data);




```

Response
```


1

{






2

  "id": "icfg_1234567890",






3

  "slug": "string",






4

  "type": "production",






5

  "description": "string",






6

  "branchMatcher": {






7

    "type": "endsWith",






8

    "pattern": "string"






9

  },






10

  "domains": [






11

    {






12

      "name": "Example Name",






13

      "apexName": "Example Name",






14

      "projectId": "example_id",






15

      "redirect": "string",






16

      "redirectStatusCode": "301",






17

      "gitBranch": "string",






18

      "customEnvironmentId": "example_id",






19

      "updatedAt": "123",






20

      "createdAt": "123",






21

      "verified": "false",






22

      "verification": [






23

        {






24

          "type": "string",






25

          "domain": "string",






26

          "value": "string",






27

          "reason": "Customer requested refund"






28

        }






29

      ]






30

    }






31

  ],






32

  "currentDeploymentAliases": [],






33

  "createdAt": "123",






34

  "updatedAt": "123"






35

}




```

##  [Authentication](https://vercel.com/docs/rest-api/environment/retrieve-the-decrypted-value-of-a-shared-environment-variable-by-id#authentication)[](https://vercel.com/docs/rest-api/environment/retrieve-the-decrypted-value-of-a-shared-environment-variable-by-id#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/environment/retrieve-the-decrypted-value-of-a-shared-environment-variable-by-id#path-parameters)[](https://vercel.com/docs/rest-api/environment/retrieve-the-decrypted-value-of-a-shared-environment-variable-by-id#path-parameters)
idOrNamestringRequired
The unique project identifier or the project name
##  [Query parameters](https://vercel.com/docs/rest-api/environment/retrieve-the-decrypted-value-of-a-shared-environment-variable-by-id#query-parameters)[](https://vercel.com/docs/rest-api/environment/retrieve-the-decrypted-value-of-a-shared-environment-variable-by-id#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Body](https://vercel.com/docs/rest-api/environment/retrieve-the-decrypted-value-of-a-shared-environment-variable-by-id#body)[](https://vercel.com/docs/rest-api/environment/retrieve-the-decrypted-value-of-a-shared-environment-variable-by-id#body)
application/json
slugstringOptional
The slug of the custom environment to create.
descriptionstringOptional
Description of the custom environment. This is optional.
branchMatcherobjectOptional
How we want to determine a matching branch. This is optional.
+Show 2 properties
copyEnvVarsFromstringOptional
Where to copy environment variables from. This is optional.
##  [Response](https://vercel.com/docs/rest-api/environment/retrieve-the-decrypted-value-of-a-shared-environment-variable-by-id#response)[](https://vercel.com/docs/rest-api/environment/retrieve-the-decrypted-value-of-a-shared-environment-variable-by-id#response)
201Success
idstringRequired
Unique identifier for the custom environment (format: env_*)
slugstringRequired
URL-friendly name of the environment
typestringRequired
The type of environment (production, preview, or development)
+Show 3 enum values
descriptionstringOptional
Optional description of the environment's purpose
branchMatcherobjectOptional
Configuration for matching git branches to this environment
+Show 2 properties
domainsarrayOptional
List of domains associated with this environment
+Show 11 properties
currentDeploymentAliasesarrayOptional
List of aliases for the current deployment
createdAtnumberRequired
Timestamp when the environment was created
updatedAtnumberRequired
Timestamp when the environment was last updated
##  [Errors](https://vercel.com/docs/rest-api/environment/retrieve-the-decrypted-value-of-a-shared-environment-variable-by-id#errors)[](https://vercel.com/docs/rest-api/environment/retrieve-the-decrypted-value-of-a-shared-environment-variable-by-id#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid.
401The request is not authorized.
402The account was soft-blocked for an unhandled reason. The account is missing a payment so payment method must be updated
403You do not have permission to access this resource.
500Error
TypeScriptNext.jscURL
https://api.vercel.com/v9/projects/{idOrName}/custom-environments
```


1

const response = await fetch('https://api.vercel.com/v9/projects/idOrName/custom-environments?teamId=string&slug=string', {






2

  method: 'POST',






3

  headers: {






4

    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',






5

    'Content-Type': 'application/json',






6

  },






7

  body: JSON.stringify({






8

    "slug": "string",






9

    "description": "string",






10

    "branchMatcher": {






11

      "type": "equals",






12

      "pattern": "string"






13

    },






14

    "copyEnvVarsFrom": "string"






15

  }),






16

});






17







18

const data = await response.json();






19

console.log(data);




```

Response
```


1

{






2

  "id": "icfg_1234567890",






3

  "slug": "string",






4

  "type": "production",






5

  "description": "string",






6

  "branchMatcher": {






7

    "type": "endsWith",






8

    "pattern": "string"






9

  },






10

  "domains": [






11

    {






12

      "name": "Example Name",






13

      "apexName": "Example Name",






14

      "projectId": "example_id",






15

      "redirect": "string",






16

      "redirectStatusCode": "301",






17

      "gitBranch": "string",






18

      "customEnvironmentId": "example_id",






19

      "updatedAt": "123",






20

      "createdAt": "123",






21

      "verified": "false",






22

      "verification": [






23

        {






24

          "type": "string",






25

          "domain": "string",






26

          "value": "string",






27

          "reason": "Customer requested refund"






28

        }






29

      ]






30

    }






31

  ],






32

  "currentDeploymentAliases": [],






33

  "createdAt": "123",






34

  "updatedAt": "123"






35

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
