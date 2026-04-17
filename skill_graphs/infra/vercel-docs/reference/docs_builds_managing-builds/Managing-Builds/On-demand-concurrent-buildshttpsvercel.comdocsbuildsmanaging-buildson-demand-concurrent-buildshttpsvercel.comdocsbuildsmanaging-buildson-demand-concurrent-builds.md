##  [On-demand concurrent builds](https://vercel.com/docs/builds/managing-builds#on-demand-concurrent-builds)[](https://vercel.com/docs/builds/managing-builds#on-demand-concurrent-builds)
On-demand concurrent builds is available on [Enterprise](https://vercel.com/docs/plans/enterprise) and [Pro](https://vercel.com/docs/plans/pro) plans
Those with the [owner](https://vercel.com/docs/rbac/access-roles#owner-role) role can access this feature
On-demand concurrent builds allow your builds to skip the queue and run immediately. By default, projects have on-demand concurrent builds enabled with full concurrency. Learn more about [concurrency modes](https://vercel.com/docs/builds/build-queues#with-on-demand-concurrent-builds).
You are charged for on-demand concurrent builds based on the number of concurrent builds required to allow the builds to proceed as explained in [usage and limits](https://vercel.com/docs/builds/managing-builds#usage-and-limits).
###  [Project-level on-demand concurrent builds](https://vercel.com/docs/builds/managing-builds#project-level-on-demand-concurrent-builds)[](https://vercel.com/docs/builds/managing-builds#project-level-on-demand-concurrent-builds)
When you enable on-demand build concurrency at the level of a project, any queued builds in that project will automatically be allowed to proceed. You can choose to [run all builds immediately or limit to one active build per branch](https://vercel.com/docs/builds/build-queues#with-on-demand-concurrent-builds).
You can configure this on the project's [Build and Deployment Settings](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fbuild-and-deployment&title=Go+to+Build+and+Deployment+Settings) page:
DashboardcURLSDK
  1. From your Vercel dashboard, select the project you wish to enable it for.
  2. Open Settings in the sidebar, and go to the Build and Deployment section of your [Project Settings](https://vercel.com/docs/projects/overview#project-settings).
  3. Under On-Demand Concurrent Builds, select one of the following:
     * Run all builds immediately: Skip the queue for all builds
     * Run up to one build per branch: Limit to one active build per branch
  4. The Turbo option is selected by default with 30 vCPUs and 60 GB of memory. You can switch to [Enhanced or Standard build machines](https://vercel.com/docs/builds/managing-builds#larger-build-machines) with fewer cores and memory.
  5. Click Save.


To create an Authorization Bearer token, see the [access token](https://vercel.com/docs/rest-api/reference/welcome#creating-an-access-token) section of the API documentation.
cURL
```
curl --request PATCH \
  --url https://api.vercel.com/v9/projects/YOUR_PROJECT_ID?teamId=YOUR_TEAM_ID \
  --header "Authorization: Bearer $VERCEL_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "resourceConfig": {
      "elasticConcurrencyEnabled": true,
      "buildQueue": {
        "configuration": "SKIP_NAMESPACE_QUEUE"
      }
    }
  }'
```

Set `configuration` to one of:
  * `SKIP_NAMESPACE_QUEUE`: Run all builds immediately
  * `WAIT_FOR_NAMESPACE_QUEUE`: Limit to one active build per branch


To create an Authorization Bearer token, see the [access token](https://vercel.com/docs/rest-api/reference/welcome#creating-an-access-token) section of the API documentation.
updateProject
```
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: '<YOUR_BEARER_TOKEN_HERE>',
});

async function run() {
  const result = await vercel.projects.updateProject({
    idOrName: 'YOUR_PROJECT_ID',
    teamId: 'YOUR_TEAM_ID',
    requestBody: {
      resourceConfig: {
        elasticConcurrencyEnabled: true,
        buildQueue: {
          configuration: 'SKIP_NAMESPACE_QUEUE',
        },
      },
    },
  });

  console.log(result);
}

run();
```

Set `configuration` to one of:
  * `SKIP_NAMESPACE_QUEUE`: Run all builds immediately
  * `WAIT_FOR_NAMESPACE_QUEUE`: Limit to one active build per branch


###  [Force an on-demand build](https://vercel.com/docs/builds/managing-builds#force-an-on-demand-build)[](https://vercel.com/docs/builds/managing-builds#force-an-on-demand-build)
For individual deployments, you can force build execution using the Start Building Now button. Regardless of the reason why this build was queued, it will proceed.
  1. Select your project from the [dashboard](https://vercel.com/dashboard).
  2. in the sidebar, open Deployments.
  3. Find the queued deployment that you would like to build from the list. You can use the Status filter to help find it. You have 2 options:
     * Select the three dots to the right of the deployment and select Start Building Now.
     * Click on the deployment list item to go to the deployment's detail page and click Start Building Now.
  4. Confirm that you would like to build this deployment in the Start Building Now dialog.
