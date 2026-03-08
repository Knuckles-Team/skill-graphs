Menu
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Update Resource
# Update Resource
PATCH`https://api.vercel.com/v1/installations/{integrationConfigurationId}/resources/{resourceId}`
This endpoint updates an existing resource in the installation. All parameters are optional, allowing partial updates.
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

  const result = await vercel.marketplace.updateResource({






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

  "name": "Example Name"






3

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/marketplace/update-resource#authentication)[](https://vercel.com/docs/rest-api/sdk/marketplace/update-resource#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/marketplace/update-resource#path-parameters)[](https://vercel.com/docs/rest-api/sdk/marketplace/update-resource#path-parameters)
integrationConfigurationIdstringRequired
resourceIdstringRequired
##  [Body](https://vercel.com/docs/rest-api/sdk/marketplace/update-resource#body)[](https://vercel.com/docs/rest-api/sdk/marketplace/update-resource#body)
application/json
ownershipstringOptional
+Show 3 enum values
namestringOptional
statusstringOptional
+Show 7 enum values
metadataobjectOptional
billingPlanobjectOptional
+Show 9 properties
notificationobjectOptional
+Show 4 properties
extrasobjectOptional
secretsobjectOptional
+Show 2 properties
##  [Response](https://vercel.com/docs/rest-api/sdk/marketplace/update-resource#response)[](https://vercel.com/docs/rest-api/sdk/marketplace/update-resource#response)
200Success
namestringRequired
##  [Errors](https://vercel.com/docs/rest-api/sdk/marketplace/update-resource#errors)[](https://vercel.com/docs/rest-api/sdk/marketplace/update-resource#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
409Error
422Error
