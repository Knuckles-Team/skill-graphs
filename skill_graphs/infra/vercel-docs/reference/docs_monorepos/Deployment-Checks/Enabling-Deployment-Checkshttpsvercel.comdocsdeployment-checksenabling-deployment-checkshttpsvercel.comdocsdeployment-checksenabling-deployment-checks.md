##  [Enabling Deployment Checks](https://vercel.com/docs/deployment-checks#enabling-deployment-checks)[](https://vercel.com/docs/deployment-checks#enabling-deployment-checks)
  1. ###  [Ensure prerequisites are enabled](https://vercel.com/docs/deployment-checks#ensure-prerequisites-are-enabled)[](https://vercel.com/docs/deployment-checks#ensure-prerequisites-are-enabled)
    1. Link your project to a Github repository using [Vercel for GitHub](https://vercel.com/docs/git/vercel-for-github). This can be verified by navigating to your [projects settings](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fgit).
    2. Visit [your project's production environment settings](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fenvironments%2Fproduction) and ensure automatic aliasing for production is turned on.
  2. ###  [Select your Deployment Checks](https://vercel.com/docs/deployment-checks#select-your-deployment-checks)[](https://vercel.com/docs/deployment-checks#select-your-deployment-checks)
Visit [your project's settings](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fdeployment-checks), and select _Add Checks_ to select required Deployment Checks.
  3. ###  [Update workflows (if necessary)](https://vercel.com/docs/deployment-checks#update-workflows-if-necessary)[](https://vercel.com/docs/deployment-checks#update-workflows-if-necessary)
If using GitHub Actions with a
```
- name: 'Notify Vercel'
  uses: 'vercel/repository-dispatch/actions/status@v1'
  with:
    # The name of the check will be used to identify the check in the Deployment Checks settings and must be unique
    name: "Vercel - my-project: e2e-tests"
```

If you are not using
  4. ###  [Create a new production deployment](https://vercel.com/docs/deployment-checks#create-a-new-production-deployment)[](https://vercel.com/docs/deployment-checks#create-a-new-production-deployment)
Deployment Checks appear as part of a production deployment's lifecycle. Production deployments will still be created, but will not be automatically assigned to your custom domains until all Deployment Checks are met.
  5. ###  [Run GitHub Actions to fulfill all Deployment Checks](https://vercel.com/docs/deployment-checks#run-github-actions-to-fulfill-all-deployment-checks)[](https://vercel.com/docs/deployment-checks#run-github-actions-to-fulfill-all-deployment-checks)
To meet Deployment Checks, run their corresponding GitHub Actions.
If you're using [`vercel.deployment.ready` event](https://vercel.com/docs/git/vercel-for-github#repository-dispatch-events). This event triggers after the deployment is created, and before checks are run.
  6. ###  [Promote to production once all Deployment Checks are met](https://vercel.com/docs/deployment-checks#promote-to-production-once-all-deployment-checks-are-met)[](https://vercel.com/docs/deployment-checks#promote-to-production-once-all-deployment-checks-are-met)
Once all of the Deployment Checks have passed, the deployment is aliased to your production domain(s) automatically.
For additional release protection, enable [Rolling Releases](https://vercel.com/docs/rolling-releases) to ensure your deployment is fractionally released before promoting to everyone.
