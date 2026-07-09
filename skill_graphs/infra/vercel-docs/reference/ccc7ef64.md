# Get Auth Token Metadata
GET`https://api.vercel.com/v5/user/tokens/{tokenId}`
Retrieve metadata about an authentication token belonging to the currently authenticated User.
TypeScriptNext.jscURL
https://api.vercel.com/v5/user/tokens/{tokenId}
```


1

const response = await fetch('https://api.vercel.com/v5/user/tokens/tokenId', {






2

  method: 'GET',






3

  headers: {






4

    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',






5

    'Content-Type': 'application/json',






6

  },






7

});






8







9

const data = await response.json();






10

console.log(data);




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
