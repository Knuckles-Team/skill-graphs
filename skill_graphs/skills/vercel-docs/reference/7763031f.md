##  [Deployment Methods](https://vercel.com/docs/deployments#deployment-methods)[](https://vercel.com/docs/deployments#deployment-methods)
###  [Git](https://vercel.com/docs/deployments#git)[](https://vercel.com/docs/deployments#git)
The most common way to create a deployment is by pushing code to a connected [Git repository](https://vercel.com/docs/git). When you [import a Git repository to Vercel](https://vercel.com/docs/git#deploying-a-git-repository), each commit or pull request (on supported Git providers) automatically triggers a new deployment.
Vercel supports the following providers:
  * [GitHub](https://vercel.com/docs/git/vercel-for-github)
  * [GitLab](https://vercel.com/docs/git/vercel-for-gitlab)
  * [Bitbucket](https://vercel.com/docs/git/vercel-for-bitbucket)
  * [Azure DevOps](https://vercel.com/docs/git/vercel-for-azure-pipelines)


You can also [create deployments from a Git reference](https://vercel.com/docs/git#creating-a-deployment-from-a-git-reference) using the Vercel Dashboard if you need to deploy specific commits or branches manually.
###  [Vercel CLI](https://vercel.com/docs/deployments#vercel-cli)[](https://vercel.com/docs/deployments#vercel-cli)
You can deploy your Projects directly from the command line using [Vercel CLI](https://vercel.com/docs/cli). This method works whether your project is connected to Git or not.
  1. Install Vercel CLI:


Terminal
```
```
npm i -g vercel
```
`
```

```
```
bun i -g vercel
```
`
```

```
```
yarn global add vercel
```
`
```

```
```
pnpm i -g vercel
```
`
```

  1. Initial Deployment:


In your project's root directory, run:
```
vercel --prod
```

This links your local directory to your Vercel Project and creates a [Production Deployment](https://vercel.com/docs/deployments/environments#production-environment). A `.vercel` directory is added to store Project and Organization IDs.
Vercel CLI can also integrate with custom CI/CD workflows or third-party pipelines. Learn more about the different [environments on Vercel](https://vercel.com/docs/deployments/environments).
###  [Deploy Hooks](https://vercel.com/docs/deployments#deploy-hooks)[](https://vercel.com/docs/deployments#deploy-hooks)
[Deploy Hooks](https://vercel.com/docs/deploy-hooks) let you trigger deployments with a unique URL. You must have a connected Git repository to use this feature, but the deployment doesn't require a new commit.
  1. From your Project settings, create a Deploy Hook
  2. Vercel generates a unique URL for each Project
  3. Make an HTTP `GET` or `POST` request to this URL to trigger the deployment


Refer to the [Deploy Hooks documentation](https://vercel.com/docs/deploy-hooks) for more information.
###  [Vercel REST API](https://vercel.com/docs/deployments#vercel-rest-api)[](https://vercel.com/docs/deployments#vercel-rest-api)
The [Vercel REST API](https://vercel.com/docs/rest-api) lets you create deployments by making an HTTP `POST` request to the deployment endpoint. In this workflow:
  1. Generate a SHA for each file you want to deploy
  2. Upload those files to Vercel
  3. Send a request to create a new deployment with those file references


This method is especially useful for custom workflows, multi-tenant applications, or integrating with third-party services not officially supported by Vercel. For more details, see the [API reference](https://vercel.com/docs/rest-api/reference/endpoints/deployments/create-a-new-deployment) and [How do I generate an SHA for uploading a file](https://vercel.com/kb/guide/how-do-i-generate-an-sha-for-uploading-a-file-to-the-vercel-api).
