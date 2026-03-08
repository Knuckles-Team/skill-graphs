##  [Errors](https://vercel.com/docs#errors)[](https://vercel.com/docs#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404The alias was not found
TypeScriptNext.jscURL
https://api.vercel.com/v4/aliases/{idOrAlias}
```


1

const response = await fetch('https://api.vercel.com/v4/aliases/idOrAlias?from=123&projectId=string&since=123&until=123&teamId=string&slug=string', {






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

  "alias": "my-alias.vercel.app",






3

  "created": "2017-04-26T23:00:34.232Z",






4

  "createdAt": "1540095775941",






5

  "creator": {






6

    "uid": "96SnxkFiMyVKsK3pnoHfx3Hz",






7

    "email": "john-doe@gmail.com",






8

    "username": "john-doe"






9

  },






10

  "deletedAt": "1540095775941",






11

  "deployment": {






12

    "id": "dpl_5m8CQaRBm3FnWRW1od3wKTpaECPx",






13

    "url": "my-instant-deployment-3ij3cxz9qr.now.sh",






14

    "meta": "[object Object]"






15

  },






16

  "deploymentId": "dpl_5m8CQaRBm3FnWRW1od3wKTpaECPx",






17

  "projectId": "prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB",






18

  "redirect": "string",






19

  "redirectStatusCode": "301",






20

  "uid": "example_id",






21

  "updatedAt": "1540095775941",






22

  "protectionBypass": "value",






23

  "microfrontends": {






24

    "defaultApp": {






25

      "projectId": "example_id"






26

    },






27

    "applications": [






28

      {






29

        "fallbackHost": "string",






30

        "projectId": "example_id"






31

      }






32

    ]






33

  }






34

}




```

Copy as MarkdownGive feedbackAsk AI about this page
