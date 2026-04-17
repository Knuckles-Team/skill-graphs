##  [fluid](https://vercel.com/docs/project-configuration/vercel-ts#fluid)[](https://vercel.com/docs/project-configuration/vercel-ts#fluid)
This value allows you to enable [Fluid compute](https://vercel.com/docs/fluid-compute) programmatically.
Type: `boolean | null`
The `fluid` property allows you to test Fluid compute on a per-deployment or per [custom environment](https://vercel.com/docs/deployments/environments#custom-environments) basis when using branch tracking, without needing to enable Fluid in production.
As of April 23, 2025, Fluid compute is enabled by default for new projects.
vercel.ts
```
import type { VercelConfig } from '@vercel/config/v1';

export const config: VercelConfig = {
  fluid: true,
};
```
