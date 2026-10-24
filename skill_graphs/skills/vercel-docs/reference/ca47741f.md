##  [Errors](https://vercel.com/docs#errors)[](https://vercel.com/docs#errors)
400One of the provided values in the request query is invalid. One of the provided values in the headers is invalid File size is not valid
401The request is not authorized.
402The account was soft-blocked for an unhandled reason. The account is missing a payment so payment method must be updated
403The customer has reached their spend cap limit and has been paused. An owner can disable the cap or raise the limit in settings. The Remote Caching usage limit has been reached for this account for this billing cycle. Remote Caching has been disabled for this team or user. An owner can enable it in the billing settings. You do not have permission to access this resource.
TypeScriptNext.jscURL
https://api.vercel.com/v8/artifacts/{hash}
```


1

const response = await fetch('https://api.vercel.com/v8/artifacts/hash?teamId=string&slug=string', {






2

  method: 'PUT',






3

  headers: {






4

    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',






5

    'Content-Type': 'application/json',






6

    'Content-Length': '123',






7

  },






8

});






9







10

const data = await response.json();






11

console.log(data);




```

Response
```


1

{






2

  "urls": []






3

}




```

Copy as MarkdownGive feedbackAsk AI about this page
