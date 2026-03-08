##  [Changing the GitHub Repository of a Project](https://vercel.com/docs/builds#changing-the-github-repository-of-a-project)[](https://vercel.com/docs/builds#changing-the-github-repository-of-a-project)
If you'd like to connect your Vercel Project to a different GitHub repository or disconnect it, you can do so from the [Git section](https://vercel.com/docs/projects/overview#git) in the Project Settings.
###  [A Deployment for Each Push](https://vercel.com/docs/builds#a-deployment-for-each-push)[](https://vercel.com/docs/builds#a-deployment-for-each-push)
Vercel for GitHub will deploy every push by default. This includes pushes and pull requests made to branches. This allows those working within the repository to preview changes made before they are pushed to production.
With each new push, if Vercel is already building a previous commit on the same branch, the current build will complete and any commit pushed during this time will be queued. Once the first build completes, the most recent commit will begin deployment and the other queued builds will be cancelled. This ensures that you always have the latest changes deployed as quickly as possible.
You can disable this feature for GitHub by configuring the [github.autoJobCancellation](https://vercel.com/docs/project-configuration/git-configuration#github.autojobcancelation) option in your `vercel.json` file.
###  [Updating the Production Domain](https://vercel.com/docs/builds#updating-the-production-domain)[](https://vercel.com/docs/builds#updating-the-production-domain)
If [Custom Domains](https://vercel.com/docs/projects/custom-domains) are set from a project domains dashboard, pushes and merges to the [Production Branch](https://vercel.com/docs/git#production-branch) (commonly "main") will be made live to those domains with the latest deployment made with a push.
If you decide to revert a commit that has already been deployed to production, the previous [Production Deployment](https://vercel.com/docs/deployments/environments#production-environment) from a commit will automatically be made available at the [Custom Domain](https://vercel.com/docs/projects/custom-domains) instantly; providing you with instant rollbacks.
###  [Preview URLs for the Latest Changes for Each Pull Request](https://vercel.com/docs/builds#preview-urls-for-the-latest-changes-for-each-pull-request)[](https://vercel.com/docs/builds#preview-urls-for-the-latest-changes-for-each-pull-request)
The latest push to any pull request will automatically be made available at a unique [preview URL](https://vercel.com/docs/deployments/environments#preview-environment-pre-production#preview-urls) based on the project name, branch, and team or username. These URLs will be provided through a comment on each pull request. Vercel also supports Comments on preview deployments made from PRs on GitHub. [Learn more about Comments on preview deployments in GitHub here](https://vercel.com/docs/deployments/environments#preview-environment-pre-production#github-integration).
###  [Deployment Authorizations for Forks](https://vercel.com/docs/builds#deployment-authorizations-for-forks)[](https://vercel.com/docs/builds#deployment-authorizations-for-forks)
If you receive a pull request from a fork of your repository, Vercel will require authorization from you or a [team member](https://vercel.com/docs/rbac/managing-team-members) to deploy the pull request.
This behavior protects you from leaking sensitive project information such as environment variables and the [OIDC Token](https://vercel.com/docs/oidc).
You can disable [Git Fork Protection](https://vercel.com/docs/projects/overview#git-fork-protection) in the Security section of your Project Settings.
Vercel for GitHub uses the deployment API to bring you an extended user interface both in GitHub, when showing deployments, and Slack, if you have notifications setup using the
You will see all of your deployments, production or preview, from within GitHub on its own page.
Due to using GitHub's Deployments API, you will also be able to integrate with other services through
###  [Configuring for GitHub](https://vercel.com/docs/builds#configuring-for-github)[](https://vercel.com/docs/builds#configuring-for-github)
To configure the Vercel for GitHub integration, see [the configuration reference for Git](https://vercel.com/docs/project-configuration/git-configuration).
###  [System environment variables](https://vercel.com/docs/builds#system-environment-variables)[](https://vercel.com/docs/builds#system-environment-variables)
You may want to use different workflows and APIs based on Git information. To support this, the following [System Environment Variables](https://vercel.com/docs/environment-variables/system-environment-variables) are exposed to your Deployments:


###  [VERCEL_GIT_PROVIDER](https://vercel.com/docs/builds#VERCEL_GIT_PROVIDER)[](https://vercel.com/docs/builds#VERCEL_GIT_PROVIDER)
The Git Provider the deployment is triggered from. In the case of GitHub, the value is always `github`.
###  [VERCEL_GIT_REPO_SLUG](https://vercel.com/docs/builds#VERCEL_GIT_REPO_SLUG)[](https://vercel.com/docs/builds#VERCEL_GIT_REPO_SLUG)
The origin repository of the app on GitHub.
.env
```


VERCEL_GIT_REPO_SLUG=my-site


```

###  [VERCEL_GIT_REPO_OWNER](https://vercel.com/docs/builds#VERCEL_GIT_REPO_OWNER)[](https://vercel.com/docs/builds#VERCEL_GIT_REPO_OWNER)
The GitHub organization that owns the repository the deployment is triggered from.
.env
```


VERCEL_GIT_REPO_OWNER=acme


```

###  [VERCEL_GIT_REPO_ID](https://vercel.com/docs/builds#VERCEL_GIT_REPO_ID)[](https://vercel.com/docs/builds#VERCEL_GIT_REPO_ID)
The ID of the GitHub repository the deployment is triggered from.
.env
```


VERCEL_GIT_REPO_ID=117716146


```

###  [VERCEL_GIT_COMMIT_REF](https://vercel.com/docs/builds#VERCEL_GIT_COMMIT_REF)[](https://vercel.com/docs/builds#VERCEL_GIT_COMMIT_REF)
The GitHub branch that the deployment was made from.
.env
```


VERCEL_GIT_COMMIT_REF=improve-about-page


```

###  [VERCEL_GIT_COMMIT_SHA](https://vercel.com/docs/builds#VERCEL_GIT_COMMIT_SHA)[](https://vercel.com/docs/builds#VERCEL_GIT_COMMIT_SHA)
The GitHub
.env
```


VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081


```

###  [VERCEL_GIT_COMMIT_MESSAGE](https://vercel.com/docs/builds#VERCEL_GIT_COMMIT_MESSAGE)[](https://vercel.com/docs/builds#VERCEL_GIT_COMMIT_MESSAGE)
The message attached to the GitHub commit the deployment was triggered by. The message is truncated if it exceeds 2048 bytes.
.env
```


VERCEL_GIT_COMMIT_MESSAGE=Update about page


```

###  [VERCEL_GIT_COMMIT_AUTHOR_LOGIN](https://vercel.com/docs/builds#VERCEL_GIT_COMMIT_AUTHOR_LOGIN)[](https://vercel.com/docs/builds#VERCEL_GIT_COMMIT_AUTHOR_LOGIN)
The GitHub username belonging to the author of the commit that the project was deployed by.
.env
```


VERCEL_GIT_COMMIT_AUTHOR_LOGIN=johndoe


```

###  [VERCEL_GIT_COMMIT_AUTHOR_NAME](https://vercel.com/docs/builds#VERCEL_GIT_COMMIT_AUTHOR_NAME)[](https://vercel.com/docs/builds#VERCEL_GIT_COMMIT_AUTHOR_NAME)
The GitHub name belonging to the author of the commit that the project was deployed by.
.env
```


VERCEL_GIT_COMMIT_AUTHOR_NAME=John Doe


```

###  [VERCEL_GIT_PULL_REQUEST_ID](https://vercel.com/docs/builds#VERCEL_GIT_PULL_REQUEST_ID)[](https://vercel.com/docs/builds#VERCEL_GIT_PULL_REQUEST_ID)
The GitHub pull request id the deployment was triggered by. If a deployment is created on a branch before a pull request is made, this value will be an empty string.
.env
```


VERCEL_GIT_PULL_REQUEST_ID=23


```

We require some permissions through our Vercel for GitHub integration. Below are listed the permissions required and a description for what they are used for.
###  [Repository Permissions](https://vercel.com/docs/builds#repository-permissions)[](https://vercel.com/docs/builds#repository-permissions)
Repository permissions allow us to interact with repositories belonging to or associated with (if permitted) the connected account.
Permission | Read | Write | Description
---|---|---|---
`Administration` | Y | Y | Allows us to create repositories on the user's behalf.
`Checks` | Y | Y | Allows us to add checks against source code on push.
`Contents` | Y | Y | Allows us to fetch and write source code for new project templates for the connected user or organization.
`Deployments` | Y | Y | Allows us to synchronize deployment status between GitHub and the Vercel infrastructure.
`Pull Requests` | Y | Y | Allows us create deployments for each Pull Request (PR) and comment on those PR's with status updates.
`Issues` | Y | Y | Allows us to interact with Pull Requests as with the `Pull Requests` permissions due to GitHub requiring both for access.
`Metadata` | Y | N | Allows us to read basic repository metadata to provide a detailed dashboard.
`Web Hooks` | Y | Y | Allows us to react to various GitHub events.
`Commit Statuses` | Y | Y | Allows us to synchronize commit status between GitHub and Vercel.
###  [Organization Permissions](https://vercel.com/docs/builds#organization-permissions)[](https://vercel.com/docs/builds#organization-permissions)
Organization permissions allow us to offer an enhanced experience through information about the connected organization.
Permission | Read | Write | Description
---|---|---|---
`Members` | Y | N | Allows us to offer a better team onboarding experience.
###  [User Permissions](https://vercel.com/docs/builds#user-permissions)[](https://vercel.com/docs/builds#user-permissions)
User permissions allow us to offer an enhanced experience through information about the connected user.
Permission | Read | Write | Description
---|---|---|---
`Email addresses` | Y | N | Allows us to associate an email with a GitHub account.
We use the permissions above in order to provide you with the best possible deployment experience. If you have any questions or concerns about any of the permission scopes, please [contact Vercel Support](https://vercel.com/help#issues).
To sign up on Vercel with a different GitHub account, sign out of your current GitHub account.
Then, restart the Vercel [signup process](https://vercel.com/signup).
