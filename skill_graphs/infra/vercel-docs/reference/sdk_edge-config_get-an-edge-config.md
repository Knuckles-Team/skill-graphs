Menu
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Get an Edge Config
# Get an Edge Config
GET`https://api.vercel.com/v1/edge-config/{edgeConfigId}`
Returns an Edge Config.
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

  const result = await vercel.edgeConfig.getEdgeConfig({






9

    edgeConfigId: "<id>",






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

##  [Authentication](https://vercel.com/docs/rest-api/sdk/edge-config/get-an-edge-config#authentication)[](https://vercel.com/docs/rest-api/sdk/edge-config/get-an-edge-config#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/edge-config/get-an-edge-config#path-parameters)[](https://vercel.com/docs/rest-api/sdk/edge-config/get-an-edge-config#path-parameters)
edgeConfigIdstringRequired
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/edge-config/get-an-edge-config#query-parameters)[](https://vercel.com/docs/rest-api/sdk/edge-config/get-an-edge-config#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sdk/edge-config/get-an-edge-config#response)[](https://vercel.com/docs/rest-api/sdk/edge-config/get-an-edge-config#response)
200The EdgeConfig.
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
##  [Errors](https://vercel.com/docs/rest-api/sdk/edge-config/get-an-edge-config#errors)[](https://vercel.com/docs/rest-api/sdk/edge-config/get-an-edge-config#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
