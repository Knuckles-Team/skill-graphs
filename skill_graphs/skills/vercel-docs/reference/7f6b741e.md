# Update network policy
POST`https://api.vercel.com/v1/sandboxes/{sandboxId}/network-policy`
Replaces the network access policy of a running sandbox. Use this to control which external hosts the sandbox can communicate with. This is a full replacement. Any previously configured network rules will be overwritten.
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

  const result = await vercel.sandboxes.updateNetworkPolicy({






9

    sandboxId: "sbx_abc123",






10

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






11

    slug: "my-team-url-slug",






12

    requestBody: {






13

      mode: "custom",






14

      allowedDomains: [






15

        "api.github.com",






16

        "*.npmjs.org",






17

      ],






18

      allowedCIDRs: [






19

        "35.192.0.0/12",






20

        "104.16.0.0/12",






21

      ],






22

      deniedCIDRs: [






23

        "35.192.0.0/12",






24

      ],






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

  "sandbox": {






3

    "id": "sbx_123a6c5209bc3778245d011443644c8d27dc2c50",






4

    "memory": "2048",






5

    "vcpus": "2",






6

    "region": "iad1",






7

    "runtime": "node22",






8

    "timeout": "3600000",






9

    "status": "running",






10

    "requestedAt": "1750344501629",






11

    "startedAt": "1750344501629",






12

    "cwd": "/vercel/sandbox",






13

    "requestedStopAt": "1750344501629",






14

    "stoppedAt": "1750344501629",






15

    "abortedAt": "1750344501629",






16

    "duration": "3600000",






17

    "sourceSnapshotId": "snap_123a6c5209bc3778245d011443644c8d27dc2c50",






18

    "snapshottedAt": "1750344501629",






19

    "createdAt": "1750344501629",






20

    "updatedAt": "1750344501629",






21

    "networkPolicy": {






22

      "mode": "custom",






23

      "allowedDomains": [],






24

      "allowedCIDRs": [],






25

      "deniedCIDRs": [],






26

      "injectionRules": [






27

        {






28

          "domain": "api.vercel.com",






29

          "headerNames": []






30

        }






31

      ]






32

    }






33

  }






34

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-sandbox#authentication)[](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-sandbox#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-sandbox#path-parameters)[](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-sandbox#path-parameters)
sandboxIdstringRequired
The unique identifier of the sandbox to update the network policy for.
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-sandbox#query-parameters)[](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-sandbox#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Body](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-sandbox#body)[](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-sandbox#body)
application/json
modestringRequired
The network access policy mode. Use "allow-all" to permit all outbound traffic. Use "deny-all" to block all outbound traffic. Use "custom" to specify explicit allow/deny rules.
+Show 5 enum values
allowedDomainsarrayOptional
List of domain names the sandbox is allowed to connect to. Only applies when mode is "custom". Supports wildcard patterns (e.g., "*.example.com" matches all subdomains).
allowedCIDRsarrayOptional
List of IP address ranges (in CIDR notation) the sandbox is allowed to connect to. Traffic to these addresses bypasses domain-based restrictions.
deniedCIDRsarrayOptional
List of IP address ranges (in CIDR notation) the sandbox is blocked from connecting to. These rules take precedence over all allowed rules.
##  [Response](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-sandbox#response)[](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-sandbox#response)
200The sandbox network policy was updated successfully.
sandboxobjectRequired
This object contains information related to a Vercel Sandbox.
+Show 19 properties
##  [Errors](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-sandbox#errors)[](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-sandbox#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid.
401The request is not authorized.
402Error
403You do not have permission to access this resource.
410The Sandbox has stopped execution and is no longer available.
422The Sandbox is creating a snapshot and will be stopped shortly. The Sandbox is stopping and is no longer available.
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

  const result = await vercel.sandboxes.updateNetworkPolicy({






9

    sandboxId: "sbx_abc123",






10

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






11

    slug: "my-team-url-slug",






12

    requestBody: {






13

      mode: "custom",






14

      allowedDomains: [






15

        "api.github.com",






16

        "*.npmjs.org",






17

      ],






18

      allowedCIDRs: [






19

        "35.192.0.0/12",






20

        "104.16.0.0/12",






21

      ],






22

      deniedCIDRs: [






23

        "35.192.0.0/12",






24

      ],






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

  "sandbox": {






3

    "id": "sbx_123a6c5209bc3778245d011443644c8d27dc2c50",






4

    "memory": "2048",






5

    "vcpus": "2",






6

    "region": "iad1",






7

    "runtime": "node22",






8

    "timeout": "3600000",






9

    "status": "running",






10

    "requestedAt": "1750344501629",






11

    "startedAt": "1750344501629",






12

    "cwd": "/vercel/sandbox",






13

    "requestedStopAt": "1750344501629",






14

    "stoppedAt": "1750344501629",






15

    "abortedAt": "1750344501629",






16

    "duration": "3600000",






17

    "sourceSnapshotId": "snap_123a6c5209bc3778245d011443644c8d27dc2c50",






18

    "snapshottedAt": "1750344501629",






19

    "createdAt": "1750344501629",






20

    "updatedAt": "1750344501629",






21

    "networkPolicy": {






22

      "mode": "custom",






23

      "allowedDomains": [],






24

      "allowedCIDRs": [],






25

      "deniedCIDRs": [],






26

      "injectionRules": [






27

        {






28

          "domain": "api.vercel.com",






29

          "headerNames": []






30

        }






31

      ]






32

    }






33

  }






34

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
