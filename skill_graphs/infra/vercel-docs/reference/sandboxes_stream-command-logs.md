Menu
APIs & SDKs
[Vercel REST API](https://vercel.com/docs/rest-api)
Stream command logs
# Stream command logs
GET`https://api.vercel.com/v1/sandboxes/{sandboxId}/cmd/{cmdId}/logs`
Streams the output of a command in real-time using newline-delimited JSON (ND-JSON). Each entry includes the output data and stream type. Stream types include `stdout`, `stderr`, and `error` (for stream failures).
TypeScriptNext.jscURL
https://api.vercel.com/v1/sandboxes/{sandboxId}/cmd/{cmdId}/logs
```


1

const response = await fetch('https://api.vercel.com/v1/sandboxes/sandboxId/cmd/cmdId/logs?teamId=string&slug=string', {






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

{}




```

##  [Authentication](https://vercel.com/docs/rest-api/sandboxes/stream-command-logs#authentication)[](https://vercel.com/docs/rest-api/sandboxes/stream-command-logs#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sandboxes/stream-command-logs#path-parameters)[](https://vercel.com/docs/rest-api/sandboxes/stream-command-logs#path-parameters)
sandboxIdstringRequired
The unique identifier of the sandbox containing the command.
cmdIdstringRequired
The unique identifier of the command to stream logs for.
##  [Query parameters](https://vercel.com/docs/rest-api/sandboxes/stream-command-logs#query-parameters)[](https://vercel.com/docs/rest-api/sandboxes/stream-command-logs#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sandboxes/stream-command-logs#response)[](https://vercel.com/docs/rest-api/sandboxes/stream-command-logs#response)
200Success
##  [Errors](https://vercel.com/docs/rest-api/sandboxes/stream-command-logs#errors)[](https://vercel.com/docs/rest-api/sandboxes/stream-command-logs#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
410The Sandbox has stopped execution and is no longer available.
422The Sandbox is creating a snapshot and will be stopped shortly. The Sandbox is stopping and is no longer available.
