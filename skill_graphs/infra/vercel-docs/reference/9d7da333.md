##  [Deploying a Git repository](https://vercel.com/docs/git#deploying-a-git-repository)[](https://vercel.com/docs/git#deploying-a-git-repository)
Setting up your GitHub, GitLab, or Bitbucket repository on Vercel is only a matter of clicking the ["New Project"](https://vercel.com/new) button on the top right of your dashboard and following the steps.
For Azure DevOps repositories, use the [Vercel Deployment Extension](https://vercel.com/docs/git/vercel-for-azure-pipelines)
After clicking it, you'll be presented with a list of Git repositories that the Git account you've signed up with has write access to.
To select a different Git namespace or provider, you can use the dropdown list on the top left of the section.
![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fgit%2Findex%2Frepo-list-light.png&w=1200&q=75)![](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fgit%2Findex%2Frepo-list-dark.png&w=1200&q=75)
A list of Git repositories your Git account has access to.
You can also:
  * Select a third-party Git repository by clicking on [Import Third-Party Git Repository](https://vercel.com/new/git/third-party) on the bottom of the section.
  * Select a pre-built solution from the section on the right.


After you've selected the Git repository or template you want to use for your new project, you'll be taken to a page where you can configure your project before it's deployed.
You can:
  * Customize the project's name
  * Select [a Framework Preset](https://vercel.com/docs/deployments/configure-a-build#framework-preset)
  * Select the root directory of your project
  * Configure [Build Output Settings](https://vercel.com/docs/deployments/configure-a-build#build-command)
  * Set [Environment Variables](https://vercel.com/docs/environment-variables)


When your settings are correct, you can select the Deploy button to initiate a deployment.
###  [Creating a deployment from a Git reference](https://vercel.com/docs/git#creating-a-deployment-from-a-git-reference)[](https://vercel.com/docs/git#creating-a-deployment-from-a-git-reference)
You can initiate new deployments directly from the Vercel Dashboard using a Git reference. This approach is ideal when automatic deployments are interrupted or unavailable.
To create a deployment from a Git reference:
  1. From your [dashboard](https://vercel.com/dashboard), select the project you'd like to create a deployment for
  2. Open Deployments in the sidebar. Once on the Deployments page, select the Create Deployment button
  3. Depending on how you would like to deploy, enter the following:
     * Targeted Deployments: Provide the unique ID (SHA) of a commit to build a deployment based on that specific commit
     * Branch-Based Deployments: Provide the full name of a branch when you want to build the most recent changes from that specific branch (for example, `https://github.com/vercel/examples/tree/deploy`)
  4. Select Create Deployment. Vercel will build and deploy your commit or branch as usual


When the same commit appears in multiple branches, Vercel will prompt you to choose the appropriate branch configuration. This choice is crucial as it affects settings like environment variables linked to each branch.
