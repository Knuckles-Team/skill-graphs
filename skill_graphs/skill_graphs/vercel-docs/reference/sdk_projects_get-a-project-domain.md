Menu
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Get a project domain
# Get a project domain
GET`https://api.vercel.com/v9/projects/{idOrName}/domains/{domain}`
Get project domain by project id/name and domain name.
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

  const result = await vercel.projects.getProjectDomain({






9

    idOrName: "<value>",






10

    domain: "www.example.com",






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

  "name": "Example Name",






3

  "apexName": "Example Name",






4

  "projectId": "example_id",






5

  "redirect": "string",






6

  "redirectStatusCode": "301",






7

  "gitBranch": "string",






8

  "customEnvironmentId": "example_id",






9

  "updatedAt": "123",






10

  "createdAt": "123",






11

  "verified": "false",






12

  "verification": [






13

    {






14

      "type": "string",






15

      "domain": "string",






16

      "value": "string",






17

      "reason": "Customer requested refund"






18

    }






19

  ]






20

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/projects/get-a-project-domain#authentication)[](https://vercel.com/docs/rest-api/sdk/projects/get-a-project-domain#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/projects/get-a-project-domain#path-parameters)[](https://vercel.com/docs/rest-api/sdk/projects/get-a-project-domain#path-parameters)
idOrNamestringRequired
The unique project identifier or the project name
domainstringRequired
The project domain name
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/projects/get-a-project-domain#query-parameters)[](https://vercel.com/docs/rest-api/sdk/projects/get-a-project-domain#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sdk/projects/get-a-project-domain#response)[](https://vercel.com/docs/rest-api/sdk/projects/get-a-project-domain#response)
200Success
namestringRequired
apexNamestringRequired
projectIdstringRequired
redirectstringOptional
redirectStatusCodenumberOptional
+Show 4 enum values
gitBranchstringOptional
customEnvironmentIdstringOptional
updatedAtnumberOptional
createdAtnumberOptional
verifiedbooleanRequired
`true` if the domain is verified for use with the project. If `false` it will not be used as an alias on this project until the challenge in `verification` is completed.
+Show 2 enum values
verificationarrayOptional
A list of verification challenges, one of which must be completed to verify the domain for use on the project. After the challenge is complete `POST /projects/:idOrName/domains/:domain/verify` to verify the domain. Possible challenges: - If `verification.type = TXT` the `verification.domain` will be checked for a TXT record matching `verification.value`.
+Show 4 properties
##  [Errors](https://vercel.com/docs/rest-api/sdk/projects/get-a-project-domain#errors)[](https://vercel.com/docs/rest-api/sdk/projects/get-a-project-domain#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
