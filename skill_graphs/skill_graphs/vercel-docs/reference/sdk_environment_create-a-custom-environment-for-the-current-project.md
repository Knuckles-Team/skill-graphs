Menu
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Create a custom environment for the current project.
# Create a custom environment for the current project.
POST`https://api.vercel.com/v9/projects/{idOrName}/custom-environments`
Creates a custom environment for the current project. Cannot be named 'Production' or 'Preview'.
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

  const result = await vercel.environment.createCustomEnvironment({






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

  "id": "icfg_1234567890",






3

  "slug": "string",






4

  "type": "production",






5

  "description": "string",






6

  "branchMatcher": {






7

    "type": "endsWith",






8

    "pattern": "string"






9

  },






10

  "domains": [






11

    {






12

      "name": "Example Name",






13

      "apexName": "Example Name",






14

      "projectId": "example_id",






15

      "redirect": "string",






16

      "redirectStatusCode": "301",






17

      "gitBranch": "string",






18

      "customEnvironmentId": "example_id",






19

      "updatedAt": "123",






20

      "createdAt": "123",






21

      "verified": "false",






22

      "verification": [






23

        {






24

          "type": "string",






25

          "domain": "string",






26

          "value": "string",






27

          "reason": "Customer requested refund"






28

        }






29

      ]






30

    }






31

  ],






32

  "currentDeploymentAliases": [],






33

  "createdAt": "123",






34

  "updatedAt": "123"






35

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/environment/create-a-custom-environment-for-the-current-project#authentication)[](https://vercel.com/docs/rest-api/sdk/environment/create-a-custom-environment-for-the-current-project#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/environment/create-a-custom-environment-for-the-current-project#path-parameters)[](https://vercel.com/docs/rest-api/sdk/environment/create-a-custom-environment-for-the-current-project#path-parameters)
idOrNamestringRequired
The unique project identifier or the project name
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/environment/create-a-custom-environment-for-the-current-project#query-parameters)[](https://vercel.com/docs/rest-api/sdk/environment/create-a-custom-environment-for-the-current-project#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Body](https://vercel.com/docs/rest-api/sdk/environment/create-a-custom-environment-for-the-current-project#body)[](https://vercel.com/docs/rest-api/sdk/environment/create-a-custom-environment-for-the-current-project#body)
application/json
slugstringOptional
The slug of the custom environment to create.
descriptionstringOptional
Description of the custom environment. This is optional.
branchMatcherobjectOptional
How we want to determine a matching branch. This is optional.
+Show 2 properties
copyEnvVarsFromstringOptional
Where to copy environment variables from. This is optional.
##  [Response](https://vercel.com/docs/rest-api/sdk/environment/create-a-custom-environment-for-the-current-project#response)[](https://vercel.com/docs/rest-api/sdk/environment/create-a-custom-environment-for-the-current-project#response)
201Success
idstringRequired
Unique identifier for the custom environment (format: env_*)
slugstringRequired
URL-friendly name of the environment
typestringRequired
The type of environment (production, preview, or development)
+Show 3 enum values
descriptionstringOptional
Optional description of the environment's purpose
branchMatcherobjectOptional
Configuration for matching git branches to this environment
+Show 2 properties
domainsarrayOptional
List of domains associated with this environment
+Show 11 properties
currentDeploymentAliasesarrayOptional
List of aliases for the current deployment
createdAtnumberRequired
Timestamp when the environment was created
updatedAtnumberRequired
Timestamp when the environment was last updated
##  [Errors](https://vercel.com/docs/rest-api/sdk/environment/create-a-custom-environment-for-the-current-project#errors)[](https://vercel.com/docs/rest-api/sdk/environment/create-a-custom-environment-for-the-current-project#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid.
401The request is not authorized.
402The account was soft-blocked for an unhandled reason. The account is missing a payment so payment method must be updated
403You do not have permission to access this resource.
500Error
