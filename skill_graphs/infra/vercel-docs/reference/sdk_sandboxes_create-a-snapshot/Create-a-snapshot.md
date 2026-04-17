# Create a snapshot
POST`https://api.vercel.com/v1/sandboxes/{sandboxId}/snapshot`
Creates a point-in-time snapshot of a running sandbox's filesystem. Snapshots can be used to quickly restore a sandbox to a previous state or to create new sandboxes with pre-configured environments. The sandbox must be running and able to accept commands for a snapshot to be created. The sandbox will be terminated after the snapshot is created.
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

  const result = await vercel.sandboxes.createSnapshot({






9

    sandboxId: "sbx_abc123",






10

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






11

    slug: "my-team-url-slug",






12

  });






13







14

  console.log(result);






15

}






16







17

run();




```

Response
```


1

{






2

  "snapshot": {






3

    "id": "snap_123a6c5209bc3778245d011443644c8d27dc2c50",






4

    "sourceSandboxId": "sbx_123a6c5209bc3778245d011443644c8d27dc2c50",






5

    "region": "iad1",






6

    "status": "created",






7

    "sizeBytes": "104857600",






8

    "expiresAt": "1750344501629",






9

    "createdAt": "1750344501629",






10

    "updatedAt": "1750344501629"






11

  },






12

  "sandbox": {






13

    "id": "sbx_123a6c5209bc3778245d011443644c8d27dc2c50",






14

    "memory": "2048",






15

    "vcpus": "2",






16

    "region": "iad1",






17

    "runtime": "node22",






18

    "timeout": "3600000",






19

    "status": "running",






20

    "requestedAt": "1750344501629",






21

    "startedAt": "1750344501629",






22

    "cwd": "/vercel/sandbox",






23

    "requestedStopAt": "1750344501629",






24

    "stoppedAt": "1750344501629",






25

    "abortedAt": "1750344501629",






26

    "duration": "3600000",






27

    "sourceSnapshotId": "snap_123a6c5209bc3778245d011443644c8d27dc2c50",






28

    "snapshottedAt": "1750344501629",






29

    "createdAt": "1750344501629",






30

    "updatedAt": "1750344501629",






31

    "networkPolicy": {






32

      "mode": "custom",






33

      "allowedDomains": [],






34

      "allowedCIDRs": [],






35

      "deniedCIDRs": [],






36

      "injectionRules": [






37

        {






38

          "domain": "api.vercel.com",






39

          "headerNames": []






40

        }






41

      ]






42

    }






43

  }






44

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-command#authentication)[](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-command#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-command#path-parameters)[](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-command#path-parameters)
sandboxIdstringRequired
The unique identifier of the sandbox to snapshot.
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-command#query-parameters)[](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-command#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Body](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-command#body)[](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-command#body)
application/json
expirationintegerOptional
The number of milliseconds after which the snapshot will expire and be deleted. Use 0 for no expiration.
##  [Response](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-command#response)[](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-command#response)
201Success
snapshotobjectRequired
This object contains information related to a Snapshot of a Vercel Sandbox.
+Show 8 properties
sandboxobjectRequired
This object contains information related to a Vercel Sandbox.
+Show 19 properties
##  [Errors](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-command#errors)[](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-command#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid.
401The request is not authorized.
402The account was soft-blocked for an unhandled reason. The account is missing a payment so payment method must be updated
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

  const result = await vercel.sandboxes.createSnapshot({






9

    sandboxId: "sbx_abc123",






10

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






11

    slug: "my-team-url-slug",






12

  });






13







14

  console.log(result);






15

}






16







17

run();




```

Response
```


1

{






2

  "snapshot": {






3

    "id": "snap_123a6c5209bc3778245d011443644c8d27dc2c50",






4

    "sourceSandboxId": "sbx_123a6c5209bc3778245d011443644c8d27dc2c50",






5

    "region": "iad1",






6

    "status": "created",






7

    "sizeBytes": "104857600",






8

    "expiresAt": "1750344501629",






9

    "createdAt": "1750344501629",






10

    "updatedAt": "1750344501629"






11

  },






12

  "sandbox": {






13

    "id": "sbx_123a6c5209bc3778245d011443644c8d27dc2c50",






14

    "memory": "2048",






15

    "vcpus": "2",






16

    "region": "iad1",






17

    "runtime": "node22",






18

    "timeout": "3600000",






19

    "status": "running",






20

    "requestedAt": "1750344501629",






21

    "startedAt": "1750344501629",






22

    "cwd": "/vercel/sandbox",






23

    "requestedStopAt": "1750344501629",






24

    "stoppedAt": "1750344501629",






25

    "abortedAt": "1750344501629",






26

    "duration": "3600000",






27

    "sourceSnapshotId": "snap_123a6c5209bc3778245d011443644c8d27dc2c50",






28

    "snapshottedAt": "1750344501629",






29

    "createdAt": "1750344501629",






30

    "updatedAt": "1750344501629",






31

    "networkPolicy": {






32

      "mode": "custom",






33

      "allowedDomains": [],






34

      "allowedCIDRs": [],






35

      "deniedCIDRs": [],






36

      "injectionRules": [






37

        {






38

          "domain": "api.vercel.com",






39

          "headerNames": []






40

        }






41

      ]






42

    }






43

  }






44

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
