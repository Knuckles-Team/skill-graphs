##  [Errors](https://vercel.com/docs#errors)[](https://vercel.com/docs#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404The deployment was not found
TypeScriptNext.jscURL
https://api.vercel.com/v2/deployments/{id}/aliases
```


1

const response = await fetch('https://api.vercel.com/v2/deployments/id/aliases?teamId=string&slug=string', {






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

  "aliases": [






3

    {






4

      "uid": "2WjyKQmM8ZnGcJsPWMrHRHrE",






5

      "alias": "my-alias.vercel.app",






6

      "created": "2017-04-26T23:00:34.232Z",






7

      "redirect": "string",






8

      "protectionBypass": "value"






9

    }






10

  ]






11

}




```

Copy as MarkdownGive feedbackAsk AI about this page
