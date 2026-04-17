Menu
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
List git repositories linked to namespace by provider
# List git repositories linked to namespace by provider
GET`https://api.vercel.com/v1/integrations/search-repo`
Lists git repositories linked to a namespace `id` for a supported provider. A specific namespace `id` can be obtained via the `git-namespaces` endpoint. Supported providers are `github`, `gitlab` and `bitbucket`. If the provider or namespace is not provided, it will try to obtain it from the user that authenticated the request.
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

  const result = await vercel.integrations.searchRepo({






9

    host: "ghes-test.now.systems",






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

##  [Authentication](https://vercel.com/docs/rest-api/sdk/integrations/list-git-repositories-linked-to-namespace-by-provider#authentication)[](https://vercel.com/docs/rest-api/sdk/integrations/list-git-repositories-linked-to-namespace-by-provider#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/integrations/list-git-repositories-linked-to-namespace-by-provider#query-parameters)[](https://vercel.com/docs/rest-api/sdk/integrations/list-git-repositories-linked-to-namespace-by-provider#query-parameters)
querystringOptional
namespaceIdanyOptional
provideranyOptional
+Show 5 enum values
installationIdstringOptional
hoststringOptional
The custom Git host if using a custom Git provider, like GitHub Enterprise Server
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sdk/integrations/list-git-repositories-linked-to-namespace-by-provider#response)[](https://vercel.com/docs/rest-api/sdk/integrations/list-git-repositories-linked-to-namespace-by-provider#response)
200Success
##  [Errors](https://vercel.com/docs/rest-api/sdk/integrations/list-git-repositories-linked-to-namespace-by-provider#errors)[](https://vercel.com/docs/rest-api/sdk/integrations/list-git-repositories-linked-to-namespace-by-provider#errors)
400One of the provided values in the request query is invalid.
401Error
403You do not have permission to access this resource.
404Error
429Error
500Error
