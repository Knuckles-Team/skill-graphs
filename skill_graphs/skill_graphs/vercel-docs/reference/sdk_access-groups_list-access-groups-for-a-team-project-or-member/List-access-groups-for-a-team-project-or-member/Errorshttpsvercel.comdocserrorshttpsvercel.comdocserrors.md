##  [Errors](https://vercel.com/docs#errors)[](https://vercel.com/docs#errors)
400One of the provided values in the request query is invalid.
401The request is not authorized.
403You do not have permission to access this resource.
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

  const result = await vercel.accessGroups.listAccessGroups({






9

    projectId: "prj_pavWOn1iLObbx3RowVvzmPrTWyTf",






10

    search: "example",






11

    membersLimit: 20,






12

    projectsLimit: 20,






13

    limit: 20,






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
"value"



```

Copy as MarkdownGive feedbackAsk AI about this page
