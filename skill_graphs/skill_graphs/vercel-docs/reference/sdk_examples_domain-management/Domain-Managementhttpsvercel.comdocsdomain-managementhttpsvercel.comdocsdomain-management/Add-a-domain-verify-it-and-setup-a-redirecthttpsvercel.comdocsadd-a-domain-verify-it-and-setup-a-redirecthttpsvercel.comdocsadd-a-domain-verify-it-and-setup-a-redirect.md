##  [Add a domain, verify it and setup a redirect](https://vercel.com/docs#add-a-domain-verify-it-and-setup-a-redirect)[](https://vercel.com/docs#add-a-domain-verify-it-and-setup-a-redirect)
In this example, you will add a custom domain, verify it, and set up a redirect from a subdomain to the main domain.
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

async function setupDomainWithRedirect() {






8

  const mainDomain = 'example.com';






9

  const subDomain = 'hello.example.com';






10

  const projectName = 'my-project'; //The project name used in the deployment URL






11







12

  try {






13

    // Add main domain






14

    const mainDomainResponse = await vercel.projects.addProjectDomain({






15

      idOrName: projectName,






16

      requestBody: {






17

        name: mainDomain,






18

      },






19

    });






20







21

    console.log(`Main domain added: ${mainDomainResponse.name}`);






22







23

    const checkConfiguration = await vercel.domains.getDomainConfig({






24

      domain: mainDomain,






25

    });






26







27

    if (mainDomainResponse.verified && !checkConfiguration.misconfigured) {






28

      // Add subdomain with 301 redirect to main domain






29

      const subDomainResponse = await vercel.projects.addProjectDomain({






30

        idOrName: projectName,






31

        requestBody: {






32

          name: subDomain,






33

          redirect: `https://${mainDomain}`,






34

          redirectStatusCode: 301,






35

        },






36

      });






37







38

      console.log(`Subdomain added and redirect set up: ${subDomain}`);






39

    }






40

  } catch (error) {






41

    console.error(






42

      error instanceof Error ? `Error: ${error.message}` : String(error),






43

    );






44

  }






45

}






46







47

setupDomainWithRedirect();




```

On this page
  * [Add a domain](https://vercel.com/docs#add-a-domain)
  * [Add a domain, verify it and setup a redirect](https://vercel.com/docs#add-a-domain-verify-it-and-setup-a-redirect)


Copy as MarkdownGive feedbackAsk AI about this page
