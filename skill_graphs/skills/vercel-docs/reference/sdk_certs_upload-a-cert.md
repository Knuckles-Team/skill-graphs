Menu
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Upload a cert
# Upload a cert
PUT`https://api.vercel.com/v8/certs`
Upload a cert
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

  const result = await vercel.certs.uploadCert({






9

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






10

    slug: "my-team-url-slug",






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

  "id": "icfg_1234567890",






3

  "createdAt": "123",






4

  "expiresAt": "123",






5

  "autoRenew": "false",






6

  "cns": []






7

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/certs/upload-a-cert#authentication)[](https://vercel.com/docs/rest-api/sdk/certs/upload-a-cert#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/certs/upload-a-cert#query-parameters)[](https://vercel.com/docs/rest-api/sdk/certs/upload-a-cert#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Body](https://vercel.com/docs/rest-api/sdk/certs/upload-a-cert#body)[](https://vercel.com/docs/rest-api/sdk/certs/upload-a-cert#body)
application/json
castringRequired
The certificate authority
keystringRequired
The certificate key
certstringRequired
The certificate
skipValidationbooleanOptional
Skip validation of the certificate
##  [Response](https://vercel.com/docs/rest-api/sdk/certs/upload-a-cert#response)[](https://vercel.com/docs/rest-api/sdk/certs/upload-a-cert#response)
200Success
idstringRequired
createdAtnumberRequired
expiresAtnumberRequired
autoRenewbooleanRequired
+Show 2 enum values
cnsarrayRequired
##  [Errors](https://vercel.com/docs/rest-api/sdk/certs/upload-a-cert#errors)[](https://vercel.com/docs/rest-api/sdk/certs/upload-a-cert#errors)
400One of the provided values in the request body is invalid.
401The request is not authorized.
402This feature is only available for Enterprise customers.
403You do not have permission to access this resource.
