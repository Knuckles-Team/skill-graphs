# Update the active rolling release to the next stage for a project
POST`https://api.vercel.com/v1/projects/{idOrName}/rolling-release/approve-stage`
Advance a rollout to the next stage. This is only needed when rolling releases is configured to require manual approval.
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

  const result = await vercel.rollingRelease.approveRollingReleaseStage({






9

    idOrName: "<value>",






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

  "rollingRelease": {






3

    "state": "ACTIVE",






4

    "currentDeployment": {






5

      "name": "my-project",






6

      "createdAt": "1540257589405",






7

      "id": "dpl_89qyp1cskzkLrVicDaZoDbjyHuDJ",






8

      "readyState": "READY",






9

      "readyStateAt": "123",






10

      "source": "cli",






11

      "target": "null",






12

      "url": "my-instant-deployment-3ij3cxz9qr.now.sh"






13

    },






14

    "canaryDeployment": {






15

      "name": "my-project",






16

      "createdAt": "1540257589405",






17

      "id": "dpl_89qyp1cskzkLrVicDaZoDbjyHuDJ",






18

      "readyState": "READY",






19

      "readyStateAt": "123",






20

      "source": "cli",






21

      "target": "null",






22

      "url": "my-instant-deployment-3ij3cxz9qr.now.sh"






23

    },






24

    "queuedDeploymentId": "dpl_ghi789",






25

    "advancementType": "manual-approval",






26

    "stages": [






27

      {






28

        "index": "0",






29

        "isFinalStage": "false",






30

        "targetPercentage": "25",






31

        "requireApproval": "false",






32

        "duration": "null",






33

        "linearShift": "false"






34

      }






35

    ],






36

    "activeStage": {






37

      "index": "0",






38

      "isFinalStage": "false",






39

      "targetPercentage": "25",






40

      "requireApproval": "false",






41

      "duration": "null",






42

      "linearShift": "false"






43

    },






44

    "nextStage": {






45

      "index": "0",






46

      "isFinalStage": "false",






47

      "targetPercentage": "25",






48

      "requireApproval": "false",






49

      "duration": "null",






50

      "linearShift": "false"






51

    },






52

    "startedAt": "1716210500000",






53

    "updatedAt": "1716210600000"






54

  }






55

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/rolling-release/update-the-rolling-release-settings-for-the-project#authentication)[](https://vercel.com/docs/rest-api/sdk/rolling-release/update-the-rolling-release-settings-for-the-project#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/rolling-release/update-the-rolling-release-settings-for-the-project#path-parameters)[](https://vercel.com/docs/rest-api/sdk/rolling-release/update-the-rolling-release-settings-for-the-project#path-parameters)
idOrNamestringRequired
Project ID or project name (URL-encoded)
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/rolling-release/update-the-rolling-release-settings-for-the-project#query-parameters)[](https://vercel.com/docs/rest-api/sdk/rolling-release/update-the-rolling-release-settings-for-the-project#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Body](https://vercel.com/docs/rest-api/sdk/rolling-release/update-the-rolling-release-settings-for-the-project#body)[](https://vercel.com/docs/rest-api/sdk/rolling-release/update-the-rolling-release-settings-for-the-project#body)
application/json
nextStageIndexnumberRequired
The index of the stage to transition to
canaryDeploymentIdstringRequired
The id of the canary deployment to approve for the next stage
##  [Response](https://vercel.com/docs/rest-api/sdk/rolling-release/update-the-rolling-release-settings-for-the-project#response)[](https://vercel.com/docs/rest-api/sdk/rolling-release/update-the-rolling-release-settings-for-the-project#response)
200Success
rollingReleaseobjectRequired
Rolling release information including configuration and document details, or null if no rolling release exists
+Show 10 properties
##  [Errors](https://vercel.com/docs/rest-api/sdk/rolling-release/update-the-rolling-release-settings-for-the-project#errors)[](https://vercel.com/docs/rest-api/sdk/rolling-release/update-the-rolling-release-settings-for-the-project#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
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

  const result = await vercel.rollingRelease.approveRollingReleaseStage({






9

    idOrName: "<value>",






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

  "rollingRelease": {






3

    "state": "ACTIVE",






4

    "currentDeployment": {






5

      "name": "my-project",






6

      "createdAt": "1540257589405",






7

      "id": "dpl_89qyp1cskzkLrVicDaZoDbjyHuDJ",






8

      "readyState": "READY",






9

      "readyStateAt": "123",






10

      "source": "cli",






11

      "target": "null",






12

      "url": "my-instant-deployment-3ij3cxz9qr.now.sh"






13

    },






14

    "canaryDeployment": {






15

      "name": "my-project",






16

      "createdAt": "1540257589405",






17

      "id": "dpl_89qyp1cskzkLrVicDaZoDbjyHuDJ",






18

      "readyState": "READY",






19

      "readyStateAt": "123",






20

      "source": "cli",






21

      "target": "null",






22

      "url": "my-instant-deployment-3ij3cxz9qr.now.sh"






23

    },






24

    "queuedDeploymentId": "dpl_ghi789",






25

    "advancementType": "manual-approval",






26

    "stages": [






27

      {






28

        "index": "0",






29

        "isFinalStage": "false",






30

        "targetPercentage": "25",






31

        "requireApproval": "false",






32

        "duration": "null",






33

        "linearShift": "false"






34

      }






35

    ],






36

    "activeStage": {






37

      "index": "0",






38

      "isFinalStage": "false",






39

      "targetPercentage": "25",






40

      "requireApproval": "false",






41

      "duration": "null",






42

      "linearShift": "false"






43

    },






44

    "nextStage": {






45

      "index": "0",






46

      "isFinalStage": "false",






47

      "targetPercentage": "25",






48

      "requireApproval": "false",






49

      "duration": "null",






50

      "linearShift": "false"






51

    },






52

    "startedAt": "1716210500000",






53

    "updatedAt": "1716210600000"






54

  }






55

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
