Menu
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
List Deployment Aliases
# List Deployment Aliases
GET`https://api.vercel.com/v2/deployments/{id}/aliases`
Retrieves all Aliases for the Deployment with the given ID. The authenticated user or team must own the deployment.
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

  const result = await vercel.aliases.listDeploymentAliases({






9

    id: "dpl_FjvFJncQHQcZMznrUm9EoB8sFuPa",






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

  "aliases": [






3

    {






4

      "uid": "2WjyKQmM8ZnGcJsPWMrHRHrE",






5

      "alias": "my-alias.vercel.app",






6

      "created": "2017-04-26T23:00:34.232Z",






7

      "redirect": "string",






8

      "protectionBypass": "value"






9

    }






10

  ]






11

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/aliases/list-deployment-aliases#authentication)[](https://vercel.com/docs/rest-api/sdk/aliases/list-deployment-aliases#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/aliases/list-deployment-aliases#path-parameters)[](https://vercel.com/docs/rest-api/sdk/aliases/list-deployment-aliases#path-parameters)
idstringRequired
The ID of the deployment the aliases should be listed for
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/aliases/list-deployment-aliases#query-parameters)[](https://vercel.com/docs/rest-api/sdk/aliases/list-deployment-aliases#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sdk/aliases/list-deployment-aliases#response)[](https://vercel.com/docs/rest-api/sdk/aliases/list-deployment-aliases#response)
200The list of aliases assigned to the deployment
aliasesarrayRequired
A list of the aliases assigned to the deployment
+Show 5 properties
##  [Errors](https://vercel.com/docs/rest-api/sdk/aliases/list-deployment-aliases#errors)[](https://vercel.com/docs/rest-api/sdk/aliases/list-deployment-aliases#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404The deployment was not found
