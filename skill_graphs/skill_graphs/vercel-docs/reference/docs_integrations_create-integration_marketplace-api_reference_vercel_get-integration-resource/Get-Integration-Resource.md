# Get Integration Resource
GET`https://api.vercel.com/v1/installations/{integrationConfigurationId}/resources/{resourceId}`
Get a resource by its partner ID.
TypeScriptNext.jscURL
https://api.vercel.com/v1/installations/{integrationConfigurationId}/resources/{resourceId}
```


1

const response = await fetch('https://api.vercel.com/v1/installations/integrationConfigurationId/resources/resourceId', {






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

  "internalId": "example_id",






4

  "name": "Example Name",






5

  "status": "ready",






6

  "productId": "example_id",






7

  "protocolSettings": {






8

    "experimentation": {






9

      "edgeConfigSyncingEnabled": "false",






10

      "edgeConfigId": "example_id",






11

      "edgeConfigTokenId": "example_id"






12

    }






13

  },






14

  "notification": {






15

    "level": "error",






16

    "title": "string",






17

    "message": "string",






18

    "href": "string"






19

  },






20

  "billingPlanId": "example_id",






21

  "metadata": "value"






22

}




```
