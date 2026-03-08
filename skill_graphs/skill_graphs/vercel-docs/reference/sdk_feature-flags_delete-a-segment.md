Menu
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Delete a segment
# Delete a segment
DEL`https://api.vercel.com/v1/projects/{projectIdOrName}/feature-flags/segments/{segmentIdOrSlug}`
Delete a feature flag segment.
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

  await vercel.featureFlags.deleteFlagSegment({






9

    projectIdOrName: "<value>",






10

    segmentIdOrSlug: "<value>",






11

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






12

    slug: "my-team-url-slug",






13

  });






14







15







16

}






17







18

run();




```

Response
```


1

{}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/feature-flags/delete-a-segment#authentication)[](https://vercel.com/docs/rest-api/sdk/feature-flags/delete-a-segment#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/feature-flags/delete-a-segment#path-parameters)[](https://vercel.com/docs/rest-api/sdk/feature-flags/delete-a-segment#path-parameters)
projectIdOrNamestringRequired
The project id or name
segmentIdOrSlugstringRequired
The segment slug
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/feature-flags/delete-a-segment#query-parameters)[](https://vercel.com/docs/rest-api/sdk/feature-flags/delete-a-segment#query-parameters)
withMetadatabooleanOptional
Whether to include metadata
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sdk/feature-flags/delete-a-segment#response)[](https://vercel.com/docs/rest-api/sdk/feature-flags/delete-a-segment#response)
204Success
##  [Errors](https://vercel.com/docs/rest-api/sdk/feature-flags/delete-a-segment#errors)[](https://vercel.com/docs/rest-api/sdk/feature-flags/delete-a-segment#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
402The account was soft-blocked for an unhandled reason. The account is missing a payment so payment method must be updated
403You do not have permission to access this resource.
404Error
409Error
412Error
