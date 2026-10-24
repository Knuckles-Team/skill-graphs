Menu
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Gets project-level redirects.
# Gets project-level redirects.
GET`https://api.vercel.com/v1/bulk-redirects`
Get the version history for a project's bulk redirects
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

  const result = await vercel.bulkRedirects.getRedirects({






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

##  [Authentication](https://vercel.com/docs/rest-api/sdk/bulk-redirects/gets-project-level-redirects#authentication)[](https://vercel.com/docs/rest-api/sdk/bulk-redirects/gets-project-level-redirects#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/bulk-redirects/gets-project-level-redirects#query-parameters)[](https://vercel.com/docs/rest-api/sdk/bulk-redirects/gets-project-level-redirects#query-parameters)
projectIdstringRequired
versionIdstringOptional
qstringOptional
diffanyOptional
pageintegerOptional
per_pageintegerOptional
sort_bystringOptional
+Show 3 enum values
sort_orderstringOptional
+Show 2 enum values
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sdk/bulk-redirects/gets-project-level-redirects#response)[](https://vercel.com/docs/rest-api/sdk/bulk-redirects/gets-project-level-redirects#response)
200Success
##  [Errors](https://vercel.com/docs/rest-api/sdk/bulk-redirects/gets-project-level-redirects#errors)[](https://vercel.com/docs/rest-api/sdk/bulk-redirects/gets-project-level-redirects#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
