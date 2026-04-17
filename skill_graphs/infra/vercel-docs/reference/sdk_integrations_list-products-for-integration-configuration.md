Menu
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
List products for integration configuration
# List products for integration configuration
GET`https://api.vercel.com/v1/integrations/configuration/{id}/products`
Returns products available for an integration configuration. Each product includes a `metadataSchema` field with the JSON Schema for required and optional metadata fields.
Request
```


1

import { Vercel } from "@vercel/sdk";






2







3

const vercel = new Vercel({






4

  bearerToken: "<YOUR_BEARER_TOKEN_HERE>",






5

});






6







7

async function run() {






8

  const result = await vercel.integrations.getConfigurationProducts({






9

    id: "icfg_cuwj0AdCdH3BwWT4LPijCC7t",






10

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






11

    slug: "my-team-url-slug",






12

  });






13







14

  console.log(result);






15

}






16







17

run();




```

Response
```


1

{






2

  "products": [






3

    {






4

      "id": "icfg_1234567890",






5

      "slug": "string",






6

      "name": "Example Name",






7

      "protocols": {






8

        "storage": {






9

          "status": "disabled",






10

          "repl": {






11

            "enabled": "false",






12

            "supportsReadOnlyMode": "false",






13

            "welcomeMessage": "string"






14

          }






15

        },






16

        "experimentation": {






17

          "status": "disabled",






18

          "edgeConfigSyncingSupport": "false"






19

        },






20

        "ai": {






21

          "status": "disabled"






22

        },






23

        "authentication": {






24

          "status": "disabled"






25

        },






26

        "observability": {






27

          "status": "disabled"






28

        },






29

        "video": {






30

          "status": "disabled"






31

        },






32

        "workflow": {






33

          "status": "disabled"






34

        },






35

        "checks": {






36

          "status": "disabled"






37

        },






38

        "logDrain": {






39

          "status": "disabled",






40

          "endpoint": "string",






41

          "headers": "value",






42

          "format": "json"






43

        },






44

        "traceDrain": {






45

          "status": "disabled",






46

          "endpoint": "string",






47

          "headers": "value",






48

          "format": "json"






49

        },






50

        "messaging": {






51

          "status": "disabled"






52

        },






53

        "other": {






54

          "status": "disabled"






55

        }






56

      },






57

      "primaryProtocol": "checks",






58

      "metadataSchema": {






59

        "type": "object",






60

        "properties": "value",






61

        "required": []






62

      }






63

    }






64

  ],






65

  "integration": {






66

    "id": "icfg_1234567890",






67

    "slug": "string",






68

    "name": "Example Name"






69

  },






70

  "configuration": {






71

    "id": "icfg_1234567890"






72

  }






73

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/integrations/list-products-for-integration-configuration#authentication)[](https://vercel.com/docs/rest-api/sdk/integrations/list-products-for-integration-configuration#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/integrations/list-products-for-integration-configuration#path-parameters)[](https://vercel.com/docs/rest-api/sdk/integrations/list-products-for-integration-configuration#path-parameters)
idstringRequired
ID of the integration configuration
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/integrations/list-products-for-integration-configuration#query-parameters)[](https://vercel.com/docs/rest-api/sdk/integrations/list-products-for-integration-configuration#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sdk/integrations/list-products-for-integration-configuration#response)[](https://vercel.com/docs/rest-api/sdk/integrations/list-products-for-integration-configuration#response)
200List of products available for this integration configuration
productsarrayRequired
+Show 6 properties
integrationobjectRequired
+Show 3 properties
configurationobjectRequired
+Show 1 properties
##  [Errors](https://vercel.com/docs/rest-api/sdk/integrations/list-products-for-integration-configuration#errors)[](https://vercel.com/docs/rest-api/sdk/integrations/list-products-for-integration-configuration#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
500Error
