# Create integration store (free and paid plans)
POST`https://api.vercel.com/v1/storage/stores/integration/direct`
Creates an integration store with automatic billing plan handling. For free resources, omit `billingPlanId` to auto-discover free plans. For paid resources, provide a `billingPlanId` from the billing plans endpoint.
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

  const result = await vercel.integrations.createIntegrationStoreDirect({






9

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






10

    slug: "my-team-url-slug",






11

    requestBody: {






12

      name: "my-dev-database",






13

      integrationConfigurationId: "icfg_cuwj0AdCdH3BwWT4LPijCC7t",






14

      integrationProductIdOrSlug: "iap_postgres_db",






15

      metadata: {






16

        "environment": "development",






17

        "project": "my-app",






18

        "tags": [






19

          "database",






20

          "postgres",






21

        ],






22

      },






23

      externalId: "dev-db-001",






24

      protocolSettings: {






25

        "experimentation": {






26

          "edgeConfigSyncingEnabled": true,






27

        },






28

      },






29

      billingPlanId: "bp_abc123def456",






30

      paymentMethodId: "pm_1AbcDefGhiJklMno",






31

      prepaymentAmountCents: 5000,






32

    },






33

  });






34







35

  console.log(result);






36

}






37







38

run();




```

Response
```


1

{






2

  "store": {






3

    "projectsMetadata": [






4

      {






5

        "id": "icfg_1234567890",






6

        "projectId": "example_id",






7

        "name": "Example Name",






8

        "framework": "blitzjs",






9

        "latestDeployment": "string",






10

        "environments": [],






11

        "envVarPrefix": "string",






12

        "environmentVariables": [],






13

        "deployments": {






14

          "required": "false",






15

          "actions": [






16

            {






17

              "slug": "string",






18

              "environments": []






19

            }






20

          ]






21

        }






22

      }






23

    ],






24

    "projectFilter": {






25

      "git": {






26

        "providers": [],






27

        "owners": [],






28

        "repos": []






29

      }






30

    },






31

    "totalConnectedProjects": "123",






32

    "usageQuotaExceeded": "false",






33

    "status": "available",






34

    "ownership": "owned",






35

    "capabilities": {






36

      "mcp": "false",






37

      "mcpReadonly": "false",






38

      "sso": "false",






39

      "billable": "false",






40

      "transferable": "false",






41

      "secretsSync": "false",






42

      "secretRotation": {






43

        "maxDelayHours": "123"






44

      },






45

      "projects": "false",






46

      "v0": "false"






47

    },






48

    "metadata": "value",






49

    "externalResourceId": "example_id",






50

    "externalResourceStatus": "error",






51

    "directPartnerConsoleUrl": "https://example.com",






52

    "product": {






53

      "id": "icfg_1234567890",






54

      "name": "Example Name",






55

      "slug": "string",






56

      "iconUrl": "https://example.com",






57

      "capabilities": {






58

        "mcp": "false",






59

        "mcpReadonly": "false",






60

        "sso": "false",






61

        "billable": "false",






62

        "transferable": "false",






63

        "secretsSync": "false",






64

        "secretRotation": {






65

          "maxDelayHours": "123"






66

        },






67

        "sandbox": "false",






68

        "linking": "false",






69

        "projects": "false",






70

        "v0": "false",






71

        "importResource": "false",






72

        "connectedImportResource": "false",






73

        "nativeImportResource": "false",






74

        "databaseUI": "false"






75

      },






76

      "shortDescription": "string",






77

      "metadataSchema": {






78

        "type": "object",






79

        "properties": "value",






80

        "required": []






81

      },






82

      "resourceLinks": [






83

        {






84

          "href": "string",






85

          "title": "string"






86

        }






87

      ],






88

      "tags": [],






89

      "projectConnectionScopes": [],






90

      "showSSOLinkOnProjectConnection": "false",






91

      "disableResourceRenaming": "false",






92

      "resourceTitle": "Instance",






93

      "agentSkillUrl": "https://example.com",






94

      "repl": {






95

        "enabled": "false",






96

        "supportsReadOnlyMode": "false",






97

        "welcomeMessage": "string"






98

      },






99

      "guides": [






100

        {






101

          "framework": "string",






102

          "title": "string",






103

          "steps": [






104

            {






105

              "title": "string",






106

              "content": "string",






107

              "actions": [






108

                {






109

                  "type": "connect_to_project"






110

                }






111

              ]






112

            }






113

          ]






114

        }






115

      ],






116

      "integration": {






117

        "id": "icfg_1234567890",






118

        "name": "Example Name",






119

        "slug": "string",






120

        "supportsInstallationBillingPlans": "false",






121

        "icon": "string",






122

        "flags": []






123

      },






124

      "integrationConfigurationId": "example_id",






125

      "supportedProtocols": [],






126

      "primaryProtocol": "experimentation",






127

      "logDrainStatus": "disabled"






128

    },






129

    "protocolSettings": {






130

      "experimentation": {






131

        "edgeConfigSyncingEnabled": "false",






132

        "edgeConfigId": "example_id",






133

        "edgeConfigTokenId": "example_id"






134

      }






135

    },






136

    "notification": {






137

      "title": "string",






138

      "level": "error",






139

      "message": "string",






140

      "href": "string"






141

    },






142

    "secrets": [






143

      {






144

        "name": "Example Name",






145

        "length": "123"






146

      }






147

    ],






148

    "billingPlan": {






149

      "type": "prepayment",






150

      "description": "string",






151

      "id": "icfg_1234567890",






152

      "name": "Example Name",






153

      "scope": "installation",






154

      "paymentMethodRequired": "false",






155

      "preauthorizationAmount": "123",






156

      "initialCharge": "string",






157

      "minimumAmount": "100.00",






158

      "maximumAmount": "100.00",






159

      "maximumAmountAutoPurchasePerPeriod": "100.00",






160

      "cost": "string",






161

      "details": [






162

        {






163

          "label": "string",






164

          "value": "string"






165

        }






166

      ],






167

      "highlightedDetails": [






168

        {






169

          "label": "string",






170

          "value": "string"






171

        }






172

      ],






173

      "quote": [






174

        {






175

          "line": "string",






176

          "amount": "100.00"






177

        }






178

      ],






179

      "effectiveDate": "string",






180

      "disabled": "false"






181

    },






182

    "secretRotationRequestedAt": "123",






183

    "secretRotationRequestedReason": "Customer requested refund",






184

    "secretRotationRequestedBy": "string",






185

    "secretRotationCompletedAt": "123",






186

    "parentId": "example_id",






187

    "targets": []






188

  }






189

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/integrations/get-configurations-for-the-authenticated-user-or-team#authentication)[](https://vercel.com/docs/rest-api/sdk/integrations/get-configurations-for-the-authenticated-user-or-team#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/integrations/get-configurations-for-the-authenticated-user-or-team#query-parameters)[](https://vercel.com/docs/rest-api/sdk/integrations/get-configurations-for-the-authenticated-user-or-team#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Body](https://vercel.com/docs/rest-api/sdk/integrations/get-configurations-for-the-authenticated-user-or-team#body)[](https://vercel.com/docs/rest-api/sdk/integrations/get-configurations-for-the-authenticated-user-or-team#body)
application/json
namestringRequired
Human-readable name for the storage resource
integrationConfigurationIdstringRequired
ID of your integration configuration. Get this from GET /v1/integrations/configurations
integrationProductIdOrSlugobjectRequired2 variants
+Show 2 variants
metadataobjectOptional
Optional key-value pairs for resource metadata
externalIdstringOptional
Optional external identifier for tracking purposes
protocolSettingsobjectOptional
Protocol-specific configuration settings
sourcestringOptional
Source of the store creation request
+Show 8 enum values
billingPlanIdstringOptional
ID of the billing plan for paid resources. Get available plans from GET /integrations/integration/{id}/products/{productId}/plans. If not provided, automatically discovers free billing plans.
paymentMethodIdstringOptional
Payment method ID for paid resources. Optional - uses default payment method if not provided.
prepaymentAmountCentsnumberOptional
Amount in cents for prepayment billing plans. Required only for prepayment plans with variable amounts.
##  [Response](https://vercel.com/docs/rest-api/sdk/integrations/get-configurations-for-the-authenticated-user-or-team#response)[](https://vercel.com/docs/rest-api/sdk/integrations/get-configurations-for-the-authenticated-user-or-team#response)
200Success
storeobjectRequired
+Show 22 properties
##  [Errors](https://vercel.com/docs/rest-api/sdk/integrations/get-configurations-for-the-authenticated-user-or-team#errors)[](https://vercel.com/docs/rest-api/sdk/integrations/get-configurations-for-the-authenticated-user-or-team#errors)
400One of the provided values in the request body is invalid.
401The request is not authorized.
402The account was soft-blocked for an unhandled reason. The account is missing a payment so payment method must be updated
403You do not have permission to access this resource.
404Error
409Error
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

  const result = await vercel.integrations.createIntegrationStoreDirect({






9

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






10

    slug: "my-team-url-slug",






11

    requestBody: {






12

      name: "my-dev-database",






13

      integrationConfigurationId: "icfg_cuwj0AdCdH3BwWT4LPijCC7t",






14

      integrationProductIdOrSlug: "iap_postgres_db",






15

      metadata: {






16

        "environment": "development",






17

        "project": "my-app",






18

        "tags": [






19

          "database",






20

          "postgres",






21

        ],






22

      },






23

      externalId: "dev-db-001",






24

      protocolSettings: {






25

        "experimentation": {






26

          "edgeConfigSyncingEnabled": true,






27

        },






28

      },






29

      billingPlanId: "bp_abc123def456",






30

      paymentMethodId: "pm_1AbcDefGhiJklMno",






31

      prepaymentAmountCents: 5000,






32

    },






33

  });






34







35

  console.log(result);






36

}






