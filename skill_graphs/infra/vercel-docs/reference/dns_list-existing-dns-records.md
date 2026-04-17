Menu
APIs & SDKs
[Vercel REST API](https://vercel.com/docs/rest-api)
List existing DNS records
# List existing DNS records
GET`https://api.vercel.com/v4/domains/{domain}/records`
Retrieves a list of DNS records created for a domain name. By default it returns 20 records if no limit is provided. The rest can be retrieved using the pagination options.
TypeScriptNext.jscURL
https://api.vercel.com/v4/domains/{domain}/records
```


1

const response = await fetch('https://api.vercel.com/v4/domains/domain/records?limit=string&since=string&until=string&teamId=string&slug=string', {






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
"string"



```

##  [Authentication](https://vercel.com/docs/rest-api/dns/list-existing-dns-records#authentication)[](https://vercel.com/docs/rest-api/dns/list-existing-dns-records#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/dns/list-existing-dns-records#path-parameters)[](https://vercel.com/docs/rest-api/dns/list-existing-dns-records#path-parameters)
domainstringRequired
##  [Query parameters](https://vercel.com/docs/rest-api/dns/list-existing-dns-records#query-parameters)[](https://vercel.com/docs/rest-api/dns/list-existing-dns-records#query-parameters)
limitstringOptional
Maximum number of records to list from a request.
sincestringOptional
Get records created after this JavaScript timestamp.
untilstringOptional
Get records created before this JavaScript timestamp.
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/dns/list-existing-dns-records#response)[](https://vercel.com/docs/rest-api/dns/list-existing-dns-records#response)
200Successful response retrieving a list of paginated DNS records.
##  [Errors](https://vercel.com/docs/rest-api/dns/list-existing-dns-records#errors)[](https://vercel.com/docs/rest-api/dns/list-existing-dns-records#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
