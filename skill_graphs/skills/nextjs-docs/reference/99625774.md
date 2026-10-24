## Use cases[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/deploymentId#use-cases)
### Rolling deployments[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/deploymentId#rolling-deployments)
During a rolling deployment, some server instances may be running the new version while others are still running the old version. Without a deployment ID, users might receive a mix of old and new assets, causing errors.
Setting a consistent `deploymentId` per deployment ensures:
  * Clients always request assets from a matching deployment version
  * Mismatches trigger a full reload to fetch the correct assets


### Multi-server environments[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/deploymentId#multi-server-environments)
When running multiple instances of your Next.js application behind a load balancer, all instances for the same deployment should use the same `deploymentId`.
next.config.js
```
module.exports = {
  deploymentId: process.env.DEPLOYMENT_VERSION || process.env.GIT_SHA,
}
```
