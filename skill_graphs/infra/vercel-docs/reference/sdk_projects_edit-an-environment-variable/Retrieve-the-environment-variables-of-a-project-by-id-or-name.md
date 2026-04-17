# Retrieve the environment variables of a project by id or name
GET`https://api.vercel.com/v10/projects/{idOrName}/env`
Retrieve the environment variables for a given project by passing either the project `id` or `name` in the URL.
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

  const result = await vercel.projects.filterProjectEnvs({






9

    idOrName: "prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA",






10

    gitBranch: "feature-1",






11

    decrypt: "true",






12

    source: "vercel-cli:pull",






13

    customEnvironmentId: "env_123abc4567",






14

    customEnvironmentSlug: "my-custom-env",






15

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






16

    slug: "my-team-url-slug",






17

  });






18







19

  console.log(result);






20

}






21







22

run();




```

Response
```


1

{






2

  "target": [],






3

  "type": "secret",






4

  "sunsetSecretId": "example_id",






5

  "legacyValue": "string",






6

  "decrypted": "false",






7

  "value": "string",






8

  "vsmValue": "string",






9

  "id": "icfg_1234567890",






10

  "key": "string",






11

  "configurationId": "example_id",






12

  "createdAt": "123",






13

  "updatedAt": "123",






14

  "createdBy": "string",






15

  "updatedBy": "string",






16

  "gitBranch": "string",






17

  "edgeConfigId": "example_id",






18

  "edgeConfigTokenId": "example_id",






19

  "contentHint": {






20

    "type": "redis-url",






21

    "storeId": "example_id"






22

  },






23

  "internalContentHint": {






24

    "type": "flags-secret",






25

    "encryptedValue": "string"






26

  },






27

  "comment": "string",






28

  "customEnvironmentIds": [],






29

  "system": "false"






30

}




```

##  [Authentication](https://vercel.com/docs/rest-api/sdk/projects/retrieve-the-environment-variables-of-a-project-by-id-or-name#authentication)[](https://vercel.com/docs/rest-api/sdk/projects/retrieve-the-environment-variables-of-a-project-by-id-or-name#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/sdk/projects/retrieve-the-environment-variables-of-a-project-by-id-or-name#path-parameters)[](https://vercel.com/docs/rest-api/sdk/projects/retrieve-the-environment-variables-of-a-project-by-id-or-name#path-parameters)
idOrNamestringRequired
The unique project identifier or the project name
##  [Query parameters](https://vercel.com/docs/rest-api/sdk/projects/retrieve-the-environment-variables-of-a-project-by-id-or-name#query-parameters)[](https://vercel.com/docs/rest-api/sdk/projects/retrieve-the-environment-variables-of-a-project-by-id-or-name#query-parameters)
gitBranchstringOptional
If defined, the git branch of the environment variable to filter the results (must have target=preview)
decryptstringOptionalDeprecated
If true, the environment variable value will be decrypted
+Show 2 enum values
sourcestringOptional
The source that is calling the endpoint.
customEnvironmentIdstringOptional
The unique custom environment identifier within the project
customEnvironmentSlugstringOptional
The custom environment slug (name) within the project
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/sdk/projects/retrieve-the-environment-variables-of-a-project-by-id-or-name#response)[](https://vercel.com/docs/rest-api/sdk/projects/retrieve-the-environment-variables-of-a-project-by-id-or-name#response)
200The list of environment variables for the given project
targetobjectOptional2 variants
+Show 2 variants
typestringRequired
+Show 5 enum values
sunsetSecretIdstringOptional
This is used to identify variables that have been migrated from type secret to sensitive.
legacyValuestringOptional
Legacy now-encryption ciphertext, present after migration swaps value/vsmValue
decryptedbooleanOptional
+Show 2 enum values
valuestringRequired
vsmValuestringOptional
idstringOptional
keystringRequired
configurationIdstringOptional
createdAtnumberOptional
updatedAtnumberOptional
createdBystringOptional
updatedBystringOptional
gitBranchstringOptional
edgeConfigIdstringOptional
edgeConfigTokenIdstringOptional
contentHintobjectOptional15 variants
+Show 15 variants
internalContentHintobjectOptional
Similar to `contentHints`, but should not be exposed to the user.
+Show 2 properties
commentstringOptional
customEnvironmentIdsarrayOptional
systembooleanOptional
+Show 2 enum values
##  [Errors](https://vercel.com/docs/rest-api/sdk/projects/retrieve-the-environment-variables-of-a-project-by-id-or-name#errors)[](https://vercel.com/docs/rest-api/sdk/projects/retrieve-the-environment-variables-of-a-project-by-id-or-name#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
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

  const result = await vercel.projects.filterProjectEnvs({






9

    idOrName: "prj_XLKmu1DyR1eY7zq8UgeRKbA7yVLA",






10

    gitBranch: "feature-1",






11

    decrypt: "true",






12

    source: "vercel-cli:pull",






13

    customEnvironmentId: "env_123abc4567",






14

    customEnvironmentSlug: "my-custom-env",






15

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






16

    slug: "my-team-url-slug",






17

  });






18







19

  console.log(result);






20

}






21







22

run();




```

Response
```


1

{






2

  "target": [],






3

  "type": "secret",






4

  "sunsetSecretId": "example_id",






5

  "legacyValue": "string",






6

  "decrypted": "false",






7

  "value": "string",






8

  "vsmValue": "string",






9

  "id": "icfg_1234567890",






10

  "key": "string",






11

  "configurationId": "example_id",






12

  "createdAt": "123",






13

  "updatedAt": "123",






14

  "createdBy": "string",






15

  "updatedBy": "string",






16

  "gitBranch": "string",






17

  "edgeConfigId": "example_id",






18

  "edgeConfigTokenId": "example_id",






19

  "contentHint": {






20

    "type": "redis-url",






21

    "storeId": "example_id"






22

  },






23

  "internalContentHint": {






24

    "type": "flags-secret",






25

    "encryptedValue": "string"






26

  },






27

  "comment": "string",






28

  "customEnvironmentIds": [],






29

  "system": "false"






30

}




```

Copy as MarkdownGive feedbackAsk AI about this page
APIs & SDKs
[Vercel SDK](https://vercel.com/docs/rest-api/sdk)
Edit an environment variable
