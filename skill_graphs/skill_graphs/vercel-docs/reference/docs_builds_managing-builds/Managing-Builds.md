# Managing Builds
Last updated February 5, 2026
Turbo build machines are now enabled by default for new Pro projects - [Learn more](https://vercel.com/docs/builds/managing-builds#larger-build-machines)
When you build your application code, Vercel runs compute to install dependencies, run your build script, and sends the build output to our [Compute](https://vercel.com/docs/fluid-compute) and [CDN](https://vercel.com/docs/cdn).
By default, we enable our fastest build settings for Pro customers' new projects: [Turbo build machines](https://vercel.com/docs/builds/managing-builds#larger-build-machines) and [On-Demand Concurrent Builds](https://vercel.com/docs/builds/managing-builds#on-demand-concurrent-builds).
  * If you're on a Hobby plan and looking for faster builds, we recommend [upgrading to Pro](https://vercel.com/docs/plans/pro-plan).
  * If you're on an Enterprise plan, build machines are managed as a part of your contract.


[Visit Build Diagnostics in the Observability section in the Vercel dashboard sidebar](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fobservability%2Fbuild-diagnostics&title=Visit+Build+Diagnostics) to find your build durations. You can also use this table to quickly identify which solution fits your needs:
Your situation | Solution | Best for
---|---|---
Builds are slow or running out of resources | [Enhanced/Turbo build machines](https://vercel.com/docs/builds/managing-builds#larger-build-machines) | Large apps, complex dependencies
Builds are frequently queued | [On-demand Concurrent Builds](https://vercel.com/docs/builds/managing-builds#on-demand-concurrent-builds) | Teams with frequent deployments
Specific projects are frequently queued | [Project-level on-demand](https://vercel.com/docs/builds/managing-builds#project-level-on-demand-concurrent-builds) | Fast-moving projects
Occasional urgent deploy stuck in queue | [Force an on-demand build](https://vercel.com/docs/builds/managing-builds#force-an-on-demand-build) | Ad-hoc critical fixes
Production builds stuck behind preview builds | [Prioritize production builds](https://vercel.com/docs/builds/managing-builds#prioritize-production-builds) | All production-heavy workflows
