Menu
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Get rolling release billing status
# Get rolling release billing status
GET`https://api.vercel.com/v1/projects/{idOrName}/rolling-release/billing`
Get the Rolling Releases billing status for a project. The team level billing status is used to determine if the project can be configured for rolling releases.
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

  const result = await vercel.rollingRelease.getRollingReleaseBillingStatus({






9

    idOrName: "<value>",






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

  "availableSlots": "0",






3

  "reason": "plan_not_supported",






4

  "message": "string"






5

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/rolling-release/get-rolling-release-billing-status#authentication)[](https://vercel.com/docs/rest-api/sdk/rolling-release/get-rolling-release-billing-status#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/rolling-release/get-rolling-release-billing-status#path-parameters)[](https://vercel.com/docs/rest-api/sdk/rolling-release/get-rolling-release-billing-status#path-parameters)
idOrNamestringRequired
Project ID or project name (URL-encoded)
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/rolling-release/get-rolling-release-billing-status#query-parameters)[](https://vercel.com/docs/rest-api/sdk/rolling-release/get-rolling-release-billing-status#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sdk/rolling-release/get-rolling-release-billing-status#response)[](https://vercel.com/docs/rest-api/sdk/rolling-release/get-rolling-release-billing-status#response)
200Success
availableSlotsnumberRequired
+Show 1 enum values
reasonstringRequired
+Show 1 enum values
messagestringRequired
##  [Errors](https://vercel.com/docs/rest-api/sdk/rolling-release/get-rolling-release-billing-status#errors)[](https://vercel.com/docs/rest-api/sdk/rolling-release/get-rolling-release-billing-status#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
