##  [Add environment variables to a project](https://vercel.com/docs#add-environment-variables-to-a-project)[](https://vercel.com/docs#add-environment-variables-to-a-project)
In this example, you will add new environment variables to a project and list the details of the added values.
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

const projectName = 'my-project'; //The project name used in the deployment URL






7







8

async function addAndListEnvVars() {






9

  try {






10

    // Add new environment variables






11

    const addResponse = await vercel.projects.createProjectEnv({






12

      idOrName: projectName,






13

      upsert: 'true',






14

      requestBody: [






15

        {






16

          key: 'API_KEY',






17

          value: 'secret_value',






18

          target: ['production', 'preview'],






19

          type: 'encrypted',






20

        },






21

        {






22

          key: 'DEBUG',






23

          value: 'true',






24

          target: ['development'],






25

          type: 'plain',






26

        },






27

      ],






28

    });






29

    console.log(






30

      'Added environment variables:',






31

      JSON.stringify(addResponse, null, 2),






32

    );






33

  } catch (error) {






34

    console.error(






35

      error instanceof Error ? `Error: ${error.message}` : String(error),






36

    );






37

  }






38

}






39







40

addAndListEnvVars();




```
