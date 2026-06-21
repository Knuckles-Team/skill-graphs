##  [Errors](https://vercel.com/docs#errors)[](https://vercel.com/docs#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
TypeScriptNext.jscURL
https://api.vercel.com/v1/installations/{integrationConfigurationId}
```


1

const response = await fetch('https://api.vercel.com/v1/installations/integrationConfigurationId', {






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

    "status": "ready",






9

    "externalId": "example_id",






10

    "billingPlan": {






11

      "id": "icfg_1234567890",






12

      "type": "prepayment",






13

      "name": "Example Name",






14

      "description": "string",






15

      "paymentMethodRequired": "true",






16

      "cost": "string",






17

      "details": [






18

        {






19

          "label": "string",






20

          "value": "string"






21

        }






22

      ],






23

      "highlightedDetails": [






24

        {






25

          "label": "string",






26

          "value": "string"






27

        }






28

      ],






29

      "effectiveDate": "string"






30

    },






31

    "notification": {






32

      "level": "info",






33

      "title": "string",






34

      "message": "string",






35

      "href": "https://example.com"






36

    }






37

  }),






38

});






39







40

const data = await response.json();






41

console.log(data);




```

Response
```


1

{}




```

Copy as MarkdownGive feedbackAsk AI about this page
Select an endpoint to view code samples
