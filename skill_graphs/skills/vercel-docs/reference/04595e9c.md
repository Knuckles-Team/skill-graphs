##  [Errors](https://vercel.com/docs#errors)[](https://vercel.com/docs#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
TypeScriptNext.jscURL
https://api.vercel.com/v1/installations/{integrationConfigurationId}/account
```


1

const response = await fetch('https://api.vercel.com/v1/installations/integrationConfigurationId/account', {






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

  "name": "Example Name",






3

  "url": "https://example.com",






4

  "contact": {






5

    "email": "user@example.com",






6

    "name": "Example Name"






7

  }






8

}




```

Copy as MarkdownGive feedbackAsk AI about this page
Select an endpoint to view code samples
