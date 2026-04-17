##  [Errors](https://vercel.com/docs#errors)[](https://vercel.com/docs#errors)
400One of the provided values in the request body is invalid. One of the provided values in the headers is invalid
401The request is not authorized.
402The account was soft-blocked for an unhandled reason. The account is missing a payment so payment method must be updated
403The customer has reached their spend cap limit and has been paused. An owner can disable the cap or raise the limit in settings. The Remote Caching usage limit has been reached for this account for this billing cycle. Remote Caching has been disabled for this team or user. An owner can enable it in the billing settings. You do not have permission to access this resource.
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

  await vercel.artifacts.recordEvents({






9

    xArtifactClientCi: "VERCEL",






10

    xArtifactClientInteractive: 0,






11

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






12

    slug: "my-team-url-slug",






13

    requestBody: [






14

      {






15

        sessionId: "<id>",






16

        source: "REMOTE",






17

        event: "MISS",






18

        hash: "12HKQaOmR5t5Uy6vdcQsNIiZgHGB",






19

        duration: 400,






20

      },






21

    ],






22

  });






23







24







25

}






26







27

run();




```

Response
```


1

{}




```

Copy as MarkdownGive feedbackAsk AI about this page
