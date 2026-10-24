##  [Errors](https://vercel.com/docs#errors)[](https://vercel.com/docs#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
TypeScriptNext.jscURL
https://api.vercel.com/v1/connect/networks
```


1

const response = await fetch('https://api.vercel.com/v1/connect/networks?includeHostedZones=true&includePeeringConnections=true&includeProjects=true&search=string&teamId=string&slug=string', {






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

    "awsAccountId": "example_id",






4

    "awsAvailabilityZoneIds": [],






5

    "awsRegion": "string",






6

    "cidr": "example_id",






7

    "createdAt": "123",






8

    "egressIpAddresses": [],






9

    "hostedZones": {






10

      "count": "123"






11

    },






12

    "id": "icfg_1234567890",






13

    "name": "Example Name",






14

    "peeringConnections": {






15

      "count": "123"






16

    },






17

    "projects": {






18

      "count": "123",






19

      "ids": []






20

    },






21

    "region": "string",






22

    "status": "create_in_progress",






23

    "teamId": "example_id",






24

    "vpcId": "example_id"






25

  }






26

]




```

Copy as MarkdownGive feedbackAsk AI about this page
