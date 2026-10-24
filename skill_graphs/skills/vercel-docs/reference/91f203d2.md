##  [Errors](https://vercel.com/docs#errors)[](https://vercel.com/docs#errors)
400Error
401The request is not authorized.
402The account was soft-blocked for an unhandled reason. The account is missing a payment so payment method must be updated
403You do not have permission to access this resource.
TypeScriptNext.jscURL
https://api.vercel.com/v8/artifacts/status
```


1

const response = await fetch('https://api.vercel.com/v8/artifacts/status?teamId=string&slug=string', {






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

  "status": "disabled"






3

}




```

Copy as MarkdownGive feedbackAsk AI about this page
