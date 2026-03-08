# Get a command
GET`https://api.vercel.com/v1/sandboxes/{sandboxId}/cmd/{cmdId}`
Retrieves the current status and details of a command executed in a sandbox. Use the `wait` parameter to block until the command finishes execution.
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

  const result = await vercel.sandboxes.getCommand({






9

    sandboxId: "sbx_abc123",






10

    cmdId: "cmd_abc123",






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

  "command": {






3

    "id": "cmd_123a6c5209bc3778245d011443644c8d27dc2c50",






4

    "name": "npm",






5

    "args": [],






6

    "cwd": "/vercel/sandbox",






7

    "sandboxId": "sbx_123a6c5209bc3778245d011443644c8d27dc2c50",






8

    "exitCode": "0",






9

    "startedAt": "1673123456789"






10

  }






11

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-command#authentication)[](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-command#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-command#path-parameters)[](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-command#path-parameters)
sandboxIdstringRequired
The unique identifier of the sandbox containing the command.
cmdIdstringRequired
The unique identifier of the command to retrieve.
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-command#query-parameters)[](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-command#query-parameters)
waitstringOptional
If set to "true", the request will block until the command finishes execution. Useful for synchronously waiting for command completion.
+Show 2 enum values
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-command#response)[](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-command#response)
200The command data along with the exit code if the command did finish.
commandobjectRequired
This object represents command run in a Vercel Sandbox.
+Show 7 properties
##  [Errors](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-command#errors)[](https://vercel.com/docs/rest-api/sdk/sandboxes/get-a-command#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
410The Sandbox has stopped execution and is no longer available.
422The Sandbox is creating a snapshot and will be stopped shortly. The Sandbox is stopping and is no longer available.
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

  const result = await vercel.sandboxes.getCommand({






9

    sandboxId: "sbx_abc123",






10

    cmdId: "cmd_abc123",






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

  "command": {






3

    "id": "cmd_123a6c5209bc3778245d011443644c8d27dc2c50",






4

    "name": "npm",






5

    "args": [],






6

    "cwd": "/vercel/sandbox",






7

    "sandboxId": "sbx_123a6c5209bc3778245d011443644c8d27dc2c50",






8

    "exitCode": "0",






9

    "startedAt": "1673123456789"






10

  }






11

}




```

Copy as MarkdownGive feedbackAsk AI about this page
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Create a snapshot
