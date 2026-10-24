##  [Errors](https://vercel.com/docs#errors)[](https://vercel.com/docs#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
404Error
500Error
503Error
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

  const result = await vercel.billing.listBillingCharges({






9

    from: "2025-01-01T00:00:00.000Z",






10

    to: "2025-01-31T00:00:00.000Z",






11

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






12

    slug: "my-team-url-slug",






13

  });






14







15

  for await (const event of result) {






16

    // Handle the event






17

    console.log(event);






18

  }






19

}






20







21

run();




```

Response
```


1

{}




```

Copy as MarkdownGive feedbackAsk AI about this page
