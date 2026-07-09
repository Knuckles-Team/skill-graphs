##  [Limits and resources](https://vercel.com/docs/builds#limits-and-resources)[](https://vercel.com/docs/builds#limits-and-resources)
Vercel enforces certain limits to ensure reliable builds for all users:
  * Build timeout: The maximum build time is 45 minutes. If your build exceeds this limit, it will be terminated, and the deployment fails.
  * Build cache: Each build cache can be up to 1 GB. The [cache](https://vercel.com/docs/deployments/troubleshoot-a-build#caching-process) is retained for one month. Restoring a build cache can speed up subsequent deployments.
  * Container resources: Vercel creates a [build container](https://vercel.com/docs/builds/build-image) with different resources depending on your plan:
| Hobby | Pro | Enterprise
---|---|---|---
Memory | 8192 MB | 8192 MB | Custom
Disk Space | 23 GB | 23 GB | Custom
CPUs | 2 | 4 | Custom


For more information, visit [Build Container Resources](https://vercel.com/docs/deployments/troubleshoot-a-build#build-container-resources) and [Cancelled Builds](https://vercel.com/docs/deployments/troubleshoot-a-build#cancelled-builds-due-to-limits).
