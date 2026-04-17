Menu
APIs & SDKs
[Vercel REST API](https://vercel.com/docs/rest-api)
Promote a staging version to production or restore a previous production version.
# Promote a staging version to production or restore a previous production version.
POST`https://api.vercel.com/v1/bulk-redirects/versions`
Update a version by promoting staging to production or restoring a previous production version
TypeScriptNext.jscURL
https://api.vercel.com/v1/bulk-redirects/versions
```


1

const response = await fetch('https://api.vercel.com/v1/bulk-redirects/versions?projectId=string&teamId=string&slug=string', {






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

    "id": "icfg_1234567890",






9

    "action": "promote",






10

    "name": "Example Name"






11

  }),






12

});






13







14

const data = await response.json();






15

console.log(data);




```

Response
```


1

{






2

  "version": {






3

    "id": "icfg_1234567890",






4

    "key": "string",






5

    "lastModified": "123",






6

    "createdBy": "string",






7

    "name": "Example Name",






8

    "isStaging": "false",






9

    "isLive": "false",






10

    "redirectCount": "123",






11

    "alias": "string"






12

  }






13

}




```

##  [Authentication](https://vercel.com/docs/rest-api/bulk-redirects/promote-a-staging-version-to-production-or-restore-a-previous-production-version#authentication)[](https://vercel.com/docs/rest-api/bulk-redirects/promote-a-staging-version-to-production-or-restore-a-previous-production-version#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Query parameters](https://vercel.com/docs/rest-api/bulk-redirects/promote-a-staging-version-to-production-or-restore-a-previous-production-version#query-parameters)[](https://vercel.com/docs/rest-api/bulk-redirects/promote-a-staging-version-to-production-or-restore-a-previous-production-version#query-parameters)
projectIdstringRequired
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Body](https://vercel.com/docs/rest-api/bulk-redirects/promote-a-staging-version-to-production-or-restore-a-previous-production-version#body)[](https://vercel.com/docs/rest-api/bulk-redirects/promote-a-staging-version-to-production-or-restore-a-previous-production-version#body)
application/json
idstringRequired
actionstringRequired
+Show 3 enum values
namestringOptional
##  [Response](https://vercel.com/docs/rest-api/bulk-redirects/promote-a-staging-version-to-production-or-restore-a-previous-production-version#response)[](https://vercel.com/docs/rest-api/bulk-redirects/promote-a-staging-version-to-production-or-restore-a-previous-production-version#response)
200Success
versionobjectRequired
+Show 9 properties
##  [Errors](https://vercel.com/docs/rest-api/bulk-redirects/promote-a-staging-version-to-production-or-restore-a-previous-production-version#errors)[](https://vercel.com/docs/rest-api/bulk-redirects/promote-a-staging-version-to-production-or-restore-a-previous-production-version#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
500Error
