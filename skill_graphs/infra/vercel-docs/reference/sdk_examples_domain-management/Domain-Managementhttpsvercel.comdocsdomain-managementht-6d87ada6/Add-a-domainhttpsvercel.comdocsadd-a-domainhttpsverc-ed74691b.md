##  [Add a domain](https://vercel.com/docs#add-a-domain)[](https://vercel.com/docs#add-a-domain)
In this example, you will add a new domain to a project and check its configuration.
run.ts
```


1

import { Vercel } from '@vercel/sdk';






2







3

const vercel = new Vercel({






4

  bearerToken: process.env.VERCEL_TOKEN,






5

});






6







7

async function addAndReviewDomain() {






8

  const domain = 'www.example.com';






9







10

  try {






11

    // Add a new domain






12

    const addDomainResponse = await vercel.projects.addProjectDomain({






13

      idOrName: 'my-project', //The project name used in the deployment URL






14

      requestBody: {






15

        name: domain,






16

      },






17

    });






18







19

    console.log(`Domain added: ${addDomainResponse.name}`);






20

    console.log('Domain Details:', JSON.stringify(addDomainResponse, null, 2));






21

  } catch (error) {






22

    console.error(






23

      error instanceof Error ? `Error: ${error.message}` : String(error),






24

    );






25

  }






26

}






27







28

addAndReviewDomain();




```
