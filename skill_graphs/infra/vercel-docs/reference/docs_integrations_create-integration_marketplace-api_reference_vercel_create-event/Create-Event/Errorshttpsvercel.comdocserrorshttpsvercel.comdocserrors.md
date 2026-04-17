##  [Errors](https://vercel.com/docs#errors)[](https://vercel.com/docs#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
TypeScriptNext.jscURL
https://api.vercel.com/v1/installations/{integrationConfigurationId}/events
```


1

const response = await fetch('https://api.vercel.com/v1/installations/integrationConfigurationId/events', {






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

    "event": {






9

      "type": "installation.updated",






10

      "billingPlanId": "example_id"






11

    }






12

  }),






13

});






14







15

const data = await response.json();






16

console.log(data);




```

Response
```


1

{}




```

Copy as MarkdownGive feedbackAsk AI about this page
Select an endpoint to view code samples
