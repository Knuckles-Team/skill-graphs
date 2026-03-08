Menu
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Delete routing rules
# Delete routing rules
DEL`https://api.vercel.com/v1/projects/{projectId}/routes`
Delete one or more routing rules from a project by ID. Stages a new version with the routes removed.
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

  const result = await vercel.projectRoutes.deleteRoutes({






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

{






2

  "deletedCount": "123",






3

  "version": {






4

    "id": "icfg_1234567890",






5

    "s3Key": "string",






6

    "lastModified": "123",






7

    "createdBy": "string",






8

    "isStaging": "false",






9

    "isLive": "false",






10

    "ruleCount": "123",






11

    "alias": "string"






12

  }






13

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/project-routes/delete-routing-rules#authentication)[](https://vercel.com/docs/rest-api/sdk/project-routes/delete-routing-rules#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/project-routes/delete-routing-rules#path-parameters)[](https://vercel.com/docs/rest-api/sdk/project-routes/delete-routing-rules#path-parameters)
projectIdstringRequired
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/project-routes/delete-routing-rules#query-parameters)[](https://vercel.com/docs/rest-api/sdk/project-routes/delete-routing-rules#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Body](https://vercel.com/docs/rest-api/sdk/project-routes/delete-routing-rules#body)[](https://vercel.com/docs/rest-api/sdk/project-routes/delete-routing-rules#body)
application/json
routeIdsarrayRequired
The IDs of the routes to delete
##  [Response](https://vercel.com/docs/rest-api/sdk/project-routes/delete-routing-rules#response)[](https://vercel.com/docs/rest-api/sdk/project-routes/delete-routing-rules#response)
200Success
deletedCountnumberRequired
versionobjectRequired
A version of routing rules stored in S3.
+Show 8 properties
##  [Errors](https://vercel.com/docs/rest-api/sdk/project-routes/delete-routing-rules#errors)[](https://vercel.com/docs/rest-api/sdk/project-routes/delete-routing-rules#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
