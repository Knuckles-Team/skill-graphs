##  [Setting a deployment retention policy](https://vercel.com/docs/deployment-retention#setting-a-deployment-retention-policy)[](https://vercel.com/docs/deployment-retention#setting-a-deployment-retention-policy)
To configure a retention policy, open Settings in the sidebar of your project and follow these steps:
  1. Select Security on the side panel of the project settings page
  2. Scroll down to the Deployment Retention Policy section
  3. Select the drop down menu with the appropriate duration
  4. Save the new retention policy for your project


###  [Viewing deployment retention policy](https://vercel.com/docs/deployment-retention#viewing-deployment-retention-policy)[](https://vercel.com/docs/deployment-retention#viewing-deployment-retention-policy)
You can view your deployments retention policy using [Vercel CLI](https://vercel.com/docs/cli/list) and running the following command from your terminal:
terminal
```
vercel list [project-name] [--policy errored=6m]
```

###  [Exceptions to the retention policy](https://vercel.com/docs/deployment-retention#exceptions-to-the-retention-policy)[](https://vercel.com/docs/deployment-retention#exceptions-to-the-retention-policy)
Deployments older than the configured retention interval are not always deleted. Deployments will be kept while any of the following is true:
  * The deployment is one of the last 10 deployments created in the project.
  * The deployment is one of the last 20 production deployments in state Ready.
  * The deployment is one of the last 20 non-production deployments in state Ready.
  * The deployment has a production alias assigned to it.
  * The deployment is the target of a [branch alias](https://vercel.com/docs/domains/working-with-domains/assign-domain-to-a-git-branch) for a [custom environment](https://vercel.com/docs/deployments/environments#custom-environments).
  * The deployment is a non-production deployment and has any custom alias assigned to it.
