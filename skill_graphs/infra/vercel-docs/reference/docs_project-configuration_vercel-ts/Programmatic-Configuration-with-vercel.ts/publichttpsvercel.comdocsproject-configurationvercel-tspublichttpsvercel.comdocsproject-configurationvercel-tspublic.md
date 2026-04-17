##  [public](https://vercel.com/docs/project-configuration/vercel-ts#public)[](https://vercel.com/docs/project-configuration/vercel-ts#public)
Type: `Boolean`.
Default Value: `false`.
When set to `true`, both the [source view](https://vercel.com/docs/deployments/build-features#source-view) and [logs view](https://vercel.com/docs/deployments/build-features#logs-view) will be publicly accessible.
vercel.ts
```
import type { VercelConfig } from '@vercel/config/v1';

export const config: VercelConfig = {
  public: true,
};
```
