##  [Silence deployment notifications on pull requests](https://vercel.com/docs/builds#silence-deployment-notifications-on-pull-requests)[](https://vercel.com/docs/builds#silence-deployment-notifications-on-pull-requests)
By default, Vercel notifies GitHub of deployments using
Because Vercel also adds a comment to the pull request with a link to the deployment, unwanted noise can accumulate from the list of deployment notifications added to a pull request.
You can disable `deployment_status` events by:
  * [Going to the Git settings for your project](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fgit&title=Project+Git+settings)
  * Disabling the `deployment_status` Events toggle


Before doing this, ensure that you aren't depending on `deployment_status` events in your GitHub Actions workflows. If you are, we encourage [migrating to `repository_dispatch` events](https://vercel.com/docs/builds#migrating-from-deployment_status).
