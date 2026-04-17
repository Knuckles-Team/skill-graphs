# Retrieve the decrypted value of a Shared Environment Variable by id.
GET`https://api.vercel.com/v1/env/{id}`
Retrieve the decrypted value of a Shared Environment Variable by id.
TypeScriptNext.jscURL
https://api.vercel.com/v1/env/{id}
```


1

const response = await fetch('https://api.vercel.com/v1/env/id?teamId=string&slug=string', {






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

  "created": "2021-02-10T13:11:49.180Z",






3

  "key": "my-api-key",






4

  "ownerId": "team_LLHUOMOoDlqOp8wPE4kFo9pE",






5

  "id": "env_XCG7t7AIHuO2SBA8667zNUiM",






6

  "createdBy": "2qDDuGFTWXBLDNnqZfWPDp1A",






7

  "deletedBy": "2qDDuGFTWXBLDNnqZfWPDp1A",






8

  "updatedBy": "2qDDuGFTWXBLDNnqZfWPDp1A",






9

  "createdAt": "1609492210000",






10

  "deletedAt": "1609492210000",






11

  "updatedAt": "1609492210000",






12

  "value": "string",






13

  "projectId": [],






14

  "type": "encrypted",






15

  "target": [],






16

  "applyToAllCustomEnvironments": "false",






17

  "decrypted": "false",






18

  "comment": "string",






19

  "lastEditedByDisplayName": "Example Name"






20

}




```

##  [Authentication](https://vercel.com/docs/rest-api/environment/retrieve-the-decrypted-value-of-a-shared-environment-variable-by-id#authentication)[](https://vercel.com/docs/rest-api/environment/retrieve-the-decrypted-value-of-a-shared-environment-variable-by-id#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/environment/retrieve-the-decrypted-value-of-a-shared-environment-variable-by-id#path-parameters)[](https://vercel.com/docs/rest-api/environment/retrieve-the-decrypted-value-of-a-shared-environment-variable-by-id#path-parameters)
idstringRequired
The unique ID for the Shared Environment Variable to get the decrypted value.
##  [Query parameters](https://vercel.com/docs/rest-api/environment/retrieve-the-decrypted-value-of-a-shared-environment-variable-by-id#query-parameters)[](https://vercel.com/docs/rest-api/environment/retrieve-the-decrypted-value-of-a-shared-environment-variable-by-id#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/environment/retrieve-the-decrypted-value-of-a-shared-environment-variable-by-id#response)[](https://vercel.com/docs/rest-api/environment/retrieve-the-decrypted-value-of-a-shared-environment-variable-by-id#response)
200Success
createdstringOptional
The date when the Shared Env Var was created.
keystringOptional
The name of the Shared Env Var.
ownerIdstringOptional
The unique identifier of the owner (team) the Shared Env Var was created for.
idstringOptional
The unique identifier of the Shared Env Var.
createdBystringOptional
The unique identifier of the user who created the Shared Env Var.
deletedBystringOptional
The unique identifier of the user who deleted the Shared Env Var.
updatedBystringOptional
The unique identifier of the user who last updated the Shared Env Var.
createdAtnumberOptional
Timestamp for when the Shared Env Var was created.
deletedAtnumberOptional
Timestamp for when the Shared Env Var was (soft) deleted.
updatedAtnumberOptional
Timestamp for when the Shared Env Var was last updated.
valuestringOptional
The value of the Shared Env Var.
projectIdarrayOptional
The unique identifiers of the projects which the Shared Env Var is linked to.
typestringOptional
The type of this cosmos doc instance, if blank, assume secret.
+Show 4 enum values
targetarrayOptional
environments this env variable targets
applyToAllCustomEnvironmentsbooleanOptional
whether or not this env variable applies to custom environments
+Show 2 enum values
decryptedbooleanOptional
whether or not this env variable is decrypted
+Show 2 enum values
commentstringOptional
A user provided comment that describes what this Shared Env Var is for.
lastEditedByDisplayNamestringOptional
The last editor full name or username.
##  [Errors](https://vercel.com/docs/rest-api/environment/retrieve-the-decrypted-value-of-a-shared-environment-variable-by-id#errors)[](https://vercel.com/docs/rest-api/environment/retrieve-the-decrypted-value-of-a-shared-environment-variable-by-id#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
TypeScriptNext.jscURL
https://api.vercel.com/v1/env/{id}
```


1

const response = await fetch('https://api.vercel.com/v1/env/id?teamId=string&slug=string', {






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

  "created": "2021-02-10T13:11:49.180Z",






3

  "key": "my-api-key",






4

  "ownerId": "team_LLHUOMOoDlqOp8wPE4kFo9pE",






5

  "id": "env_XCG7t7AIHuO2SBA8667zNUiM",






6

  "createdBy": "2qDDuGFTWXBLDNnqZfWPDp1A",






7

  "deletedBy": "2qDDuGFTWXBLDNnqZfWPDp1A",






8

  "updatedBy": "2qDDuGFTWXBLDNnqZfWPDp1A",






9

  "createdAt": "1609492210000",






10

  "deletedAt": "1609492210000",






11

  "updatedAt": "1609492210000",






12

  "value": "string",






13

  "projectId": [],






14

  "type": "encrypted",






15

  "target": [],






16

  "applyToAllCustomEnvironments": "false",






17

  "decrypted": "false",






18

  "comment": "string",






19

  "lastEditedByDisplayName": "Example Name"






20

}




```

Copy as MarkdownGive feedbackAsk AI about this page
APIs & SDKs
[Vercel REST API](https://vercel.com/docs/rest-api)
Create a custom environment for the current project.
