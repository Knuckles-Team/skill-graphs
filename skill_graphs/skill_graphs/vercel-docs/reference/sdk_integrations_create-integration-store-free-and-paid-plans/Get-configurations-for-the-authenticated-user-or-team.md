# Get configurations for the authenticated user or team
GET`https://api.vercel.com/v1/integrations/configurations`
Allows to retrieve all configurations for an authenticated integration. When the `project` view is used, configurations generated for the authorization flow will be filtered out of the results.
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

  const result = await vercel.integrations.getConfigurations({






9

    view: "account",






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

[






2

  {






3

    "completedAt": "1558531915505",






4

    "createdAt": "1558531915505",






5

    "id": "icfg_3bwCLgxL8qt5kjRLcv2Dit7F",






6

    "integrationId": "oac_xzpVzcUOgcB1nrVlirtKhbWV",






7

    "ownerId": "kr1PsOIzqEL5Xg6M4VZcZosf",






8

    "status": "error",






9

    "externalId": "example_id",






10

    "projects": [],






11

    "source": "marketplace",






12

    "slug": "slack",






13

    "teamId": "team_nLlpyC6RE1qxydlFKbrxDlud",






14

    "type": "integration-configuration",






15

    "updatedAt": "1558531915505",






16

    "userId": "kr1PsOIzqEL5Xg6M4VZcZosf",






17

    "scopes": [],






18

    "disabledAt": "1558531915505",






19

    "deletedAt": "1558531915505",






20

    "deleteRequestedAt": "1558531915505",






21

    "disabledReason": "disabled-by-owner",






22

    "installationType": "marketplace"






23

  }






24

]




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/integrations/get-configurations-for-the-authenticated-user-or-team#authentication)[](https://vercel.com/docs/rest-api/sdk/integrations/get-configurations-for-the-authenticated-user-or-team#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/integrations/get-configurations-for-the-authenticated-user-or-team#query-parameters)[](https://vercel.com/docs/rest-api/sdk/integrations/get-configurations-for-the-authenticated-user-or-team#query-parameters)
viewstringRequired
+Show 2 enum values
installationTypestringOptional
+Show 3 enum values
integrationIdOrSlugstringOptional
ID of the integration
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sdk/integrations/get-configurations-for-the-authenticated-user-or-team#response)[](https://vercel.com/docs/rest-api/sdk/integrations/get-configurations-for-the-authenticated-user-or-team#response)
200The list of configurations for the authenticated user
##  [Errors](https://vercel.com/docs/rest-api/sdk/integrations/get-configurations-for-the-authenticated-user-or-team#errors)[](https://vercel.com/docs/rest-api/sdk/integrations/get-configurations-for-the-authenticated-user-or-team#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
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

  const result = await vercel.integrations.getConfigurations({






9

    view: "account",






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

[






2

  {






3

    "completedAt": "1558531915505",






4

    "createdAt": "1558531915505",






5

    "id": "icfg_3bwCLgxL8qt5kjRLcv2Dit7F",






6

    "integrationId": "oac_xzpVzcUOgcB1nrVlirtKhbWV",






7

    "ownerId": "kr1PsOIzqEL5Xg6M4VZcZosf",






8

    "status": "error",






9

    "externalId": "example_id",






10

    "projects": [],






11

    "source": "marketplace",






12

    "slug": "slack",






13

    "teamId": "team_nLlpyC6RE1qxydlFKbrxDlud",






14

    "type": "integration-configuration",






15

    "updatedAt": "1558531915505",






16

    "userId": "kr1PsOIzqEL5Xg6M4VZcZosf",






17

    "scopes": [],






18

    "disabledAt": "1558531915505",






19

    "deletedAt": "1558531915505",






20

    "deleteRequestedAt": "1558531915505",






21

    "disabledReason": "disabled-by-owner",






22

    "installationType": "marketplace"






23

  }






24

]




```

Copy as MarkdownGive feedbackAsk AI about this page
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Create integration store (free and paid plans)
