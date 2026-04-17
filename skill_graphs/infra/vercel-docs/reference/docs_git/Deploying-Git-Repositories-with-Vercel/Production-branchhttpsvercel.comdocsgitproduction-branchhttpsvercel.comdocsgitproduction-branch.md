##  [Production branch](https://vercel.com/docs/git#production-branch)[](https://vercel.com/docs/git#production-branch)
A [Production deployment](https://vercel.com/docs/deployments/environments#production-environment) will be created each time you merge to the production branch.
###  [Default configuration](https://vercel.com/docs/git#default-configuration)[](https://vercel.com/docs/git#default-configuration)
When you create a new Project from a Git repository on Vercel, the Production Branch will be selected in the following order:
  * The `main` branch.
  * If not present, the `master` branch ([more details](https://vercel.com/blog/custom-production-branch#a-note-on-the-master-branch)).
  * [Only for Bitbucket]: If not present, the "production branch" setting of your Git repository is used.
  * If not present, the Git repository's default branch.


###  [Customizing the production branch](https://vercel.com/docs/git#customizing-the-production-branch)[](https://vercel.com/docs/git#customizing-the-production-branch)
On the Environments page in the Project Settings, you can change your production branch:
  * Click on the Production environment and go to Branch Tracking
  * Change the name of the branch and click Save


Whenever a new commit is then pushed to the branch you configured here, a [production deployment](https://vercel.com/docs/deployments/environments#production-environment) will be created for you.
