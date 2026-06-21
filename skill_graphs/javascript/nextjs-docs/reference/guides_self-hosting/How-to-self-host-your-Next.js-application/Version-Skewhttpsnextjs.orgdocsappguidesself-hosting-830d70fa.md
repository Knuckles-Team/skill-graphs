## Version Skew[](https://nextjs.org/docs/app/guides/self-hosting#version-skew)
When self-hosting across multiple instances or doing rolling deployments, [version skew](https://nextjs.org/docs/app/glossary#version-skew) can cause:
  * **Missing assets** : The client requests JavaScript or CSS files that no longer exist on the server
  * **Server Function mismatches** : The client invokes a Server Function using an ID from a previous build that the server no longer recognizes
  * **Navigation failures** : Prefetched page data from an old deployment is incompatible with the new server


Next.js uses the [`deploymentId`](https://nextjs.org/docs/app/api-reference/config/next-config-js/deploymentId) to detect and handle version skew. When a deployment ID is configured:
  * Static assets include a `?dpl=<deploymentId>` query parameter
  * Client-side navigation requests include an `x-deployment-id` header
  * The server compares the client's deployment ID with its own


If a mismatch is detected, Next.js triggers a hard navigation (full page reload) instead of a client-side navigation. This ensures the client fetches assets from a consistent deployment version.
next.config.js
```
module.exports = {
  deploymentId: process.env.DEPLOYMENT_VERSION,
}
```

> **Good to know:** When the application is reloaded, there may be a loss of application state if it's not designed to persist between page navigations. URL state or local storage would persist, but component state like `useState` would be lost.
