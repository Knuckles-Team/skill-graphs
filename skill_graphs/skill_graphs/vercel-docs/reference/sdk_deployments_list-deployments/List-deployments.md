# List deployments
GET`https://api.vercel.com/v6/deployments`
List deployments under the authenticated user or team. If a deployment hasn't finished uploading (is incomplete), the `url` property will have a value of `null`.
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

  const result = await vercel.deployments.getDeployments({






9

    app: "docs",






10

    from: 1612948664566,






11

    limit: 10,






12

    projectId: "QmXGTs7mvAMMC7WW5ebrM33qKG32QK3h4vmQMjmY",






13

    projectIds: [






14

      "prj_123",






15

      "prj_456",






16

    ],






17

    target: "production",






18

    to: 1612948664566,






19

    users: "kr1PsOIzqEL5Xg6M4VZcZosf,K4amb7K9dAt5R2vBJWF32bmY",






20

    since: 1540095775941,






21

    until: 1540095775951,






22

    state: "BUILDING,READY",






23

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






24

    slug: "my-team-url-slug",






25

  });






26







27

  console.log(result);






28

}






29







30

run();




```

Response
```


1

{






2

  "pagination": {






3

    "count": "20",






4

    "next": "1540095775951",






5

    "prev": "1540095775951"






6

  },






7

  "deployments": [






8

    {






9

      "uid": "dpl_2euZBFqxYdDMDG1jTrHFnNZ2eUVa",






10

      "name": "docs",






11

      "projectId": "example_id",






12

      "url": "docs-9jaeg38me.vercel.app",






13

      "created": "1609492210000",






14

      "defaultRoute": "/docs",






15

      "deleted": "1609492210000",






16

      "undeleted": "1609492210000",






17

      "softDeletedByRetention": "true",






18

      "source": "cli",






19

      "state": "READY",






20

      "readyState": "READY",






21

      "type": "LAMBDAS",






22

      "creator": {






23

        "uid": "eLrCnEgbKhsHyfbiNR7E8496",






24

        "email": "example@example.com",






25

        "username": "johndoe",






26

        "githubLogin": "johndoe",






27

        "gitlabLogin": "johndoe"






28

      },






29

      "meta": "value",






30

      "target": "production",






31

      "aliasError": {






32

        "code": "string",






33

        "message": "string"






34

      },






35

      "aliasAssigned": "123",






36

      "createdAt": "1609492210000",






37

      "buildingAt": "1609492210000",






38

      "ready": "1609492210000",






39

      "readySubstate": "STAGED",






40

      "checksState": "registered",






41

      "checksConclusion": "succeeded",






42

      "checks": {






43

        "deployment-alias": {






44

          "state": "succeeded",






45

          "startedAt": "123",






46

          "completedAt": "123"






47

        }






48

      },






49

      "inspectorUrl": "https://vercel.com/acme/nextjs/J1hXN00qjUeoYfpEEf7dnDtpSiVq",






50

      "errorCode": "BUILD_FAILED",






51

      "errorMessage": "The Deployment has been canceled because this project was not affected",






52

      "oomReport": "out-of-memory",






53

      "isRollbackCandidate": "false",






54

      "prebuilt": "false",






55

      "projectSettings": {






56

        "framework": "blitzjs",






57

        "gitForkProtection": "false",






58

        "customerSupportCodeVisibility": "false",






59

        "gitLFS": "false",






60

        "devCommand": "string",






61

        "installCommand": "string",






62

        "buildCommand": "string",






63

        "nodeVersion": "24.x",






64

        "outputDirectory": "string",






65

        "publicSource": "false",






66

        "rootDirectory": "string",






67

        "sourceFilesOutsideRootDirectory": "false",






68

        "commandForIgnoringBuildStep": "string",






69

        "createdAt": "123",






70

        "speedInsights": {






71

          "id": "icfg_1234567890",






72

          "enabledAt": "123",






73

          "disabledAt": "123",






74

          "canceledAt": "123",






75

          "hasData": "false",






76

          "paidAt": "123"






77

        },






78

        "webAnalytics": {






79

          "id": "icfg_1234567890",






80

          "disabledAt": "123",






81

          "canceledAt": "123",






82

          "enabledAt": "123",






83

          "hasData": "true"






84

        },






85

        "skipGitConnectDuringLink": "false",






86

        "gitComments": {






87

          "onPullRequest": "false",






88

          "onCommit": "false"






89

        }






90

      },






91

      "connectBuildsEnabled": "false",






92

      "connectConfigurationId": "example_id",






93

      "passiveConnectConfigurationId": "example_id",






94

      "expiration": "123",






95

      "proposedExpiration": "123",






96

      "platform": {






97

        "source": {






98

          "name": "Example Name"






99

        },






100

        "origin": {






101

          "type": "url",






102

          "value": "string"






103

        },






104

        "creator": {






105

          "name": "Example Name",






106

          "avatar": "string"






107

        },






108

        "meta": "value"






109

      },






110

      "customEnvironment": {






111

        "id": "icfg_1234567890",






112

        "slug": "string"






113

      },






114

      "seatBlock": {






115

        "blockCode": "TEAM_ACCESS_REQUIRED",






116

        "userId": "example_id",






117

        "isVerified": "false"






118

      }






119

    }






120

  ]






121

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/deployments/create-a-new-deployment#authentication)[](https://vercel.com/docs/rest-api/sdk/deployments/create-a-new-deployment#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/deployments/create-a-new-deployment#query-parameters)[](https://vercel.com/docs/rest-api/sdk/deployments/create-a-new-deployment#query-parameters)
appstringOptional
Name of the deployment.
fromnumberOptionalDeprecated
Gets the deployment created after this Date timestamp. (default: current time)
limitnumberOptional
Maximum number of deployments to list from a request.
projectIdstringOptional
Filter deployments from the given ID or name.
projectIdsarrayOptional
Filter deployments from the given project IDs. Cannot be used when projectId is specified.
targetstringOptional
Filter deployments based on the environment.
tonumberOptionalDeprecated
Gets the deployment created before this Date timestamp. (default: current time)
usersstringOptional
Filter out deployments based on users who have created the deployment.
sincenumberOptional
Get Deployments created after this JavaScript timestamp.
untilnumberOptional
Get Deployments created before this JavaScript timestamp.
statestringOptional
Filter deployments based on their state (`BUILDING`, `ERROR`, `INITIALIZING`, `QUEUED`, `READY`, `CANCELED`)
rollbackCandidatebooleanOptional
Filter deployments based on their rollback candidacy
branchstringOptional
Filter deployments based on the branch name
shastringOptional
Filter deployments based on the SHA
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sdk/deployments/create-a-new-deployment#response)[](https://vercel.com/docs/rest-api/sdk/deployments/create-a-new-deployment#response)
200Success
paginationobjectRequired
This object contains information related to the pagination of the current request, including the necessary parameters to get the next or previous page of data.
+Show 3 properties
deploymentsarrayRequired
+Show 40 properties
##  [Errors](https://vercel.com/docs/rest-api/sdk/deployments/create-a-new-deployment#errors)[](https://vercel.com/docs/rest-api/sdk/deployments/create-a-new-deployment#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
422Error
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

  const result = await vercel.deployments.getDeployments({






9

    app: "docs",






10

    from: 1612948664566,






11

    limit: 10,






12

    projectId: "QmXGTs7mvAMMC7WW5ebrM33qKG32QK3h4vmQMjmY",






13

    projectIds: [






14

      "prj_123",






15

      "prj_456",






16

    ],






17

    target: "production",






18

    to: 1612948664566,






19

    users: "kr1PsOIzqEL5Xg6M4VZcZosf,K4amb7K9dAt5R2vBJWF32bmY",






20

    since: 1540095775941,






21

    until: 1540095775951,






22

    state: "BUILDING,READY",






23

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






24

    slug: "my-team-url-slug",






25

  });






26







27

  console.log(result);






28

}






