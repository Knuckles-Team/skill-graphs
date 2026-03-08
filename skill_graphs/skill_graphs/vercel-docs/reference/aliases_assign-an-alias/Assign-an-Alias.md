# Assign an Alias
POST`https://api.vercel.com/v2/deployments/{id}/aliases`
Creates a new alias for the deployment with the given deployment ID. The authenticated user or team must own this deployment. If the desired alias is already assigned to another deployment, then it will be removed from the old deployment and assigned to the new one.
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
