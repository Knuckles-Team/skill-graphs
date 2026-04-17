# Retrieve an integration configuration
GET`https://api.vercel.com/v1/integrations/configuration/{id}`
Allows to retrieve a the configuration with the provided id in case it exists. The authenticated user or team must be the owner of the config in order to access it.
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

  const result = await vercel.integrations.getConfiguration({






9

    id: "icfg_cuwj0AdCdH3BwWT4LPijCC7t",






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

  "projectSelection": "all",






3

  "notification": {






4

    "level": "error",






5

    "title": "string",






6

    "message": "string",






7

    "href": "string"






8

  },






9

  "transferRequest": {






10

    "kind": "transfer-to-marketplace",






11

    "metadata": "value",






12

    "billingPlan": {






13

      "id": "icfg_1234567890",






14

      "type": "prepayment",






15

      "scope": "installation",






16

      "name": "Example Name",






17

      "description": "string",






18

      "paymentMethodRequired": "false",






19

      "preauthorizationAmount": "123"






20

    },






21

    "requestId": "example_id",






22

    "transferId": "example_id",






23

    "requester": {






24

      "name": "Example Name",






25

      "email": "user@example.com"






26

    },






27

    "createdAt": "123",






28

    "expiresAt": "123",






29

    "discardedAt": "123",






30

    "discardedBy": "string",






31

    "approvedAt": "123",






32

    "approvedBy": "string",






33

    "authorizationId": "example_id"






34

  },






35

  "projects": [],






36

  "status": "error",






37

  "type": "integration-configuration",






38

  "createdAt": "1558531915505",






39

  "deletedAt": "1558531915505",






40

  "id": "icfg_3bwCLgxL8qt5kjRLcv2Dit7F",






41

  "slug": "slack",






42

  "teamId": "team_nLlpyC6RE1qxydlFKbrxDlud",






43

  "updatedAt": "1558531915505",






44

  "userId": "kr1PsOIzqEL5Xg6M4VZcZosf",






45

  "scopes": [],






46

  "source": "marketplace",






47

  "integrationId": "oac_xzpVzcUOgcB1nrVlirtKhbWV",






48

  "ownerId": "kr1PsOIzqEL5Xg6M4VZcZosf",






49

  "canConfigureOpenTelemetry": "false",






50

  "completedAt": "1558531915505",






51

  "externalId": "example_id",






52

  "disabledAt": "1558531915505",






53

  "deleteRequestedAt": "1558531915505",






54

  "disabledReason": "disabled-by-owner",






55

  "installationType": "marketplace"






56

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/integrations/list-git-repositories-linked-to-namespace-by-provider#authentication)[](https://vercel.com/docs/rest-api/sdk/integrations/list-git-repositories-linked-to-namespace-by-provider#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/integrations/list-git-repositories-linked-to-namespace-by-provider#path-parameters)[](https://vercel.com/docs/rest-api/sdk/integrations/list-git-repositories-linked-to-namespace-by-provider#path-parameters)
idstringRequired
ID of the configuration to check
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/integrations/list-git-repositories-linked-to-namespace-by-provider#query-parameters)[](https://vercel.com/docs/rest-api/sdk/integrations/list-git-repositories-linked-to-namespace-by-provider#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sdk/integrations/list-git-repositories-linked-to-namespace-by-provider#response)[](https://vercel.com/docs/rest-api/sdk/integrations/list-git-repositories-linked-to-namespace-by-provider#response)
200The configuration with the provided id
projectSelectionstringRequired
A string representing the permission for projects. Possible values are `all` or `selected`.
+Show 2 enum values
notificationobjectRequired
+Show 4 properties
transferRequestobjectRequired2 variants
+Show 2 variants
projectsarrayOptional
When a configuration is limited to access certain projects, this will contain each of the project ID it is allowed to access. If it is not defined, the configuration has full access.
statusstringOptional
The configuration status. Optional. If not defined, assume 'ready'.
+Show 7 enum values
typestringRequired
+Show 1 enum values
createdAtnumberRequired
A timestamp that tells you when the configuration was created
deletedAtnumberOptional
A timestamp that tells you when the configuration was deleted.
idstringRequired
The unique identifier of the configuration
slugstringRequired
The slug of the integration the configuration is created for.
teamIdstringOptional
When the configuration was created for a team, this will show the ID of the team.
updatedAtnumberRequired
A timestamp that tells you when the configuration was updated.
userIdstringRequired
The ID of the user that created the configuration.
scopesarrayRequired
The resources that are allowed to be accessed by the configuration.
sourcestringOptional
Source defines where the configuration was installed from. It is used to analyze user engagement for integration installations in product metrics.
+Show 8 enum values
integrationIdstringRequired
The unique identifier of the app the configuration was created for
ownerIdstringRequired
The user or team ID that owns the configuration
canConfigureOpenTelemetrybooleanOptional
+Show 2 enum values
completedAtnumberOptional
A timestamp that tells you when the configuration was installed successfully
externalIdstringOptional
An external identifier defined by the integration vendor.
disabledAtnumberOptional
A timestamp that tells you when the configuration was disabled. Note: Configurations can be disabled when the associated user loses access to a team. They do not function during this time until the configuration is 'transferred', meaning the associated user is changed to one with access to the team.
deleteRequestedAtnumberOptional
A timestamp that tells you when the configuration deletion has been started for cases when the deletion needs to be settled/approved by partners, such as when marketplace invoices have been paid.
disabledReasonstringOptional
+Show 6 enum values
installationTypestringOptional
Defines the installation type. - 'external' integrations are installed via the existing integrations flow - 'marketplace' integrations are natively installed: - when accepting the TOS of a partner during the store creation process - if undefined, assume 'external'
+Show 2 enum values
##  [Errors](https://vercel.com/docs/rest-api/sdk/integrations/list-git-repositories-linked-to-namespace-by-provider#errors)[](https://vercel.com/docs/rest-api/sdk/integrations/list-git-repositories-linked-to-namespace-by-provider#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404The configuration was not found
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

  const result = await vercel.integrations.getConfiguration({






9

    id: "icfg_cuwj0AdCdH3BwWT4LPijCC7t",






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

  "projectSelection": "all",






3

  "notification": {






4

    "level": "error",






5

    "title": "string",






6

    "message": "string",






7

    "href": "string"






8

  },






9

  "transferRequest": {






10

    "kind": "transfer-to-marketplace",






11

    "metadata": "value",






12

    "billingPlan": {






13

      "id": "icfg_1234567890",






14

      "type": "prepayment",






15

      "scope": "installation",






16

      "name": "Example Name",






17

      "description": "string",






18

      "paymentMethodRequired": "false",






19

      "preauthorizationAmount": "123"






20

    },






21

    "requestId": "example_id",






22

    "transferId": "example_id",






23

    "requester": {






24

      "name": "Example Name",






25

      "email": "user@example.com"






26

    },






27

    "createdAt": "123",






28

    "expiresAt": "123",






29

    "discardedAt": "123",






30

    "discardedBy": "string",






31

    "approvedAt": "123",






32

    "approvedBy": "string",






33

    "authorizationId": "example_id"






34

  },






35

  "projects": [],






36

  "status": "error",






37

  "type": "integration-configuration",






38

  "createdAt": "1558531915505",






39

  "deletedAt": "1558531915505",






40

  "id": "icfg_3bwCLgxL8qt5kjRLcv2Dit7F",






41

  "slug": "slack",






42

  "teamId": "team_nLlpyC6RE1qxydlFKbrxDlud",






43

  "updatedAt": "1558531915505",






44

  "userId": "kr1PsOIzqEL5Xg6M4VZcZosf",






45

  "scopes": [],






46

  "source": "marketplace",






47

  "integrationId": "oac_xzpVzcUOgcB1nrVlirtKhbWV",






48

  "ownerId": "kr1PsOIzqEL5Xg6M4VZcZosf",






49

  "canConfigureOpenTelemetry": "false",






50

  "completedAt": "1558531915505",






51

  "externalId": "example_id",






52

  "disabledAt": "1558531915505",






53

  "deleteRequestedAt": "1558531915505",






54

  "disabledReason": "disabled-by-owner",






55

  "installationType": "marketplace"






56

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
