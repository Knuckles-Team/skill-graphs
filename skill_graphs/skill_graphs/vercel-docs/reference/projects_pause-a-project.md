Menu
APIs & SDKs
[Vercel REST API](https://vercel.com/docs/rest-api)
Pause a project
# Pause a project
POST`https://api.vercel.com/v1/projects/{projectId}/pause`
Pause a project by passing its project `id` in the URL. If the project does not exist given the id then the request will fail with 400 status code. If the project disables auto assigning custom production domains and blocks the active Production Deployment then the request will return with 200 status code.
TypeScriptNext.jscURL
https://api.vercel.com/v1/projects/{projectId}/pause
```


1

const response = await fetch('https://api.vercel.com/v1/projects/projectId/pause?teamId=string&slug=string', {






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

{}




```

##  [Authentication](https://vercel.com/docs/rest-api/projects/pause-a-project#authentication)[](https://vercel.com/docs/rest-api/projects/pause-a-project#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/projects/pause-a-project#path-parameters)[](https://vercel.com/docs/rest-api/projects/pause-a-project#path-parameters)
projectIdstringRequired
The unique project identifier
##  [Query parameters](https://vercel.com/docs/rest-api/projects/pause-a-project#query-parameters)[](https://vercel.com/docs/rest-api/projects/pause-a-project#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/projects/pause-a-project#response)[](https://vercel.com/docs/rest-api/projects/pause-a-project#response)
200Success
##  [Errors](https://vercel.com/docs/rest-api/projects/pause-a-project#errors)[](https://vercel.com/docs/rest-api/projects/pause-a-project#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
500Error
