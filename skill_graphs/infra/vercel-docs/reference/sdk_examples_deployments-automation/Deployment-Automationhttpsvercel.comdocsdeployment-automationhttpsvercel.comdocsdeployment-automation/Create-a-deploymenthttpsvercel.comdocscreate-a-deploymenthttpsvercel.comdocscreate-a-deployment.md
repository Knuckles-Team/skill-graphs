##  [Create a deployment](https://vercel.com/docs#create-a-deployment)[](https://vercel.com/docs#create-a-deployment)
In this example, you will trigger a new deployment from a GitHub repository and then retrieve its status.
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

async function createAndCheckDeployment() {






8

  try {






9

    // Create a new deployment






10

    const createResponse = await vercel.deployments.createDeployment({






11

      requestBody: {






12

        name: 'my-project', //The project name used in the deployment URL






13

        target: 'production',






14

        gitSource: {






15

          type: 'github',






16

          repo: 'repo-name',






17

          ref: 'main',






18

          org: 'org-name', //For a personal account, the org-name is your GH username






19

        },






20

      },






21

    });






22







23

    console.log(






24

      `Deployment created: ID ${createResponse.id} and status ${createResponse.status}`,






25

    );






26

  } catch (error) {






27

    console.error(






28

      error instanceof Error ? `Error: ${error.message}` : String(error),






29

    );






30

  }






31

}






32







33

createAndCheckDeployment();




```
