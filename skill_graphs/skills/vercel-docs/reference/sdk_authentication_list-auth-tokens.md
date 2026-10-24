Menu
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
List Auth Tokens
# List Auth Tokens
GET`https://api.vercel.com/v5/user/tokens`
Retrieve a list of the current User's authentication tokens.
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

  const result = await vercel.authentication.listAuthTokens();






9







10

  console.log(result);






11

}






12







13

run();




```

Response
```


1

{






2

  "tokens": [






3

    {






4

      "id": "5d9f2ebd38ddca62e5d51e9c1704c72530bdc8bfdd41e782a6687c48399e8391",






5

      "name": "Example Name",






6

      "type": "oauth2-token",






7

      "prefix": "vcp_",






8

      "suffix": "abc123",






9

      "origin": "github",






10

      "scopes": [






11

        {






12

          "type": "user",






13

          "sudo": {






14

            "origin": "totp",






15

            "expiresAt": "123"






16

          },






17

          "origin": "saml",






18

          "createdAt": "123",






19

          "expiresAt": "123"






20

        }






21

      ],






22

      "createdAt": "1632816536002",






23

      "activeAt": "1632816536002",






24

      "expiresAt": "1632816536002",






25

      "leakedAt": "1632816536002",






26

      "leakedUrl": "https://example.com"






27

    }






28

  ],






29

  "pagination": {






30

    "count": "20",






31

    "next": "1540095775951",






32

    "prev": "1540095775951"






33

  }






34

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/authentication/list-auth-tokens#authentication)[](https://vercel.com/docs/rest-api/sdk/authentication/list-auth-tokens#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Response](https://vercel.com/docs/rest-api/sdk/authentication/list-auth-tokens#response)[](https://vercel.com/docs/rest-api/sdk/authentication/list-auth-tokens#response)
200Success
tokensarrayRequired
+Show 12 properties
paginationobjectRequired
This object contains information related to the pagination of the current request, including the necessary parameters to get the next or previous page of data.
+Show 3 properties
##  [Errors](https://vercel.com/docs/rest-api/sdk/authentication/list-auth-tokens#errors)[](https://vercel.com/docs/rest-api/sdk/authentication/list-auth-tokens#errors)
400Error
401The request is not authorized.
403You do not have permission to access this resource.
