Menu
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Retrieve a custom environment
# Retrieve a custom environment
GET`https://api.vercel.com/v9/projects/{idOrName}/custom-environments/{environmentSlugOrId}`
Retrieve a custom environment for the project. Must not be named 'Production' or 'Preview'.
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

  const result = await vercel.environment.getCustomEnvironment({






9

    idOrName: "<value>",






10

    environmentSlugOrId: "<id>",






11

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






12

    slug: "my-team-url-slug",






13

  });






14







15

  console.log(result);






16

}






17







18

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

##  [Authentication](https://vercel.com/docs/rest-api/sdk/environment/retrieve-a-custom-environment#authentication)[](https://vercel.com/docs/rest-api/sdk/environment/retrieve-a-custom-environment#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/environment/retrieve-a-custom-environment#path-parameters)[](https://vercel.com/docs/rest-api/sdk/environment/retrieve-a-custom-environment#path-parameters)
idOrNamestringRequired
The unique project identifier or the project name
environmentSlugOrIdstringRequired
The unique custom environment identifier within the project
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/environment/retrieve-a-custom-environment#query-parameters)[](https://vercel.com/docs/rest-api/sdk/environment/retrieve-a-custom-environment#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sdk/environment/retrieve-a-custom-environment#response)[](https://vercel.com/docs/rest-api/sdk/environment/retrieve-a-custom-environment#response)
200Success
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
##  [Errors](https://vercel.com/docs/rest-api/sdk/environment/retrieve-a-custom-environment#errors)[](https://vercel.com/docs/rest-api/sdk/environment/retrieve-a-custom-environment#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
