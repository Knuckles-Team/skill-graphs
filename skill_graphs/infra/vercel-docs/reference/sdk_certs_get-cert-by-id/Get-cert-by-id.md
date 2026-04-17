# Get cert by id
GET`https://api.vercel.com/v8/certs/{id}`
Get cert by id
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

  const result = await vercel.certs.getCertById({






9

    id: "<id>",






10

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






11

    slug: "my-team-url-slug",






12

  });






13







14

  console.log(result);






15

}






16







17

run();




```

Response
```


1

{






2

  "id": "icfg_1234567890",






3

  "createdAt": "123",






4

  "expiresAt": "123",






5

  "autoRenew": "false",






6

  "cns": []






7

}




```
