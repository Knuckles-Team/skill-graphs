Menu
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Read active attack data
# Read active attack data
GET`https://api.vercel.com/v1/security/firewall/attack-status`
Retrieve active attack data within the last N days (default: 1 day)
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

  const result = await vercel.security.getActiveAttackStatus({






9

    projectId: "<id>",






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
"value"



```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/security/read-active-attack-data#authentication)[](https://vercel.com/docs/rest-api/sdk/security/read-active-attack-data#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/security/read-active-attack-data#query-parameters)[](https://vercel.com/docs/rest-api/sdk/security/read-active-attack-data#query-parameters)
projectIdstringRequired
sincenumberOptional
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sdk/security/read-active-attack-data#response)[](https://vercel.com/docs/rest-api/sdk/security/read-active-attack-data#response)
200Success
##  [Errors](https://vercel.com/docs/rest-api/sdk/security/read-active-attack-data#errors)[](https://vercel.com/docs/rest-api/sdk/security/read-active-attack-data#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
