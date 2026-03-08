Menu
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Create an Auth Token
# Create an Auth Token
POST`https://api.vercel.com/v3/user/tokens`
Creates and returns a new authentication token for the currently authenticated User. The `bearerToken` property is only provided once, in the response body, so be sure to save it on the client for use with API requests.
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

  const result = await vercel.authentication.createAuthToken({






9

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






10

    slug: "my-team-url-slug",






11

    requestBody: {






12

      name: "<value>",






13

    },






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

{






2

  "token": {






3

    "id": "5d9f2ebd38ddca62e5d51e9c1704c72530bdc8bfdd41e782a6687c48399e8391",






4

    "name": "Example Name",






5

    "type": "oauth2-token",






6

    "prefix": "vcp_",






7

    "suffix": "abc123",






8

    "origin": "github",






9

    "scopes": [






10

      {






11

        "type": "user",






12

        "sudo": {






13

          "origin": "totp",






14

          "expiresAt": "123"






15

        },






16

        "origin": "saml",






17

        "createdAt": "123",






18

        "expiresAt": "123"






19

      }






20

    ],






21

    "createdAt": "1632816536002",






22

    "activeAt": "1632816536002",






23

    "expiresAt": "1632816536002",






24

    "leakedAt": "1632816536002",






25

    "leakedUrl": "https://example.com"






26

  },






27

  "bearerToken": "uRKJSTt0L4RaSkiMj41QTkxM"






28

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/authentication/create-an-auth-token#authentication)[](https://vercel.com/docs/rest-api/sdk/authentication/create-an-auth-token#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/authentication/create-an-auth-token#query-parameters)[](https://vercel.com/docs/rest-api/sdk/authentication/create-an-auth-token#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Body](https://vercel.com/docs/rest-api/sdk/authentication/create-an-auth-token#body)[](https://vercel.com/docs/rest-api/sdk/authentication/create-an-auth-token#body)
application/json
namestringRequired
expiresAtnumberOptional
projectIdstringOptional
The ID of the project to scope this token to
##  [Response](https://vercel.com/docs/rest-api/sdk/authentication/create-an-auth-token#response)[](https://vercel.com/docs/rest-api/sdk/authentication/create-an-auth-token#response)
200Successful response.
tokenobjectRequired
Authentication token metadata.
+Show 12 properties
bearerTokenstringRequired
The authentication token's actual value. This token is only provided in this response, and can never be retrieved again in the future. Be sure to save it somewhere safe!
##  [Errors](https://vercel.com/docs/rest-api/sdk/authentication/create-an-auth-token#errors)[](https://vercel.com/docs/rest-api/sdk/authentication/create-an-auth-token#errors)
400One of the provided values in the request body is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
