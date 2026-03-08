##  [Errors](https://vercel.com/docs#errors)[](https://vercel.com/docs#errors)
403Operation failed because the authentication is not allowed to perform this operation
errorobjectRequired
+Show 3 properties
409Operation failed because of a conflict with the current state of the resource
errorobjectRequired
+Show 3 properties
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

Copy as MarkdownGive feedbackAsk AI about this page
Select an endpoint to view code samples
