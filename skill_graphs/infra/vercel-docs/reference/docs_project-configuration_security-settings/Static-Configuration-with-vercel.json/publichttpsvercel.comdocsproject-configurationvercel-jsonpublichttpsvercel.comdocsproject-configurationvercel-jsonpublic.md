##  [public](https://vercel.com/docs/project-configuration/vercel-json#public)[](https://vercel.com/docs/project-configuration/vercel-json#public)
Type: `Boolean`.
Default Value: `false`.
When set to `true`, both the [source view](https://vercel.com/docs/deployments/build-features#source-view) and [logs view](https://vercel.com/docs/deployments/build-features#logs-view) will be publicly accessible.
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "public": true
}
```
