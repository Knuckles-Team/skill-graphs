# Delete rolling release configuration
DEL`https://api.vercel.com/v1/projects/{idOrName}/rolling-release/config`
Disable Rolling Releases for a project means that future deployments will not undergo a rolling release. Changing the config never alters a rollout that's already in-flight—it only affects the next production deployment. If you want to also stop the current rollout, call this endpoint to disable the feature, and then call either the /complete or /abort endpoint.
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

  const result = await vercel.rollingRelease.deleteRollingReleaseConfig({






9

    idOrName: "<value>",






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

  "rollingRelease": "value"






3

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/rolling-release/delete-rolling-release-configuration#authentication)[](https://vercel.com/docs/rest-api/sdk/rolling-release/delete-rolling-release-configuration#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/rolling-release/delete-rolling-release-configuration#path-parameters)[](https://vercel.com/docs/rest-api/sdk/rolling-release/delete-rolling-release-configuration#path-parameters)
idOrNamestringRequired
Project ID or project name (URL-encoded)
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/rolling-release/delete-rolling-release-configuration#query-parameters)[](https://vercel.com/docs/rest-api/sdk/rolling-release/delete-rolling-release-configuration#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sdk/rolling-release/delete-rolling-release-configuration#response)[](https://vercel.com/docs/rest-api/sdk/rolling-release/delete-rolling-release-configuration#response)
200Success
rollingReleaseobjectRequired
##  [Errors](https://vercel.com/docs/rest-api/sdk/rolling-release/delete-rolling-release-configuration#errors)[](https://vercel.com/docs/rest-api/sdk/rolling-release/delete-rolling-release-configuration#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
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

  const result = await vercel.rollingRelease.deleteRollingReleaseConfig({






9

    idOrName: "<value>",






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

  "rollingRelease": "value"






3

}




```

Copy as MarkdownGive feedbackAsk AI about this page
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Complete the rolling release for the project
