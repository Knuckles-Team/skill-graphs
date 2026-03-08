# Import Resource
PUT`https://api.vercel.com/v1/installations/{integrationConfigurationId}/resources/{resourceId}`
This endpoint imports (upserts) a resource to Vercel's installation. This may be needed if resources can be independently created on the partner's side and need to be synchronized to Vercel.
TypeScriptNext.jscURL
https://api.vercel.com/v1/installations/{integrationConfigurationId}/resources/{resourceId}
```


1

const response = await fetch('https://api.vercel.com/v1/installations/integrationConfigurationId/resources/resourceId', {






2

  method: 'PUT',






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

    "productId": "example_id",






10

    "name": "Example Name",






11

    "status": "ready",






12

    "metadata": "value",






13

    "billingPlan": {






14

      "id": "icfg_1234567890",






15

      "type": "prepayment",






16

      "name": "Example Name",






17

      "description": "string",






18

      "paymentMethodRequired": "true",






19

      "cost": "string",






20

      "details": [






21

        {






22

          "label": "string",






23

          "value": "string"






24

        }






25

      ],






26

      "highlightedDetails": [






27

        {






28

          "label": "string",






29

          "value": "string"






30

        }






31

      ],






32

      "effectiveDate": "string"






33

    },






34

    "notification": {






35

      "level": "info",






36

      "title": "string",






37

      "message": "string",






38

      "href": "https://example.com"






39

    },






40

    "extras": "value",






41

    "secrets": [






42

      {






43

        "name": "Example Name",






44

        "value": "string",






45

        "prefix": "string",






46

        "environmentOverrides": {






47

          "development": "string",






48

          "preview": "string",






49

          "production": "string"






50

        }






51

      }






52

    ]






53

  }),






54

});






55







56

const data = await response.json();






57

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
