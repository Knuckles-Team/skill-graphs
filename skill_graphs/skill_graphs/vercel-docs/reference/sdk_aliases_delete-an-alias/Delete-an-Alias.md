# Delete an Alias
DEL`https://api.vercel.com/v2/aliases/{aliasId}`
Delete an Alias with the specified ID.
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

  const result = await vercel.aliases.deleteAlias({






9

    aliasId: "2WjyKQmM8ZnGcJsPWMrHRHrE",






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

  "status": "SUCCESS"






3

}




```
