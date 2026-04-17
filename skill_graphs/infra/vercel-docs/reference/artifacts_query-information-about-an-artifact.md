Menu
APIs & SDKs
[Vercel REST API](https://vercel.com/docs/rest-api)
Query information about an artifact
# Query information about an artifact
POST`https://api.vercel.com/v8/artifacts`
Query information about an array of artifacts.
TypeScriptNext.jscURL
https://api.vercel.com/v8/artifacts
```


1

const response = await fetch('https://api.vercel.com/v8/artifacts?teamId=string&slug=string', {






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

    "hashes": []






9

  }),






10

});






11







12

const data = await response.json();






13

console.log(data);




```

Response
```


1
"value"



```

##  [Authentication](https://vercel.com/docs/rest-api/artifacts/query-information-about-an-artifact#authentication)[](https://vercel.com/docs/rest-api/artifacts/query-information-about-an-artifact#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Query parameters](https://vercel.com/docs/rest-api/artifacts/query-information-about-an-artifact#query-parameters)[](https://vercel.com/docs/rest-api/artifacts/query-information-about-an-artifact#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Body](https://vercel.com/docs/rest-api/artifacts/query-information-about-an-artifact#body)[](https://vercel.com/docs/rest-api/artifacts/query-information-about-an-artifact#body)
application/json
hashesarrayRequired
artifact hashes
##  [Response](https://vercel.com/docs/rest-api/artifacts/query-information-about-an-artifact#response)[](https://vercel.com/docs/rest-api/artifacts/query-information-about-an-artifact#response)
200Success
##  [Errors](https://vercel.com/docs/rest-api/artifacts/query-information-about-an-artifact#errors)[](https://vercel.com/docs/rest-api/artifacts/query-information-about-an-artifact#errors)
400One of the provided values in the request body is invalid.
401The request is not authorized.
402The account was soft-blocked for an unhandled reason. The account is missing a payment so payment method must be updated
403The customer has reached their spend cap limit and has been paused. An owner can disable the cap or raise the limit in settings. The Remote Caching usage limit has been reached for this account for this billing cycle. Remote Caching has been disabled for this team or user. An owner can enable it in the billing settings. You do not have permission to access this resource.
