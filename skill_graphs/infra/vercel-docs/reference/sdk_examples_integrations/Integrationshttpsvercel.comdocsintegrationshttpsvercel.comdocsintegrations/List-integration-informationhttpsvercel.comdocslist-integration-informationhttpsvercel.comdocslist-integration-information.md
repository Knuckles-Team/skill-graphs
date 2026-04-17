##  [List integration information](https://vercel.com/docs#list-integration-information)[](https://vercel.com/docs#list-integration-information)
In this example, you list the available integrations in your account.
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

async function listAccountIntegrations() {






8

  try {






9

    const integrationsResponse = await vercel.integrations.getConfigurations({






10

      view: 'account',






11

    });






12







13

    integrationsResponse.forEach((config) => {






14

      console.log(






15

        `- ${config.slug}: ${






16

          config.installationType ? `${config.installationType}` : ``






17

        }integration installed in ${config.projects?.join(' ')}`,






18

      );






19

    });






20

  } catch (error) {






21

    console.error(






22

      error instanceof Error ? `Error: ${error.message}` : String(error),






23

    );






24

  }






25

}






26







27

listAccountIntegrations();




```

On this page
  * [List integration information](https://vercel.com/docs#list-integration-information)


Copy as MarkdownGive feedbackAsk AI about this page
