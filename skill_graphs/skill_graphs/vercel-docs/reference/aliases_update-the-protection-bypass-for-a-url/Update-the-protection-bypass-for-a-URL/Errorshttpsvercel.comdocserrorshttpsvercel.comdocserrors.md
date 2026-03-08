##  [Errors](https://vercel.com/docs#errors)[](https://vercel.com/docs#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
409Error
428Error
TypeScriptNext.jscURL
https://api.vercel.com/aliases/{id}/protection-bypass
```


1

const response = await fetch('https://api.vercel.com/aliases/id/protection-bypass?teamId=string&slug=string', {






2

  method: 'PATCH',






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

    "ttl": "123",






9

    "revoke": {






10

      "secret": "string",






11

      "regenerate": "true"






12

    }






13

  }),






14

});






15







16

const data = await response.json();






17

console.log(data);




```

Response
```


1
"value"



```

Copy as MarkdownGive feedbackAsk AI about this page