29







30

run();




```

Response
```


1

{






2

  "pagination": {






3

    "count": "20",






4

    "next": "1540095775951",






5

    "prev": "1540095775951"






6

  },






7

  "deployments": [






8

    {






9

      "uid": "dpl_2euZBFqxYdDMDG1jTrHFnNZ2eUVa",






10

      "name": "docs",






11

      "projectId": "example_id",






12

      "url": "docs-9jaeg38me.vercel.app",






13

      "created": "1609492210000",






14

      "defaultRoute": "/docs",






15

      "deleted": "1609492210000",






16

      "undeleted": "1609492210000",






17

      "softDeletedByRetention": "true",






18

      "source": "cli",






19

      "state": "READY",






20

      "readyState": "READY",






21

      "type": "LAMBDAS",






22

      "creator": {






23

        "uid": "eLrCnEgbKhsHyfbiNR7E8496",






24

        "email": "example@example.com",






25

        "username": "johndoe",






26

        "githubLogin": "johndoe",






27

        "gitlabLogin": "johndoe"






28

      },






29

      "meta": "value",






30

      "target": "production",






31

      "aliasError": {






32

        "code": "string",






33

        "message": "string"






34

      },






35

      "aliasAssigned": "123",






36

      "createdAt": "1609492210000",






37

      "buildingAt": "1609492210000",






38

      "ready": "1609492210000",






39

      "readySubstate": "STAGED",






40

      "checksState": "registered",






41

      "checksConclusion": "succeeded",






42

      "checks": {






43

        "deployment-alias": {






44

          "state": "succeeded",






45

          "startedAt": "123",






46

          "completedAt": "123"






47

        }






48

      },






49

      "inspectorUrl": "https://vercel.com/acme/nextjs/J1hXN00qjUeoYfpEEf7dnDtpSiVq",






50

      "errorCode": "BUILD_FAILED",






51

      "errorMessage": "The Deployment has been canceled because this project was not affected",






52

      "oomReport": "out-of-memory",






53

      "isRollbackCandidate": "false",






54

      "prebuilt": "false",






55

      "projectSettings": {






56

        "framework": "blitzjs",






57

        "gitForkProtection": "false",






58

        "customerSupportCodeVisibility": "false",






59

        "gitLFS": "false",






60

        "devCommand": "string",






61

        "installCommand": "string",






62

        "buildCommand": "string",






63

        "nodeVersion": "24.x",






64

        "outputDirectory": "string",






65

        "publicSource": "false",






66

        "rootDirectory": "string",






67

        "sourceFilesOutsideRootDirectory": "false",






68

        "commandForIgnoringBuildStep": "string",






69

        "createdAt": "123",






70

        "speedInsights": {






71

          "id": "icfg_1234567890",






72

          "enabledAt": "123",






73

          "disabledAt": "123",






74

          "canceledAt": "123",






75

          "hasData": "false",






76

          "paidAt": "123"






77

        },






78

        "webAnalytics": {






79

          "id": "icfg_1234567890",






80

          "disabledAt": "123",






81

          "canceledAt": "123",






82

          "enabledAt": "123",






83

          "hasData": "true"






84

        },






85

        "skipGitConnectDuringLink": "false",






86

        "gitComments": {






87

          "onPullRequest": "false",






88

          "onCommit": "false"






89

        }






90

      },






91

      "connectBuildsEnabled": "false",






92

      "connectConfigurationId": "example_id",






93

      "passiveConnectConfigurationId": "example_id",






94

      "expiration": "123",






95

      "proposedExpiration": "123",






96

      "platform": {






97

        "source": {






98

          "name": "Example Name"






99

        },






100

        "origin": {






101

          "type": "url",






102

          "value": "string"






103

        },






104

        "creator": {






105

          "name": "Example Name",






106

          "avatar": "string"






107

        },






108

        "meta": "value"






109

      },






110

      "customEnvironment": {






111

        "id": "icfg_1234567890",






112

        "slug": "string"






113

      },






114

      "seatBlock": {






115

        "blockCode": "TEAM_ACCESS_REQUIRED",






116

        "userId": "example_id",






117

        "isVerified": "false"






118

      }






119

    }






120

  ]






121

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
