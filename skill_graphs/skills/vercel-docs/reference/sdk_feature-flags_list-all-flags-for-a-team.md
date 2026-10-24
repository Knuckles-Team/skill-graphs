Menu
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
List all flags for a team
# List all flags for a team
GET`https://api.vercel.com/v1/teams/{teamId}/feature-flags/flags`
Retrieve all feature flags for a team across all projects. The list can be filtered by state and supports pagination.
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

  const result = await vercel.featureFlags.listTeamFlags({






9

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






10

    slug: "my-team-url-slug",






11

  });






12







13

  console.log(result);






14

}






15







16

run();




```

Response
```


1

{






2

  "data": [






3

    {






4

      "description": "string",






5

      "variants": [






6

        {






7

          "description": "string",






8

          "label": "string",






9

          "value": "string",






10

          "id": "icfg_1234567890"






11

        }






12

      ],






13

      "id": "icfg_1234567890",






14

      "environments": "value",






15

      "kind": "string",






16

      "revision": "123",






17

      "seed": "123",






18

      "state": "active",






19

      "slug": "string",






20

      "createdAt": "123",






21

      "updatedAt": "123",






22

      "createdBy": "string",






23

      "ownerId": "example_id",






24

      "projectId": "example_id",






25

      "typeName": "flag",






26

      "metadata": {






27

        "creator": {






28

          "id": "icfg_1234567890",






29

          "name": "Example Name"






30

        }






31

      }






32

    }






33

  ],






34

  "pagination": {






35

    "next": "string"






36

  }






37

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/feature-flags/list-all-flags-for-a-team#authentication)[](https://vercel.com/docs/rest-api/sdk/feature-flags/list-all-flags-for-a-team#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/feature-flags/list-all-flags-for-a-team#path-parameters)[](https://vercel.com/docs/rest-api/sdk/feature-flags/list-all-flags-for-a-team#path-parameters)
teamIdstringRequired
The Team identifier to perform the request on behalf of.
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/feature-flags/list-all-flags-for-a-team#query-parameters)[](https://vercel.com/docs/rest-api/sdk/feature-flags/list-all-flags-for-a-team#query-parameters)
statestringOptional
The state of the flags to retrieve. Defaults to `active`.
+Show 2 enum values
withMetadatabooleanOptional
Whether to include metadata in the response
limitintegerOptional
Maximum number of flags to return.
cursorstringOptional
Pagination cursor to continue from.
searchstringOptional
Search flags by their slug or description. Case-insensitive.
kindstringOptional
The kind of flags to retrieve.
+Show 3 enum values
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sdk/feature-flags/list-all-flags-for-a-team#response)[](https://vercel.com/docs/rest-api/sdk/feature-flags/list-all-flags-for-a-team#response)
200Success
dataarrayRequired
+Show 16 properties
paginationobjectRequired
+Show 1 properties
##  [Errors](https://vercel.com/docs/rest-api/sdk/feature-flags/list-all-flags-for-a-team#errors)[](https://vercel.com/docs/rest-api/sdk/feature-flags/list-all-flags-for-a-team#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
