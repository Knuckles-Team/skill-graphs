##  [Force completion of a rolling release](https://vercel.com/docs#force-completion-of-a-rolling-release)[](https://vercel.com/docs#force-completion-of-a-rolling-release)
In this example, you force-complete an active rolling release, immediately promoting the canary deployment to serve 100% of traffic. This is useful for emergency situations or when you want to skip remaining stages.
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

async function forceCompleteRollingRelease() {






8

  const projectId = "your-project-id";






9







10

  try {






11

    const currentStatus = await vercel.rollingRelease.getActiveRollingRelease({






12

      idOrName: projectId,






13

      teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






14

    });






15







16

    if (!currentStatus.rollingRelease || currentStatus.rollingRelease.state !== "ACTIVE") {






17

      console.log("No active rolling release found for this project");






18

      return;






19

    }






20







21

    const { rollingRelease } = currentStatus;






22







23

    if (!rollingRelease.canaryDeployment?.id) {






24

      console.error("No canary deployment found to complete");






25

      return;






26

    }






27







28

    const completionResult = await vercel.rollingRelease.completeRollingRelease({






29

      idOrName: projectId,






30

      teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






31

      requestBody: {






32

        canaryDeploymentId: rollingRelease.canaryDeployment.id,






33

      },






34

    });






35







36

    console.log("Rolling release completed successfully!");






37

    console.log(`Final state: ${completionResult.rollingRelease?.state}`);






38

  } catch (error) {






39

    console.error("Failed to complete rolling release:", error);






40

  }






41

}






42







43

forceCompleteRollingRelease();




```

On this page
  * [Updating your project's rolling release configuration](https://vercel.com/docs#updating-your-project's-rolling-release-configuration)
  * [Approve the next stage of a rolling release](https://vercel.com/docs#approve-the-next-stage-of-a-rolling-release)
  * [Force completion of a rolling release](https://vercel.com/docs#force-completion-of-a-rolling-release)


Copy as MarkdownGive feedbackAsk AI about this page
