# List flags
GET`https://api.vercel.com/v1/projects/{projectIdOrName}/feature-flags/flags`
Retrieve feature flags for a project. The list can be filtered by state and supports pagination.
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

  const result = await vercel.featureFlags.listFlags({






9

    projectIdOrName: "<value>",






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

##  [Authentication](https://vercel.com/docs/rest-api/sdk/feature-flags/list-flags#authentication)[](https://vercel.com/docs/rest-api/sdk/feature-flags/list-flags#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/feature-flags/list-flags#path-parameters)[](https://vercel.com/docs/rest-api/sdk/feature-flags/list-flags#path-parameters)
projectIdOrNamestringRequired
The project id or name
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/feature-flags/list-flags#query-parameters)[](https://vercel.com/docs/rest-api/sdk/feature-flags/list-flags#query-parameters)
statestringOptional
The state of the flags to retrieve. Defaults to `active`.
+Show 2 enum values
withMetadatabooleanOptional
Whether to include metadata in the response
limitintegerOptional
Maximum number of flags to return. When not set, all flags are returned.
cursorstringOptional
Pagination cursor to continue from.
searchstringOptional
Search flags by their slug or description. Case-insensitive.
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sdk/feature-flags/list-flags#response)[](https://vercel.com/docs/rest-api/sdk/feature-flags/list-flags#response)
200Success
dataarrayRequired
+Show 16 properties
paginationobjectRequired
+Show 1 properties
##  [Errors](https://vercel.com/docs/rest-api/sdk/feature-flags/list-flags#errors)[](https://vercel.com/docs/rest-api/sdk/feature-flags/list-flags#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
402The account was soft-blocked for an unhandled reason. The account is missing a payment so payment method must be updated
403You do not have permission to access this resource.
404Error
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

  const result = await vercel.featureFlags.listFlags({






9

    projectIdOrName: "<value>",






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

Copy as MarkdownGive feedbackAsk AI about this page
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Get project flag settings
