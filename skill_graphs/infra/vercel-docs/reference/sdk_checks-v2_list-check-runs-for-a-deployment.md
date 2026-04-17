Menu
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
List check runs for a deployment
# List check runs for a deployment
GET`https://api.vercel.com/v2/deployments/{deploymentId}/check-runs`
List all check runs for a deployment.
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

  const result = await vercel.checksV2.listDeploymentCheckRuns({






9

    deploymentId: "<id>",






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

  "runs": [






3

    {






4

      "id": "icfg_1234567890",






5

      "name": "Example Name",






6

      "checkId": "example_id",






7

      "ownerId": "example_id",






8

      "deploymentId": "example_id",






9

      "projectId": "example_id",






10

      "source": {






11

        "kind": "integration",






12

        "integrationId": "example_id",






13

        "integrationConfigurationId": "example_id",






14

        "resourceId": "example_id",






15

        "externalResourceId": "example_id"






16

      },






17

      "requires": "build-ready",






18

      "blocks": "none",






19

      "targets": [],






20

      "status": "queued",






21

      "conclusion": "timeout",






22

      "conclusionText": "string",






23

      "externalId": "example_id",






24

      "externalUrl": "https://example.com",






25

      "output": "value",






26

      "timeout": "123",






27

      "createdAt": "123",






28

      "updatedAt": "123",






29

      "completedAt": "123"






30

    }






31

  ]






32

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/checks-v2/list-check-runs-for-a-deployment#authentication)[](https://vercel.com/docs/rest-api/sdk/checks-v2/list-check-runs-for-a-deployment#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/checks-v2/list-check-runs-for-a-deployment#path-parameters)[](https://vercel.com/docs/rest-api/sdk/checks-v2/list-check-runs-for-a-deployment#path-parameters)
deploymentIdstringRequired
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/checks-v2/list-check-runs-for-a-deployment#query-parameters)[](https://vercel.com/docs/rest-api/sdk/checks-v2/list-check-runs-for-a-deployment#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sdk/checks-v2/list-check-runs-for-a-deployment#response)[](https://vercel.com/docs/rest-api/sdk/checks-v2/list-check-runs-for-a-deployment#response)
200Success
runsarrayRequired
+Show 20 properties
##  [Errors](https://vercel.com/docs/rest-api/sdk/checks-v2/list-check-runs-for-a-deployment#errors)[](https://vercel.com/docs/rest-api/sdk/checks-v2/list-check-runs-for-a-deployment#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
500Error
