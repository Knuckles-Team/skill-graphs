# Read System Bypass
GET`https://api.vercel.com/v1/security/firewall/bypass`
Retrieve the system bypass rules configured for the specified project
TypeScriptNext.jscURL
https://api.vercel.com/v1/security/firewall/bypass
```


1

const response = await fetch('https://api.vercel.com/v1/security/firewall/bypass?projectId=string&limit=123&sourceIp=string&domain=string&projectScope=true&offset=string&teamId=string&slug=string', {






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

  "result": [






3

    {






4

      "OwnerId": "example_id",






5

      "Id": "icfg_1234567890",






6

      "Domain": "string",






7

      "Ip": "string",






8

      "Action": "bypass",






9

      "ProjectId": "example_id",






10

      "IsProjectRule": "false",






11

      "Note": "string",






12

      "CreatedAt": "string",






13

      "ActorId": "example_id",






14

      "UpdatedAt": "string",






15

      "UpdatedAtHour": "string",






16

      "DeletedAt": "string",






17

      "ExpiresAt": "123"






18

    }






19

  ],






20

  "pagination": {






21

    "OwnerId": "example_id",






22

    "Id": "icfg_1234567890"






23

  }






24

}




```

##  [Authentication](https://vercel.com/docs/rest-api/security/put-firewall-configuration#authentication)[](https://vercel.com/docs/rest-api/security/put-firewall-configuration#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Query parameters](https://vercel.com/docs/rest-api/security/put-firewall-configuration#query-parameters)[](https://vercel.com/docs/rest-api/security/put-firewall-configuration#query-parameters)
projectIdstringRequired
limitnumberOptional
sourceIpstringOptional
Filter by source IP
domainstringOptional
Filter by domain
projectScopebooleanOptional
Filter by project scoped rules
offsetstringOptional
Used for pagination. Retrieves results after the provided id
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/security/put-firewall-configuration#response)[](https://vercel.com/docs/rest-api/security/put-firewall-configuration#response)
200Success
resultarrayRequired
+Show 14 properties
paginationobjectOptional
+Show 2 properties
##  [Errors](https://vercel.com/docs/rest-api/security/put-firewall-configuration#errors)[](https://vercel.com/docs/rest-api/security/put-firewall-configuration#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
500Error
TypeScriptNext.jscURL
https://api.vercel.com/v1/security/firewall/bypass
```


1

const response = await fetch('https://api.vercel.com/v1/security/firewall/bypass?projectId=string&limit=123&sourceIp=string&domain=string&projectScope=true&offset=string&teamId=string&slug=string', {






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

  "result": [






3

    {






4

      "OwnerId": "example_id",






5

      "Id": "icfg_1234567890",






6

      "Domain": "string",






7

      "Ip": "string",






8

      "Action": "bypass",






9

      "ProjectId": "example_id",






10

      "IsProjectRule": "false",






11

      "Note": "string",






12

      "CreatedAt": "string",






13

      "ActorId": "example_id",






14

      "UpdatedAt": "string",






15

      "UpdatedAtHour": "string",






16

      "DeletedAt": "string",






17

      "ExpiresAt": "123"






18

    }






19

  ],






20

  "pagination": {






21

    "OwnerId": "example_id",






22

    "Id": "icfg_1234567890"






23

  }






24

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
