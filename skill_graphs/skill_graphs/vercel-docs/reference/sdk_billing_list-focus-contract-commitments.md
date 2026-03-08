Menu
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
List FOCUS contract commitments
# List FOCUS contract commitments
GET`https://api.vercel.com/v1/billing/contract-commitments`
Returns commitment allocations per contract period in FOCUS v1.3 JSONL format for a specified Vercel team. The response is streamed as newline-delimited JSON (JSONL). This endpoint is only applicable to Enterprise Vercel customers. An empty response is returned for non-Enterprise (Pro/Flex) customers.
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

  const result = await vercel.billing.listContractCommitments({






9

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






10

    slug: "my-team-url-slug",






11

  });






12







13

  for await (const event of result) {






14

    // Handle the event






15

    console.log(event);






16

  }






17

}






18







19

run();




```

Response
```


1

{}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/billing/list-focus-contract-commitments#authentication)[](https://vercel.com/docs/rest-api/sdk/billing/list-focus-contract-commitments#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/billing/list-focus-contract-commitments#query-parameters)[](https://vercel.com/docs/rest-api/sdk/billing/list-focus-contract-commitments#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sdk/billing/list-focus-contract-commitments#response)[](https://vercel.com/docs/rest-api/sdk/billing/list-focus-contract-commitments#response)
200Success
##  [Errors](https://vercel.com/docs/rest-api/sdk/billing/list-focus-contract-commitments#errors)[](https://vercel.com/docs/rest-api/sdk/billing/list-focus-contract-commitments#errors)
400Error
401The request is not authorized.
403You do not have permission to access this resource.
404Error
