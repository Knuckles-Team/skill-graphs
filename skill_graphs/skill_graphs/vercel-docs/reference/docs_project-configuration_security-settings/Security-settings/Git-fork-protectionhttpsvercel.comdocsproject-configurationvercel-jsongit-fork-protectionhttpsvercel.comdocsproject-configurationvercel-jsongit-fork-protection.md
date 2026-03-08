##  [Git fork protection](https://vercel.com/docs/project-configuration/vercel-json#git-fork-protection)[](https://vercel.com/docs/project-configuration/vercel-json#git-fork-protection)
If you receive a pull request from a fork of your repository, Vercel will require authorization from you or a [Team Member](https://vercel.com/docs/rbac/managing-team-members) to deploy the pull request.
This behavior protects you from leaking sensitive project information such as environment variables and the [OIDC Token](https://vercel.com/docs/oidc).
You can disable this protection in the Security section of your Project Settings.
Do not disable this setting until you review Environment Variables in your project as well as `vercel.json` in your source code.