37







38

run();




```

Response
```


1

{






2

  "store": {






3

    "projectsMetadata": [






4

      {






5

        "id": "icfg_1234567890",






6

        "projectId": "example_id",






7

        "name": "Example Name",






8

        "framework": "blitzjs",






9

        "latestDeployment": "string",






10

        "environments": [],






11

        "envVarPrefix": "string",






12

        "environmentVariables": [],






13

        "deployments": {






14

          "required": "false",






15

          "actions": [






16

            {






17

              "slug": "string",






18

              "environments": []






19

            }






20

          ]






21

        }






22

      }






23

    ],






24

    "projectFilter": {






25

      "git": {






26

        "providers": [],






27

        "owners": [],






28

        "repos": []






29

      }






30

    },






31

    "totalConnectedProjects": "123",






32

    "usageQuotaExceeded": "false",






33

    "status": "available",






34

    "ownership": "owned",






35

    "capabilities": {






36

      "mcp": "false",






37

      "mcpReadonly": "false",






38

      "sso": "false",






39

      "billable": "false",






40

      "transferable": "false",






41

      "secretsSync": "false",






42

      "secretRotation": {






43

        "maxDelayHours": "123"






44

      },






45

      "projects": "false",






46

      "v0": "false"






47

    },






48

    "metadata": "value",






49

    "externalResourceId": "example_id",






50

    "externalResourceStatus": "error",






51

    "directPartnerConsoleUrl": "https://example.com",






52

    "product": {






53

      "id": "icfg_1234567890",






54

      "name": "Example Name",






55

      "slug": "string",






56

      "iconUrl": "https://example.com",






57

      "capabilities": {






58

        "mcp": "false",






59

        "mcpReadonly": "false",






60

        "sso": "false",






61

        "billable": "false",






62

        "transferable": "false",






63

        "secretsSync": "false",






64

        "secretRotation": {






65

          "maxDelayHours": "123"






66

        },






67

        "sandbox": "false",






68

        "linking": "false",






69

        "projects": "false",






70

        "v0": "false",






71

        "importResource": "false",






72

        "connectedImportResource": "false",






73

        "nativeImportResource": "false",






74

        "databaseUI": "false"






75

      },






76

      "shortDescription": "string",






77

      "metadataSchema": {






78

        "type": "object",






79

        "properties": "value",






80

        "required": []






81

      },






82

      "resourceLinks": [






83

        {






84

          "href": "string",






85

          "title": "string"






86

        }






87

      ],






88

      "tags": [],






89

      "projectConnectionScopes": [],






90

      "showSSOLinkOnProjectConnection": "false",






91

      "disableResourceRenaming": "false",






92

      "resourceTitle": "Instance",






93

      "agentSkillUrl": "https://example.com",






94

      "repl": {






95

        "enabled": "false",






96

        "supportsReadOnlyMode": "false",






97

        "welcomeMessage": "string"






98

      },






99

      "guides": [






100

        {






101

          "framework": "string",






102

          "title": "string",






103

          "steps": [






104

            {






105

              "title": "string",






106

              "content": "string",






107

              "actions": [






108

                {






109

                  "type": "connect_to_project"






110

                }






111

              ]






112

            }






113

          ]






114

        }






115

      ],






116

      "integration": {






117

        "id": "icfg_1234567890",






118

        "name": "Example Name",






119

        "slug": "string",






120

        "supportsInstallationBillingPlans": "false",






121

        "icon": "string",






122

        "flags": []






123

      },






124

      "integrationConfigurationId": "example_id",






125

      "supportedProtocols": [],






126

      "primaryProtocol": "experimentation",






127

      "logDrainStatus": "disabled"






128

    },






129

    "protocolSettings": {






130

      "experimentation": {






131

        "edgeConfigSyncingEnabled": "false",






132

        "edgeConfigId": "example_id",






133

        "edgeConfigTokenId": "example_id"






134

      }






135

    },






136

    "notification": {






137

      "title": "string",






138

      "level": "error",






139

      "message": "string",






140

      "href": "string"






141

    },






142

    "secrets": [






143

      {






144

        "name": "Example Name",






145

        "length": "123"






146

      }






147

    ],






148

    "billingPlan": {






149

      "type": "prepayment",






150

      "description": "string",






151

      "id": "icfg_1234567890",






152

      "name": "Example Name",






153

      "scope": "installation",






154

      "paymentMethodRequired": "false",






155

      "preauthorizationAmount": "123",






156

      "initialCharge": "string",






157

      "minimumAmount": "100.00",






158

      "maximumAmount": "100.00",






159

      "maximumAmountAutoPurchasePerPeriod": "100.00",






160

      "cost": "string",






161

      "details": [






162

        {






163

          "label": "string",






164

          "value": "string"






165

        }






166

      ],






167

      "highlightedDetails": [






168

        {






169

          "label": "string",






170

          "value": "string"






171

        }






172

      ],






173

      "quote": [






174

        {






175

          "line": "string",






176

          "amount": "100.00"






177

        }






178

      ],






179

      "effectiveDate": "string",






180

      "disabled": "false"






181

    },






182

    "secretRotationRequestedAt": "123",






183

    "secretRotationRequestedReason": "Customer requested refund",






184

    "secretRotationRequestedBy": "string",






185

    "secretRotationCompletedAt": "123",






186

    "parentId": "example_id",






187

    "targets": []






188

  }






189

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
