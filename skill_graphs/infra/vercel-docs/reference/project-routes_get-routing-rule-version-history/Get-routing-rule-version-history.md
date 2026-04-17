# Get routing rule version history
GET`https://api.vercel.com/v1/projects/{projectId}/routes/versions`
Get the version history for a project's routing rules. Returns the staging version (if one exists) followed by production versions, most recent first. The staging version has `isStaging: true` and the current production version has `isLive: true`.
TypeScriptNext.jscURL
https://api.vercel.com/v1/projects/{projectId}/routes/versions
```


1

const response = await fetch('https://api.vercel.com/v1/projects/projectId/routes/versions?teamId=string&slug=string', {






2

  method: 'GET',






3

  headers: {






4

    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',






5

    'Content-Type': 'application/json',






6

  },






7

});






8







9

const data = await response.json();






10

console.log(data);




```

Response
```


1

{






2

  "versions": [






3

    {






4

      "id": "icfg_1234567890",






5

      "s3Key": "string",






6

      "lastModified": "123",






7

      "createdBy": "string",






8

      "isStaging": "false",






9

      "isLive": "false",






10

      "ruleCount": "123",






11

      "alias": "string"






12

    }






13

  ]






14

}




```

##  [Authentication](https://vercel.com/docs/rest-api/project-routes/add-a-routing-rule#authentication)[](https://vercel.com/docs/rest-api/project-routes/add-a-routing-rule#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/project-routes/add-a-routing-rule#path-parameters)[](https://vercel.com/docs/rest-api/project-routes/add-a-routing-rule#path-parameters)
projectIdstringRequired
##  [Query parameters](https://vercel.com/docs/rest-api/project-routes/add-a-routing-rule#query-parameters)[](https://vercel.com/docs/rest-api/project-routes/add-a-routing-rule#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/project-routes/add-a-routing-rule#response)[](https://vercel.com/docs/rest-api/project-routes/add-a-routing-rule#response)
200Success
versionsarrayRequired
+Show 8 properties
##  [Errors](https://vercel.com/docs/rest-api/project-routes/add-a-routing-rule#errors)[](https://vercel.com/docs/rest-api/project-routes/add-a-routing-rule#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
TypeScriptNext.jscURL
https://api.vercel.com/v1/projects/{projectId}/routes/versions
```


1

const response = await fetch('https://api.vercel.com/v1/projects/projectId/routes/versions?teamId=string&slug=string', {






2

  method: 'GET',






3

  headers: {






4

    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',






5

    'Content-Type': 'application/json',






6

  },






7

});






8







9

const data = await response.json();






10

console.log(data);




```

Response
```


1

{






2

  "versions": [






3

    {






4

      "id": "icfg_1234567890",






5

      "s3Key": "string",






6

      "lastModified": "123",






7

      "createdBy": "string",






8

      "isStaging": "false",






9

      "isLive": "false",






10

      "ruleCount": "123",






11

      "alias": "string"






12

    }






13

  ]






14

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
