Menu
APIs & SDKs
[Vercel REST API](https://vercel.com/docs/rest-api)
Get Integration Resource
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

  "status": "error",






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

    "title": "string",






16

    "level": "error",






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

##  [Authentication](https://vercel.com/docs/rest-api/marketplace/get-integration-resource#authentication)[](https://vercel.com/docs/rest-api/marketplace/get-integration-resource#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/marketplace/get-integration-resource#path-parameters)[](https://vercel.com/docs/rest-api/marketplace/get-integration-resource#path-parameters)
integrationConfigurationIdstringRequired
The ID of the integration configuration (installation) the resource belongs to
resourceIdstringRequired
The ID provided by the 3rd party provider for the given resource
##  [Response](https://vercel.com/docs/rest-api/marketplace/get-integration-resource#response)[](https://vercel.com/docs/rest-api/marketplace/get-integration-resource#response)
200Success
idstringRequired
The ID provided by the 3rd party provider for the given resource
internalIdstringRequired
The ID assigned by Vercel for the given resource
namestringRequired
The name of the resource as it is recorded in Vercel
statusstringOptional
The current status of the resource
+Show 7 enum values
productIdstringRequired
The ID of the product the resource is derived from
protocolSettingsobjectOptional
Any settings provided for the resource to support its product's protocols
+Show 1 properties
notificationobjectOptional
The notification, if set, displayed to the user when viewing the resource in Vercel
+Show 4 properties
billingPlanIdstringOptional
The ID of the billing plan the resource is subscribed to, if applicable
metadataobjectOptional
The configured metadata for the resource as defined by its product's Metadata Schema
##  [Errors](https://vercel.com/docs/rest-api/marketplace/get-integration-resource#errors)[](https://vercel.com/docs/rest-api/marketplace/get-integration-resource#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
