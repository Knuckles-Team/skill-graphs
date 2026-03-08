##  [Errors](https://vercel.com/docs#errors)[](https://vercel.com/docs#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
409Error
422Error
TypeScriptNext.jscURL
https://api.vercel.com/v1/installations/{integrationConfigurationId}/resources/{resourceId}/secrets
```


1

const response = await fetch('https://api.vercel.com/v1/installations/integrationConfigurationId/resources/resourceId/secrets', {






2

  method: 'PUT',






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

    "secrets": [






9

      {






10

        "name": "Example Name",






11

        "value": "string",






12

        "prefix": "string",






13

        "environmentOverrides": {






14

          "development": "string",






15

          "preview": "string",






16

          "production": "string"






17

        }






18

      }






19

    ],






20

    "partial": "true"






21

  }),






22

});






23







24

const data = await response.json();






25

console.log(data);




```

Response
```


1

{}




```

Copy as MarkdownGive feedbackAsk AI about this page
Select an endpoint to view code samples
