##  [Usage](https://vercel.com/docs/monorepos/remote-caching#usage)[](https://vercel.com/docs/monorepos/remote-caching#usage)
Vercel Remote Cache is free for all plans, subject to fair use guidelines.
Plan | Fair use upload limit | Fair use artifacts request limit
---|---|---
Hobby | 100GB / month | 100 / minute
Pro | 1TB / month | 10000 / minute
Enterprise | 4TB / month | 10000 / minute
###  [Artifacts](https://vercel.com/docs/monorepos/remote-caching#artifacts)[](https://vercel.com/docs/monorepos/remote-caching#artifacts)
Metric | Description | Priced | Optimize
---|---|---|---
[Number of Remote Cache Artifacts](https://vercel.com/docs/monorepos/remote-caching#number-of-remote-cache-artifacts) | The number of uploaded and downloaded artifacts using the Remote Cache API | No | N/A
Total Size of Remote Cache Artifacts | The size of uploaded and downloaded artifacts using the Remote Cache API | No | [Learn More](https://vercel.com/docs/monorepos/remote-caching#optimizing-total-size-of-remote-cache-artifacts)
[Time Saved](https://vercel.com/docs/monorepos/remote-caching#time-saved) | The time saved by using artifacts cached on the Vercel Remote Cache API | No | N/A
Artifacts are blobs of data or files that are uploaded and downloaded using the [Vercel Remote Cache API](https://vercel.com/docs/monorepos/remote-caching), including calls made using [Turborepo](https://vercel.com/docs/monorepos/turborepo#setup-remote-caching-for-turborepo-on-vercel) and the [build](https://vercel.com/docs/deployments/configure-a-build) by any [team members](https://vercel.com/docs/accounts/team-members-and-roles).
Vercel automatically expires uploaded artifacts after 7 days to avoid unbounded cache growth.
####  [Time Saved](https://vercel.com/docs/monorepos/remote-caching#time-saved)[](https://vercel.com/docs/monorepos/remote-caching#time-saved)
Artifacts get annotated with a task duration, which is the time required for the task to run and generate the artifact. The time saved is the sum of that task duration for each artifact multiplied by the number of times that artifact is reused from a cache.
  * Remote Cache: The time saved by using artifacts cached on the Vercel Remote Cache API
  * Local Cache: The time saved by using artifacts cached on your local filesystem cache


####  [Number of Remote Cache Artifacts](https://vercel.com/docs/monorepos/remote-caching#number-of-remote-cache-artifacts)[](https://vercel.com/docs/monorepos/remote-caching#number-of-remote-cache-artifacts)
When your team enables [Vercel Remote Cache](https://vercel.com/docs/monorepos/remote-caching#enable-and-disable-remote-caching-for-your-team), Vercel will automatically cache [Turborepo](https://vercel.com/docs/monorepos/turborepo) outputs (such as files and logs) and create cache artifacts from your builds. This can help speed up your builds by reusing artifacts from previous builds. To learn more about what is cached, see the Turborepo docs on
For other monorepo implementations like [Nx](https://vercel.com/docs/monorepos/nx), you need to manually configure your project using the
You are not charged based on the number of artifacts, but rather the size in GB downloaded.
####  [Optimizing total size of Remote Cache artifacts](https://vercel.com/docs/monorepos/remote-caching#optimizing-total-size-of-remote-cache-artifacts)[](https://vercel.com/docs/monorepos/remote-caching#optimizing-total-size-of-remote-cache-artifacts)
Caching only the files needed for the task will improve cache restoration performance.
For example, the `.next` folder contains your build artifacts. You can avoid caching the `.next/cache` folder since it is only used for development and will not speed up your production builds.
