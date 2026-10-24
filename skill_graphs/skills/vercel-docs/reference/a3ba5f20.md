# Assign an Alias
POST`https://api.vercel.com/v2/deployments/{id}/aliases`
Creates a new alias for the deployment with the given deployment ID. The authenticated user or team must own this deployment. If the desired alias is already assigned to another deployment, then it will be removed from the old deployment and assigned to the new one.
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

  const result = await vercel.aliases.assignAlias({






9

    id: "dpl_FjvFJncQHQcZMznrUm9EoB8sFuPa",






10

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






11

    slug: "my-team-url-slug",






12

    requestBody: {






13

      alias: "my-alias.vercel.app",






14

      redirect: null,






15

    },






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

  "uid": "2WjyKQmM8ZnGcJsPWMrHRHrE",






3

  "alias": "my-alias.vercel.app",






4

  "created": "2017-04-26T23:00:34.232Z",






5

  "oldDeploymentId": "dpl_FjvFJncQHQcZMznrUm9EoB8sFuPa"






6

}




```
