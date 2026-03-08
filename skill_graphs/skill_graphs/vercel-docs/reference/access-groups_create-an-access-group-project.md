Menu
APIs & SDKs
[Vercel REST API](https://vercel.com/docs/rest-api)
Create an access group project
# Create an access group project
POST`https://api.vercel.com/v1/access-groups/{accessGroupIdOrName}/projects`
Allows creation of an access group project
TypeScriptNext.jscURL
https://api.vercel.com/v1/access-groups/{accessGroupIdOrName}/projects
```


1

const response = await fetch('https://api.vercel.com/v1/access-groups/accessGroupIdOrName/projects?teamId=string&slug=string', {






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

    "projectId": "prj_ndlgr43fadlPyCtREAqxxdyFK",






9

    "role": "ADMIN"






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

{






2

  "teamId": "example_id",






3

  "accessGroupId": "example_id",






4

  "projectId": "example_id",






5

  "role": "ADMIN",






6

  "createdAt": "string",






7

  "updatedAt": "string"






8

}




```

##  [Authentication](https://vercel.com/docs/rest-api/access-groups/create-an-access-group-project#authentication)[](https://vercel.com/docs/rest-api/access-groups/create-an-access-group-project#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/access-groups/create-an-access-group-project#path-parameters)[](https://vercel.com/docs/rest-api/access-groups/create-an-access-group-project#path-parameters)
accessGroupIdOrNamestringRequired
##  [Query parameters](https://vercel.com/docs/rest-api/access-groups/create-an-access-group-project#query-parameters)[](https://vercel.com/docs/rest-api/access-groups/create-an-access-group-project#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Body](https://vercel.com/docs/rest-api/access-groups/create-an-access-group-project#body)[](https://vercel.com/docs/rest-api/access-groups/create-an-access-group-project#body)
application/json
projectIdstringRequired
The ID of the project.
rolestringRequired
The project role that will be added to this Access Group.
+Show 3 enum values
##  [Response](https://vercel.com/docs/rest-api/access-groups/create-an-access-group-project#response)[](https://vercel.com/docs/rest-api/access-groups/create-an-access-group-project#response)
200Success
teamIdstringRequired
accessGroupIdstringRequired
projectIdstringRequired
rolestringRequired
+Show 4 enum values
createdAtstringRequired
updatedAtstringRequired
##  [Errors](https://vercel.com/docs/rest-api/access-groups/create-an-access-group-project#errors)[](https://vercel.com/docs/rest-api/access-groups/create-an-access-group-project#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
