##  [Errors](https://vercel.com/docs#errors)[](https://vercel.com/docs#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
TypeScriptNext.jscURL
https://api.vercel.com/v1/installations/{integrationConfigurationId}/member/{memberId}
```


1

const response = await fetch('https://api.vercel.com/v1/installations/integrationConfigurationId/member/memberId', {






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

  "id": "icfg_1234567890",






3

  "role": "ADMIN",






4

  "globalUserId": "example_id",






5

  "userEmail": "user@example.com"






6

}




```

Copy as MarkdownGive feedbackAsk AI about this page
Select an endpoint to view code samples
