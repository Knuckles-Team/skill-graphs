Menu
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Accept project transfer request
# Accept project transfer request
PUT`https://api.vercel.com/projects/transfer-request/{code}`
Accept a project transfer request initated by another team.
The `code` is generated using the `POST /projects/:idOrName/transfer-request` endpoint.
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

  const result = await vercel.projects.acceptProjectTransferRequest({






9

    code: "<value>",






10

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






11

    slug: "my-team-url-slug",






12

    requestBody: {






13

      newProjectName: "a-project-name",






14

    },






15

  });






16







17

  console.log(result);






18

}






19







20

run();




```

Response
```


1

{






2

  "partnerCalls": [






3

    {






4

      "installationId": "example_id",






5

      "resourceIds": [],






6

      "result": {






7

        "status": "errored",






8

        "error": "value",






9

        "code": "string"






10

      }






11

    }






12

  ],






13

  "resourceTransferErrors": [






14

    "value"






15

  ],






16

  "transferredStoreIds": []






17

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/projects/accept-project-transfer-request#authentication)[](https://vercel.com/docs/rest-api/sdk/projects/accept-project-transfer-request#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/projects/accept-project-transfer-request#path-parameters)[](https://vercel.com/docs/rest-api/sdk/projects/accept-project-transfer-request#path-parameters)
codestringRequired
The code of the project transfer request.
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/projects/accept-project-transfer-request#query-parameters)[](https://vercel.com/docs/rest-api/sdk/projects/accept-project-transfer-request#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Body](https://vercel.com/docs/rest-api/sdk/projects/accept-project-transfer-request#body)[](https://vercel.com/docs/rest-api/sdk/projects/accept-project-transfer-request#body)
application/json
newProjectNamestringOptional
The desired name for the project
paidFeaturesobjectOptional
+Show 3 properties
acceptedPoliciesobjectOptional
##  [Response](https://vercel.com/docs/rest-api/sdk/projects/accept-project-transfer-request#response)[](https://vercel.com/docs/rest-api/sdk/projects/accept-project-transfer-request#response)
202The project has been transferred successfully.
partnerCallsarrayRequired
+Show 3 properties
resourceTransferErrorsarrayRequired
transferredStoreIdsarrayRequired
##  [Errors](https://vercel.com/docs/rest-api/sdk/projects/accept-project-transfer-request#errors)[](https://vercel.com/docs/rest-api/sdk/projects/accept-project-transfer-request#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
422Error
