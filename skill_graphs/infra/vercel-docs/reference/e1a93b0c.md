##  [When does a monorepo build occur?](https://vercel.com/docs/deployment-checks#when-does-a-monorepo-build-occur)[](https://vercel.com/docs/deployment-checks#when-does-a-monorepo-build-occur)
By default, pushing a commit to your monorepo will create a deployment for each of the connected Vercel projects. However, you can choose to:
  * [Skip unaffected projects](https://vercel.com/docs/deployment-checks#skipping-unaffected-projects) by only building projects whose files have changed.
  * [Ignore the build step](https://vercel.com/docs/deployment-checks#ignoring-the-build-step) for projects whose files haven't changed.


###  [Skipping unaffected projects](https://vercel.com/docs/deployment-checks#skipping-unaffected-projects)[](https://vercel.com/docs/deployment-checks#skipping-unaffected-projects)
Vercel considers a project in a monorepo changed if any of the following conditions are true:
  1. The project source code has changed
  2. Any of the project's internal dependencies have changed.
  3. A change to a package manager lockfile has occurred, that _only_ impacts the dependencies of the project.


Vercel automatically skips builds for projects in a monorepo that are unchanged by the commit.
This setting does not occupy [concurrent build slots](https://vercel.com/docs/deployments/concurrent-builds), unlike the [Ignored Build Step](https://vercel.com/docs/project-configuration/project-settings#ignored-build-step) feature, reducing build queue times.
####  [Requirements](https://vercel.com/docs/deployment-checks#requirements)[](https://vercel.com/docs/deployment-checks#requirements)
  * This feature is only available for projects connected to GitHub repositories.
  * The monorepo must be using npm, yarn, pnpm, or Bun workspaces, following JavaScript ecosystem conventions. Packages in the workspace must be included in the workspace definition (`workspaces` key in `package.json` for npm and yarn or `pnpm-workspace.yaml` for pnpm).
    * Changes that are not a part of the workspace definition will be considered global changes and deploy all applications in the repository.
    * We automatically detect your package manager using the lockfile at the repository root. You can also explicitly set a package manager with the `packageManager` field in root `package.json` file.
  * All packages within the workspace must have a unique `name` field in their `package.json` file.
  * Dependencies between packages in the monorepo must be explicitly stated in each package's `package.json` file. This is necessary to determine the dependency graph between packages.
    * For example, an end-to-end tests package (`package-e2e`) tests must depend on the package it tests (`package-core`) in the `package.json` of `package-e2e`.


####  [Disable the skipping unaffected projects feature](https://vercel.com/docs/deployment-checks#disable-the-skipping-unaffected-projects-feature)[](https://vercel.com/docs/deployment-checks#disable-the-skipping-unaffected-projects-feature)
To disable this behavior, [visit the project's Root Directory settings](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fbuild-and-deployment%23root-directory&title=Disable+unaffected+project+skipping).
  1. From the [Dashboard](https://vercel.com/d?to=%2Fdashboard&title=Open+Dashboard), select the project you want to configure and open Settings in the sidebar.
  2. Go to the Build and Deployment page of the project's Settings.
  3. Scroll down to Root Directory
  4. Toggle the Skip deployment switch to Disabled.
  5. Click Save to apply the changes.


###  [Ignoring the build step](https://vercel.com/docs/deployment-checks#ignoring-the-build-step)[](https://vercel.com/docs/deployment-checks#ignoring-the-build-step)
If you want to cancel the Build Step for projects if their files didn't change, you can do so with the [Ignored Build Step](https://vercel.com/docs/project-configuration/project-settings#ignored-build-step) project setting. Canceled builds initiated using the ignore build step do count towards your deployment and concurrent build limits and so [skipping unaffected projects](https://vercel.com/docs/deployment-checks#skipping-unaffected-projects) may be a better option for monorepos with many projects.
If you have created a script to ignore the build step, you can skip the [the script](https://vercel.com/kb/guide/how-do-i-use-the-ignored-build-step-field-on-vercel) when redeploying or promoting your app to production. This can be done through the dashboard when you click on the Redeploy button, and unchecking the Use project's Ignore Build Step checkbox.
