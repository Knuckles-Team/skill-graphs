##  [Create a deployment with alias](https://vercel.com/docs#create-a-deployment-with-alias)[](https://vercel.com/docs#create-a-deployment-with-alias)
In this example, you will create a deployment, wait for it to complete, and then create an alias if successful.
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

async function createDeploymentAndAlias() {






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

    const deploymentId = createResponse.id;






24







25

    console.log(






26

      `Deployment created: ID ${deploymentId} and status ${createResponse.status}`,






27

    );






28







29

    // Check deployment status






30

    let deploymentStatus;






31

    let deploymentURL;






32

    do {






33

      await new Promise((resolve) => setTimeout(resolve, 5000)); // Wait 5 seconds between checks






34







35

      const statusResponse = await vercel.deployments.getDeployment({






36

        idOrUrl: deploymentId,






37

        withGitRepoInfo: 'true',






38

      });






39







40

      deploymentStatus = statusResponse.status;






41

      deploymentURL = statusResponse.url;






42

      console.log(`Deployment status: ${deploymentStatus}`);






43

    } while (






44

      deploymentStatus === 'BUILDING' ||






45

      deploymentStatus === 'INITIALIZING'






46

    );






47







48

    if (deploymentStatus === 'READY') {






49

      console.log(`Deployment successful. URL: ${deploymentURL}`);






50







51

      const aliasResponse = await vercel.aliases.assignAlias({






52

        id: deploymentId,






53

        requestBody: {






54

          alias: `my-project-alias.vercel.app`,






55

          redirect: null,






56

        },






57

      });






58







59

      console.log(`Alias created: ${aliasResponse.alias}`);






60

    } else {






61

      console.log('Deployment failed or was canceled');






62

    }






63

  } catch (error) {






64

    console.error(






65

      error instanceof Error ? `Error: ${error.message}` : String(error),






66

    );






67

  }






68

}






69







70

createDeploymentAndAlias();




```

On this page
  * [Create a deployment](https://vercel.com/docs#create-a-deployment)
  * [Create a deployment with alias](https://vercel.com/docs#create-a-deployment-with-alias)


Copy as MarkdownGive feedbackAsk AI about this page
