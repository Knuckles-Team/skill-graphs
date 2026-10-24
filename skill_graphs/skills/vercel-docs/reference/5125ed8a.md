##  [Add variables to custom environments](https://vercel.com/docs#add-variables-to-custom-environments)[](https://vercel.com/docs#add-variables-to-custom-environments)
In this example, you will add environment variables to a custom environment in a project.
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

const projectName = 'my-project';






8

const customEnvironmentSlug = 'staging';






9







10

async function addEnvToCustomEnvironment() {






11

  try {






12

    // Get custom environments for the project






13

    const customEnvs = await vercel.environment.getV9ProjectsIdOrNameCustomEnvironments({






14

      idOrName: projectName,






15

    });






16







17

    console.log('Custom environments:', customEnvs);






18







19

    // Find the staging environment






20

    const stagingEnv = customEnvs.environments.find(






21

      (env) => env.slug === customEnvironmentSlug,






22

    );






23

    const stagingEnvId = stagingEnv?.id;






24







25

    console.log(`Staging environment ID: ${stagingEnvId || 'not found'}`);






26







27

    if (stagingEnvId) {






28

      // Create/upsert an environment variable for the custom environment






29

      const createEnvResult = await vercel.projects.createProjectEnv({






30

        idOrName: projectName,






31

        upsert: 'true',






32

        requestBody: {






33

          key: 'TEST_VAR',






34

          value: 'test-value',






35

          type: 'plain',






36

          customEnvironmentIds: [stagingEnvId],






37

          comment: 'Test variable created via SDK',






38

        },






39

      });






40







41

      console.log('Environment variable created:', createEnvResult);






42

    } else {






43

      console.log(






44

        'Staging environment not found, skipping environment variable creation',






45

      );






46

    }






47

  } catch (error) {






48

    console.error(






49

      error instanceof Error ? `Error: ${error.message}` : String(error),






50

    );






51

  }






52

}






53







54

addEnvToCustomEnvironment();




```

On this page
  * [Add environment variables to a project](https://vercel.com/docs#add-environment-variables-to-a-project)
  * [Manage variables across projects](https://vercel.com/docs#manage-variables-across-projects)
  * [Add variables to custom environments](https://vercel.com/docs#add-variables-to-custom-environments)


Copy as MarkdownGive feedbackAsk AI about this page
