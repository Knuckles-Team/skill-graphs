Menu
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Dangerously delete by source image
# Dangerously delete by source image
POST`https://api.vercel.com/v1/edge-cache/dangerously-delete-by-src-images`
Marks a source image as deleted, causing cache entries associated with that source image to be revalidated in the foreground on the next request. Use this method with caution because one source image can be associated with many paths and deleting the cache can cause many concurrent requests to the origin leading to cache stampede problem. This method is for advanced use cases and is not recommended; prefer using `invalidateBySrcImage` instead.
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

  await vercel.edgeCache.dangerouslyDeleteBySrcImages({






9

    projectIdOrName: "<value>",






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

##  [Authentication](https://vercel.com/docs/rest-api/sdk/edge-cache/dangerously-delete-by-source-image#authentication)[](https://vercel.com/docs/rest-api/sdk/edge-cache/dangerously-delete-by-source-image#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/edge-cache/dangerously-delete-by-source-image#query-parameters)[](https://vercel.com/docs/rest-api/sdk/edge-cache/dangerously-delete-by-source-image#query-parameters)
projectIdOrNamestringRequired
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Body](https://vercel.com/docs/rest-api/sdk/edge-cache/dangerously-delete-by-source-image#body)[](https://vercel.com/docs/rest-api/sdk/edge-cache/dangerously-delete-by-source-image#body)
application/json
revalidationDeadlineSecondsnumberOptional
srcImagesarrayRequired
##  [Response](https://vercel.com/docs/rest-api/sdk/edge-cache/dangerously-delete-by-source-image#response)[](https://vercel.com/docs/rest-api/sdk/edge-cache/dangerously-delete-by-source-image#response)
200Success
##  [Errors](https://vercel.com/docs/rest-api/sdk/edge-cache/dangerously-delete-by-source-image#errors)[](https://vercel.com/docs/rest-api/sdk/edge-cache/dangerously-delete-by-source-image#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid.
401The request is not authorized.
402Error
403You do not have permission to access this resource.
404Error
