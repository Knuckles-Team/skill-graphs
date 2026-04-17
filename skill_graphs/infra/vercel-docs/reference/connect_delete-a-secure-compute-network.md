Menu
APIs & SDKs
[Vercel REST API](https://vercel.com/docs/rest-api)
Delete a Secure Compute network
# Delete a Secure Compute network
DEL`https://api.vercel.com/v1/connect/networks/{networkId}`
Allows to delete a Secure Compute network.
TypeScriptNext.jscURL
https://api.vercel.com/v1/connect/networks/{networkId}
```


1

const response = await fetch('https://api.vercel.com/v1/connect/networks/networkId?teamId=string&slug=string', {






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

##  [Authentication](https://vercel.com/docs/rest-api/connect/delete-a-secure-compute-network#authentication)[](https://vercel.com/docs/rest-api/connect/delete-a-secure-compute-network#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/connect/delete-a-secure-compute-network#path-parameters)[](https://vercel.com/docs/rest-api/connect/delete-a-secure-compute-network#path-parameters)
networkIdstringRequired
The ID of the network to delete
##  [Query parameters](https://vercel.com/docs/rest-api/connect/delete-a-secure-compute-network#query-parameters)[](https://vercel.com/docs/rest-api/connect/delete-a-secure-compute-network#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/connect/delete-a-secure-compute-network#response)[](https://vercel.com/docs/rest-api/connect/delete-a-secure-compute-network#response)
204Success
##  [Errors](https://vercel.com/docs/rest-api/connect/delete-a-secure-compute-network#errors)[](https://vercel.com/docs/rest-api/connect/delete-a-secure-compute-network#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
402Error
403You do not have permission to access this resource.
409Error
