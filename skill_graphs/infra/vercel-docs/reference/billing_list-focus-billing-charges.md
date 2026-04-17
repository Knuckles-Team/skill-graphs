Menu
APIs & SDKs
[Vercel REST API](https://vercel.com/docs/rest-api)
List FOCUS billing charges
# List FOCUS billing charges
GET`https://api.vercel.com/v1/billing/charges`
Returns the billing charge data in FOCUS v1.3 JSONL format for a specified Vercel team, within a date range specified by `from` and `to` query parameters. Supports 1-day granularity with a maximum date range of 1 year. The response is streamed as newline-delimited JSON (JSONL) and can be optionally compressed with gzip if the `Accept-Encoding: gzip` header is provided. This is only available for Owner, Member, Developer, Security, Billing, and Enterprise Viewer roles for the supplied team.
TypeScriptNext.jscURL
https://api.vercel.com/v1/billing/charges
```


1

const response = await fetch('https://api.vercel.com/v1/billing/charges?from=string&to=string&teamId=string&slug=string', {






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

{}




```

##  [Authentication](https://vercel.com/docs/rest-api/billing/list-focus-billing-charges#authentication)[](https://vercel.com/docs/rest-api/billing/list-focus-billing-charges#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Query parameters](https://vercel.com/docs/rest-api/billing/list-focus-billing-charges#query-parameters)[](https://vercel.com/docs/rest-api/billing/list-focus-billing-charges#query-parameters)
fromstringRequired
Inclusive start of the date range as an ISO 8601 date-time string in UTC.
tostringRequired
Exclusive end of the date range as an ISO 8601 date-time string in UTC.
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/billing/list-focus-billing-charges#response)[](https://vercel.com/docs/rest-api/billing/list-focus-billing-charges#response)
200Success
##  [Errors](https://vercel.com/docs/rest-api/billing/list-focus-billing-charges#errors)[](https://vercel.com/docs/rest-api/billing/list-focus-billing-charges#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
500Error
503Error
