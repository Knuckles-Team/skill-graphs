##  [Updating your project's rolling release configuration](https://vercel.com/docs#updating-your-project's-rolling-release-configuration)[](https://vercel.com/docs#updating-your-project's-rolling-release-configuration)
In this example, you configure rolling releases for your project with multiple stages. This allows you to gradually roll out deployments to production, starting with a small percentage of traffic and progressively increasing it.
run.ts
```


1

import { Vercel } from "@vercel/sdk";






2







3

const vercel = new Vercel({






4

  bearerToken: process.env.VERCEL_TOKEN,






5

});






6







7

async function setRollingReleaseConfig() {






8

  const result = await vercel.rollingRelease.updateRollingReleaseConfig({






9

    idOrName: "your-project-id",






10

    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






11

    slug: "my-team-url-slug",






12

    requestBody: {






13

      target: "production",






14

      stages: [






15

        {






16

          targetPercentage: 5,     // Start with 5% of traffic






17

          duration: 300           // Wait 5 minutes before next stage






18

        },






19

        {






20

          targetPercentage: 25,    // Then 25% of traffic






21

          duration: 600           // Wait 10 minutes






22

        },






23

        {






24

          targetPercentage: 50,    // Then 50% of traffic






25

          duration: 900           // Wait 15 minutes if approved






26

        },






27

        {






28

          targetPercentage: 100,   // Finally, 100% of traffic






29

        }






30

      ]






31

    }






32

  });






33







34

  console.log("Rolling Release Configuration Updated:", result.rollingRelease);






35

}






36







37

setRollingReleaseConfig();




```
