# Update a Team
PATCH`https://api.vercel.com/v2/teams/{teamId}`
Update the information of a Team specified by the `teamId` parameter. The request body should contain the information that will be updated on the Team.
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

  const result = await vercel.teams.patchTeam({






9

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






10

    slug: "my-team-url-slug",






11

    requestBody: {






12

      description: "Our mission is to make cloud computing accessible to everyone",






13

      emailDomain: "example.com",






14

      name: "My Team",






15

      previewDeploymentSuffix: "example.dev",






16

      regenerateInviteCode: true,






17

      saml: {






18

        enforced: true,






19

      },






20

      slug: "my-team",






21

      enablePreviewFeedback: "on",






22

      enableProductionFeedback: "on",






23

      sensitiveEnvironmentVariablePolicy: "on",






24

      remoteCaching: {






25

        enabled: true,






26

      },






27

      hideIpAddresses: false,






28

      hideIpAddressesInLogDrains: false,






29

      defaultExpirationSettings: {






30

        expiration: "1y",






31

        expirationProduction: "1y",






32

        expirationCanceled: "1y",






33

        expirationErrored: "1y",






34

      },






35

      strictDeploymentProtectionSettings: {






36

        enabled: true,






37

      },






38

      resourceConfig: {






39

        buildMachine: {






40

          default: "standard",






41

        },






42

      },






43

    },






44

  });






45







46

  console.log(result);






47

}






48







49

run();




```

Response
```


1

