##  [Staging and promoting a production deployment](https://vercel.com/docs/deploy-hooks#staging-and-promoting-a-production-deployment)[](https://vercel.com/docs/deploy-hooks#staging-and-promoting-a-production-deployment)
In some cases you may want to create a production-like deployment to use as a staging environment before promoting it to production.
In this scenario, you can turn off the auto-assignment of domains for your production build, as described below. Turning off the auto-assignment of domains means the deployment won't automatically be served to your production traffic, but also means you must manually promote it to production.
###  [CLI](https://vercel.com/docs/deploy-hooks#cli)[](https://vercel.com/docs/deploy-hooks#cli)
For steps on using this workflow in the CLI, see [Deploying a staged production build](https://vercel.com/docs/cli/deploying-from-cli#deploying-a-staged-production-build).
###  [Dashboard](https://vercel.com/docs/deploy-hooks#dashboard)[](https://vercel.com/docs/deploy-hooks#dashboard)
  1. On your [dashboard](https://vercel.com/dashboard), select your project
  2. Open [Settings](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fenvironments&title=Go+to+Environments) in the sidebar and go to your Environments settings
  3. Click on Production and go to the Branch Tracking section
  4. Disable the Auto-assign Custom Production Domains toggle
  5. When you are ready to promote this staged deployment to production, select the ellipses (…) next to the deployment
  6. From the menu, select the Promote option
  7. From the Promote dialog, confirm the deployment, and select the Promote button:

![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpromote-to-prod-light.png&w=1080&q=75)![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpromote-to-prod-dark.png&w=1080&q=75)
Vercel will instantly promote the deployment; it doesn't require a rebuild. Once promoted, the deployment is marked as [Current](https://vercel.com/docs/deploy-hooks#production-deployment-state).
