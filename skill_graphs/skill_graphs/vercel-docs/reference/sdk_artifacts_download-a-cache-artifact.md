Menu
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Download a cache artifact
# Download a cache artifact
GET`https://api.vercel.com/v8/artifacts/{hash}`
Downloads a cache artifact identified by its `hash` specified on the request path. The artifact is downloaded as an octet-stream. The client should verify the content-length header and response body.
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

  const result = await vercel.artifacts.downloadArtifact({






9

    xArtifactClientCi: "VERCEL",






10

    xArtifactClientInteractive: 0,






11

    hash: "12HKQaOmR5t5Uy6vdcQsNIiZgHGB",






12

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






13

    slug: "my-team-url-slug",






14

  });






15







16

  console.log(result);






17

}






18







19

run();




```

Response
```


1
"string"



```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/artifacts/download-a-cache-artifact#authentication)[](https://vercel.com/docs/rest-api/sdk/artifacts/download-a-cache-artifact#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/artifacts/download-a-cache-artifact#path-parameters)[](https://vercel.com/docs/rest-api/sdk/artifacts/download-a-cache-artifact#path-parameters)
hashstringRequired
The artifact hash
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/artifacts/download-a-cache-artifact#query-parameters)[](https://vercel.com/docs/rest-api/sdk/artifacts/download-a-cache-artifact#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Header parameters](https://vercel.com/docs/rest-api/sdk/artifacts/download-a-cache-artifact#header-parameters)[](https://vercel.com/docs/rest-api/sdk/artifacts/download-a-cache-artifact#header-parameters)
x-artifact-client-cistringOptional
The continuous integration or delivery environment where this artifact is downloaded.
x-artifact-client-interactiveintegerOptional
1 if the client is an interactive shell. Otherwise 0
##  [Response](https://vercel.com/docs/rest-api/sdk/artifacts/download-a-cache-artifact#response)[](https://vercel.com/docs/rest-api/sdk/artifacts/download-a-cache-artifact#response)
200The artifact was found and is downloaded as a stream. Content-Length should be verified.
##  [Errors](https://vercel.com/docs/rest-api/sdk/artifacts/download-a-cache-artifact#errors)[](https://vercel.com/docs/rest-api/sdk/artifacts/download-a-cache-artifact#errors)
400One of the provided values in the request query is invalid. One of the provided values in the headers is invalid
401The request is not authorized.
402The account was soft-blocked for an unhandled reason. The account is missing a payment so payment method must be updated
403The customer has reached their spend cap limit and has been paused. An owner can disable the cap or raise the limit in settings. The Remote Caching usage limit has been reached for this account for this billing cycle. Remote Caching has been disabled for this team or user. An owner can enable it in the billing settings. You do not have permission to access this resource.
404The artifact was not found
