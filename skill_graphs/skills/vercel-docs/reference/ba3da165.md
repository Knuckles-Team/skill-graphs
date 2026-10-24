# SSO Token Exchange
POST`https://api.vercel.com/v1/integrations/sso/token`
During the authorization process, Vercel sends the user to the provider [redirectLoginUrl](https://vercel.com/docs/integrations/create-integration/submit-integration#redirect-login-url), that includes the OAuth authorization `code` parameter. The provider then calls the SSO Token Exchange endpoint with the sent code and receives the OIDC token. They log the user in based on this token and redirects the user back to the Vercel account using deep-link parameters included the redirectLoginUrl. Providers should not persist the returned `id_token` in a database since the token will expire. See [**Authentication with SSO**](https://vercel.com/docs/integrations/create-integration/marketplace-api#authentication-with-sso) for more details.
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
