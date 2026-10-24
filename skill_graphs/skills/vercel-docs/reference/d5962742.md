##  [Setting your default function memory / CPU size](https://vercel.com/docs/functions#setting-your-default-function-memory-/-cpu-size)[](https://vercel.com/docs/functions#setting-your-default-function-memory-/-cpu-size)
Those on the Pro or Enterprise plans can configure the default memory size for all functions in a project.
To change the default function memory size:
  1. Choose the appropriate project from your [dashboard](https://vercel.com/dashboard)
  2. Open Settings in the sidebar
  3. Scroll to [Functions](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Ffunctions&title=Go+to+Functions+Settings)
  4. Select Advanced Settings
  5. In the Function CPU section, select your preferred memory size option:

![The Function CPU setting in a Vercel project's dashboard](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Ffunctions%2Fconfigure-mem-light.png&w=1920&q=75)![The Function CPU setting in a Vercel project's dashboard](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Ffunctions%2Fconfigure-mem-dark.png&w=1920&q=75)The Function CPU setting in a Vercel project's dashboard
  1. The change will be applied to all future deployments made by your team. You must create a new deployment for your changes to take effect


You cannot set your memory size using `vercel.json`. If you try to do so, you will receive a warning at build time. Only Pro and Enterprise users can set the default memory size in the dashboard. Hobby users will always use the default memory size of 2 GB (1 vCPU).
###  [Memory / CPU type](https://vercel.com/docs/functions#memory-/-cpu-type)[](https://vercel.com/docs/functions#memory-/-cpu-type)
The memory size you select will also determine the CPU allocated to your Vercel Functions. The following table shows the memory and CPU allocation for each type.
With [fluid compute enabled](https://vercel.com/docs/fluid-compute) on Pro and Enterprise plans, the default memory size is 2 GB (1 vCPU) and can be upgraded to 4 GB / 2 vCPUs, for Hobby users, Vercel manages the CPU with a minimum of 1 vCPU.
Type | Memory / CPU | Use
---|---|---
Standard Default | 2 GB / 1 vCPU | Predictable performance for production workloads. Default for [fluid compute](https://vercel.com/docs/fluid-compute).
Performance | 4 GB / 2 vCPUs | Increased performance for latency-sensitive applications and SSR workloads.
Users on the Hobby plan can only use the default memory size of 2 GB (1 vCPU). Hobby users cannot configure this size. If you are on the Hobby plan, and have enabled fluid compute, the memory size will be managed by Vercel with a minimum of 1 vCPU.
Projects created before 2019-11-08 have the default function memory size set to 1024 MB/0.6 vCPU for Hobby plan, and 3008 MB/1.67 vCPU for Pro and Enterprise plan. Although the dashboard may not have any memory size option selected by default for those projects, you can start using the new memory size options by selecting your preferred memory size in the dashboard.