{






2

  "connect": {






3

    "enabled": "false"






4

  },






5

  "creatorId": "R6efeCJQ2HKXywuasPDc0fOWB",






6

  "updatedAt": "1611796915677",






7

  "emailDomain": "example.com",






8

  "saml": {






9

    "connection": {






10

      "type": "OktaSAML",






11

      "status": "linked",






12

      "state": "active",






13

      "connectedAt": "1611796915677",






14

      "lastReceivedWebhookEvent": "1611796915677",






15

      "lastSyncedAt": "1611796915677",






16

      "syncState": "SETUP"






17

    },






18

    "directory": {






19

      "type": "OktaSAML",






20

      "state": "active",






21

      "connectedAt": "1611796915677",






22

      "lastReceivedWebhookEvent": "1611796915677",






23

      "lastSyncedAt": "1611796915677",






24

      "syncState": "SETUP"






25

    },






26

    "enforced": "false",






27

    "defaultRedirectUri": "vercel.com",






28

    "roles": "value"






29

  },






30

  "inviteCode": "hasihf9e89",






31

  "description": "Our mission is to make cloud computing accessible to everyone.",






32

  "defaultRoles": {






33

    "teamRoles": [],






34

    "teamPermissions": []






35

  },






36

  "stagingPrefix": "string",






37

  "resourceConfig": {






38

    "concurrentBuilds": "123",






39

    "elasticConcurrencyEnabled": "false",






40

    "edgeConfigSize": "123",






41

    "edgeConfigs": "123",






42

    "kvDatabases": "123",






43

    "blobStores": "123",






44

    "postgresDatabases": "123",






45

    "buildEntitlements": {






46

      "enhancedBuilds": "false"






47

    },






48

    "buildMachine": {






49

      "default": "enhanced"






50

    }






51

  },






52

  "previewDeploymentSuffix": "example.dev",






53

  "platform": "true",






54

  "disableHardAutoBlocks": "123",






55

  "remoteCaching": {






56

    "enabled": "false"






57

  },






58

  "defaultDeploymentProtection": {






59

    "passwordProtection": {






60

      "deploymentType": "string"






61

    },






62

    "ssoProtection": {






63

      "deploymentType": "string"






64

    }






65

  },






66

  "defaultExpirationSettings": {






67

    "expirationDays": "123",






68

    "expirationDaysProduction": "123",






69

    "expirationDaysCanceled": "123",






70

    "expirationDaysErrored": "123",






71

    "deploymentsToKeep": "123"






72

  },






73

  "enablePreviewFeedback": "default",






74

  "enableProductionFeedback": "default",






75

  "sensitiveEnvironmentVariablePolicy": "default",






76

  "hideIpAddresses": "false",






77

  "hideIpAddressesInLogDrains": "false",






78

  "ipBuckets": [






79

    {






80

      "bucket": "string",






81

      "supportUntil": "123"






82

    }






83

  ],






84

  "strictDeploymentProtectionSettings": {






85

    "enabled": "false",






86

    "updatedAt": "123"






87

  },






88

  "nsnbConfig": {






89

    "preference": "auto-approval"






90

  },






91

  "id": "team_nllPyCtREAqxxdyFKbbMDlxd",






92

  "slug": "my-team",






93

  "name": "My Team",






94

  "avatar": "6eb07268bcfadd309905ffb1579354084c24655c",






95

  "membership": {






96

    "uid": "example_id",






97

    "entitlements": [






98

      {






99

        "entitlement": "string"






100

      }






101

    ],






102

    "teamId": "example_id",






103

    "confirmed": "true",






104

    "accessRequestedAt": "123",






105

    "role": "OWNER",






106

    "teamRoles": [],






107

    "teamPermissions": [],






108

    "createdAt": "123",






109

    "created": "123",






110

    "joinedFrom": {






111

      "origin": "link",






112

      "commitId": "example_id",






113

      "repoId": "example_id",






114

      "repoPath": "string",






115

      "gitUserId": "example_id",






116

      "gitUserLogin": "string",






117

      "ssoUserId": "example_id",






118

      "ssoConnectedAt": "123",






119

      "idpUserId": "example_id",






120

      "dsyncUserId": "example_id",






121

      "dsyncConnectedAt": "123"






122

    }






123

  },






124

  "createdAt": "1630748523395"






125

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/teams/get-access-request-status#authentication)[](https://vercel.com/docs/rest-api/sdk/teams/get-access-request-status#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/teams/get-access-request-status#path-parameters)[](https://vercel.com/docs/rest-api/sdk/teams/get-access-request-status#path-parameters)
teamIdstringRequired
The Team identifier to perform the request on behalf of.
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/teams/get-access-request-status#query-parameters)[](https://vercel.com/docs/rest-api/sdk/teams/get-access-request-status#query-parameters)
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Body](https://vercel.com/docs/rest-api/sdk/teams/get-access-request-status#body)[](https://vercel.com/docs/rest-api/sdk/teams/get-access-request-status#body)
application/json
avatarstringOptional
The hash value of an uploaded image.
descriptionstringOptional
A short text that describes the team.
emailDomainstringOptional
namestringOptional
The name of the team.
previewDeploymentSuffixstringOptional
Suffix that will be used for all preview deployments.
regenerateInviteCodebooleanOptional
Create a new invite code and replace the current one.
samlobjectOptional
+Show 2 properties
slugstringOptional
A new slug for the team.
enablePreviewFeedbackstringOptional
Enable preview toolbar: one of on, off or default.
enableProductionFeedbackstringOptional
Enable production toolbar: one of on, off or default.
sensitiveEnvironmentVariablePolicystringOptional
Sensitive environment variable policy: one of on, off or default.
remoteCachingobjectOptional
Whether or not remote caching is enabled for the team
+Show 1 properties
hideIpAddressesbooleanOptional
Display or hide IP addresses in Monitoring queries.
hideIpAddressesInLogDrainsbooleanOptional
Display or hide IP addresses in Log Drains.
defaultDeploymentProtectionobjectOptional
Default deployment protection settings for new projects.
+Show 2 properties
defaultExpirationSettingsobjectOptional
+Show 4 properties
strictDeploymentProtectionSettingsobjectOptional
When enabled, deployment protection settings require stricter permissions (owner-only).
+Show 1 properties
nsnbConfigobjectOptional
NSNB configuration for the team.
+Show 1 properties
resourceConfigobjectOptional
Resource configuration for the team.
+Show 1 properties
##  [Response](https://vercel.com/docs/rest-api/sdk/teams/get-access-request-status#response)[](https://vercel.com/docs/rest-api/sdk/teams/get-access-request-status#response)
200Success
connectobjectOptional
+Show 1 properties
creatorIdstringRequired
The ID of the user who created the Team.
updatedAtnumberRequired
Timestamp (in milliseconds) of when the Team was last updated.
emailDomainstringOptional
Hostname that'll be matched with emails on sign-up to automatically join the Team.
samlobjectOptional
When "Single Sign-On (SAML)" is configured, this object contains information regarding the configuration of the Identity Provider (IdP).
+Show 5 properties
inviteCodestringOptional
Code that can be used to join this Team. Only visible to Team owners.
descriptionstringRequired
A short description of the Team.
defaultRolesobjectOptional
Default roles for the team.
+Show 2 properties
stagingPrefixstringRequired
The prefix that is prepended to automatic aliases.
resourceConfigobjectOptional
+Show 9 properties
previewDeploymentSuffixstringOptional
The hostname that is current set as preview deployment suffix.
platformbooleanOptional
Whether the team is a platform team.
+Show 2 enum values
disableHardAutoBlocksobjectOptional2 variants
+Show 2 variants
remoteCachingobjectOptional
Is remote caching enabled for this team
+Show 1 properties
defaultDeploymentProtectionobjectOptional
Default deployment protection for this team null indicates protection is disabled
+Show 2 properties
defaultExpirationSettingsobjectOptional
Default deployment expiration settings for this team
+Show 5 properties
enablePreviewFeedbackstringOptional
Whether toolbar is enabled on preview deployments
+Show 6 enum values
enableProductionFeedbackstringOptional
Whether toolbar is enabled on production deployments
+Show 6 enum values
sensitiveEnvironmentVariablePolicystringOptional
Sensitive environment variable policy for this team
+Show 3 enum values
hideIpAddressesbooleanOptional
Indicates if IP addresses should be accessible in observability (o11y) tooling
+Show 2 enum values
hideIpAddressesInLogDrainsbooleanOptional
Indicates if IP addresses should be accessible in log drains
+Show 2 enum values
ipBucketsarrayOptional
+Show 2 properties
strictDeploymentProtectionSettingsobjectOptional
When enabled, deployment protection settings require stricter permissions (owner-only).
+Show 2 properties
nsnbConfigobjectOptional
NSNB configuration for the team.
+Show 1 properties
idstringRequired
The Team's unique identifier.
slugstringRequired
The Team's slug, which is unique across the Vercel platform.
namestringRequired
Name associated with the Team account, or `null` if none has been provided.
avatarstringRequired
The ID of the file used as avatar for this Team.
membershipobjectRequired
The membership of the authenticated User in relation to the Team.
+Show 11 properties
createdAtnumberRequired
UNIX timestamp (in milliseconds) when the Team was created.
##  [Errors](https://vercel.com/docs/rest-api/sdk/teams/get-access-request-status#errors)[](https://vercel.com/docs/rest-api/sdk/teams/get-access-request-status#errors)
400One of the provided values in the request body is invalid.
401The request is not authorized.
402Error
403You do not have permission to access this resource. Not authorized to update the team. Must be an OWNER.
428Owner does not have protection add-on Advanced Deployment Protection is not available for the user plan
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

  const result = await vercel.teams.patchTeam({






9

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






10

    slug: "my-team-url-slug",






11

    requestBody: {






12

      description: "Our mission is to make cloud computing accessible to everyone",






13

      emailDomain: "example.com",






14

      name: "My Team",






15

      previewDeploymentSuffix: "example.dev",






16

      regenerateInviteCode: true,






17

      saml: {






18

        enforced: true,






19

      },






20

      slug: "my-team",






21

      enablePreviewFeedback: "on",






22

      enableProductionFeedback: "on",






23

      sensitiveEnvironmentVariablePolicy: "on",






24

      remoteCaching: {






25

        enabled: true,






26

      },






27

      hideIpAddresses: false,






28

      hideIpAddressesInLogDrains: false,






29

      defaultExpirationSettings: {






30

        expiration: "1y",






31

        expirationProduction: "1y",






32

        expirationCanceled: "1y",






33

        expirationErrored: "1y",






34

      },






35

      strictDeploymentProtectionSettings: {






36

        enabled: true,






37

      },






38

      resourceConfig: {






39

        buildMachine: {






40

          default: "standard",






41

        },






42

      },






43

    },






44

  });






45







46

  console.log(result);






47

}






