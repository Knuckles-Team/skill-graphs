##  [Errors](https://vercel.com/docs#errors)[](https://vercel.com/docs#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
409Error
422Error
TypeScriptNext.jscURL
https://api.vercel.com/v1/installations/{integrationConfigurationId}/resources/{resourceId}
```


1

const response = await fetch('https://api.vercel.com/v1/installations/integrationConfigurationId/resources/resourceId', {






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

    "ownership": "owned",






9

    "name": "Example Name",






10

    "status": "ready",






11

    "metadata": "value",






12

    "billingPlan": {






13

      "id": "icfg_1234567890",






14

      "type": "prepayment",






15

      "name": "Example Name",






16

      "description": "string",






17

      "paymentMethodRequired": "true",






18

      "cost": "string",






19

      "details": [






20

        {






21

          "label": "string",






22

          "value": "string"






23

        }






24

      ],






25

      "highlightedDetails": [






26

        {






27

          "label": "string",






28

          "value": "string"






29

        }






30

      ],






31

      "effectiveDate": "string"






32

    },






33

    "notification": {






34

      "level": "info",






35

      "title": "string",






36

      "message": "string",






37

      "href": "https://example.com"






38

    },






39

    "extras": "value",






40

    "secrets": [






41

      {






42

        "name": "Example Name",






43

        "value": "string",






44

        "prefix": "string",






45

        "environmentOverrides": {






46

          "development": "string",






47

          "preview": "string",






48

          "production": "string"






49

        }






50

      }






51

    ]






52

  }),






53

});






54







55

const data = await response.json();






56

console.log(data);




```

Response
```


1

{






2

  "name": "Example Name"






3

}




```

Copy as MarkdownGive feedbackAsk AI about this page
Select an endpoint to view code samples
