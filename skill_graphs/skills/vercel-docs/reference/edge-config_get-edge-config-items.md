Menu
APIs & SDKs
[Vercel REST API](https://vercel.com/docs/rest-api)
Get Edge Config items
# Get Edge Config items
GET`https://api.vercel.com/v1/edge-config/{edgeConfigId}/items`
Returns all items of an Edge Config.
TypeScriptNext.jscURL
https://api.vercel.com/v1/edge-config/{edgeConfigId}/items
```


1

const response = await fetch('https://api.vercel.com/v1/edge-config/edgeConfigId/items?teamId=string&slug=string', {






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

[






2

  {






3

    "key": "string",






4

    "value": "string",






5

    "description": "string",






6

    "edgeConfigId": "example_id",






7

    "createdAt": "123",






8

    "updatedAt": "123"






9

  }






10

]




```

##  [Authentication](https://vercel.com/docs/rest-api/edge-config/get-edge-config-items#authentication)[](https://vercel.com/docs/rest-api/edge-config/get-edge-config-items#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/edge-config/get-edge-config-items#path-parameters)[](https://vercel.com/docs/rest-api/edge-config/get-edge-config-items#path-parameters)
edgeConfigIdstringRequired
##  [Query parameters](https://vercel.com/docs/rest-api/edge-config/get-edge-config-items#query-parameters)[](https://vercel.com/docs/rest-api/edge-config/get-edge-config-items#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/edge-config/get-edge-config-items#response)[](https://vercel.com/docs/rest-api/edge-config/get-edge-config-items#response)
200List of all Edge Config items.
##  [Errors](https://vercel.com/docs/rest-api/edge-config/get-edge-config-items#errors)[](https://vercel.com/docs/rest-api/edge-config/get-edge-config-items#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
