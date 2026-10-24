Menu
APIs & SDKs
[Vercel REST API](https://vercel.com/docs/rest-api)
List members of an access group
# List members of an access group
GET`https://api.vercel.com/v1/access-groups/{idOrName}/members`
List members of an access group
TypeScriptNext.jscURL
https://api.vercel.com/v1/access-groups/{idOrName}/members
```


1

const response = await fetch('https://api.vercel.com/v1/access-groups/idOrName/members?limit=123&next=string&search=string&teamId=string&slug=string', {






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

{






2

  "members": [






3

    {






4

      "avatar": "string",






5

      "email": "user@example.com",






6

      "uid": "example_id",






7

      "username": "string",






8

      "name": "Example Name",






9

      "createdAt": "string",






10

      "teamRole": "OWNER"






11

    }






12

  ],






13

  "pagination": {






14

    "count": "123",






15

    "next": "string"






16

  }






17

}




```

##  [Authentication](https://vercel.com/docs/rest-api/access-groups/list-members-of-an-access-group#authentication)[](https://vercel.com/docs/rest-api/access-groups/list-members-of-an-access-group#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/access-groups/list-members-of-an-access-group#path-parameters)[](https://vercel.com/docs/rest-api/access-groups/list-members-of-an-access-group#path-parameters)
idOrNamestringRequired
The ID or name of the Access Group.
##  [Query parameters](https://vercel.com/docs/rest-api/access-groups/list-members-of-an-access-group#query-parameters)[](https://vercel.com/docs/rest-api/access-groups/list-members-of-an-access-group#query-parameters)
limitintegerOptional
Limit how many access group members should be returned.
nextstringOptional
Continuation cursor to retrieve the next page of results.
searchstringOptional
Search project members by their name, username, and email.
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/access-groups/list-members-of-an-access-group#response)[](https://vercel.com/docs/rest-api/access-groups/list-members-of-an-access-group#response)
200Success
membersarrayRequired
+Show 7 properties
paginationobjectRequired
+Show 2 properties
##  [Errors](https://vercel.com/docs/rest-api/access-groups/list-members-of-an-access-group#errors)[](https://vercel.com/docs/rest-api/access-groups/list-members-of-an-access-group#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
