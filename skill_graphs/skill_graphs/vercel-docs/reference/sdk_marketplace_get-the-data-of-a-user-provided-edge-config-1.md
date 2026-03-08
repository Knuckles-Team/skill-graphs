Menu
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Get the data of a user-provided Edge Config
# Get the data of a user-provided Edge Config
HEAD`https://api.vercel.com/v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/edge-config`
When the user enabled Edge Config syncing, then this endpoint can be used by the partner to fetch the contents of the Edge Config.
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

  const result = await vercel.marketplace.createInstallationIntegrationEdgeConfig({






9

    integrationConfigurationId: "<id>",






10

    resourceId: "<id>",






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

  "items": "value",






3

  "updatedAt": "123",






4

  "digest": "string",






5

  "purpose": "flags"






6

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/marketplace/get-the-data-of-a-user-provided-edge-config-1#authentication)[](https://vercel.com/docs/rest-api/sdk/marketplace/get-the-data-of-a-user-provided-edge-config-1#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/marketplace/get-the-data-of-a-user-provided-edge-config-1#path-parameters)[](https://vercel.com/docs/rest-api/sdk/marketplace/get-the-data-of-a-user-provided-edge-config-1#path-parameters)
integrationConfigurationIdstringRequired
resourceIdstringRequired
##  [Response](https://vercel.com/docs/rest-api/sdk/marketplace/get-the-data-of-a-user-provided-edge-config-1#response)[](https://vercel.com/docs/rest-api/sdk/marketplace/get-the-data-of-a-user-provided-edge-config-1#response)
200The Edge Config data
itemsobjectRequired
updatedAtnumberRequired
digeststringRequired
purposestringOptional
+Show 2 enum values
##  [Errors](https://vercel.com/docs/rest-api/sdk/marketplace/get-the-data-of-a-user-provided-edge-config-1#errors)[](https://vercel.com/docs/rest-api/sdk/marketplace/get-the-data-of-a-user-provided-edge-config-1#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
