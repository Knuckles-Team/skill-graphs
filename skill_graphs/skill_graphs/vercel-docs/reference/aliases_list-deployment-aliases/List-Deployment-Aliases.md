# List Deployment Aliases
GET`https://api.vercel.com/v2/deployments/{id}/aliases`
Retrieves all Aliases for the Deployment with the given ID. The authenticated user or team must own the deployment.
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
