# Update the rolling release settings for the project
PATCH`https://api.vercel.com/v1/projects/{idOrName}/rolling-release/config`
Update (or disable) Rolling Releases for a project. When disabling with the resolve-on-disable feature flag enabled, any active rolling release document is resolved using the disableRolloutAction parameter: "abort" to roll back (default), or "complete" to promote the canary to production. When enabling or updating config, changes only affect the next production deployment and do not alter a rollout that's already in-flight. Note: Enabling Rolling Releases automatically enables skew protection on the project with the default value if it wasn't configured already.
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

  const result = await vercel.rollingRelease.updateRollingReleaseConfig({






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

##  [Authentication](https://vercel.com/docs/rest-api/sdk/rolling-release/update-the-rolling-release-settings-for-the-project#authentication)[](https://vercel.com/docs/rest-api/sdk/rolling-release/update-the-rolling-release-settings-for-the-project#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/rolling-release/update-the-rolling-release-settings-for-the-project#path-parameters)[](https://vercel.com/docs/rest-api/sdk/rolling-release/update-the-rolling-release-settings-for-the-project#path-parameters)
idOrNamestringRequired
Project ID or project name (URL-encoded)
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/rolling-release/update-the-rolling-release-settings-for-the-project#query-parameters)[](https://vercel.com/docs/rest-api/sdk/rolling-release/update-the-rolling-release-settings-for-the-project#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sdk/rolling-release/update-the-rolling-release-settings-for-the-project#response)[](https://vercel.com/docs/rest-api/sdk/rolling-release/update-the-rolling-release-settings-for-the-project#response)
200Success
rollingReleaseobjectRequired
##  [Errors](https://vercel.com/docs/rest-api/sdk/rolling-release/update-the-rolling-release-settings-for-the-project#errors)[](https://vercel.com/docs/rest-api/sdk/rolling-release/update-the-rolling-release-settings-for-the-project#errors)
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

  const result = await vercel.rollingRelease.updateRollingReleaseConfig({






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
Update the active rolling release to the next stage for a project
