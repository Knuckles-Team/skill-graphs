##  [Limitations](https://vercel.com/docs/deployment-retention#limitations)[](https://vercel.com/docs/deployment-retention#limitations)
Building a Next.js application that is using [Skew Protection](https://vercel.com/docs/skew-protection) always results in a Turborepo cache miss. This occurs because Skew Protection for Next.js uses an environment variable that changes with each deployment, resulting in Turborepo cache misses. There can still be cache hits for the Vercel CDN Cache.
If you are using a version of Turborepo below 2.4.1, you may encounter issues with Skew Protection related to missing assets in production. We strongly recommend upgrading to Turborepo 2.4.1+ to restore desired behavior.
* * *
[ Previous Deployment Checks ](https://vercel.com/docs/deployment-checks)[ Next Deployments ](https://vercel.com/docs/deployments)
Was this helpful?
Send
On this page
  * [Deploy Turborepo to Vercel](https://vercel.com/docs/deployment-retention#deploy-turborepo-to-vercel)
  * [Handling environment variables](https://vercel.com/docs/deployment-retention#handling-environment-variables)
  * [Import your Turborepo to Vercel](https://vercel.com/docs/deployment-retention#import-your-turborepo-to-vercel)
  * [Using global turbo](https://vercel.com/docs/deployment-retention#using-global-turbo)
  * [Ignoring unchanged builds](https://vercel.com/docs/deployment-retention#ignoring-unchanged-builds)
  * [Setup Remote Caching for Turborepo on Vercel](https://vercel.com/docs/deployment-retention#setup-remote-caching-for-turborepo-on-vercel)
  * [Link your project to the Vercel Remote Cache](https://vercel.com/docs/deployment-retention#link-your-project-to-the-vercel-remote-cache)
  * [Test the caching](https://vercel.com/docs/deployment-retention#test-the-caching)
  * [Troubleshooting](https://vercel.com/docs/deployment-retention#troubleshooting)
  * [Build outputs cannot be found on cache hit](https://vercel.com/docs/deployment-retention#build-outputs-cannot-be-found-on-cache-hit)
  * [Unexpected cache misses](https://vercel.com/docs/deployment-retention#unexpected-cache-misses)
  * [Limitations](https://vercel.com/docs/deployment-retention#limitations)


Copy as MarkdownGive feedbackAsk AI about this page
