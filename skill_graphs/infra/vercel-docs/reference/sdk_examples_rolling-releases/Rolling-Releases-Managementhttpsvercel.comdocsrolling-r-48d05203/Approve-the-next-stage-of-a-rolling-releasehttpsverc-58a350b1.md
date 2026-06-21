##  [Approve the next stage of a rolling release](https://vercel.com/docs#approve-the-next-stage-of-a-rolling-release)[](https://vercel.com/docs#approve-the-next-stage-of-a-rolling-release)
In this example, you manually approve advancing a rolling release to the next stage. This is useful when you have stages configured with requireApproval: true and want to control the rollout progression.
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

async function approveNextStage() {






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

    if (!rollingRelease.nextStage) {






24

      console.log("Rolling release is already at the final stage");






25

      return;






26

    }






27







28

    if (!rollingRelease.nextStage.requireApproval) {






29

      console.log("Next stage does not require manual approval");






30

      return;






31

    }






32







33

    const approvalResult = await vercel.rollingRelease.approveRollingReleaseStage({






34

      idOrName: projectId,






35

      teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",






36

      requestBody: {






37

        nextStageIndex: rollingRelease.nextStage.index,






38

        canaryDeploymentId: rollingRelease.canaryDeployment?.id || "",






39

      },






40

    });






41







42

    console.log("Rolling release stage approved successfully!");






43

    console.log(`Advanced to stage ${approvalResult.rollingRelease?.activeStage?.index}`);






44

  } catch (error) {






45

    console.error("Failed to approve rolling release stage:", error);






46

  }






47

}






48







49

approveNextStage();




```
