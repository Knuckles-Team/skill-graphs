##  [Errors](https://vercel.com/docs#errors)[](https://vercel.com/docs#errors)
400Input has failed validation
errorobjectRequired
+Show 4 properties
403Operation failed because the authentication is not allowed to perform this operation
errorobjectRequired
+Show 3 properties
409Operation failed because of a conflict with the current state of the resource
errorobjectRequired
+Show 3 properties
TypeScriptNext.jscURL
/v1/installations/{installationId}/resources
```


1

const response = await fetch('/v1/installations/installationId/resources', {






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

    "productId": "example_id",






9

    "name": "Example Name",






10

    "metadata": "value",






11

    "billingPlanId": "example_id",






12

    "externalId": "example_id",






13

    "protocolSettings": {






14

      "experimentation": {






15

        "edgeConfigId": "example_id"






16

      }






17

    }






18

  }),






19

});






20







21

const data = await response.json();






22

console.log(data);




```

Response
```


1

{






2

  "id": "icfg_1234567890",






3

  "productId": "example_id",






4

  "protocolSettings": {






5

    "experimentation": {






6

      "edgeConfigSyncingEnabled": "true",






7

      "edgeConfigId": "example_id",






8

      "edgeConfigTokenId": "example_id"






9

    }






10

  },






11

  "billingPlan": {






12

    "id": "icfg_1234567890",






13

    "type": "prepayment",






14

    "name": "Example Name",






15

    "scope": "installation",






16

    "description": "string",






17

    "paymentMethodRequired": "true",






18

    "preauthorizationAmount": "123",






19

    "initialCharge": "string",






20

    "minimumAmount": "100.00",






21

    "maximumAmount": "100.00",






22

    "maximumAmountAutoPurchasePerPeriod": "100.00",






23

    "cost": "string",






24

    "details": [






25

      {






26

        "label": "string",






27

        "value": "string"






28

      }






29

    ],






30

    "highlightedDetails": [






31

      {






32

        "label": "string",






33

        "value": "string"






34

      }






35

    ],






36

    "quote": [






37

      {






38

        "line": "string",






39

        "amount": "100.00"






40

      }






41

    ],






42

    "effectiveDate": "2024-01-01T00:00:00Z",






43

    "disabled": "true"






44

  },






45

  "name": "Example Name",






46

  "metadata": "value",






47

  "status": "ready",






48

  "notification": {






49

    "level": "info",






50

    "title": "string",






51

    "message": "string",






52

    "href": "https://example.com"






53

  },






54

  "secrets": [






55

    {






56

      "name": "Example Name",






57

      "value": "string",






58

      "prefix": "string",






59

      "environmentOverrides": {






60

        "development": "string",






61

        "preview": "string",






62

        "production": "string"






63

      }






64

    }






65

  ]






66

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

Copy as MarkdownGive feedbackAsk AI about this page
Select an endpoint to view code samples
