# Deprecated: true. Update Resource Secrets (Deprecated)
PUT`https://api.vercel.com/v1/installations/{integrationConfigurationId}/products/{integrationProductIdOrSlug}/resources/{resourceId}/secrets`
This endpoint is deprecated and replaced with the endpoint [Update Resource Secrets](https://vercel.com/docs#update-resource-secrets).
This endpoint updates the secrets of a resource. If a resource has projects connected, the connected secrets are updated with the new secrets. The old secrets may still be used by existing connected projects because they are not automatically redeployed. Redeployment is a manual action and must be completed by the user. All new project connections will use the new secrets.

Use cases for this endpoint:

- Resetting the credentials of a database in the partner. If the user requests the credentials to be updated in the partner’s application, the partner post the new set of secrets to Vercel, the user should redeploy their application and the expire the old credentials.

This endpoint is deprecated
TypeScriptNext.jscURL
https://api.vercel.com/v1/installations/{integrationConfigurationId}/products/{integrationProductIdOrSlug}/resources/{resourceId}/secrets
```


1

const response = await fetch('https://api.vercel.com/v1/installations/integrationConfigurationId/products/integrationProductIdOrSlug/resources/resourceId/secrets', {






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

    "secrets": [






9

      {






10

        "name": "Example Name",






11

        "value": "string",






12

        "prefix": "string",






13

        "environmentOverrides": {






14

          "development": "string",






15

          "preview": "string",






16

          "production": "string"






17

        }






18

      }






19

    ],






20

    "partial": "true"






21

  }),






22

});






23







24

const data = await response.json();






25

console.log(data);




```

Response
```


1

{}




```