48







49

run();




```

Response
```


1

{






2

  "connect": {






3

    "enabled": "false"






4

  },






5

  "creatorId": "R6efeCJQ2HKXywuasPDc0fOWB",






6

  "updatedAt": "1611796915677",






7

  "emailDomain": "example.com",






8

  "saml": {






9

    "connection": {






10

      "type": "OktaSAML",






11

      "status": "linked",






12

      "state": "active",






13

      "connectedAt": "1611796915677",






14

      "lastReceivedWebhookEvent": "1611796915677",






15

      "lastSyncedAt": "1611796915677",






16

      "syncState": "SETUP"






17

    },






18

    "directory": {






19

      "type": "OktaSAML",






20

      "state": "active",






21

      "connectedAt": "1611796915677",






22

      "lastReceivedWebhookEvent": "1611796915677",






23

      "lastSyncedAt": "1611796915677",






24

      "syncState": "SETUP"






25

    },






26

    "enforced": "false",






27

    "defaultRedirectUri": "vercel.com",






28

    "roles": "value"






29

  },






30

  "inviteCode": "hasihf9e89",






31

  "description": "Our mission is to make cloud computing accessible to everyone.",






32

  "defaultRoles": {






33

    "teamRoles": [],






34

    "teamPermissions": []






35

  },






36

  "stagingPrefix": "string",






37

  "resourceConfig": {






38

    "concurrentBuilds": "123",






39

    "elasticConcurrencyEnabled": "false",






40

    "edgeConfigSize": "123",






41

    "edgeConfigs": "123",






42

    "kvDatabases": "123",






43

    "blobStores": "123",






44

    "postgresDatabases": "123",






45

    "buildEntitlements": {






46

      "enhancedBuilds": "false"






47

    },






48

    "buildMachine": {






49

      "default": "enhanced"






50

    }






51

  },






52

  "previewDeploymentSuffix": "example.dev",






53

  "platform": "true",






54

  "disableHardAutoBlocks": "123",






55

  "remoteCaching": {






56

    "enabled": "false"






57

  },






58

  "defaultDeploymentProtection": {






59

    "passwordProtection": {






60

      "deploymentType": "string"






61

    },






62

    "ssoProtection": {






63

      "deploymentType": "string"






64

    }






65

  },






66

  "defaultExpirationSettings": {






67

    "expirationDays": "123",






68

    "expirationDaysProduction": "123",






69

    "expirationDaysCanceled": "123",






70

    "expirationDaysErrored": "123",






71

    "deploymentsToKeep": "123"






72

  },






73

  "enablePreviewFeedback": "default",






74

  "enableProductionFeedback": "default",






75

  "sensitiveEnvironmentVariablePolicy": "default",






76

  "hideIpAddresses": "false",






77

  "hideIpAddressesInLogDrains": "false",






78

  "ipBuckets": [






79

    {






80

      "bucket": "string",






81

      "supportUntil": "123"






82

    }






83

  ],






84

  "strictDeploymentProtectionSettings": {






85

    "enabled": "false",






86

    "updatedAt": "123"






87

  },






88

  "nsnbConfig": {






89

    "preference": "auto-approval"






90

  },






91

  "id": "team_nllPyCtREAqxxdyFKbbMDlxd",






92

  "slug": "my-team",






93

  "name": "My Team",






94

  "avatar": "6eb07268bcfadd309905ffb1579354084c24655c",






95

  "membership": {






96

    "uid": "example_id",






97

    "entitlements": [






98

      {






99

        "entitlement": "string"






100

      }






101

    ],






102

    "teamId": "example_id",






103

    "confirmed": "true",






104

    "accessRequestedAt": "123",






105

    "role": "OWNER",






106

    "teamRoles": [],






107

    "teamPermissions": [],






108

    "createdAt": "123",






109

    "created": "123",






110

    "joinedFrom": {






111

      "origin": "link",






112

      "commitId": "example_id",






113

      "repoId": "example_id",






114

      "repoPath": "string",






115

      "gitUserId": "example_id",






116

      "gitUserLogin": "string",






117

      "ssoUserId": "example_id",






118

      "ssoConnectedAt": "123",






119

      "idpUserId": "example_id",






120

      "dsyncUserId": "example_id",






121

      "dsyncConnectedAt": "123"






122

    }






123

  },






124

  "createdAt": "1630748523395"






125

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
