##  [Errors](https://vercel.com/docs#errors)[](https://vercel.com/docs#errors)
400One of the provided values in the request query is invalid.
401Error
403You do not have permission to access this resource.
404Token not found with the requested `tokenId`.
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

  const result = await vercel.authentication.getAuthToken({






9

    tokenId: "5d9f2ebd38ddca62e5d51e9c1704c72530bdc8bfdd41e782a6687c48399e8391",






10

  });






11







12

  console.log(result);






13

}






14







15

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

  }






27

}




```

Copy as MarkdownGive feedbackAsk AI about this page
