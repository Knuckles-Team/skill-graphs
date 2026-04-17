# Update Installation
PATCH`/v1/installations/{installationId}`
Update an installation
TypeScriptNext.jscURL
/v1/installations/{installationId}
```


1

const response = await fetch('/v1/installations/installationId', {






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

    "billingPlanId": "example_id"






9

  }),






10

});






11







12

const data = await response.json();






13

console.log(data);




```

Response
```


1

{






2

  "billingPlan": {






3

    "id": "icfg_1234567890",






4

    "type": "prepayment",






5

    "name": "Example Name",






6

    "scope": "installation",






7

    "description": "string",






8

    "paymentMethodRequired": "true",






9

    "preauthorizationAmount": "123",






10

    "initialCharge": "string",






11

    "minimumAmount": "100.00",






12

    "maximumAmount": "100.00",






13

    "maximumAmountAutoPurchasePerPeriod": "100.00",






14

    "cost": "string",






15

    "details": [






16

      {






17

        "label": "string",






18

        "value": "string"






19

      }






20

    ],






21

    "highlightedDetails": [






22

      {






23

        "label": "string",






24

        "value": "string"






25

      }






26

    ],






27

    "quote": [






28

      {






29

        "line": "string",






30

        "amount": "100.00"






31

      }






32

    ],






33

    "effectiveDate": "2024-01-01T00:00:00Z",






34

    "disabled": "true"






35

  },






36

  "notification": {






37

    "level": "info",






38

    "title": "string",






39

    "message": "string",






40

    "href": "https://example.com"






41

  }






42

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
