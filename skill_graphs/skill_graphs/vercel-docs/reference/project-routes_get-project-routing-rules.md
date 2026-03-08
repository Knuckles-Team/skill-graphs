Menu
APIs & SDKs
[Vercel REST API](https://vercel.com/docs/rest-api)
Get project routing rules
# Get project routing rules
GET`https://api.vercel.com/v1/projects/{projectId}/routes`
Get the routing rules for a project. Supports searching by name/ID/pattern, filtering by route type, and diffing staged changes against production.
TypeScriptNext.jscURL
https://api.vercel.com/v1/projects/{projectId}/routes
```


1

const response = await fetch('https://api.vercel.com/v1/projects/projectId/routes?versionId=string&q=string&filter=string&diff=value&teamId=string&slug=string', {






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

##  [Authentication](https://vercel.com/docs/rest-api/project-routes/get-project-routing-rules#authentication)[](https://vercel.com/docs/rest-api/project-routes/get-project-routing-rules#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/project-routes/get-project-routing-rules#path-parameters)[](https://vercel.com/docs/rest-api/project-routes/get-project-routing-rules#path-parameters)
projectIdstringRequired
##  [Query parameters](https://vercel.com/docs/rest-api/project-routes/get-project-routing-rules#query-parameters)[](https://vercel.com/docs/rest-api/project-routes/get-project-routing-rules#query-parameters)
versionIdstringOptional
qstringOptional
filterstringOptional
+Show 4 enum values
diffanyOptional
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/project-routes/get-project-routing-rules#response)[](https://vercel.com/docs/rest-api/project-routes/get-project-routing-rules#response)
200Success
##  [Errors](https://vercel.com/docs/rest-api/project-routes/get-project-routing-rules#errors)[](https://vercel.com/docs/rest-api/project-routes/get-project-routing-rules#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
