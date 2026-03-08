# deploymentId
Last updated February 27, 2026
The `deploymentId` option allows you to set an identifier for your deployment. This identifier is used for [version skew](https://nextjs.org/docs/app/guides/self-hosting#version-skew) protection and cache busting during rolling deployments.
next.config.js
```
module.exports = {
  deploymentId: 'my-deployment-id',
}
```

You can also set the deployment ID using the `NEXT_DEPLOYMENT_ID` environment variable:
```
NEXT_DEPLOYMENT_ID=my-deployment-id next build
```

> **Good to know:** If both are set, the `deploymentId` value in `next.config.js` takes precedence over the `NEXT_DEPLOYMENT_ID` environment variable.
