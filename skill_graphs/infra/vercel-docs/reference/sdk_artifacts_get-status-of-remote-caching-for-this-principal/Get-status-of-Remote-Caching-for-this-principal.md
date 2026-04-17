# Get status of Remote Caching for this principal
GET`https://api.vercel.com/v8/artifacts/status`
Check the status of Remote Caching for this principal. Returns a JSON-encoded status indicating if Remote Caching is enabled, disabled, or disabled due to usage limits.
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

  const result = await vercel.artifacts.status({






9

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






10

    slug: "my-team-url-slug",






11

  });






12







13

  console.log(result);






14

}






15







16

run();




```

Response
```


1

{






2

  "status": "disabled"






3

}




```
