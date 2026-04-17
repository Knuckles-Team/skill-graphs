Menu
APIs & SDKs
[Vercel REST API](https://vercel.com/docs/rest-api)
Restore staged project-level redirects to their production version.
# Restore staged project-level redirects to their production version.
POST`https://api.vercel.com/v1/bulk-redirects/restore`
Restores the provided redirects in the staging version to the value in the production version. If no production version exists, removes the redirects from staging.
TypeScriptNext.jscURL
https://api.vercel.com/v1/bulk-redirects/restore
```


1

const response = await fetch('https://api.vercel.com/v1/bulk-redirects/restore?projectId=string&teamId=string&slug=string', {






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

    "name": "Example Name",






9

    "redirects": []






10

  }),






11

});






12







13

const data = await response.json();






14

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

  },






13

  "restored": [],






14

  "failedToRestore": []






15

}




```

##  [Authentication](https://vercel.com/docs/rest-api/bulk-redirects/restore-staged-project-level-redirects-to-their-production-version#authentication)[](https://vercel.com/docs/rest-api/bulk-redirects/restore-staged-project-level-redirects-to-their-production-version#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Query parameters](https://vercel.com/docs/rest-api/bulk-redirects/restore-staged-project-level-redirects-to-their-production-version#query-parameters)[](https://vercel.com/docs/rest-api/bulk-redirects/restore-staged-project-level-redirects-to-their-production-version#query-parameters)
projectIdstringRequired
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Body](https://vercel.com/docs/rest-api/bulk-redirects/restore-staged-project-level-redirects-to-their-production-version#body)[](https://vercel.com/docs/rest-api/bulk-redirects/restore-staged-project-level-redirects-to-their-production-version#body)
application/json
namestringOptional
redirectsarrayRequired
The redirects to restore. The source of the redirect is used to match the redirect to restore.
##  [Response](https://vercel.com/docs/rest-api/bulk-redirects/restore-staged-project-level-redirects-to-their-production-version#response)[](https://vercel.com/docs/rest-api/bulk-redirects/restore-staged-project-level-redirects-to-their-production-version#response)
200Success
versionobjectRequired
+Show 9 properties
restoredarrayRequired
failedToRestorearrayRequired
##  [Errors](https://vercel.com/docs/rest-api/bulk-redirects/restore-staged-project-level-redirects-to-their-production-version#errors)[](https://vercel.com/docs/rest-api/bulk-redirects/restore-staged-project-level-redirects-to-their-production-version#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
500Error
