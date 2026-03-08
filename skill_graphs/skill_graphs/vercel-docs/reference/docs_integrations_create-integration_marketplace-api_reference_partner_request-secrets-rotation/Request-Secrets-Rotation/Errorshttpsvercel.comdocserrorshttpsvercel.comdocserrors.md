##  [Errors](https://vercel.com/docs#errors)[](https://vercel.com/docs#errors)
400Input has failed validation
errorobjectRequired
+Show 4 properties
403Operation failed because the authentication is not allowed to perform this operation
errorobjectRequired
+Show 3 properties
409Operation failed because of a conflict with the current state of the resource
errorobjectRequired
+Show 3 properties
TypeScriptNext.jscURL
/v1/installations/{installationId}/resources/{resourceId}/secrets/rotate
```


1

const response = await fetch('/v1/installations/installationId/resources/resourceId/secrets/rotate', {






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

    "reason": "Customer requested refund",






9

    "delayOldSecretsExpirationHours": "123"






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

  "sync": "false"






3

}




```

400403409
Errors
```


1

{






2

  "error": {






3

    "code": "validation_error",






4

    "message": "string",






5

    "user": {






6

      "message": "string",






7

      "url": "https://example.com"






8

    },






9

    "fields": [






10

      {






11

        "key": "string",






12

        "message": "string"






13

      }






14

    ]






15

  }






16

}




```

Copy as MarkdownGive feedbackAsk AI about this page
Select an endpoint to view code samples
