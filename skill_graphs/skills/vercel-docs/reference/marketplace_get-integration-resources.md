Menu
APIs & SDKs
[Vercel REST API](https://vercel.com/docs/rest-api)
Get Integration Resources
# Get Integration Resources
GET`https://api.vercel.com/v1/installations/{integrationConfigurationId}/resources`
Get all resources for a given installation ID.
TypeScriptNext.jscURL
https://api.vercel.com/v1/installations/{integrationConfigurationId}/resources
```


1

const response = await fetch('https://api.vercel.com/v1/installations/integrationConfigurationId/resources', {






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

  "resources": [






3

    {






4

      "partnerId": "example_id",






5

      "internalId": "example_id",






6

      "name": "Example Name",






7

      "status": "error",






8

      "productId": "example_id",






9

      "protocolSettings": {






10

        "experimentation": {






11

          "edgeConfigSyncingEnabled": "false",






12

          "edgeConfigId": "example_id",






13

          "edgeConfigTokenId": "example_id"






14

        }






15

      },






16

      "notification": {






17

        "title": "string",






18

        "level": "error",






19

        "message": "string",






20

        "href": "string"






21

      },






22

      "billingPlanId": "example_id",






23

      "metadata": "value"






24

    }






25

  ]






26

}




```

##  [Authentication](https://vercel.com/docs/rest-api/marketplace/get-integration-resources#authentication)[](https://vercel.com/docs/rest-api/marketplace/get-integration-resources#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/marketplace/get-integration-resources#path-parameters)[](https://vercel.com/docs/rest-api/marketplace/get-integration-resources#path-parameters)
integrationConfigurationIdstringRequired
##  [Response](https://vercel.com/docs/rest-api/marketplace/get-integration-resources#response)[](https://vercel.com/docs/rest-api/marketplace/get-integration-resources#response)
200Success
resourcesarrayRequired
+Show 9 properties
##  [Errors](https://vercel.com/docs/rest-api/marketplace/get-integration-resources#errors)[](https://vercel.com/docs/rest-api/marketplace/get-integration-resources#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
