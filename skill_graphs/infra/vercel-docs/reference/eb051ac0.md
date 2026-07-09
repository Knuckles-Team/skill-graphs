##  [Errors](https://vercel.com/docs#errors)[](https://vercel.com/docs#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid. The cert for the provided alias is not ready The deployment is not READY and can not be aliased The supplied alias is invalid
401The request is not authorized.
402The account was soft-blocked for an unhandled reason. The account is missing a payment so payment method must be updated
403You do not have permission to access this resource. If no .vercel.app alias exists then we fail (nothing to mirror)
404The domain used for the alias was not found The deployment was not found
409The provided alias is already assigned to the given deployment The domain is not allowed to be used
TypeScriptNext.jscURL
https://api.vercel.com/v2/deployments/{id}/aliases
```


1

const response = await fetch('https://api.vercel.com/v2/deployments/id/aliases?teamId=string&slug=string', {






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

    "alias": "my-alias.vercel.app",






9

    "redirect": "null"






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

  "uid": "2WjyKQmM8ZnGcJsPWMrHRHrE",






3

  "alias": "my-alias.vercel.app",






4

  "created": "2017-04-26T23:00:34.232Z",






5

  "oldDeploymentId": "dpl_FjvFJncQHQcZMznrUm9EoB8sFuPa"






6

}




```

Copy as MarkdownGive feedbackAsk AI about this page
