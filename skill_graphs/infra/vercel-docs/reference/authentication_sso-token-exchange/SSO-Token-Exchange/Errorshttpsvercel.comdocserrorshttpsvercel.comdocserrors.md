##  [Errors](https://vercel.com/docs#errors)[](https://vercel.com/docs#errors)
400One of the provided values in the request body is invalid.
403Error
500Error
TypeScriptNext.jscURL
https://api.vercel.com/v1/integrations/sso/token
```


1

const response = await fetch('https://api.vercel.com/v1/integrations/sso/token', {






2

  method: 'POST',






3

  headers: {






4

    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',






5

    'Content-Type': 'application/json',






6

  },






7

  body: JSON.stringify({






8

    "code": "string",






9

    "state": "string",






10

    "client_id": "example_id",






11

    "client_secret": "string",






12

    "redirect_uri": "https://example.com",






13

    "grant_type": "authorization_code"






14

  }),






15

});






16







17

const data = await response.json();






18

console.log(data);




```

Response
```


1

{






2

  "id_token": "example_id",






3

  "token_type": "string",






4

  "expires_in": "123",






5

  "access_token": "string",






6

  "refresh_token": "string"






7

}




```

Copy as MarkdownGive feedbackAsk AI about this page
