# Request Secrets Rotation
POST`/v1/installations/{installationId}/resources/{resourceId}/secrets/rotate`
Request rotation of secrets for a specific resource
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
