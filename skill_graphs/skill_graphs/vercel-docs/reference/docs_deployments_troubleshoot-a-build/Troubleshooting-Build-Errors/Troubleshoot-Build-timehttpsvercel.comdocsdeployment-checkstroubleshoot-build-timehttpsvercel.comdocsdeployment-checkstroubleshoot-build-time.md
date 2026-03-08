##  [Troubleshoot Build time](https://vercel.com/docs/deployment-checks#troubleshoot-build-time)[](https://vercel.com/docs/deployment-checks#troubleshoot-build-time)
###  [Understanding Build cache](https://vercel.com/docs/deployment-checks#understanding-build-cache)[](https://vercel.com/docs/deployment-checks#understanding-build-cache)
The first Build in a Project will take longer as the Build cache is initially empty. Subsequent builds that have the same [Build cache key](https://vercel.com/docs/deployment-checks#caching-process) will take less time because elements from your build, such as [framework files and node modules](https://vercel.com/docs/deployment-checks#what-is-cached), will be reused from the available cache. The next sections will describe the factors that affect the Build cache to help you decrease the Build time
###  [What is cached](https://vercel.com/docs/deployment-checks#what-is-cached)[](https://vercel.com/docs/deployment-checks#what-is-cached)
Vercel caches files based on the [Framework Preset](https://vercel.com/docs/deployments/configure-a-build#framework-preset) selected in your [Project settings](https://vercel.com/docs/projects/overview#project-settings). The following files are cached in addition to `node_modules/**`:
Framework | Cache Pattern
---|---
Next.js | `.next/cache/**`
Nuxt | `.nuxt/**`
Gatsby.js | `{.cache,public}/**`
Eleventy | `.cache/**`
Jekyll | `{vendor/bin,vendor/cache,vendor/bundle}/**`
Middleman | `{vendor/bin,vendor/cache,vendor/bundle}/**`
Note that the framework detection is dependent on the preset selection made in the [Build settings](https://vercel.com/docs/deployments/configure-a-build#build-and-development-settings). You should make sure that the correct framework is set for your project for optimum build caching.
###  [Caching process](https://vercel.com/docs/deployment-checks#caching-process)[](https://vercel.com/docs/deployment-checks#caching-process)
At the beginning of each build, the previous Build's cache is restored prior to the [Install Command](https://vercel.com/docs/deployments/configure-a-build#install-command) or [Build command](https://vercel.com/docs/deployments/configure-a-build#build-command) executing. Each deployment is associated with a unique Build cache key that is derived from the combination of the following data:
  * [Personal Account](https://vercel.com/docs/teams-and-accounts#creating-a-personal-account) or [Team](https://vercel.com/docs/teams-and-accounts)
  * [Project](https://vercel.com/docs/projects/overview)
  * [Framework Preset](https://vercel.com/docs/deployments/configure-a-build#framework-preset)
  * [Root Directory](https://vercel.com/docs/deployments/configure-a-build#root-directory)
  * [Node.js Version](https://vercel.com/docs/functions/runtimes/node-js#node.js-version)
  * [Package Manager](https://vercel.com/docs/deployments/configure-a-build#install-command)
  * [Git branch](https://vercel.com/docs/git)


Let's say that under your account `MyTeam`, you have a project `MySite` that is connected to your Git repository `MyCode` on the `main` branch for the production environment. When you make a commit to the `main` branch for the first time, you trigger a build that creates a production deployment with a new unique cache key. For any new commits to the `main` branch of `MyCode`, the existing Build cache is used as long as `MySite` is under `MyTeam`.
If you create a new Git branch in `MyCode` and make a commit to it, there is no cache for that specific branch. In this case, the last [production Deployment](https://vercel.com/docs/deployments/environments#production-environment) cache is used to create a preview deployment and a new branch cache is created for subsequent commits to the new branch.
If you use [Vercel functions](https://vercel.com/docs/functions) to process HTTP requests in your project, each Vercel Function is built separately in the Build step and has its own cache, based on the [Runtime](https://vercel.com/docs/functions/runtimes) used. Therefore, the number and size of Vercel functions will affect your Build time. For Next.js projects, Vercel functions are bundled to optimize Build resources as described [here](https://vercel.com/docs/functions/configuring-functions/advanced-configuration#bundling-vercel-functions).
At the end of each Build step, successful builds will update the cache and failed builds will not modify the existing cache.
###  [Excluding development dependencies](https://vercel.com/docs/deployment-checks#excluding-development-dependencies)[](https://vercel.com/docs/deployment-checks#excluding-development-dependencies)
Since development dependencies (for example, packages such as `webpack` or `Babel`) are not needed in production, you may want to prevent them from being installed when deploying to Vercel to reduce the Build time. To skip development dependencies, customize the [Install Command](https://vercel.com/docs/deployments/configure-a-build#install-command) to be `npm install --only=production` or `yarn install --production`.
