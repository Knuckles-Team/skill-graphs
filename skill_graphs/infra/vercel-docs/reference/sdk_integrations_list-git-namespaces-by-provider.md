Menu
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
List git namespaces by provider
# List git namespaces by provider
GET`https://api.vercel.com/v1/integrations/git-namespaces`
Lists git namespaces for a supported provider. Supported providers are `github`, `gitlab` and `bitbucket`. If the provider is not provided, it will try to obtain it from the user that authenticated the request.
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

  const result = await vercel.integrations.gitNamespaces({






9

    host: "ghes-test.now.systems",






10

  });






11







12

  console.log(result);






13

}






14







15

run();




```

Response
```


1

[






2

  {






3

    "provider": "example_id",






4

    "slug": "string",






5

    "id": "icfg_1234567890",






6

    "ownerType": "string",






7

    "name": "Example Name",






8

    "isAccessRestricted": "false",






9

    "installationId": "123",






10

    "requireReauth": "false"






11

  }






12

]




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/integrations/list-git-namespaces-by-provider#authentication)[](https://vercel.com/docs/rest-api/sdk/integrations/list-git-namespaces-by-provider#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/integrations/list-git-namespaces-by-provider#query-parameters)[](https://vercel.com/docs/rest-api/sdk/integrations/list-git-namespaces-by-provider#query-parameters)
hoststringOptional
The custom Git host if using a custom Git provider, like GitHub Enterprise Server
provideranyOptional
+Show 5 enum values
##  [Response](https://vercel.com/docs/rest-api/sdk/integrations/list-git-namespaces-by-provider#response)[](https://vercel.com/docs/rest-api/sdk/integrations/list-git-namespaces-by-provider#response)
200Success
##  [Errors](https://vercel.com/docs/rest-api/sdk/integrations/list-git-namespaces-by-provider#errors)[](https://vercel.com/docs/rest-api/sdk/integrations/list-git-namespaces-by-provider#errors)
400One of the provided values in the request query is invalid.
401Error
403You do not have permission to access this resource.
404Error
429Error
500Error
