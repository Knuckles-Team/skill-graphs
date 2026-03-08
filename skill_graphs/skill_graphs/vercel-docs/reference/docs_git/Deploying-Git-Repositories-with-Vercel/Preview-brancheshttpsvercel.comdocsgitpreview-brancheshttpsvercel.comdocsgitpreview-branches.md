##  [Preview branches](https://vercel.com/docs/git#preview-branches)[](https://vercel.com/docs/git#preview-branches)
While the [production branch](https://vercel.com/docs/git#production-branch) is a single Git branch that contains the code that is served to your visitors, all other branches are deployed as pre-production branches (either preview branches, or if you have configured them, custom environments branches).
For example, if your production branch is `main`, then [by default](https://vercel.com/docs/git#using-custom-environments) all the Git branches that are not `main` are considered preview branches. That means there can be many preview branches, but only a single production branch.
To learn more about previews, see the [Preview Deployments](https://vercel.com/docs/deployments/environments#preview-environment-pre-production) page.
By default, every preview branch automatically receives its own domain similar to the one shown below, whenever a commit is pushed to it. To learn more about generated URLs, see the [Accessing Deployments through Generated URLs](https://vercel.com/docs/deployments/generated-urls#generated-from-git) page.
###  [Multiple preview phases](https://vercel.com/docs/git#multiple-preview-phases)[](https://vercel.com/docs/git#multiple-preview-phases)
For most use cases, the default preview behavior mentioned above is enough. If you'd like your changes to pass through multiple phases of preview branches instead of just one, you can accomplish it by [assigning Domains](https://vercel.com/docs/domains/working-with-domains/assign-domain-to-a-git-branch) and [Environment Variables](https://vercel.com/docs/environment-variables#preview-environment-variables) to specific Preview Branches.
For example, you could create a phase called "Staging" where you can accumulate Preview changes before merging them onto production by following these steps:
  1. Create a Git branch called "staging" in your Git repository.
  2. Add a domain of your choice (like `staging.example.com`) on your Vercel project and assign it to the "staging" Git branch [like this](https://vercel.com/docs/domains/working-with-domains/assign-domain-to-a-git-branch).
  3. Add Environment Variables that you'd like to use for your new Staging phase on your Vercel project [like this](https://vercel.com/docs/environment-variables#preview-environment-variables).
  4. Push to the "staging" Git branch to update your Staging phase and automatically receive the domain and environment variables you've defined.
  5. Once you're happy with your changes, you would then merge the respective Preview Branch into your production branch. However, unlike with the default Preview behavior, you'd then keep the branch around instead of deleting it, so that you can push to it again in the future.


Alternatively, teams on the Pro plan can use [custom environments](https://vercel.com/docs/deployments/environments#custom-environments).
###  [Using custom environments](https://vercel.com/docs/git#using-custom-environments)[](https://vercel.com/docs/git#using-custom-environments)
[Custom environments](https://vercel.com/docs/deployments/environments#custom-environments) allow you to create and define a pre-production environment. As part of creating a custom environment, you can match specific branches or branch names, including `main`, to automatically deploy to that environment. You can also attach a domain to the environment.
* * *
[ Previous Environment Variables ](https://vercel.com/docs/environment-variables)[ Next GitHub ](https://vercel.com/docs/git/vercel-for-github)
Was this helpful?
Send
On this page
  * [Supported Git Providers](https://vercel.com/docs/git#supported-git-providers)
  * [Self-Hosted examples](https://vercel.com/docs/git#self-hosted-examples)
  * [Deploying a Git repository](https://vercel.com/docs/git#deploying-a-git-repository)
  * [Creating a deployment from a Git reference](https://vercel.com/docs/git#creating-a-deployment-from-a-git-reference)
  * [Deploying private Git repositories](https://vercel.com/docs/git#deploying-private-git-repositories)
  * [Using Pro teams](https://vercel.com/docs/git#using-pro-teams)
  * [Using Hobby teams](https://vercel.com/docs/git#using-hobby-teams)
  * [Deploying forks of public Git repositories](https://vercel.com/docs/git#deploying-forks-of-public-git-repositories)
  * [Production branch](https://vercel.com/docs/git#production-branch)
  * [Default configuration](https://vercel.com/docs/git#default-configuration)
  * [Customizing the production branch](https://vercel.com/docs/git#customizing-the-production-branch)
  * [Preview branches](https://vercel.com/docs/git#preview-branches)
  * [Multiple preview phases](https://vercel.com/docs/git#multiple-preview-phases)
  * [Using custom environments](https://vercel.com/docs/git#using-custom-environments)


Copy as MarkdownGive feedbackAsk AI about this page
