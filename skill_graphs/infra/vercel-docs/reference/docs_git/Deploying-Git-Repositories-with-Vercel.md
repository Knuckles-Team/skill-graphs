# Deploying Git Repositories with Vercel
Last updated January 7, 2026
Vercel allows for automatic deployments on every branch push and merges onto the [production branch](https://vercel.com/docs/git#production-branch) of your [GitHub](https://vercel.com/docs/git/vercel-for-github), [GitLab](https://vercel.com/docs/git/vercel-for-gitlab), [Bitbucket](https://vercel.com/docs/git/vercel-for-bitbucket) and [Azure DevOps Pipelines](https://vercel.com/docs/git/vercel-for-azure-pipelines) projects.
Using Git with Vercel provides the following benefits:
  * [Preview deployments](https://vercel.com/docs/deployments/environments#preview-environment-pre-production#) for every push.
  * [Production deployments](https://vercel.com/docs/deployments/environments#production-environment) for the most recent changes from the [production branch](https://vercel.com/docs/git#production-branch).
  * Instant rollbacks when reverting changes assigned to a custom domain.


When working with Git, have a branch that works as your production branch, often called `main`. After you create a pull request (PR) to that branch, Vercel creates a unique deployment you can use to preview any changes. Once you are happy with the changes, you can merge your PR into the `main` branch, and Vercel will create a production deployment.
You can choose to use a different branch as the [production branch](https://vercel.com/docs/git#production-branch).
