##  [installCommand](https://vercel.com/docs/project-configuration/vercel-ts#installcommand)[](https://vercel.com/docs/project-configuration/vercel-ts#installcommand)
This value overrides the [Install Command](https://vercel.com/docs/deployments/configure-a-build#install-command) in Project Settings.
Type: `string | null`
The `installCommand` property can be used to override the Install Command in the Project Settings dashboard for a given deployment. This setting is useful for trying out a new package manager for the project. An empty string value will cause the Install Command to be skipped. For more information on the default behavior of the install command visit the [Configure a Build - Install Command](https://vercel.com/docs/deployments/configure-a-build#install-command) section.
vercel.ts
```
import type { VercelConfig } from '@vercel/config/v1';

export const config: VercelConfig = {
  installCommand: 'npm install',
};
```
