##  [Build Cache](https://vercel.com/docs/deploy-hooks#build-cache)[](https://vercel.com/docs/deploy-hooks#build-cache)
Builds triggered by a Deploy Hook are automatically provided with an appropriate [Build Cache](https://vercel.com/docs/deployments/troubleshoot-a-build#what-is-cached) by default, if it exists.
Caching helps speed up the [Build Step](https://vercel.com/docs/deployments/configure-a-build), so we encourage you to keep the default behavior. However, if you explicitly want to opt out of using a Build Cache, you can disable it by appending `?buildCache=false` to the Deploy Hook URL.
Here is an example request that explicitly disables the Build Cache:
example-request
```
curl -X POST https://api.vercel.com/v1/integrations/deploy/prj_98g22o5YUFVHlKOzj9vKPTyN2SDG/tKybBxqhQs?buildCache=false
```

Deploy Hooks created before May 11th, 2021 do not have the Build Cache enabled by default. To change it, you can either explicitly append `?buildCache=true` to the Deploy Hook URL, or replace your existing Deploy Hook with a newly created one.
