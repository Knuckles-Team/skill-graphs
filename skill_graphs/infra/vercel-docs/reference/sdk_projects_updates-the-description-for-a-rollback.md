Menu
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Updates the description for a rollback
# Updates the description for a rollback
PATCH`https://api.vercel.com/v1/projects/{projectId}/rollback/{deploymentId}/update-description`
Updates the reason for a rollback, without changing the rollback status itself.
Request
```


1

import { Vercel } from "@vercel/sdk";






2







3

const vercel = new Vercel();






4







5

async function run() {






6

  await vercel.projects.patchV1ProjectsProjectIdRollbackDeploymentIdUpdateDescription({






7

    projectId: "<id>",






8

    deploymentId: "<id>",






9

  });






10







11







12

}






13







14

run();




```

Response
```


1

{}




```

##  [Path parameters](https://vercel.com/docs/rest-api/sdk/projects/updates-the-description-for-a-rollback#path-parameters)[](https://vercel.com/docs/rest-api/sdk/projects/updates-the-description-for-a-rollback#path-parameters)
projectIdstringRequired
deploymentIdstringRequired
##  [Body](https://vercel.com/docs/rest-api/sdk/projects/updates-the-description-for-a-rollback#body)[](https://vercel.com/docs/rest-api/sdk/projects/updates-the-description-for-a-rollback#body)
application/json
descriptionstringOptional
The reason for the rollback
##  [Response](https://vercel.com/docs/rest-api/sdk/projects/updates-the-description-for-a-rollback#response)[](https://vercel.com/docs/rest-api/sdk/projects/updates-the-description-for-a-rollback#response)
200Success
##  [Errors](https://vercel.com/docs/rest-api/sdk/projects/updates-the-description-for-a-rollback#errors)[](https://vercel.com/docs/rest-api/sdk/projects/updates-the-description-for-a-rollback#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
409Error
422Error
