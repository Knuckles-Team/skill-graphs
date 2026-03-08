##  [Features](https://vercel.com/docs/functions/runtimes#features)[](https://vercel.com/docs/functions/runtimes#features)
  * Location: Deployed as region-first, [can customize location](https://vercel.com/docs/functions/configuring-functions/region#setting-your-default-region). Pro and Enterprise teams can set [multiple regions](https://vercel.com/docs/functions/configuring-functions/region#project-configuration)
  * [Failover](https://vercel.com/docs/functions/runtimes#failover-mode): Automatic failover to [defined regions](https://vercel.com/docs/functions/configuring-functions/region#node.js-runtime-failover)
  * [Automatic concurrency scaling](https://vercel.com/docs/functions/concurrency-scaling#automatic-concurrency-scaling): Auto-scales up to 30,000 (Hobby and Pro) or 100,000+ (Enterprise) concurrency
  * [Isolation boundary](https://vercel.com/docs/functions/runtimes#isolation-boundary): microVM
  * [File system support](https://vercel.com/docs/functions/runtimes#file-system-support): Read-only filesystem with writable `/tmp` scratch space up to 500 MB
  * [Archiving](https://vercel.com/docs/functions/runtimes#archiving): Functions are archived when not invoked
  * [Functions created per deployment](https://vercel.com/docs/functions/runtimes#functions-created-per-deployment): Hobby: Framework-dependent, Pro and Enterprise: No limit


###  [Location](https://vercel.com/docs/functions/runtimes#location)[](https://vercel.com/docs/functions/runtimes#location)
Location refers to where your functions are executed. Vercel Functions are region-first, and can be [deployed](https://vercel.com/docs/functions/configuring-functions/region#project-configuration) to up to 3 regions on Pro or 18 on Enterprise. Deploying to more regions than your plan allows for will cause your deployment to fail before entering the [build step](https://vercel.com/docs/deployments/configure-a-build).
###  [Failover mode](https://vercel.com/docs/functions/runtimes#failover-mode)[](https://vercel.com/docs/functions/runtimes#failover-mode)
Vercel's failover mode refers to the system's behavior when a function fails to execute because of data center downtime.
Vercel provides [redundancy](https://vercel.com/docs/regions#outage-resiliency) and automatic failover for Vercel Functions using the Edge runtime. For Vercel Functions on the Node.js runtime, you can use the [`functionFailoverRegions` configuration](https://vercel.com/docs/project-configuration#functionfailoverregions) in your `vercel.json` file to specify which regions the function should automatically failover to.
###  [Isolation boundary](https://vercel.com/docs/functions/runtimes#isolation-boundary)[](https://vercel.com/docs/functions/runtimes#isolation-boundary)
In Vercel, the isolation boundary refers to the separation of individual instances of a function to ensure they don't interfere with each other. This provides a secure execution environment for each function.
With traditional serverless infrastructure, each function uses a microVM for isolation, which provides strong security but also makes them slower to start and more resource intensive.
###  [File system support](https://vercel.com/docs/functions/runtimes#file-system-support)[](https://vercel.com/docs/functions/runtimes#file-system-support)
Filesystem support refers to a function's ability to read and write to the filesystem. Vercel functions have a read-only filesystem with writable `/tmp` scratch space up to 500 MB.
###  [Archiving](https://vercel.com/docs/functions/runtimes#archiving)[](https://vercel.com/docs/functions/runtimes#archiving)
Vercel Functions are archived when they are not invoked:
  * Within 2 weeks for [Production Deployments](https://vercel.com/docs/deployments)
  * Within 48 hours for [Preview Deployments](https://vercel.com/docs/deployments/environments#preview-environment-pre-production)


Archived functions will be unarchived when they're invoked, which can make the initial [cold start](https://vercel.com/docs/infrastructure/compute#cold-and-hot-boots) time at least 1 second longer than usual.
###  [Functions created per deployment](https://vercel.com/docs/functions/runtimes#functions-created-per-deployment)[](https://vercel.com/docs/functions/runtimes#functions-created-per-deployment)
When using [Next.js](https://vercel.com/docs/frameworks/nextjs) or [SvelteKit](https://vercel.com/docs/frameworks/sveltekit) on Vercel, dynamic code (APIs, server-rendered pages, or dynamic `fetch` requests) will be bundled into the fewest number of Vercel Functions possible, to help reduce cold starts. Because of this, it's unlikely that you'll hit the limit of 12 bundled Vercel Functions per deployment.
When using other [frameworks](https://vercel.com/docs/frameworks), or Vercel Functions [directly without a framework](https://vercel.com/docs/functions), every API maps directly to one Vercel Function. For example, having five files inside `api/` would create five Vercel Functions. For Hobby, this approach is limited to 12 Vercel Functions per deployment.
