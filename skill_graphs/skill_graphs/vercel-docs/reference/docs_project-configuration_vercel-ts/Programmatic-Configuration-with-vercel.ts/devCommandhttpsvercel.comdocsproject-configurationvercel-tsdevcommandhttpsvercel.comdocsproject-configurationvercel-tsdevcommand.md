##  [devCommand](https://vercel.com/docs/project-configuration/vercel-ts#devcommand)[](https://vercel.com/docs/project-configuration/vercel-ts#devcommand)
This value overrides the [Development Command](https://vercel.com/docs/deployments/configure-a-build#development-command) in Project Settings.
Type: `string | null`
The `devCommand` property can be used to override the Development Command in the Project Settings dashboard. For more information on the default behavior of the Development Command, visit the [Configure a Build - Development Command](https://vercel.com/docs/deployments/configure-a-build#development-command) section.
vercel.ts
```
import type { VercelConfig } from '@vercel/config/v1';

export const config: VercelConfig = {
  devCommand: 'next dev',
};
```
