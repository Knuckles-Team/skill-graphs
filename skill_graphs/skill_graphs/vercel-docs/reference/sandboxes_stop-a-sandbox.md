Menu
APIs & SDKs
[Vercel REST API](https://vercel.com/docs/rest-api)
List sandboxes
# List sandboxes
GET`https://api.vercel.com/v1/sandboxes`
Retrieves a paginated list of sandboxes belonging to a specific project. Results can be filtered by creation time using the `since` and `until` parameters.
TypeScriptNext.jscURL
https://api.vercel.com/v1/sandboxes
```


1

const response = await fetch('https://api.vercel.com/v1/sandboxes?project=string&limit=123&since=123&until=123&teamId=string&slug=string', {






2

  method: 'GET',






3

  headers: {






4

    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',






5

    'Content-Type': 'application/json',






6

  },






7

});






8







9

const data = await response.json();






10

console.log(data);




```

Response
```


1
"value"



```

##  [Authentication](https://vercel.com/docs/rest-api/sandboxes/list-sandboxes#authentication)[](https://vercel.com/docs/rest-api/sandboxes/list-sandboxes#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Query parameters](https://vercel.com/docs/rest-api/sandboxes/list-sandboxes#query-parameters)[](https://vercel.com/docs/rest-api/sandboxes/list-sandboxes#query-parameters)
projectstringOptional
The unique identifier or name of the project to list sandboxes for.
limitnumberOptional
Maximum number of sandboxes to return in the response. Used for pagination.
sincenumberOptional
Filter sandboxes created after this timestamp. Specified as Unix time in milliseconds.
untilnumberOptional
Filter sandboxes created before this timestamp. Specified as Unix time in milliseconds.
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sandboxes/list-sandboxes#response)[](https://vercel.com/docs/rest-api/sandboxes/list-sandboxes#response)
200The list of sandboxes matching the request filters.
##  [Errors](https://vercel.com/docs/rest-api/sandboxes/list-sandboxes#errors)[](https://vercel.com/docs/rest-api/sandboxes/list-sandboxes#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404The project does not exist or the team does not have access to it.
APIs & SDKs
[Vercel REST API](https://vercel.com/docs/rest-api)
Stop a sandbox
# Stop a sandbox
POST`https://api.vercel.com/v1/sandboxes/{sandboxId}/stop`
Stops a running sandbox and releases its allocated resources. All running processes within the sandbox will be terminated. This action cannot be undone. A stopped sandbox cannot be restarted.
TypeScriptNext.jscURL
https://api.vercel.com/v1/sandboxes/{sandboxId}/stop
```


1

const response = await fetch('https://api.vercel.com/v1/sandboxes/sandboxId/stop?teamId=string&slug=string', {






2

  method: 'POST',






3

  headers: {






4

    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',






5

    'Content-Type': 'application/json',






6

  },






7

});






8







9

const data = await response.json();






10

console.log(data);




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

  }






34

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sandboxes/list-sandboxes#authentication)[](https://vercel.com/docs/rest-api/sandboxes/list-sandboxes#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sandboxes/list-sandboxes#path-parameters)[](https://vercel.com/docs/rest-api/sandboxes/list-sandboxes#path-parameters)
sandboxIdstringRequired
The unique identifier of the sandbox to stop.
##  [Query parameters](https://vercel.com/docs/rest-api/sandboxes/list-sandboxes#query-parameters)[](https://vercel.com/docs/rest-api/sandboxes/list-sandboxes#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sandboxes/list-sandboxes#response)[](https://vercel.com/docs/rest-api/sandboxes/list-sandboxes#response)
200The sandbox was stopped successfully.
sandboxobjectRequired
This object contains information related to a Vercel Sandbox.
+Show 19 properties
##  [Errors](https://vercel.com/docs/rest-api/sandboxes/list-sandboxes#errors)[](https://vercel.com/docs/rest-api/sandboxes/list-sandboxes#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
410The Sandbox has stopped execution and is no longer available.
422The Sandbox is creating a snapshot and will be stopped shortly. The Sandbox is stopping and is no longer available.
