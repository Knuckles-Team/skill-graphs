##  [Cancelled Builds due to limits](https://vercel.com/docs/deployment-checks#cancelled-builds-due-to-limits)[](https://vercel.com/docs/deployment-checks#cancelled-builds-due-to-limits)
Sometimes, your Deployment Build can hit platform limits so that the build will be cancelled and throw a corresponding error that will be shown in the Build logs. Review the limits below in case you run into them.
###  [Build container resources](https://vercel.com/docs/deployment-checks#build-container-resources)[](https://vercel.com/docs/deployment-checks#build-container-resources)
Every build container has a fixed amount of resources available to it. You can find the resources available for each build machine type [here](https://vercel.com/docs/builds/managing-builds#larger-build-machines).
By default, the system generates this report only when it detects a problem. To receive a report for every deployment, set `VERCEL_BUILD_SYSTEM_REPORT=1` as an [environment variable](https://vercel.com/docs/environment-variables#creating-environment-variables).
This report helps you detect hidden Out of Memory (OOM) events, and provides insights into disk usage by breaking down the sizes of your source code, `node_modules`, and output, and flagging files over 100 MB. The input size in the report corresponds to the size of your checked-out repository or files uploaded by CLI. The `node_modules` size represents the total size of all `node_modules` folders on disk.
Resource | Allocation | Description
---|---|---
Memory | 8192 MB | Fixed memory allocation. Builds exceeding this limit will be cancelled
CPUs | 4 | Number of CPUs allocated for build processing
Disk Space | 23 GB | Fixed disk space allocation. Builds exceeding this limit will be cancelled
System Report | Conditional | Generated in [Build logs](https://vercel.com/docs/deployments/logs) when memory or disk space limits are reached. Available by default
Forced Reporting | Optional | Set `VERCEL_BUILD_SYSTEM_REPORT=1` as an [environment variable](https://vercel.com/docs/environment-variables#creating-environment-variables) to enable reporting for all builds
Review the below steps to help navigate this situation:
  * Review what package the error is related to and explore the package's documentation to see if the memory allocation can be customized with an install or Build command
  * If no package is specified, look into reducing the amount of JavaScript that your Project might be using or find a more efficient JavaScript bundler
  * Review what you are importing in your code such as third-party services, icons and media files


###  [Build duration](https://vercel.com/docs/deployment-checks#build-duration)[](https://vercel.com/docs/deployment-checks#build-duration)
The total build duration is shown on the Vercel Dashboard and includes all three steps: building, checking, and assigning domains. Each step also shows the individual duration.
A Build can last for a maximum of 45 minutes. If the build exceeds this time, the deployment will be canceled and the error will be shown on the Deployment's Build logs. If you run into this limit, review this [guide](https://vercel.com/kb/guide/how-do-i-reduce-my-build-time-with-next-js-on-vercel) that explains how to reduce the Build time with a Next.js Project.
###  [Caching](https://vercel.com/docs/deployment-checks#caching)[](https://vercel.com/docs/deployment-checks#caching)
The maximum size of the Build's cache is 1 GB. It is retained for one month and it applies at the level of each [Build cache key](https://vercel.com/docs/deployment-checks#caching-process).
It is not possible to manually configure which files are cached at this time.
