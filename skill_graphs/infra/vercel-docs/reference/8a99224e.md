# Stages new redirects for a project.
PUT`https://api.vercel.com/v1/bulk-redirects`
Stages new redirects for a project and returns the new version.
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

  const result = await vercel.bulkRedirects.stageRedirects({






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

  "alias": "string",






3

  "version": {






4

    "id": "icfg_1234567890",






5

    "key": "string",






6

    "lastModified": "123",






7

    "createdBy": "string",






8

    "name": "Example Name",






9

    "isStaging": "false",






10

    "isLive": "false",






11

    "redirectCount": "123",






12

    "alias": "string"






13

  }






14

}




```
