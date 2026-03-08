Menu
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Get Edge Config token meta data
# Get Edge Config token meta data
GET`https://api.vercel.com/v1/edge-config/{edgeConfigId}/token/{token}`
Return meta data about an Edge Config token.
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

  const result = await vercel.edgeConfig.getEdgeConfigToken({






9

    edgeConfigId: "<id>",






10

    token: "<value>",






11

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






12

    slug: "my-team-url-slug",






13

  });






14







15

  console.log(result);






16

}






17







18

run();




```

Response
```


1

{






2

  "token": "string",






3

  "label": "string",






4

  "id": "icfg_1234567890",






5

  "edgeConfigId": "example_id",






6

  "createdAt": "123"






7

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/edge-config/get-edge-config-token-meta-data#authentication)[](https://vercel.com/docs/rest-api/sdk/edge-config/get-edge-config-token-meta-data#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/edge-config/get-edge-config-token-meta-data#path-parameters)[](https://vercel.com/docs/rest-api/sdk/edge-config/get-edge-config-token-meta-data#path-parameters)
edgeConfigIdstringRequired
tokenstringRequired
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/edge-config/get-edge-config-token-meta-data#query-parameters)[](https://vercel.com/docs/rest-api/sdk/edge-config/get-edge-config-token-meta-data#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sdk/edge-config/get-edge-config-token-meta-data#response)[](https://vercel.com/docs/rest-api/sdk/edge-config/get-edge-config-token-meta-data#response)
200The EdgeConfig.
tokenstringRequired
labelstringRequired
idstringRequired
This is not the token itself, but rather an id to identify the token by
edgeConfigIdstringRequired
createdAtnumberRequired
##  [Errors](https://vercel.com/docs/rest-api/sdk/edge-config/get-edge-config-token-meta-data#errors)[](https://vercel.com/docs/rest-api/sdk/edge-config/get-edge-config-token-meta-data#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
