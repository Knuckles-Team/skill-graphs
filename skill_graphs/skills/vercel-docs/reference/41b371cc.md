##  [Errors](https://vercel.com/docs#errors)[](https://vercel.com/docs#errors)
400One of the provided values in the request body is invalid. One of the provided values in the request query is invalid. The cert for the provided alias is not ready The deployment is not READY and can not be aliased The supplied alias is invalid
401The request is not authorized.
402The account was soft-blocked for an unhandled reason. The account is missing a payment so payment method must be updated
403You do not have permission to access this resource. If no .vercel.app alias exists then we fail (nothing to mirror)
404The domain used for the alias was not found The deployment was not found
409The provided alias is already assigned to the given deployment The domain is not allowed to be used
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

Copy as MarkdownGive feedbackAsk AI about this page
