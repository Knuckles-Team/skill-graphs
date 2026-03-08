##  [Manage variables across projects](https://vercel.com/docs#manage-variables-across-projects)[](https://vercel.com/docs#manage-variables-across-projects)
In this example, you manage environment variables across multiple projects and environments.
run.ts
```


1

import { Vercel } from '@vercel/sdk';






2

import { OneTarget } from '@vercel/sdk/models/operations/createprojectenv';






3







4

const PROJECTS = ['project-id-1', 'project-id-2', 'project-id-3'];






5

const environments = ['development', 'preview', 'production'];






6

const VERCEL_TOKEN = process.env.VERCEL_TOKEN;






7







8

const vercel = new Vercel({






9

  bearerToken: VERCEL_TOKEN,






10

});






11







12

async function manageEnvironmentVariables() {






13

  try {






14

    const variables = [






15

      { key: 'API_URL', value: 'https://api.example.com' },






16

      { key: 'DEBUG', value: 'true', environments: ['development', 'preview'] },






17

      {






18

        key: 'SECRET_KEY',






19

        value: 'super-secret-key',






20

        encrypt: true,






21

        environments: ['production', 'preview'],






22

      },






23

    ];






24







25

    for (const projectId of PROJECTS) {






26

      console.log(`Managing environment variables for project: ${projectId}`);






27

      for (const variable of variables) {






28

        const targets =






29

          (variable.environments as OneTarget[]) ||






30

          (environments as OneTarget[]);






31







32

        const addEnv = await vercel.projects.createProjectEnv({






33

          idOrName: projectId,






34

          upsert: 'true',






35

          requestBody: {






36

            key: variable.key,






37

            value: variable.value,






38

            target: targets,






39

            type: variable.encrypt ? 'encrypted' : 'plain',






40

          },






41

        });






42

        console.log(addEnv.created);






43

      }






44

      const readEnvs = await vercel.projects.filterProjectEnvs({






45

        idOrName: projectId,






46

      });






47

      console.log(






48

        'Env Details for ',






49

        projectId,






50

        ':',






51

        JSON.stringify(readEnvs, null, 2),






52

      );






53

    }






54

  } catch (error) {






55

    console.error('Error:', error.response?.data || error.message);






56

  }






57

}






58







59

manageEnvironmentVariables();




```
