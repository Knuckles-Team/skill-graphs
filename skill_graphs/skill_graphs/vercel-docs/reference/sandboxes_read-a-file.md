Menu
APIs & SDKs
[Vercel REST API](https://vercel.com/docs/rest-api)
Read a file
# Read a file
POST`https://api.vercel.com/v1/sandboxes/{sandboxId}/fs/read`
Downloads the contents of a file from a sandbox's filesystem. The file content is returned as a binary stream with appropriate Content-Disposition headers for file download.
TypeScriptNext.jscURL
https://api.vercel.com/v1/sandboxes/{sandboxId}/fs/read
```


1

const response = await fetch('https://api.vercel.com/v1/sandboxes/sandboxId/fs/read?teamId=string&slug=string', {






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

    "cwd": "/home/vercel-sandbox",






9

    "path": "dist/agent-output.md"






10

  }),






11

});






12







13

const data = await response.json();






14

console.log(data);




```

Response
```


1

{}




```

##  [Authentication](https://vercel.com/docs/rest-api/sandboxes/read-a-file#authentication)[](https://vercel.com/docs/rest-api/sandboxes/read-a-file#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sandboxes/read-a-file#path-parameters)[](https://vercel.com/docs/rest-api/sandboxes/read-a-file#path-parameters)
sandboxIdstringRequired
The unique identifier of the sandbox to read the file from.
##  [Query parameters](https://vercel.com/docs/rest-api/sandboxes/read-a-file#query-parameters)[](https://vercel.com/docs/rest-api/sandboxes/read-a-file#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Body](https://vercel.com/docs/rest-api/sandboxes/read-a-file#body)[](https://vercel.com/docs/rest-api/sandboxes/read-a-file#body)
application/json
cwdstringOptional
The base directory for resolving relative paths. If not specified, paths are resolved from the sandbox home directory.
pathstringRequired
The path of the file to read. Can be absolute or relative to the working directory.
##  [Response](https://vercel.com/docs/rest-api/sandboxes/read-a-file#response)[](https://vercel.com/docs/rest-api/sandboxes/read-a-file#response)
200Success
##  [Errors](https://vercel.com/docs/rest-api/sandboxes/read-a-file#errors)[](https://vercel.com/docs/rest-api/sandboxes/read-a-file#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
410The Sandbox has stopped execution and is no longer available.
422The Sandbox is creating a snapshot and will be stopped shortly. The Sandbox is stopping and is no longer available.
