Menu
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Update an Edge Config
# Update an Edge Config
PUT`https://api.vercel.com/v1/edge-config/{edgeConfigId}`
Updates an Edge Config.
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

  const result = await vercel.edgeConfig.updateEdgeConfig({






9

    edgeConfigId: "<id>",






10

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






11

    slug: "my-team-url-slug",






12

    requestBody: {






13

      slug: "<value>",






14

    },






15

  });






16







17

  console.log(result);






18

}






19







20

run();




```

Response
```


1

{






2

  "transfer": {






3

    "fromAccountId": "example_id",






4

    "startedAt": "123",






5

    "doneAt": "123"






6

  },






7

  "id": "icfg_1234567890",






8

  "createdAt": "123",






9

  "createdBy": "string",






10

  "ownerId": "example_id",






11

  "slug": "string",






12

  "updatedAt": "123",






13

  "digest": "string",






14

  "purpose": {






15

    "type": "flags",






16

    "projectId": "example_id"






17

  },






18

  "deletedAt": "123",






19

  "schema": "value",






20

  "syncedToDynamoAt": "123",






21

  "sizeInBytes": "123",






22

  "itemCount": "123"






23

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/edge-config/update-an-edge-config#authentication)[](https://vercel.com/docs/rest-api/sdk/edge-config/update-an-edge-config#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/edge-config/update-an-edge-config#path-parameters)[](https://vercel.com/docs/rest-api/sdk/edge-config/update-an-edge-config#path-parameters)
edgeConfigIdstringRequired
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/edge-config/update-an-edge-config#query-parameters)[](https://vercel.com/docs/rest-api/sdk/edge-config/update-an-edge-config#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Body](https://vercel.com/docs/rest-api/sdk/edge-config/update-an-edge-config#body)[](https://vercel.com/docs/rest-api/sdk/edge-config/update-an-edge-config#body)
application/json
slugstringRequired
##  [Response](https://vercel.com/docs/rest-api/sdk/edge-config/update-an-edge-config#response)[](https://vercel.com/docs/rest-api/sdk/edge-config/update-an-edge-config#response)
200Success
transferobjectOptional
Keeps track of the current state of the Edge Config while it gets transferred.
+Show 3 properties
idstringRequired
createdAtnumberRequired
createdBystringOptional
The ID of the user who created the Edge Config, optional because it is not always set.
ownerIdstringRequired
slugstringRequired
Name for the Edge Config Names are not unique. Must start with an alphabetic character and can contain only alphanumeric characters and underscores).
updatedAtnumberRequired
digeststringRequired
purposeobjectOptional2 variants
+Show 2 variants
deletedAtnumberOptional
schemaobjectOptional
syncedToDynamoAtnumberOptional
Timestamp of when the Edge Config was synced to DynamoDB initially. It is only set when syncing the entire Edge Config, not when updating.
sizeInBytesnumberRequired
itemCountnumberRequired
##  [Errors](https://vercel.com/docs/rest-api/sdk/edge-config/update-an-edge-config#errors)[](https://vercel.com/docs/rest-api/sdk/edge-config/update-an-edge-config#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid.
401The request is not authorized.
402The account was soft-blocked for an unhandled reason. The account is missing a payment so payment method must be updated
403You do not have permission to access this resource.
404Error
409Error
