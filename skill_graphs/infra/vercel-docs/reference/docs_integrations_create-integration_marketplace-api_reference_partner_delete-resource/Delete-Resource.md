# Delete Resource
DEL`/v1/installations/{installationId}/resources/{resourceId}`
Uninstalls and de-provisions a Resource
TypeScriptNext.jscURL
/v1/installations/{installationId}/resources/{resourceId}
```


1

const response = await fetch('/v1/installations/installationId/resources/resourceId', {






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

403409
Errors
```


1

{






2

  "error": {






3

    "code": "forbidden",






4

    "message": "string",






5

    "user": {






6

      "message": "string",






7

      "url": "https://example.com"






8

    }






9

  }






10

}




```
