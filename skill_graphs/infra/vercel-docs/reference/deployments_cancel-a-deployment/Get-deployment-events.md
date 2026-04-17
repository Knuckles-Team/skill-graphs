# Get deployment events
GET`https://api.vercel.com/v3/deployments/{idOrUrl}/events`
Get the build logs of a deployment by deployment ID and build ID. It can work as an infinite stream of logs or as a JSON endpoint depending on the input parameters.
TypeScriptNext.jscURL
https://api.vercel.com/v3/deployments/{idOrUrl}/events
```


1

const response = await fetch('https://api.vercel.com/v3/deployments/idOrUrl/events?direction=string&follow=123&limit=123&name=string&since=123&until=123&statusCode=value&delimiter=123&builds=123&teamId=string&slug=string', {






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

[






2

  {






3

    "type": "delimiter",






4

    "created": "123",






5

    "payload": {






6

      "deploymentId": "example_id",






7

      "info": {






8

        "type": "string",






9

        "name": "Example Name",






10

        "entrypoint": "string",






11

        "path": "string",






12

        "step": "string",






13

        "readyState": "string"






14

      },






15

      "text": "string",






16

      "id": "icfg_1234567890",






17

      "date": "123",






18

      "serial": "string",






19

      "created": "123",






20

      "statusCode": "123",






21

      "requestId": "example_id",






22

      "proxy": {






23

        "timestamp": "123",






24

        "method": "string",






25

        "host": "string",






26

        "path": "string",






27

        "statusCode": "123",






28

        "userAgent": [],






29

        "referer": "string",






30

        "clientIp": "string",






31

        "region": "string",






32

        "scheme": "string",






33

        "responseByteSize": "123",






34

        "cacheId": "example_id",






35

        "pathType": "string",






36

        "pathTypeVariant": "string",






37

        "vercelId": "example_id",






38

        "vercelCache": "MISS",






39

        "lambdaRegion": "string",






40

        "wafAction": "log",






41

        "wafRuleId": "example_id"






42

      }






43

    }






44

  }






45

]




```

##  [Authentication](https://vercel.com/docs/rest-api/deployments/get-deployment-events#authentication)[](https://vercel.com/docs/rest-api/deployments/get-deployment-events#authentication)
AuthorizationbearerToken
Default authentication mechanism
##  [Path parameters](https://vercel.com/docs/rest-api/deployments/get-deployment-events#path-parameters)[](https://vercel.com/docs/rest-api/deployments/get-deployment-events#path-parameters)
idOrUrlstringRequired
The unique identifier or hostname of the deployment.
##  [Query parameters](https://vercel.com/docs/rest-api/deployments/get-deployment-events#query-parameters)[](https://vercel.com/docs/rest-api/deployments/get-deployment-events#query-parameters)
directionstringOptional
Order of the returned events based on the timestamp.
+Show 2 enum values
follownumberOptional
When enabled, this endpoint will return live events as they happen.
+Show 2 enum values
limitnumberOptional
Maximum number of events to return. Provide `-1` to return all available logs.
namestringOptional
Deployment build ID.
sincenumberOptional
Timestamp for when build logs should be pulled from.
untilnumberOptional
Timestamp for when the build logs should be pulled up until.
statusCodeanyOptional
HTTP status code range to filter events by.
delimiternumberOptional
+Show 2 enum values
buildsnumberOptional
+Show 2 enum values
teamIdstringOptional
The Team identifier to perform the request on behalf of.
slugstringOptional
The Team slug to perform the request on behalf of.
##  [Response](https://vercel.com/docs/rest-api/deployments/get-deployment-events#response)[](https://vercel.com/docs/rest-api/deployments/get-deployment-events#response)
200Success
##  [Errors](https://vercel.com/docs/rest-api/deployments/get-deployment-events#errors)[](https://vercel.com/docs/rest-api/deployments/get-deployment-events#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
500Error
TypeScriptNext.jscURL
https://api.vercel.com/v3/deployments/{idOrUrl}/events
```


1

const response = await fetch('https://api.vercel.com/v3/deployments/idOrUrl/events?direction=string&follow=123&limit=123&name=string&since=123&until=123&statusCode=value&delimiter=123&builds=123&teamId=string&slug=string', {






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

[






2

  {






3

    "type": "delimiter",






4

    "created": "123",






5

    "payload": {






6

      "deploymentId": "example_id",






7

      "info": {






8

        "type": "string",






9

        "name": "Example Name",






10

        "entrypoint": "string",






11

        "path": "string",






12

        "step": "string",






13

        "readyState": "string"






14

      },






15

      "text": "string",






16

      "id": "icfg_1234567890",






17

      "date": "123",






18

      "serial": "string",






19

      "created": "123",






20

      "statusCode": "123",






21

      "requestId": "example_id",






22

      "proxy": {






23

        "timestamp": "123",






24

        "method": "string",






25

        "host": "string",






26

        "path": "string",






27

        "statusCode": "123",






28

        "userAgent": [],






29

        "referer": "string",






30

        "clientIp": "string",






31

        "region": "string",






32

        "scheme": "string",






33

        "responseByteSize": "123",






34

        "cacheId": "example_id",






35

        "pathType": "string",






36

        "pathTypeVariant": "string",






37

        "vercelId": "example_id",






38

        "vercelCache": "MISS",






39

        "lambdaRegion": "string",






40

        "wafAction": "log",






41

        "wafRuleId": "example_id"






42

      }






43

    }






44

  }






45

]




```

Copy as MarkdownGive feedbackAsk AI about this page
APIs & SDKs
[Vercel REST API](https://vercel.com/docs/rest-api)
Cancel a deployment
