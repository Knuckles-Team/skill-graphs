# Reads an access group
GET`https://api.vercel.com/v1/access-groups/{idOrName}`
Allows to read an access group
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

  const result = await vercel.accessGroups.readAccessGroup({






9

    idOrName: "ag_1a2b3c4d5e6f7g8h9i0j",






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

  "teamPermissions": [],






3

  "entitlements": [],






4

  "isDsyncManaged": "false",






5

  "name": "my-access-group",






6

  "createdAt": "1588720733602",






7

  "teamId": "team_123a6c5209bc3778245d011443644c8d27dc2c50",






8

  "updatedAt": "1588720733602",






9

  "accessGroupId": "ag_123a6c5209bc3778245d011443644c8d27dc2c50",






10

  "membersCount": "5",






11

  "projectsCount": "2",






12

  "teamRoles": []






13

}




```
