##  [Errors](https://vercel.com/docs#errors)[](https://vercel.com/docs#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404The alias was not found
Request
```


1

import { Vercel } from "@vercel/sdk";






2







3

const vercel = new Vercel({






4

  bearerToken: "<YOUR_BEARER_TOKEN_HERE>",






5

});






6







7

async function run() {






8

  const result = await vercel.aliases.getAlias({






9

    from: 1540095775951,






10

    idOrAlias: "example.vercel.app",






11

    projectId: "prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB",






12

    since: 1540095775941,






13

    until: 1540095775951,






14

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






15

    slug: "my-team-url-slug",






16

  });






17







18

  console.log(result);






19

}






20







21

run();




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
