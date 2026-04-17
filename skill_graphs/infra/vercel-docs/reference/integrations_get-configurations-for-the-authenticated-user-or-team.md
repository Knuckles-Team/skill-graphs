Menu
APIs & SDKs
[Vercel REST API](https://vercel.com/docs/rest-api)
Get configurations for the authenticated user or team
# Get configurations for the authenticated user or team
GET`https://api.vercel.com/v1/integrations/configurations`
Allows to retrieve all configurations for an authenticated integration. When the `project` view is used, configurations generated for the authorization flow will be filtered out of the results.
TypeScriptNext.jscURL
https://api.vercel.com/v1/integrations/configurations
```


1

const response = await fetch('https://api.vercel.com/v1/integrations/configurations?view=string&installationType=string&integrationIdOrSlug=string&teamId=string&slug=string', {






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

##  [Authentication](https://vercel.com/docs/rest-api/integrations/get-configurations-for-the-authenticated-user-or-team#authentication)[](https://vercel.com/docs/rest-api/integrations/get-configurations-for-the-authenticated-user-or-team#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Query parameters](https://vercel.com/docs/rest-api/integrations/get-configurations-for-the-authenticated-user-or-team#query-parameters)[](https://vercel.com/docs/rest-api/integrations/get-configurations-for-the-authenticated-user-or-team#query-parameters)
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
##  [Response](https://vercel.com/docs/rest-api/integrations/get-configurations-for-the-authenticated-user-or-team#response)[](https://vercel.com/docs/rest-api/integrations/get-configurations-for-the-authenticated-user-or-team#response)
200The list of configurations for the authenticated user
##  [Errors](https://vercel.com/docs/rest-api/integrations/get-configurations-for-the-authenticated-user-or-team#errors)[](https://vercel.com/docs/rest-api/integrations/get-configurations-for-the-authenticated-user-or-team#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
