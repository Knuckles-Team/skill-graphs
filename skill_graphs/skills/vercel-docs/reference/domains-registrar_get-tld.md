Menu
APIs & SDKs
[Vercel REST API](https://vercel.com/docs/rest-api)
Get TLD
# Get TLD
GET`https://api.vercel.com/v1/registrar/tlds/{tld}`
Get the metadata for a specific TLD.
TypeScriptNext.jscURL
https://api.vercel.com/v1/registrar/tlds/{tld}
```


1

const response = await fetch('https://api.vercel.com/v1/registrar/tlds/tld?teamId=string', {






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

  "supportedLanguageCodes": {}






3

}




```

Errors
400
400 401 403 429 500
```


1

{






2

  "status": "400",






3

  "code": "tld_not_supported",






4

  "message": "string"






5

}




```

##  [Authentication](https://vercel.com/docs/rest-api/domains-registrar/get-tld#authentication)[](https://vercel.com/docs/rest-api/domains-registrar/get-tld#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/domains-registrar/get-tld#path-parameters)[](https://vercel.com/docs/rest-api/domains-registrar/get-tld#path-parameters)
tldstringRequired
##  [Query parameters](https://vercel.com/docs/rest-api/domains-registrar/get-tld#query-parameters)[](https://vercel.com/docs/rest-api/domains-registrar/get-tld#query-parameters)
teamIdstringOptional
##  [Response](https://vercel.com/docs/rest-api/domains-registrar/get-tld#response)[](https://vercel.com/docs/rest-api/domains-registrar/get-tld#response)
200Success
supportedLanguageCodesobjectRequired
The language codes that are supported for the TLD. The key is the language code, and the value is the name of the language.
##  [Errors](https://vercel.com/docs/rest-api/domains-registrar/get-tld#errors)[](https://vercel.com/docs/rest-api/domains-registrar/get-tld#errors)
400There was something wrong with the request
statusnumberRequired
+Show 1 enum values
codestringRequired
+Show 1 enum values
messagestringRequired
401Unauthorized
statusnumberRequired
+Show 1 enum values
codestringRequired
+Show 1 enum values
messagestringRequired
403NotAuthorizedForScope
statusnumberRequired
+Show 1 enum values
codestringRequired
+Show 1 enum values
messagestringRequired
429TooManyRequests
statusnumberRequired
+Show 1 enum values
codestringRequired
+Show 1 enum values
messagestringRequired
retryAfterobjectRequired
+Show 2 properties
limitobjectRequired
+Show 3 properties
500InternalServerError
statusnumberRequired
+Show 1 enum values
codestringRequired
+Show 1 enum values
messagestringRequired
