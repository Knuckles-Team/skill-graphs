##  [Managing Build cache](https://vercel.com/docs/deployment-checks#managing-build-cache)[](https://vercel.com/docs/deployment-checks#managing-build-cache)
Sometimes, you may not want to use the Build cache for a specific deployment. You can invalidate or delete the existing Build cache in the following ways:
  * Use the Redeploy button for the specific deployment in the Project's [Deployments](https://vercel.com/docs/deployments/managing-deployments) page. In the popup window that follows, leave the checkbox Use existing Build Cache unchecked. See [Redeploying a project](https://vercel.com/docs/deployments/managing-deployments#redeploy-a-project) for more information.
  * Use [`vercel --force`](https://vercel.com/docs/cli/deploy#force) with [Vercel CLI](https://vercel.com/docs/cli) to build and deploy the project without the Build cache
  * Use an Environment Variable `VERCEL_FORCE_NO_BUILD_CACHE` with a value of `1` on your project to skip the Build cache
  * Use an Environment Variable `TURBO_FORCE` with a value of `true` on your project to skip Turborepo [Remote Cache](https://vercel.com/docs/monorepos/remote-caching)
  * Use the `forceNew` optional query parameter with a value of `1` when [creating a new deployment with the Vercel API](https://vercel.com/docs/rest-api/reference/endpoints/deployments/create-a-new-deployment) to skip the Build cache


When redeploying without the existing Build Cache, the Remote Cache from
* * *
[ Previous Deploy Hooks ](https://vercel.com/docs/deploy-hooks)[ Next Deployment Retention ](https://vercel.com/docs/deployment-retention)
Was this helpful?
Send
On this page
  * [Troubleshooting views](https://vercel.com/docs/deployment-checks#troubleshooting-views)
  * [Troubleshoot Build failures](https://vercel.com/docs/deployment-checks#troubleshoot-build-failures)
  * [Investigating Build logs](https://vercel.com/docs/deployment-checks#investigating-build-logs)
  * [Build Logs not available](https://vercel.com/docs/deployment-checks#build-logs-not-available)
  * [Cancelled Builds due to limits](https://vercel.com/docs/deployment-checks#cancelled-builds-due-to-limits)
  * [Build container resources](https://vercel.com/docs/deployment-checks#build-container-resources)
  * [Build duration](https://vercel.com/docs/deployment-checks#build-duration)
  * [Caching](https://vercel.com/docs/deployment-checks#caching)
  * [Other Build errors](https://vercel.com/docs/deployment-checks#other-build-errors)
  * [Troubleshoot Build time](https://vercel.com/docs/deployment-checks#troubleshoot-build-time)
  * [Understanding Build cache](https://vercel.com/docs/deployment-checks#understanding-build-cache)
  * [What is cached](https://vercel.com/docs/deployment-checks#what-is-cached)
  * [Caching process](https://vercel.com/docs/deployment-checks#caching-process)
  * [Excluding development dependencies](https://vercel.com/docs/deployment-checks#excluding-development-dependencies)
  * [Managing Build cache](https://vercel.com/docs/deployment-checks#managing-build-cache)


Copy as MarkdownGive feedbackAsk AI about this page
