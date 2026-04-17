# Create one or more environment variables
POST`https://api.vercel.com/v10/projects/{idOrName}/env`
Create one or more environment variables for a project by passing its `key`, `value`, `type` and `target` and by specifying the project by either passing the project `id` or `name` in the URL. If you include `upsert=true` as a query parameter, a new environment variable will not be created if it already exists but, the existing variable's value will be updated.
TypeScriptNext.jscURL
https://api.vercel.com/v10/projects/{idOrName}/env
```


1

const response = await fetch('https://api.vercel.com/v10/projects/idOrName/env?upsert=string&teamId=string&slug=string', {






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

    "key": "API_URL",






9

    "value": "https://api.vercel.com",






10

    "type": "plain",






11

    "target": [],






12

    "gitBranch": "feature-1",






13

    "comment": "database connection string for production",






14

    "customEnvironmentIds": []






15

  }),






16

});






17







18

const data = await response.json();






19

console.log(data);




```

Response
```


1

{






2

  "created": {






3

    "target": [],






4

    "type": "secret",






5

    "sunsetSecretId": "example_id",






6

    "legacyValue": "string",






7

    "decrypted": "false",






8

    "value": "string",






9

    "vsmValue": "string",






10

    "id": "icfg_1234567890",






11

    "key": "string",






12

    "configurationId": "example_id",






13

    "createdAt": "123",






14

    "updatedAt": "123",






15

    "createdBy": "string",






16

    "updatedBy": "string",






17

    "gitBranch": "string",






18

    "edgeConfigId": "example_id",






19

    "edgeConfigTokenId": "example_id",






20

    "contentHint": {






21

      "type": "redis-url",






22

      "storeId": "example_id"






23

    },






24

    "internalContentHint": {






25

      "type": "flags-secret",






26

      "encryptedValue": "string"






27

    },






28

    "comment": "string",






29

    "customEnvironmentIds": [],






30

    "system": "false"






31

  },






32

  "failed": [






33

    {






34

      "error": {






35

        "code": "string",






36

        "message": "string",






37

        "key": "string",






38

        "envVarId": "example_id",






39

        "envVarKey": "string",






40

        "action": "string",






41

        "link": "string",






42

        "value": "string",






43

        "gitBranch": "string",






44

        "target": [],






45

        "project": "string"






46

      }






47

    }






48

  ]






49

}




```

##  [Authentication](https://vercel.com/docs/rest-api/projects/create-one-or-more-environment-variables#authentication)[](https://vercel.com/docs/rest-api/projects/create-one-or-more-environment-variables#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/projects/create-one-or-more-environment-variables#path-parameters)[](https://vercel.com/docs/rest-api/projects/create-one-or-more-environment-variables#path-parameters)
idOrNamestringRequired
The unique project identifier or the project name
##  [Query parameters](https://vercel.com/docs/rest-api/projects/create-one-or-more-environment-variables#query-parameters)[](https://vercel.com/docs/rest-api/projects/create-one-or-more-environment-variables#query-parameters)
upsertstringOptional
Allow override of environment variable if it already exists
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Body](https://vercel.com/docs/rest-api/projects/create-one-or-more-environment-variables#body)[](https://vercel.com/docs/rest-api/projects/create-one-or-more-environment-variables#body)
application/json
Option 1Option 2
keystringRequired
The name of the environment variable
valuestringRequired
The value of the environment variable
typestringRequired
The type of environment variable
+Show 5 enum values
targetarrayOptional
The target environment of the environment variable
gitBranchstringOptional
If defined, the git branch of the environment variable (must have target=preview)
commentstringOptional
A comment to add context on what this environment variable is for
customEnvironmentIdsarrayOptional
The custom environment IDs associated with the environment variable
##  [Response](https://vercel.com/docs/rest-api/projects/create-one-or-more-environment-variables#response)[](https://vercel.com/docs/rest-api/projects/create-one-or-more-environment-variables#response)
201The environment variable was created successfully
createdobjectRequired
+Show 22 properties
failedarrayRequired
+Show 1 properties
##  [Errors](https://vercel.com/docs/rest-api/projects/create-one-or-more-environment-variables#errors)[](https://vercel.com/docs/rest-api/projects/create-one-or-more-environment-variables#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid. The environment variable couldn't be created because an ongoing update env update is already happening The environment variable couldn't be created because project document is too large
401The request is not authorized.
402The account was soft-blocked for an unhandled reason. The account is missing a payment so payment method must be updated
403You do not have permission to access this resource. The environment variable cannot be created because it already exists Additional permissions are required to create production environment variables
404Error
409The project is being transferred and creating an environment variable is not possible
429Error
500Error
TypeScriptNext.jscURL
https://api.vercel.com/v10/projects/{idOrName}/env
```


1

const response = await fetch('https://api.vercel.com/v10/projects/idOrName/env?upsert=string&teamId=string&slug=string', {






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

    "key": "API_URL",






9

    "value": "https://api.vercel.com",






10

    "type": "plain",






11

    "target": [],






12

    "gitBranch": "feature-1",






13

    "comment": "database connection string for production",






14

    "customEnvironmentIds": []






15

  }),






16

});






17







18

const data = await response.json();






19

console.log(data);




```

Response
```


1

{






2

  "created": {






3

    "target": [],






4

    "type": "secret",






5

    "sunsetSecretId": "example_id",






6

    "legacyValue": "string",






7

    "decrypted": "false",






8

    "value": "string",






9

    "vsmValue": "string",






10

    "id": "icfg_1234567890",






11

    "key": "string",






12

    "configurationId": "example_id",






13

    "createdAt": "123",






14

    "updatedAt": "123",






15

    "createdBy": "string",






16

    "updatedBy": "string",






17

    "gitBranch": "string",






18

    "edgeConfigId": "example_id",






19

    "edgeConfigTokenId": "example_id",






20

    "contentHint": {






21

      "type": "redis-url",






22

      "storeId": "example_id"






23

    },






24

    "internalContentHint": {






25

      "type": "flags-secret",






26

      "encryptedValue": "string"






27

    },






28

    "comment": "string",






29

    "customEnvironmentIds": [],






30

    "system": "false"






31

  },






32

  "failed": [






33

    {






34

      "error": {






35

        "code": "string",






36

        "message": "string",






37

        "key": "string",






38

        "envVarId": "example_id",






39

        "envVarKey": "string",






40

        "action": "string",






41

        "link": "string",






42

        "value": "string",






43

        "gitBranch": "string",






44

        "target": [],






45

        "project": "string"






46

      }






47

    }






48

  ]






49

}




```

Copy as MarkdownGive feedbackAsk AI about this page
APIs & SDKs
[Vercel REST API](https://vercel.com/docs/rest-api)
Remove an environment variable
