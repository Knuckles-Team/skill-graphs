Menu
APIs & SDKs
[Vercel REST API](https://vercel.com/docs/rest-api)
Delete an access group project
# Delete an access group project
DEL`https://api.vercel.com/v1/access-groups/{accessGroupIdOrName}/projects/{projectId}`
Allows deletion of an access group project
TypeScriptNext.jscURL
https://api.vercel.com/v1/access-groups/{accessGroupIdOrName}/projects/{projectId}
```


1

const response = await fetch('https://api.vercel.com/v1/access-groups/accessGroupIdOrName/projects/projectId?teamId=string&slug=string', {






2

  method: 'DELETE',






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

##  [Authentication](https://vercel.com/docs/rest-api/access-groups/delete-an-access-group-project#authentication)[](https://vercel.com/docs/rest-api/access-groups/delete-an-access-group-project#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/access-groups/delete-an-access-group-project#path-parameters)[](https://vercel.com/docs/rest-api/access-groups/delete-an-access-group-project#path-parameters)
accessGroupIdOrNamestringRequired
projectIdstringRequired
##  [Query parameters](https://vercel.com/docs/rest-api/access-groups/delete-an-access-group-project#query-parameters)[](https://vercel.com/docs/rest-api/access-groups/delete-an-access-group-project#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/access-groups/delete-an-access-group-project#response)[](https://vercel.com/docs/rest-api/access-groups/delete-an-access-group-project#response)
200Success
##  [Errors](https://vercel.com/docs/rest-api/access-groups/delete-an-access-group-project#errors)[](https://vercel.com/docs/rest-api/access-groups/delete-an-access-group-project#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
