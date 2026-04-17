# List all teams
GET`https://api.vercel.com/v2/teams`
Get a paginated list of all the Teams the authenticated User is a member of.
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

  const result = await vercel.teams.getTeams({






9

    limit: 20,






10

    since: 1540095775951,






11

    until: 1540095775951,






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

  "teams": [






3

    {






4

      "connect": {






5

        "enabled": "false"






6

      },






7

      "creatorId": "R6efeCJQ2HKXywuasPDc0fOWB",






8

      "updatedAt": "1611796915677",






9

      "emailDomain": "example.com",






10

      "saml": {






11

        "connection": {






12

          "type": "OktaSAML",






13

          "status": "linked",






14

          "state": "active",






15

          "connectedAt": "1611796915677",






16

          "lastReceivedWebhookEvent": "1611796915677",






17

          "lastSyncedAt": "1611796915677",






18

          "syncState": "SETUP"






19

        },






20

        "directory": {






21

          "type": "OktaSAML",






22

          "state": "active",






23

          "connectedAt": "1611796915677",






24

          "lastReceivedWebhookEvent": "1611796915677",






25

          "lastSyncedAt": "1611796915677",






26

          "syncState": "SETUP"






27

        },






28

        "enforced": "false",






29

        "defaultRedirectUri": "vercel.com",






30

        "roles": "value"






31

      },






32

      "inviteCode": "hasihf9e89",






33

      "description": "Our mission is to make cloud computing accessible to everyone.",






34

      "defaultRoles": {






35

        "teamRoles": [],






36

        "teamPermissions": []






37

      },






38

      "stagingPrefix": "string",






39

      "resourceConfig": {






40

        "concurrentBuilds": "123",






41

        "elasticConcurrencyEnabled": "false",






42

        "edgeConfigSize": "123",






43

        "edgeConfigs": "123",






44

        "kvDatabases": "123",






45

        "blobStores": "123",






46

        "postgresDatabases": "123",






47

        "buildEntitlements": {






48

          "enhancedBuilds": "false"






49

        },






50

        "buildMachine": {






51

          "default": "enhanced"






52

        }






53

      },






54

      "previewDeploymentSuffix": "example.dev",






55

      "platform": "true",






56

      "disableHardAutoBlocks": "123",






57

      "remoteCaching": {






58

        "enabled": "false"






59

      },






60

      "defaultDeploymentProtection": {






61

        "passwordProtection": {






62

          "deploymentType": "string"






63

        },






64

        "ssoProtection": {






65

          "deploymentType": "string"






66

        }






67

      },






68

      "defaultExpirationSettings": {






69

        "expirationDays": "123",






70

        "expirationDaysProduction": "123",






71

        "expirationDaysCanceled": "123",






72

        "expirationDaysErrored": "123",






73

        "deploymentsToKeep": "123"






74

      },






75

      "enablePreviewFeedback": "default",






76

      "enableProductionFeedback": "default",






77

      "sensitiveEnvironmentVariablePolicy": "default",






78

      "hideIpAddresses": "false",






79

      "hideIpAddressesInLogDrains": "false",






80

      "ipBuckets": [






81

        {






82

          "bucket": "string",






83

          "supportUntil": "123"






84

        }






85

      ],






86

      "strictDeploymentProtectionSettings": {






87

        "enabled": "false",






88

        "updatedAt": "123"






89

      },






90

      "nsnbConfig": {






91

        "preference": "auto-approval"






92

      },






93

      "id": "team_nllPyCtREAqxxdyFKbbMDlxd",






94

      "slug": "my-team",






95

      "name": "My Team",






96

      "avatar": "6eb07268bcfadd309905ffb1579354084c24655c",






97

      "membership": {






98

        "uid": "example_id",






99

        "entitlements": [






100

          {






101

            "entitlement": "string"






102

          }






103

        ],






104

        "teamId": "example_id",






105

        "confirmed": "true",






106

        "accessRequestedAt": "123",






107

        "role": "OWNER",






108

        "teamRoles": [],






109

        "teamPermissions": [],






110

        "createdAt": "123",






111

        "created": "123",






112

        "joinedFrom": {






113

          "origin": "link",






114

          "commitId": "example_id",






115

          "repoId": "example_id",






116

          "repoPath": "string",






117

          "gitUserId": "example_id",






118

          "gitUserLogin": "string",






119

          "ssoUserId": "example_id",






120

          "ssoConnectedAt": "123",






121

          "idpUserId": "example_id",






122

          "dsyncUserId": "example_id",






123

          "dsyncConnectedAt": "123"






124

        }






125

      },






126

      "createdAt": "1630748523395"






127

    }






128

  ],






129

  "pagination": {






130

    "count": "20",






131

    "next": "1540095775951",






132

    "prev": "1540095775951"






133

  }






134

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/teams/list-all-teams#authentication)[](https://vercel.com/docs/rest-api/sdk/teams/list-all-teams#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/teams/list-all-teams#query-parameters)[](https://vercel.com/docs/rest-api/sdk/teams/list-all-teams#query-parameters)
limitnumberOptional
Maximum number of Teams which may be returned.
sincenumberOptional
Timestamp (in milliseconds) to only include Teams created since then.
untilnumberOptional
Timestamp (in milliseconds) to only include Teams created until then.
##  [Response](https://vercel.com/docs/rest-api/sdk/teams/list-all-teams#response)[](https://vercel.com/docs/rest-api/sdk/teams/list-all-teams#response)
200A paginated list of teams.
teamsarrayRequired
+Show 30 properties
paginationobjectRequired
This object contains information related to the pagination of the current request, including the necessary parameters to get the next or previous page of data.
+Show 3 properties
##  [Errors](https://vercel.com/docs/rest-api/sdk/teams/list-all-teams#errors)[](https://vercel.com/docs/rest-api/sdk/teams/list-all-teams#errors)
400One of the provided values in the request query is invalid.
401Error
403You do not have permission to access this resource.
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

  const result = await vercel.teams.getTeams({






9

    limit: 20,






10

    since: 1540095775951,






11

    until: 1540095775951,






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

  "teams": [






3

    {






4

      "connect": {






5

        "enabled": "false"






6

      },






7

      "creatorId": "R6efeCJQ2HKXywuasPDc0fOWB",






8

      "updatedAt": "1611796915677",






9

      "emailDomain": "example.com",






10

      "saml": {






11

        "connection": {






12

          "type": "OktaSAML",






13

          "status": "linked",






14

          "state": "active",






15

          "connectedAt": "1611796915677",






16

          "lastReceivedWebhookEvent": "1611796915677",






17

          "lastSyncedAt": "1611796915677",






18

          "syncState": "SETUP"






19

        },






20

        "directory": {






21

          "type": "OktaSAML",






22

          "state": "active",






23

          "connectedAt": "1611796915677",






24

          "lastReceivedWebhookEvent": "1611796915677",






25

          "lastSyncedAt": "1611796915677",






26

          "syncState": "SETUP"






27

        },






28

        "enforced": "false",






29

        "defaultRedirectUri": "vercel.com",






30

        "roles": "value"






31

      },






32

      "inviteCode": "hasihf9e89",






33

      "description": "Our mission is to make cloud computing accessible to everyone.",






34

      "defaultRoles": {






35

        "teamRoles": [],






36

        "teamPermissions": []






37

      },






38

      "stagingPrefix": "string",






39

      "resourceConfig": {






40

        "concurrentBuilds": "123",






41

        "elasticConcurrencyEnabled": "false",






42

        "edgeConfigSize": "123",






43

        "edgeConfigs": "123",






44

        "kvDatabases": "123",






45

        "blobStores": "123",






46

        "postgresDatabases": "123",






47

        "buildEntitlements": {






48

          "enhancedBuilds": "false"






49

        },






50

        "buildMachine": {






51

          "default": "enhanced"






52

        }






53

      },






54

      "previewDeploymentSuffix": "example.dev",






55

      "platform": "true",






56

      "disableHardAutoBlocks": "123",






57

      "remoteCaching": {






58

        "enabled": "false"






59

      },






60

      "defaultDeploymentProtection": {






61

        "passwordProtection": {






62

          "deploymentType": "string"






63

        },






64

        "ssoProtection": {






65

          "deploymentType": "string"






66

        }






67

      },






68

      "defaultExpirationSettings": {






69

        "expirationDays": "123",






70

        "expirationDaysProduction": "123",






71

        "expirationDaysCanceled": "123",






72

        "expirationDaysErrored": "123",






73

        "deploymentsToKeep": "123"






74

      },






75

      "enablePreviewFeedback": "default",






76

      "enableProductionFeedback": "default",






77

      "sensitiveEnvironmentVariablePolicy": "default",






78

      "hideIpAddresses": "false",






79

      "hideIpAddressesInLogDrains": "false",






80

      "ipBuckets": [






81

        {






82

          "bucket": "string",






83

          "supportUntil": "123"






84

        }






85

      ],






86

      "strictDeploymentProtectionSettings": {






87

        "enabled": "false",






88

        "updatedAt": "123"






89

      },






90

      "nsnbConfig": {






91

        "preference": "auto-approval"






92

      },






93

      "id": "team_nllPyCtREAqxxdyFKbbMDlxd",






94

      "slug": "my-team",






95

      "name": "My Team",






96

      "avatar": "6eb07268bcfadd309905ffb1579354084c24655c",






97

      "membership": {






98

        "uid": "example_id",






99

        "entitlements": [






100

          {






101

            "entitlement": "string"






102

          }






103

        ],






104

        "teamId": "example_id",






105

        "confirmed": "true",






106

        "accessRequestedAt": "123",






107

        "role": "OWNER",






108

        "teamRoles": [],






109

        "teamPermissions": [],






110

        "createdAt": "123",






111

        "created": "123",






112

        "joinedFrom": {






113

          "origin": "link",






114

          "commitId": "example_id",






115

          "repoId": "example_id",






116

          "repoPath": "string",






117

          "gitUserId": "example_id",






118

          "gitUserLogin": "string",






119

          "ssoUserId": "example_id",






120

          "ssoConnectedAt": "123",






121

          "idpUserId": "example_id",






122

          "dsyncUserId": "example_id",






123

          "dsyncConnectedAt": "123"






124

        }






125

      },






126

      "createdAt": "1630748523395"






127

    }






128

  ],






129

  "pagination": {






130

    "count": "20",






131

    "next": "1540095775951",






132

    "prev": "1540095775951"






133

  }






134

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
