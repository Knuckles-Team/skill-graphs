# Create a flag
PUT`https://api.vercel.com/v1/projects/{projectIdOrName}/feature-flags/flags`
Create a new feature flag for a project. The flag must have a unique slug within the project and specify its kind (boolean, string, or number).
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

  const result = await vercel.featureFlags.createFlag({






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

  "description": "string",






3

  "variants": [






4

    {






5

      "description": "string",






6

      "label": "string",






7

      "value": "string",






8

      "id": "icfg_1234567890"






9

    }






10

  ],






11

  "id": "icfg_1234567890",






12

  "environments": "value",






13

  "kind": "string",






14

  "revision": "123",






15

  "seed": "123",






16

  "state": "active",






17

  "slug": "string",






18

  "createdAt": "123",






19

  "updatedAt": "123",






20

  "createdBy": "string",






21

  "ownerId": "example_id",






22

  "projectId": "example_id",






23

  "typeName": "flag"






24

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/feature-flags/create-a-flag#authentication)[](https://vercel.com/docs/rest-api/sdk/feature-flags/create-a-flag#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/feature-flags/create-a-flag#path-parameters)[](https://vercel.com/docs/rest-api/sdk/feature-flags/create-a-flag#path-parameters)
projectIdOrNamestringRequired
The project id or name
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/feature-flags/create-a-flag#query-parameters)[](https://vercel.com/docs/rest-api/sdk/feature-flags/create-a-flag#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Body](https://vercel.com/docs/rest-api/sdk/feature-flags/create-a-flag#body)[](https://vercel.com/docs/rest-api/sdk/feature-flags/create-a-flag#body)
application/json
slugstringRequired
A unique (per project) key for the flag, composed of letters, numbers, dashes, and underscores
kindobjectRequired
The kind of flag
+Show 3 enum values
variantsarrayOptional
The variants of the flag
+Show 4 properties
environmentsobjectRequired
The configuration for the flag in different environments
seednumberOptional
A random seed to prevent split points in different flags from having the same targets
descriptionstringOptional
A description of the flag
statestringOptional
+Show 2 enum values
##  [Response](https://vercel.com/docs/rest-api/sdk/feature-flags/create-a-flag#response)[](https://vercel.com/docs/rest-api/sdk/feature-flags/create-a-flag#response)
201Success
descriptionstringOptional
variantsarrayRequired
+Show 4 properties
idstringRequired
environmentsobjectRequired
kindstringRequired
+Show 3 enum values
revisionnumberRequired
seednumberRequired
statestringRequired
+Show 2 enum values
slugstringRequired
createdAtnumberRequired
updatedAtnumberRequired
createdBystringRequired
ownerIdstringRequired
projectIdstringRequired
typeNamestringRequired
+Show 1 enum values
##  [Errors](https://vercel.com/docs/rest-api/sdk/feature-flags/create-a-flag#errors)[](https://vercel.com/docs/rest-api/sdk/feature-flags/create-a-flag#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid.
401The request is not authorized.
402The account was soft-blocked for an unhandled reason. The account is missing a payment so payment method must be updated
403You do not have permission to access this resource.
404Error
409Error
412Error
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

  const result = await vercel.featureFlags.createFlag({






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

  "description": "string",






3

  "variants": [






4

    {






5

      "description": "string",






6

      "label": "string",






7

      "value": "string",






8

      "id": "icfg_1234567890"






9

    }






10

  ],






11

  "id": "icfg_1234567890",






12

  "environments": "value",






13

  "kind": "string",






14

  "revision": "123",






15

  "seed": "123",






16

  "state": "active",






17

  "slug": "string",






18

  "createdAt": "123",






19

  "updatedAt": "123",






20

  "createdBy": "string",






21

  "ownerId": "example_id",






22

  "projectId": "example_id",






23

  "typeName": "flag"






24

}




```

Copy as MarkdownGive feedbackAsk AI about this page
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Update project flag settings
