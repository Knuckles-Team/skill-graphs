Menu
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Unpause a project
# Unpause a project
POST`https://api.vercel.com/v1/projects/{projectId}/unpause`
Unpause a project by passing its project `id` in the URL. If the project does not exist given the id then the request will fail with 400 status code. If the project enables auto assigning custom production domains and unblocks the active Production Deployment then the request will return with 200 status code.
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

  await vercel.projects.unpauseProject({






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







15

}






16







17

run();




```

Response
```


1

{}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/projects/unpause-a-project#authentication)[](https://vercel.com/docs/rest-api/sdk/projects/unpause-a-project#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/projects/unpause-a-project#path-parameters)[](https://vercel.com/docs/rest-api/sdk/projects/unpause-a-project#path-parameters)
projectIdstringRequired
The unique project identifier
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/projects/unpause-a-project#query-parameters)[](https://vercel.com/docs/rest-api/sdk/projects/unpause-a-project#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sdk/projects/unpause-a-project#response)[](https://vercel.com/docs/rest-api/sdk/projects/unpause-a-project#response)
200Success
##  [Errors](https://vercel.com/docs/rest-api/sdk/projects/unpause-a-project#errors)[](https://vercel.com/docs/rest-api/sdk/projects/unpause-a-project#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
500Error
