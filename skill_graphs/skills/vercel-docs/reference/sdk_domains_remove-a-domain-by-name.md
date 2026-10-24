Menu
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Remove a domain by name
# Remove a domain by name
DEL`https://api.vercel.com/v6/domains/{domain}`
Delete a previously registered domain name from Vercel. Deleting a domain will automatically remove any associated aliases.
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

  const result = await vercel.domains.deleteDomain({






9

    domain: "example.com",






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

{






2

  "uid": "example_id"






3

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/domains/remove-a-domain-by-name#authentication)[](https://vercel.com/docs/rest-api/sdk/domains/remove-a-domain-by-name#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/domains/remove-a-domain-by-name#path-parameters)[](https://vercel.com/docs/rest-api/sdk/domains/remove-a-domain-by-name#path-parameters)
domainstringRequired
The name of the domain.
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/domains/remove-a-domain-by-name#query-parameters)[](https://vercel.com/docs/rest-api/sdk/domains/remove-a-domain-by-name#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sdk/domains/remove-a-domain-by-name#response)[](https://vercel.com/docs/rest-api/sdk/domains/remove-a-domain-by-name#response)
200Successful response removing a domain.
uidstringRequired
##  [Errors](https://vercel.com/docs/rest-api/sdk/domains/remove-a-domain-by-name#errors)[](https://vercel.com/docs/rest-api/sdk/domains/remove-a-domain-by-name#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
409Error
