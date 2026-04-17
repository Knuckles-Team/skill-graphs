Menu
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Configures Static IPs for a project
# Configures Static IPs for a project
PATCH`https://api.vercel.com/v1/projects/{idOrName}/shared-connect-links`
Allows configuring Static IPs for a project
updateStaticIpsupdateStaticIps
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

  const result = await vercel.connect.updateStaticIps({






9

    idOrName: "<value>",






10

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






11

    slug: "my-team-url-slug",






12

    requestBody: {






13

      regions: [






14

        "iad1",






15

      ],






16

    },






17

  });






18







19

  console.log(result);






20

}






21







22

run();




```

Response
```


1

[






2

  {






3

    "envId": "example_id",






4

    "connectConfigurationId": "example_id",






5

    "dc": "string",






6

    "passive": "false",






7

    "buildsEnabled": "false",






8

    "aws": {






9

      "subnetIds": [],






10

      "securityGroupId": "https://example.com"






11

    },






12

    "createdAt": "123",






13

    "updatedAt": "123"






14

  }






15

]




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/connect/configures-static-ips-for-a-project#authentication)[](https://vercel.com/docs/rest-api/sdk/connect/configures-static-ips-for-a-project#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/connect/configures-static-ips-for-a-project#path-parameters)[](https://vercel.com/docs/rest-api/sdk/connect/configures-static-ips-for-a-project#path-parameters)
idOrNamestringRequired
The unique project identifier or the project name
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/connect/configures-static-ips-for-a-project#query-parameters)[](https://vercel.com/docs/rest-api/sdk/connect/configures-static-ips-for-a-project#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Body](https://vercel.com/docs/rest-api/sdk/connect/configures-static-ips-for-a-project#body)[](https://vercel.com/docs/rest-api/sdk/connect/configures-static-ips-for-a-project#body)
application/json
Option 1Option 2
buildsbooleanRequired
Whether to use Static IPs for builds.
regionsarrayOptional
##  [Response](https://vercel.com/docs/rest-api/sdk/connect/configures-static-ips-for-a-project#response)[](https://vercel.com/docs/rest-api/sdk/connect/configures-static-ips-for-a-project#response)
200Success
##  [Errors](https://vercel.com/docs/rest-api/sdk/connect/configures-static-ips-for-a-project#errors)[](https://vercel.com/docs/rest-api/sdk/connect/configures-static-ips-for-a-project#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid.
401The request is not authorized.
402Error
403You do not have permission to access this resource.
404Error
409Error
500Error
