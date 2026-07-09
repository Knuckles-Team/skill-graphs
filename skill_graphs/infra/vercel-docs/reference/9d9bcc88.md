# Get a sandbox
GET`https://api.vercel.com/v1/sandboxes/{sandboxId}`
Retrieves detailed information about a specific sandbox, including its current status, resource configuration, and exposed routes.
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

  const result = await vercel.sandboxes.getSandbox({






9

    sandboxId: "sbx_abc123",






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

  "sandbox": {






3

    "id": "sbx_123a6c5209bc3778245d011443644c8d27dc2c50",






4

    "memory": "2048",






5

    "vcpus": "2",






6

    "region": "iad1",






7

    "runtime": "node22",






8

    "timeout": "3600000",






9

    "status": "running",






10

    "requestedAt": "1750344501629",






11

    "startedAt": "1750344501629",






12

    "cwd": "/vercel/sandbox",






13

    "requestedStopAt": "1750344501629",






14

    "stoppedAt": "1750344501629",






15

    "abortedAt": "1750344501629",






16

    "duration": "3600000",






17

    "sourceSnapshotId": "snap_123a6c5209bc3778245d011443644c8d27dc2c50",






18

    "snapshottedAt": "1750344501629",






19

    "createdAt": "1750344501629",






20

    "updatedAt": "1750344501629",






21

    "networkPolicy": {






22

      "mode": "custom",






23

      "allowedDomains": [],






24

      "allowedCIDRs": [],






25

      "deniedCIDRs": [],






26

      "injectionRules": [






27

        {






28

          "domain": "api.vercel.com",






29

          "headerNames": []






30

        }






31

      ]






32

    }






33

  },






34

  "routes": [






35

    {






36

      "url": "https://example.com",






37

      "port": "123",






38

      "subdomain": "string",






39

      "system": "true"






40

    }






41

  ]






42

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-sandbox#authentication)[](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-sandbox#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-sandbox#path-parameters)[](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-sandbox#path-parameters)
sandboxIdstringRequired
The unique identifier of the sandbox to retrieve.
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-sandbox#query-parameters)[](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-sandbox#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-sandbox#response)[](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-sandbox#response)
200Success
sandboxobjectRequired
This object contains information related to a Vercel Sandbox.
+Show 19 properties
routesarrayRequired
+Show 4 properties
##  [Errors](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-sandbox#errors)[](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-sandbox#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
410The Sandbox has stopped execution and is no longer available.
422The Sandbox is creating a snapshot and will be stopped shortly. The Sandbox is stopping and is no longer available.
429Error
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

  const result = await vercel.sandboxes.getSandbox({






9

    sandboxId: "sbx_abc123",






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

  "sandbox": {






3

    "id": "sbx_123a6c5209bc3778245d011443644c8d27dc2c50",






4

    "memory": "2048",






5

    "vcpus": "2",






6

    "region": "iad1",






7

    "runtime": "node22",






8

    "timeout": "3600000",






9

    "status": "running",






10

    "requestedAt": "1750344501629",






11

    "startedAt": "1750344501629",






12

    "cwd": "/vercel/sandbox",






13

    "requestedStopAt": "1750344501629",






14

    "stoppedAt": "1750344501629",






15

    "abortedAt": "1750344501629",






16

    "duration": "3600000",






17

    "sourceSnapshotId": "snap_123a6c5209bc3778245d011443644c8d27dc2c50",






18

    "snapshottedAt": "1750344501629",






19

    "createdAt": "1750344501629",






20

    "updatedAt": "1750344501629",






21

    "networkPolicy": {






22

      "mode": "custom",






23

      "allowedDomains": [],






24

      "allowedCIDRs": [],






25

      "deniedCIDRs": [],






26

      "injectionRules": [






27

        {






28

          "domain": "api.vercel.com",






29

          "headerNames": []






30

        }






31

      ]






32

    }






33

  },






34

  "routes": [






35

    {






36

      "url": "https://example.com",






37

      "port": "123",






38

      "subdomain": "string",






39

      "system": "true"






40

    }






41

  ]






42

}




```

Copy as MarkdownGive feedbackAsk AI about this page
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Update network policy
