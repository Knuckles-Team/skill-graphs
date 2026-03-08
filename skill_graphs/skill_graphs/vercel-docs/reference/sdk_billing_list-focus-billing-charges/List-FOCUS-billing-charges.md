# List FOCUS billing charges
GET`https://api.vercel.com/v1/billing/charges`
Returns the billing charge data in FOCUS v1.3 JSONL format for a specified Vercel team, within a date range specified by `from` and `to` query parameters. Supports 1-day granularity with a maximum date range of 1 year. The response is streamed as newline-delimited JSON (JSONL) and can be optionally compressed with gzip if the `Accept-Encoding: gzip` header is provided. This is only available for Owner, Member, Developer, Security, Billing, and Enterprise Viewer roles for the supplied team.
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
