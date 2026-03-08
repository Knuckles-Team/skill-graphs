##  [Prioritize production builds](https://vercel.com/docs/builds/managing-builds#prioritize-production-builds)[](https://vercel.com/docs/builds/managing-builds#prioritize-production-builds)
Prioritize production builds is available on [all plans](https://vercel.com/docs/plans)
If a build has to wait for queued preview deployments to finish, it can delay the production release process. When Vercel queues builds, we'll processes them in chronological order (FIFO Order).
For any new projects created after December 12, 2024, Vercel will prioritize production builds by default.
To ensure that changes to the [production environment](https://vercel.com/docs/deployments/environments#production-environment) are prioritized over [preview deployments](https://vercel.com/docs/deployments/environments#preview-environment-pre-production) in the queue, you can enable Prioritize Production Builds:
  1. From your Vercel dashboard, select the project you wish to enable it for
  2. Open Settings in the sidebar, and go to the [Build and Deployment section](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fbuild-and-deployment&title=Prioritize+Production+Builds+Setting) of your [Project Settings](https://vercel.com/docs/projects/overview#project-settings)
  3. Under Prioritize Production Builds, toggle the switch to Enabled
