Menu
APIs & SDKs
[Vercel REST API](https://vercel.com/docs/rest-api)
Update an existing DNS record
# Update an existing DNS record
PATCH`https://api.vercel.com/v1/domains/records/{recordId}`
Updates an existing DNS record for a domain name.
TypeScriptNext.jscURL
https://api.vercel.com/v1/domains/records/{recordId}
```


1

const response = await fetch('https://api.vercel.com/v1/domains/records/recordId?teamId=string&slug=string', {






2

  method: 'PATCH',






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

    "name": "example-1",






9

    "value": "google.com",






10

    "type": "A",






11

    "ttl": "60",






12

    "mxPriority": "123",






13

    "srv": {






14

      "target": "example2.com.",






15

      "weight": "123",






16

      "port": "123",






17

      "priority": "123"






18

    },






19

    "https": {






20

      "priority": "123",






21

      "target": "example2.com.",






22

      "params": "string"






23

    },






24

    "comment": "used to verify ownership of domain"






25

  }),






26

});






27







28

const data = await response.json();






29

console.log(data);




```

Response
```


1

{






2

  "id": "icfg_1234567890",






3

  "name": "Example Name",






4

  "type": "record",






5

  "value": "string",






6

  "creator": "string",






7

  "domain": "string",






8

  "ttl": "123",






9

  "comment": "string",






10

  "recordType": "A",






11

  "createdAt": "123"






12

}




```

##  [Authentication](https://vercel.com/docs/rest-api/dns/update-an-existing-dns-record#authentication)[](https://vercel.com/docs/rest-api/dns/update-an-existing-dns-record#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/dns/update-an-existing-dns-record#path-parameters)[](https://vercel.com/docs/rest-api/dns/update-an-existing-dns-record#path-parameters)
recordIdstringRequired
The id of the DNS record
##  [Query parameters](https://vercel.com/docs/rest-api/dns/update-an-existing-dns-record#query-parameters)[](https://vercel.com/docs/rest-api/dns/update-an-existing-dns-record#query-parameters)
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Body](https://vercel.com/docs/rest-api/dns/update-an-existing-dns-record#body)[](https://vercel.com/docs/rest-api/dns/update-an-existing-dns-record#body)
application/json
namestringOptional
The name of the DNS record
valuestringOptional
The value of the DNS record
typestringOptional
The type of the DNS record
+Show 10 enum values
ttlintegerOptional
The Time to live (TTL) value of the DNS record
mxPriorityintegerOptional
The MX priority value of the DNS record
srvobjectOptional
+Show 4 properties
httpsobjectOptional
+Show 3 properties
commentstringOptional
A comment to add context on what this DNS record is for
##  [Response](https://vercel.com/docs/rest-api/dns/update-an-existing-dns-record#response)[](https://vercel.com/docs/rest-api/dns/update-an-existing-dns-record#response)
200Success
idstringRequired
namestringRequired
typestringRequired
+Show 2 enum values
valuestringRequired
creatorstringRequired
domainstringRequired
ttlnumberOptional
commentstringOptional
recordTypestringRequired
+Show 10 enum values
createdAtnumberOptional
##  [Errors](https://vercel.com/docs/rest-api/dns/update-an-existing-dns-record#errors)[](https://vercel.com/docs/rest-api/dns/update-an-existing-dns-record#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid.
401The request is not authorized.
402The account was soft-blocked for an unhandled reason. The account is missing a payment so payment method must be updated
403You do not have permission to access this resource.
404Error
409Error
