Menu
APIs & SDKs
[Vercel REST API](https://vercel.com/docs/rest-api)
Extend sandbox timeout
# Extend sandbox timeout
POST`https://api.vercel.com/v1/sandboxes/{sandboxId}/extend-timeout`
Extends the maximum execution time of a running sandbox. The sandbox must be active and able to accept commands. The total timeout cannot exceed the maximum allowed limit for your account.
TypeScriptNext.jscURL
https://api.vercel.com/v1/sandboxes/{sandboxId}/extend-timeout
```


1

const response = await fetch('https://api.vercel.com/v1/sandboxes/sandboxId/extend-timeout?teamId=string&slug=string', {






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

  body: JSON.stringify({






8

    "duration": "300000"






9

  }),






10

});






11







12

const data = await response.json();






13

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

##  [Authentication](https://vercel.com/docs/rest-api/sandboxes/extend-sandbox-timeout#authentication)[](https://vercel.com/docs/rest-api/sandboxes/extend-sandbox-timeout#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sandboxes/extend-sandbox-timeout#path-parameters)[](https://vercel.com/docs/rest-api/sandboxes/extend-sandbox-timeout#path-parameters)
sandboxIdstringRequired
The unique identifier of the sandbox to extend the timeout for.
##  [Query parameters](https://vercel.com/docs/rest-api/sandboxes/extend-sandbox-timeout#query-parameters)[](https://vercel.com/docs/rest-api/sandboxes/extend-sandbox-timeout#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Body](https://vercel.com/docs/rest-api/sandboxes/extend-sandbox-timeout#body)[](https://vercel.com/docs/rest-api/sandboxes/extend-sandbox-timeout#body)
application/json
durationnumberRequired
The amount of time in milliseconds to add to the current timeout. Must be at least 1000ms (1 second).
##  [Response](https://vercel.com/docs/rest-api/sandboxes/extend-sandbox-timeout#response)[](https://vercel.com/docs/rest-api/sandboxes/extend-sandbox-timeout#response)
200The sandbox timeout was extended successfully.
sandboxobjectRequired
This object contains information related to a Vercel Sandbox.
+Show 19 properties
##  [Errors](https://vercel.com/docs/rest-api/sandboxes/extend-sandbox-timeout#errors)[](https://vercel.com/docs/rest-api/sandboxes/extend-sandbox-timeout#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
410The Sandbox has stopped execution and is no longer available.
422The Sandbox is creating a snapshot and will be stopped shortly. The Sandbox is stopping and is no longer available.
