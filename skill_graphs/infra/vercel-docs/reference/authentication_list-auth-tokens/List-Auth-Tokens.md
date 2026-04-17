# List Auth Tokens
GET`https://api.vercel.com/v5/user/tokens`
Retrieve a list of the current User's authentication tokens.
TypeScriptNext.jscURL
https://api.vercel.com/v5/user/tokens
```


1

const response = await fetch('https://api.vercel.com/v5/user/tokens', {






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
